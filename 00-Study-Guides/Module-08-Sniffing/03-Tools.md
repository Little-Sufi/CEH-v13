# 03. Tools — Sniffing

> [!TOOL] 🛠️ **Command-Line & GUI Network Sniffing Tools Reference Matrix**
> Direct technical extraction from official CEH v13 Syllabus (Module 08). Covers Wireshark, TShark, Tcpdump, Ettercap, Bettercap, Arpspoof, Yersinia, and Macof.

---

## 🛠️ 1. Primary Sniffing Tools Reference Matrix

> [!TOOL] 📋 **Comprehensive Network Protocol Analyzer Reference Matrix**

| Utility Name | Vendor / Developer | Primary Operational Role | Platform Support |
| :--- | :--- | :--- | :--- |
| **Wireshark** | Wireshark Foundation | Premier GUI network protocol analyzer & packet decoder | Windows, Linux, macOS |
| **Tcpdump** | Open Source | Standard command-line BPF network packet sniffer | Linux, macOS |
| **TShark** | Wireshark Foundation | Command-line version of Wireshark for automated scripts | Cross-platform |
| **Ettercap** | ALOR & NaGA | Comprehensive suite for MitM ARP poisoning & packet filtering | Linux, Windows |
| **Bettercap** | Simone Margaritelli | Modern Go-based network MitM attack framework | Linux, macOS |
| **Yersinia** | Alfredo Almendro | Layer 2 attack framework (DHCP, STP, CDP, 802.1q) | Linux |

---

## 💻 2. Command-Line Syntax & Sniffing Commands

### 2.1 Tcpdump & TShark Capture Syntax
- **Capture 100 packets on eth0 and write to PCAP file**:
  ```bash
  tcpdump -i eth0 -c 100 -w capture.pcap
  ```
- **Read PCAP file and display HTTP POST requests**:
  ```bash
  tshark -r capture.pcap -Y 'http.request.method == "POST"'
  ```
