#!/usr/bin/env python3
# LAB-ONLY: Hash Identifier Helper
# CEH v13 Master Module 05
# STRICTLY FOR AUTHORIZED LAB USE ONLY!
# DETAILED EXPLANATION: Generates hash-identifier and hashcat commands for cracking
import sys

# -------------------------- EDIT THESE VALUES FOR YOUR LAB --------------------------
LAB_SAMPLE_HASH = "5d41402abc4b2a76b9719d911017c592"
# -----------------------------------------------------------------------------------

def main():
    print("="*80)
    print("LAB-ONLY: Hash Identifier Helper")
    print("="*80)
    print(f"Hash to identify: {LAB_SAMPLE_HASH}")
    print()
    print("# 1. Use hash-identifier:")
    print(f"hash-identifier {LAB_SAMPLE_HASH}")
    print()
    print("# 2. Once type is known (e.g., MD5, hashcat mode 0):")
    print("hashcat -m 0 hash.txt wordlist.txt")

if __name__ == "__main__":
    main()
