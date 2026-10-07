# 📜 07. Full PDF Reference — Enumeration

> [!INFO] 🏛️ **Official CEH v13 PDF Source Master Repository**
> Cleaned, high-readability technical text extraction directly from official CEH v13 Syllabus PDF (`CEH_v13__Module_04_Enumeration.pdf`). Formatted as structured Markdown prose with proper paragraphs, section headers, and key term highlights.

---

## 📊 Syllabus Metadata & Source Breakdown

> [!ABSTRACT] 📋 **Comprehensive PDF Syllabus Metadata Reference Matrix**

| Metadata Attribute | Syllabus Parameter Value |
| :--- | :--- |
| **Course Module** | **Module 04: Enumeration** |
| **Source PDF File** | `CEH_v13__Module_04_Enumeration.pdf` |
| **Total Extracted Pages** | `39 Pages` |
| **Formatting Standard** | Ultra-Readable Markdown Prose & Structured Headings |
| **Extraction Status** | 100% Complete / Verified Text Flow |

---

## 📑 Structured & Readable Syllabus Reference

> [!NOTE]- 📄 **Pages 1 to 5 Syllabus Content**
>
> ### 📍 Page 1
>
> 
> #### 🔹 🔬
> 
> 
> 
> #### 🔹 Enumeration
> 
> 
> 
> #### 🔹 Enumeration
> 
> 
> 
> #### 🔹 📋Module Overview
> 
> 
> This module covers enumeration techniques for extracting detailed information from target systems through active interaction. Topics
> 
> 
> #### 🔹 include NetBIOS, SNMP, LDAP, NTP, NFS, SMTP, DNS, SMB, RPC,
> 
> 
> VoIP, and IPsec enumeration, along with defensive countermeasures.
> 
> 
> #### 🔹 1. Enumeration Concepts
> 
> 
> 
> #### 🔹 1.1 What is Enumeration?
> 
> 
> 
> #### 🔹 🎯Definition
> 
> 
> Enumeration is the active process of extracting detailed information from target systems through direct interaction. Unlike reconnaissance
> 
> 
> #### 🔹 (passive) and scanning (semi-active), enumeration requires
> 
> 
> established connections and queries to target services.
> 
> 
> #### 🔹 Information Gathered Through Enumeration
> 
> 
> 
> #### 🔹 User and Group Information:
> 
> 
> 
> #### 🔹 Usernames and account details
> 
> 
> 
> #### 🔹 Group memberships and hierarchies
> 
>
> ---
>
> ### 📍 Page 2
>
> 
> #### 🔹 User privileges and permissions
> 
> 
> 
> #### 🔹 Password policies and requirements
> 
> 
> 
> #### 🔹 Network Resources:
> 
> 
> 
> #### 🔹 Shared folders and drives
> 
> 
> 
> #### 🔹 Network printers and devices
> 
> 
> 
> #### 🔹 Available services and applications
> 
> 
> 
> #### 🔹 Active sessions and connections
> 
> 
> 
> #### 🔹 System Information:
> 
> 
> 
> #### 🔹 Operating system versions and patch levels
> 
> 
> 
> #### 🔹 Server banners and service versions
> 
> 
> 
> #### 🔹 Routing tables and network topology
> 
> 
> 
> #### 🔹 SNMP data and MIB information
> 
> 
> 
> #### 🔹 System configuration details
> 
> 
> 
> #### 🔹 Policy Information:
> 
> 
> 
> #### 🔹 Security policies and configurations
> 
> 
> 
> #### 🔹 Domain policies and trust relationships
> 
> 
> 
> #### 🔹 Access control lists ACLs)
> 
> 
> 
> #### 🔹 Authentication mechanisms
> 
> 
> 
> #### 🔹 1.2 Techniques for Enumeration
> 
> 
> 
> #### 🔹 Common Enumeration Techniques
> 
> 
> 
> #### 🔹 NetBIOS Enumeration
> 
> 
> 
> #### 🔹 Extracting Windows networking information via ports 137139
> 
> 
> 
> #### 🔹 SNMP Enumeration
> 
> 
> 
> #### 🔹 Querying network device management information
> 
> 
> 
> #### 🔹 LDAP Queries
> 
> 
> Enumerating Active Directory users, groups, and organizational units
> 
> 
> #### 🔹 SMB Enumeration
> 
>
> ---
>
> ### 📍 Page 3
>
> Identifying shares, users, and system information via Server Message Block
> 
> 
> #### 🔹 NFS Exports Enumeration
> 
> 
> 
> #### 🔹 Discovering Unix/Linux shared file systems
> 
> 
> 
> #### 🔹 DNS Zone Transfers
> 
> 
> 
> #### 🔹 Attempting to retrieve complete DNS zone files
> 
> 
> 
> #### 🔹 SMTP Enumeration
> 
> 
> 
> #### 🔹 Validating email addresses using VRFY and EXPN commands
> 
> 
> 
> #### 🔹 SNMP MIB Walking
> 
> 
> 
> #### 🔹 Systematically querying Management Information Base objects
> 
> 
> 
> #### 🔹 RPC Enumeration
> 
> 
> 
> #### 🔹 Identifying Remote Procedure Call services and endpoints
> 
> 
> 
> #### 🔹 VoIP and SIP Enumeration
> 
> 
> 
> #### 🔹 Discovering Voice over IP infrastructure and extensions
> 
> 
> 
> #### 🔹 OS Banner Grabbing
> 
> 
> 
> #### 🔹 Collecting service banners revealing software versions
> 
> 
> 
> #### 🔹 IPsec Enumeration
> 
> 
> 
> #### 🔹 Identifying VPN endpoints and security associations
> 
> 
> 
> #### 🔹 Active Directory Enumeration
> 
> 
> 
> #### 🔹 Comprehensive AD structure and object discovery
> 
> 
> 
> #### 🔹 1.3 Services and Ports to Enumerate
> 
> 
> 
> #### 🔹 Enumeration Target Reference
> 
> 
> 
> #### 🔹 Service Port(s) Protocol Purpose
> 
> 
> 
> #### 🔹 DNS 53 TCP/UDP Zone transfers, DNS records
> 
> 
> 
> #### 🔹 SMB/NetBIOS 139, 445 TCP Users, shares, OS information
> 
> 
> 
> #### 🔹 SNMP 161 UDP MIB information, system details
> 
> 
> 
> #### 🔹 LDAP 389, 636 TCP AD users, groups, organizational
> 
> 
> 
> #### 🔹 units
> 
> 
> 
> #### 🔹 SMTP 25, 587 TCP User validation, email
> 
> 
> 
> #### 🔹 enumeration
> 
>
> ---
>
> ### 📍 Page 4
>
> 
> #### 🔹 Service Port(s) Protocol Purpose
> 
> 
> 
> #### 🔹 RPC 135, 111 TCP Service listing, endpoint mapping
> 
> 
> 
> #### 🔹 NTP 123 UDP Time synchronization, system info
> 
> 
> 
> #### 🔹 NFS 2049 TCP Exported file shares
> 
> 
> 
> #### 🔹 SIP/VoIP 5060, 5061 TCP/UDP Extensions, server information
> 
> 
> 
> #### 🔹 IPsec 500, 4500 UDP VPN endpoints, security policies
> 
> 
> 
> #### 🔹 FTP 21 TCP Anonymous access, file listings
> 
> 
> 
> #### 🔹 SSH 22 TCP Supported authentication
> 
> 
> 
> #### 🔹 methods
> 
> 
> 
> #### 🔹 Telnet 23 TCP Banner grabbing, system info
> 
> 
> 
> #### 🔹 2. NetBIOS Enumeration
> 
> 
> 
> #### 🔹 🪟NetBIOS Overview
> 
> 
> NetBIOS Network Basic Input/Output System) provides information
> 
> 
> #### 🔹 about Windows systems via ports 137 (name service), 138
> 
> 
> (datagram), and 139 (session).
> 
> 
> #### 🔹 2.1 NetBIOS Enumeration Tools
> 
> 
> 
> #### 🔹 Built-In Windows Tools
> 
> 
> 
> #### 🔹 nbtstat
> 
> 
> 
> #### 🔹 Windows built-in NetBIOS statistics tool
> 
> 
> 
> #### 🔹 nbtstat A <target_ip>
> 
> 
> 
> #### 🔹 nbtstat -n
> 
> 
> 
> #### 🔹 Net Commands
> 
> 
> 
> #### 🔹 Windows networking commands
> 
> 
> 
> #### 🔹 net view \\<target_ip>
> 
> 
> 
> #### 🔹 net use
> 
>
> ---
>
> ### 📍 Page 5
>
> 
> #### 🔹 net user /domain
> 
> 
> 
> #### 🔹 net group /domain
> 
> 
> 
> #### 🔹 Third-Party Tools
> 
> 
> 
> #### 🔹 NetBIOS Enumerator
> 
> 
> 
> #### 🔹 GUI-based NetBIOS information extraction
> 
> 
> 
> #### 🔹 nbtscan
> 
> 
> 
> #### 🔹 Fast NetBIOS name scanner
> 
> 
> 
> #### 🔹 nbtscan 192.168.1.0/24
> 
> 
> 
> #### 🔹 Hyena
> 
> 
> 
> #### 🔹 Comprehensive Windows network management tool
> 
> 
> 
> #### 🔹 enum4linux
> 
> 
> 
> #### 🔹 Linux tool for enumerating Windows systems
> 
> 
> 
> #### 🔹 enum4linux -a <target_ip>
> 
> 
> 
> #### 🔹 2.2 Enumerating User Accounts
> 
> 
> 
> #### 🔹 User Enumeration Methods
> 
> 
> 
> #### 🔹 Domain User Enumeration
> 
> 
> 
> #### 🔹 net user /domain
> 
> 
> 
> #### 🔹 net group "Domain Admins" /domain
> 
> 
> 
> #### 🔹 net group "Domain Users" /domain
> 
> 
> 
> #### 🔹 Local User Enumeration
> 
> 
> 
> #### 🔹 net user
> 
> 
> 
> #### 🔹 net localgroup administrators
> 
> 
> 
> #### 🔹 Using nbtstat
> 
>
> ---
>

> [!NOTE]- 📄 **Pages 6 to 10 Syllabus Content**
>
> ### 📍 Page 6
>
> 
> #### 🔹 nbtstat A <target_ip>
> 
> 
> 
> #### 🔹 Reveals:
> 
> 
> 
> #### 🔹 Computer name
> 
> 
> 
> #### 🔹 Domain/Workgroup
> 
> 
> 
> #### 🔹 Logged-in users
> 
> 
> 
> #### 🔹 Services running
> 
> 
> 
> #### 🔹 Using enum4linux
> 
> 
> 
> #### 🔹 enum4linux U <target_ip>  # Users
> 
> 
> 
> #### 🔹 enum4linux G <target_ip>  # Groups
> 
> 
> 
> #### 🔹 enum4linux S <target_ip>  # Shares
> 
> 
> 
> #### 🔹 2.3 Enumerating Shared Resources Using Net View
> 
> 
> 
> #### 🔹 Share Enumeration
> 
> 
> 
> #### 🔹 Basic Net View
> 
> 
> 
> #### 🔹 net view \\<target_ip>
> 
> 
> 
> #### 🔹 Information Extracted:
> 
> 
> 
> #### 🔹 Shared folders and drives
> 
> 
> 
> #### 🔹 Shared printers
> 
> 
> 
> #### 🔹 Administrative shares C$, ADMIN$, IPC$
> 
> 
> 
> #### 🔹 Hidden shares (ending with $
> 
> 
> 
> #### 🔹 Advanced Share Enumeration
> 
> 
> 
> #### 🔹 # Using smbclient
> 
> 
> 
> #### 🔹 smbclient L //<target_ip> N
> 
> 
> 
> #### 🔹 # Using crackmapexec
> 
> 
> 
> #### 🔹 crackmapexec smb <target_ip> --shares
> 
>
> ---
>
> ### 📍 Page 7
>
> 
> #### 🔹 2.4 NetBIOS Enumeration Using AI
> 
> 
> 
> #### 🔹 AI enhances NetBIOS enumeration:
> 
> 
> 
> #### 🔹 AI Capabilities
> 
> 
> 
> #### 🔹 Automated Scan Orchestration
> 
> 
> 
> #### 🔹 Intelligently sequencing NetBIOS enumeration steps
> 
> 
> 
> #### 🔹 Share List Parsing
> 
> 
> Automatically categorizing and prioritizing discovered shares
> 
> 
> #### 🔹 Attack Path Mapping
> 
> 
> 
> #### 🔹 Mapping network names to potential exploitation routes
> 
> 
> 
> #### 🔹 Public SMB Share Detection
> 
> 
> 
> #### 🔹 Identifying publicly accessible shares with sensitive data
> 
> 
> 
> #### 🔹 Permission Risk Scoring
> 
> 
> Scoring share permissions based on access levels and content
> 
> 
> #### 🔹 Correlation Analysis
> 
> 
> 
> #### 🔹 Linking NetBIOS data with other enumeration findings
> 
> 
> 
> #### 🔹 3. SNMP Enumeration
> 
> 
> 
> #### 🔹 3.1 Working of SNMP
> 
> 
> 
> #### 🔹 📡SNMP Architecture
> 
> 
> Simple Network Management Protocol SNMP is used for managing and monitoring network devices. It operates in a manager-agent model where managers query agents running on network devices.
> 
> 
> #### 🔹 SNMP Versions
> 
> 
> 
> #### 🔹 SNMPv1
> 
> 
> 
> #### 🔹 Original version
> 
> 
> 
> #### 🔹 Plaintext community strings
> 
>
> ---
>
> ### 📍 Page 8
>
> 
> #### 🔹 No encryption
> 
> 
> 
> #### 🔹 Highly insecure
> 
> 
> 
> #### 🔹 SNMPv2c
> 
> 
> 
> #### 🔹 Community-based authentication
> 
> 
> 
> #### 🔹 Bulk operations support
> 
> 
> 
> #### 🔹 Still uses plaintext
> 
> 
> 
> #### 🔹 Backward compatible
> 
> 
> 
> #### 🔹 SNMPv3
> 
> 
> 
> #### 🔹 User-based security model
> 
> 
> 
> #### 🔹 Authentication and encryption
> 
> 
> 
> #### 🔹 Access control
> 
> 
> 
> #### 🔹 Industry standard for secure SNMP
> 
> 
> 
> #### 🔹 Core Components
> 
> 
> 
> #### 🔹 SNMP Agent
> 
> 
> 
> #### 🔹 Runs on managed devices (routers, switches, servers)
> 
> 
> 
> #### 🔹 SNMP Manager
> 
> 
> 
> #### 🔹 Queries agents and receives notifications
> 
> 
> 
> #### 🔹 Community Strings
> 
> 
> 
> #### 🔹 "public"  Default read-only community string
> 
> 
> 
> #### 🔹 "private"  Default read-write community string
> 
> 
> 
> #### 🔹 Acts as password for SNMP access
> 
> 
> 
> #### 🔹 SNMP Operations:
> 
> 
> 
> #### 🔹 GET  Retrieve specific value
> 
> 
> 
> #### 🔹 GETNEXT  Retrieve next value in tree
> 
> 
> 
> #### 🔹 GETBULK  Retrieve multiple values
> 
> 
> 
> #### 🔹 SET  Modify value (write community required)
> 
> 
> 
> #### 🔹 TRAP  Asynchronous notification from agent
> 
>
> ---
>
> ### 📍 Page 9
>
> 
> #### 🔹 3.2 Management Information Base (MIB)
> 
> 
> MIB is a hierarchical database of managed objects identified by Object Identifiers OIDs).
> 
> 
> #### 🔹 Key OID Categories
> 
> 
> 
> #### 🔹 System Information
> 
> 
> 
> #### 🔹 1.3.6.1.2.1.1.1.0    System description
> 
> 
> 
> #### 🔹 1.3.6.1.2.1.1.3.0    System uptime
> 
> 
> 
> #### 🔹 1.3.6.1.2.1.1.4.0    System contact
> 
> 
> 
> #### 🔹 1.3.6.1.2.1.1.5.0    System name
> 
> 
> 
> #### 🔹 1.3.6.1.2.1.1.6.0    System location
> 
> 
> 
> #### 🔹 Network Interfaces
> 
> 
> 
> #### 🔹 1.3.6.1.2.1.2         Interfaces table
> 
> 
> 
> #### 🔹 1.3.6.1.2.1.2.2.1.2   Interface descriptions
> 
> 
> 
> #### 🔹 Host Resources
> 
> 
> 
> #### 🔹 1.3.6.1.2.1.25.1      System info
> 
> 
> 
> #### 🔹 1.3.6.1.2.1.25.2      Storage
> 
> 
> 
> #### 🔹 1.3.6.1.2.1.25.4      Processes
> 
> 
> 
> #### 🔹 1.3.6.1.2.1.25.6      Software installed
> 
> 
> 
> #### 🔹 IP Information
> 
> 
> 
> #### 🔹 1.3.6.1.2.1.4         IP group
> 
> 
> 
> #### 🔹 1.3.6.1.2.1.4.20      IP address table
> 
> 
> 
> #### 🔹 1.3.6.1.2.1.4.21      IP routing table
> 
> 
> 
> #### 🔹 Vendor-Specific
> 
> 
> 
> #### 🔹 1.3.6.1.4.1           Enterprise/vendor MIBs
> 
> 
> 
> #### 🔹 3.3 Enumerating SNMP Using snmpwalk
> 
>
> ---
>
> ### 📍 Page 10
>
> snmpwalk traverses the entire MIB tree or specific branches.
> 
> 
> #### 🔹 Basic Usage
> 
> 
> 
> #### 🔹 # Full MIB walk SNMPv1
> 
> 
> 
> #### 🔹 snmpwalk -v1 -c public <target>
> 
> 
> 
> #### 🔹 # Full MIB walk SNMPv2c)
> 
> 
> 
> #### 🔹 snmpwalk -v2c -c public <target>
> 
> 
> 
> #### 🔹 # Specific OID walk
> 
> 
> 
> #### 🔹 snmpwalk -v2c -c public <target> 1.3.6.1.2.1.1
> 
> 
> 
> #### 🔹 # SNMPv3 (authenticated)
> 
> 
> snmpwalk -v3 -u <username> -l authPriv -a SHA A <auth_pass> -x AES 
> 
> 
> #### 🔹 X <priv_pass> <target>
> 
> 
> 
> #### 🔹 Information Revealed
> 
> 
> 
> #### 🔹 System Details:
> 
> 
> 
> #### 🔹 Hostname and description
> 
> 
> 
> #### 🔹 OS version and architecture
> 
> 
> 
> #### 🔹 System uptime
> 
> 
> 
> #### 🔹 Contact and location information
> 
> 
> 
> #### 🔹 Network Configuration:
> 
> 
> 
> #### 🔹 IP addresses and subnets
> 
> 
> 
> #### 🔹 Network interfaces and MAC addresses
> 
> 
> 
> #### 🔹 Routing tables
> 
> 
> 
> #### 🔹 ARP cache
> 
> 
> 
> #### 🔹 Running Processes:
> 
> 
> 
> #### 🔹 Process names and paths
> 
> 
> 
> #### 🔹 Running services
> 
> 
> 
> #### 🔹 Command-line arguments
> 
>
> ---
>

> [!NOTE]- 📄 **Pages 11 to 15 Syllabus Content**
>
> ### 📍 Page 11
>
> 
> #### 🔹 Installed Software:
> 
> 
> 
> #### 🔹 Application names and versions
> 
> 
> 
> #### 🔹 Patch levels
> 
> 
> 
> #### 🔹 Installed packages
> 
> 
> 
> #### 🔹 Storage Information:
> 
> 
> 
> #### 🔹 Disk usage and capacity
> 
> 
> 
> #### 🔹 Mount points
> 
> 
> 
> #### 🔹 File system types
> 
> 
> 
> #### 🔹 User Accounts:
> 
> 
> 
> #### 🔹 Logged-in users (on some systems)
> 
> 
> 
> #### 🔹 User account names
> 
> 
> 
> #### 🔹 3.4 SNMP Enumeration Using Nmap
> 
> 
> Nmap includes powerful NSE scripts for SNMP enumeration.
> 
> 
> #### 🔹 SNMP NSE Scripts
> 
> 
> 
> #### 🔹 # Basic SNMP info
> 
> 
> 
> #### 🔹 nmap -sU -p 161 --script snmp-info <target>
> 
> 
> 
> #### 🔹 # SNMP process enumeration
> 
> 
> 
> #### 🔹 nmap -sU -p 161 --script snmp-processes <target>
> 
> 
> 
> #### 🔹 # SNMP interface enumeration
> 
> 
> 
> #### 🔹 nmap -sU -p 161 --script snmp-interfaces <target>
> 
> 
> 
> #### 🔹 # SNMP NetBIOS name discovery
> 
> 
> 
> #### 🔹 nmap -sU -p 161 --script snmp-netstat <target>
> 
> 
> 
> #### 🔹 # SNMP system information
> 
> 
> 
> #### 🔹 nmap -sU -p 161 --script snmp-sysdescr <target>
> 
> 
> 
> #### 🔹 # SNMP user enumeration
> 
> 
> 
> #### 🔹 nmap -sU -p 161 --script snmp-win32-users <target>
> 
>
> ---
>
> ### 📍 Page 12
>
> 
> #### 🔹 # SNMP community string brute force
> 
> 
> 
> #### 🔹 nmap -sU -p 161 --script snmp-brute <target>
> 
> 
> 
> #### 🔹 # All SNMP scripts
> 
> 
> 
> #### 🔹 nmap -sU -p 161 --script snmp-* <target>
> 
> 
> 
> #### 🔹 3.5 SNMP Enumeration Tools
> 
> 
> 
> #### 🔹 Command-Line Tools
> 
> 
> 
> #### 🔹 snmpwalk
> 
> 
> 
> #### 🔹 Traverse MIB trees
> 
> 
> 
> #### 🔹 snmpget
> 
> 
> 
> #### 🔹 Retrieve specific OID values
> 
> 
> 
> #### 🔹 snmpbulkwalk
> 
> 
> 
> #### 🔹 Fast bulk retrieval
> 
> 
> 
> #### 🔹 onesixtyone
> 
> 
> 
> #### 🔹 Fast SNMP scanner and brute forcer
> 
> 
> 
> #### 🔹 onesixtyone -c community.txt <target>
> 
> 
> 
> #### 🔹 snmpcheck
> 
> 
> 
> #### 🔹 Comprehensive SNMP enumeration tool
> 
> 
> 
> #### 🔹 snmpcheck -t <target> -c public
> 
> 
> 
> #### 🔹 GUI Tools
> 
> 
> 
> #### 🔹 SolarWinds SNMP Walker
> 
> 
> 
> #### 🔹 Commercial SNMP browser and analyzer
> 
> 
> 
> #### 🔹 OpUtils
> 
> 
> 
> #### 🔹 Network monitoring and SNMP tool suite
> 
> 
> 
> #### 🔹 SNMP MIB Browser
> 
>
> ---
>
> ### 📍 Page 13
>
> 
> #### 🔹 Interactive MIB tree navigation
> 
> 
> 
> #### 🔹 iReasoning MIB Browser
> 
> 
> 
> #### 🔹 Free SNMP MIB browser with comprehensive features
> 
> 
> 
> #### 🔹 3.6 SNMP Enumeration with AI
> 
> 
> 
> #### 🔹 AI enhances SNMP enumeration efficiency:
> 
> 
> 
> #### 🔹 AI Applications
> 
> 
> 
> #### 🔹 Sensitive OID Identification
> 
> 
> Automatically identifying OIDs containing credentials, keys, or sensitive configs
> 
> 
> #### 🔹 Misconfiguration Detection
> 
> 
> Recognizing SNMP configurations that expose excessive information
> 
> 
> #### 🔹 Risk Scoring
> 
> 
> Prioritizing SNMP findings based on exploitability and impact
> 
> 
> #### 🔹 Attack Graph Generation
> 
> 
> Building network topology and attack paths from routing and interface data
> 
> 
> #### 🔹 Pattern Recognition
> 
> 
> Identifying anomalous SNMP responses indicating deception or honeypots
> 
> 
> #### 🔹 Automated Reporting
> 
> 
> Generating structured reports with actionable SNMP intelligence
> 
> 
> #### 🔹 4. LDAP Enumeration
> 
> 
> 
> #### 🔹 📁LDAP Overview
> 
> 
> Lightweight Directory Access Protocol LDAP is used for accessing and managing directory information services, particularly in Active
> 
> 
> #### 🔹 Directory environments. LDAP enumeration reveals critical
> 
> 
> organizational structure and user information.
> 
> 
> #### 🔹 4.1 Manual and Automated LDAP Enumeration
> 
>
> ---
>
> ### 📍 Page 14
>
> 
> #### 🔹 Manual LDAP Enumeration
> 
> 
> 
> #### 🔹 Using ldapsearch
> 
> 
> 
> #### 🔹 # Anonymous bind (if allowed)
> 
> 
> 
> #### 🔹 ldapsearch -x -h <target_ip> -b "dc=example,dc=com"
> 
> 
> 
> #### 🔹 # Authenticated bind
> 
> 
> ldapsearch -x -h <target_ip> D "cn=admin,dc=example,dc=com" -w pass
> 
> 
> #### 🔹 word -b "dc=example,dc=com"
> 
> 
> 
> #### 🔹 # Enumerate users
> 
> 
> ldapsearch -x -h <target_ip> -b "dc=example,dc=com" "(objectClass=use
> 
> 
> #### 🔹 r)"
> 
> 
> 
> #### 🔹 # Enumerate groups
> 
> 
> ldapsearch -x -h <target_ip> -b "dc=example,dc=com" "(objectClass=grou
> 
> 
> #### 🔹 p)"
> 
> 
> 
> #### 🔹 # Enumerate computers
> 
> 
> ldapsearch -x -h <target_ip> -b "dc=example,dc=com" "(objectClass=com
> 
> 
> #### 🔹 puter)"
> 
> 
> 
> #### 🔹 # Get naming contexts
> 
> 
> 
> #### 🔹 ldapsearch -x -h <target_ip> -s base namingContexts
> 
> 
> 
> #### 🔹 Automated LDAP Enumeration
> 
> 
> 
> #### 🔹 LDAPDomainDump
> 
> 
> 
> #### 🔹 ldapdomaindump -u 'DOMAIN\user' -p 'password' <target_ip>
> 
> 
> 
> #### 🔹 Windapsearch
> 
> 
> 
> #### 🔹 # Enumerate users
> 
> 
> windapsearch -d example.com --dc <target_ip> -u user@example.com -p
> 
> 
> #### 🔹 password --users
> 
> 
> 
> #### 🔹 # Enumerate groups
> 
>
> ---
>
> ### 📍 Page 15
>
> windapsearch -d example.com --dc <target_ip> -u user@example.com -p
> 
> 
> #### 🔹 password --groups
> 
> 
> 
> #### 🔹 # Enumerate privileged users
> 
> 
> windapsearch -d example.com --dc <target_ip> -u user@example.com -p
> 
> 
> #### 🔹 password --privileged-users
> 
> 
> 
> #### 🔹 Information Retrieved
> 
> 
> 
> #### 🔹 User Information:
> 
> 
> 
> #### 🔹 Usernames and display names
> 
> 
> 
> #### 🔹 Email addresses
> 
> 
> 
> #### 🔹 Last logon timestamps
> 
> 
> 
> #### 🔹 Password last set dates
> 
> 
> 
> #### 🔹 Account expiration dates
> 
> 
> 
> #### 🔹 User attributes and descriptions
> 
> 
> 
> #### 🔹 Group Information:
> 
> 
> 
> #### 🔹 Group names and descriptions
> 
> 
> 
> #### 🔹 Group memberships
> 
> 
> 
> #### 🔹 Nested groups
> 
> 
> 
> #### 🔹 Privileged groups Domain Admins, Enterprise Admins)
> 
> 
> 
> #### 🔹 Organizational Units (OUs):
> 
> 
> 
> #### 🔹 OU structure and hierarchy
> 
> 
> 
> #### 🔹 Computer organization
> 
> 
> 
> #### 🔹 User organization
> 
> 
> 
> #### 🔹 Policy Information:
> 
> 
> 
> #### 🔹 Password policies
> 
> 
> 
> #### 🔹 Account lockout policies
> 
> 
> 
> #### 🔹 Kerberos policies
> 
> 
> 
> #### 🔹 Service Principal Names SPNs):
> 
>
> ---
>

> [!NOTE]- 📄 **Pages 16 to 20 Syllabus Content**
>
> ### 📍 Page 16
>
> 
> #### 🔹 Kerberoastable accounts
> 
> 
> 
> #### 🔹 Service accounts
> 
> 
> 
> #### 🔹 Service mappings
> 
> 
> 
> #### 🔹 Domain Controllers:
> 
> 
> 
> #### 🔹 DC hostnames
> 
> 
> 
> #### 🔹 DC IP addresses
> 
> 
> 
> #### 🔹 FSMO role holders
> 
> 
> 
> #### 🔹 4.2 LDAP Enumeration Tools
> 
> 
> 
> #### 🔹 Command-Line Tools
> 
> 
> 
> #### 🔹 ldapsearch
> 
> 
> 
> #### 🔹 Standard LDAP query tool OpenLDAP
> 
> 
> 
> #### 🔹 ldapdomaindump
> 
> 
> Dumps Active Directory information in human-readable formats
> 
> 
> #### 🔹 windapsearch
> 
> 
> 
> #### 🔹 Python script for AD enumeration via LDAP
> 
> 
> 
> #### 🔹 ADExplorer Sysinternals)
> 
> 
> 
> #### 🔹 Windows tool for AD browsing and snapshots
> 
> 
> 
> #### 🔹 GUI Tools
> 
> 
> 
> #### 🔹 Softerra LDAP Browser
> 
> 
> 
> #### 🔹 Comprehensive LDAP client with query builder
> 
> 
> 
> #### 🔹 JXplorer
> 
> 
> 
> #### 🔹 Open-source LDAP browser
> 
> 
> 
> #### 🔹 Apache Directory Studio
> 
> 
> 
> #### 🔹 Eclipse-based LDAP browser and directory client
> 
> 
> 
> #### 🔹 Nmap LDAP Scripts
> 
> 
> 
> #### 🔹 # LDAP root DSE enumeration
> 
> 
> 
> #### 🔹 nmap -p 389 --script ldap-rootdse <target>
> 
>
> ---
>
> ### 📍 Page 17
>
> 
> #### 🔹 # LDAP search
> 
> 
> 
> #### 🔹 nmap -p 389 --script ldap-search <target>
> 
> 
> 
> #### 🔹 # LDAP brute force
> 
> 
> 
> #### 🔹 nmap -p 389 --script ldap-brute <target>
> 
> 
> 
> #### 🔹 5. NTP and NFS Enumeration
> 
> 
> 
> #### 🔹 5.1 NTP Enumeration
> 
> 
> Network Time Protocol NTP can leak sensitive system information.
> 
> 
> #### 🔹 Information Leaked via NTP
> 
> 
> 
> #### 🔹 System Details:
> 
> 
> 
> #### 🔹 Operating system version
> 
> 
> 
> #### 🔹 System uptime
> 
> 
> 
> #### 🔹 Server time and timezone
> 
> 
> 
> #### 🔹 Network Topology:
> 
> 
> 
> #### 🔹 NTP peers and stratum levels
> 
> 
> 
> #### 🔹 Network time sources
> 
> 
> 
> #### 🔹 Server relationships
> 
> 
> 
> #### 🔹 Client Information:
> 
> 
> 
> #### 🔹 Recent client connections (via monlist)
> 
> 
> 
> #### 🔹 Client IP addresses
> 
> 
> 
> #### 🔹 Connection timestamps
> 
> 
> 
> #### 🔹 5.2 NTP Enumeration Commands
> 
> 
> 
> #### 🔹 Using ntpq
> 
>
> ---
>
> ### 📍 Page 18
>
> 
> #### 🔹 # Query NTP peers
> 
> 
> 
> #### 🔹 ntpq -c peers <target>
> 
> 
> 
> #### 🔹 # Query NTP associations
> 
> 
> 
> #### 🔹 ntpq -c associations <target>
> 
> 
> 
> #### 🔹 # Get system variables
> 
> 
> 
> #### 🔹 ntpq -c sysinfo <target>
> 
> 
> 
> #### 🔹 # Get detailed peer info
> 
> 
> 
> #### 🔹 ntpq -c "rv 0" <target>
> 
> 
> 
> #### 🔹 Using ntpdc (Legacy)
> 
> 
> 
> #### 🔹 # Get monitor list (last 600 clients)
> 
> 
> 
> #### 🔹 ntpdc -c monlist <target>
> 
> 
> 
> #### 🔹 # Get system info
> 
> 
> 
> #### 🔹 ntpdc -c sysinfo <target>
> 
> 
> 
> #### 🔹 # Get peer info
> 
> 
> 
> #### 🔹 ntpdc -c peers <target>
> 
> 
> 
> #### 🔹 ⚠Monlist Vulnerability
> 
> 
> The monlist  command reveals the last 600 NTP clients that connected to the server, including their IP addresses. This can be used for:
> 
> 
> #### 🔹 Network mapping
> 
> 
> 
> #### 🔹 DDoS amplification attacks
> 
> 
> 
> #### 🔹 Identifying internal network ranges
> 
> 
> Modern NTP implementations disable monlist by default.
> 
> 
> #### 🔹 5.3 NTP Enumeration Tools
> 
> 
> 
> #### 🔹 ntpq
> 
>
> ---
>
> ### 📍 Page 19
>
> 
> #### 🔹 Standard NTP query tool
> 
> 
> 
> #### 🔹 ntpdc
> 
> 
> 
> #### 🔹 Legacy NTP control and monitoring
> 
> 
> 
> #### 🔹 Nmap NTP Scripts
> 
> 
> 
> #### 🔹 nmap -sU -p 123 --script ntp-info <target>
> 
> 
> 
> #### 🔹 nmap -sU -p 123 --script ntp-monlist <target>
> 
> 
> 
> #### 🔹 5.4 NFS Enumeration
> 
> 
> Network File System NFS allows file sharing across networks.
> 
> 
> #### 🔹 Discovering NFS Exports
> 
> 
> 
> #### 🔹 # Show exported file systems
> 
> 
> 
> #### 🔹 showmount -e <target>
> 
> 
> 
> #### 🔹 # Show all mount points
> 
> 
> 
> #### 🔹 showmount -a <target>
> 
> 
> 
> #### 🔹 # Show directories
> 
> 
> 
> #### 🔹 showmount -d <target>
> 
> 
> 
> #### 🔹 Mounting NFS Shares
> 
> 
> 
> #### 🔹 # Create mount point
> 
> 
> 
> #### 🔹 mkdir /mnt/nfs
> 
> 
> 
> #### 🔹 # Mount NFS share
> 
> 
> 
> #### 🔹 mount -t nfs <target>:/exported/path /mnt/nfs
> 
> 
> 
> #### 🔹 # Mount with NFS version 3
> 
> 
> 
> #### 🔹 mount -t nfs -o vers=3 <target>:/exported/path /mnt/nfs
> 
> 
> 
> #### 🔹 Exploiting NFS Misconfigurations
> 
> 
> 
> #### 🔹 no_root_squash
> 
>
> ---
>
> ### 📍 Page 20
>
> Allows root user on client to have root privileges on NFS share
> 
> 
> #### 🔹 # Create SUID binary on NFS share as root
> 
> 
> 
> #### 🔹 cp /bin/bash /mnt/nfs/bash
> 
> 
> 
> #### 🔹 chmod +s /mnt/nfs/bash
> 
> 
> 
> #### 🔹 # On victim, execute: /exported/path/bash -p
> 
> 
> 
> #### 🔹 5.5 NFS Enumeration Tools
> 
> 
> 
> #### 🔹 showmount
> 
> 
> 
> #### 🔹 Display NFS exports
> 
> 
> 
> #### 🔹 nmap NFS Scripts
> 
> 
> 
> #### 🔹 nmap -p 111,2049 --script nfs-* <target>
> 
> 
> 
> #### 🔹 nmap -p 111 --script rpcinfo <target>
> 
> 
> 
> #### 🔹 RPCinfo
> 
> 
> 
> #### 🔹 rpcinfo -p <target>
> 
> 
> 
> #### 🔹 6. SMTP and DNS Enumeration
> 
> 
> 
> #### 🔹 6.1 SMTP Enumeration
> 
> 
> 
> #### 🔹 📧SMTP Enumeration Overview
> 
> 
> SMTP Simple Mail Transfer Protocol) can be exploited to validate user accounts and enumerate email addresses through specific commands.
> 
> 
> #### 🔹 SMTP Enumeration Commands
> 
> 
> 
> #### 🔹 VRFY Verify)
> 
> 
> 
> #### 🔹 Validates if a user mailbox exists
> 
>
> ---
>

> [!NOTE]- 📄 **Pages 21 to 25 Syllabus Content**
>
> ### 📍 Page 21
>
> 
> #### 🔹 telnet <target> 25
> 
> 
> 
> #### 🔹 VRFY admin
> 
> 
> 
> #### 🔹 VRFY root
> 
> 
> 
> #### 🔹 VRFY user@domain.com
> 
> 
> 
> #### 🔹 EXPN Expand)
> 
> 
> 
> #### 🔹 Expands mailing lists and aliases
> 
> 
> 
> #### 🔹 telnet <target> 25
> 
> 
> 
> #### 🔹 EXPN admin
> 
> 
> 
> #### 🔹 EXPN all@domain.com
> 
> 
> 
> #### 🔹 RCPT TO
> 
> 
> 
> #### 🔹 Can indirectly validate email addresses
> 
> 
> 
> #### 🔹 telnet <target> 25
> 
> 
> 
> #### 🔹 MAIL FROM test@example.com
> 
> 
> 
> #### 🔹 RCPT TO user@target.com
> 
> 
> 
> #### 🔹 Response Interpretation
> 
> 
> 
> #### 🔹 250 Code
> 
> 
> 
> #### 🔹 User exists / Command successful
> 
> 
> 
> #### 🔹 550 Code
> 
> 
> 
> #### 🔹 User does not exist / Mailbox unavailable
> 
> 
> 
> #### 🔹 252 Code
> 
> 
> 
> #### 🔹 Cannot verify user, but will attempt delivery
> 
> 
> 
> #### 🔹 6.2 SMTP Enumeration Using Nmap
> 
> 
> 
> #### 🔹 # SMTP user enumeration
> 
> 
> 
> #### 🔹 nmap -p 25 --script smtp-enum-users <target>
> 
> 
> 
> #### 🔹 # SMTP command support
> 
> 
> 
> #### 🔹 nmap -p 25 --script smtp-commands <target>
> 
>
> ---
>
> ### 📍 Page 22
>
> 
> #### 🔹 # SMTP open relay check
> 
> 
> 
> #### 🔹 nmap -p 25 --script smtp-open-relay <target>
> 
> 
> 
> #### 🔹 # SMTP NTLM info
> 
> 
> 
> #### 🔹 nmap -p 25,587 --script smtp-ntlm-info <target>
> 
> 
> 
> #### 🔹 6.3 SMTP Enumeration Using Metasploit
> 
> 
> 
> #### 🔹 Metasploit SMTP Modules
> 
> 
> 
> #### 🔹 # SMTP user enumeration
> 
> 
> 
> #### 🔹 use auxiliary/scanner/smtp/smtp_enum
> 
> 
> 
> #### 🔹 set RHOSTS <target>
> 
> 
> 
> #### 🔹 set USER_FILE /usr/share/wordlists/users.txt
> 
> 
> 
> #### 🔹 run
> 
> 
> 
> #### 🔹 # SMTP version detection
> 
> 
> 
> #### 🔹 use auxiliary/scanner/smtp/smtp_version
> 
> 
> 
> #### 🔹 set RHOSTS <target>
> 
> 
> 
> #### 🔹 run
> 
> 
> 
> #### 🔹 6.4 SMTP Enumeration Tools
> 
> 
> 
> #### 🔹 smtp-user-enum
> 
> 
> 
> #### 🔹 Perl script for SMTP user enumeration
> 
> 
> 
> #### 🔹 smtp-user-enum M VRFY U users.txt -t <target>
> 
> 
> 
> #### 🔹 smtp-user-enum M EXPN U users.txt -t <target>
> 
> 
> 
> #### 🔹 smtp-user-enum M RCPT U users.txt -t <target>
> 
> 
> 
> #### 🔹 SWAKS Swiss Army Knife for SMTP
> 
> 
> 
> #### 🔹 Testing and troubleshooting SMTP
> 
> 
> 
> #### 🔹 swaks --to user@target.com --server <target>
> 
> 
> 
> #### 🔹 Metasploit
> 
>
> ---
>
> ### 📍 Page 23
>
> 
> #### 🔹 Auxiliary SMTP modules
> 
> 
> 
> #### 🔹 Nmap
> 
> 
> 
> #### 🔹 NSE SMTP scripts
> 
> 
> 
> #### 🔹 6.5 SMTP Enumeration Using AI
> 
> 
> 
> #### 🔹 AI enhances SMTP enumeration:
> 
> 
> 
> #### 🔹 AI Capabilities
> 
> 
> 
> #### 🔹 Banner Anomaly Recognition
> 
> 
> Identifying unusual SMTP banners indicating honeypots or deception
> 
> 
> #### 🔹 Username Prediction
> 
> 
> Generating likely valid usernames based on discovered patterns
> 
> 
> #### 🔹 Automated Command Replay
> 
> 
> Intelligently sequencing SMTP commands for maximum information extraction
> 
> 
> #### 🔹 Response Pattern Analysis
> 
> 
> Parsing SMTP responses to identify subtle differences indicating account
> 
> 
> #### 🔹 existence
> 
> 
> 
> #### 🔹 Email Format Inference
> 
> 
> 
> #### 🔹 Deducing email address formats from partial information
> 
> 
> 
> #### 🔹 6.6 DNS Enumeration
> 
> 
> 
> #### 🔹 🌐DNS Enumeration Overview
> 
> 
> DNS enumeration extracts domain information including subdomains, mail servers, name servers, and IP addresses. Misconfigurations can expose entire network infrastructures.
> 
> 
> #### 🔹 DNS Zone Transfer
> 
> 
> 
> #### 🔹 AXFR Full Zone Transfer)
> 
> 
> 
> #### 🔹 Attempts to retrieve complete DNS zone file:
> 
>
> ---
>
> ### 📍 Page 24
>
> 
> #### 🔹 # Using dig
> 
> 
> 
> #### 🔹 dig axfr @nameserver target.com
> 
> 
> 
> #### 🔹 # Using host
> 
> 
> 
> #### 🔹 host -l target.com nameserver
> 
> 
> 
> #### 🔹 # Using nslookup
> 
> 
> 
> #### 🔹 nslookup
> 
> 
> 
> #### 🔹 server nameserver
> 
> 
> 
> #### 🔹 ls -d target.com
> 
> 
> 
> #### 🔹 If successful, exposes:
> 
> 
> 
> #### 🔹 All subdomains
> 
> 
> 
> #### 🔹 IP addresses
> 
> 
> 
> #### 🔹 Mail servers
> 
> 
> 
> #### 🔹 Name servers
> 
> 
> 
> #### 🔹 TXT records SPF, DKIM, DMARC
> 
> 
> 
> #### 🔹 Service records SRV
> 
> 
> 
> #### 🔹 DNS Cache Snooping
> 
> 
> 
> #### 🔹 Checks if DNS server has cached specific domains:
> 
> 
> 
> #### 🔹 # Non-recursive query
> 
> 
> 
> #### 🔹 dig @<dns_server> targetdomain.com A +norecurse
> 
> 
> 
> #### 🔹 # If cached, responds immediately
> 
> 
> 
> #### 🔹 # If not cached, returns SERVFAIL or referral
> 
> 
> 
> #### 🔹 Use Cases:
> 
> 
> 
> #### 🔹 Determining visited websites
> 
> 
> 
> #### 🔹 Identifying internal domain usage
> 
> 
> 
> #### 🔹 Mapping customer/partner relationships
> 
> 
> 
> #### 🔹 DNSSEC Zone Walking
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
> #### 🔹 DNSSEC uses NSEC/NSEC3 records which can leak domain names:
> 
> 
> 
> #### 🔹 # Using ldns-walk
> 
> 
> 
> #### 🔹 ldns-walk target.com
> 
> 
> 
> #### 🔹 # Using nsec3walker (for NSEC3
> 
> 
> 
> #### 🔹 nsec3walker target.com
> 
> 
> 
> #### 🔹 DNS Subdomain Enumeration
> 
> 
> 
> #### 🔹 Brute Force Methods:
> 
> 
> 
> #### 🔹 # Using dnsenum
> 
> 
> 
> #### 🔹 dnsenum --enum target.com
> 
> 
> 
> #### 🔹 # Using fierce
> 
> 
> 
> #### 🔹 fierce --domain target.com
> 
> 
> 
> #### 🔹 # Using sublist3r
> 
> 
> 
> #### 🔹 sublist3r -d target.com
> 
> 
> 
> #### 🔹 DNS Enumeration Using OWASP Amass
> 
> 
> Amass is a powerful OSINT and DNS enumeration tool.
> 
> 
> #### 🔹 # Passive enumeration
> 
> 
> 
> #### 🔹 amass enum -passive -d target.com
> 
> 
> 
> #### 🔹 # Active enumeration
> 
> 
> 
> #### 🔹 amass enum -active -d target.com
> 
> 
> 
> #### 🔹 # Subdomain brute forcing
> 
> 
> 
> #### 🔹 amass enum -brute -d target.com
> 
> 
> 
> #### 🔹 # With all techniques
> 
> 
> 
> #### 🔹 amass enum -d target.com -o output.txt
> 
> 
> 
> #### 🔹 Capabilities:
> 
>
> ---
>

> [!NOTE]- 📄 **Pages 26 to 30 Syllabus Content**
>
> ### 📍 Page 26
>
> 
> #### 🔹 Subdomain discovery via multiple sources
> 
> 
> 
> #### 🔹 DNS brute forcing with intelligent wordlists
> 
> 
> 
> #### 🔹 API integration VirusTotal, AlienVault, etc.)
> 
> 
> 
> #### 🔹 Correlation with external databases
> 
> 
> 
> #### 🔹 DNS relationship graphing
> 
> 
> 
> #### 🔹 Recursive subdomain discovery
> 
> 
> 
> #### 🔹 DNS Enumeration Using Nmap
> 
> 
> 
> #### 🔹 # DNS brute force
> 
> 
> 
> #### 🔹 nmap --script dns-brute target.com
> 
> 
> 
> #### 🔹 # DNS cache snoop
> 
> 
> nmap -sU -p 53 --script dns-cache-snoop --script-args 'dns-cache-snoo p.mode=timed,dns-cache-snoop.domains={google.com,facebook.com}' <
> 
> 
> #### 🔹 dns_server>
> 
> 
> 
> #### 🔹 # DNS NSEC enumeration
> 
> 
> nmap --script dns-nsec-enum --script-args dns-nsec-enum.domains=targ
> 
> 
> #### 🔹 et.com
> 
> 
> 
> #### 🔹 # DNS zone transfer
> 
> 
> nmap --script dns-zone-transfer --script-args dns-zone-transfer.domain=t
> 
> 
> #### 🔹 arget.com <nameserver>
> 
> 
> 
> #### 🔹 # DNS service discovery
> 
> 
> nmap --script dns-srv-enum --script-args dns-srv-enum.domain=target.co
> 
> 
> #### 🔹 m
> 
> 
> 
> #### 🔹 DNS Enumeration with Nmap Using AI
> 
> 
> 
> #### 🔹 AI enhances DNS enumeration:
> 
> 
> 
> #### 🔹 Complex Relationship Mapping
> 
> 
> 
> #### 🔹 Visualizing intricate DNS hierarchies and dependencies
> 
> 
> 
> #### 🔹 Wildcard Detection
> 
>
> ---
>
> ### 📍 Page 27
>
> 
> #### 🔹 Identifying and filtering wildcard DNS records
> 
> 
> 
> #### 🔹 Misconfiguration Identification
> 
> 
> 
> #### 🔹 Automatically detecting security weaknesses in DNS configs
> 
> 
> 
> #### 🔹 Exploitable Leak Prioritization
> 
> 
> 
> #### 🔹 Ranking DNS findings by exploitability and business impact
> 
> 
> 
> #### 🔹 DNS Cache Snooping Using AI
> 
> 
> 
> #### 🔹 AI analyzes cache snooping results:
> 
> 
> 
> #### 🔹 Query Pattern Analysis
> 
> 
> 
> #### 🔹 Identifying patterns in cached queries
> 
> 
> 
> #### 🔹 Domain Relationship Mapping
> 
> 
> 
> #### 🔹 Connecting related domains and subdomains
> 
> 
> 
> #### 🔹 Internal Domain Discovery
> 
> 
> 
> #### 🔹 Inferring internal domain structures from cache behavior
> 
> 
> 
> #### 🔹 Temporal Analysis
> 
> 
> 
> #### 🔹 Understanding when and how frequently domains are accessed
> 
> 
> 
> #### 🔹 7. Other Enumeration Techniques
> 
> 
> 
> #### 🔹 7.1 IPsec Enumeration
> 
> 
> IPsec Internet Protocol Security) enumeration identifies VPN endpoints and configurations.
> 
> 
> #### 🔹 IPsec Ports and Protocols
> 
> 
> Port 500/UDP  ISAKMP Internet Security Association and Key
> 
> 
> #### 🔹 Management Protocol)
> 
> 
> 
> #### 🔹 Port 4500/UDP  NATT NAT Traversal)
> 
> 
> 
> #### 🔹 Protocol 50  ESP Encapsulating Security Payload)
> 
> 
> 
> #### 🔹 Protocol 51  AH Authentication Header)
> 
> 
> 
> #### 🔹 IPsec Enumeration Tools
> 
>
> ---
>
> ### 📍 Page 28
>
> 
> #### 🔹 ike-scan
> 
> 
> 
> #### 🔹 Discover and fingerprint IKE hosts
> 
> 
> 
> #### 🔹 # Basic IKE scan
> 
> 
> 
> #### 🔹 ike-scan <target>
> 
> 
> 
> #### 🔹 # Aggressive mode scan
> 
> 
> 
> #### 🔹 ike-scan A <target>
> 
> 
> 
> #### 🔹 # PSK cracking
> 
> 
> 
> #### 🔹 ike-scan A M P <hashfile> <target>
> 
> 
> 
> #### 🔹 ikeforce
> 
> 
> 
> #### 🔹 Brute force and enumerate IKE VPNs
> 
> 
> 
> #### 🔹 7.2 IPsec Enumeration with AI
> 
> 
> 
> #### 🔹 AI assists IPsec enumeration:
> 
> 
> 
> #### 🔹 Weak Cipher Detection
> 
> 
> 
> #### 🔹 Identifying outdated or vulnerable encryption algorithms
> 
> 
> 
> #### 🔹 Default Policy Identification
> 
> 
> 
> #### 🔹 Recognizing vendor default IPsec configurations
> 
> 
> 
> #### 🔹 VPN Setup Prediction
> 
> 
> Predicting VPN architectures based on port and protocol patterns
> 
> 
> #### 🔹 Configuration Analysis
> 
> 
> 
> #### 🔹 Analyzing IKE proposals for security weaknesses
> 
> 
> 
> #### 🔹 7.3 VoIP Enumeration
> 
> 
> Voice over IP VoIP enumeration discovers telephony infrastructure.
> 
> 
> #### 🔹 SIP Enumeration
> 
> 
> SIP Session Initiation Protocol) uses port 5060 UDP/TCP and 5061 TLS.
> 
> 
> #### 🔹 SIP Enumeration Methods
> 
> 
> 
> #### 🔹 OPTIONS Request
> 
>
> ---
>
> ### 📍 Page 29
>
> 
> #### 🔹 # Using sipvicious
> 
> 
> 
> #### 🔹 svmap <target_network>
> 
> 
> 
> #### 🔹 # Extension enumeration
> 
> 
> 
> #### 🔹 svwar -e 10009999 <target>
> 
> 
> 
> #### 🔹 # User enumeration
> 
> 
> 
> #### 🔹 svcrack -u users.txt <target>
> 
> 
> 
> #### 🔹 ENUM Queries
> 
> 
> 
> #### 🔹 E.164 number to URI mapping
> 
> 
> 
> #### 🔹 Information Gathered:
> 
> 
> 
> #### 🔹 SIP server version and capabilities
> 
> 
> 
> #### 🔹 Valid extensions
> 
> 
> 
> #### 🔹 User accounts
> 
> 
> 
> #### 🔹 Supported codecs
> 
> 
> 
> #### 🔹 Authentication mechanisms
> 
> 
> 
> #### 🔹 7.4 RPC Enumeration
> 
> 
> Remote Procedure Call RPC enumeration reveals running services.
> 
> 
> #### 🔹 RPC Ports
> 
> 
> 
> #### 🔹 Port 135/TCP  Windows RPC Endpoint Mapper
> 
> 
> 
> #### 🔹 Port 111/TCP  Unix RPC Portmapper
> 
> 
> 
> #### 🔹 RPC Enumeration Tools
> 
> 
> 
> #### 🔹 rpcinfo
> 
> 
> 
> #### 🔹 rpcinfo -p <target>
> 
> 
> 
> #### 🔹 rpcclient
> 
> 
> 
> #### 🔹 rpcclient U "" <target>
> 
> 
> 
> #### 🔹 > enumdomusers
> 
>
> ---
>
> ### 📍 Page 30
>
> 
> #### 🔹 > enumdomgroups
> 
> 
> 
> #### 🔹 > querydominfo
> 
> 
> 
> #### 🔹 Nmap RPC Scripts
> 
> 
> 
> #### 🔹 nmap -p 111 --script rpcinfo <target>
> 
> 
> 
> #### 🔹 nmap -p 135 --script msrpc-enum <target>
> 
> 
> 
> #### 🔹 7.5 Unix/Linux User Enumeration
> 
> 
> 
> #### 🔹 Enumeration Methods
> 
> 
> 
> #### 🔹 SSH Banner Grabbing
> 
> 
> 
> #### 🔹 nc <target> 22
> 
> 
> 
> #### 🔹 ssh <target>
> 
> 
> 
> #### 🔹 Finger Service Port 79
> 
> 
> 
> #### 🔹 finger @<target>
> 
> 
> 
> #### 🔹 finger username@<target>
> 
> 
> 
> #### 🔹 RServices Ports 512514
> 
> 
> 
> #### 🔹 Legacy remote execution services
> 
> 
> 
> #### 🔹 rwho Port 513
> 
> 
> 
> #### 🔹 Displays logged-in users
> 
> 
> 
> #### 🔹 rusers
> 
> 
> 
> #### 🔹 rusers <target>
> 
> 
> 
> #### 🔹 /etc/passwd Exposure
> 
> 
> 
> #### 🔹 If accessible via LFI or misconfiguration:
> 
> 
> 
> #### 🔹 curl http://target/index.php?page=../../../../etc/passwd
> 
>
> ---
>

> [!NOTE]- 📄 **Pages 31 to 35 Syllabus Content**
>
> ### 📍 Page 31
>
> 
> #### 🔹 7.6 SMB Enumeration
> 
> 
> Server Message Block SMB enumeration is crucial for Windows environments.
> 
> 
> #### 🔹 SMB Information Gathered
> 
> 
> 
> #### 🔹 User Information:
> 
> 
> 
> #### 🔹 Local and domain users
> 
> 
> 
> #### 🔹 User SIDs Security Identifiers)
> 
> 
> 
> #### 🔹 User descriptions
> 
> 
> 
> #### 🔹 Last logon times
> 
> 
> 
> #### 🔹 Share Information:
> 
> 
> 
> #### 🔹 Share names and paths
> 
> 
> 
> #### 🔹 Share permissions
> 
> 
> 
> #### 🔹 Hidden shares
> 
> 
> 
> #### 🔹 Administrative shares
> 
> 
> 
> #### 🔹 System Information:
> 
> 
> 
> #### 🔹 Operating system version
> 
> 
> 
> #### 🔹 Domain/workgroup name
> 
> 
> 
> #### 🔹 Computer name
> 
> 
> 
> #### 🔹 SMB signing status
> 
> 
> 
> #### 🔹 Policy Information:
> 
> 
> 
> #### 🔹 Password policies
> 
> 
> 
> #### 🔹 Lockout policies
> 
> 
> 
> #### 🔹 Minimum password length
> 
> 
> 
> #### 🔹 Password complexity requirements
> 
> 
> 
> #### 🔹 SMB Enumeration Tools
> 
> 
> 
> #### 🔹 enum4linux
> 
> 
> 
> #### 🔹 Comprehensive SMB/NetBIOS enumeration
> 
>
> ---
>
> ### 📍 Page 32
>
> 
> #### 🔹 enum4linux -a <target>
> 
> 
> 
> #### 🔹 smbclient
> 
> 
> 
> #### 🔹 Connect to SMB shares
> 
> 
> 
> #### 🔹 smbclient L //<target> N
> 
> 
> 
> #### 🔹 smbclient //<target>/share U username
> 
> 
> 
> #### 🔹 crackmapexec
> 
> 
> 
> #### 🔹 Advanced SMB enumeration and exploitation
> 
> 
> 
> #### 🔹 crackmapexec smb <target>
> 
> 
> 
> #### 🔹 crackmapexec smb <target> --shares
> 
> 
> 
> #### 🔹 crackmapexec smb <target> -u user -p password --users
> 
> 
> 
> #### 🔹 crackmapexec smb <target> -u user -p password --groups
> 
> 
> 
> #### 🔹 smbmap
> 
> 
> 
> #### 🔹 SMB share enumeration
> 
> 
> 
> #### 🔹 smbmap H <target>
> 
> 
> 
> #### 🔹 smbmap H <target> -u username -p password
> 
> 
> 
> #### 🔹 Nmap SMB Scripts
> 
> 
> 
> #### 🔹 nmap --script smb-enum-shares <target>
> 
> 
> 
> #### 🔹 nmap --script smb-enum-users <target>
> 
> 
> 
> #### 🔹 nmap --script smb-enum-domains <target>
> 
> 
> 
> #### 🔹 nmap --script smb-os-discovery <target>
> 
> 
> 
> #### 🔹 nmap --script smb-security-mode <target>
> 
> 
> 
> #### 🔹 7.7 SMB Enumeration with AI
> 
> 
> 
> #### 🔹 AI enhances SMB enumeration:
> 
> 
> 
> #### 🔹 Automated Share Mapping
> 
> 
> 
> #### 🔹 Systematically cataloging all accessible shares
> 
>
> ---
>
> ### 📍 Page 33
>
> 
> #### 🔹 Permission Analysis
> 
> 
> 
> #### 🔹 Analyzing and visualizing complex share permissions
> 
> 
> 
> #### 🔹 Weak ACL Identification
> 
> 
> 
> #### 🔹 Detecting misconfigured access control lists
> 
> 
> 
> #### 🔹 Exploitable Share Prioritization
> 
> 
> 
> #### 🔹 Ranking shares by likelihood of containing sensitive data
> 
> 
> 
> #### 🔹 Credential Reuse Detection
> 
> 
> Identifying patterns suggesting credential reuse across systems
> 
> 
> #### 🔹 7.8 AI Automation Script for Enumeration
> 
> 
> 
> #### 🔹 Comprehensive AI-driven enumeration automation:
> 
> 
> 
> #### 🔹 Script Capabilities
> 
> 
> 
> #### 🔹 Multi-Protocol Enumeration
> 
> 
> 
> #### 🔹 Simultaneous enumeration across all protocols
> 
> 
> 
> #### 🔹 Intelligent protocol detection and adaptation
> 
> 
> 
> #### 🔹 Automatic fallback to alternative methods
> 
> 
> 
> #### 🔹 Data Correlation
> 
> 
> 
> #### 🔹 Cross-referencing findings across protocols
> 
> 
> 
> #### 🔹 Identifying relationships between discovered assets
> 
> 
> 
> #### 🔹 Building comprehensive attack graphs
> 
> 
> 
> #### 🔹 Automatic AD Mapping
> 
> 
> 
> #### 🔹 Complete Active Directory structure discovery
> 
> 
> 
> #### 🔹 User and group relationship mapping
> 
> 
> 
> #### 🔹 Privilege path identification
> 
> 
> 
> #### 🔹 Finding Prioritization
> 
> 
> 
> #### 🔹 AI-driven risk scoring
> 
> 
> 
> #### 🔹 Exploitability assessment
> 
> 
> 
> #### 🔹 Business impact evaluation
> 
>
> ---
>
> ### 📍 Page 34
>
> 
> #### 🔹 Reporting
> 
> 
> 
> #### 🔹 JSON/XML structured data export
> 
> 
> 
> #### 🔹 HTML interactive reports
> 
> 
> 
> #### 🔹 Executive summaries
> 
> 
> 
> #### 🔹 Technical detail sections
> 
> 
> 
> #### 🔹 Remediation recommendations
> 
> 
> 
> #### 🔹 8. Enumeration Countermeasures
> 
> 
> 
> #### 🔹 🛡Defensive Posture
> 
> 
> Effective enumeration countermeasures reduce the attack surface by limiting information disclosure and implementing strong access controls.
> 
> 
> #### 🔹 8.1 SNMP Countermeasures
> 
> 
> 
> #### 🔹 Protection Strategies
> 
> 
> 
> #### 🔹 Use SNMPv3 with Encryption
> 
> 
> 
> #### 🔹 Implement authenticated and encrypted SNMP communications
> 
> 
> 
> #### 🔹 # SNMPv3 configuration example
> 
> 
> 
> #### 🔹 snmp-server group v3group v3 auth
> 
> 
> snmp-server user v3user v3group v3 auth sha AuthPass priv aes 128 PrivP
> 
> 
> #### 🔹 ass
> 
> 
> 
> #### 🔹 Change Default Community Strings
> 
> 
> 
> #### 🔹 Replace "public" and "private" with complex strings
> 
> 
> 
> #### 🔹 Implement ACLs
> 
> 
> 
> #### 🔹 Restrict SNMP access to specific management IPs
> 
> 
> 
> #### 🔹 access-list 10 permit 192.168.1.100
> 
> 
> 
> #### 🔹 snmp-server community SecureString RO 10
> 
>
> ---
>
> ### 📍 Page 35
>
> 
> #### 🔹 Disable SNMP if Unused
> 
> 
> 
> #### 🔹 Remove SNMP service from systems not requiring monitoring
> 
> 
> 
> #### 🔹 Monitor SNMP Traffic
> 
> 
> 
> #### 🔹 Log and alert on SNMP queries from unauthorized sources
> 
> 
> 
> #### 🔹 8.2 LDAP Countermeasures
> 
> 
> 
> #### 🔹 Security Measures
> 
> 
> 
> #### 🔹 Disable Anonymous Binds
> 
> 
> 
> #### 🔹 Prevent unauthenticated LDAP queries
> 
> 
> 
> #### 🔹 # Active Directory
> 
> 
> Set-ADObject Identity "CNDirectory Service,CNWindows NT,CNServic es,CNConfiguration,DC=domain,DC=com" Replace @{dSHeuristics="00
> 
> 
> #### 🔹 00002"}
> 
> 
> 
> #### 🔹 Enforce LDAPS SSL/TLS
> 
> 
> 
> #### 🔹 Encrypt LDAP traffic using port 636
> 
> 
> 
> #### 🔹 Apply ACL Restrictions
> 
> 
> 
> #### 🔹 Limit LDAP query permissions to necessary users only
> 
> 
> 
> #### 🔹 Harden AD Permissions
> 
> 
> 
> #### 🔹 Remove unnecessary permissions
> 
> 
> 
> #### 🔹 Implement least privilege
> 
> 
> 
> #### 🔹 Audit permission changes
> 
> 
> 
> #### 🔹 Enable Signing and Channel Binding
> 
> 
> 
> #### 🔹 Prevent LDAP relay attacks
> 
> 
> 
> #### 🔹 8.3 NFS Countermeasures
> 
> 
> 
> #### 🔹 NFS Hardening
> 
> 
> 
> #### 🔹 Restrict Exports to Specific Hosts
> 
>
> ---
>

> [!NOTE]- 📄 **Pages 36 to 39 Syllabus Content**
>
> ### 📍 Page 36
>
> 
> #### 🔹 # /etc/exports
> 
> 
> 
> #### 🔹 /shared 192.168.1.0/24(ro,root_squash,no_subtree_check)
> 
> 
> 
> #### 🔹 Enable root_squash
> 
> 
> 
> #### 🔹 Map root user to anonymous UID
> 
> 
> 
> #### 🔹 Disable NFS if Not Required
> 
> 
> 
> #### 🔹 Remove NFS packages from systems not file sharing
> 
> 
> 
> #### 🔹 Use NFSv4 with Kerberos
> 
> 
> 
> #### 🔹 Implement strong authentication
> 
> 
> 
> #### 🔹 Firewall NFS Ports
> 
> 
> 
> #### 🔹 Block NFS traffic from public networks
> 
> 
> iptables A INPUT -p tcp --dport 2049 -s 192.168.1.0/24 -j ACCEPT
> 
> 
> #### 🔹 iptables A INPUT -p tcp --dport 2049 -j DROP
> 
> 
> 
> #### 🔹 8.4 SMTP Countermeasures
> 
> 
> 
> #### 🔹 SMTP Hardening
> 
> 
> 
> #### 🔹 Disable VRFY and EXPN Commands
> 
> 
> 
> #### 🔹 Postfix:
> 
> 
> 
> #### 🔹 # /etc/postfix/main.cf
> 
> 
> 
> #### 🔹 disable_vrfy_command = yes
> 
> 
> 
> #### 🔹 Sendmail:
> 
> 
> 
> #### 🔹 # /etc/mail/sendmail.cf
> 
> 
> 
> #### 🔹 O PrivacyOptions=goaway
> 
> 
> 
> #### 🔹 Enforce Authentication
> 
> 
> 
> #### 🔹 Require SMTP AUTH for all connections
> 
> 
> 
> #### 🔹 Hide Version Information
> 
> 
> 
> #### 🔹 Modify SMTP banners to remove version details
> 
>
> ---
>
> ### 📍 Page 37
>
> 
> #### 🔹 Implement Rate Limiting
> 
> 
> 
> #### 🔹 Limit connections and commands per IP
> 
> 
> 
> #### 🔹 Use SMTP Tarpitting
> 
> 
> 
> #### 🔹 Delay responses to suspected enumeration attempts
> 
> 
> 
> #### 🔹 Deploy Greylisting
> 
> 
> 
> #### 🔹 Temporarily reject first-time senders
> 
> 
> 
> #### 🔹 8.5 SMB Countermeasures
> 
> 
> 
> #### 🔹 SMB Security
> 
> 
> 
> #### 🔹 Disable SMBv1
> 
> 
> 
> #### 🔹 Remove outdated and vulnerable SMB version
> 
> 
> 
> #### 🔹 # Windows
> 
> 
> Disable-WindowsOptionalFeature Online FeatureName SMB1Protocol
> 
> 
> #### 🔹 Use Firewall Filtering
> 
> 
> 
> #### 🔹 Block SMB from untrusted networks
> 
> 
> iptables A INPUT -p tcp --dport 445 -s 10.0.0.0/8 -j ACCEPT
> 
> 
> #### 🔹 iptables A INPUT -p tcp --dport 445 -j DROP
> 
> 
> 
> #### 🔹 Require Strong Authentication
> 
> 
> 
> #### 🔹 Disable null sessions
> 
> 
> 
> #### 🔹 Enforce NTLMv2 or Kerberos
> 
> 
> 
> #### 🔹 Implement SMB signing
> 
> 
> 
> #### 🔹 Restrict Share Permissions
> 
> 
> 
> #### 🔹 Apply least privilege
> 
> 
> 
> #### 🔹 Remove Everyone group permissions
> 
> 
> 
> #### 🔹 Audit share access regularly
> 
> 
> 
> #### 🔹 Block External SMB Traffic
> 
> 
> 
> #### 🔹 SMB should never be exposed to the Internet
> 
>
> ---
>
> ### 📍 Page 38
>
> 
> #### 🔹 8.6 DNS Enumeration Countermeasures
> 
> 
> 
> #### 🔹 DNS Security
> 
> 
> 
> #### 🔹 Restrict Zone Transfers
> 
> 
> 
> #### 🔹 Limit AXFR to authorized secondary name servers only
> 
> 
> 
> #### 🔹 # BIND configuration
> 
> 
> 
> #### 🔹 zone "example.com" {
> 
> 
> 
> #### 🔹 type master;
> 
> 
> 
> #### 🔹 file "/etc/bind/db.example.com";
> 
> 
> 
> #### 🔹 allow-transfer  192.168.1.2; };
> 
> 
> 
> #### 🔹 };
> 
> 
> 
> #### 🔹 Disable Recursive Queries
> 
> 
> 
> #### 🔹 For authoritative name servers, disable recursion
> 
> 
> 
> #### 🔹 recursion no;
> 
> 
> 
> #### 🔹 Implement DNSSEC
> 
> 
> 
> #### 🔹 Authenticate DNS responses and prevent spoofing
> 
> 
> 
> #### 🔹 Rate Limit DNS Queries
> 
> 
> 
> #### 🔹 Prevent DNS enumeration and amplification attacks
> 
> 
> 
> #### 🔹 Monitor DNS Query Logs
> 
> 
> 
> #### 🔹 Detect reconnaissance attempts and anomalous queries
> 
> 
> 
> #### 🔹 Split-Horizon DNS
> 
> 
> Provide different responses to internal vs. external queries
>
> ---
>
> ### 📍 Page 39
>
> 
> #### 🔹 ✅Module Summary
> 
> 
> This module covered comprehensive enumeration techniques across
> 
> 
> #### 🔹 multiple protocols and services. Key takeaways include:
> 
> 
> Active Nature: Enumeration requires direct interaction with target
> 
> 
> #### 🔹 systems
> 
> 
> Protocol Diversity: Different protocols reveal different types of
> 
> 
> #### 🔹 information
> 
> 
> Tool Proficiency: Mastering various enumeration tools is essential AI Enhancement: AI significantly improves enumeration efficiency
> 
> 
> #### 🔹 and analysis
> 
> 
> 
> #### 🔹 Defense: Implementing proper countermeasures reduces
> 
> 
> 
> #### 🔹 enumeration effectiveness
> 
> 
> Enumeration bridges the gap between scanning and exploitation,
> 
> 
> #### 🔹 providing the detailed information necessary for successful
> 
> 
> penetration testing. Understanding both offensive enumeration
> 
> 
> #### 🔹 techniques and defensive countermeasures is critical for
> 
> 
> comprehensive security assessment.
>
> ---
>
