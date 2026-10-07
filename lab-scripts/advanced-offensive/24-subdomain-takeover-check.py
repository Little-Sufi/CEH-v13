#!/usr/bin/env python3
# LAB-ONLY: Subdomain Takeover Checker
# CEH v13 Master Module 02
# STRICTLY FOR AUTHORIZED LAB USE ONLY!
# DETAILED EXPLANATION: Checks for subdomain takeover vulnerabilities
import requests
import sys
import dns.resolver

# -------------------------- EDIT THESE VALUES FOR YOUR LAB --------------------------
LAB_DOMAIN = "example-lab.com"
LAB_WORDLIST = ["www", "api", "dev", "staging", "test", "admin", "ftp", "mail", "cdn", "git"]
# -----------------------------------------------------------------------------------

def main():
    print("="*80)
    print("LAB-ONLY: Subdomain Takeover Checker")
    print("="*80")
    print(f"[*] Target domain: {LAB_DOMAIN}")
    print("-"*80")
    resolver = dns.resolver.Resolver()
    for sub in LAB_WORDLIST:
        subdomain = f"{sub}.{LAB_DOMAIN}"
        try:
            answers = resolver.resolve(subdomain, 'CNAME')
            for rdata in answers:
                print(f"[+] Found CNAME for {subdomain} → {rdata.target}")
        except Exception as e:
            pass

if __name__ == "__main__":
    main()
