#!/usr/bin/env python3
# LAB-ONLY: WPScan Command Helper
# CEH v13 Master Module 14
# STRICTLY FOR AUTHORIZED LAB USE ONLY!
# DETAILED EXPLANATION: Generates WPScan commands for WordPress enumeration and vulnerability scanning
import sys

# -------------------------- EDIT THESE VALUES FOR YOUR LAB --------------------------
LAB_TARGET_WP_URL = "http://192.168.100.10/wordpress/"
# -----------------------------------------------------------------------------------

def main():
    print("="*80)
    print("LAB-ONLY: WPScan Helper")
    print("="*80)
    print("# 1. Basic scan:")
    print(f"wpscan --url {LAB_TARGET_WP_URL} --enumerate u,vp --random-agent")
    print()
    print("# 2. Enumerate users only:")
    print(f"wpscan --url {LAB_TARGET_WP_URL} --enumerate u --random-agent")
    print()

if __name__ == "__main__":
    main()
