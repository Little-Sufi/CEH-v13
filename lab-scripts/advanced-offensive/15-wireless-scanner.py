#!/usr/bin/env python3
# LAB-ONLY: Wireless Network Scanner (Scapy)
# CEH v13 Master Module 16
# STRICTLY FOR AUTHORIZED LAB USE ONLY!
from scapy.all import sniff, Dot11, Dot11Beacon, Dot11Elt
import sys, time

# -------------------------- EDIT THESE VALUES FOR YOUR LAB --------------------------
LAB_WIRELESS_INTERFACE = "wlan0mon"  # YOUR lab monitor interface (must be in monitor mode!)
LAB_SCAN_TIME = 30  # Scan for N seconds
# -----------------------------------------------------------------------------------

networks = {}

def packet_callback(packet):
    if packet.haslayer(Dot11Beacon):
        bssid = packet[Dot11].addr2
        ssid = packet[Dot11Elt].info.decode()
        stats = packet[Dot11Beacon].network_stats()
        channel = stats.get("channel")
        crypto = stats.get("crypto")
        if bssid not in networks:
            networks[bssid] = {"ssid": ssid, "channel": channel, "crypto": crypto}
            print(f"[+] Found: BSSID={bssid} SSID='{ssid}' Ch={channel} Crypto={crypto}")

def main():
    print("="*80)
    print("LAB-ONLY: Wireless Network Scanner")
    print(f"Interface: {LAB_WIRELESS_INTERFACE}, Scan Time: {LAB_SCAN_TIME}s")
    print("="*80)
    print("Starting scan...")
    try:
        sniff(iface=LAB_WIRELESS_INTERFACE, prn=packet_callback, timeout=LAB_SCAN_TIME)
    except Exception as e:
        print(f"Error: {e}")
        print("Make sure interface is in monitor mode!")
        print("(Use airmon-ng start wlan0 to create wlan0mon)")

if __name__ == "__main__":
    main()
