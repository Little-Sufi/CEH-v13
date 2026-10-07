#!/usr/bin/env python3
# LAB-ONLY: SNMP Enumeration Helper
# CEH v13 Master Module 04
# STRICTLY FOR AUTHORIZED LAB USE ONLY!
# DETAILED EXPLANATION: Generates snmpwalk, snmp-check, etc., commands
import sys

# -------------------------- EDIT THESE VALUES FOR YOUR LAB --------------------------
LAB_TARGET_IP = "192.168.100.10"
LAB_COMMUNITY_STRING = "public"
# -----------------------------------------------------------------------------------

def main():
    print("="*80)
    print("LAB-ONLY: SNMP Enumeration Helper")
    print("="*80)
    print("# 1. snmpwalk full enumeration:")
    print(f"snmpwalk -c {LAB_COMMUNITY_STRING} -v 2c {LAB_TARGET_IP}")
    print()
    print("# 2. snmp-check:")
    print(f"snmp-check {LAB_TARGET_IP} -c {LAB_COMMUNITY_STRING}")

if __name__ == "__main__":
    main()
