# 03. Tools — Evading IDS, Firewalls, and Honeypots

> [!TOOL] 🛠️ **Command-Line & GUI Software Reference Matrix**
> Direct technical extraction from official CEH v13 Syllabus (Module 12). Covers Nmap, Snort, Suricata, Fragroute, Iodine, Dnscat2, Proxychains, and Canary Tokens.

---

## 🛠️ 1. Primary Evasion & IDS Software Reference Matrix

> [!TOOL] 📋 **Comprehensive IDS / Firewall Evasion Tools Reference Matrix**

| Software Name | Operational Category | Primary Technical Capability | Supported Platform |
| :--- | :--- | :--- | :--- |
| **Snort / Suricata** | Open-source NIDS/NIPS | Signature-based rules, DPI, packet logging | Linux, Windows |
| **Nmap** | Network Port Scanner | Decoy scanning (`-D`), Idle scan (`-sI`), fragmentation | Cross-platform |
| **Fragroute** | Evasion Testing Suite | Intercepts, modifies, and fragments egress IP traffic | Linux |
| **Iodine / Dnscat2** | DNS Tunneling Suite | Tunnels IPv4 data through DNS queries over port 53 | Cross-platform |
| **Proxychains** | Proxy Wrapper | Forces application traffic through SOCKS4/5 proxies | Linux |
| **HoneyD** | Low-Interaction Honeypot | Emulates virtual hosts and open port services | Linux |
