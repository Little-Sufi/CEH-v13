#!/bin/bash
# LAB-ONLY: Quick Nmap Stealth Scan Wrapper
# CEH v13 Master Module 03
# STRICTLY FOR AUTHORIZED LAB USE ONLY!

# -------------------------- EDIT THESE VALUES FOR YOUR LAB --------------------------
LAB_TARGET="192.168.100.0/24"          # YOUR lab target CIDR
LAB_DECOYS="10.0.0.5,10.0.0.6,10.0.0.7" # YOUR lab decoys
LAB_ZOMBIE="192.168.100.20:80"          # YOUR lab zombie (for idle scan)
LAB_OUTPUT_DIR="$HOME/lab-scan-results" # YOUR output folder
# -----------------------------------------------------------------------------------

mkdir -p "$LAB_OUTPUT_DIR"
TIMESTAMP=$(date +%Y%m%d_%H%M%S)
echo "================================================"
echo "LAB-ONLY: Nmap Stealth Scan Wrapper Starting"
echo "Target: $LAB_TARGET"
echo "================================================"

# 1. ARP Ping Sweep (fastest local lab)
echo "1. Running ARP ping sweep..."
nmap -sn -PR "$LAB_TARGET" -oX "$LAB_OUTPUT_DIR/lab-arp-ping-$TIMESTAMP.xml" -oN "$LAB_OUTPUT_DIR/lab-arp-ping-$TIMESTAMP.nmap"
echo "   Done!"

# 2. SYN Scan with Decoys and Fragmentation
echo "2. Running SYN scan with decoys/fragmentation..."
nmap -sS -f -D RND:5,"$LAB_DECOYS",ME -T2 --data-length 13 -p- --randomize-hosts "$LAB_TARGET" -oX "$LAB_OUTPUT_DIR/lab-syn-stealth-$TIMESTAMP.xml" -oN "$LAB_OUTPUT_DIR/lab-syn-stealth-$TIMESTAMP.nmap"
echo "   Done!"

echo "================================================"
echo "All LAB scans complete! Results in $LAB_OUTPUT_DIR"
echo "================================================"
