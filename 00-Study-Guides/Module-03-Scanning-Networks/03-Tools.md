# 03. Tools — Scanning Networks

> [!TOOL] 🛠️ **Command-Line & GUI Software Reference Matrix**
> Direct technical extraction from official CEH v13 Syllabus (Module 03). Covers Nmap, Hping3, Masscan, Zenmap, and Metasploit Auxiliary Scanners.

---

## 🛠️ 1. Primary Network Scanning Tools Reference Matrix

> [!TOOL] 📋 **Comprehensive Network Scanning Tools Reference Matrix**

| Utility Name | Category / Type | Primary Operational Purpose | Platform Compatibility |
| :--- | :--- | :--- | :--- |
| **Nmap** | CLI / Raw Socket | Network mapper, port scanner, service detection & NSE engine | Linux, Windows, macOS |
| **Hping3** | CLI / Packet Crafting | Custom TCP/IP packet generator, ping sweeper & firewall tester | Linux, macOS |
| **Masscan** | CLI / Asynchronous | Ultra-fast internet-scale port scanner (10M pps) | Linux, Windows, macOS |
| **Zenmap** | GUI / Nmap Interface | Official visual frontend for Nmap with topology mapping | Linux, Windows, macOS |
| **fping** | CLI / Ping Sweep | Parallel ICMP echo host discovery utility | Linux, macOS |

---

## 💻 2. Command-Line Syntax & Flag Breakdown

### 2.1 Essential Nmap Execution Commands
- **Full SYN Scan with Version & OS Detection**:
  ```bash
  nmap -sS -sV -O -p- -T4 192.168.1.100
  ```
- **Firewall Evasion Scan (Fragmented + Decoys + Source Port 53)**:
  ```bash
  nmap -sS -f -D RND:5 --source-port 53 -Pn 10.0.0.50
  ```

### 2.2 Essential Hping3 Custom Packet Commands
- **TCP SYN Scan on Port 80**:
  ```bash
  hping3 -S -p 80 192.168.1.1
  ```
- **ICMP Ping Sweep**:
  ```bash
  hping3 -1 192.168.1.x
  ```
- **SYN Flood Stress Test**:
  ```bash
  hping3 -S -p 80 --flood --rand-source 192.168.1.1
  ```
