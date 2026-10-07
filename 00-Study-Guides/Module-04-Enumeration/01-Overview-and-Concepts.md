# 01. Overview and Concepts — Enumeration

> [!INFO] 📌 **Module Scope & Core Objectives**
> Direct technical extraction from official CEH v13 Syllabus (Module 04). Covers Enumeration Concepts, NetBIOS/SMB Enumeration, SNMP MIB Architecture, LDAP Active Directory Schema, NTP/SMTP Mailbox Discovery, DNS SRV/AXFR Records, IPsec/IKE Probing, and VoIP/SIP Enumeration.

---

## 🧠 1. Fundamental Principles of Network & Service Enumeration

### 1.1 Detailed Analysis of Enumeration Mechanics
Enumeration is the third critical phase of ethical hacking. Unlike passive footprinting or general host discovery, enumeration establishes active connections to target hosts to extract specific technical metadata: valid user accounts, group memberships, network shares, system hostnames, service configurations, SNMP community strings, LDAP directory schemas, and system banners.

#### Key Enumeration Targets & Protocol Scope:
1. **NetBIOS / SMB Enumeration (TCP Ports 139 / 445)**: Enumerates Windows computer names, workgroups, domain controller roles, null session access, active SMB shares, user accounts, and Password Policies.
2. **SNMP Enumeration (UDP Ports 161 / 162)**: Queries Simple Network Management Protocol agents using community strings (`public`, `private`) to extract router interfaces, ARP routing tables, installed software, and system uptime.
3. **LDAP Enumeration (TCP Ports 389 / 636)**: Queries Lightweight Directory Access Protocol services to extract Active Directory user objects, organizational units (OUs), group memberships, and email addresses.
4. **NTP / SMTP Enumeration (UDP Port 123 / TCP Port 25)**: Queries Network Time Protocol for internal system clocks (`monlist`) and leverages SMTP commands (`VRFY`, `EXPN`, `RCPT TO`) to validate legitimate email mailboxes.
5. **DNS SRV & Zone Transfer Enumeration (TCP/UDP Port 53)**: Queries Service (`SRV`) records and Zone Transfers (`AXFR`) to discover Active Directory Domain Controllers (`_kerberos._tcp`, `_ldap._tcp`).
6. **IPsec / IKE & VoIP / SIP Enumeration**: Probes IKE VPN gateways (`ike-scan`) for Pre-Shared Key (PSK) hashes and scans Session Initiation Protocol (`svmap`, `svwar`) endpoints.

> [!ABSTRACT] 🏛️ **📋 Comprehensive Service Enumeration Protocol Reference Matrix**

| Protocol / Service | Standard Port | Primary Metadata Disclosed | Dominant Tool / Utility |
| :--- | :---: | :--- | :--- |
| **NetBIOS Name Service** | UDP 137 / TCP 139 | Workgroups, NetBIOS hostnames, MAC addresses | `nbtstat -A`, `nbtscan` |
| **SMB / CIFS** | TCP 445 | Shared folders, domain users, NULL session data | `enum4linux`, `smbclient`, `crackmapexec` |
| **SNMP** | UDP 161 / 162 | Device uptime, network interfaces, installed apps | `snmpwalk`, `snmp-check`, `onesixtyone` |
| **LDAP** | TCP 389 / 636 | Active Directory OU schema, user accounts, groups | `ldapsearch`, `ldp.exe`, `bloodhound` |
| **SMTP** | TCP 25 | Valid email user mailboxes (`VRFY`, `EXPN`) | `smtp-user-enum`, `nc`, `telnet` |
| **NTP** | UDP 123 | System time, connected peer IPs, OS clock skew | `ntpdate`, `ntpq`, `ntpdc` |
| **DNS SRV / AXFR** | TCP/UDP 53 | AD Domain Controllers, internal host maps | `dig AXFR`, `dnsrecon`, `dnsenum` |
| **IPsec / IKE** | UDP 500 / 4500 | Main/Aggressive mode transform proposals, PSKs | `ike-scan` |
| **VoIP / SIP** | UDP 5060 / 5061 | Extension numbers, SIP gateways, user agents | `svmap`, `svwar`, `sipsak` |

---

## ⚡ 2. NetBIOS & SMB Enumeration Deep Dive

### 2.1 NetBIOS Suffix Codes & NULL Sessions
NetBIOS (Network Basic Input/Output System) relies on 16-character names, where the 16th byte represents a unique suffix code indicating the host's network role:

- `<00>`: Workstation / Unique Host Name.
- `<20>`: File Server Service (SMB enabled).
- `<1B>`: Domain Master Browser.
- `<1C>`: Domain Controller.
- `<03>`: Messenger Service.

#### SMB NULL Sessions (IPC$ Exploitation)
A NULL Session allows an unauthenticated remote connection to a Windows system's `IPC$` (Inter-Process Communication) share using a blank username `""` and blank password `""`.
- **Command**: `net use \\target\IPC$ "" /user:""`
- **Exploitation Impact**: Allows attackers to query Security Identifier (SID) user rid lists, enumerate local shares, and extract domain user policies.

> [!IMPORTANT] 🔄 **📋 Comprehensive NetBIOS Suffix Code Reference Matrix**

| Suffix Code | Hex Identifier | Service / Function Role | Security Significance |
| :---: | :---: | :--- | :--- |
| **`<00>`** | `0x00` | Workstation Service Name | Confirms unique host device identity |
| **`<20>`** | `0x20` | Server Service (File / Print Sharing) | Indicates active SMB share capability |
| **`<1B>`** | `0x1B` | Domain Master Browser | Identifies primary domain browsing host |
| **`<1C>`** | `0x1C` | Domain Controller Group | Identifies Windows Domain Controllers |
| **`<03>`** | `0x03` | Messenger Service | Reveals active logged-in username |
