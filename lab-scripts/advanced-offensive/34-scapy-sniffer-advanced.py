#!/usr/bin/env python3
# LAB-ONLY: Advanced Packet Sniffer with Scapy
# CEH v13 Master Module 08
# STRICTLY FOR AUTHORIZED LAB USE ONLY!
# DETAILED EXPLANATION: Captures packets and extracts interesting info!
from scapy.all import sniff, IP, TCP, UDP, HTTP
import sys

# -------------------------- EDIT THESE VALUES FOR YOUR LAB --------------------------
LAB_INTERFACE = "eth0"
LAB_COUNT = 100
LAB_FILTER = "tcp port 80 or tcp port 443"
# -----------------------------------------------------------------------------------

def packet_callback(packet):
    if IP in packet:
        src_ip = packet[IP].src
        dst_ip = packet[IP].dst
        print(f"[+] {src_ip} -> {dst_ip}")
        if TCP in packet:
            print(f"    TCP: {packet[TCP].sport} -> {packet[TCP].dport}")
        if UDP in packet:
            print(f"    UDP: {packet[UDP].sport} -> {packet[UDP].dport}")
        if packet.haslayer(HTTP):
            print(f"    HTTP: {packet[HTTP].Method} {packet[HTTP].Path}")

def main():
    print("="*80)
    print("LAB-ONLY: Advanced Packet Sniffer")
    print("="*80)
    print(f"[*] Sniffing on {LAB_INTERFACE} (LAB ONLY!)...")
    print("-"*80")
    sniff(iface=LAB_INTERFACE, filter=LAB_FILTER, prn=packet_callback, count=LAB_COUNT)

if __name__ == "__main__":
    main()
