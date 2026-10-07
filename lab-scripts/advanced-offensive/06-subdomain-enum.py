#!/usr/bin/env python3
# LAB-ONLY: Advanced Subdomain Enumeration (OSINT)
# CEH v13 Master Module 02
# STRICTLY FOR AUTHORIZED LAB USE ONLY!
import sys
import requests
import re

# -------------------------- EDIT THESE VALUES FOR YOUR LAB --------------------------
LAB_TARGET_DOMAIN = "lab-domain.local"  # YOUR lab domain to enumerate
LAB_WORDLIST_PATH = "/usr/share/seclists/Discovery/DNS/subdomains-top1million-5000.txt"  # Edit path as needed
LAB_NAMESERVERS = ["8.8.8.8", "1.1.1.1"]  # Optional: Use your lab DNS
LAB_CHECK_HTTP = True  # Also check if subdomain has HTTP/HTTPS server?
# -----------------------------------------------------------------------------------

def brute_subdomains(domain, wordlist):
    found = []
    print(f"Brute-forcing subdomains for {domain} from wordlist...")
    try:
        with open(wordlist, "r", encoding="utf-8", errors="ignore") as f:
            lines = f.read().splitlines()
            total = len(lines)
            for i, sub in enumerate(lines):
                if not sub or sub.startswith("#"):
                    continue
                full = f"{sub}.{domain}"
                if i % 500 == 0:
                    print(f"Progress: {i}/{total} ({(i/total)*100:.1f}%)")
                try:
                    # Quick DNS check (using requests to simulate, or use dns.resolver for better)
                    # For lab, we'll just try a HEAD request if CHECK_HTTP is true
                    if LAB_CHECK_HTTP:
                        for proto in ["http://", "https://"]:
                            try:
                                r = requests.head(f"{proto}{full}", timeout=2, verify=False)
                                found.append(f"{proto}{full}")
                                break
                            except:
                                pass
                except Exception as e:
                    pass
    except FileNotFoundError:
        print(f"ERROR: Wordlist not found at {wordlist}!")
        print("Edit LAB_WORDLIST_PATH in the script!")
        return []
    return found

def main():
    print("="*80)
    print("LAB-ONLY: Advanced Subdomain Enumeration")
    print("="*80)
    print(f"Target Domain: {LAB_TARGET_DOMAIN}")
    print("-"*80)
    results = brute_subdomains(LAB_TARGET_DOMAIN, LAB_WORDLIST_PATH)
    print("-"*80)
    if results:
        print(f"âœ… Found {len(results)} subdomains:")
        for sd in results:
            print(f"  - {sd}")
    else:
        print("No subdomains found (lab-only domain may be invalid, or wordlist is wrong)")

if __name__ == "__main__":
    import urllib3
    urllib3.disable_warnings()
    main()
