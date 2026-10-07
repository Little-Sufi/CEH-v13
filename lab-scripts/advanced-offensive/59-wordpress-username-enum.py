#!/usr/bin/env python3
# LAB-ONLY: WordPress Username Enumeration Tester
# CEH v13 Master Module 14
# STRICTLY FOR AUTHORIZED LAB USE ONLY!
# DETAILED EXPLANATION: Enumerates WordPress users via author archive
import requests
import sys

# -------------------------- EDIT THESE VALUES FOR YOUR LAB --------------------------
LAB_TARGET_WP = "http://192.168.100.10/wordpress/"
LAB_MAX_USER_ID = 20
# -----------------------------------------------------------------------------------

def main():
    print("="*80)
    print("LAB-ONLY: WordPress Username Enumeration Tester")
    print("="*80)
    for uid in range(1, LAB_MAX_USER_ID +1):
        try:
            url = f"{LAB_TARGET_WP}?author={uid}"
            r = requests.get(url, allow_redirects=True, timeout=5)
            if r.status_code == 200:
                print(f"✅ User ID {uid} found: {r.url}")
        except Exception as e:
            pass

if __name__ == "__main__":
    if not any(p in LAB_TARGET_WP for p in ["10.", "172.16.", "192.168.", "localhost"]):
        sys.exit("ERROR: LAB-ONLY!")
    import urllib3
    urllib3.disable_warnings()
    main()
