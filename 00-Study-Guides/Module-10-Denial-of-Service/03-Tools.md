# 03. Tools — Denial-of-Service

> [!TOOL] 🛠️ **Command-Line & GUI DoS Software Reference Matrix**
> Direct technical extraction from official CEH v13 Syllabus (Module 10). Covers hping3, LOIC, HOIC, Slowloris, RUDY, Yersinia, and Wireshark.

---

## 🛠️ 1. Primary DoS Software Reference Matrix

> [!TOOL] 📋 **Comprehensive Denial-of-Service Tools Reference Matrix**

| Software Name | Operational Category | Primary Attack Vector | Platform Support |
| :--- | :--- | :--- | :--- |
| **hping3** | Command-line Packet Crafter | TCP SYN, UDP, ICMP packet flooding | Linux |
| **LOIC (Low Orbit Ion Cannon)**| GUI Flooding Tool | TCP/UDP/HTTP packet flooding | Windows, Linux |
| **HOIC (High Orbit Ion Cannon)**| GUI Multi-threaded Flooding | High-speed HTTP GET/POST flooding with booster scripts | Windows |
| **Slowloris** | Python Slow-Rate Tool | Partial HTTP header thread exhaustion | Cross-platform |
| **R-U-Dead-Yet (RUDY)** | Python Slow-Rate Tool | Slow HTTP POST body submission | Cross-platform |
| **Yersinia** | Layer 2 Attack Tool | DHCP starvation, STP loop attacks | Linux |

---

## 💻 2. Command-Line Syntax & Execution Commands

### 2.1 Slowloris Execution Syntax
- **Execute Slowloris against target web server on port 80**:
  ```bash
  python3 slowloris.py 192.168.1.50 -p 80 -s 500
  ```
