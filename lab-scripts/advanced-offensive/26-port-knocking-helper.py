#!/usr/bin/env python3
# LAB-ONLY: Port Knocking Helper
# CEH v13 Master Module 03
# STRICTLY FOR AUTHORIZED LAB USE ONLY!
# DETAILED EXPLANATION: Sends port knocking sequences to open hidden ports!
import socket
import sys
import time

# -------------------------- EDIT THESE VALUES FOR YOUR LAB --------------------------
LAB_TARGET_IP = "192.168.100.10"
LAB_KNOCK_SEQUENCE = [1000, 2000, 3000]
LAB_DELAY = 0.2  # Seconds between knocks
# -----------------------------------------------------------------------------------

def knock_port(ip, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(0.5)
    try:
        sock.connect((ip, port))
    except:
        pass
    finally:
        sock.close()

def main():
    print("="*80)
    print("LAB-ONLY: Port Knocking Helper")
    print("="*80)
    print(f"[*] Target: {LAB_TARGET_IP}")
    print(f"[*] Knock sequence: {LAB_KNOCK_SEQUENCE}")
    print("-"*80")
    for port in LAB_KNOCK_SEQUENCE:
        print(f"[*] Knocking on port {port}...")
        knock_port(LAB_TARGET_IP, port)
        time.sleep(LAB_DELAY)
    print("[+] Knocking sequence complete! Now try connecting to the hidden port!")

if __name__ == "__main__":
    if not any(prefix in LAB_TARGET_IP for prefix in ["10.", "172.16.", "172.17.", "172.18.", "172.19.", "172.20.", "172.21.", "172.22.", "172.23.", "172.24.", "172.25.", "172.26.", "172.27.", "172.28.", "172.29.", "172.30.", "172.31.", "192.168.", "localhost", "127.0.0.1"]):
        print("ERROR: LAB-ONLY! Use only private lab targets!")
        sys.exit(1)
    main()
