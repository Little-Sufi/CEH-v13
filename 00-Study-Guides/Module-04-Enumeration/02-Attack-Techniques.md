# 02. Attack Techniques — Enumeration

> [!WARNING] ⚡ **Offensive Enumeration Methodologies & Command Syntax**
> Direct extraction from official CEH v13 Syllabus (Module 04). Covers SMB Enumeration, SNMP Management Information Base (MIB) Querying, LDAP Search Syntax, SMTP Mailbox Enumeration, IPsec IKE Probing, and VoIP SIP Extension Discovery.

---

## ⚔️ 1. SNMP & MIB Architecture Enumeration

### 1.1 Management Information Base (MIB) Structure & PDUs
SNMP relies on two default community strings for read/write access:
- `public`: Default read-only community string.
- `private`: Default read-write community string.

SNMP operations utilize Protocol Data Units (PDUs): `GetRequest`, `GetNextRequest`, `SetRequest`, `GetResponse`, `Trap`, `GetBulkRequest`, and `InformRequest`.

SNMP objects are structured hierarchically in a MIB tree using Object Identifiers (OIDs):
- `1.3.6.1.2.1.1.1` (`sysDescr`): System description, kernel version, OS.
- `1.3.6.1.2.1.25.4.2.1.2` (`hrSWRunName`): List of currently running processes.
- `1.3.6.1.4.1.77.1.2.25`: List of local user accounts on Windows hosts.
- `1.3.6.1.2.1.6.13.1.3`: Listening TCP ports.

> [!DANGER] 🛡️ **📋 Comprehensive SNMP MIB OID Reference Matrix**

| OID String | Object Name | Metadata Disclosed | Attack Value |
| :--- | :--- | :--- | :--- |
| `1.3.6.1.2.1.1.1` | `sysDescr` | OS hardware & software version | Discovers outdated vulnerable OS |
| `1.3.6.1.2.1.25.4.2.1.2` | `hrSWRunName` | Running process executable names | Identifies active security daemons |
| `1.3.6.1.4.1.77.1.2.25` | `sysUsers` | Windows user account names | Discovers valid username accounts |
| `1.3.6.1.2.1.6.13.1.3` | `tcpConnLocalPort` | Listening local TCP ports | Enumerates internal network services |
| `1.3.6.1.2.1.2.2.1.6` | `ifPhysAddress` | Physical MAC addresses | Discovers network interface hardware |

---

## 🛡️ 2. Advanced Service Enumeration Mechanics

### 2.1 LDAP Naming Conventions & Search Syntax
LDAP entries use hierarchical Distinguished Names (DNs):
- **DN (Distinguished Name)**: `CN=John Smith,OU=Engineering,DC=corp,DC=com`
- **CN (Common Name)**: `John Smith`
- **OU (Organizational Unit)**: `Engineering`
- **DC (Domain Component)**: `corp` / `com`

#### Command Syntax:
```bash
ldapsearch -x -h 10.0.0.5 -b "dc=corp,dc=com" "(objectClass=user)" sAMAccountName
```

### 2.2 IPsec / IKE VPN Enumeration (`ike-scan`)
VPN endpoints are probed using `ike-scan` to determine encryption algorithms and extract Aggressive Mode pre-shared key (PSK) hashes for offline cracking.
```bash
ike-scan -M -A -P psk_hash.txt 192.168.1.1
```

> [!SHIELD] 🏰 **📋 Comprehensive Service Enumeration Execution Reference Matrix**

| Target Service | Attack Command / Tool Example | Expected Output / Intelligence |
| :--- | :--- | :--- |
| **SMB Shares** | `smbclient -L //192.168.1.10 -N` | Displays listing of accessible share folders |
| **Enum4linux** | `enum4linux -a 192.168.1.10` | Full automated dump of users, groups & shares |
| **SNMP Walk** | `snmpwalk -v2c -c public 10.0.0.1` | Dumps complete MIB tree hierarchy |
| **LDAP Search** | `ldapsearch -x -h 10.0.0.5 -b "dc=corp,dc=com"` | Dumps Active Directory directory schema |
| **SMTP VRFY** | `smtp-user-enum -M VRFY -U users.txt -t 10.0.0.1` | Identifies valid corporate email accounts |
| **IPsec IKE** | `ike-scan -A -M 192.168.1.1` | Aggressive Mode PSK hash extraction |
| **VoIP / SIP** | `svmap 192.168.1.0/24` | Scans for active SIP VoIP gateways |
