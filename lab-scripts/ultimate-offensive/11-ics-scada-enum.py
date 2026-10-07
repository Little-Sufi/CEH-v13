#!/usr/bin/env python3
# LAB-ONLY: ICS/SCADA Enumeration (Modbus/TCP)
# CEH v13 Ultimate Offensive Script 11
# STRICTLY FOR AUTHORIZED LAB USE ONLY!
import sys
import socket

# -------------------------- EDIT THESE VALUES FOR YOUR LAB --------------------------
LAB_ICS_TARGET = "192.168.100.100"
LAB_MODBUS_PORT = 502
LAB_TIMEOUT = 3
# -----------------------------------------------------------------------------------

def modbus_enum():
    print("="*80)
    print("LAB-ONLY: ICS/SCADA Modbus/TCP Enumeration")
    print("="*80)
    print(f"[*] Target: {LAB_ICS_TARGET}:{LAB_MODBUS_PORT}")
    print("-"*80)
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(LAB_TIMEOUT)
        sock.connect((LAB_ICS_TARGET, LAB_MODBUS_PORT))
        print("[+] Connected to Modbus/TCP port!")
        # Send read holding registers request (function code 03)
        req = b'\x00\x01\x00\x00\x00\x06\x01\x03\x00\x00\x00\x01'
        sock.send(req)
        resp = sock.recv(1024)
        print(f"[+] Response: {resp.hex()}")
        sock.close()
    except Exception as e:
        print(f"[-] Error: {e}")

if __name__ == "__main__":
    if not LAB_ICS_TARGET.startswith(("10.", "172.16.", "172.17.", "172.18.", "172.19.", "172.20.", "172.21.", "172.22.", "172.23.", "172.24.", "172.25.", "172.26.", "172.27.", "172.28.", "172.29.", "172.30.", "172.31.", "192.168.")):
        print("ERROR: LAB-ONLY! Use private lab targets!")
        sys.exit(1)
    modbus_enum()
