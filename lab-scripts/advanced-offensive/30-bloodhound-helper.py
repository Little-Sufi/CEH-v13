#!/usr/bin/env python3
# LAB-ONLY: BloodHound Helper
# CEH v13 Master Module 06
# STRICTLY FOR AUTHORIZED LAB USE ONLY!
# DETAILED EXPLANATION: Generates BloodHound commands and Neo4j queries!
import sys

# -------------------------- EDIT THESE VALUES FOR YOUR LAB --------------------------
LAB_DOMAIN = "lab-domain.local"
LAB_DOMAIN_CONTROLLER = "192.168.100.10"
# -----------------------------------------------------------------------------------

def main():
    print("="*80)
    print("LAB-ONLY: BloodHound Helper")
    print("="*80")
    print("-"*80")
    print("[*] Commands:")
    print("-"*80")
    print("# Collect data:")
    print(f"   bloodhound-python -c All -d {LAB_DOMAIN} -u user -p labpass123 -ns {LAB_DOMAIN_CONTROLLER}")
    print("# Neo4j queries (paste into BloodHound):")
    print("   MATCH p=shortestPath((u:User)-[*1..]->(g:Group {name:'Domain Admins@LAB-DOMAIN.LOCAL'}) RETURN p")
    print("   MATCH (c:Computer) RETURN c")
    print("-"*80")

if __name__ == "__main__":
    main()
