# 🎯 Module 16: Hacking Wireless Networks - Exam Scenario Practice Engine

> [!ABSTRACT] 📊 **Interactive Module Scorecard**
>
> - **Target Module**: Module 16: Hacking Wireless Networks
> - **Total Questions**: 25 Ultra-Detailed, 100% Unique Indirect Scenarios
> - **Exam Difficulty Standard**: Senior CEH v13 (Scenario-Driven Logic & Technical Deduction)
> - **Passing Threshold**: 85% Accuracy (22/25 Correct)
> 
> *Instructions: Evaluate the scenario context below. Select your choice, then expand the **Show Correct Answer & Exam Breakdown** callout to verify your answer and review the deep technical analysis and distractor refutations.*

---

### 🧩 Question 01 | Scenario Challenge

> [!QUESTION] 📌 **Scenario Context**
> A penetration tester sets up a rogue access point broadcast with the exact same SSID, MAC address (BSSID), and radio channel as an enterprise corporate Wi-Fi network, forcing victim laptops to automatically connect to it.
>
> What attack vector was deployed?

#### 🔘 Available Options:

- **A**: Evil Twin Attack
- **B**: Bluejacking
- **C**: WPS Pin Crack
- **D**: Jamming Attack

> [!SUCCESS]- 🔑 **Show Correct Answer & Exam Breakdown**
> **Correct Answer**: **Option A**
>
> #### 💡 Technical Deep Dive:
> An Evil Twin is a rogue AP configured to impersonate a legitimate AP's SSID and BSSID to intercept traffic or capture credentials.
>
> #### 🚫 Distractor Analysis & Refutations:
>
> - **Option B is incorrect** because Bluejacking sends unauthorized messages over Bluetooth.
> - **Option C is incorrect** because WPS Pin Crack targets WPS feature authentication.
> - **Option D is incorrect** because Jamming disrupts RF signals.

---

### 🧩 Question 02 | Scenario Challenge

> [!QUESTION] 📌 **Scenario Context**
> An attacker uses `aireplay-ng --deauth 10 -a 00:11:22:33:44:55 -c AA:BB:CC:DD:EE:FF wlan0mon` to disconnect a laptop from an access point.
>
> What is the attacker's primary objective?

#### 🔘 Available Options:

- **A**: To capture the WPA/WPA2 4-Way Authentication Handshake when the client automatically reconnects
- **B**: To crash the wireless Access Point firmware
- **C**: To bypass WPA3 SAE encryption
- **D**: To format the victim's hard drive

> [!SUCCESS]- 🔑 **Show Correct Answer & Exam Breakdown**
> **Correct Answer**: **Option A**
>
> #### 💡 Technical Deep Dive:
> Deauthentication attacks force target devices off the wireless network so that the attacker can capture the 4-way EAPOL handshake upon reconnection.
>
> #### 🚫 Distractor Analysis & Refutations:
>
> - **Option B is incorrect** because deauth frames do not crash AP firmware.
> - **Option C is incorrect** because WPA3 SAE uses dragonblood mitigations and differs from 4-way PSK captures.
> - **Option D is incorrect** because wireless frames cannot format client hard drives.

---

### 🧩 Question 03 | Scenario Challenge

> [!QUESTION] 📌 **Scenario Context**
> Why is WEP (Wired Equivalent Privacy) considered completely insecure and obsolete in modern network security?

#### 🔘 Available Options:

- **A**: WEP uses a small 24-bit static Initialization Vector (IV), resulting in IV collisions that allow RC4 key recovery in minutes
- **B**: WEP requires 802.1X RADIUS authentication
- **C**: WEP uses AES-256 encryption which is too CPU intensive
- **D**: WEP does not support 2.4 GHz frequencies

> [!SUCCESS]- 🔑 **Show Correct Answer & Exam Breakdown**
> **Correct Answer**: **Option A**
>
> #### 💡 Technical Deep Dive:
> WEP relies on RC4 with a 24-bit static IV, leading to rapid key recovery after collecting sufficient encrypted packets.
>
> #### 🚫 Distractor Analysis & Refutations:
>
> - **Option B is incorrect** because WEP does not support 802.1X natively.
> - **Option C is incorrect** because WEP uses RC4, not AES.
> - **Option D is incorrect** because WEP was built for 2.4 GHz.

---

### 🧩 Question 04 | Scenario Challenge

> [!QUESTION] 📌 **Scenario Context**
> What IEEE 802.11 amendment standard introduces Protected Management Frames (PMF) to defend against spoofed Deauthentication and Disassociation attacks?

#### 🔘 Available Options:

- **A**: IEEE 802.11w
- **B**: IEEE 802.11a
- **C**: IEEE 802.11b
- **D**: IEEE 802.11g

> [!SUCCESS]- 🔑 **Show Correct Answer & Exam Breakdown**
> **Correct Answer**: **Option A**
>
> #### 💡 Technical Deep Dive:
> IEEE 802.11w protects management frames (like Deauth and Disassociation) from spoofing attacks.
>
> #### 🚫 Distractor Analysis & Refutations:
>
> - **Option B is incorrect** because 802.11a defines 5 GHz OFDM standards.
> - **Option C is incorrect** because 802.11b defines 2.4 GHz DSSS standards.
> - **Option D is incorrect** because 802.11g defines 2.4 GHz 54 Mbps standards.

---

### 🧩 Question 05 | Scenario Challenge

> [!QUESTION] 📌 **Scenario Context**
> An attacker uses `reaver -i wlan0mon -b 00:11:22:33:44:55` against an access point. What specific feature is being targeted?

#### 🔘 Available Options:

- **A**: Wi-Fi Protected Setup (WPS) 8-digit PIN verification flaw
- **B**: WPA3 SAE Handshake
- **C**: Bluetooth Low Energy pairing
- **D**: RADIUS Server EAP-TLS certificate

> [!SUCCESS]- 🔑 **Show Correct Answer & Exam Breakdown**
> **Correct Answer**: **Option A**
>
> #### 💡 Technical Deep Dive:
> Reaver brute forces the 8-digit WPS PIN by exploiting how APs validate the PIN in two separate 4-digit halves.
>
> #### 🚫 Distractor Analysis & Refutations:
>
> - **Option B is incorrect** because WPA3 SAE relies on SAE, not WPS PINs.
> - **Option C is incorrect** because Reaver does not target Bluetooth.
> - **Option D is incorrect** because Reaver targets WPS, not EAP-TLS certificates.

---

### 🧩 Question 06 | Scenario Challenge

> [!QUESTION] 📌 **Scenario Context**
> What attack vector involves an attacker stealing phone contacts, emails, and private photos from a target mobile phone over an unauthenticated Bluetooth connection?

#### 🔘 Available Options:

- **A**: Bluesnarfing
- **B**: Bluejacking
- **C**: Bluebugging
- **D**: Evil Twin

> [!SUCCESS]- 🔑 **Show Correct Answer & Exam Breakdown**
> **Correct Answer**: **Option A**
>
> #### 💡 Technical Deep Dive:
> Bluesnarfing is the unauthorized theft of data from a Bluetooth-enabled device without user knowledge.
>
> #### 🚫 Distractor Analysis & Refutations:
>
> - **Option B is incorrect** because Bluejacking sends unwanted messages without stealing data.
> - **Option C is incorrect** because Bluebugging provides full phone control.
> - **Option D is incorrect** because Evil Twin is a Wi-Fi attack.

---

### 🧩 Question 07 | Scenario Challenge

> [!QUESTION] 📌 **Scenario Context**
> An attacker sends unsolicited anonymous text messages and vCards to surrounding smartphones in a coffee shop using Bluetooth.
>
> What attack vector is this?

#### 🔘 Available Options:

- **A**: Bluejacking
- **B**: Bluesnarfing
- **C**: Bluebugging
- **D**: KRACK

> [!SUCCESS]- 🔑 **Show Correct Answer & Exam Breakdown**
> **Correct Answer**: **Option A**
>
> #### 💡 Technical Deep Dive:
> Bluejacking involves sending unsolicited short messages or contact cards over Bluetooth.
>
> #### 🚫 Distractor Analysis & Refutations:
>
> - **Option B is incorrect** because Bluesnarfing steals data.
> - **Option C is incorrect** because Bluebugging controls phone calls/SMS.
> - **Option D is incorrect** because KRACK is a WPA2 Wi-Fi flaw.

---

### 🧩 Question 08 | Scenario Challenge

> [!QUESTION] 📌 **Scenario Context**
> What enterprise wireless authentication model uses an 802.1X RADIUS server and mandates dual-side X.509 digital certificates for both server and client verification?

#### 🔘 Available Options:

- **A**: WPA2-Enterprise with EAP-TLS
- **B**: WPA2-Personal (PSK)
- **C**: WEP Open Authentication
- **D**: PEAP-MSCHAPv2

> [!SUCCESS]- 🔑 **Show Correct Answer & Exam Breakdown**
> **Correct Answer**: **Option A**
>
> #### 💡 Technical Deep Dive:
> EAP-TLS provides highest enterprise security requiring mutual authentication using X.509 certificates.
>
> #### 🚫 Distractor Analysis & Refutations:
>
> - **Option B is incorrect** because WPA2-Personal uses static pre-shared keys.
> - **Option C is incorrect** because WEP is unauthenticated stream cipher.
> - **Option D is incorrect** because PEAP-MSCHAPv2 uses passwords for client auth.

---

### 🧩 Question 09 | Scenario Challenge

> [!QUESTION] 📌 **Scenario Context**
> What key management mechanism introduced in WPA3 replaces the vulnerable WPA2 4-Way PSK Handshake to prevent offline dictionary attacks?

#### 🔘 Available Options:

- **A**: Simultaneous Authentication of Equals (SAE) / Dragonfly Handshake
- **B**: Temporal Key Integrity Protocol (TKIP)
- **C**: RC4 Stream Cipher
- **D**: Cyclic Redundancy Check (CRC32)

> [!SUCCESS]- 🔑 **Show Correct Answer & Exam Breakdown**
> **Correct Answer**: **Option A**
>
> #### 💡 Technical Deep Dive:
> WPA3 uses SAE (based on Dragonfly key exchange) to provide forward secrecy and resist offline dictionary cracking.
>
> #### 🚫 Distractor Analysis & Refutations:
>
> - **Option B is incorrect** because TKIP is legacy WPA.
> - **Option C is incorrect** because RC4 is obsolete WEP encryption.
> - **Option D is incorrect** because CRC32 is integrity checksum.

---

### 🧩 Question 10 | Scenario Challenge

> [!QUESTION] 📌 **Scenario Context**
> What command-line tool in Linux is used to toggle a wireless interface into Monitor Mode (`RFMON`) for packet capture?

#### 🔘 Available Options:

- **A**: airmon-ng start wlan0
- **B**: nmap -sV wlan0
- **C**: wireshark --monitor
- **D**: ettercap -G

> [!SUCCESS]- 🔑 **Show Correct Answer & Exam Breakdown**
> **Correct Answer**: **Option A**
>
> #### 💡 Technical Deep Dive:
> `airmon-ng start wlan0` enables monitor mode on wireless NICs.
>
> #### 🚫 Distractor Analysis & Refutations:
>
> - **Option B is incorrect** because Nmap is a network scanner.
> - **Option C is incorrect** because Wireshark is a GUI sniffer.
> - **Option D is incorrect** because Ettercap is an ARP spoofing tool.

---

### 🧩 Question 11 | Scenario Challenge

> [!QUESTION] 📌 **Scenario Context**
> What hardware sniffer platform allows security researchers to capture raw 2.4 GHz Bluetooth RF packets?

#### 🔘 Available Options:

- **A**: Ubertooth One
- **B**: Wi-Fi Pineapple
- **C**: HackRF One
- **D**: LAN Turtle

> [!SUCCESS]- 🔑 **Show Correct Answer & Exam Breakdown**
> **Correct Answer**: **Option A**
>
> #### 💡 Technical Deep Dive:
> Ubertooth One is an open-source 2.4 GHz wireless development platform suitable for Bluetooth experimentation and packet sniffing.
>
> #### 🚫 Distractor Analysis & Refutations:
>
> - **Option B is incorrect** because Wi-Fi Pineapple is a Wi-Fi auditing platform.
> - **Option C is incorrect** because HackRF is a wideband SDR.
> - **Option D is incorrect** because LAN Turtle is an inline Ethernet tap.

---

### 🧩 Question 12 | Scenario Challenge

> [!QUESTION] 📌 **Scenario Context**
> An attacker targets a WPA2-Personal network. Which file captured by `airodump-ng` contains the EAPOL handshake required for offline password cracking?

#### 🔘 Available Options:

- **A**: .cap file
- **B**: .txt file
- **C**: .csv file
- **D**: .png file

> [!SUCCESS]- 🔑 **Show Correct Answer & Exam Breakdown**
> **Correct Answer**: **Option A**
>
> #### 💡 Technical Deep Dive:
> `airodump-ng` saves raw network packets including the 4-way EAPOL handshake in `.cap` (PCAP) format.
>
> #### 🚫 Distractor Analysis & Refutations:
>
> - **Option B is incorrect** because `.txt` is plain text.
> - **Option C is incorrect** because `.csv` contains AP scan metadata.
> - **Option D is incorrect** because `.png` is an image file.

---

### 🧩 Question 13 | Scenario Challenge

> [!QUESTION] 📌 **Scenario Context**
> What vulnerability standard describes side-channel timing and cache attacks against the WPA3 SAE (Simultaneous Authentication of Equals) handshake?

#### 🔘 Available Options:

- **A**: Dragonblood Vulnerabilities
- **B**: KRACK Attack
- **C**: Bluebugging
- **D**: Chopchop Attack

> [!SUCCESS]- 🔑 **Show Correct Answer & Exam Breakdown**
> **Correct Answer**: **Option A**
>
> #### 💡 Technical Deep Dive:
> Dragonblood refers to vulnerabilities in WPA3 SAE implementation allowing password recovery via side-channel attacks.
>
> #### 🚫 Distractor Analysis & Refutations:
>
> - **Option B is incorrect** because KRACK affects WPA2.
> - **Option C is incorrect** because Bluebugging affects Bluetooth.
> - **Option D is incorrect** because Chopchop affects WEP.

---

### 🧩 Question 14 | Scenario Challenge

> [!QUESTION] 📌 **Scenario Context**
> What is an Unauthorized Access Point connected to an enterprise corporate Ethernet network without IT approval called?

#### 🔘 Available Options:

- **A**: Rogue Access Point
- **B**: Evil Twin
- **C**: Honeypot AP
- **D**: Wi-Fi Direct

> [!SUCCESS]- 🔑 **Show Correct Answer & Exam Breakdown**
> **Correct Answer**: **Option A**
>
> #### 💡 Technical Deep Dive:
> A Rogue AP is any unauthorized wireless AP connected directly to a secured LAN switch port.
>
> #### 🚫 Distractor Analysis & Refutations:
>
> - **Option B is incorrect** because Evil Twin spoofs an existing SSID wirelessly.
> - **Option C is incorrect** because Honeypot AP is set up to entrap attackers.
> - **Option D is incorrect** because Wi-Fi Direct is peer-to-peer wireless standard.

---

### 🧩 Question 15 | Scenario Challenge

> [!QUESTION] 📌 **Scenario Context**
> What tool is a passive 802.11 wireless network sniffer and Wireless Intrusion Detection System (WIDS) that operates without transmitting any packets?

#### 🔘 Available Options:

- **A**: Kismet
- **B**: Aircrack-ng
- **C**: Reaver
- **D**: Airgeddon

> [!SUCCESS]- 🔑 **Show Correct Answer & Exam Breakdown**
> **Correct Answer**: **Option A**
>
> #### 💡 Technical Deep Dive:
> Kismet is a passive 802.11 wireless network detector and packet sniffer that operates quietly without broadcasting.
>
> #### 🚫 Distractor Analysis & Refutations:
>
> - **Option B is incorrect** because Aircrack-ng can actively inject packets.
> - **Option C is incorrect** because Reaver actively brute-forces WPS PINs.
> - **Option D is incorrect** because Airgeddon executes active wireless attacks.

---

### 🧩 Question 16 | Scenario Challenge

> [!QUESTION] 📌 **Scenario Context**
> What Wi-Fi frequency band provides highest data rates and lowest interference across 6 GHz spectrum channels as introduced in Wi-Fi 6E?

#### 🔘 Available Options:

- **A**: 6 GHz Band
- **B**: 2.4 GHz Band
- **C**: 5 GHz Band
- **D**: 900 MHz Band

> [!SUCCESS]- 🔑 **Show Correct Answer & Exam Breakdown**
> **Correct Answer**: **Option A**
>
> #### 💡 Technical Deep Dive:
> Wi-Fi 6E expands Wi-Fi 6 into the 6 GHz spectrum, providing high bandwidth and low latency.
>
> #### 🚫 Distractor Analysis & Refutations:
>
> - **Option B is incorrect** because 2.4 GHz has high interference.
> - **Option C is incorrect** because 5 GHz was used in Wi-Fi 5/6.
> - **Option D is incorrect** because 900 MHz is legacy cellular spectrum.

---

### 🧩 Question 17 | Scenario Challenge

> [!QUESTION] 📌 **Scenario Context**
> What encryption cipher algorithm is used in modern WPA2-CCMP wireless security?

#### 🔘 Available Options:

- **A**: AES (Advanced Encryption Standard)
- **B**: RC4
- **C**: DES
- **D**: Blowfish

> [!SUCCESS]- 🔑 **Show Correct Answer & Exam Breakdown**
> **Correct Answer**: **Option A**
>
> #### 💡 Technical Deep Dive:
> WPA2-CCMP uses AES in Counter Mode with CBC-MAC (CCMP) for confidentiality and integrity.
>
> #### 🚫 Distractor Analysis & Refutations:
>
> - **Option B is incorrect** because RC4 was used in WEP and WPA-TKIP.
> - **Option C is incorrect** because DES is insecure 56-bit block cipher.
> - **Option D is incorrect** because Blowfish is not used in 802.11.

---

### 🧩 Question 18 | Scenario Challenge

> [!QUESTION] 📌 **Scenario Context**
> What interactive script framework automates Evil Twin, Captive Portal, and WPA/WPA2 Enterprise wireless attacks via a bash menu interface?

#### 🔘 Available Options:

- **A**: Airgeddon
- **B**: Nmap
- **C**: Wireshark
- **D**: Nikto

> [!SUCCESS]- 🔑 **Show Correct Answer & Exam Breakdown**
> **Correct Answer**: **Option A**
>
> #### 💡 Technical Deep Dive:
> Airgeddon is a multi-use bash script for auditing wireless networks.
>
> #### 🚫 Distractor Analysis & Refutations:
>
> - **Option B is incorrect** because Nmap is a port scanner.
> - **Option C is incorrect** because Wireshark is a packet analyzer.
> - **Option D is incorrect** because Nikto is a web scanner.

---

### 🧩 Question 19 | Scenario Challenge

> [!QUESTION] 📌 **Scenario Context**
> What attack vector leverages forced nonce reuse in the WPA2 4-Way Handshake to decrypt wireless packets transmitted by a client?

#### 🔘 Available Options:

- **A**: KRACK (Key Reinstallation Attack)
- **B**: Reaver
- **C**: Bluejacking
- **D**: Chopchop Attack

> [!SUCCESS]- 🔑 **Show Correct Answer & Exam Breakdown**
> **Correct Answer**: **Option A**
>
> #### 💡 Technical Deep Dive:
> KRACK targets the 4-way handshake by tricking a client into reinstalling an already-in-use key, resetting message numbers and nonces.
>
> #### 🚫 Distractor Analysis & Refutations:
>
> - **Option B is incorrect** because Reaver targets WPS PINs.
> - **Option C is incorrect** because Bluejacking targets Bluetooth.
> - **Option D is incorrect** because Chopchop targets WEP.

---

### 🧩 Question 20 | Scenario Challenge

> [!QUESTION] 📌 **Scenario Context**
> Why is hiding a wireless Access Point's SSID (disabling SSID Broadcast) INSUFFICIENT as a standalone security measure?

#### 🔘 Available Options:

- **A**: SSID names are transmitted in plaintext in Probe Request and Association Response management frames whenever clients connect
- **B**: Hidden SSIDs crash wireless drivers
- **C**: Hidden SSIDs force WEP encryption
- **D**: Hidden SSIDs disable firewalls

> [!SUCCESS]- 🔑 **Show Correct Answer & Exam Breakdown**
> **Correct Answer**: **Option A**
>
> #### 💡 Technical Deep Dive:
> Disabling SSID broadcast does not hide the network because SSIDs are broadcast in plaintext during active client probe requests and association responses.
>
> #### 🚫 Distractor Analysis & Refutations:
>
> - **Option B is incorrect** because hidden SSIDs do not crash drivers.
> - **Option C is incorrect** because SSIDs do not dictate cipher choice.
> - **Option D is incorrect** because SSIDs do not touch host firewalls.

---

### 🧩 Question 21 | Scenario Challenge

> [!QUESTION] 📌 **Scenario Context**
> What security control prevents clients connected to a Guest Wi-Fi Access Point from communicating directly with each other on the local wireless subnet?

#### 🔘 Available Options:

- **A**: Client Isolation / Wireless Station Isolation
- **B**: Port Forwarding
- **C**: Dynamic Host Configuration Protocol (DHCP)
- **D**: Network Address Translation (NAT)

> [!SUCCESS]- 🔑 **Show Correct Answer & Exam Breakdown**
> **Correct Answer**: **Option A**
>
> #### 💡 Technical Deep Dive:
> Client Isolation blocks client-to-client traffic on the same AP, preventing lateral movement.
>
> #### 🚫 Distractor Analysis & Refutations:
>
> - **Option B is incorrect** because Port Forwarding routes WAN traffic to LAN hosts.
> - **Option C is incorrect** because DHCP assigns IP addresses.
> - **Option D is incorrect** because NAT translates IP addresses across boundaries.

---

### 🧩 Question 22 | Scenario Challenge

> [!QUESTION] 📌 **Scenario Context**
> An attacker uses `wifite` on a wireless network. What is the primary capability of `wifite`?

#### 🔘 Available Options:

- **A**: Fully automated auditing of WEP, WPA, WPA2, and WPS wireless networks
- **B**: Cracking SSH password hashes
- **C**: Defeating AES-256 BitLocker encryption
- **D**: Launching BGP routing floods

> [!SUCCESS]- 🔑 **Show Correct Answer & Exam Breakdown**
> **Correct Answer**: **Option A**
>
> #### 💡 Technical Deep Dive:
> Wifite is an automated wireless attack tool designed to scan and attack WEP/WPA/WPS networks sequentially.
>
> #### 🚫 Distractor Analysis & Refutations:
>
> - **Option B is incorrect** because Wifite does not audit SSH.
> - **Option C is incorrect** because Wifite does not attack BitLocker disk encryption.
> - **Option D is incorrect** because Wifite does not deal with BGP routers.

---

### 🧩 Question 23 | Scenario Challenge

> [!QUESTION] 📌 **Scenario Context**
> What 802.11 management frame is continuously broadcast by an Access Point to announce its presence, SSID, supported data rates, and encryption capabilities?

#### 🔘 Available Options:

- **A**: Beacon Frame
- **B**: Deauthentication Frame
- **C**: Probe Request
- **D**: ACK Frame

> [!SUCCESS]- 🔑 **Show Correct Answer & Exam Breakdown**
> **Correct Answer**: **Option A**
>
> #### 💡 Technical Deep Dive:
> Beacon frames are periodically sent by APs to announce the network's existence and parameters.
>
> #### 🚫 Distractor Analysis & Refutations:
>
> - **Option B is incorrect** because Deauthentication frames disconnect clients.
> - **Option C is incorrect** because Probe Requests are sent by clients searching for APs.
> - **Option D is incorrect** because ACK is a Control frame confirming reception.

---

### 🧩 Question 24 | Scenario Challenge

> [!QUESTION] 📌 **Scenario Context**
> What wireless attack vector involves jamming or flooding radio frequencies with noise to disrupt all wireless communications within a facility?

#### 🔘 Available Options:

- **A**: Wireless Signal Jamming (DoS)
- **B**: Evil Twin
- **C**: Bluesnarfing
- **D**: KRACK

> [!SUCCESS]- 🔑 **Show Correct Answer & Exam Breakdown**
> **Correct Answer**: **Option A**
>
> #### 💡 Technical Deep Dive:
> RF Jamming floods wireless channels with noise or interference, causing a Denial of Service for all 802.11 devices.
>
> #### 🚫 Distractor Analysis & Refutations:
>
> - **Option B is incorrect** because Evil Twin intercepts data via rogue APs.
> - **Option C is incorrect** because Bluesnarfing steals Bluetooth data.
> - **Option D is incorrect** because KRACK decrypts WPA2 traffic.

---

### 🧩 Question 25 | Scenario Challenge

> [!QUESTION] 📌 **Scenario Context**
> What is the primary operational objective of implementing Wireless Intrusion Prevention Systems (WIPS) in enterprise networks?

#### 🔘 Available Options:

- **A**: To continuously monitor radio spectrum, detect unauthorized rogue access points, and suppress spoofed deauthentication attacks in real time
- **B**: To increase Wi-Fi throughput speed
- **C**: To generate SSL certificates
- **D**: To assign static IP addresses

> [!SUCCESS]- 🔑 **Show Correct Answer & Exam Breakdown**
> **Correct Answer**: **Option A**
>
> #### 💡 Technical Deep Dive:
> WIPS solutions monitor radio frequencies to identify rogue APs, unauthorized devices, and wireless attack patterns.
>
> #### 🚫 Distractor Analysis & Refutations:
>
> - **Option B is incorrect** because WIPS is a security control, not a throughput accelerator.
> - **Option C is incorrect** because PKI/CAs issue SSL certificates.
> - **Option D is incorrect** because DHCP/IPAM manages IP assignments.
