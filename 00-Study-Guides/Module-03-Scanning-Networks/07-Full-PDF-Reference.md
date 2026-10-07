# 📜 07. Full PDF Reference — Scanning Networks

> [!INFO] 🏛️ **Official CEH v13 PDF Source Master Repository**
> Cleaned, high-readability technical text extraction directly from official CEH v13 Syllabus PDF (`CEH_v13__Module_03_Scanning_Networks.pdf`). Formatted as structured Markdown prose with proper paragraphs, section headers, and key term highlights.

---

## 📊 Syllabus Metadata & Source Breakdown

> [!ABSTRACT] 📋 **Comprehensive PDF Syllabus Metadata Reference Matrix**

| Metadata Attribute | Syllabus Parameter Value |
| :--- | :--- |
| **Course Module** | **Module 03: Scanning Networks** |
| **Source PDF File** | `CEH_v13__Module_03_Scanning_Networks.pdf` |
| **Total Extracted Pages** | `37 Pages` |
| **Formatting Standard** | Ultra-Readable Markdown Prose & Structured Headings |
| **Extraction Status** | 100% Complete / Verified Text Flow |

---

## 📑 Structured & Readable Syllabus Reference

> [!NOTE]- 📄 **Pages 1 to 5 Syllabus Content**
>
> ### 📍 Page 1
>
> 
> #### 🔹 🔎
> 
> 
> 
> #### 🔹 Scanning Networks
> 
> 
> 
> #### 🔹 Scanning Networks
> 
> 
> 
> #### 🔹 📋Module Overview
> 
> 
> This module covers network scanning techniques, including host discovery, port scanning, service enumeration, OS fingerprinting, firewall evasion, and defensive countermeasures. Scanning is the second phase of ethical hacking after reconnaissance.
> 
> 
> #### 🔹 1. Network Scanning Concepts
> 
> 
> 
> #### 🔹 1.1 Overview of Network Scanning
> 
> 
> Network scanning is the process of systematically probing a network to identify active hosts, open ports, running services, and security configurations.
> 
> 
> #### 🔹 Objectives of Network Scanning
> 
> 
> 
> #### 🔹 Live Host Identification
> 
> 
> Determining which IP addresses are assigned to active systems
> 
> 
> #### 🔹 Port State Discovery
> 
> 
> Identifying open, closed, and filtered ports on target systems
> 
> 
> #### 🔹 Service Enumeration
> 
> 
> 
> #### 🔹 Detecting running services and their versions
> 
> 
> 
> #### 🔹 Operating System Detection
> 
>
> ---
>
> ### 📍 Page 2
>
> 
> #### 🔹 Fingerprinting the OS and version of target systems
> 
> 
> 
> #### 🔹 Network Topology Mapping
> 
> 
> 
> #### 🔹 Understanding network architecture and device placement
> 
> 
> 
> #### 🔹 Security Policy Analysis
> 
> 
> Identifying filtering devices such as firewalls, IDS/IPS, and load balancers
> 
> 
> #### 🔹 🔄Position in the Attack Lifecycle
> 
> 
> Scanning is the second phase of ethical hacking, immediately following reconnaissance. It transitions from passive information gathering to active probing of target systems.
> 
> 
> #### 🔹 1.2 TCP Communication Flags
> 
> 
> TCP uses control flags in the header to manage connection state and data flow.
> 
> 
> #### 🔹 TCP Flag Reference
> 
> 
> 
> #### 🔹 Flag Meaning Purpose
> 
> 
> 
> #### 🔹 SYN Synchronize Initiate a connection
> 
> 
> 
> #### 🔹 ACK AcknowledgmentAcknowledge received data
> 
> 
> 
> #### 🔹 FIN Finish Graceful connection termination
> 
> 
> 
> #### 🔹 RST Reset Abort connection immediately
> 
> 
> 
> #### 🔹 PSH Push Push buffered data to application
> 
> 
> 
> #### 🔹 URG Urgent Urgent pointer field is significant
> 
>
> ---
>
> ### 📍 Page 3
>
> 
> #### 🔹 🔑Significance for Port Scanning
> 
> 
> These flags form the basis of many port-scanning techniques. By
> 
> 
> #### 🔹 manipulating flag combinations, attackers can:
> 
> 
> 
> #### 🔹 Evade detection by IDS/IPS systems
> 
> 
> 
> #### 🔹 Bypass firewall rules
> 
> 
> 
> #### 🔹 Fingerprint operating systems
> 
> 
> 
> #### 🔹 Determine port states indirectly
> 
> 
> 
> #### 🔹 1.3 TCP/IP Communication
> 
> 
> Understanding TCP/IP communication is essential for effective network scanning.
> 
> 
> #### 🔹 TCP Three-Way Handshake
> 
> 
> 
> #### 🔹 Normal connection establishment:
> 
> 
> 
> #### 🔹 Client  Server: SYN
> 
> 
> 
> #### 🔹 Server  Client: SYN/ACK
> 
> 
> 
> #### 🔹 Client  Server: ACK
> 
> 
> 
> #### 🔹 Connection established]
> 
> 
> 
> #### 🔹 Connection Termination
> 
> 
> 
> #### 🔹 Graceful Termination:
> 
> 
> 
> #### 🔹 Client  Server: FIN
> 
> 
> 
> #### 🔹 Server  Client: FIN/ACK
> 
> 
> 
> #### 🔹 Client  Server: ACK
> 
> 
> 
> #### 🔹 Immediate Termination:
> 
> 
> 
> #### 🔹 Either side: RST
> 
> 
> 
> #### 🔹 ICMP in Host Discovery
> 
> 
> ICMP Internet Control Message Protocol) is commonly used for:
>
> ---
>
> ### 📍 Page 4
>
> 
> #### 🔹 Host discovery (ping)
> 
> 
> 
> #### 🔹 Network diagnostics
> 
> 
> 
> #### 🔹 Error reporting
> 
> 
> 
> #### 🔹 Path MTU discovery
> 
> 
> 
> #### 🔹 📦UDP Scanning Challenge
> 
> 
> UDP is stateless and connectionless, making scanning difficult:
> 
> 
> #### 🔹 No handshake or session establishment
> 
> 
> 
> #### 🔹 Requires indirect methods for scanning
> 
> 
> 
> #### 🔹 Port state inferred from ICMP Port Unreachable responses
> 
> 
> 
> #### 🔹 Open ports often yield no response (timeout)
> 
> 
> 
> #### 🔹 Makes UDP scanning slower and less reliable than TCP
> 
> 
> 
> #### 🔹 2. Scanning Tools
> 
> 
> 
> #### 🔹 2.1 **Nmap**
> 
> 
> 
> #### 🔹 ⚔**Nmap**: The Industry Standard
> 
> 
> **Nmap** Network Mapper) is the most widely used network scanning tool in the security industry, offering comprehensive capabilities for host discovery, port scanning, and service enumeration.
> 
> 
> #### 🔹 Core Capabilities
> 
> 
> 
> #### 🔹 Host Discovery
> 
> 
> 
> #### 🔹 Identifying live systems using various ping techniques
> 
> 
> 
> #### 🔹 Port Scanning
> 
> 
> Multiple scan types SYN, Connect, UDP, FIN, NULL, Xmas, etc.)
> 
> 
> #### 🔹 OS Detection
> 
> 
> 
> #### 🔹 TCP/IP stack fingerprinting to identify operating systems
> 
>
> ---
>
> ### 📍 Page 5
>
> 
> #### 🔹 Version Detection
> 
> 
> 
> #### 🔹 Service and application version identification
> 
> 
> 
> #### 🔹 NSE Scripting
> 
> 
> **Nmap** Scripting Engine for automation and vulnerability detection
> 
> 
> #### 🔹 Firewall Evasion
> 
> 
> 
> #### 🔹 Techniques to bypass filtering devices
> 
> 
> 
> #### 🔹 IPv6 Support
> 
> 
> 
> #### 🔹 Native IPv6 scanning capabilities
> 
> 
> 
> #### 🔹 Common **Nmap** Commands
> 
> 
> 
> #### 🔹 # Basic host discovery
> 
> 
> 
> #### 🔹 **nmap** -sn 192.168.1.0/24
> 
> 
> 
> #### 🔹 # **SYN scan** (stealth)
> 
> 
> 
> #### 🔹 **nmap** -sS 192.168.1.10
> 
> 
> 
> #### 🔹 # Full port scan with version detection
> 
> 
> 
> #### 🔹 **nmap** -p- -sV 192.168.1.10
> 
> 
> 
> #### 🔹 # OS detection
> 
> 
> 
> #### 🔹 **nmap** O 192.168.1.10
> 
> 
> 
> #### 🔹 # Aggressive scan with scripts
> 
> 
> 
> #### 🔹 **nmap** A 192.168.1.10
> 
> 
> 
> #### 🔹 # **UDP scan**
> 
> 
> 
> #### 🔹 **nmap** -sU 192.168.1.10
> 
> 
> 
> #### 🔹 2.2 **Hping3**
> 
> 
> **Hping3** is a powerful packet crafting and network testing tool.
> 
> 
> #### 🔹 Primary Uses
> 
> 
> 
> #### 🔹 Custom Packet Crafting
> 
>
> ---
>

> [!NOTE]- 📄 **Pages 6 to 10 Syllabus Content**
>
> ### 📍 Page 6
>
> Create TCP/UDP/ICMP packets with specific flags and payloads
> 
> 
> #### 🔹 Advanced Firewall Testing
> 
> 
> 
> #### 🔹 Test firewall rules and filtering behavior
> 
> 
> 
> #### 🔹 Idle Scans
> 
> 
> 
> #### 🔹 Perform stealthy scans using zombie hosts
> 
> 
> 
> #### 🔹 Traceroute
> 
> 
> 
> #### 🔹 Custom traceroute with various protocols
> 
> 
> 
> #### 🔹 TTL Manipulation
> 
> 
> 
> #### 🔹 Modify Time-To-Live values for fingerprinting and evasion
> 
> 
> 
> #### 🔹 **Hping3** Examples
> 
> 
> 
> #### 🔹 # **SYN scan** on port 80
> 
> 
> 
> #### 🔹 **hping3** S -p 80 192.168.1.10
> 
> 
> 
> #### 🔹 # **UDP scan**
> 
> 
> 
> #### 🔹 **hping3** 2 -p 53 192.168.1.10
> 
> 
> 
> #### 🔹 # ICMP flood test
> 
> 
> 
> #### 🔹 **hping3** 1 --flood 192.168.1.10
> 
> 
> 
> #### 🔹 # Custom TTL
> 
> 
> 
> #### 🔹 **hping3** S -p 80 -t 5 192.168.1.10
> 
> 
> 
> #### 🔹 2.3 Hping Scan with AI
> 
> 
> 
> #### 🔹 AI enhances **Hping3**'s capabilities:
> 
> 
> 
> #### 🔹 AI Enhancements
> 
> 
> 
> #### 🔹 Automating packet modification based on target responses
> 
> 
> Identifying anomalies in replies that indicate filtering or deception Pattern-based port/state inference from incomplete or ambiguous
> 
> 
> #### 🔹 responses
> 
> 
> 
> #### 🔹 Creating custom payloads based on target behavior analysis
> 
>
> ---
>
> ### 📍 Page 7
>
> Adaptive timing to optimize scan speed while avoiding detection
> 
> 
> #### 🔹 Intelligent retry logic for unreliable network conditions
> 
> 
> 
> #### 🔹 2.4 Metasploit
> 
> 
> Metasploit Framework includes powerful auxiliary scanning modules.
> 
> 
> #### 🔹 Scanning Capabilities
> 
> 
> 
> #### 🔹 Auxiliary Scanning Modules
> 
> 
> 
> #### 🔹 Pre-built scanners for various protocols and services
> 
> 
> 
> #### 🔹 Protocol-Specific Scanners:
> 
> 
> 
> #### 🔹 SMB  SMB version detection, share enumeration
> 
> 
> 
> #### 🔹 SSH  SSH version and algorithm detection
> 
> 
> 
> #### 🔹 FTP  Anonymous FTP detection, version identification
> 
> 
> 
> #### 🔹 SNMP  SNMP enumeration and community string testing
> 
> 
> 
> #### 🔹 Automated Vulnerability Checks
> 
> 
> 
> #### 🔹 Integrated vulnerability scanning and exploitation
> 
> 
> 
> #### 🔹 Metasploit Scanner Examples
> 
> 
> 
> #### 🔹 # SMB version detection
> 
> 
> 
> #### 🔹 use auxiliary/scanner/smb/smb_version
> 
> 
> 
> #### 🔹 # SSH version scan
> 
> 
> 
> #### 🔹 use auxiliary/scanner/ssh/ssh_version
> 
> 
> 
> #### 🔹 # Port scanner
> 
> 
> 
> #### 🔹 use auxiliary/scanner/portscan/tcp
> 
> 
> 
> #### 🔹 2.5 NetScanTools Pro
> 
> 
> NetScanTools Pro is a comprehensive commercial network scanning suite.
> 
> 
> #### 🔹 Features
> 
> 
> 
> #### 🔹 **DNS** Tools
> 
>
> ---
>
> ### 📍 Page 8
>
> 
> #### 🔹 **DNS** lookup, zone transfer testing, reverse **DNS**
> 
> 
> 
> #### 🔹 Ping Sweeps
> 
> 
> 
> #### 🔹 ICMP-based host discovery across ranges
> 
> 
> 
> #### 🔹 ARP Scanning
> 
> 
> 
> #### 🔹 Local network MAC address discovery
> 
> 
> 
> #### 🔹 Packet Capture
> 
> 
> 
> #### 🔹 Network traffic analysis and inspection
> 
> 
> 
> #### 🔹 Banner Grabbing
> 
> 
> 
> #### 🔹 Service identification through banner collection
> 
> 
> 
> #### 🔹 Additional Utilities:
> 
> 
> 
> #### 🔹 **WHOIS** lookup
> 
> 
> 
> #### 🔹 Traceroute visualization
> 
> 
> 
> #### 🔹 Port scanner
> 
> 
> 
> #### 🔹 Network connection monitor
> 
> 
> 
> #### 🔹 3. Host Discovery
> 
> 
> 
> #### 🔹 🎯Primary Goal
> 
> 
> Host discovery aims to identify which IP addresses correspond to live, active hosts on the target network before conducting more intensive port scanning.
> 
> 
> #### 🔹 3.1 Host Discovery Techniques
> 
> 
> 
> #### 🔹 Five Primary Categories
> 
> 
> 
> #### 🔹 ICMPBased Discovery
> 
> 
> 
> #### 🔹 Using ICMP echo, timestamp, and address mask requests
> 
> 
> 
> #### 🔹 TCPBased Discovery
> 
> 
> 
> #### 🔹 Sending TCP packets SYN, ACK to common ports
> 
> 
> 
> #### 🔹 UDPBased Discovery
> 
>
> ---
>
> ### 📍 Page 9
>
> 
> #### 🔹 Sending UDP packets to elicit responses
> 
> 
> 
> #### 🔹 ARPBased Discovery
> 
> 
> 
> #### 🔹 ARP requests on local networks Layer 2
> 
> 
> 
> #### 🔹 Protocol-Based Discovery
> 
> 
> 
> #### 🔹 Using IGMP, IP protocol scans, and IP options
> 
> 
> 
> #### 🔹 3.2 ARP Ping Scan
> 
> 
> ARP Address Resolution Protocol) scanning is highly effective on local networks.
> 
> 
> #### 🔹 Characteristics
> 
> 
> 
> #### 🔹 Works only on local LAN (same broadcast domain)
> 
> 
> 
> #### 🔹 Cannot be blocked by host firewalls (operates at Layer 2
> 
> 
> 
> #### 🔹 Bypasses ICMP filtering completely
> 
> 
> 
> #### 🔹 Most reliable method for local network discovery
> 
> 
> 
> #### 🔹 Instant response if host is alive
> 
> 
> 
> #### 🔹 **Nmap** ARP Scan
> 
> 
> 
> #### 🔹 # Automatic ARP scan on local network
> 
> 
> 
> #### 🔹 **nmap** -sn 192.168.1.0/24
> 
> 
> 
> #### 🔹 # Explicit ARP ping
> 
> 
> 
> #### 🔹 **nmap** PR 192.168.1.0/24
> 
> 
> 
> #### 🔹 3.3 UDP Ping Scan
> 
> 
> UDP ping sends empty or small UDP packets to target hosts.
> 
> 
> #### 🔹 Response Interpretation
> 
> 
> 
> #### 🔹 ICMP Port Unreachable Response
> 
> 
> 
> #### 🔹 Host is alive (port is closed)
> 
> 
> 
> #### 🔹 No Response
> 
>
> ---
>
> ### 📍 Page 10
>
> 
> #### 🔹 Port is open or filtered (ambiguous)
> 
> 
> 
> #### 🔹 UDP Service Response
> 
> 
> 
> #### 🔹 Host is alive and port is open
> 
> 
> 
> #### 🔹 **Nmap** UDP Ping
> 
> 
> 
> #### 🔹 **nmap** PU 192.168.1.10
> 
> 
> 
> #### 🔹 3.4 ICMP Echo Ping Scan
> 
> 
> The classic ping using ICMP Echo Request Type 8.
> 
> 
> #### 🔹 Characteristics
> 
> 
> 
> #### 🔹 Most common host discovery method
> 
> 
> 
> #### 🔹 Often blocked by firewalls and host-based filtering
> 
> 
> 
> #### 🔹 Simple and fast when allowed
> 
> 
> 
> #### 🔹 ICMP Echo Reply Type 0 indicates host is alive
> 
> 
> 
> #### 🔹 Usage
> 
> 
> 
> #### 🔹 # Standard ping
> 
> 
> 
> #### 🔹 ping 192.168.1.10
> 
> 
> 
> #### 🔹 # **Nmap** ICMP echo ping
> 
> 
> 
> #### 🔹 **nmap** PE 192.168.1.10
> 
> 
> 
> #### 🔹 3.5 ICMP Echo Ping Sweep
> 
> 
> Ping sweep scans multiple hosts in a range for live systems.
> 
> 
> #### 🔹 Tools
> 
> 
> 
> #### 🔹 fping
> 
> 
> 
> #### 🔹 Fast, parallelized ping utility
> 
> 
> 
> #### 🔹 fping -a -g 192.168.1.0/24
> 
>
> ---
>

> [!NOTE]- 📄 **Pages 11 to 15 Syllabus Content**
>
> ### 📍 Page 11
>
> 
> #### 🔹 Angry IP Scanner
> 
> 
> 
> #### 🔹 GUI-based IP scanner with ping sweep capabilities
> 
> 
> 
> #### 🔹 **Nmap**
> 
> 
> 
> #### 🔹 **nmap** -sn PE 192.168.1.0/24
> 
> 
> 
> #### 🔹 3.6 ICMP Timestamp Ping Scan
> 
> 
> ICMP Timestamp Request Type 13 queries system time.
> 
> 
> #### 🔹 Advantages
> 
> 
> 
> #### 🔹 Rarely filtered by firewalls
> 
> 
> 
> #### 🔹 Alternative when ICMP Echo is blocked
> 
> 
> 
> #### 🔹 Can reveal timezone information
> 
> 
> 
> #### 🔹 Useful for clock skew analysis
> 
> 
> 
> #### 🔹 **Nmap** Command
> 
> 
> 
> #### 🔹 **nmap** PP 192.168.1.10
> 
> 
> 
> #### 🔹 3.7 ICMP Address Mask Ping Scan
> 
> 
> ICMP Address Mask Request Type 17 queries subnet mask.
> 
> 
> #### 🔹 Intelligence Gathered
> 
> 
> 
> #### 🔹 Reveals network class and subnet design
> 
> 
> 
> #### 🔹 Often overlooked by security teams
> 
> 
> 
> #### 🔹 Less commonly filtered than Echo requests
> 
> 
> 
> #### 🔹 Can aid in network topology mapping
> 
> 
> 
> #### 🔹 **Nmap** Command
> 
> 
> 
> #### 🔹 **nmap** PM 192.168.1.10
> 
>
> ---
>
> ### 📍 Page 12
>
> 
> #### 🔹 3.8 TCP SYN Ping Scan
> 
> 
> TCP SYN ping sends SYN packets to commonly open ports.
> 
> 
> #### 🔹 Response Analysis
> 
> 
> 
> #### 🔹 SYN/ACK Response
> 
> 
> 
> #### 🔹 Host is alive, port is open
> 
> 
> 
> #### 🔹 RST Response
> 
> 
> 
> #### 🔹 Host is alive, port is closed
> 
> 
> 
> #### 🔹 No Response
> 
> 
> 
> #### 🔹 Port is filtered or host is down
> 
> 
> 
> #### 🔹 Common Target Ports
> 
> 
> 
> #### 🔹 Port 80 HTTP
> 
> 
> 
> #### 🔹 Port 443 HTTPS
> 
> 
> 
> #### 🔹 Port 22 SSH
> 
> 
> 
> #### 🔹 Port 3389 RDP
> 
> 
> 
> #### 🔹 **Nmap** Command
> 
> 
> 
> #### 🔹 # SYN ping to ports 80 and 443
> 
> 
> 
> #### 🔹 **nmap** PS80,443 192.168.1.10
> 
> 
> 
> #### 🔹 3.9 TCP ACK Ping Scan
> 
> 
> TCP ACK ping sends packets with the ACK flag set.
> 
> 
> #### 🔹 Purpose
> 
> 
> 
> #### 🔹 Used to bypass stateless firewalls
> 
> 
> 
> #### 🔹 Detects stateful vs. stateless filtering behavior
> 
> 
> 
> #### 🔹 RST response indicates host is alive
> 
> 
> 
> #### 🔹 Useful when SYN packets are filtered
> 
> 
> 
> #### 🔹 **Nmap** Command
> 
>
> ---
>
> ### 📍 Page 13
>
> 
> #### 🔹 **nmap** PA80,443 192.168.1.10
> 
> 
> 
> #### 🔹 3.10 IP Protocol Ping Scan
> 
> 
> IP Protocol Scan sends packets with different IP protocol numbers 1255.
> 
> 
> #### 🔹 Characteristics
> 
> 
> 
> #### 🔹 Tests which IP protocols are supported
> 
> 
> 
> #### 🔹 ICMP Protocol Unreachable indicates host is alive
> 
> 
> 
> #### 🔹 Useful for fingerprinting and discovery
> 
> 
> 
> #### 🔹 Rarely used but effective when other methods fail
> 
> 
> 
> #### 🔹 **Nmap** Command
> 
> 
> 
> #### 🔹 **nmap** PO 192.168.1.10
> 
> 
> 
> #### 🔹 3.11 Host Discovery with AI
> 
> 
> AI enhances host discovery through intelligent analysis.
> 
> 
> #### 🔹 AI Capabilities
> 
> 
> 
> #### 🔹 Automatic Pattern Inference
> 
> 
> Learning which discovery methods work best for specific targets
> 
> 
> #### 🔹 Adaptive Retry Logic
> 
> 
> 
> #### 🔹 Intelligently adjusting timeouts and retry attempts
> 
> 
> 
> #### 🔹 Predicting Live Hosts
> 
> 
> 
> #### 🔹 Inferring host status from partial or ambiguous responses
> 
> 
> 
> #### 🔹 Reducing False Positives
> 
> 
> 
> #### 🔹 Machine learning to distinguish real hosts from honeypots
> 
> 
> 
> #### 🔹 Detecting Stealth Firewall Rules
> 
> 
> 
> #### 🔹 Identifying filtering patterns through response analysis
> 
> 
> 
> #### 🔹 Optimizing Scan Order
> 
>
> ---
>
> ### 📍 Page 14
>
> 
> #### 🔹 Prioritizing likely-live hosts based on network patterns
> 
> 
> 
> #### 🔹 3.12 Ping Sweep Tools
> 
> 
> 
> #### 🔹 Popular Tools
> 
> 
> 
> #### 🔹 fping
> 
> 
> 
> #### 🔹 Fast, scriptable ping utility with range support
> 
> 
> 
> #### 🔹 **Nmap**
> 
> 
> 
> #### 🔹 Comprehensive host discovery with multiple techniques
> 
> 
> 
> #### 🔹 Angry IP Scanner
> 
> 
> 
> #### 🔹 User-friendly GUI scanner for Windows/Linux/Mac
> 
> 
> 
> #### 🔹 SolarWinds IP Scanner
> 
> 
> 
> #### 🔹 Enterprise-grade commercial IP scanning tool
> 
> 
> 
> #### 🔹 **Masscan**
> 
> 
> 
> #### 🔹 Extremely fast port scanner with ping capabilities
> 
> 
> 
> #### 🔹 Netdiscover
> 
> 
> 
> #### 🔹 ARP-based network discovery tool
> 
> 
> 
> #### 🔹 4. Port and Service Discovery
> 
> 
> 
> #### 🔹 4.1 Port Scanning Techniques
> 
> 
> 
> #### 🔹 4.1.1 TCP Connect / Full-Open Scan
> 
> 
> Full TCP connection using the complete three-way handshake.
>
> ---
>
> ### 📍 Page 15
>
> 
> #### 🔹 🔌Characteristics
> 
> 
> 
> #### 🔹 Uses full 3-way handshake: SYN  SYN/ACK  ACK
> 
> 
> 
> #### 🔹 Most accurate port state detection
> 
> 
> 
> #### 🔹 Easily detected and logged by target systems
> 
> 
> 
> #### 🔹 Does not require root/administrator privileges
> 
> 
> 
> #### 🔹 Slower than half-open scans
> 
> 
> 
> #### 🔹 **Nmap** Command:
> 
> 
> 
> #### 🔹 **nmap** -sT 192.168.1.10
> 
> 
> 
> #### 🔹 4.1.2 Stealth Scan (Half-Open **SYN Scan**)
> 
> 
> **SYN scan** does not complete the three-way handshake.
> 
> 
> #### 🔹 Process:
> 
> 
> 
> #### 🔹 Attacker  Target: SYN
> 
> 
> 
> #### 🔹 Target  Attacker: SYN/ACK (port open)
> 
> 
> 
> #### 🔹 Attacker  Target: RST (abort)
> 
> 
> 
> #### 🔹 Advantages
> 
> 
> 
> #### 🔹 Most common scan type **Nmap** default with privileges)
> 
> 
> 
> #### 🔹 Harder to detect than full connect scan
> 
> 
> 
> #### 🔹 Faster than TCP connect
> 
> 
> 
> #### 🔹 Less likely to be logged by applications
> 
> 
> 
> #### 🔹 Requires root/administrator privileges
> 
> 
> 
> #### 🔹 **Nmap** Command:
> 
> 
> 
> #### 🔹 **nmap** -sS 192.168.1.10
> 
> 
> 
> #### 🔹 4.1.3 Inverse TCP Flag Scan
> 
>
> ---
>

> [!NOTE]- 📄 **Pages 16 to 20 Syllabus Content**
>
> ### 📍 Page 16
>
> Scans using abnormal flag combinations to elicit responses.
> 
> 
> #### 🔹 ⚠RFC 793 Behavior
> 
> 
> 
> #### 🔹 According to RFC 793
> 
> 
> 
> #### 🔹 Closed ports should return RST
> 
> 
> Open ports should ignore packets with unusual flag combinations This behavior enables stealthy port detection.
> 
> 
> #### 🔹 FIN Scan
> 
> 
> Sends packets with only the FIN flag set.
> 
> 
> #### 🔹 Response Interpretation:
> 
> 
> 
> #### 🔹 No response  Open or filtered
> 
> 
> 
> #### 🔹 RST  Closed
> 
> 
> 
> #### 🔹 **nmap** -sF 192.168.1.10
> 
> 
> 
> #### 🔹 NULL Scan
> 
> 
> Sends packets with no flags set.
> 
> 
> #### 🔹 **nmap** -sN 192.168.1.10
> 
> 
> 
> #### 🔹 **Xmas Scan**
> 
> 
> Sends packets with FIN, PSH, and URG flags set ("lit up like a Christmas tree").
> 
> 
> #### 🔹 **nmap** -sX 192.168.1.10
> 
> 
> 
> #### 🔹 4.1.4 **Xmas Scan**
> 
> 
> Abnormal packet with multiple flags for fingerprinting.
> 
> 
> #### 🔹 Characteristics
> 
> 
> 
> #### 🔹 Useful for OS fingerprinting
> 
>
> ---
>
> ### 📍 Page 17
>
> 
> #### 🔹 Bypasses some simple firewalls
> 
> 
> 
> #### 🔹 Windows systems may not respond according to RFC 793
> 
> 
> 
> #### 🔹 Effective against Unix/Linux systems
> 
> 
> 
> #### 🔹 4.1.5 TCP Maimon Scan
> 
> 
> Sends FIN/ACK packets.
> 
> 
> #### 🔹 Purpose
> 
> 
> 
> #### 🔹 Exploits RFC ambiguities in BSD-derived systems
> 
> 
> 
> #### 🔹 Named after Uriel Maimon who discovered the technique
> 
> 
> 
> #### 🔹 Most modern systems have patched this behavior
> 
> 
> 
> #### 🔹 **nmap** -sM 192.168.1.10
> 
> 
> 
> #### 🔹 4.1.6 ACK Flag Probe Scan
> 
> 
> **ACK scan** determines firewall rule sets, not port state.
> 
> 
> #### 🔹 Use Cases
> 
> 
> 
> #### 🔹 Mapping firewall rules
> 
> 
> 
> #### 🔹 Detecting stateful vs. stateless firewalls
> 
> 
> 
> #### 🔹 Identifying filtered ports
> 
> 
> 
> #### 🔹 Understanding firewall configurations
> 
> 
> 
> #### 🔹 Response Analysis:
> 
> 
> 
> #### 🔹 RST  Unfiltered
> 
> 
> 
> #### 🔹 No response  Filtered
> 
> 
> 
> #### 🔹 **nmap** -sA 192.168.1.10
> 
> 
> 
> #### 🔹 4.1.7 IDLE/IPID Header Scan
> 
> 
> Zombie scan uses a third-party "zombie" host.
>
> ---
>
> ### 📍 Page 18
>
> 
> #### 🔹 🧟How IDLE Scan Works
> 
> 
> 
> #### 🔹  Find a zombie host with predictable IPID sequence
> 
> 
> 
> #### 🔹  Spoof packets from zombie to target
> 
> 
> 
> #### 🔹  Monitor zombie's IPID increment
> 
> 
> 
> #### 🔹  Infer target port state from IPID changes
> 
> 
> 
> #### 🔹 Advantages:
> 
> 
> 
> #### 🔹 Completely spoofed source address
> 
> 
> 
> #### 🔹 Target logs show zombie, not attacker
> 
> 
> 
> #### 🔹 Ultimate stealth technique
> 
> 
> 
> #### 🔹 **nmap** -sI zombie_ip target_ip
> 
> 
> 
> #### 🔹 4.1.8 **UDP Scan**
> 
> 
> UDP scanning is challenging due to protocol characteristics.
> 
> 
> #### 🔹 Challenges
> 
> 
> 
> #### 🔹 No handshake mechanism
> 
> 
> 
> #### 🔹 Slow and unreliable
> 
> 
> 
> #### 🔹 High rate of false positives
> 
> 
> 
> #### 🔹 Often rate-limited by OS and firewalls
> 
> 
> 
> #### 🔹 Response Interpretation
> 
> 
> 
> #### 🔹 No Response
> 
> 
> 
> #### 🔹 Port is open or filtered (ambiguous)
> 
> 
> 
> #### 🔹 ICMP Port Unreachable
> 
> 
> 
> #### 🔹 Port is closed
> 
> 
> 
> #### 🔹 UDP Service Banner
> 
> 
> 
> #### 🔹 Port is open with responding service
> 
>
> ---
>
> ### 📍 Page 19
>
> 
> #### 🔹 **nmap** -sU 192.168.1.10
> 
> 
> 
> #### 🔹 4.1.9 SCTP INIT Scan
> 
> 
> SCTP Stream Control Transmission Protocol) equivalent of **SYN scan**.
> 
> 
> #### 🔹 Characteristics
> 
> 
> 
> #### 🔹 Used for SCTP-based services SS7, SIGTRAN
> 
> 
> 
> #### 🔹 Less commonly filtered than TCP
> 
> 
> 
> #### 🔹 Stealth alternative for SCTP networks
> 
> 
> 
> #### 🔹 **nmap** -sY 192.168.1.10
> 
> 
> 
> #### 🔹 4.1.10 SCTP COOKIE ECHO Scan
> 
> 
> Stealth SCTP scanning technique.
> 
> 
> #### 🔹 Advantages
> 
> 
> 
> #### 🔹 Does not complete SCTP association
> 
> 
> 
> #### 🔹 Bypasses some firewall rules
> 
> 
> 
> #### 🔹 Effective on SCTP-aware networks
> 
> 
> 
> #### 🔹 **nmap** -sZ 192.168.1.10
> 
> 
> 
> #### 🔹 4.1.11 SSDP and List Scan
> 
> 
> SSDP Simple Service Discovery Protocol) for IoT enumeration.
> 
> 
> #### 🔹 Applications
> 
> 
> 
> #### 🔹 IoT device discovery
> 
> 
> 
> #### 🔹 UPnP enumeration
> 
> 
> 
> #### 🔹 Smart home device identification
> 
> 
> 
> #### 🔹 Network printer discovery
> 
> 
> 
> #### 🔹 List Scan:
> 
>
> ---
>
> ### 📍 Page 20
>
> 
> #### 🔹 Simply lists targets without scanning **DNS** resolution only)
> 
> 
> 
> #### 🔹 **nmap** -sL 192.168.1.0/24
> 
> 
> 
> #### 🔹 4.1.12 IPv6 Scan
> 
> 
> IPv6 scanning presents unique challenges.
> 
> 
> #### 🔹 Characteristics
> 
> 
> Massive address space makes brute-force scanning impractical
> 
> 
> #### 🔹 Requires knowledge of SLAAC patterns
> 
> 
> 
> #### 🔹 Often less filtered than IPv4
> 
> 
> 
> #### 🔹 Many networks have weak IPv6 security
> 
> 
> 
> #### 🔹 Tools
> 
> 
> 
> #### 🔹 **Nmap**
> 
> 
> 
> #### 🔹 **nmap** 6 fe801
> 
> 
> 
> #### 🔹 THCIPv6
> 
> 
> 
> #### 🔹 Specialized IPv6 attack toolkit
> 
> 
> 
> #### 🔹 IPv6 Considerations:
> 
> 
> 
> #### 🔹 Slower than IPv4 scanning
> 
> 
> 
> #### 🔹 Requires understanding of addressing schemes
> 
> 
> 
> #### 🔹 Link-local, unique local, and global addresses
> 
> 
> 
> #### 🔹 4.2 Port Scanning with AI
> 
> 
> AI optimizes port scanning efficiency and accuracy.
> 
> 
> #### 🔹 AI Contributions
> 
> 
> 
> #### 🔹 Adaptive Timeout Tuning
> 
> 
> 
> #### 🔹 Dynamically adjusting timeouts based on network conditions
> 
> 
> 
> #### 🔹 Predicting Filtering Behavior
> 
>
> ---
>

> [!NOTE]- 📄 **Pages 21 to 25 Syllabus Content**
>
> ### 📍 Page 21
>
> 
> #### 🔹 Inferring firewall rules from response patterns
> 
> 
> 
> #### 🔹 Anomaly-Based Service Classification
> 
> 
> 
> #### 🔹 Identifying services from unusual banner responses
> 
> 
> 
> #### 🔹 Automated Summarization
> 
> 
> 
> #### 🔹 Generating human-readable scan reports
> 
> 
> 
> #### 🔹 Risk Scoring
> 
> 
> Prioritizing vulnerabilities based on exposure and exploitability
> 
> 
> #### 🔹 Intelligent Retry Logic
> 
> 
> 
> #### 🔹 Adaptive retry strategies for unreliable networks
> 
> 
> 
> #### 🔹 4.3 Service Version Discovery
> 
> 
> Service versioning identifies specific software versions running on open ports.
> 
> 
> #### 🔹 Techniques
> 
> 
> 
> #### 🔹 Banner Grabbing
> 
> 
> 
> #### 🔹 Connecting to services and capturing welcome banners
> 
> 
> 
> #### 🔹 **Nmap** Version Detection
> 
> 
> 
> #### 🔹 **nmap** -sV 192.168.1.10
> 
> 
> 
> #### 🔹 Protocol-Specific Probing
> 
> 
> Sending protocol-specific payloads to elicit version information
> 
> 
> #### 🔹 Information Revealed
> 
> 
> 
> #### 🔹 Application name and version
> 
> 
> 
> #### 🔹 Operating system hints
> 
> 
> 
> #### 🔹 Service configuration details
> 
> 
> 
> #### 🔹 Patch levels and build numbers
> 
> 
> 
> #### 🔹 4.4 Service Version Discovery with AI
> 
> 
> AI enhances version detection capabilities.
>
> ---
>
> ### 📍 Page 22
>
> 
> #### 🔹 AI Applications
> 
> 
> 
> #### 🔹 Banner Parsing
> 
> 
> Extracting version information from complex or obfuscated banners
> 
> 
> #### 🔹 Obfuscation Detection
> 
> 
> 
> #### 🔹 Identifying modified or disguised banners
> 
> 
> 
> #### 🔹 Disguised Service Identification
> 
> 
> 
> #### 🔹 Recognizing services running on non-standard ports
> 
> 
> 
> #### 🔹 CVE Correlation
> 
> 
> 
> #### 🔹 Automatically matching versions to known vulnerabilities
> 
> 
> 
> #### 🔹 Confidence Scoring
> 
> 
> 
> #### 🔹 Providing probability scores for uncertain identifications
> 
> 
> 
> #### 🔹 4.5 **Nmap** Scan Time Reduction Techniques
> 
> 
> 
> #### 🔹 Optimization Strategies
> 
> 
> 
> #### 🔹 Aggressive Timing Template
> 
> 
> 
> #### 🔹 **nmap** T5 192.168.1.10
> 
> 
> 
> #### 🔹 Fastest timing (may trigger IDS
> 
> 
> 
> #### 🔹 Scan Top Ports Only
> 
> 
> 
> #### 🔹 **nmap** --top-ports 100 192.168.1.10
> 
> 
> 
> #### 🔹 Scans most common 100 ports
> 
> 
> 
> #### 🔹 Skip **DNS** Resolution
> 
> 
> 
> #### 🔹 **nmap** -n 192.168.1.10
> 
> 
> 
> #### 🔹 Avoids reverse **DNS** lookups
> 
> 
> 
> #### 🔹 Disable Retries
> 
> 
> 
> #### 🔹 **nmap** --max-retries 0 192.168.1.10
> 
>
> ---
>
> ### 📍 Page 23
>
> 
> #### 🔹 No retransmission of probes
> 
> 
> 
> #### 🔹 Ping Before Port Scan
> 
> 
> 
> #### 🔹 **nmap** -sn 192.168.1.0/24  hosts.txt
> 
> 
> 
> #### 🔹 **nmap** -iL hosts.txt
> 
> 
> 
> #### 🔹 Only scan confirmed live hosts
> 
> 
> 
> #### 🔹 Use Host Lists
> 
> 
> 
> #### 🔹 Provide explicit IP lists instead of ranges
> 
> 
> 
> #### 🔹 Parallel Scanning
> 
> 
> 
> #### 🔹 **nmap** --min-parallelism 100 192.168.1.10
> 
> 
> 
> #### 🔹 Increase parallel probe count
> 
> 
> 
> #### 🔹 5. OS Discovery (Banner Grabbing /
> 
> 
> 
> #### 🔹 Fingerprinting)
> 
> 
> 
> #### 🔹 5.1 OS Discovery Techniques
> 
> 
> 
> #### 🔹 Primary Methods
> 
> 
> 
> #### 🔹 Banner Grabbing
> 
> 
> 
> #### 🔹 Collecting service banners HTTP, SSH, FTP, SMTP, Telnet)
> 
> 
> 
> #### 🔹 TCP/IP Stack Fingerprinting
> 
> 
> 
> #### 🔹 Analyzing TCP/IP implementation differences
> 
> 
> 
> #### 🔹 TTL / Window Size Analysis
> 
> 
> 
> #### 🔹 Examining default TTL and TCP window sizes
> 
> 
> 
> #### 🔹 ICMP Signature Analysis
> 
> 
> 
> #### 🔹 Evaluating ICMP response characteristics
> 
> 
> 
> #### 🔹 5.2 Ways to Identify Target OS
> 
> 
> 
> #### 🔹 Fingerprinting Indicators
> 
>
> ---
>
> ### 📍 Page 24
>
> 
> #### 🔹 Default Port Behavior
> 
> 
> 
> #### 🔹 OS-specific open port patterns
> 
> 
> 
> #### 🔹 Time-Based Responses
> 
> 
> 
> #### 🔹 Timing characteristics of replies
> 
> 
> 
> #### 🔹 TCP Flag Responses
> 
> 
> 
> #### 🔹 Reactions to unusual flag combinations
> 
> 
> 
> #### 🔹 Application Headers
> 
> 
> 
> #### 🔹 HTTP, SSH, and other protocol banners revealing OS
> 
> 
> 
> #### 🔹 Network Stack Quirks
> 
> 
> 
> #### 🔹 Initial window size
> 
> 
> 
> #### 🔹 Window scaling
> 
> 
> 
> #### 🔹 Timestamp options
> 
> 
> 
> #### 🔹 Maximum segment size
> 
> 
> 
> #### 🔹 TCP options ordering
> 
> 
> 
> #### 🔹 5.3 OS Discovery Tools
> 
> 
> 
> #### 🔹 Tool Overview
> 
> 
> 
> #### 🔹 **Nmap**
> 
> 
> 
> #### 🔹 **nmap** O 192.168.1.10
> 
> 
> 
> #### 🔹 Most comprehensive OS detection database
> 
> 
> 
> #### 🔹 Unicornscan
> 
> 
> 
> #### 🔹 High-speed, flexible scanner with OS detection
> 
> 
> 
> #### 🔹 Xprobe2
> 
> 
> 
> #### 🔹 Active OS fingerprinting tool using ICMP
> 
> 
> 
> #### 🔹 p0f
> 
> 
> 
> #### 🔹 Passive OS fingerprinting (no active probing)
> 
> 
> 
> #### 🔹 Ettercap
> 
> 
> 
> #### 🔹 Passive fingerprinting in MITM scenarios
> 
> 
> 
> #### 🔹 2 4
> 
>
> ---
>
> ### 📍 Page 25
>
> 
> #### 🔹 5.4 **Nmap** Script Engine for OS Discovery
> 
> 
> NSE scripts provide targeted OS and service fingerprinting.
> 
> 
> #### 🔹 Useful Scripts
> 
> 
> 
> #### 🔹 http-useragent
> 
> 
> 
> #### 🔹 **nmap** --script http-useragent 192.168.1.10
> 
> 
> 
> #### 🔹 Extracts HTTP server information
> 
> 
> 
> #### 🔹 smb-os-discovery
> 
> 
> 
> #### 🔹 **nmap** --script smb-os-discovery 192.168.1.10
> 
> 
> 
> #### 🔹 Detects OS via SMB protocol
> 
> 
> 
> #### 🔹 ssh-hostkey
> 
> 
> 
> #### 🔹 **nmap** --script ssh-hostkey 192.168.1.10
> 
> 
> 
> #### 🔹 Reveals SSH key fingerprints and OS hints
> 
> 
> 
> #### 🔹 Additional Scripts:
> 
> 
> 
> #### 🔹 banner   Generic banner grabbing
> 
> 
> 
> #### 🔹 ftp-anon  FTP version and anonymous access
> 
> 
> 
> #### 🔹 telnet-encryption  Telnet capabilities
> 
> 
> 
> #### 🔹 5.5 IPv6 OS Fingerprinting
> 
> 
> IPv6 OS detection uses unique characteristics.
> 
> 
> #### 🔹 IPv6 Fingerprinting Methods
> 
> 
> 
> #### 🔹 Flow Label Field
> 
> 
> 
> #### 🔹 OS-specific flow label generation patterns
> 
> 
> 
> #### 🔹 Hop Limit Values
> 
> 
> 
> #### 🔹 Default hop limit differs by OS (similar to IPv4 TTL
> 
> 
> 
> #### 🔹 ICMPv6 Type Responses
> 
>
> ---
>

> [!NOTE]- 📄 **Pages 26 to 30 Syllabus Content**
>
> ### 📍 Page 26
>
> 
> #### 🔹 Response types and error messages
> 
> 
> 
> #### 🔹 Extension Header Ordering
> 
> 
> 
> #### 🔹 OS-specific header ordering preferences
> 
> 
> 
> #### 🔹 5.6 OS Discovery with AI
> 
> 
> AI significantly improves OS fingerprinting accuracy.
> 
> 
> #### 🔹 AI Enhancements
> 
> 
> 
> #### 🔹 Signature Pattern Matching
> 
> 
> 
> #### 🔹 Machine learning models trained on OS signatures
> 
> 
> 
> #### 🔹 Anomaly Recognition
> 
> 
> 
> #### 🔹 Identifying modified or hardened systems
> 
> 
> 
> #### 🔹 Containerized OS Detection
> 
> 
> 
> #### 🔹 Distinguishing containers from host OS
> 
> 
> 
> #### 🔹 Predictive OS Identification
> 
> 
> 
> #### 🔹 Inferring OS from incomplete or ambiguous data
> 
> 
> 
> #### 🔹 Version Prediction
> 
> 
> 
> #### 🔹 Estimating patch levels and build versions
> 
> 
> 
> #### 🔹 5.7 AI-Automated Network Scanning Script
> 
> 
> Custom scripts leverage AI for comprehensive scanning.
> 
> 
> #### 🔹 Script Capabilities
> 
> 
> 
> #### 🔹 Automated Module Execution
> 
> 
> 
> #### 🔹 Run **Nmap**, Hping, and other tools sequentially
> 
> 
> 
> #### 🔹 Response Parsing
> 
> 
> 
> #### 🔹 AI-driven interpretation of scan results
> 
> 
> 
> #### 🔹 Network Mapping
> 
> 
> 
> #### 🔹 Automated topology visualization
> 
> 
> 
> #### 🔹 OS/Service Identification
> 
> 
> 
> #### 🔹 Machine learning classification
> 
>
> ---
>
> ### 📍 Page 27
>
> 
> #### 🔹 Structured Output
> 
> 
> 
> #### 🔹 JSON, XML, or database export
> 
> 
> 
> #### 🔹 Vulnerability Correlation
> 
> 
> 
> #### 🔹 Automatic CVE lookup and risk assessment
> 
> 
> 
> #### 🔹 Example Workflow
> 
> 
> 
> #### 🔹  Discovery: Host discovery across network range
> 
> 
> 
> #### 🔹  Enumeration: Port and service scanning of live hosts
> 
> 
> 
> #### 🔹  Fingerprinting: OS detection and version identification
> 
> 
> 
> #### 🔹  Analysis: AI-driven classification and risk scoring
> 
> 
>  Reporting: Automated report generation with recommendations
> 
> 
> #### 🔹 6. Scanning Beyond IDS and Firewall
> 
> 
> 
> #### 🔹 🕵Evasion Techniques
> 
> 
> These methods help bypass intrusion detection systems IDS, intrusion prevention systems IPS, and firewalls by obfuscating or manipulating scanning traffic.
> 
> 
> #### 🔹 6.1 Packet Fragmentation
> 
> 
> Fragmentation splits packets into smaller pieces.
> 
> 
> #### 🔹 Purpose
> 
> 
> 
> #### 🔹 Bypasses simple packet inspection
> 
> 
> 
> #### 🔹 Evades signature-based detection
> 
> 
> 
> #### 🔹 Fragments payload across multiple packets
> 
> 
> 
> #### 🔹 Exploits reassembly weaknesses
> 
> 
> 
> #### 🔹 **Nmap** Command:
> 
> 
> 
> #### 🔹 **nmap** -f 192.168.1.10
> 
>
> ---
>
> ### 📍 Page 28
>
> 
> #### 🔹 6.2 Source Routing
> 
> 
> Source routing specifies the path packets take.
> 
> 
> #### 🔹 Characteristics
> 
> 
> 
> #### 🔹 Rarely allowed in modern networks
> 
> 
> 
> #### 🔹 Can bypass firewall rules
> 
> 
> 
> #### 🔹 Mostly blocked due to security concerns
> 
> 
> 
> #### 🔹 Useful in legacy environments
> 
> 
> 
> #### 🔹 **Nmap** Command:
> 
> 
> 
> #### 🔹 **nmap** --ip-options "L 192.168.1.1 192.168.1.10" target
> 
> 
> 
> #### 🔹 6.3 Source Port Manipulation
> 
> 
> Spoofing source port to appear as trusted traffic.
> 
> 
> #### 🔹 Common Trusted Ports
> 
> 
> 
> #### 🔹 Port 53 **DNS**
> 
> 
> 
> #### 🔹 Often allowed through firewalls for **DNS** responses
> 
> 
> 
> #### 🔹 Port 20 FTPDATA
> 
> 
> 
> #### 🔹 FTP active mode data connections
> 
> 
> 
> #### 🔹 Port 80 HTTP
> 
> 
> 
> #### 🔹 Web traffic source port
> 
> 
> 
> #### 🔹 Port 443 HTTPS
> 
> 
> 
> #### 🔹 Secure web traffic
> 
> 
> 
> #### 🔹 **Nmap** Command:
> 
> 
> 
> #### 🔹 **nmap** --source-port 53 192.168.1.10
> 
> 
> 
> #### 🔹 6.4 IP Address Decoy
> 
> 
> Decoy scanning includes fake source IP addresses.
>
> ---
>
> ### 📍 Page 29
>
> 
> #### 🔹 Technique
> 
> 
> 
> #### 🔹 Generates packets from multiple fake IPs
> 
> 
> 
> #### 🔹 Makes it difficult to identify the real attacker
> 
> 
> 
> #### 🔹 Target sees scans from many sources
> 
> 
> 
> #### 🔹 Overwhelms logging and analysis
> 
> 
> 
> #### 🔹 **Nmap** Command:
> 
> 
> 
> #### 🔹 **nmap** D RND10 192.168.1.10
> 
> 
> 
> #### 🔹 **nmap** D decoy1,decoy2,ME,decoy3 192.168.1.10
> 
> 
> 
> #### 🔹 6.5 IP Address Spoofing
> 
> 
> Modifying the source IP address in packets.
> 
> 
> #### 🔹 Use Cases
> 
> 
> 
> #### 🔹 IDLE Scans
> 
> 
> 
> #### 🔹 Using zombie hosts for scanning
> 
> 
> 
> #### 🔹 Amplification Attacks
> 
> 
> 
> #### 🔹 DDoS reflection techniques
> 
> 
> 
> #### 🔹 Bypassing IPBased ACLs
> 
> 
> 
> #### 🔹 Evading IP whitelist/blacklist
> 
> 
> 
> #### 🔹 Limitations
> 
> 
> 
> #### 🔹 Cannot receive replies directly
> 
> 
> 
> #### 🔹 Requires packet sniffing or IDLE technique
> 
> 
> 
> #### 🔹 Ineffective against stateful firewalls
> 
> 
> 
> #### 🔹 6.6 MAC Address Spoofing
> 
> 
> Changing NIC MAC address to avoid tracking.
> 
> 
> #### 🔹 Applications
> 
> 
> 
> #### 🔹 Bypass MAC filtering
> 
>
> ---
>
> ### 📍 Page 30
>
> 
> #### 🔹 Impersonate trusted devices
> 
> 
> 
> #### 🔹 Avoid device tracking
> 
> 
> 
> #### 🔹 Reset bandwidth limits
> 
> 
> 
> #### 🔹 **Nmap** Command:
> 
> 
> 
> #### 🔹 **nmap** --spoof-mac Cisco 192.168.1.10
> 
> 
> 
> #### 🔹 **nmap** --spoof-mac 0 192.168.1.10  # Random MAC
> 
> 
> 
> #### 🔹 Manual Spoofing Linux):
> 
> 
> 
> #### 🔹 ifconfig eth0 down
> 
> 
> 
> #### 🔹 ifconfig eth0 hw ether 001122334455
> 
> 
> 
> #### 🔹 ifconfig eth0 up
> 
> 
> 
> #### 🔹 6.7 Creating Custom Packets
> 
> 
> Custom packet crafting for advanced evasion.
> 
> 
> #### 🔹 Tools
> 
> 
> 
> #### 🔹 **Hping3**
> 
> 
> 
> #### 🔹 Command-line packet crafter
> 
> 
> 
> #### 🔹 Scapy
> 
> 
> 
> #### 🔹 Python-based interactive packet manipulation
> 
> 
> 
> #### 🔹 from scapy.all import *
> 
> 
> 
> #### 🔹 packet  IP(dst="192.168.1.10")/TCP(dport=80,flags="S")
> 
> 
> 
> #### 🔹 send(packet)
> 
> 
> 
> #### 🔹 Nemesis
> 
> 
> 
> #### 🔹 Command-line packet injection tool
> 
> 
> 
> #### 🔹 6.8 Randomizing Host Order / Bad Checksums
> 
> 
> 
> #### 🔹 Randomization
> 
> 
> 
> #### 🔹 Randomize Host Order
> 
>
> ---
>

> [!NOTE]- 📄 **Pages 31 to 35 Syllabus Content**
>
> ### 📍 Page 31
>
> 
> #### 🔹 Scan targets in random sequence to avoid pattern detection
> 
> 
> 
> #### 🔹 **nmap** --randomize-hosts 192.168.1.0/24
> 
> 
> 
> #### 🔹 Bad Checksums
> 
> 
> Send packets with invalid checksums to test firewall behavior
> 
> 
> #### 🔹 **nmap** --badsum 192.168.1.10
> 
> 
> 
> #### 🔹 6.9 Proxy Servers
> 
> 
> Proxies forward traffic to hide origin.
> 
> 
> #### 🔹 Types
> 
> 
> 
> #### 🔹 HTTP Proxies
> 
> 
> 
> #### 🔹 Web traffic proxying
> 
> 
> 
> #### 🔹 SOCKS Proxies
> 
> 
> 
> #### 🔹 Protocol-agnostic proxying SOCKS4/SOCKS5
> 
> 
> 
> #### 🔹 Anonymous Proxies
> 
> 
> 
> #### 🔹 Remove identifying information from requests
> 
> 
> 
> #### 🔹 Transparent Proxies
> 
> 
> 
> #### 🔹 Intercepting proxies (not anonymous)
> 
> 
> 
> #### 🔹 6.10 Proxy Chaining
> 
> 
> Chaining multiple proxies for increased anonymity.
> 
> 
> #### 🔹 Benefits
> 
> 
> 
> #### 🔹 Each proxy only knows previous and next hop
> 
> 
> 
> #### 🔹 Extremely difficult to trace back to origin
> 
> 
> 
> #### 🔹 Can combine different proxy types
> 
> 
> 
> #### 🔹 Geographic obfuscation
> 
> 
> 
> #### 🔹 Example Chain:
> 
>
> ---
>
> ### 📍 Page 32
>
> Attacker  SOCKS5 Proxy  HTTP Proxy  TOR Exit Node  Target
> 
> 
> #### 🔹 6.11 Proxy Tools
> 
> 
> 
> #### 🔹 Popular Tools
> 
> 
> 
> #### 🔹 ProxyChains
> 
> 
> 
> #### 🔹 proxychains **nmap** 192.168.1.10
> 
> 
> 
> #### 🔹 Force any application through proxy chains
> 
> 
> 
> #### 🔹 Burp Suite
> 
> 
> 
> #### 🔹 Web application proxy and security testing
> 
> 
> 
> #### 🔹 TOR The Onion Router)
> 
> 
> 
> #### 🔹 Anonymous communication network
> 
> 
> 
> #### 🔹 Privoxy
> 
> 
> 
> #### 🔹 Non-caching web proxy with advanced filtering
> 
> 
> 
> #### 🔹 Shadowsocks
> 
> 
> 
> #### 🔹 Secure SOCKS5 proxy
> 
> 
> 
> #### 🔹 6.12 Anonymizers
> 
> 
> Anonymizers hide your IP through obfuscation networks.
> 
> 
> #### 🔹 Services
> 
> 
> 
> #### 🔹 VPN services
> 
> 
> 
> #### 🔹 Web-based anonymizers
> 
> 
> 
> #### 🔹 TOR network
> 
> 
> 
> #### 🔹 I2P Invisible Internet Project)
> 
> 
> 
> #### 🔹 Freenet
> 
> 
> 
> #### 🔹 6.13 Censorship Circumvention Tools
> 
> 
> 
> #### 🔹 Tools to bypass censorship and filtering:
> 
>
> ---
>
> ### 📍 Page 33
>
> 
> #### 🔹 VPN Virtual Private Network)
> 
> 
> 
> #### 🔹 Encrypted tunnel to bypass restrictions
> 
> 
> 
> #### 🔹 TOR
> 
> 
> 
> #### 🔹 Onion routing for anonymous browsing
> 
> 
> 
> #### 🔹 Psiphon
> 
> 
> 
> #### 🔹 Censorship circumvention tool
> 
> 
> 
> #### 🔹 Shadowsocks
> 
> 
> 
> #### 🔹 Lightweight SOCKS5 proxy
> 
> 
> 
> #### 🔹 V2Ray
> 
> 
> 
> #### 🔹 Advanced proxy platform
> 
> 
> 
> #### 🔹 Lantern
> 
> 
> 
> #### 🔹 P2P censorship circumvention
> 
> 
> 
> #### 🔹 7. Network Scanning Countermeasures
> 
> 
> 
> #### 🔹 🛡Defensive Strategy
> 
> 
> Organizations must implement multiple layers of defense to detect, prevent, and respond to network scanning activities.
> 
> 
> #### 🔹 7.1 Ping Sweep Countermeasures
> 
> 
> 
> #### 🔹 Defensive Measures
> 
> 
> 
> #### 🔹 Block ICMP Types
> 
> 
> 
> #### 🔹 Filter ICMP Echo Request Type 8 and Echo Reply Type 0
> 
> 
> 
> #### 🔹 # iptables example
> 
> 
> 
> #### 🔹 iptables A INPUT -p icmp --icmp-type echo-request -j DROP
> 
> 
> 
> #### 🔹 Rate Limiting
> 
> 
> 
> #### 🔹 Limit ICMP response rate to slow down scanning
> 
> 
> 
> #### 🔹 Network Intrusion Detection
> 
>
> ---
>
> ### 📍 Page 34
>
> 
> #### 🔹 Deploy IDS to detect ping sweep patterns
> 
> 
> 
> #### 🔹 Hide Non-Public Systems
> 
> 
> 
> #### 🔹 Place internal systems behind NAT or firewall
> 
> 
> 
> #### 🔹 7.2 Port Scanning Countermeasures
> 
> 
> 
> #### 🔹 Protection Strategies
> 
> 
> 
> #### 🔹 Firewall Rules
> 
> 
> 
> #### 🔹 Block unnecessary ports and services
> 
> 
> 
> #### 🔹 SYN Cookies
> 
> 
> 
> #### 🔹 Protect against SYN flood during scans
> 
> 
> 
> #### 🔹 Port Knocking
> 
> 
> 
> #### 🔹 Require specific sequence before opening ports
> 
> 
> 
> #### 🔹 # Example: knock ports 1234, 5678, 9012 to open SSH
> 
> 
> 
> #### 🔹 Dynamic Port Filtering
> 
> 
> 
> #### 🔹 Temporarily block IPs showing scanning behavior
> 
> 
> 
> #### 🔹 Service Minimization
> 
> 
> 
> #### 🔹 Disable unnecessary services and close unused ports
> 
> 
> 
> #### 🔹 Network Segmentation
> 
> 
> 
> #### 🔹 Isolate critical systems from scanning attempts
> 
> 
> 
> #### 🔹 7.3 Banner Grabbing Countermeasures
> 
> 
> 
> #### 🔹 Mitigation Techniques
> 
> 
> 
> #### 🔹 Disable Verbose Banners
> 
> 
> 
> #### 🔹 Remove version information from service banners
> 
> 
> 
> #### 🔹 Generic Headers
> 
> 
> 
> #### 🔹 Replace specific banners with generic responses
> 
> 
> 
> #### 🔹 # Nginx example
> 
>
> ---
>
> ### 📍 Page 35
>
> 
> #### 🔹 server_tokens off;
> 
> 
> 
> #### 🔹 # Apache example
> 
> 
> 
> #### 🔹 ServerTokens Prod
> 
> 
> 
> #### 🔹 ServerSignature Off
> 
> 
> 
> #### 🔹 Banner Randomization
> 
> 
> 
> #### 🔹 Randomize or falsify banner information
> 
> 
> 
> #### 🔹 Reverse Proxies
> 
> 
> 
> #### 🔹 Use reverse proxies to mask backend services
> 
> 
> 
> #### 🔹 7.4 IP Spoofing Detection
> 
> 
> 
> #### 🔹 Detection Methods
> 
> 
> 
> #### 🔹 Packet Filtering
> 
> 
> 
> #### 🔹 Ingress/egress filtering at network boundaries
> 
> 
> 
> #### 🔹 Reverse Path Forwarding RPF
> 
> 
> 
> #### 🔹 Verify source IP against routing table
> 
> 
> 
> #### 🔹 TTL Analysis
> 
> 
> 
> #### 🔹 Detect inconsistent TTL values
> 
> 
> 
> #### 🔹 OS Fingerprinting Mismatch
> 
> 
> 
> #### 🔹 Identify when OS fingerprint doesn't match claimed IP
> 
> 
> 
> #### 🔹 SYN Cookie Validation
> 
> 
> 
> #### 🔹 Validate return path for TCP handshakes
> 
> 
> 
> #### 🔹 7.5 IP Spoofing Countermeasures
> 
> 
> 
> #### 🔹 Prevention Measures
> 
> 
> 
> #### 🔹 Anti-Spoof ACLs
> 
> 
> 
> #### 🔹 Access control lists rejecting spoofed traffic
> 
> 
> 
> #### 🔹 # Block RFC 1918 private addresses from WAN
> 
> 
> 
> #### 🔹 iptables A INPUT -i eth0 -s 10.0.0.0/8 -j DROP
> 
>
> ---
>

> [!NOTE]- 📄 **Pages 36 to 37 Syllabus Content**
>
> ### 📍 Page 36
>
> 
> #### 🔹 iptables A INPUT -i eth0 -s 172.16.0.0/12 -j DROP
> 
> 
> 
> #### 🔹 iptables A INPUT -i eth0 -s 192.168.0.0/16 -j DROP
> 
> 
> 
> #### 🔹 Ingress/Egress Filtering
> 
> 
> 
> #### 🔹 BCP 38 and BCP 84 best practices
> 
> 
> 
> #### 🔹 Disable IP Source Routing
> 
> 
> 
> #### 🔹 Reject packets with source routing options
> 
> 
> 
> #### 🔹 # Linux kernel parameter
> 
> 
> 
> #### 🔹 sysctl -w net.ipv4.conf.all.accept_source_route=0
> 
> 
> 
> #### 🔹 Stateful Inspection
> 
> 
> 
> #### 🔹 Stateful firewalls tracking connection state
> 
> 
> 
> #### 🔹 7.6 Scanning Detection Tools
> 
> 
> 
> #### 🔹 Detection and Prevention Systems
> 
> 
> 
> #### 🔹 Snort
> 
> 
> 
> #### 🔹 Open-source network intrusion detection system
> 
> 
> 
> #### 🔹 # Example Snort rule for port scan detection
> 
> 
> alert tcp any any  $HOME_NET any (flags: S; detection_filter: track by_sr c, count 20, seconds 60; msg:"Possible port scan detected";)
> 
> 
> #### 🔹 Suricata
> 
> 
> 
> #### 🔹 High-performance IDS/IPS engine
> 
> 
> 
> #### 🔹 Zeek (formerly Bro)
> 
> 
> 
> #### 🔹 Network analysis framework
> 
> 
> 
> #### 🔹 OSSEC
> 
> 
> 
> #### 🔹 Host-based intrusion detection system
> 
> 
> 
> #### 🔹 SIEM Correlation
> 
> 
> 
> #### 🔹 Security Information and Event Management platforms
> 
> 
> 
> #### 🔹 Firewall Logs
> 
>
> ---
>
> ### 📍 Page 37
>
> 
> #### 🔹 Regular analysis of firewall and IDS logs
> 
> 
> 
> #### 🔹 Additional Tools:
> 
> 
> 
> #### 🔹 PortSentry  Port scan detection and response
> 
> 
> 
> #### 🔹 Fail2Ban  Automated ban based on log patterns
> 
> 
> 
> #### 🔹 PSAD  Port Scan Attack Detector
> 
> 
> 
> #### 🔹 ✅Module Summary
> 
> 
> This module covered comprehensive network scanning techniques, from basic host discovery using ICMP, TCP, and UDP methods to
> 
> 
> #### 🔹 advanced port scanning techniques including stealth scans,
> 
> 
> fragmentation, and firewall evasion.
> 
> 
> #### 🔹 Key concepts include:
> 
> 
> 
> #### 🔹 TCP/IP communication fundamentals and flag manipulation
> 
> 
> 
> #### 🔹 Host discovery techniques ARP, ICMP, TCP, UDP
> 
> 
> 
> #### 🔹 Port scanning methods SYN, Connect, FIN, NULL, Xmas, IDLE
> 
> 
> 
> #### 🔹 Service and OS fingerprinting
> 
> 
> Evasion techniques (fragmentation, spoofing, decoys, proxies)
> 
> 
> #### 🔹 Defensive countermeasures and detection methods
> 
> 
> 
> #### 🔹 Network scanning is a critical phase that bridges passive
> 
> 
> reconnaissance and active exploitation, requiring both technical skill and strategic thinking to execute effectively while avoiding detection.
>
> ---
>
