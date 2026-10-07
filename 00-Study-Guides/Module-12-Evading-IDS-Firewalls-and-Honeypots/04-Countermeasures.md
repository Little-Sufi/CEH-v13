# 04. Countermeasures — Evading IDS, Firewalls, and Honeypots

> [!SHIELD] 🏰 **Defensive Hardening Standards & Detection Rule Audit**
> Direct technical extraction from official CEH v13 Syllabus (Module 12). Covers IP Reassembly Normalization, Stateful Inspection, WAF Hardening, and Firewall ACL Shadowing Resolution.

---

## 🛡️ 1. Defensive Hardening & Mitigations

### 1.1 Technical Defenses Against Evasion

1. **IP Packet Reassembly Normalization**: Configure inline NIPS engines to perform full TCP stream and IP packet reassembly prior to running signature evaluation routines.
2. **Deep Packet Inspection (DPI)**: Enforce DPI on NGFWs to inspect Layer 7 protocol contents regardless of non-standard port numbers.
3. **Firewall ACL Shadowing Resolution**: Regularly audit firewall Access Control Lists to resolve shadowed rules (where top rules inadvertently match traffic intended for bottom restrictive rules).

> [!SHIELD] 🏰 **📋 Comprehensive Evasion Mitigation Reference Matrix**

| Evasion Vector | Defensive Technology | Configuration Standard | Operational Outcome |
| :--- | :--- | :--- | :--- |
| **IP Fragmentation** | NIPS Stream Normalizer | Enable `stream5` / `resequence` | Reassembles fragments before signature scan |
| **URL Double Encoding**| WAF Input Normalizer | Enable multi-pass URL decoding | Decodes all input layers before regex scan |
| **DNS Tunneling** | Egress DNS Monitoring | Block external direct UDP 53; enforce internal DNS | Detects high-frequency TXT/ANY query volume |
