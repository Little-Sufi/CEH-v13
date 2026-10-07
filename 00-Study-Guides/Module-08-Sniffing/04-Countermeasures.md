# 04. Countermeasures — Sniffing

> [!SHIELD] 🏰 **Defensive Security Controls & Hardware Hardening**
> Direct technical extraction from official CEH v13 Syllabus (Module 08). Covers Dynamic ARP Inspection (DAI), DHCP Snooping, Port Security, MACsec (802.1AE), and Encrypted Protocols.

---

## 🛡️ 1. Switch Security Hardening & MitM Defenses

### 1.1 Dynamic ARP Inspection (DAI) & DHCP Snooping
To mitigate active sniffing and MitM attacks, network administrators implement hardware switch security features:

1. **DHCP Snooping**: Configures switch ports as trusted or untrusted. Untrusted ports are prevented from sending DHCP Offer or Acknowledgement messages, blocking Rogue DHCP Servers. DHCP Snooping builds a binding table mapping MACs to valid IP leases.
2. **Dynamic ARP Inspection (DAI)**: Intercepts all ARP requests and responses on untrusted ports and validates them against the DHCP Snooping Binding Database. Invalid ARP packets matching forged MACs are automatically dropped.
3. **Port Security**: Limits the maximum number of unique MAC addresses allowed on a single physical switch port (e.g., max 1 MAC address). Violations shutdown the switch port (`err-disable`), preventing MAC Flooding attacks (`macof`).
4. **Encrypted Protocols**: Upgrading legacy cleartext protocols (HTTP, FTP, Telnet, POP3) to secure encrypted equivalents (HTTPS, SFTP, SSH, IMAP over TLS).

> [!SHIELD] 🏰 **📋 Comprehensive Switch Defense Reference Matrix**

| Defensive Control | Switch Mechanism | Attack Mitigated | Configuration Command (Cisco) |
| :--- | :--- | :--- | :--- |
| **Dynamic ARP Inspection** | Validates ARP packets against DHCP bindings | ARP Poisoning / MitM | `ip arp inspection vlan 1` |
| **DHCP Snooping** | Blocks rogue DHCP server responses | DHCP Starvation & Rogue DHCP | `ip dhcp snooping` |
| **Port Security** | Enforces maximum MAC count per port | MAC Flooding (`macof`) | `switchport port-security maximum 1` |
| **MACsec (802.1AE)** | Encrypts Layer 2 ethernet frames between switches | Passive & Active Sniffing | `macsec network-agreement` |
