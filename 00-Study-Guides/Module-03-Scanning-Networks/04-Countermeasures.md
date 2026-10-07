# 04. Countermeasures — Scanning Networks

> [!SHIELD] 🏰 **Defensive Security Controls & Hardening Specifications**
> Direct technical extraction from official CEH v13 Syllabus (Module 03). Covers Intrusion Detection/Prevention System (IDS/IPS) Configuration, Snort Rule Writing, Firewall Stateful Packet Inspection, Honeypot Deception Systems, and Server Banner Suppression.

---

## 🛡️ 1. Hardening & Defensive Countermeasures

### 1.1 IDS/IPS Signature Tuning & Snort Rules
To detect active scanning probes (such as SYN sweeps, Xmas scans, or Null scans), network security engineers deploy Intrusion Detection Systems (IDS) like Snort or Suricata.

#### Sample Snort Detection Rules:
- **Detecting Xmas Scan**:
  ```text
  alert tcp any any -> $HOME_NET any (msg:"SCAN Xmas Scan Detected"; flags:FPU; sid:1000001; rev:1;)
  ```
- **Detecting Null Scan**:
  ```text
  alert tcp any any -> $HOME_NET any (msg:"SCAN Null Scan Detected"; flags:0; sid:1000002; rev:1;)
  ```

> [!SHIELD] 🏰 **📋 Comprehensive Network Scanning Countermeasures Reference Matrix**

| Threat Vector | Primary Countermeasure | Technical Implementation | Defensive Tool / Standard |
| :--- | :--- | :--- | :--- |
| **SYN / Xmas Scans** | Deploy Stateful Firewalls & EDR | Block malformed TCP flag combinations | iptables, PfSense, Palo Alto |
| **Port Sweeping** | IDS/IPS Signature Detection | Configure threshold alert rules for rapid connections | Snort, Suricata |
| **Banner Grabbing** | Banner Suppression & Masking | Modify server headers (`ServerTokens Prod`) | Apache, Nginx, IIS config |
| **Host Reconnaissance** | Honeypot Deception Systems | Deploy decoy fake services to capture attackers | Dionaea, Honeyd, Canary |
| **ICMP Ping Sweeps** | Disable ICMP Inbound Responses | Drop ICMP Echo Requests (`Type 8`) at perimeter | Edge Router ACLs |
