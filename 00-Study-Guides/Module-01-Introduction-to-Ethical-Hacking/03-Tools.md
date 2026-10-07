# 03. Tools — Introduction to Ethical Hacking

> [!TOOL] 🛠️ **Comprehensive Ethical Hacking Tool Suite**
> Direct extraction from official CEH v13 Syllabus (Module 01 Section 3). Covers key offensive security tools, network analyzers, vulnerability scanners, and exploitation frameworks.

---

## 🧰 1. Core Ethical Hacking Tool Matrix

> [!TOOL] 🛠️ **📋 Comprehensive Ethical Hacking Tool Suite Reference Matrix**

| Utility Name | Category & Type | Primary Operational Focus | Key Command / Usage Syntax |
| :--- | :--- | :--- | :--- |
| **Nmap** | Port Scanner & Enum | Network discovery, open port scanning, OS fingerprinting | `nmap -sV -sC -p- 192.168.1.1` |
| **Metasploit** | Exploitation Framework | Penetration testing framework, exploit payloads & C2 | `msfconsole`, `use exploit/...` |
| **Wireshark** | Packet Analyzer | Deep packet inspection, protocol analysis, traffic capture | Packet capture interface GUI |
| **Burp Suite** | Web Application Proxy | Intercepting HTTP requests, parameter manipulation, SAST | Local proxy listener (`127.0.0.1:8080`) |
| **John the Ripper** | Password Cracker | Offline password hash cracking via dictionary/brute-force | `john --wordlist=pass.txt hashes.txt` |
| **Hydra** | Network Logon Cracker | Online brute-force password cracking against SSH/FTP/RDP | `hydra -l admin -P pass.txt ssh://10.0.0.1` |
| **SQLmap** | Database Exploitation | Automating SQL injection discovery & database exfiltration | `sqlmap -u "http://target.com/page.php?id=1" --dbs` |
