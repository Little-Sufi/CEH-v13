#!/usr/bin/env python3
# LAB-ONLY: Advanced Active Directory Enumeration Helper
# CEH v13 Master Module 04
# STRICTLY FOR AUTHORIZED LAB USE ONLY!
# DETAILED EXPLANATION: Generates commands for enum4linux-ng, bloodhound-python, etc.!
import sys

# -------------------------- EDIT THESE VALUES FOR YOUR LAB --------------------------
LAB_DOMAIN = "lab-domain.local"
LAB_DOMAIN_CONTROLLER = "192.168.100.10"
# -----------------------------------------------------------------------------------

def main():
    print("="*80)
    print("LAB-ONLY: AD Enumeration Helper")
    print("="*80")
    print("-"*80")
    print("[*] Commands to run in your lab:")
    print("-"*80")
    print("# 1. enum4linux-ng:")
    print(f"   enum4linux-ng {LAB_DOMAIN_CONTROLLER} -A")
    print("# 2. bloodhound-python:")
    print(f"   bloodhound-python -c All -d {LAB_DOMAIN} -u user -p 'labpass123 -ns {LAB_DOMAIN_CONTROLLER}")
    print("# 3. ldapsearch:")
    print(f"   ldapsearch -x -h {LAB_DOMAIN_CONTROLLER} -b \"dc=lab-domain,dc=local\"")
    print("# 4. crackmapexec:")
    print(f"   crackmapexec smb {LAB_DOMAIN_CONTROLLER} --users")
    print(f"   crackmapexec smb {LAB_DOMAIN_CONTROLLER} --shares")
    print(f"   crackmapexec smb {LAB_DOMAIN_CONTROLLER} --groups")
    print("-"*80")

if __name__ == "__main__":
    main()
