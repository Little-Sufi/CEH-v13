# 02. Attack Techniques — Evading IDS, Firewalls, and Honeypots

> [!WARNING] ⚡ **Exploitation Methodologies & Evasion Execution**
> Direct extraction from official CEH v13 Syllabus (Module 12). Covers Nmap Evasion Scans, Protocol Tunneling (DNS/ICMP/SSH), Double URL Encoding, and Obfuscation Execution.

---

## ⚔️ 1. Primary Evasion Methodologies

### 1.1 Nmap Scanning Evasion Techniques
Security testers leverage Nmap command-line flags to bypass simple stateless firewalls and IDS rules.

- **Decoy Scanning (`-D RND:10`)**: Mixes real scan traffic with 10 spoofed random IP addresses to confuse SOC log analysis.
- **ACK Scanning (`-sA`)**: Sends TCP ACK packets to map firewall statefulness. If a port returns a `RST` packet, the port is **unfiltered**.
- **Idle (Zombie) Scanning (`-sI <zombie_ip>`)**: Uses a silent zombie host's IP and predictable IP ID sequence to scan target ports anonymously.
- **Fragmentation (`-f` or `--mtu 8`)**: Splits Nmap probe headers into small 8-byte MTU fragments to bypass simple signature filters.

### 1.2 Encapsulation & Protocol Tunneling
- **DNS Tunneling**: Tools like `iodine` or `dnscat2` encapsulate arbitrary TCP traffic inside outbound DNS UDP 53 query/response payloads.
- **ICMP Tunneling**: Encapsulates TCP data frames inside ICMP Echo Request payloads (`icmptunnel`).
- **SSH Dynamic Port Forwarding**: Tunnels traffic through encrypted SSH connections (`ssh -D 1080 user@pivot`).

> [!DANGER] 🛡️ **📋 Comprehensive Evasion Execution Reference Matrix**

| Evasion Technique | Target Component | Command / Payload Syntax | Primary Technical Mechanism |
| :--- | :--- | :--- | :--- |
| **Decoy Scanning** | Firewall Logs | `nmap -D RND:10 192.168.1.50` | Spoofs 10 fake source IP addresses |
| **ACK Scan** | Stateful Firewall | `nmap -sA 192.168.1.50` | Probes state table connection rules |
| **Double Encoding** | WAF Input Filter | `%2527` (Double encoded `'`) | Bypasses single-pass WAF decoding |
| **DNS Tunneling** | Perimeter Firewall | `iodine -f -P password tunnel.domain.com` | Encapsulates payloads inside DNS UDP 53 |

---

## 🛡️ 2. Tool Execution CLI Commands

```bash
# 1. Execute Idle Scan using Zombie Host
nmap -Pn -p 80,443 -sI 192.168.1.100 192.168.1.50

# 2. Execute Xmas Scan (FIN, URG, PSH flags)
nmap -sX -p 22,80 192.168.1.50

# 3. Execute Packet Fragmentation Scan
nmap -sS -f --mtu 16 192.168.1.50
```
