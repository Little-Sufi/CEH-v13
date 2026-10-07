#!/usr/bin/env python3
# LAB-ONLY: Basic Active Directory Enumeration (SMB/LDAP)
# CEH v13 Master Module 04, 05
# STRICTLY FOR AUTHORIZED LAB USE ONLY!
import sys
import subprocess

# -------------------------- EDIT THESE VALUES FOR YOUR LAB --------------------------
LAB_DOMAIN_CONTROLLER = "192.168.100.10"  # YOUR lab DC IP
LAB_DOMAIN_NAME = "LAB.LOCAL"              # YOUR lab domain name
LAB_USERNAME = ""                          # Optional: lab user (if needed)
LAB_PASSWORD = ""                          # Optional: lab pass
# -----------------------------------------------------------------------------------

def run_enum4linux():
    print("Running enum4linux-ng (lab-only)...")
    cmd = ["enum4linux-ng", LAB_DOMAIN_CONTROLLER, "-A"]
    if LAB_USERNAME and LAB_PASSWORD:
        cmd.extend(["-u", LAB_USERNAME, "-p", LAB_PASSWORD])
    try:
        result = subprocess.run(cmd, capture_output=True, text=True)
        print(result.stdout)
        if result.stderr:
            print("STDERR:", result.stderr)
    except FileNotFoundError:
        print("ERROR: enum4linux-ng not found! Install it first!")

def run_smbclient():
    print("\nTesting SMB null session (lab-only)...")
    cmd = ["smbclient", "-L", f"//{LAB_DOMAIN_CONTROLLER}", "-N"]
    try:
        result = subprocess.run(cmd, capture_output=True, text=True)
        print(result.stdout)
    except Exception as e:
        print(f"Error: {e}")

def main():
    print("="*80)
    print("LAB-ONLY: Active Directory Enumeration Helper")
    print("="*80)
    print(f"Target DC: {LAB_DOMAIN_CONTROLLER}")
    print("-"*80)
    run_enum4linux()
    run_smbclient()

if __name__ == "__main__":
    if not (LAB_DOMAIN_CONTROLLER.startswith(("10.", "172.16.", "172.17.", "172.18.", "172.19.", "172.20.", "172.21.", "172.22.", "172.23.", "172.24.", "172.25.", "172.26.", "172.27.", "172.28.", "172.29.", "172.30.", "172.31.", "192.168."))):
        print("ERROR: LAB-ONLY! Use private lab IP!")
        sys.exit(1)
    main()
