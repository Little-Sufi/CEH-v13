# 04. Countermeasures — Hacking Wireless Networks

> [!SHIELD] 🏰 **Defensive Hardening Standards & Secure Configurations**
> Direct technical extraction from official CEH v13 Syllabus (Module 16). Covers WPA3 Implementation, WPA2-Enterprise (802.1X/EAP-TLS), Wireless Intrusion Prevention Systems (WIPS), WPS Disabling, and AP Hardening.

---

## 🛡️ 1. Wireless Hardening Checklist

### 1.1 Technical Defensive Standards

1. **Mandatory Adoption of WPA3 / WPA2-Enterprise**: Migrate away from WEP and WPA/WPA2-Personal. Implement **WPA2-Enterprise** with **802.1X EAP-TLS** authentication backed by a RADIUS server and internal PKI certificates.
2. **Disable Wi-Fi Protected Setup (WPS)**: Completely turn off WPS on all wireless access points to mitigate Reaver/Bully PIN brute-force attacks.
3. **Deploy Wireless Intrusion Prevention Systems (WIPS)**: Continuously monitor radio frequencies for rogue APs, spoofed deauthentication floods, and MAC spoofing.
4. **Disable SSID Broadcast & Implement Client Isolation**: Hide network SSIDs (though insufficient alone) and enable **Client Isolation** on guest networks to block peer-to-peer lateral movement.

> [!SHIELD] 🏰 **📋 Comprehensive Wireless Security Hardening Reference Matrix**

| Vulnerability Vector | Insecure Legacy Configuration | Mandatory Hardening Countermeasure |
| :--- | :--- | :--- |
| **WPA2 Handshake Cracking** | WPA2 PSK (Short / Dictionary Password) | WPA3 SAE or WPA2-Enterprise (802.1X EAP-TLS) |
| **WPS PIN Exploitation** | Enabled WPS Feature | Disable WPS completely on Access Point |
| **Rogue Access Points** | Unmonitored Ethernet Ports | Port Security (802.1X) + WIPS Detection |
| **Deauthentication Attacks** | 802.11 Unprotected Management Frames | Enable 802.11w Protected Management Frames (PMF) |
