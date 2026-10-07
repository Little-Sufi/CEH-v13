![Header Image](https://images.unsplash.com/photo-1460925895917-afdab827c52f?w=800&h=200&fit=crop)

# 🗺️ CEH v13 to MITRE ATT&CK Mapping

[⬅️ Tools & References Home](Home.md)

---

## 🔍 Hacking Phases to MITRE ATT&CK Tactics
This guide helps translate standard CEH phases into the industry-standard MITRE ATT&CK framework.

| CEH Hacking Phase | MITRE ATT&CK Tactic | Description | Common Techniques |
|-------------------|--------------------|-------------|-------------------|
| **Footprinting & Recon** | **Reconnaissance (TA0043)** | Gathering information to plan future operations. | Active/Passive scanning, search engines, WHOIS, DNS queries. |
| **Scanning Networks** | **Discovery (TA0007)** | Figuring out the layout of the target network. | Network service discovery, port scanning, OS identification. |
| **Enumeration** | **Discovery (TA0007)** | Querying services directly for user/share information. | SMB share discovery, SNMP queries, LDAP enumeration. |
| **System Hacking** | **Initial Access (TA0001)** / **Execution (TA0002)** | Gaining entry and executing malicious payloads. | Exploit public-facing application, command injection, reverse shell execution. |
| **Privilege Escalation** | **Privilege Escalation (TA0004)** | Elevating credentials to admin (Root / SYSTEM). | Exploiting SUID binaries, kernel exploits, service misconfigurations. |
| **Covering Tracks** | **Defense Evasion (TA0005)** | Hiding evidence of the compromise. | Deleting audit logs, disabling logging, indicator removal on host. |
| **Maintaining Access** | **Persistence (TA0003)** | Ensuring access survives restarts or credential changes. | Creating backdoors, scheduled tasks, registry run keys, SSH keys. |

---

## 🛡️ Defensive Mapping
Understanding how defensive controls map to ATT&CK helps implement proper countermeasures.

- **IDS/IPS (Snort):** Mitigates **Execution (TA0002)** and **Lateral Movement (TA0008)** by detecting anomalies in network traffic.
- **Firewalls:** Restricts **Initial Access (TA0001)** and block unauthorized egress associated with **Command and Control (TA0011)**.
- **WAF:** Protects public-facing applications from **Credential Access (TA0006)** and **Injection** attacks.
- **Endpoint Detection & Response (EDR):** Detects **Privilege Escalation (TA0004)** and **Persistence (TA0003)** anomalies on hosts.

---

[⬅️ Tools & References Home](Home.md)
