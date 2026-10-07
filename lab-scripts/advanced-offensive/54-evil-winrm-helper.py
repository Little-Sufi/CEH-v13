#!/usr/bin/env python3
# LAB-ONLY: Evil-WinRM Helper
# CEH v13 Master Module 06
# STRICTLY FOR AUTHORIZED LAB USE ONLY!
# DETAILED EXPLANATION: Generates Evil-WinRM commands for connecting to Windows via WinRM
import sys

# -------------------------- EDIT THESE VALUES FOR YOUR LAB --------------------------
LAB_TARGET = "192.168.100.10"
LAB_USER = "Administrator"
LAB_PASS = "labpass123!"
# -----------------------------------------------------------------------------------

def main():
    print("="*80)
    print("LAB-ONLY: Evil-WinRM Helper")
    print("="*80)
    print("# 1. Connect with password:")
    print(f"evil-winrm -i {LAB_TARGET} -u {LAB_USER} -p '{LAB_PASS}'")

if __name__ == "__main__":
    main()
