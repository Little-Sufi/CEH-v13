#!/usr/bin/env python3
# LAB-ONLY: CrackMapExec Helper
# CEH v13 Master Module 06
# STRICTLY FOR AUTHORIZED LAB USE ONLY!
# DETAILED EXPLANATION: Generates CrackMapExec commands for SMB enumeration, spraying, etc.
import sys

# -------------------------- EDIT THESE VALUES FOR YOUR LAB --------------------------
LAB_TARGET = "192.168.100.0/24"
LAB_USERNAME = "labuser"
LAB_PASSWORD = "labpass123!"
LAB_DOMAIN = "LAB-DOMAIN"
# -----------------------------------------------------------------------------------

def main():
    print("="*80)
    print("LAB-ONLY: CrackMapExec (CME) Helper")
    print("="*80)
    print("# 1. Enumerate hosts:")
    print(f"crackmapexec smb {LAB_TARGET}")
    print()
    print("# 2. Enumerate users:")
    print(f"crackmapexec smb {LAB_TARGET} -u {LAB_USERNAME} -p '{LAB_PASSWORD}' --users")
    print()
    print("# 3. Password spray:")
    print(f"crackmapexec smb {LAB_TARGET} -u users.txt -p passwords.txt --continue-on-success")

if __name__ == "__main__":
    main()
