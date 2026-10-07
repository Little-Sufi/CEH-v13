# 01. Overview and Concepts — Hacking Wireless Networks

> [!INFO] 📌 **Module Scope & Core Objectives**
> Direct technical extraction from official CEH v13 Syllabus (Module 16). Covers Wireless IEEE 802.11 Standards, Frequency Bands (2.4GHz, 5GHz, 6GHz), Encryption Protocols (WEP, WPA, WPA2, WPA3), Wi-Fi Attack Taxonomies (Rogue AP, Evil Twin, Deauthentication, Krack, Dragonblood), Bluetooth Security, and Wireless Hardening Standards.

---

## 🧠 1. Wireless IEEE 802.11 Standards & Encryption Architecture

### 1.1 IEEE 802.11 Standards Matrix
Wireless communications operate across specified radio frequency spectra and modulation schemes governed by IEEE 802.11 specifications.

- **IEEE 802.11a**: 5 GHz frequency band, maximum data rate 54 Mbps, OFDM modulation.
- **IEEE 802.11b**: 2.4 GHz frequency band, maximum data rate 11 Mbps, DSSS modulation.
- **IEEE 802.11g**: 2.4 GHz frequency band, maximum data rate 54 Mbps, OFDM/DSSS modulation.
- **IEEE 802.11n (Wi-Fi 4)**: Dual-band (2.4 GHz / 5 GHz), up to 600 Mbps, uses MIMO (Multiple Input Multiple Output).
- **IEEE 802.11ac (Wi-Fi 5)**: 5 GHz frequency band, multi-gigabit throughput, MU-MIMO support.
- **IEEE 802.11ax (Wi-Fi 6 / 6E)**: 2.4 GHz / 5 GHz / 6 GHz frequency bands, OFDMA modulation, high-density performance.

> [!ABSTRACT] 🏛️ **📋 Comprehensive Wireless Encryption Protocol Reference Matrix**

| Wireless Encryption Standard | Cipher Algorithm | Key Management / Handshake | Integrity Verification | Vulnerability / Flaw |
| :--- | :--- | :--- | :--- | :--- |
| **WEP** | RC4 Stream Cipher | Static 24-bit Initialization Vector (IV) | CRC32 (ICV) | IV collision / Chopchop attack |
| **WPA (TKIP)** | RC4 Stream Cipher | Temporal Key Integrity Protocol (TKIP) | Michael (MIC) | Beck-Tews / Michael attack |
| **WPA2 (Personal)**| AES / CCMP | 4-Way Handshake (PSK) | CBC-MAC | Offline WPA2 dictionary attack |
| **WPA2 (Enterprise)**| AES / CCMP | EAP-TLS / RADIUS Server Authentication | CBC-MAC | Rogue RADIUS / Misconfigured EAP |
| **WPA3** | AES / GCMP-256 | Simultaneous Authentication of Equals (SAE)| GMAC | Dragonblood side-channel attack |

---

## ⚡ 2. Wi-Fi Attack Vector Taxonomies

### 2.1 Wireless Attack Vectors
1. **Rogue Access Point**: Unauthorized Wi-Fi AP connected to an enterprise network switch port, bypassing network perimeter security.
2. **Evil Twin Attack**: Rogue AP configured with identical SSID, MAC address (BSSID), and channel as a legitimate AP, luring clients into connecting to intercept traffic.
3. **Deauthentication Attack**: Transmits spoofed 802.11 management frames (Deauth/Disassoc) to force victim clients off APs and capture the 4-way handshake upon reconnection.
4. **WPS Pin Crack (Reaver / Bully)**: Exploits the 8-digit PIN verification mechanism of Wi-Fi Protected Setup (WPS), cracking it in under $10^4$ attempts.
5. **KRACK (Key Reinstallation Attack)**: Exploits flaws in WPA2 4-Way Handshake, forcing nonce reuse to decrypt client traffic.

> [!IMPORTANT] 🔄 **📋 Comprehensive Wireless Attack Execution Comparison Matrix**

| Attack Type | Target Component | Attack Payload / Frame | Primary Security Impact |
| :--- | :--- | :--- | :--- |
| **Deauthentication** | 802.11 Management Frame | `aireplay-ng --deauth 10 -a BSSID -c Client` | Forces disconnect & 4-way capture |
| **Evil Twin** | Client Auto-Connect | Hostapd / Airgeddon captive portal | Steals WPA2 PSK / Credentials |
| **WPS Brute Force** | WPS PIN Protocol | `reaver -i wlan0mon -b BSSID -vv` | Recovers WPA2 PSK in hours |
| **WPA3 Dragonblood** | SAE Handshake | Side-channel timing / cache attacks | Recovers WPA3 SAE password |
