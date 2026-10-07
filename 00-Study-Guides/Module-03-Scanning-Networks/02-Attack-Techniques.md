# 02. Attack Techniques — Scanning Networks

> [!WARNING] ⚡ **Offensive Scanning Methodologies & Evasion Mechanics**
> Direct extraction from official CEH v13 Syllabus (Module 03). Covers Nmap Scan Types (`-sT`, `-sS`, `-sX`, `-sF`, `-sN`, `-sI`, `-sU`), Firewall Evasion Techniques (`-f`, `-D`, `--source-port`, `--spoof-mac`), Hping3 Packet Crafting, and Masscan Internet-Scale Scanning.

---

## ⚔️ 1. Nmap Port Scanning Methodologies

### 1.1 Detailed Technical Mechanics of Scan Types

#### 1. TCP Full Connect Scan (`nmap -sT`)
- **Mechanic**: Completes the full TCP 3-way handshake (`SYN` -> `SYN/ACK` -> `ACK`). Once established, Nmap closes the connection with a `RST/ACK`.
- **Pros**: Does not require root/administrative privileges.
- **Cons**: Extremely noisy; target applications log the full connection attempt.

#### 2. TCP Stealth SYN Scan (`nmap -sS`)
- **Mechanic**: Half-open scan. Transmits a `SYN` packet. If the port is open, the target returns `SYN/ACK`. Nmap immediately responds with a `RST` packet to tear down the connection before it completes.
- **Pros**: Highly efficient; bypasses application-level connection logging.
- **Cons**: Requires root/administrator privileges to raw-craft packets.

#### 3. Inverse TCP Secret Scans (Xmas, FIN, Null)
- **Xmas Scan (`nmap -sX`)**: Sets FIN, URG, and PSH flags simultaneously.
- **FIN Scan (`nmap -sF`)**: Sets only the FIN flag.
- **Null Scan (`nmap -sN`)**: Sets zero control flags.
- **RFC 793 Rules**:
  - Closed ports MUST return a TCP `RST` packet.
  - Open or Filtered ports will silently DROP the packet without responding.
- **Cons**: Ineffective against Microsoft Windows target stacks (Windows returns `RST` for all ports regardless of state).

#### 4. TCP Idle Scan (`nmap -sI <zombie_ip>`)
- **Mechanic**: Advanced blind scanning technique that spoofs the IP address of an idle third-party host ("zombie") and monitors IP ID sequence increments on the zombie host to infer target port states without sending a single packet with the attacker's real IP address.

> [!DANGER] 🛡️ **📋 Comprehensive Nmap Scan Type Reference Matrix**

| Scan Name | Nmap Flag | Flags Set | Open Port Response | Closed Port Response | Privileges Needed |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **TCP Full Connect** | `-sT` | `SYN` | `SYN/ACK` (Handshake completes) | `RST/ACK` | User |
| **TCP Stealth SYN** | `-sS` | `SYN` | `SYN/ACK` (Nmap sends `RST`) | `RST/ACK` | Root |
| **TCP Xmas Scan** | `-sX` | `FIN, URG, PSH` | No Response (Silent drop) | `RST` | Root |
| **TCP FIN Scan** | `-sF` | `FIN` | No Response (Silent drop) | `RST` | Root |
| **TCP Null Scan** | `-sN` | None (`0`) | No Response (Silent drop) | `RST` | Root |
| **TCP ACK Scan** | `-sA` | `ACK` | `RST` (Filtered vs Unfiltered) | `RST` | Root |
| **UDP Scan** | `-sU` | UDP Datagram | UDP response or No Response | ICMP Type 3 Code 3 | Root |
| **TCP Idle Scan** | `-sI` | Spoofed `SYN` | Zombie IP ID increments by 2 | Zombie IP ID +1 | Root |

---

## 🛡️ 2. Firewall Evasion & Obfuscation Techniques

### 2.1 Technical Evasion Syntax & Mechanics

#### 1. IP Header Fragmentation (`nmap -f` or `--mtu`)
Splits TCP header packets into small 8-byte fragments to evade stateless firewall inspection engines and simple IDS signature rules.

#### 2. Decoy IP Scanning (`nmap -D RND:10 <target>`)
Mixes the attacker's real IP address with fake decoy IP addresses, confounding firewall log analysis and incident response attribution.

#### 3. Source Port Manipulation (`nmap --source-port 53` or `-g 53`)
Forces Nmap scan traffic to originate from trusted well-known ports (e.g., DNS port 53 or HTTP port 80), bypassing poorly configured inbound firewall rules.

#### 4. MAC Address Spoofing (`nmap --spoof-mac Cisco`)
Spoofs the hardware MAC address of the network interface card to bypass local layer-2 MAC address filtering rules.

> [!SHIELD] 🏰 **📋 Comprehensive Firewall Evasion Technique Reference Matrix**

| Evasion Technique | Nmap CLI Flag / Parameter | Operational Evasion Mechanic | Defense Mitigation |
| :--- | :--- | :--- | :--- |
| **Packet Fragmentation** | `nmap -f` or `nmap --mtu 16` | Splits IP header into 8/16-byte chunks | Stateful packet reassembly firewalls |
| **Decoy Scanning** | `nmap -D RND:10 <target>` | Hides real IP among fake decoy IPs | Deep packet flow correlation & netflow |
| **Source Port Spoofing** | `nmap --source-port 53` | Bypasses rules trusting DNS/HTTP ports | Strict directional stateful rules |
| **MAC Address Spoofing** | `nmap --spoof-mac <vendor>` | Spoofs layer-2 hardware address | 802.1X Port Security & ARP inspection |
| **Payload Padding** | `nmap --data-length 25` | Appends random bytes to alter signature | Anomaly-based IPS inspection |
