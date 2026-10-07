# 05. Course Detailed Notes — Session Hijacking

> [!ABSTRACT] 🏛️ **Comprehensive Syllabus Notes & Technical Reference**
> Direct technical extraction from official CEH v13 Syllabus (Module 11). Covers Kerberos Ticket Replay, Pass-the-Ticket, and Session Entropy Metrics.

---

## 📌 1. Kerberos Pass-the-Ticket & Token Replay

### 1.1 Pass-the-Ticket (PtT) Mechanics
In Active Directory environments, session tickets (Ticket Granting Tickets - TGT) issued by Kerberos KDC can be harvested from LSASS memory using `Mimikatz` (`sekurlsa::tickets /export`). Attackers inject these tickets into their current logon session (`kerberos::pty`) to access domain resources without cracking passwords.

> [!INFO] 📋 **Comprehensive Session Token Entropy Matrix**

| Session Identifier Type | Minimum Bit Length | Recommended Randomness Source | Security Standard |
| :--- | :---: | :--- | :--- |
| **Web Session Cookie** | 128 bits | Cryptographic PRNG (e.g., `/dev/urandom`) | High Entropy / Unpredictable |
| **JWT Token** | 256 bits (HS256/RS256) | HMAC-SHA256 Secret Key | Cryptographically Signed |
