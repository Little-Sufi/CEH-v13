# 05. Course Detailed Notes — Enumeration

> [!ABSTRACT] 🏛️ **Comprehensive Syllabus Notes & Technical Reference**
> Direct technical extraction from official CEH v13 Syllabus (Module 04). Covers Active Directory Enumeration, SID Structure Parsing, and DNS Zone Transfers.

---

## 📌 1. Windows Security Identifier (SID) Architecture

### 1.1 Relative Identifier (RID) Structure
Windows user and group accounts are identified by Security Identifiers (SIDs). SIDs take the format: `S-1-5-21-domain_identifier-RID`.

#### Standard Relative Identifiers (RIDs):
- **`500`**: Administrator Account (`S-1-5-21-...-500`).
- **`501`**: Guest Account (`S-1-5-21-...-501`).
- **`502`**: KRBTGT (Kerberos Ticket Granting Ticket Account).
- **`512`**: Domain Admins Group.
- **`513`**: Domain Users Group.
- **`1000+`**: Custom domain user accounts created by administrators.

> [!INFO] 📋 **Comprehensive Windows SID / RID Reference Matrix**

| RID Value | Account / Group Name | Security Significance |
| :---: | :--- | :--- |
| **`500`** | Built-in Administrator | High-value target; local administrative rights |
| **`501`** | Built-in Guest | Frequently disabled; weak default security |
| **`502`** | KRBTGT Account | Kerberos master key; target for Golden Ticket |
| **`512`** | Domain Admins Group | Full Active Directory domain administrative control |
| **`513`** | Domain Users Group | Default group for all newly provisioned accounts |
