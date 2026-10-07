#!/usr/bin/env python3
# LAB-ONLY: Simple Packet Sniffer (Scapy)
# CEH v13 Master Module 08
# STRICTLY FOR AUTHORIZED LAB USE ONLY!
from scapy.all import sniff, IP, TCP, UDP
import sys

# -------------------------- EDIT THESE VALUES FOR YOUR LAB --------------------------
LAB_INTERFACE = "eth0"  # YOUR lab interface (eth0, wlan0, etc.)
LAB_PACKET_COUNT = 100  # Number of packets to capture (0 = infinite)
LAB_FILTER = ""         # Optional: BPF filter (e.g., "tcp port 80", "host 192.168.100.10")
# -----------------------------------------------------------------------------------

def packet_callback(packet):
    if IP in packet:
        src_ip = packet[IP].src
        dst_ip = packet[IP].dst
        proto = packet[IP].proto
        print(f"[+] {src_ip} -> {dst_ip} (Proto: {proto})")
        if TCP in packet:
            print(f"    TCP: {packet[TCP].sport} -> {packet[TCP].dport} Flags: {packet[TCP].flags}")
        elif UDP in packet:
            print(f"    UDP: {packet[UDP].sport} -> {packet[UDP].dport}")

def main():
    print("="*80)
    print("LAB-ONLY: Simple Scapy Packet Sniffer")
    print(f"Interface: {LAB_INTERFACE}, Count: {LAB_PACKET_COUNT}")
    print("="*80)
    print("Starting capture (press Ctrl+C to stop)...")
    try:
        sniff(iface=LAB_INTERFACE, prn=packet_callback, count=LAB_PACKET_COUNT, filter=LAB_FILTER)
    except Exception as e:
        print(f"Error: {e}")
        print("Make sure scapy is installed: pip install scapy")
        print("And run with sudo/root!")

if __name__ == "__main__":
    main()
