# 01. Overview and Concepts — Sniffing

> [!INFO] 📌 **Module Scope & Core Objectives**
> Direct technical extraction from official CEH v13 Syllabus (Module 08). Covers Packet Sniffing Fundamentals, Passive vs Active Sniffing Mechanics, Promiscuous Mode Network Interfaces, MAC Address Table CAM Overflows, ARP Poisoning Man-in-the-Middle (MitM) Attacks, DHCP Starvation, and DNS Spoofing.

---

## 🧠 1. Fundamental Principles of Packet Sniffing

### 1.1 Passive vs. Active Packet Sniffing
Packet Sniffing involves capturing live data frames passing across a computer network using protocol analyzers (e.g., Wireshark, TShark, Tcpdump).

#### 1. Passive Sniffing
Occurs on legacy network Hubs or unswitched collision domains where all transmitted frames are broadcast to every connected network interface card (NIC). The sniffer passively listens to raw data frames without injecting any network traffic.

#### 2. Active Sniffing
Required on modern Layer 2 Ethernet Switches. Switches maintain a Content Addressable Memory (CAM) table mapping MAC addresses to physical switch ports, isolating unicast traffic. To sniff traffic across switched networks, attackers must execute active attacks (MAC Flooding, ARP Poisoning) to force switches to flood unicast traffic to all ports or redirect frames through the attacker's machine.

#### 3. Network Interface Promiscuous Mode
Standard NIC drivers filter out ethernet frames whose destination MAC address does not match the local host MAC or broadcast MAC (`FF:FF:FF:FF:FF:FF`). Enabling **Promiscuous Mode** instructs the hardware controller to pass ALL captured ethernet frames directly to the OS protocol analyzer regardless of destination MAC.

> [!ABSTRACT] 🏛️ **📋 Comprehensive Sniffing Environment Reference Matrix**

| Environment Type | Switch Architecture | Sniffing Methodology | Hardware Requirement | Promiscuous Mode Required |
| :--- | :--- | :--- | :--- | :---: |
| **Hub-Based (Legacy)** | Broadcast Domain (Shared) | Passive Sniffing | Standard NIC | Yes |
| **Switch-Based (Modern)**| Isolated CAM Table | Active Sniffing (ARP/MAC) | Packet Injection NIC | Yes |
| **SPAN / Mirror Port** | Port Mirrored Switch | Passive Network Tap | Dual NIC / Monitor Port | Yes |

---

## ⚡ 2. Active Sniffing Vector Mechanics

### 2.1 MAC Flooding & CAM Table Exhaustion
Ethernet switches maintain CAM tables with finite memory limits (e.g., 8,000 to 16,000 MAC entries).

#### MAC Flooding Attack Mechanics:
1. **Tool Execution**: Attacker executes MAC flooding utilities (e.g., `macof`) to flood thousands of bogus, randomly generated MAC addresses per second (`macof -i eth0 -n 100000`) to the switch port.
2. **CAM Exhaustion**: The switch CAM table memory completely fills up, purging legitimate MAC entry mappings.
3. **Fail-Open Mode**: The switch degrades into a legacy "Fail-Open" broadcast hub mode, broadcasting all subsequent unicast ethernet frames to EVERY switch port, enabling passive packet sniffing.

> [!IMPORTANT] 🔄 **📋 Comprehensive Active Sniffing Technique Reference Matrix**

| Active Attack Vector | Protocol Layer | Primary Operational Mechanism | Core Tool Used |
| :--- | :---: | :--- | :--- |
| **MAC Flooding** | Layer 2 (Data Link) | Floods bogus MACs to force switch into Fail-Open hub mode | `macof` |
| **ARP Poisoning** | Layer 2 (Data Link) | Sends forged Gratuitous ARP replies mapping victim IP to attacker MAC | `arpspoof`, `ettercap` |
| **DHCP Starvation** | Layer 7 / UDP 67/68 | Exhausts DHCP IP address pool with spoofed MAC requests | `yersinia`, `dhcpxs` |
| **DNS Poisoning** | Layer 7 / UDP 53 | Injects spoofed DNS A-record responses to redirect victim domain traffic | `dnsspoof`, `ettercap` |
