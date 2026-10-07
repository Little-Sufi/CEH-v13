#!/usr/bin/env python3
# LAB-ONLY: Socat Port Forwarding Helper
# CEH v13 Master Module 07
# STRICTLY FOR AUTHORIZED LAB USE ONLY!
# DETAILED EXPLANATION: Generates Socat commands for port forwarding, pivoting, etc.
import sys

# -------------------------- EDIT THESE VALUES FOR YOUR LAB --------------------------
LAB_LOCAL_PORT = "8080"
LAB_REMOTE_TARGET = "192.168.100.10:80"
# -----------------------------------------------------------------------------------

def main():
    print("="*80)
    print("LAB-ONLY: Socat Port Forwarding Helper")
    print("="*80)
    print("# 1. Simple TCP port forward (local port 8080 -> remote):")
    print(f"socat TCP-LISTEN:{LAB_LOCAL_PORT},fork TCP:{LAB_REMOTE_TARGET}")

if __name__ == "__main__":
    main()
