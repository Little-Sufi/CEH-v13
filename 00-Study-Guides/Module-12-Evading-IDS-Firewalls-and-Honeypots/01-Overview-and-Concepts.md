# 01. Overview and Concepts — Evading IDS, Firewalls, and Honeypots

> [!INFO] 📌 **Module Scope & Core Objectives**
> Direct technical extraction from official CEH v13 Syllabus (Module 12). Covers Intrusion Detection/Prevention System (IDS/IPS) architecture, Firewall classifications (Packet Filtering, Stateful Inspection, Application Proxy, WAF), Evasion Techniques (IP Fragmentation, Session Splicing, TTL Manipulation, Obfuscation, Tunneling), and Honeypot Technologies (Low-Interaction vs High-Interaction, Canary Tokens).

---

## 🧠 1. IDS / IPS & Firewall Architectural Taxonomies

### 1.1 Intrusion Detection & Prevention Architectures
Intrusion Detection Systems (IDS) inspect network traffic or host logs for malicious activity.
- **Passive NIDS (Network IDS)**: Placed on a switch SPAN/TAP port. Sniffs traffic copies in promiscuous mode; detects threats and sends alerts without altering inline traffic flow.
- **Inline NIPS (Network IPS)**: Deployed directly in the physical traffic path. Inspects active packets in real time and can actively drop malicious packets or reset TCP connections.

#### Primary Detection Methodologies:
1. **Signature-Based Detection**: Compares traffic against a database of known attack patterns (e.g., Snort rules). Extremely fast, but completely blind to zero-day attacks.
2. **Anomaly-Based Detection**: Establishes a baseline of normal network behavior (bandwidth, protocol frequency). Triggers alerts when activity deviates statistically from the baseline. High false-positive rate.
3. **Protocol State Analysis**: Verifies incoming traffic against strict RFC protocol specifications.

### 1.2 Firewall Types & Filtering Mechanics
Firewalls enforce security boundaries by filtering traffic based on predefined Access Control Lists (ACLs).

> [!ABSTRACT] 🏛️ **📋 Comprehensive Firewall Architecture Comparison Matrix**

| Firewall Type | OSI Inspection Layer | Primary Filtering Criteria | Key Advantage | Vulnerability Vector |
| :--- | :---: | :--- | :--- | :--- |
| **Packet Filtering** | Layer 3 / Layer 4 | Source/Dest IP, Port, Protocol | High speed, minimal latency | Spoofed IP, ACK scan evasion |
| **Stateful Inspection**| Layer 3 / Layer 4 | Connection State Table (SYN/ACK) | Blocks unestablished state traffic | State table exhaustion DDoS |
| **Application Proxy** | Layer 7 | Complete Layer 7 Payload & Command | Deep inspection, terminates conn | High processing latency / CPU load |
| **Next-Gen WAF** | Layer 7 | Web Payloads (SQLi, XSS, Path Trav)| Contextual web app protection | Encoding / Obfuscation bypass |

---

## ⚡ 2. Evasion Mechanics & Honeypot Architectures

### 2.1 Evasion Attack Mechanics

#### 1. IP Fragmentation
Splits an attack payload across multiple small IP fragments. If an inline NIDS does not perform IP packet reassembly normalization, it inspects fragments individually, missing signature matches that assemble on the target host.

#### 2. Insertion vs Evasion Attacks
- **Insertion Attack**: Attacker crafts a packet accepted by the NIDS but dropped by the end-host (e.g., bad checksum or expired TTL=1). The NIDS sees data that the host never executes.
- **Evasion Attack**: Attacker crafts a packet rejected or missed by the NIDS but accepted and executed by the destination end-host.

#### 3. Session Splicing
Transmits TCP data payloads 1 byte at a time across multiple TCP packets to bypass signature matching engines that evaluate single packets without stream reassembly.

### 2.2 Honeypots & Canary Tokens
Honeypots are decoy systems designed to trap attackers, log TTPs, and divert attention from production servers.
- **Low-Interaction Honeypots**: Emulate listening services (e.g., SSH, FTP) without running a real OS kernel (e.g., Honeyd). Safe, easy to deploy, but easily fingerprinted by advanced attackers.
- **High-Interaction Honeypots**: Real operating systems and hardware (e.g., Sebek). Capture deep zero-day malware analytics, but carry risks if an attacker compromises the honeypot to attack third parties.
- **Canary Tokens (Honeytokens)**: Decoy credentials, database rows, or files deployed in production environments that trigger instant alerts when accessed.

> [!IMPORTANT] 🔄 **📋 Comprehensive Honeypot Classification Reference Matrix**

| Honeypot Category | Interaction Level | OS Kernel Exposure | Primary Use Case | Risk Profile |
| :--- | :---: | :--- | :--- | :--- |
| **Low-Interaction** | Low | Emulated services only | Gathering basic port scan trends | Very Low (Isolated software) |
| **High-Interaction**| High | Full production OS kernel | Deep zero-day malware research | High (Requires strict egress filtering) |
| **Canary Tokens** | Data-Level | N/A (Decoy files/API keys) | Breach detection alerting | Zero operational risk |
