#!/usr/bin/env python3
# LAB-ONLY: SSH Pivoting Helper
# CEH v13 Master Module 07
# STRICTLY FOR AUTHORIZED LAB USE ONLY!
# DETAILED EXPLANATION: Generates SSH local/remote/dynamic port forwarding commands
import sys

# -------------------------- EDIT THESE VALUES FOR YOUR LAB --------------------------
LAB_PIVOT_HOST = "pivot.lab.local"
LAB_PIVOT_USER = "pivot_user"
LAB_LOCAL_PORT = "9050"
LAB_TARGET_INTERNAL = "10.0.0.10:3389"
# -----------------------------------------------------------------------------------

def main():
    print("="*80)
    print("LAB-ONLY: SSH Pivoting Helper")
    print("="*80)
    print("# 1. Dynamic port forward (SOCKs proxy):")
    print(f"ssh -D {LAB_LOCAL_PORT} {LAB_PIVOT_USER}@{LAB_PIVOT_HOST}")
    print()
    print("# 2. Local port forward (forward local port to internal target):")
    print(f"ssh -L 3390:{LAB_TARGET_INTERNAL} {LAB_PIVOT_USER}@{LAB_PIVOT_HOST}")
    print()

if __name__ == "__main__":
    main()
