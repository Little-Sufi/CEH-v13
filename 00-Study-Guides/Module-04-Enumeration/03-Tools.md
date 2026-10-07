# 03. Tools — Enumeration

> [!TOOL] 🛠️ **Command-Line & GUI Software Reference Matrix**
> Direct technical extraction from official CEH v13 Syllabus (Module 04). Covers Enum4linux, Smbclient, Snmpcheck, Ldp.exe, BloodHound, RPCclient, Ike-scan, and SIPVicious (`svmap`/`svwar`).

---

## 🛠️ 1. Primary Enumeration Tools Reference Matrix

> [!TOOL] 📋 **Comprehensive Enumeration Software Reference Matrix**

| Utility Name | Primary Protocol | Operational Capability | Compatible OS |
| :--- | :---: | :--- | :--- |
| **Enum4linux** | SMB / RPC | Wraps `rpcclient` to dump SMB shares, users & password policies | Linux |
| **rpcclient** | MS-RPC | Issues raw RPC calls (`enumdomusers`, `querydispinfo`) | Linux |
| **snmp-check** | SNMP | Queries SNMP MIB tree to enumerate network interfaces & processes | Linux, Windows |
| **ldp.exe** | LDAP | GUI LDAP browser tool for querying Active Directory | Windows |
| **BloodHound** | LDAP / Kerberos | Uses graph theory to map Active Directory attack paths | Linux, Windows |
| **ike-scan** | IPsec / IKE | Scans VPN gateways for IKE transforms & PSK hashes | Linux, macOS |
| **SIPVicious (`svmap`)**| SIP / VoIP | Scans IP ranges for listening SIP PBX phone servers | Linux |

---

## 💻 2. Execution CLI Commands

### 2.1 RPCClient Command Usage
- **Connect anonymously**: `rpcclient -U "" 192.168.1.100`
- **Enumerate domain users**: `enumdomusers`
- **Enumerate domain groups**: `enumdomgroups`
- **Query specific user SID info**: `queryuser 0x1f4`

### 2.2 SIPVicious VoIP Toolsuite Usage
- **Scan IP subnet for SIP gateways**: `svmap 192.168.1.0/24`
- **Enumerate extension numbers on PBX**: `svwar -m INVITE 192.168.1.50`
