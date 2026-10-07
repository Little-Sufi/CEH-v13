#!/usr/bin/env python3
# LAB-ONLY: Advanced Nmap Enumeration Automation
# CEH v13 Master Module 03,04
# STRICTLY FOR AUTHORIZED LAB USE ONLY!
import subprocess
import sys
import json
from datetime import datetime

# -------------------------- EDIT THESE VALUES FOR YOUR LAB --------------------------
LAB_TARGET = "192.168.100.10"          # Change to YOUR lab target IP/CIDR
LAB_NMAP_FLAGS = "-sS -sV -O -sC -T4"  # Edit scan flags as needed
LAB_OUTPUT_BASE = "lab-enum-results"   # Edit output filename base
LAB_EXCLUDED_PORTS = "9100,9101"       # Optional: Edit/remove ports to exclude
# -----------------------------------------------------------------------------------

def log_message(msg):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"[{timestamp}] [INFO] {msg}")

def run_nmap_scan(scan_type, extra_flags="", output_suffix=""):
    output_file = f"{LAB_OUTPUT_BASE}-{output_suffix}.xml"
    cmd = [
        "nmap",
        *LAB_NMAP_FLAGS.split(),
        "-oX", output_file,
        *extra_flags.split(),
        LAB_TARGET
    ]
    if LAB_EXCLUDED_PORTS:
        cmd.extend(["--exclude-ports", LAB_EXCLUDED_PORTS])
    log_message(f"Running {scan_type} scan on {LAB_TARGET}...")
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, check=True)
        log_message(f"{scan_type} scan completed successfully! Output: {output_file}")
        return output_file
    except subprocess.CalledProcessError as e:
        log_message(f"ERROR: {scan_type} scan failed: {e.stderr}")
        return None

def main():
    log_message("="*80)
    log_message("LAB-ONLY: CEH v13 Master Nmap Enumeration Automation Starting")
    log_message("="*80)
    scans = [
        ("Full TCP SYN + Version + OS", "-p-", "full-tcp"),
        ("UDP Top 100", "-sU --top-ports 100", "udp-top100"),
        ("NSE Vulnerability Scripts", "--script=vuln,auth,exploit", "nse-vuln"),
        ("Firewall Evasion Test", "-f -D RND:5 -g 53", "evasion-test")
    ]
    for scan_name, extra_flags, suffix in scans:
        run_nmap_scan(scan_name, extra_flags, suffix)
    log_message("="*80)
    log_message("All scans completed (LAB ONLY)!")
    log_message("="*80)

if __name__ == "__main__":
    # Quick validation: Check if target is private lab IP
    if not (LAB_TARGET.startswith(("10.", "172.16.", "172.17.", "172.18.", "172.19.", "172.20.", "172.21.", "172.22.", "172.23.", "172.24.", "172.25.", "172.26.", "172.27.", "172.28.", "172.29.", "172.30.", "172.31.", "192.168.")) or LAB_TARGET == "localhost" or LAB_TARGET == "127.0.0.1"):
        print("ERROR: This script is LAB-ONLY! Use only private lab IP ranges!")
        sys.exit(1)
    main()
