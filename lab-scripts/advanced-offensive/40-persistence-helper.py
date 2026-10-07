#!/usr/bin/env python3
# LAB-ONLY: Persistence Helper (LAB ONLY!)
# CEH v13 Master Module 06
# STRICTLY FOR AUTHORIZED LAB USE ONLY!
# DETAILED EXPLANATION: Generates persistence methods for Linux/Windows
import sys

def main():
    print("="*80)
    print("LAB-ONLY: Persistence Helper")
    print("="*80)
    print("-"*80")
    print("[*] Linux persistence methods:")
    print("  1. Add to ~/.bashrc")
    print("  2. Add to /etc/crontab")
    print("  3. Add to /etc/rc.local")
    print("  4. Create systemd service")
    print("-"*80")
    print("[*] Windows persistence methods:")
    print("  1. Add to HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Run")
    print("  2. Add to HKLM\\Software\\Microsoft\\Windows\\CurrentVersion\\Run")
    print("  3. Scheduled Tasks")
    print("  4. Startup folder")
    print("-"*80")

if __name__ == "__main__":
    main()
