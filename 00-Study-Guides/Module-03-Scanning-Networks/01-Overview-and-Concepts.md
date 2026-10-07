# 01. Overview and Concepts — Scanning Networks

> [!INFO] 📌 **Module Scope & Core Objectives**
> Direct technical extraction from official CEH v13 Syllabus (Module 03). Covers Network Scanning Objectives, Host Discovery (ICMP/ARP pings), TCP 3-Way Handshake & 4-Way Teardown, TCP Control Flags (`SYN`, `ACK`, `FIN`, `RST`, `PSH`, `URG`), Port States (Open, Closed, Filtered), and Scanning Methodology Architecture.

---

## 🧠 1. Network Scanning Taxonomy & Objectives

### 1.1 Detailed Analysis of Network Scanning Objectives
Network scanning is the second phase of penetration testing. Unlike passive footprinting, network scanning involves active packet transmission to target networks to discover live hosts, identify open TCP/UDP ports, enumerate active network service software versions, detect operating system signatures, and discover infrastructure vulnerabilities.

#### 1. Host Discovery (Ping Sweeping)
Identifies live target hosts operating on a given IP subnet range (e.g., using ICMP Echo Requests, ARP requests, TCP ACK pings). Host discovery prevents pentesters from wasting time probing inactive IP addresses.

#### 2. Port Scanning & Service Enumeration
Identifies open TCP and UDP logical ports (ranging from 0 to 65535) and determines the exact daemon software name and version (e.g., Apache 2.4.50, OpenSSH 8.2p1) listening on those endpoints.

#### 3. Operating System Fingerprinting
Determines target host operating systems (Linux, Windows, FreeBSD, Cisco IOS) by analyzing TCP/IP stack implementation nuances, default initial Time-To-Live (TTL) values, TCP window sizes, and responses to malformed flag combinations.

#### 4. Vulnerability Identification & Evasion Assessment
Probes exposed services for known vulnerabilities (CVEs) and assesses the operational posture of firewalls, Intrusion Detection Systems (IDS), and Intrusion Prevention Systems (IPS).

> [!ABSTRACT] 🏛️ **📋 Comprehensive Network Scanning Objectives Reference Matrix**

| Scanning Objective | Primary Technical Purpose | Core Utilities / Flags | Typical Output / Intelligence |
| :--- | :--- | :--- | :--- |
| **Host Discovery** | Locate active, reachable hosts on IP subnet | `nmap -sn`, `fping`, `arp-scan` | Active IP list (`192.168.1.10-50`) |
| **Port Scanning** | Identify open TCP/UDP transport ports | `nmap -sS`, `nmap -sU`, `masscan` | Port status list (`Port 80/tcp OPEN`) |
| **Version Detection** | Grab application banners & software versions | `nmap -sV`, `nc -v`, `banner-grab` | Service release (`OpenSSH 8.2p1`) |
| **OS Fingerprinting** | Determine host OS kernel & platform | `nmap -O`, `xprobe2`, `p0f` | Operating System (`Linux 5.x / TTL 64`) |
| **Firewall Evasion** | Test filtering rules & IDS bypass mechanics | `nmap -f`, `nmap -D`, `nmap --source-port` | Filtered vs Unfiltered port map |

---

## ⚡ 2. TCP Protocol Mechanics & Control Flag Architecture

### 2.1 The TCP 3-Way Handshake & Control Flags
The Transmission Control Protocol (TCP) is a connection-oriented transport protocol specified in RFC 793. Connection establishment requires a rigid 3-way handshake:

1. **SYN (Synchronize)**: The client transmits a TCP packet with the `SYN` bit set to initiate a session and synchronize sequence numbers.
2. **SYN/ACK (Synchronize-Acknowledge)**: The server responds with `SYN` and `ACK` bits set, acknowledging the client's sequence number and sending its own.
3. **ACK (Acknowledge)**: The client sends a final packet with the `ACK` bit set, establishing an active TCP connection.

#### The 6 Primary TCP Control Flags:
- **SYN (Synchronize)**: Initiates connection and synchronizes sequence numbers.
- **ACK (Acknowledge)**: Confirms receipt of transmitted data or sequence packets.
- **FIN (Finish)**: Initiates graceful connection teardown.
- **RST (Reset)**: Abruptly terminates a connection or notifies a client that a port is closed.
- **PSH (Push)**: Commands the receiving TCP stack to push data directly to the application layer without buffering.
- **URG (Urgent)**: Indicates that the packet contains urgent data requiring immediate processing.

> [!IMPORTANT] 🔄 **📋 Comprehensive TCP Control Flag Reference Matrix**

| TCP Flag | Flag Bit Position | Operational Function | Scanning / Protocol Usage |
| :---: | :---: | :--- | :--- |
| **SYN** | Bit 1 | Synchronize sequence numbers | Initiates connection; used in SYN scans (`-sS`) |
| **ACK** | Bit 4 | Acknowledge received data | Completes handshake; used in ACK scans (`-sA`) |
| **FIN** | Bit 0 | Terminate connection gracefully | Connection teardown; used in FIN scans (`-sF`) |
| **RST** | Bit 2 | Reset / abort connection immediately | Closed port response; used in Stealth scans |
| **PSH** | Bit 3 | Push data directly to application | Forces immediate data processing |
| **URG** | Bit 5 | Process urgent payload data | Prioritizes urgent payload bytes |
