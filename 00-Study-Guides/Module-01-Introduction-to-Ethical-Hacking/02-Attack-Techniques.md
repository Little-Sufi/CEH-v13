# 02. Attack Techniques — Introduction to Ethical Hacking

> [!WARNING] ⚡ **Offensive Methodologies & Framework Alignment**
> Direct extraction from official CEH v13 Syllabus (Module 01 Section 4). Covers the CEH 5-Phase Framework, Cyber Kill Chain, Indicators of Compromise (IoCs), MITRE ATT&CK, and the Diamond Model.

---

## 🔄 1. The 5 Phases of Ethical Hacking

### 1.1 In-Depth Analysis of the Penetration Testing Lifecycle
The CEH penetration testing methodology breaks down offensive security engagements into five sequential phases:

#### Phase 1: Reconnaissance (Information Gathering)
Reconnaissance is the initial research phase where an ethical hacker collects as much technical and non-technical intelligence about the target as possible.
- **Passive Reconnaissance**: Gathering publicly available data via WHOIS, DNS records, search engine dorks, Shodan, and social media without directly probing target servers.
- **Active Reconnaissance**: Interacting directly with target systems using ping sweeps, DNS zone transfer queries (`AXFR`), and social engineering calls.

#### Phase 2: Scanning & Enumeration
The tester uses active probing utilities to map out live hosts, open TCP/UDP ports, running service versions, and host operating systems on target IP subnets.
- **Key Tasks**: Port scanning (`nmap -sS`), service banner grabbing (`nmap -sV`), network topology mapping, and enumeration of user accounts, SMB shares, and SNMP strings.

#### Phase 3: Gaining Access (Exploitation)
In this critical phase, the ethical hacker leverages vulnerabilities identified during scanning to bypass security controls and achieve unauthorized remote system access or code execution.
- **Execution Vectors**: Memory corruption exploits, buffer overflows, SQL injection, remote code execution (RCE) flaws, web shell uploads, and weaponized spear-phishing payloads.

#### Phase 4: Maintaining Access (Persistence)
Once initial access is gained, the tester establishes persistent backdoors to ensure continued access across system reboots, user logouts, or network reconnections.
- **Persistence Vectors**: Installing Remote Access Trojans (RATs), creating rogue administrative user accounts, deploying web shells, modifying registry run keys (`HKLM\Software\Microsoft\Windows\CurrentVersion\Run`), and scheduling tasks (`cron` or Windows Task Scheduler).

#### Phase 5: Clearing Tracks (Anti-Forensics)
To prevent detection by security analysts and maintain access, adversaries attempt to erase evidence of their presence from system logs and forensic artifacts.
- **Anti-Forensic Techniques**: Clearing Windows Event Logs (`wevtutil cl`), purging bash command history (`history -c`), modifying file timestamps (timestomping), hiding files inside Alternate Data Streams (ADS), and uninstalling exploit tools.

> [!IMPORTANT] 🔄 **📋 Comprehensive CEH 5-Phase Penetration Testing Reference Matrix**

| Phase # | Phase Name | Primary Technical Goals | Core Utilities & Execution Vectors |
| :---: | :--- | :--- | :--- |
| **Phase 1** | **Reconnaissance** | Harvest target domain, IP subnets, email structures, OSINT footprint | WHOIS, Google Dorking, Shodan, crt.sh, theHarvester |
| **Phase 2** | **Scanning & Enum** | Locate live hosts, open ports, OS versions, user/share objects | Nmap, Masscan, Enum4linux, Rpcclient, Snmpwalk |
| **Phase 3** | **Gaining Access** | Exploit system flaws to achieve remote code execution (RCE) | Metasploit, SQLmap, Buffer Overflows, Spear-phishing |
| **Phase 4** | **Maintaining Access** | Secure persistent remote access across reboots & privileges | RATs, Web shells, Scheduled Tasks, Registry Run Keys |
| **Phase 5** | **Clearing Tracks** | Erase audit trails, event logs, and forensic artifacts | `wevtutil cl`, `history -c`, Timestomping, ADS hiding |

---

## ⚔️ 2. Cyber Kill Chain vs. MITRE ATT&CK Framework

### 2.1 The Lockheed Martin Cyber Kill Chain (7 Sequential Stages)
The Cyber Kill Chain defines the linear sequence of steps an advanced threat actor must complete to carry out a successful cyber breach:

1. **Reconnaissance**: Researching and profiling target organizations, personnel, and network defenses.
2. **Weaponization**: Pairing an automated exploit payload with a malicious deliverable format (e.g., weaponizing a PDF file with a zero-day exploit).
3. **Delivery**: Transmitting the weaponized package to the victim via email attachments, malicious links, or USB drives.
4. **Exploitation**: Triggering the malicious payload to exploit a software vulnerability on the target host.
5. **Installation**: Installing persistent backdoors, Trojans, or rootkits on the compromised system.
6. **Command & Control (C2)**: Establishing an encrypted communication channel between the victim host and adversary infrastructure.
7. **Actions on Objectives**: Carrying out the attack goal—exfiltrating sensitive corporate data, encrypting systems with ransomware, or sabotaging operations.

> [!DANGER] 🛡️ **📋 Comprehensive Lockheed Martin Cyber Kill Chain Reference Matrix**

| Stage # | Stage Name | Technical Operational Objective | Primary Threat Vector |
| :---: | :--- | :--- | :--- |
| **Stage 1** | 🔍 **Reconnaissance** | Target research, employee profiling, OSINT, and perimeter probing | WHOIS, DNS Harvesting, Social Engineering |
| **Stage 2** | 🛠️ **Weaponization** | Coupling exploit with malicious payload into a deliverable package | Weaponized PDF, Office Macro, Custom Binary |
| **Stage 3** | 📨 **Delivery** | Transmitting weaponized payload to the victim target environment | Spear-Phishing, Watering Hole, Rogue USB |
| **Stage 4** | ⚡ **Exploitation** | Triggering adversary code by exploiting system/application vulnerability | Memory Corruption, Buffer Overflow, RCE |
| **Stage 5** | 🚪 **Installation** | Establishing persistent backdoor, Trojan implant, or registry run key | RAT Implants, Rootkits, Scheduled Tasks |
| **Stage 6** | 📡 **Command & Control** | Opening covert encrypted C2 channel to issue remote commands | Encrypted HTTP/DNS Beacons, Reverse Shells |
| **Stage 7** | 🎯 **Actions on Objectives** | Executing attack mission: exfiltration, destruction, or ransomware | Data Exfiltration, Ransomware Deployment |

---

## 🔍 3. Indicators of Compromise (IoCs) & Categories

### 3.1 Forensic IoC Categorization
Security Analysts and Threat Hunters use Indicators of Compromise (IoCs) to detect malicious activity across enterprise networks. CEH classifies IoCs into three distinct operational categories:

1. **Atomic IoCs**: Static, discrete pieces of forensic data that cannot be broken down into smaller components (e.g., IP addresses, MD5/SHA-256 hashes, email addresses).
2. **Computed IoCs**: Derived data elements calculated by processing raw security data (e.g., YARA signature rules, regex patterns, hash match profiles).
3. **Behavioral IoCs**: Sequences of operational events or behavioral anomalies that characterize Tactics, Techniques, and Procedures (TTPs) (e.g., anomalous PowerShell execution combined with outbound lateral SMB connections).

> [!NOTE] 🔍 **📋 Comprehensive Indicator of Compromise (IoC) Reference Matrix**

| IoC Category | Definition & Characteristics | Concrete Technical Examples |
| :--- | :--- | :--- |
| **1. Atomic IoCs** | Discrete data points that cannot be broken down further | IP Addresses, SHA-256 Hashes, Hostnames, Email Addresses |
| **2. Computed IoCs** | Intelligence derived by combining or processing data points | YARA Signatures, Regex Patterns, Hash Match Profiles |
| **3. Behavioral IoCs** | Observed sequences of event anomalies representing TTPs | PowerShell Execution Spikes, Lateral Movement Anomaly |
