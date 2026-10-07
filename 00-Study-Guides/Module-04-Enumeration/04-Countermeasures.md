# 04. Countermeasures — Enumeration

> [!SHIELD] 🏰 **Defensive Security Controls & Hardening Specifications**
> Direct technical extraction from official CEH v13 Syllabus (Module 04). Covers Restricting SMB Null Sessions, Securing SNMP Community Strings, Disabling SMTP VRFY/EXPN, and Enforcing LDAP Signing.

---

## 🛡️ 1. Hardening & Defensive Countermeasures

### 1.1 Protocol Hardening Protocols
- **Disable SMB NULL Sessions**: Configure Windows Group Policy `RestrictAnonymous = 2` (No access without explicit anonymous permissions).
- **Secure SNMP**: Upgrade from SNMP v1/v2c (cleartext community strings) to SNMP v3 (enforces USM authentication and AES privacy encryption).
- **Disable SMTP User Verification**: Disable `VRFY` and `EXPN` commands on Postfix/Exchange mail gateways to prevent mailbox enumeration.
- **Enforce LDAP Signing**: Require LDAP signing and channel binding (`LDAPS` over TLS port 636).

> [!SHIELD] 🏰 **📋 Comprehensive Service Hardening Reference Matrix**

| Vulnerable Protocol | Primary Hardening Countermeasure | Registry / Configuration Setting |
| :--- | :--- | :--- |
| **SMB Null Sessions** | Restrict Anonymous Connections | Set `HKLM\System\CurrentControlSet\Control\Lsa\RestrictAnonymous` to `2` |
| **SNMP v1/v2c** | Upgrade to SNMP v3 | Enforce SHA authentication and AES encryption |
| **SMTP VRFY/EXPN** | Disable VRFY/EXPN Commands | Set `disable_vrfy_command = yes` in Postfix config |
| **LDAP Cleartext** | Enforce LDAPS (TLS Port 636) | Require LDAP signing via Group Policy |
