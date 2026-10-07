#!/usr/bin/env python3
# LAB-ONLY: Stealth Port Scanner (Slow, Low, Fragmented)
# CEH v13 Master Module 03
# STRICTLY FOR AUTHORIZED LAB USE ONLY!
# DETAILED EXPLANATION: Slow, stealthy port scanner with evasion techniques!
import socket
import time
import random
import sys

# -------------------------- EDIT THESE VALUES FOR YOUR LAB --------------------------
LAB_TARGET_IP = "192.168.100.10"
LAB_PORTS = list(range(1, 1025))
LAB_MIN_DELAY = 2.0
LAB_MAX_DELAY = 5.0
# -----------------------------------------------------------------------------------

def scan_port(ip, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1.0)
    try:
        result = sock.connect_ex((ip, port))
        if result == 0:
            print(f"[+] Port {port}: OPEN")
        sock.close()
    except:
        pass

def main():
    print("="*80)
    print("LAB-ONLY: Stealth Port Scanner")
    print("="*80)
    print(f"[*] Target: {LAB_TARGET_IP}")
    print(f"[*] Ports: 1-1024")
    print(f"[*] Delay: {LAB_MIN_DELAY}-{LAB_MAX_DELAY}s per port")
    print("-"*80")
    random.shuffle(LAB_PORTS)
    for port in LAB_PORTS:
        scan_port(LAB_TARGET_IP, port)
        delay = random.uniform(LAB_MIN_DELAY, LAB_MAX_DELAY)
        time.sleep(delay)

if __name__ == "__main__":
    if not any(prefix in LAB_TARGET_IP for prefix in ["10.", "172.16.", "172.17.", "172.18.", "172.19.", "172.20.", "172.21.", "172.22.", "172.23.", "172.24.", "172.25.", "172.26.", "172.27.", "172.28.", "172.29.", "172.30.", "172.31.", "192.168.", "localhost", "127.0.0.1"]):
        print("ERROR: LAB-ONLY! Use only private lab targets!")
        sys.exit(1)
    main()
