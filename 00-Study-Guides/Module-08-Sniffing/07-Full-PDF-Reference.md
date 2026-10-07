# 📜 07. Full PDF Reference — Sniffing

> [!INFO] 🏛️ **Official CEH v13 PDF Source Master Repository**
> Cleaned, high-readability technical text extraction directly from official CEH v13 Syllabus PDF (`CEH_v13__Module_08_Sniffing.pdf`). Formatted as structured Markdown prose with proper paragraphs, section headers, and key term highlights.

---

## 📊 Syllabus Metadata & Source Breakdown

> [!ABSTRACT] 📋 **Comprehensive PDF Syllabus Metadata Reference Matrix**

| Metadata Attribute | Syllabus Parameter Value |
| :--- | :--- |
| **Course Module** | **Module 08: Sniffing** |
| **Source PDF File** | `CEH_v13__Module_08_Sniffing.pdf` |
| **Total Extracted Pages** | `29 Pages` |
| **Formatting Standard** | Ultra-Readable Markdown Prose & Structured Headings |
| **Extraction Status** | 100% Complete / Verified Text Flow |

---

## 📑 Structured & Readable Syllabus Reference

> [!NOTE]- 📄 **Pages 1 to 5 Syllabus Content**
>
> ### 📍 Page 1
>
> 
> #### 🔹 📡
> 
> 
> 
> #### 🔹 Sniffing
> 
> 
> 
> #### 🔹 📋Module Overview
> 
> 
> This module covers network sniffing concepts, techniques, and countermeasures. Topics include passive and active sniffing, MAC attacks, DHCP attacks, ARP poisoning, spoofing techniques, DNS poisoning, sniffing tools Wireshark), and comprehensive defensive strategies.
> 
> 
> #### 🔹 1. Sniffing Concepts
> 
> 
> 
> #### 🔹 1.1 Network Sniffing
> 
> 
> 
> #### 🔹 🔍Network Sniffing Definition
> 
> 
> Network sniffing is the process of capturing and analyzing network packets to extract information such as credentials, sessions, network traffic patterns, protocol weaknesses, and cleartext communications.
> 
> 
> #### 🔹 What Sniffers Capture:
> 
> 
> Credentials  Usernames and passwords transmitted in cleartext Session tokens  Authentication cookies and session identifiers Network traffic patterns  Communication flows and bandwidth usage
> 
> 
> #### 🔹 Protocol weaknesses  Vulnerabilities in network protocols
> 
>
> ---
>
> ### 📍 Page 2
>
> Cleartext protocols  Unencrypted communications HTTP, FTP, Telnet)
> 
> 
> #### 🔹 Network Environments:
> 
> 
> 
> #### 🔹 Sniffers intercept packets traveling over:
> 
> 
> 
> #### 🔹 Local Area Networks LANs)
> 
> 
> 
> #### 🔹 Wireless LANs WLANs)
> 
> 
> 
> #### 🔹 Switched networks (with additional techniques required)
> 
> 
> 
> #### 🔹 1.2 How a Sniffer Works
> 
> 
> 
> #### 🔹 Network Interface Modes:
> 
> 
> 
> #### 🔹 Promiscuous Mode Wired Networks)
> 
> 
> 
> #### 🔹 NIC captures all packets on the network segment
> 
> 
> 
> #### 🔹 Not just packets destined for its MAC address
> 
> 
> 
> #### 🔹 Allows interception of all traffic on broadcast domain
> 
> 
> 
> #### 🔹 Monitor Mode Wireless Networks)
> 
> 
> 
> #### 🔹 Captures all wireless frames in the air
> 
> 
> 
> #### 🔹 Doesn't require association with access point
> 
> 
> 
> #### 🔹 Captures management, control, and data frames
> 
> 
> 
> #### 🔹 Packet Processing:
> 
> 
> 
> #### 🔹  Capture  Intercept packets from network interface
> 
> 
> 
> #### 🔹  Filter  Apply capture filters to reduce data volume
> 
> 
> 
> #### 🔹  Decode  Parse protocol headers and payloads
> 
> 
> 
> #### 🔹  Analyze  Extract meaningful information
> 
> 
> 
> #### 🔹  Store  Save packets for later analysis
> 
> 
> 
> #### 🔹 1.3 Types of Sniffing
> 
> 
> 
> #### 🔹 Passive Sniffing
> 
>
> ---
>
> ### 📍 Page 3
>
> 
> #### 🔹 👁Passive Sniffing
> 
> 
> Silently monitors network traffic without any direct interaction or modification. Works on network segments where all traffic is visible to the sniffer.
> 
> 
> #### 🔹 Characteristics:
> 
> 
> 
> #### 🔹 No direct interaction  Silent monitoring only
> 
> 
> 
> #### 🔹 Works on hubs  All traffic broadcast to all ports
> 
> 
> 
> #### 🔹 Unencrypted Wi-Fi  Open wireless networks
> 
> 
> 
> #### 🔹 Cannot be detected easily  No active packets sent
> 
> 
> 
> #### 🔹 Example scenarios  Hub-based networks, broadcast domains
> 
> 
> 
> #### 🔹 Active Sniffing
> 
> 
> 
> #### 🔹 ⚡Active Sniffing
> 
> 
> Involves traffic manipulation or injection to redirect traffic to the attacker. Required on switched networks where traffic is not naturally broadcast.
> 
> 
> #### 🔹 Characteristics:
> 
> 
> 
> #### 🔹 Traffic manipulation  Actively altering network behavior
> 
> 
> Works on switches  Requires attack techniques to bypass switching Detectable  Generates network traffic that can be monitored
> 
> 
> #### 🔹 Examples: ARP poisoning, MAC flooding, DHCP spoofing
> 
> 
> 
> #### 🔹 1.4 How Attackers Exploit Sniffing
> 
> 
> 
> #### 🔹 Attack Scenarios:
> 
> 
> 
> #### 🔹 Credential Theft
> 
> 
> 
> #### 🔹 Intercept FTP, Telnet, HTTP, POP3, IMAP passwords
> 
> 
> 
> #### 🔹 Capture authentication attempts
> 
> 
> 
> #### 🔹 Extract credentials from cleartext protocols
> 
>
> ---
>
> ### 📍 Page 4
>
> 
> #### 🔹 Session Hijacking
> 
> 
> 
> #### 🔹 Capture session cookies
> 
> 
> 
> #### 🔹 Steal authentication tokens
> 
> 
> 
> #### 🔹 Replay captured sessions
> 
> 
> 
> #### 🔹 Man-in-the-Middle MITM Attacks
> 
> 
> 
> #### 🔹 Position between client and server
> 
> 
> 
> #### 🔹 Intercept and potentially modify traffic
> 
> 
> 
> #### 🔹 Impersonate legitimate parties
> 
> 
> 
> #### 🔹 Packet Injection
> 
> 
> 
> #### 🔹 Inject malicious packets into communication streams
> 
> 
> 
> #### 🔹 Modify ongoing communications
> 
> 
> 
> #### 🔹 Hijack TCP sessions
> 
> 
> 
> #### 🔹 Network Reconnaissance
> 
> 
> 
> #### 🔹 Map network architecture
> 
> 
> 
> #### 🔹 Identify active hosts and services
> 
> 
> 
> #### 🔹 Discover network topology and relationships
> 
> 
> 
> #### 🔹 1.5 Protocols Vulnerable to Sniffing
> 
> 
> 
> #### 🔹 Cleartext Protocol Risks:
> 
> 
> 
> #### 🔹 Especially Vulnerable:
> 
> 
> 
> #### 🔹 HTTP  Web traffic without encryption
> 
> 
> 
> #### 🔹 Telnet  Remote terminal access
> 
> 
> 
> #### 🔹 FTP  File transfer protocol
> 
> 
> 
> #### 🔹 SMTP/POP3/IMAP  Email protocols
> 
> 
> 
> #### 🔹 SNMP v1/v2  Network management
> 
> 
> 
> #### 🔹 Rlogin  Remote login (legacy)
> 
> 
> 
> #### 🔹 SMB (older versions)  File sharing
> 
> 
> 
> #### 🔹 ARP  Address resolution (no authentication)
> 
>
> ---
>
> ### 📍 Page 5
>
> 
> #### 🔹 DNS  Domain name resolution (can be spoofed)
> 
> 
> 
> #### 🔹 1.6 Sniffing in the Data Link Layer
> 
> 
> 
> #### 🔹 OSI Layer 2 Attacks:
> 
> 
> 
> #### 🔹 At the Data Link Layer Ethernet), attackers can exploit:
> 
> 
> 
> #### 🔹 ARP poisoning  Redirect traffic by manipulating ARP cache
> 
> 
> 
> #### 🔹 CAM table attacks  Overflow switch MAC address tables
> 
> 
> 
> #### 🔹 MAC spoofing  Impersonate other network devices
> 
> 
> 
> #### 🔹 VLAN hopping  Break VLAN segmentation
> 
> 
> 
> #### 🔹 STP manipulation  Spanning Tree Protocol attacks
> 
> 
> 
> #### 🔹 DHCP attacks  Rogue DHCP servers, DHCP starvation
> 
> 
> 
> #### 🔹 ⚠Layer 2 Impact
> 
> 
> Layer-2 attacks often provide full control over traffic flow, making them particularly dangerous as they bypass many higher-layer security controls.
> 
> 
> #### 🔹 1.7 Hardware Protocol Analyzers
> 
> 
> 
> #### 🔹 Physical Network Analysis Devices:
> 
> 
> 
> #### 🔹 Hardware analyzers are dedicated devices used for:
> 
> 
> 
> #### 🔹 Deep packet inspection  Detailed protocol analysis
> 
> 
> 
> #### 🔹 Network forensics  Post-incident investigation
> 
> 
> 
> #### 🔹 Performance monitoring  Bandwidth and latency analysis
> 
> 
> 
> #### 🔹 Compliance testing  Protocol conformance verification
> 
> 
> 
> #### 🔹 Examples:
> 
> 
> 
> #### 🔹 Fluke Networks analyzers
> 
> 
> 
> #### 🔹 Network General Sniffer (legacy)
> 
> 
> 
> #### 🔹 Distributed analyzers in NOCs/SOCs
> 
> 
> 
> #### 🔹 Portable network test equipment
> 
>
> ---
>

> [!NOTE]- 📄 **Pages 6 to 10 Syllabus Content**
>
> ### 📍 Page 6
>
> 
> #### 🔹 1.8 SPAN Port (Port Mirroring)
> 
> 
> 
> #### 🔹 Switch Port Analyzer:
> 
> 
> SPAN Switched Port Analyzer) or port mirroring is a switch feature that: Mirrors traffic from one or more ports to a designated monitoring port Enables legitimate monitoring  Security monitoring and troubleshooting
> 
> 
> #### 🔹 Used by security teams  IDS/IPS deployment, packet capture
> 
> 
> 
> #### 🔹 Configuration Example Cisco):
> 
> 
> 
> #### 🔹 monitor session 1 source interface Gi0/1
> 
> 
> 
> #### 🔹 monitor session 1 destination interface Gi0/24
> 
> 
> 
> #### 🔹 1.9 Wiretapping
> 
> 
> 
> #### 🔹 Physical Interception:
> 
> 
> Wiretapping involves physically intercepting communications:
> 
> 
> #### 🔹 Physical tapping  Direct connection to cables
> 
> 
> 
> #### 🔹 Optical fiber taps  Beam splitters for fiber optic cables
> 
> 
> 
> #### 🔹 Network taps  Passive or active hardware taps
> 
> 
> 
> #### 🔹 Cable splitters  Y-splitters for Ethernet cables
> 
> 
> 
> #### 🔹 1.10 Lawful Interception
> 
> 
> 
> #### 🔹 Authorized Government Monitoring:
> 
> 
> Lawful interception is government-authorized communication monitoring for:
> 
> 
> #### 🔹 Intelligence gathering  National security purposes
> 
> 
> 
> #### 🔹 Criminal investigations  Law enforcement activities
> 
> 
> 
> #### 🔹 Regulatory requirements  Legal compliance CALEA in US
> 
> 
> 
> #### 🔹 Court-ordered surveillance  Warrant-based monitoring
> 
> 
> 
> #### 🔹 2. MAC Attacks
> 
>
> ---
>
> ### 📍 Page 7
>
> 
> #### 🔹 2.1 MAC Address Fundamentals
> 
> 
> 
> #### 🔹 MAC Address Media Access Control):
> 
> 
> 48-bit hardware address  Uniquely identifies network interface cards
> 
> 
> #### 🔹 Format: XXXXXXXXXXXX (hexadecimal)
> 
> 
> First 24 bits  Organizationally Unique Identifier OUI  manufacturer
> 
> 
> #### 🔹 Last 24 bits  Device-specific identifier
> 
> 
> 
> #### 🔹 2.2 CAM Table
> 
> 
> 
> #### 🔹 Content Addressable Memory Table:
> 
> 
> 
> #### 🔹 Switches use CAM tables to:
> 
> 
> 
> #### 🔹 Map MAC addresses to physical ports
> 
> 
> Make forwarding decisions  Send traffic only to destination port
> 
> 
> #### 🔹 Enable switching  Prevent unnecessary traffic flooding
> 
> 
> 
> #### 🔹 Maintain efficiency  Fast lookup and forwarding
> 
> 
> 
> #### 🔹 CAM Table Structure:
> 
> 
> 
> #### 🔹 MAC Address
> 
> 
> 
> #### 🔹 Port Number
> 
> 
> 
> #### 🔹 VLAN ID
> 
> 
> 
> #### 🔹 Timestamp (for aging)
> 
> 
> 
> #### 🔹 2.3 How CAM Works
> 
> 
> 
> #### 🔹 Normal Switch Operation:
> 
> 
>  Learning  Switch learns MAC addresses from source addresses of
> 
> 
> #### 🔹 incoming frames
> 
> 
> 
> #### 🔹  Storing  MAC-to-port mappings stored in CAM table
> 
> 
> 
> #### 🔹  Forwarding  Frames forwarded only to destination port
> 
> 
> 
> #### 🔹  Aging  Old entries removed after timeout period
> 
> 
> 
> #### 🔹 Dynamic Entry Management:
> 
> 
> 
> #### 🔹 Entries added automatically as traffic flows
> 
>
> ---
>
> ### 📍 Page 8
>
> 
> #### 🔹 Timeout typically 300 seconds 5 minutes)
> 
> 
> 
> #### 🔹 Refresh on each packet from that MAC
> 
> 
> 
> #### 🔹 2.4 CAM Table Overflow Attack
> 
> 
> 
> #### 🔹 What Happens When CAM Table is Full:
> 
> 
> 
> #### 🔹 When the CAM table reaches capacity:
> 
> 
> 
> #### 🔹 Fail-open mode  Switch behaves like a hub
> 
> 
> 
> #### 🔹 Floods all packets  Broadcasts to all ports
> 
> 
> 
> #### 🔹 Enables passive sniffing  All traffic visible to attackers
> 
> 
> 
> #### 🔹 Security bypass  Circumvents switch security
> 
> 
> 
> #### 🔹 2.5 MAC Flooding
> 
> 
> 
> #### 🔹 💥MAC Flooding Attack
> 
> 
> 
> #### 🔹 Attackers send thousands of frames with random fake MAC
> 
> 
> addresses to overflow the CAM table, forcing the switch into fail-open mode where it broadcasts all traffic.
> 
> 
> #### 🔹 Attack Process:
> 
> 
> 
> #### 🔹  Send large volume of frames with spoofed source MACs
> 
> 
> 
> #### 🔹  Fill CAM table with fake entries
> 
> 
> 
> #### 🔹  Switch enters fail-open mode
> 
> 
> 
> #### 🔹  All traffic broadcast to all ports
> 
> 
> 
> #### 🔹  Attacker can sniff all traffic
> 
> 
> 
> #### 🔹 Tools:
> 
> 
> 
> #### 🔹 macof (dsniff suite)
> 
> 
> 
> #### 🔹 Yersinia
> 
> 
> 
> #### 🔹 Ettercap
> 
> 
> 
> #### 🔹 2.6 Switch Port Stealing
> 
>
> ---
>
> ### 📍 Page 9
>
> 
> #### 🔹 Traffic Redirection Attack:
> 
> 
> 
> #### 🔹 Attacker sends frames with victim's MAC address as source:
> 
> 
> 
> #### 🔹 Binds victim MAC to attacker's port in CAM table
> 
> 
> 
> #### 🔹 Redirects traffic intended for victim to attacker
> 
> 
> 
> #### 🔹 Hijacks connections  Intercepts victim's traffic
> 
> 
> 
> #### 🔹 Enables MITM attacks  Position between victim and gateway
> 
> 
> 
> #### 🔹 2.7 Defending Against MAC Attacks
> 
> 
> 
> #### 🔹 Security Measures:
> 
> 
> 
> #### 🔹 Port Security
> 
> 
> 
> #### 🔹 switchport port-security
> 
> 
> 
> #### 🔹 switchport port-security maximum 2
> 
> 
> 
> #### 🔹 switchport port-security violation restrict
> 
> 
> 
> #### 🔹 switchport port-security mac-address sticky
> 
> 
> 
> #### 🔹 Additional Defenses:
> 
> 
> 
> #### 🔹 802.1X authentication  Network access control
> 
> 
> 
> #### 🔹 Dynamic ARP Inspection DAI  Validate ARP packets
> 
> 
> 
> #### 🔹 DHCP Snooping  Prevent rogue DHCP servers
> 
> 
> 
> #### 🔹 Use managed switches  Enterprise-grade equipment
> 
> 
> 
> #### 🔹 Disable unused ports  Reduce attack surface
> 
> 
> 
> #### 🔹 Monitor for anomalies  Detect MAC flooding attempts
> 
> 
> 
> #### 🔹 3. DHCP Attacks
> 
> 
> 
> #### 🔹 3.1 How DHCP Works
> 
> 
> 
> #### 🔹 DORA Process:
> 
>
> ---
>
> ### 📍 Page 10
>
> 
> #### 🔹 🔄DHCP Four-Step Process
> 
> 
> 
> #### 🔹  Discovery  Client broadcasts DHCPDISCOVER
> 
> 
> 
> #### 🔹  Offer  Server responds with DHCPOFFER
> 
> 
> 
> #### 🔹  Request  Client sends DHCPREQUEST
> 
> 
> 
> #### 🔹  Acknowledgment  Server confirms with DHCPACK
> 
> 
> 
> #### 🔹 Configuration Provided:
> 
> 
> 
> #### 🔹 IP address
> 
> 
> 
> #### 🔹 Subnet mask
> 
> 
> 
> #### 🔹 Default gateway
> 
> 
> 
> #### 🔹 DNS servers
> 
> 
> 
> #### 🔹 Lease time
> 
> 
> 
> #### 🔹 3.2 DHCP Messages and Packet Format
> 
> 
> 
> #### 🔹 IPv4 DHCP Packet Structure:
> 
> 
> 
> #### 🔹 op  Operation code 1=request, 2=reply)
> 
> 
> 
> #### 🔹 htype  Hardware type 1Ethernet)
> 
> 
> 
> #### 🔹 hlen  Hardware address length
> 
> 
> 
> #### 🔹 hops  Relay agent hops
> 
> 
> 
> #### 🔹 xid  Transaction ID (random number)
> 
> 
> 
> #### 🔹 secs  Seconds elapsed
> 
> 
> 
> #### 🔹 flags  Broadcast flag
> 
> 
> 
> #### 🔹 ciaddr  Client IP address
> 
> 
> 
> #### 🔹 yiaddr  Your (client) IP address
> 
> 
> 
> #### 🔹 siaddr  Server IP address
> 
> 
> 
> #### 🔹 giaddr  Gateway IP address
> 
> 
> 
> #### 🔹 chaddr  Client hardware address
> 
>
> ---
>

> [!NOTE]- 📄 **Pages 11 to 15 Syllabus Content**
>
> ### 📍 Page 11
>
> 
> #### 🔹 sname  Server hostname
> 
> 
> 
> #### 🔹 file  Boot filename
> 
> 
> 
> #### 🔹 options  DHCP options (message type, lease time, etc.)
> 
> 
> 
> #### 🔹 3.3 DHCP Starvation Attack
> 
> 
> 
> #### 🔹 🚫DHCP Starvation
> 
> 
> Attacker floods DHCP server with DHCPDISCOVER messages using spoofed MAC addresses, exhausting the IP address pool so legitimate users cannot obtain IP addresses.
> 
> 
> #### 🔹 Attack Process:
> 
> 
> 
> #### 🔹  Send thousands of DHCPDISCOVER messages
> 
> 
> 
> #### 🔹  Use different spoofed MAC addresses for each
> 
> 
> 
> #### 🔹  Exhaust DHCP pool
> 
> 
> 
> #### 🔹  Legitimate users cannot get IP addresses
> 
> 
> 
> #### 🔹  Denial of service condition
> 
> 
> 
> #### 🔹 Tools:
> 
> 
> 
> #### 🔹 Yersinia
> 
> 
> 
> #### 🔹 DHCPig
> 
> 
> 
> #### 🔹 Gobbler
> 
> 
> 
> #### 🔹 3.4 Rogue DHCP Server Attack
> 
> 
> 
> #### 🔹 Malicious DHCP Server:
> 
> 
> 
> #### 🔹 Attacker sets up unauthorized DHCP server to:
> 
> 
> Provide fake gateway address  Redirect traffic through attacker
> 
> 
> #### 🔹 Provide fake DNS servers  Enable DNS poisoning
> 
> 
> 
> #### 🔹 Launch MITM attacks  Intercept all client traffic
> 
> 
> 
> #### 🔹 Redirect web traffic  Phishing and credential theft
> 
> 
> 
> #### 🔹 Attack Scenario:
> 
>
> ---
>
> ### 📍 Page 12
>
> 
> #### 🔹  Deploy rogue DHCP server
> 
> 
> 
> #### 🔹  Respond to DHCPDISCOVER faster than legitimate server
> 
> 
> 
> #### 🔹  Clients receive malicious configuration
> 
> 
> 
> #### 🔹  Traffic routes through attacker
> 
> 
> 
> #### 🔹 3.5 DHCP Attack Tools
> 
> 
> 
> #### 🔹 Offensive Tools:
> 
> 
> 
> #### 🔹 Yersinia  Comprehensive Layer 2 attack framework
> 
> 
> 
> #### 🔹 Gobbler  DHCP exhaustion tool
> 
> 
> 
> #### 🔹 DHCPig  DHCP starvation tool
> 
> 
> Metasploit auxiliary modules  DHCP reconnaissance and attacks
> 
> 
> #### 🔹 3.6 Defending Against DHCP Attacks
> 
> 
> 
> #### 🔹 Protection Mechanisms:
> 
> 
> 
> #### 🔹 DHCP Snooping
> 
> 
> 
> #### 🔹 ip dhcp snooping
> 
> 
> 
> #### 🔹 ip dhcp snooping vlan 10
> 
> 
> 
> #### 🔹 ip dhcp snooping trust (on uplink ports)
> 
> 
> 
> #### 🔹 Validates DHCP messages
> 
> 
> 
> #### 🔹 Builds binding table IPMACPort-VLAN
> 
> 
> 
> #### 🔹 Prevents rogue DHCP servers
> 
> 
> 
> #### 🔹 Additional Protections:
> 
> 
> 
> #### 🔹 IP Source Guard  Prevents IP spoofing
> 
> 
> Dynamic ARP Inspection  Works with DHCP snooping binding table
> 
> 
> #### 🔹 Rate limiting  Limit DHCP messages per port
> 
> 
> 
> #### 🔹 Port security  Limit MAC addresses per port
> 
> 
> 
> #### 🔹 Monitor DHCP traffic  Alert on anomalies
> 
>
> ---
>
> ### 📍 Page 13
>
> 
> #### 🔹 4. ARP Poisoning
> 
> 
> 
> #### 🔹 4.1 What is ARP?
> 
> 
> 
> #### 🔹 Address Resolution Protocol:
> 
> 
> 
> #### 🔹 🔗ARP Purpose
> 
> 
> ARP maps IP addresses to MAC addresses on local networks. When a device needs to communicate with an IP address on the same subnet, it uses ARP to discover the corresponding MAC address.
> 
> 
> #### 🔹 ARP Characteristics:
> 
> 
> 
> #### 🔹 Stateless protocol  No verification of responses
> 
> 
> 
> #### 🔹 Broadcast-based  ARP requests sent to all hosts
> 
> 
> 
> #### 🔹 Cache-based  Mappings stored in ARP cache
> 
> 
> 
> #### 🔹 No authentication  Easy to spoof
> 
> 
> Critical for local networking  Required for Layer 2 communication
> 
> 
> #### 🔹 4.2 ARP Spoofing Attack
> 
> 
> 
> #### 🔹 ARP Cache Poisoning:
> 
> 
> 
> #### 🔹 Attacker sends forged ARP replies to victims:
> 
> 
> Fake MAC-to-IP mappings  Associate attacker MAC with target IP
> 
> 
> #### 🔹 Poisons ARP cache  Victims store incorrect mappings
> 
> 
> Redirects traffic  Traffic intended for gateway goes to attacker Enables MITM  Attacker positioned between client and gateway
> 
> 
> #### 🔹 Attack Process:
> 
> 
> 
> #### 🔹  Attacker sends gratuitous ARP replies
> 
> 
> 
> #### 🔹  Claims to be the gateway (or another host)
> 
> 
> 
> #### 🔹  Victims update ARP cache with attacker's MAC
> 
> 
> 
> #### 🔹  Traffic flows through attacker
> 
>
> ---
>
> ### 📍 Page 14
>
> 
> #### 🔹  Attacker can inspect, modify, or forward traffic
> 
> 
> 
> #### 🔹 4.3 Threats of ARP Poisoning
> 
> 
> 
> #### 🔹 Attack Capabilities:
> 
> 
> 
> #### 🔹 Credential Theft
> 
> 
> 
> #### 🔹 Capture passwords transmitted over network
> 
> 
> 
> #### 🔹 Session Hijacking
> 
> 
> 
> #### 🔹 Steal session cookies and tokens
> 
> 
> 
> #### 🔹 DNS Spoofing
> 
> 
> 
> #### 🔹 Redirect DNS queries to malicious servers
> 
> 
> 
> #### 🔹 Traffic Manipulation
> 
> 
> 
> #### 🔹 Modify data in transit
> 
> 
> 
> #### 🔹 Man-in-the-Middle Attacks
> 
> 
> 
> #### 🔹 Full interception and control of communications
> 
> 
> 
> #### 🔹 SSL Stripping
> 
> 
> 
> #### 🔹 Downgrade HTTPS to HTTP
> 
> 
> 
> #### 🔹 4.4 ARP Spoofing Tools
> 
> 
> 
> #### 🔹 Popular Tools:
> 
> 
> 
> #### 🔹 Ettercap  Comprehensive MITM framework with GUI
> 
> 
> 
> #### 🔹 Cain & Abel  Windows-based ARP poisoning tool
> 
> 
> 
> #### 🔹 Bettercap  Modern, powerful network attack framework
> 
> 
> 
> #### 🔹 Arpspoof (dsniff suite)  Simple command-line ARP poisoning
> 
> 
> 
> #### 🔹 MITMf  Framework for MITM attacks
> 
> 
> 
> #### 🔹 Example (arpspoof):
> 
> 
> 
> #### 🔹 # Poison victim's cache (claim to be gateway)
> 
> 
> 
> #### 🔹 arpspoof -i eth0 -t 192.168.1.100 192.168.1.1
> 
> 
> 
> #### 🔹 # Poison gateway's cache (claim to be victim)
> 
> 
> 
> #### 🔹 arpspoof -i eth0 -t 192.168.1.1 192.168.1.100
> 
>
> ---
>
> ### 📍 Page 15
>
> 
> #### 🔹 # Enable IP forwarding
> 
> 
> 
> #### 🔹 echo 1  /proc/sys/net/ipv4/ip_forward
> 
> 
> 
> #### 🔹 4.5 Defending Against ARP Poisoning
> 
> 
> 
> #### 🔹 Mitigation Strategies:
> 
> 
> 
> #### 🔹 Static ARP Entries
> 
> 
> 
> #### 🔹 Manually configure ARP mappings (not scalable)
> 
> 
> 
> #### 🔹 arp -s 192.168.1.1 001122334455
> 
> 
> 
> #### 🔹 Dynamic ARP Inspection DAI
> 
> 
> 
> #### 🔹 Validates ARP packets against DHCP snooping bindings
> 
> 
> 
> #### 🔹 ip arp inspection vlan 10
> 
> 
> 
> #### 🔹 ip arp inspection validate src-mac dst-mac ip
> 
> 
> 
> #### 🔹 ARP Watch
> 
> 
> 
> #### 🔹 Monitor and alert on ARP changes
> 
> 
> 
> #### 🔹 Encryption
> 
> 
> 
> #### 🔹 Use HTTPS, SSH, VPN to protect data in transit
> 
> 
> 
> #### 🔹 Network Segmentation
> 
> 
> 
> #### 🔹 Limit broadcast domains to reduce attack scope
> 
> 
> 
> #### 🔹 4.6 DHCP Snooping + DAI on Cisco
> 
> 
> 
> #### 🔹 Integrated Protection:
> 
> 
> DHCP Snooping builds IPMACPort-VLAN binding table, which DAI uses to validate ARP packets.
> 
> 
> #### 🔹 Configuration:
> 
> 
> 
> #### 🔹 ! Enable DHCP Snooping
> 
> 
> 
> #### 🔹 ip dhcp snooping
> 
> 
> 
> #### 🔹 ip dhcp snooping vlan 10
> 
>
> ---
>

> [!NOTE]- 📄 **Pages 16 to 20 Syllabus Content**
>
> ### 📍 Page 16
>
> 
> #### 🔹 interface GigabitEthernet0/1
> 
> 
> 
> #### 🔹 ip dhcp snooping trust
> 
> 
> 
> #### 🔹 ! Enable Dynamic ARP Inspection
> 
> 
> 
> #### 🔹 ip arp inspection vlan 10
> 
> 
> 
> #### 🔹 interface GigabitEthernet0/1
> 
> 
> 
> #### 🔹 ip arp inspection trust
> 
> 
> 
> #### 🔹 4.7 ARP Spoofing Detection Tools
> 
> 
> 
> #### 🔹 Detection Solutions:
> 
> 
> 
> #### 🔹 XArp  Windows ARP monitoring and protection
> 
> 
> 
> #### 🔹 ARPWatch  Unix/Linux ARP monitoring daemon
> 
> 
> 
> #### 🔹 Arpalert  ARP anomaly detection
> 
> 
> 
> #### 🔹 Arpwatch  Monitors ARP activity and reports changes
> 
> 
> 
> #### 🔹 Wireshark  Manual analysis of gratuitous ARP packets
> 
> 
> 
> #### 🔹 5. Spoofing Attacks
> 
> 
> 
> #### 🔹 5.1 MAC Spoofing
> 
> 
> 
> #### 🔹 MAC Address Manipulation:
> 
> 
> 
> #### 🔹 Changing NIC MAC address to:
> 
> 
> 
> #### 🔹 Impersonate another device  Bypass MAC filtering
> 
> 
> 
> #### 🔹 Evade detection  Change identity
> 
> 
> 
> #### 🔹 Bypass network restrictions  MAC-based access control
> 
> 
> 
> #### 🔹 Reset bandwidth limits  ISP MAC-based throttling
> 
> 
> 
> #### 🔹 5.2 MAC Spoofing on Windows
> 
> 
> 
> #### 🔹 Methods:
> 
> 
> 
> #### 🔹 Device Manager Method:
> 
> 
> 
> #### 🔹  Device Manager  Network Adapters
> 
>
> ---
>
> ### 📍 Page 17
>
> 
> #### 🔹  Properties  Advanced Tab
> 
> 
> 
> #### 🔹  Network Address or Locally Administered Address
> 
> 
> 
> #### 🔹  Enter new MAC address
> 
> 
> 
> #### 🔹 Registry Method:
> 
> 
> 
> #### 🔹 Edit registry key:
> 
> 
> HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Class\4D36E
> 
> 
> #### 🔹 972E32511CEBFC108002BE10318\Interface]
> 
> 
> 
> #### 🔹 Add NetworkAddress value
> 
> 
> 
> #### 🔹 5.3 MAC Spoofing Tools
> 
> 
> 
> #### 🔹 Popular Tools:
> 
> 
> 
> #### 🔹 Technitium MAC Address Changer TMAC  Windows GUI tool
> 
> 
> 
> #### 🔹 Macchanger Linux)  Command-line MAC changing
> 
> 
> 
> #### 🔹 macchanger -r eth0  # Random MAC
> 
> 
> 
> #### 🔹 macchanger -m 001122334455 eth0  # Specific MAC
> 
> 
> 
> #### 🔹 SMAC  Windows MAC changer
> 
> 
> 
> #### 🔹 macshift — macOS MAC changing
> 
> 
> 
> #### 🔹 5.4 IRDP Spoofing
> 
> 
> 
> #### 🔹 ICMP Router Discovery Protocol:
> 
> 
> 
> #### 🔹 IRDP allows hosts to discover routers. Attackers can:
> 
> 
> Send fake router advertisements  Claim to be default gateway
> 
> 
> #### 🔹 Redirect traffic  Route through attacker system
> 
> 
> 
> #### 🔹 Launch MITM attacks  Intercept communications
> 
> 
> 
> #### 🔹 Mitigation:
> 
> 
> 
> #### 🔹 Disable IRDP on end hosts
> 
> 
> 
> #### 🔹 Use static routing
> 
>
> ---
>
> ### 📍 Page 18
>
> 
> #### 🔹 Implement router authentication
> 
> 
> 
> #### 🔹 5.5 VLAN Hopping
> 
> 
> 
> #### 🔹 🚀VLAN Hopping
> 
> 
> Attacks that allow an attacker to access traffic on VLANs that should be segmented and isolated.
> 
> 
> #### 🔹 Attack Techniques:
> 
> 
> 
> #### 🔹 Switch Spoofing
> 
> 
> 
> #### 🔹 Attacker negotiates trunk link with switch
> 
> 
> 
> #### 🔹 Sends DTP Dynamic Trunking Protocol) messages
> 
> 
> 
> #### 🔹 Switch converts port to trunk
> 
> 
> 
> #### 🔹 Attacker gains access to all VLANs
> 
> 
> 
> #### 🔹 Double Tagging
> 
> 
> 
> #### 🔹 Insert two VLAN tags in Ethernet frame
> 
> 
> 
> #### 🔹 First tag stripped by first switch
> 
> 
> 
> #### 🔹 Second tag used by next switch
> 
> 
> 
> #### 🔹 Packet routed to different VLAN
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
> #### 🔹 Manually configure trunk ports
> 
> 
> 
> #### 🔹 Use native VLAN other than VLAN 1
> 
> 
> 
> #### 🔹 Enable VLAN access control lists VACLs)
> 
> 
> 
> #### 🔹 5.6 STP Attack
> 
> 
> 
> #### 🔹 Spanning Tree Protocol Manipulation:
> 
> 
> 
> #### 🔹 STP prevents loops in switched networks. Attacks include:
> 
> 
> 
> #### 🔹 Root bridge manipulation  Claim to be root bridge
> 
>
> ---
>
> ### 📍 Page 19
>
> 
> #### 🔹 BPDU spoofing  Send forged Bridge Protocol Data Units
> 
> 
> 
> #### 🔹 Topology manipulation  Force suboptimal paths
> 
> 
> 
> #### 🔹 Impact:
> 
> 
> 
> #### 🔹 Redirect traffic
> 
> 
> 
> #### 🔹 Cause network instability
> 
> 
> 
> #### 🔹 Enable MITM attacks
> 
> 
> 
> #### 🔹 Mitigation:
> 
> 
> 
> #### 🔹 Enable BPDU Guard on access ports
> 
> 
> 
> #### 🔹 Enable Root Guard on designated ports
> 
> 
> 
> #### 🔹 Use STP authentication
> 
> 
> 
> #### 🔹 5.7 Defending Against Spoofing
> 
> 
> 
> #### 🔹 Comprehensive Defenses:
> 
> 
> 
> #### 🔹 VLAN Security:
> 
> 
> 
> #### 🔹 Disable trunking on access ports  Prevent switch spoofing
> 
> 
> 
> #### 🔹 Disable DTP  Manual trunk configuration only
> 
> 
> 
> #### 🔹 Use private VLANs  Isolate hosts within VLAN
> 
> 
> 
> #### 🔹 STP Protection:
> 
> 
> 
> #### 🔹 Enable BPDU Guard  Shutdown ports receiving BPDUs
> 
> 
> 
> #### 🔹 Enable Root Guard  Prevent inferior BPDUs
> 
> 
> 
> #### 🔹 Enable Loop Guard  Prevent loops from unidirectional links
> 
> 
> 
> #### 🔹 General Best Practices:
> 
> 
> 
> #### 🔹 Port security  Limit MAC addresses per port
> 
> 
> 
> #### 🔹 802.1X authentication  Network access control
> 
> 
> 
> #### 🔹 DHCP snooping  Validate DHCP messages
> 
> 
> 
> #### 🔹 Dynamic ARP Inspection  Validate ARP packets
> 
> 
> 
> #### 🔹 6. DNS Poisoning
> 
>
> ---
>
> ### 📍 Page 20
>
> 
> #### 🔹 6.1 DNS Poisoning Techniques
> 
> 
> 
> #### 🔹 🗺DNS Poisoning
> 
> 
> Attacks that corrupt DNS resolution to redirect users to malicious servers by manipulating DNS queries, responses, or cache entries.
> 
> 
> #### 🔹 Attack Types:
> 
> 
> 
> #### 🔹 DNS spoofing  Fake DNS responses
> 
> 
> DNS cache poisoning  Inject malicious entries into resolver cache
> 
> 
> #### 🔹 DNS hijacking  Compromise DNS servers or configurations
> 
> 
> Rogue DNS servers  Unauthorized DNS servers providing fake answers
> 
> 
> #### 🔹 6.2 Intranet DNS Spoofing
> 
> 
> 
> #### 🔹 Local Network Attack:
> 
> 
> 
> #### 🔹 On local networks, combined with MITM
> 
> 
> 
> #### 🔹  ARP poisoning  Position between victim and gateway
> 
> 
> 
> #### 🔹  Intercept DNS queries  Capture outgoing DNS requests
> 
> 
> 
> #### 🔹  Send fake DNS responses  Provide malicious IP addresses
> 
> 
> 
> #### 🔹  Redirect to phishing sites  Credential harvesting
> 
> 
> 
> #### 🔹 6.3 Internet DNS Spoofing
> 
> 
> 
> #### 🔹 Wide-Area Attack:
> 
> 
> 
> #### 🔹 Intercepting DNS over WAN
> 
> 
> Hijacking authoritative name servers  Compromise primary DNS
> 
> 
> #### 🔹 BGP hijacking  Redirect DNS traffic
> 
> 
> 
> #### 🔹 DNS resolver compromise  Attack recursive resolvers
> 
> 
> 
> #### 🔹 6.4 Proxy Server DNS Poisoning
> 
> 
> 
> #### 🔹 Proxy-Based Attack:
> 
> 
> 
> #### 🔹 Modify proxy settings or compromise proxy servers:
> 
>
> ---
>

> [!NOTE]- 📄 **Pages 21 to 25 Syllabus Content**
>
> ### 📍 Page 21
>
> 
> #### 🔹 Redirect DNS queries through malicious proxy
> 
> 
> 
> #### 🔹 Modify DNS responses in transit
> 
> 
> 
> #### 🔹 WPAD exploitation  Web Proxy Auto-Discovery poisoning
> 
> 
> 
> #### 🔹 6.5 DNS Cache Poisoning
> 
> 
> 
> #### 🔹 Kaminsky Attack:
> 
> 
> 
> #### 🔹 Inject malicious DNS entries into resolver cache:
> 
> 
> 
> #### 🔹  Send DNS query to target resolver
> 
> 
> 
> #### 🔹  Flood resolver with fake responses
> 
> 
> 
> #### 🔹  Guess transaction ID and source port
> 
> 
> 
> #### 🔹  If successful, malicious entry cached
> 
> 
> 
> #### 🔹  All subsequent queries return poisoned result
> 
> 
> 
> #### 🔹 Modern Mitigations:
> 
> 
> 
> #### 🔹 Source port randomization
> 
> 
> 
> #### 🔹 Transaction ID randomization
> 
> 
> 
> #### 🔹 DNSSEC validation
> 
> 
> 
> #### 🔹 6.6 DNS Poisoning Tools
> 
> 
> 
> #### 🔹 Attack Tools:
> 
> 
> 
> #### 🔹 dnsspoof (dsniff suite)  Forge DNS responses
> 
> 
> 
> #### 🔹 Ettercap  Integrated DNS spoofing plugin
> 
> 
> 
> #### 🔹 DNSChef  DNS proxy for malicious responses
> 
> 
> 
> #### 🔹 Bettercap  Modern DNS spoofing capabilities
> 
> 
> 
> #### 🔹 Example (dnsspoof):
> 
> 
> 
> #### 🔹 dnsspoof -i eth0 -f hosts.txt
> 
> 
> 
> #### 🔹 # hosts.txt contains:
> 
> 
> 
> #### 🔹 # target.com 192.168.1.50
> 
> 
> 
> #### 🔹 6.7 Defending Against DNS Spoofing
> 
>
> ---
>
> ### 📍 Page 22
>
> 
> #### 🔹 Protection Measures:
> 
> 
> 
> #### 🔹 DNSSEC DNS Security Extensions)
> 
> 
> 
> #### 🔹 Cryptographically sign DNS records
> 
> 
> 
> #### 🔹 Validate authenticity and integrity
> 
> 
> 
> #### 🔹 Prevent cache poisoning
> 
> 
> 
> #### 🔹 DNS over TLS DoT / DNS over HTTPS DoH
> 
> 
> 
> #### 🔹 Encrypt DNS queries
> 
> 
> 
> #### 🔹 Prevent interception and modification
> 
> 
> 
> #### 🔹 Port 853 DoT or HTTPS DoH
> 
> 
> 
> #### 🔹 Additional Protections:
> 
> 
> Secure recursive resolvers  Use trusted DNS servers 1.1.1.1, 8.8.8.8
> 
> 
> #### 🔹 Disable DNS recursion on authoritative servers
> 
> 
> 
> #### 🔹 Clear DNS cache regularly  Reduce poisoning window
> 
> 
> 
> #### 🔹 Deploy endpoint DNS filtering  Block malicious domains
> 
> 
> 
> #### 🔹 Monitor DNS traffic  Detect anomalies
> 
> 
> 
> #### 🔹 7. Sniffing Tools
> 
> 
> 
> #### 🔹 7.1 Wireshark
> 
> 
> 
> #### 🔹 🦈Wireshark
> 
> 
> The world's most popular network protocol analyzer. Free, open- source tool for packet capture and analysis with comprehensive protocol support.
> 
> 
> #### 🔹 Key Features:
> 
> 
> 
> #### 🔹 Deep protocol inspection
> 
> 
> 
> #### 🔹 Live capture and offline analysis
> 
> 
> 
> #### 🔹 Rich filtering capabilities
> 
>
> ---
>
> ### 📍 Page 23
>
> 
> #### 🔹 Protocol decryption WPA, SSL with keys)
> 
> 
> 
> #### 🔹 Export capabilities
> 
> 
> 
> #### 🔹 Cross-platform Windows, Linux, macOS
> 
> 
> 
> #### 🔹 Common Use Cases:
> 
> 
> 
> #### 🔹 Protocol analysis and troubleshooting
> 
> 
> 
> #### 🔹 Security analysis and incident investigation
> 
> 
> 
> #### 🔹 Network forensics
> 
> 
> 
> #### 🔹 Malware analysis
> 
> 
> 
> #### 🔹 Credential extraction
> 
> 
> 
> #### 🔹 7.2 Follow TCP Stream
> 
> 
> 
> #### 🔹 Stream Reconstruction:
> 
> 
> 
> #### 🔹 Wireshark can reassemble TCP streams to show:
> 
> 
> 
> #### 🔹 HTTP sessions  Complete web requests and responses
> 
> 
> 
> #### 🔹 Telnet sessions  Full terminal sessions with passwords
> 
> 
> 
> #### 🔹 FTP commands  File transfer commands and credentials
> 
> 
> 
> #### 🔹 Chat conversations  IRC, XMPP messages
> 
> 
> 
> #### 🔹 Email content  SMTP, POP3, IMAP messages
> 
> 
> 
> #### 🔹 Usage:
> 
> 
> 
> #### 🔹 Right-click packet  Follow  TCP Stream
> 
> 
> 
> #### 🔹 7.3 Display Filters
> 
> 
> 
> #### 🔹 Common Wireshark Filters:
> 
> 
> 
> #### 🔹 IP-based filters:
> 
> 
> ip.addr  192.168.1.10          # Traffic to/from specific IP
> 
> 
> #### 🔹 ip.src  192.168.1.10           # Source IP
> 
> 
> 
> #### 🔹 ip.dst  192.168.1.10           # Destination IP
> 
> 
> 
> #### 🔹 Protocol filters:
> 
>
> ---
>
> ### 📍 Page 24
>
> 
> #### 🔹 tcp.port  80                   # HTTP traffic
> 
> 
> 
> #### 🔹 tcp.port  443                  # HTTPS traffic
> 
> 
> 
> #### 🔹 udp                              # All UDP traffic
> 
> 
> 
> #### 🔹 dns                              # DNS queries/responses
> 
> 
> 
> #### 🔹 http                             # HTTP protocol
> 
> 
> 
> #### 🔹 arp                              # ARP traffic
> 
> 
> 
> #### 🔹 HTTP-specific:
> 
> 
> 
> #### 🔹 http.request                     # HTTP requests
> 
> 
> 
> #### 🔹 http.request.method == "POST"    # POST requests
> 
> 
> 
> #### 🔹 http.response.code  200        # Successful responses
> 
> 
> 
> #### 🔹 7.4 Additional Wireshark Filters
> 
> 
> 
> #### 🔹 Advanced Filtering:
> 
> 
> 
> #### 🔹 TCP Flags:
> 
> 
> 
> #### 🔹 tcp.flags.syn  1 && tcp.flags.ack  0    # SYN packets
> 
> 
> 
> #### 🔹 tcp.flags.reset  1                         # RST packets
> 
> 
> 
> #### 🔹 Credential Sniffing:
> 
> 
> ftp                              # FTP traffic (cleartext creds)
> 
> 
> #### 🔹 telnet                           # Telnet traffic
> 
> 
> 
> #### 🔹 smtp.auth                        # SMTP authentication
> 
> 
> 
> #### 🔹 http.authorization               # HTTP auth headers
> 
> 
> 
> #### 🔹 Network Mapping:
> 
> 
> 
> #### 🔹 icmp                             # ICMP traffic
> 
> 
> 
> #### 🔹 icmp.type  8                   # Ping requests
> 
> 
> 
> #### 🔹 Detection:
> 
> 
> 
> #### 🔹 dhcp                             # DHCP traffic
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
> #### 🔹 arp.duplicate-address-detected   # ARP conflicts
> 
> 
> 
> #### 🔹 7.5 Other Sniffing Tools
> 
> 
> 
> #### 🔹 Command-Line Tools:
> 
> 
> 
> #### 🔹 tcpdump
> 
> 
> 
> #### 🔹 Classic Unix packet sniffer
> 
> 
> 
> #### 🔹 tcpdump -i eth0 -w capture.pcap
> 
> 
> 
> #### 🔹 tcpdump -r capture.pcap 'port 80'
> 
> 
> 
> #### 🔹 tshark
> 
> 
> 
> #### 🔹 Wireshark's command-line version
> 
> 
> 
> #### 🔹 tshark -i eth0 -f "tcp port 80"
> 
> 
> 
> #### 🔹 Network Analysis Frameworks:
> 
> 
> 
> #### 🔹 Ettercap  Comprehensive MITM framework
> 
> 
> 
> #### 🔹 Bettercap  Modern network attack framework
> 
> 
> 
> #### 🔹 Kismet  Wireless network detector and sniffer
> 
> 
> 
> #### 🔹 Commercial Tools:
> 
> 
> 
> #### 🔹 OmniPeek  Enterprise packet analyzer
> 
> 
> 
> #### 🔹 SolarWinds Network Performance Monitor
> 
> 
> 
> #### 🔹 IDS/IPS
> 
> 
> 
> #### 🔹 Snort  Network intrusion detection
> 
> 
> 
> #### 🔹 Suricata  IDS/IPS engine
> 
> 
> 
> #### 🔹 8. Sniffing Countermeasures
> 
> 
> 
> #### 🔹 8.1 How to Defend Against Sniffing
> 
>
> ---
>

> [!NOTE]- 📄 **Pages 26 to 29 Syllabus Content**
>
> ### 📍 Page 26
>
> 
> #### 🔹 🛡Defense Strategy
> 
> 
> Protecting against sniffing requires a combination of encryption, secure protocols, network segmentation, and monitoring.
> 
> 
> #### 🔹 Primary Defenses:
> 
> 
> 
> #### 🔹 Use Encrypted Protocols:
> 
> 
> 
> #### 🔹 HTTPS instead of HTTP
> 
> 
> 
> #### 🔹 SSH instead of Telnet
> 
> 
> 
> #### 🔹 SFTP/SCP instead of FTP
> 
> 
> 
> #### 🔹 IMAPS/POP3S instead of IMAP/POP3
> 
> 
> 
> #### 🔹 VPN for remote access
> 
> 
> 
> #### 🔹 Secure Wi-Fi:
> 
> 
> 
> #### 🔹 WPA3  Latest Wi-Fi security
> 
> 
> 
> #### 🔹 WPA2 Enterprise with 802.1X
> 
> 
> 
> #### 🔹 Strong passphrases
> 
> 
> 
> #### 🔹 Disable WPS
> 
> 
> 
> #### 🔹 Network Architecture:
> 
> 
> 
> #### 🔹 Network segmentation  VLANs and subnets
> 
> 
> 
> #### 🔹 Micro-segmentation  Isolate critical assets
> 
> 
> 
> #### 🔹 Zero Trust architecture  Never trust, always verify
> 
> 
> 
> #### 🔹 Layer 2 Security:
> 
> 
> 
> #### 🔹 Port security  Limit MAC addresses
> 
> 
> 
> #### 🔹 DHCP snooping  Prevent rogue DHCP
> 
> 
> 
> #### 🔹 Dynamic ARP Inspection  Validate ARP
> 
> 
> 
> #### 🔹 802.1X  Network access control
> 
> 
> 
> #### 🔹 Monitoring:
> 
> 
> 
> #### 🔹 Anti-sniffing tools  Detect promiscuous NICs
> 
> 
> 
> #### 🔹 IDS/IPS  Detect attack patterns
> 
>
> ---
>
> ### 📍 Page 27
>
> 
> #### 🔹 SIEM  Correlate security events
> 
> 
> 
> #### 🔹 8.2 How to Detect Sniffing
> 
> 
> 
> #### 🔹 Detection Indicators:
> 
> 
> 
> #### 🔹 ARP Monitoring
> 
> 
> 
> #### 🔹 Unusual ARP traffic patterns
> 
> 
> 
> #### 🔹 Gratuitous ARP packets
> 
> 
> 
> #### 🔹 ARP cache inconsistencies
> 
> 
> 
> #### 🔹 DNS Anomalies
> 
> 
> 
> #### 🔹 DNS responses without queries
> 
> 
> 
> #### 🔹 Multiple answers for same query
> 
> 
> 
> #### 🔹 Unusual TTL values
> 
> 
> 
> #### 🔹 Promiscuous Mode Detection
> 
> 
> 
> #### 🔹 NICs in promiscuous mode accept all packets
> 
> 
> 
> #### 🔹 Can be detected through various techniques
> 
> 
> 
> #### 🔹 Network Behavior:
> 
> 
> 
> #### 🔹 Unusual traffic patterns
> 
> 
> 
> #### 🔹 Unexpected MAC addresses
> 
> 
> 
> #### 🔹 Latency increases (due to MITM
> 
> 
> 
> #### 🔹 8.3 Sniffer Detection Techniques
> 
> 
> 
> #### 🔹 Detection Methods:
> 
> 
> 
> #### 🔹 ARP Probe Method
> 
> 
> 
> #### 🔹 Send non-broadcast ARP packets to specific host
> 
> 
> 
> #### 🔹 Normal NIC ignores (not its MAC
> 
> 
> 
> #### 🔹 Promiscuous NIC processes and may respond
> 
> 
> 
> #### 🔹 DNS Probe Method
> 
> 
> 
> #### 🔹 Send DNS queries with fake destination MAC
> 
> 
> 
> #### 🔹 Only promiscuous NICs process
> 
>
> ---
>
> ### 📍 Page 28
>
> 
> #### 🔹 Monitor for anomalous DNS traffic
> 
> 
> 
> #### 🔹 ICMP Probe Method
> 
> 
> 
> #### 🔹 Send ICMP packets with wrong MAC address
> 
> 
> 
> #### 🔹 Promiscuous NIC processes
> 
> 
> 
> #### 🔹 May generate responses
> 
> 
> 
> #### 🔹 Response Time Analysis
> 
> 
> 
> #### 🔹 Sniffing and forwarding adds latency
> 
> 
> 
> #### 🔹 Measure round-trip times for anomalies
> 
> 
> 
> #### 🔹 Crafted Packet Test
> 
> 
> 
> #### 🔹 Send packets with specific characteristics
> 
> 
> 
> #### 🔹 Monitor for unexpected processing
> 
> 
> 
> #### 🔹 8.4 Promiscuous Mode Detection Tools
> 
> 
> 
> #### 🔹 Detection Software:
> 
> 
> 
> #### 🔹 Nmap Script
> 
> 
> 
> #### 🔹 nmap --script=sniffer-detect 192.168.1.0/24
> 
> 
> 
> #### 🔹 Promiscan
> 
> 
> 
> #### 🔹 Detects promiscuous interfaces on local network
> 
> 
> 
> #### 🔹 AntiSniff
> 
> 
> 
> #### 🔹 Tests for promiscuous mode using various techniques
> 
> 
> 
> #### 🔹 Sniffdet
> 
> 
> 
> #### 🔹 Remote sniffer detector for Unix systems
> 
> 
> 
> #### 🔹 Sentinel
> 
> 
> 
> #### 🔹 Monitors for ARP and DNS anomalies
> 
> 
> 
> #### 🔹 NEPED Network Promiscuous Ethernet Detector)
> 
> 
> 
> #### 🔹 Windows-based detection tool
> 
>
> ---
>
> ### 📍 Page 29
>
> 
> #### 🔹 ✅Module Summary
> 
> 
> This module covered comprehensive network sniffing concepts and
> 
> 
> #### 🔹 techniques:
> 
> 
> 
> #### 🔹 Key Takeaways:
> 
> 
> 
> #### 🔹 Sniffing Fundamentals  Passive vs. active sniffing,
> 
> 
> 
> #### 🔹 promiscuous mode, vulnerable protocols
> 
> 
> 
> #### 🔹 MAC Attacks  MAC flooding, switch port stealing, CAM table
> 
> 
> 
> #### 🔹 attacks
> 
> 
> 
> #### 🔹 DHCP Attacks  DHCP starvation, rogue DHCP servers
> 
> 
> 
> #### 🔹 ARP Poisoning  Cache poisoning, MITM attacks, traffic
> 
> 
> 
> #### 🔹 redirection
> 
> 
> 
> #### 🔹 Spoofing Techniques  MAC spoofing, VLAN hopping, STP
> 
> 
> 
> #### 🔹 attacks
> 
> 
> 
> #### 🔹 DNS Poisoning  Cache poisoning, DNS spoofing, DNSSEC
> 
> 
> 
> #### 🔹 Sniffing Tools  Wireshark, tcpdump, Ettercap, filtering
> 
> 
> 
> #### 🔹 techniques
> 
> 
> 
> #### 🔹 Countermeasures  Encryption, port security, DAI, DHCP
> 
> 
> 
> #### 🔹 snooping, detection methods
> 
> 
> Network sniffing remains a fundamental attack technique. Defense requires encryption, secure network architecture, Layer 2 security controls, and continuous monitoring for anomalous activity.
>
> ---
>
