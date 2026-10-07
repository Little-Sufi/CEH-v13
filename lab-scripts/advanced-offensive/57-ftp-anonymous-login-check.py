#!/usr/bin/env python3
# LAB-ONLY: FTP Anonymous Login Checker
# CEH v13 Master Module 04
# STRICTLY FOR AUTHORIZED LAB USE ONLY!
# DETAILED EXPLANATION: Checks for FTP servers that allow anonymous login
import ftplib
import sys

# -------------------------- EDIT THESE VALUES FOR YOUR LAB --------------------------
LAB_TARGET_IP = "192.168.100.10"
# -----------------------------------------------------------------------------------

def check_ftp_anonymous(ip):
    print("="*80)
    print("LAB-ONLY: FTP Anonymous Login Checker")
    print("="*80)
    try:
        ftp = ftplib.FTP(ip)
        ftp.login("anonymous", "anonymous@example.com")
        print(f"✅ SUCCESS: Anonymous login allowed on {ip}!")
        print("Files found:")
        ftp.retrlines("LIST")
        ftp.quit()
    except Exception as e:
        print(f"❌ FAILURE: {e}")

if __name__ == "__main__":
    if not any(p in LAB_TARGET_IP for p in ["10.", "172.16.", "192.168.", "localhost"]):
        sys.exit("ERROR: LAB-ONLY!")
    check_ftp_anonymous(LAB_TARGET_IP)
