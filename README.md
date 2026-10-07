# 🛡️ CEH v13 Master Vault — Certified Ethical Hacker Study & Lab Guide

[![Certification](https://img.shields.io/badge/Certification-CEH%20v13%20AI%20Edition-red?logo=target)](https://www.eccouncil.org/programs/certified-ethical-hacker-ceh/)
[![Obsidian Vault](https://img.shields.io/badge/Obsidian-Ready%20Vault-purple?logo=obsidian)](https://obsidian.md)
[![Modules](https://img.shields.io/badge/Modules-21%20Complete-green)]()
[![License](https://img.shields.io/badge/License-MIT-blue)](LICENSE)

Curated & Architected by **[Amar Sufiyan KC (@Little-Sufi)](https://github.com/Little-Sufi)**

---

## 📖 Vault Overview

The **CEH v13 Master Vault** is an all-inclusive, highly structured study system and technical lab notebook for the **EC-Council Certified Ethical Hacker (CEH v13 AI Edition)** examination. 

Designed specifically for Obsidian users, security practitioners, and certification aspirants, this vault breaks down complex offensive security domains into high-yield, modular notes covering theory, real-world attack techniques, practical exploitation steps, CLI tool matrices, and exam-focused multiple-choice question (MCQ) review.

---

## 🏆 Interactive Master Dashboard & Gamification

Inside **`00-Study-Guides/Home.md`**, this vault includes an embedded **Interactive XP Tracking Dashboard**:
- Tracks your progress across all 21 modules dynamically using localized storage.
- Earn XP as you complete **Overview**, **Techniques**, **Tools**, **Mitigations**, **Course Notes**, **MCQ Practice**, and **Practical Labs**.
- Live visual progress bar with module completion percentages.

---

## 📚 Complete 21-Module Syllabus Breakdown

| # | Module Name | Focus & Key Concepts |
|:---:|:---|:---|
| **01** | **Introduction to Ethical Hacking** | CIA Triad, Hacking Phases, Cyber Kill Chain, MITRE ATT&CK, CFAA, GDPR |
| **02** | **Footprinting & Reconnaissance** | Search Engine Dorking, OSINT, DNS Enumeration, Shodan, Recon-ng, Whois |
| **03** | **Scanning Networks** | Nmap/NSE, Hping3, Masscan, Port Scanning, OS Fingerprinting, Decoy Scans |
| **04** | **Enumeration** | NetBIOS, SMB (enum4linux), SNMP, LDAP, NFS, DNS Zone Transfers, RPC |
| **05** | **Vulnerability Analysis** | CVE/CWE, CVSS v3.1 Scoring, Nessus, OpenVAS/GVM, Vulnerability Life Cycle |
| **06** | **System Hacking** | Password Cracking (Hydra, Hashcat), Windows PrivEsc, Buffer Overflows, Cover Tracks |
| **07** | **Malware Threats** | Trojans, Ransomware, Polymorphic/Metamorphic Malware, Droppers, Dynamic Analysis |
| **08** | **Sniffing** | Wireshark, TCPDump, ARP Poisoning (Ettercap, Bettercap), MAC Flooding, DHCP Starvation |
| **09** | **Social Engineering** | Phishing, Vishing, Spear Phishing, Social-Engineer Toolkit (SET), Credential Harvesting |
| **10** | **Denial-of-Service** | SYN Floods, UDP Amplification, Slowloris, DDoS Botnets, LOIC/XOIC, BGP Hijacking |
| **11** | **Session Hijacking** | TCP Session Hijacking, Session Fixation, Cross-Site Scripting (XSS), MitM |
| **12** | **Evading IDS, Firewalls & Honeypots** | Fragmentation, Proxy Chains, Source Routing, SSH/DNS Tunneling, Decoys |
| **13** | **Hacking Web Servers** | Apache/IIS Misconfigurations, Directory Traversal, Web Shells, Defacement |
| **14** | **Hacking Web Applications** | OWASP Top 10, SQLi, XSS, CSRF, IDOR, SSRF, Command Injection, Burp Suite |
| **15** | **SQL Injection** | Union-based, Error-based, Blind (Boolean/Time) SQLi, SQLmap Automation, Out-of-Band |
| **16** | **Hacking Wireless Networks** | 802.11 WPA2/WPA3 Handshake Capture, Aircrack-ng, Evil Twin, Rogue AP, Deauth |
| **17** | **Hacking Mobile Platforms** | Android Rooting, APK Reverse Engineering (Jadx, APKTool), iOS Jailbreaking |
| **18** | **IoT & OT Hacking** | Smart Devices, Firmware Extraction (Binwalk), SCADA/ICS, Modbus, MQTT Attacks |
| **19** | **Cloud Computing** | AWS, Azure, GCP Security, Cloud IAM Misconfigurations, S3 Bucket Auditing |
| **20** | **Cryptography** | Symmetric/Asymmetric Ciphers, RSA, ECC, AES, PKI, Digital Signatures, Cryptanalysis |
| **21** | **AI-Powered Ethical Hacking** | Prompt Injection, Adversarial Machine Learning, Model Inversion, AI Threat Hunting |

---

## 📁 Vault Directory Structure

```text
CEH v13/
├── Home.md                                              # Global Vault Landing Page
├── CEH v13 Master Practical Lab & Exploitation Vault.md # Comprehensive single-doc lab cheat sheet
├── 00-Study-Guides/                                     # Core structured modules (M01 to M21)
│   ├── Home.md                                          # Interactive XP Master Dashboard
│   └── Module-01 through Module-21/                     # Individual module notes, MCQs & guides
├── 01-Practical-Labs/                                   # Step-by-step hands-on laboratory exercises
├── lab-scripts/                                         # Exploit & helper scripts (Python, Bash)
├── Tools-Guides/                                        # Reference sheets for primary tools
└── Resources/                                           # Cheat sheets, diagrams, and quick references
```

---

## ⚙️ How to Use with Obsidian

1. Install [Obsidian](https://obsidian.md).
2. Choose **Open folder as vault** and select this directory (`CEH v13`).
3. Recommended Community Plugins:
   - **Dataview**: For custom module querying and task tracking.
   - **Hover Editor**: For quick popup previews of internal links.
   - **Outliner**: For structured note taking during study sessions.
4. Open **`00-Study-Guides/Home.md`** and start tracking your exam preparation!

---

## ⚖️ Ethical Disclaimer

> **DISCLAIMER:** This repository is intended exclusively for educational purposes and authorized penetration testing training in controlled lab environments. Any unauthorized utilization of these techniques against systems without explicit permission is illegal.
