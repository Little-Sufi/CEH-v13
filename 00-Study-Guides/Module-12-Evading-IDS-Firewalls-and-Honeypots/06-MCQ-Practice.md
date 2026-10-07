# 🎯 Module 12: Evading IDS, Firewalls, and Honeypots - Exam Scenario Practice Engine

> [!ABSTRACT] 📊 **Interactive Module Scorecard**
>
> - **Target Module**: Module 12: Evading IDS, Firewalls, and Honeypots
> - **Total Questions**: 25 Ultra-Detailed, 100% Unique Indirect Scenarios
> - **Exam Difficulty Standard**: Senior CEH v13 (Scenario-Driven Logic & Technical Deduction)
> - **Passing Threshold**: 85% Accuracy (22/25 Correct)
> 
> *Instructions: Evaluate the scenario context below. Select your choice, then expand the **Show Correct Answer & Exam Breakdown** callout to verify your answer and review the deep technical analysis and distractor refutations.*

---

### 🧩 Question 01 | Scenario Challenge

> [!QUESTION] 📌 **Scenario Context**
> An attacker splits a single malicious exploit payload across 50 small IP fragments to bypass an inline Network Intrusion Detection System (NIDS) that fails to reassemble fragmented packets.
>
> What evasion technique was executed?

#### 🔘 Available Options:

- **A**: IP Fragmentation Attack
- **B**: Session Splicing
- **C**: Decoy Scanning
- **D**: MAC Flooding

> [!SUCCESS]- 🔑 **Show Correct Answer & Exam Breakdown**
> **Correct Answer**: **Option A**
>
> #### 💡 Technical Deep Dive:
> IP Fragmentation breaks IP packets into smaller fragments to evade signature detection on NIDS engines that do not reassemble packet streams.
>
> #### 🚫 Distractor Analysis & Refutations:
>
> - **Option B is incorrect** because Session Splicing operates at the TCP layer.
> - **Option C is incorrect** because Decoy Scanning uses fake source IPs.
> - **Option D is incorrect** because MAC Flooding fills switch tables.

---

### 🧩 Question 02 | Scenario Challenge

> [!QUESTION] 📌 **Scenario Context**
> What firewall architecture inspects stateful connection tables (tracking TCP 3-way handshakes, SYN/ACK sequence numbers, and connection states) at Layer 3 and Layer 4?

#### 🔘 Available Options:

- **A**: Stateful Inspection Firewall
- **B**: Packet Filtering Firewall
- **C**: Application Proxy Firewall
- **D**: Circuit-Level Gateway

> [!SUCCESS]- 🔑 **Show Correct Answer & Exam Breakdown**
> **Correct Answer**: **Option A**
>
> #### 💡 Technical Deep Dive:
> Stateful Inspection firewalls keep track of active connection state tables to filter unestablished or out-of-order packets.
>
> #### 🚫 Distractor Analysis & Refutations:
>
> - **Option B is incorrect** because Packet Filtering firewalls inspect headers statelessly.
> - **Option C is incorrect** because Application Proxies inspect Layer 7 payloads.
> - **Option D is incorrect** because Circuit-Level Gateways inspect SOCKS sessions.

---

### 🧩 Question 03 | Scenario Challenge

> [!QUESTION] 📌 **Scenario Context**
> An attacker deploys a fake, highly restricted decoy system designed to log unauthorized access attempts, capture attacker TTPs, and alert SOC analysts without housing production data.
>
> What system is described?

#### 🔘 Available Options:

- **A**: Honeypot
- **B**: DMZ
- **C**: Proxy Server
- **D**: VLAN

> [!SUCCESS]- 🔑 **Show Correct Answer & Exam Breakdown**
> **Correct Answer**: **Option A**
>
> #### 💡 Technical Deep Dive:
> A Honeypot is a trap system configured to detect, deflect, or study unauthorized access attempts.
>
> #### 🚫 Distractor Analysis & Refutations:
>
> - **Option B is incorrect** because DMZ is a demilitarized network segment.
> - **Option C is incorrect** because Proxy Server forwards client traffic.
> - **Option D is incorrect** because VLAN segments local switches.

---

### 🧩 Question 04 | Scenario Challenge

> [!QUESTION] 📌 **Scenario Context**
> What Nmap scan option (`-D RND:10`) generates 10 random decoy IP addresses to obscure the real source IP address of the scanner in target firewall logs?

#### 🔘 Available Options:

- **A**: Decoy Scan (`-D`)
- **B**: Idle Scan (`-sI`)
- **C**: FIN Scan (`-sF`)
- **D**: ACK Scan (`-sA`)

> [!SUCCESS]- 🔑 **Show Correct Answer & Exam Breakdown**
> **Correct Answer**: **Option A**
>
> #### 💡 Technical Deep Dive:
> Decoy scanning (`-D`) spoofs multiple fake source IP addresses alongside the real IP to confuse log analysis.
>
> #### 🚫 Distractor Analysis & Refutations:
>
> - **Option B is incorrect** because Idle Scan uses a zombie host IP.
> - **Option C is incorrect** because FIN Scan sends TCP FIN packets.
> - **Option D is incorrect** because ACK Scan checks firewall filtering rules.

---

### 🧩 Question 05 | Scenario Challenge

> [!QUESTION] 📌 **Scenario Context**
> What technique sends TCP data payloads 1 byte at a time across multiple TCP packets to evade signature-based NIDS inspection?

#### 🔘 Available Options:

- **A**: Session Splicing
- **B**: IP Fragmentation
- **C**: URL Encoding
- **D**: Obfuscation

> [!SUCCESS]- 🔑 **Show Correct Answer & Exam Breakdown**
> **Correct Answer**: **Option A**
>
> #### 💡 Technical Deep Dive:
> Session Splicing splits attack payloads into multiple small TCP segments to prevent signature matching.
>
> #### 🚫 Distractor Analysis & Refutations:
>
> - **Option B is incorrect** because IP Fragmentation operates at Layer 3.
> - **Option C is incorrect** because URL Encoding encodes web strings.
> - **Option D is incorrect** because Obfuscation hides code logic.

---

### 🧩 Question 06 | Scenario Challenge

> [!QUESTION] 📌 **Scenario Context**
> What honeypot classification describes a low-interaction decoy that only simulates basic network services (e.g., listening ports 21, 80, 22) without running a full underlying OS kernel?

#### 🔘 Available Options:

- **A**: Low-Interaction Honeypot
- **B**: High-Interaction Honeypot
- **C**: Production Honeypot
- **D**: Research Honeypot

> [!SUCCESS]- 🔑 **Show Correct Answer & Exam Breakdown**
> **Correct Answer**: **Option A**
>
> #### 💡 Technical Deep Dive:
> Low-interaction honeypots simulate services and protocols to collect basic threat intelligence without giving attackers OS root access.
>
> #### 🚫 Distractor Analysis & Refutations:
>
> - **Option B is incorrect** because High-Interaction honeypots run real OS kernels.
> - **Option C is incorrect** because Production honeypots protect real corporate networks.
> - **Option D is incorrect** because Research honeypots gather complex zero-day malware analytics.

---

### 🧩 Question 07 | Scenario Challenge

> [!QUESTION] 📌 **Scenario Context**
> An attacker uses `nmap -sA 192.168.1.50` to probe a target network. What specific intelligence does an ACK scan reveal?

#### 🔘 Available Options:

- **A**: Determines whether the target firewall is Stateful or Stateless and identifies filtered vs unfiltered ports
- **B**: Identifies open web server vulnerabilities
- **C**: Cracks target SSH passwords
- **D**: Dumps database tables

> [!SUCCESS]- 🔑 **Show Correct Answer & Exam Breakdown**
> **Correct Answer**: **Option A**
>
> #### 💡 Technical Deep Dive:
> TCP ACK scans (`-sA`) send ACK packets; un-responded or RST packets indicate whether ports are filtered by stateful firewalls.
>
> #### 🚫 Distractor Analysis & Refutations:
>
> - **Option B is incorrect** because ACK scans do not scan application vulnerabilities.
> - **Option C is incorrect** because ACK scans do not crack passwords.
> - **Option D is incorrect** because ACK scans do not query databases.

---

### 🧩 Question 08 | Scenario Challenge

> [!QUESTION] 📌 **Scenario Context**
> What tool evasion feature converts HTTP request URLs into hex format (`%2f%61%64%6d%69%6e`) to bypass simple string-matching WAF rules?

#### 🔘 Available Options:

- **A**: URL Encoding / Obfuscation
- **B**: Session Splicing
- **C**: Tunneling
- **D**: Steganography

> [!SUCCESS]- 🔑 **Show Correct Answer & Exam Breakdown**
> **Correct Answer**: **Option A**
>
> #### 💡 Technical Deep Dive:
> URL Encoding replaces characters with `%` hexadecimal equivalents to bypass naive text string WAF filters.
>
> #### 🚫 Distractor Analysis & Refutations:
>
> - **Option B is incorrect** because Session Splicing splits TCP packets.
> - **Option C is incorrect** because Tunneling encapsulates protocols.
> - **Option D is incorrect** because Steganography hides data inside images.

---

### 🧩 Question 09 | Scenario Challenge

> [!QUESTION] 📌 **Scenario Context**
> Which Next-Generation Firewall (NGFW) capability performs Deep Packet Inspection (DPI) to identify application layer protocols (e.g., Skype, BitTorrent) regardless of destination port?

#### 🔘 Available Options:

- **A**: Application Identification (App-ID) & DPI
- **B**: Port Security
- **C**: Static Routing
- **D**: NAT Mapping

> [!SUCCESS]- 🔑 **Show Correct Answer & Exam Breakdown**
> **Correct Answer**: **Option A**
>
> #### 💡 Technical Deep Dive:
> NGFW App-ID uses DPI to identify protocol signatures regardless of non-standard port numbers.
>
> #### 🚫 Distractor Analysis & Refutations:
>
> - **Option B is incorrect** because Port Security operates at Layer 2 MACs.
> - **Option C is incorrect** because Static Routing routes IP packets.
> - **Option D is incorrect** because NAT translates IP addresses.

---

### 🧩 Question 10 | Scenario Challenge

> [!QUESTION] 📌 **Scenario Context**
> What open-source software tool provides an inline Network Intrusion Prevention System (NIPS) using rule-based signature detection syntax (`alert tcp any any -> any 80`)?

#### 🔘 Available Options:

- **A**: Snort / Suricata
- **B**: Wireshark
- **C**: Metasploit
- **D**: Hashcat

> [!SUCCESS]- 🔑 **Show Correct Answer & Exam Breakdown**
> **Correct Answer**: **Option A**
>
> #### 💡 Technical Deep Dive:
> Snort and Suricata are premier open-source NIDS/NIPS platforms using signature rules.
>
> #### 🚫 Distractor Analysis & Refutations:
>
> - **Option B is incorrect** because Wireshark is a passive sniffer.
> - **Option C is incorrect** because Metasploit is an exploit framework.
> - **Option D is incorrect** because Hashcat is a password cracker.

---

### 🧩 Question 11 | Scenario Challenge

> [!QUESTION] 📌 **Scenario Context**
> An attacker uses SSH Dynamic Port Forwarding (`ssh -D 1080 user@pivot`) to tunnel internal subnet traffic through a compromised gateway server.
>
> What technique is this?

#### 🔘 Available Options:

- **A**: SOCKS Proxy Tunneling
- **B**: IP Fragmentation
- **C**: DNS Spoofing
- **D**: MAC Flooding

> [!SUCCESS]- 🔑 **Show Correct Answer & Exam Breakdown**
> **Correct Answer**: **Option A**
>
> #### 💡 Technical Deep Dive:
> SSH Dynamic Port Forwarding creates a local SOCKS proxy server that tunnels arbitrary traffic through an encrypted SSH connection.
>
> #### 🚫 Distractor Analysis & Refutations:
>
> - **Option B is incorrect** because IP Fragmentation breaks IP packets.
> - **Option C is incorrect** because DNS Spoofing alters domain resolution.
> - **Option D is incorrect** because MAC Flooding fills switch tables.

---

### 🧩 Question 12 | Scenario Challenge

> [!QUESTION] 📌 **Scenario Context**
> What type of decoy deployment integrates fake credentials or files (e.g., `passwords.txt` or AWS access keys) into production systems to alert SOC analysts when accessed?

#### 🔘 Available Options:

- **A**: Canary Tokens / Honeytokens
- **B**: Sandbox
- **C**: Firewall ACL
- **D**: VPN Tunnel

> [!SUCCESS]- 🔑 **Show Correct Answer & Exam Breakdown**
> **Correct Answer**: **Option A**
>
> #### 💡 Technical Deep Dive:
> Honeytokens or Canary Tokens are decoy data assets (API keys, files, DB records) that trigger instant alerts when accessed by attackers.
>
> #### 🚫 Distractor Analysis & Refutations:
>
> - **Option B is incorrect** because Sandboxes isolate malware execution.
> - **Option C is incorrect** because Firewall ACLs filter IP traffic.
> - **Option D is incorrect** because VPN Tunnels encrypt connections.

---

### 🧩 Question 13 | Scenario Challenge

> [!QUESTION] 📌 **Scenario Context**
> An attacker modifies the IP header Time-To-Live (TTL) field so that an attack packet reaches a target NIDS (TTL=5) but expires before reaching the destination host behind it (TTL=3).
>
> What evasion attack is described?

#### 🔘 Available Options:

- **A**: Insertion Attack
- **B**: Evasion Attack
- **C**: Session Splicing
- **D**: Denial of Service

> [!SUCCESS]- 🔑 **Show Correct Answer & Exam Breakdown**
> **Correct Answer**: **Option A**
>
> #### 💡 Technical Deep Dive:
> An Insertion Attack tricks an NIDS into accepting a packet that the destination end-host will drop due to TTL expiration.
>
> #### 🚫 Distractor Analysis & Refutations:
>
> - **Option B is incorrect** because Evasion Attack causes the host to accept a packet the NIDS dropped.
> - **Option C is incorrect** because Session Splicing splits TCP packets.
> - **Option D is incorrect** because DoS degrades availability.

---

### 🧩 Question 14 | Scenario Challenge

> [!QUESTION] 📌 **Scenario Context**
> What type of IDS evasion occurs when an attacker crafts a packet that the NIDS rejects or ignores, but the destination target end-system accepts and executes?

#### 🔘 Available Options:

- **A**: Evasion Attack
- **B**: Insertion Attack
- **C**: Buffer Overflow
- **D**: Replay Attack

> [!SUCCESS]- 🔑 **Show Correct Answer & Exam Breakdown**
> **Correct Answer**: **Option A**
>
> #### 💡 Technical Deep Dive:
> An Evasion Attack causes the NIDS to miss a malicious packet that is successfully processed and executed by the destination host.
>
> #### 🚫 Distractor Analysis & Refutations:
>
> - **Option B is incorrect** because Insertion attack causes NIDS to see packets the end-host drops.
> - **Option C is incorrect** because Buffer Overflow overwrites memory.
> - **Option D is incorrect** because Replay Attack retransmits packets.

---

### 🧩 Question 15 | Scenario Challenge

> [!QUESTION] 📌 **Scenario Context**
> An attacker uses DNS Tunneling (`iodine` or `dnscat2`) to exfiltrate sensitive data out of a restrictive enterprise network over outbound UDP port 53.
>
> What technique is executed?

#### 🔘 Available Options:

- **A**: DNS Tunneling Exfiltration
- **B**: DNS Poisoning
- **C**: DNS Amplification
- **D**: Zone Transfer

> [!SUCCESS]- 🔑 **Show Correct Answer & Exam Breakdown**
> **Correct Answer**: **Option A**
>
> #### 💡 Technical Deep Dive:
> DNS Tunneling encapsulates non-DNS data inside DNS query and response records to bypass firewall outbound restrictions.
>
> #### 🚫 Distractor Analysis & Refutations:
>
> - **Option B is incorrect** because DNS Poisoning alters DNS cache.
> - **Option C is incorrect** because DNS Amplification is a DDoS technique.
> - **Option D is incorrect** because Zone Transfer replicates DNS zones.

---

### 🧩 Question 16 | Scenario Challenge

> [!QUESTION] 📌 **Scenario Context**
> Which Web Application Firewall (WAF) evasion technique uses double URL encoding (`%2527` for single quote `'`) to bypass single-pass sanitization routines?

#### 🔘 Available Options:

- **A**: Double Encoding
- **B**: SQL Injection
- **C**: CSRF
- **D**: XSS

> [!SUCCESS]- 🔑 **Show Correct Answer & Exam Breakdown**
> **Correct Answer**: **Option A**
>
> #### 💡 Technical Deep Dive:
> Double Encoding applies URL encoding twice to bypass security filters that decode inputs only once.
>
> #### 🚫 Distractor Analysis & Refutations:
>
> - **Option B is incorrect** because SQL Injection is the underlying attack.
> - **Option C is incorrect** because CSRF forces unauthorized actions.
> - **Option D is incorrect** because XSS executes scripts.

---

### 🧩 Question 17 | Scenario Challenge

> [!QUESTION] 📌 **Scenario Context**
> What firewall configuration error occurs when a rule placed higher in an Access Control List (ACL) matches and permits traffic that a lower rule was intended to block?

#### 🔘 Available Options:

- **A**: Rule Shadowing
- **B**: Rule Redundancy
- **C**: Rule Exception
- **D**: Rule Auditing

> [!SUCCESS]- 🔑 **Show Correct Answer & Exam Breakdown**
> **Correct Answer**: **Option A**
>
> #### 💡 Technical Deep Dive:
> Rule Shadowing occurs when a top ACL rule overlaps with and prevents a bottom rule from ever being evaluated.
>
> #### 🚫 Distractor Analysis & Refutations:
>
> - **Option B is incorrect** because Rule Redundancy duplicates identical actions.
> - **Option C is incorrect** because Rule Exception creates sub-rules.
> - **Option D is incorrect** because Rule Auditing logs ACL traffic.

---

### 🧩 Question 18 | Scenario Challenge

> [!QUESTION] 📌 **Scenario Context**
> Which utility allows security testers to bypass firewalls by encapsulating TCP data frames inside ICMP Echo Request packets (`icmptunnel`)?

#### 🔘 Available Options:

- **A**: ICMP Tunneling
- **B**: ARP Poisoning
- **C**: MAC Flooding
- **D**: DHCP Starvation

> [!SUCCESS]- 🔑 **Show Correct Answer & Exam Breakdown**
> **Correct Answer**: **Option A**
>
> #### 💡 Technical Deep Dive:
> ICMP Tunneling encodes arbitrary data inside the payload section of ICMP echo packets to bypass IP/port filters.
>
> #### 🚫 Distractor Analysis & Refutations:
>
> - **Option B is incorrect** because ARP Poisoning maps IP to MAC.
> - **Option C is incorrect** because MAC Flooding fills switch tables.
> - **Option D is incorrect** because DHCP Starvation consumes IP pools.

---

### 🧩 Question 19 | Scenario Challenge

> [!QUESTION] 📌 **Scenario Context**
> An attacker crafts custom TCP flags (`FIN, URG, PSH`) using Nmap (`nmap -sX 192.168.1.1`). What is the name of this scan type?

#### 🔘 Available Options:

- **A**: Xmas Scan
- **B**: NULL Scan
- **C**: FIN Scan
- **D**: SYN Scan

> [!SUCCESS]- 🔑 **Show Correct Answer & Exam Breakdown**
> **Correct Answer**: **Option A**
>
> #### 💡 Technical Deep Dive:
> An Xmas scan lights up a TCP packet like a Christmas tree by setting FIN, URG, and PSH flags simultaneously.
>
> #### 🚫 Distractor Analysis & Refutations:
>
> - **Option B is incorrect** because NULL scan sets zero flags.
> - **Option C is incorrect** because FIN scan sets only FIN flag.
> - **Option D is incorrect** because SYN scan sets SYN flag.

---

### 🧩 Question 20 | Scenario Challenge

> [!QUESTION] 📌 **Scenario Context**
> What TCP scan sets NO flags (`0x00`) to test how target operating systems handle invalid TCP packet flags?

#### 🔘 Available Options:

- **A**: NULL Scan (`-sN`)
- **B**: Xmas Scan (`-sX`)
- **C**: ACK Scan (`-sA`)
- **D**: UDP Scan (`-sU`)

> [!SUCCESS]- 🔑 **Show Correct Answer & Exam Breakdown**
> **Correct Answer**: **Option A**
>
> #### 💡 Technical Deep Dive:
> A NULL scan (`-sN`) sends TCP packets with all control flags cleared (set to zero).
>
> #### 🚫 Distractor Analysis & Refutations:
>
> - **Option B is incorrect** because Xmas scan sets FIN/URG/PSH flags.
> - **Option C is incorrect** because ACK scan sets ACK flag.
> - **Option D is incorrect** because UDP scan sends UDP packets.

---

### 🧩 Question 21 | Scenario Challenge

> [!QUESTION] 📌 **Scenario Context**
> What defensive device acts as an intermediary between internal web clients and external servers, terminating client connections and re-initiating requests on their behalf?

#### 🔘 Available Options:

- **A**: Forward Proxy Server
- **B**: Hub
- **C**: Repeater
- **D**: Modem

> [!SUCCESS]- 🔑 **Show Correct Answer & Exam Breakdown**
> **Correct Answer**: **Option A**
>
> #### 💡 Technical Deep Dive:
> A Forward Proxy terminates client TCP connections, evaluates policy, and initiates outbound requests to internet servers.
>
> #### 🚫 Distractor Analysis & Refutations:
>
> - **Option B is incorrect** because Hubs repeat Layer 1 signals.
> - **Option C is incorrect** because Repeaters amplify physical signals.
> - **Option D is incorrect** because Modems modulate digital to analog.

---

### 🧩 Question 22 | Scenario Challenge

> [!QUESTION] 📌 **Scenario Context**
> An attacker uses obfuscation tools to introduce dead code, register swapping, and instruction reordering into a binary to evade static signature IDS.
>
> What type of obfuscation engine is this?

#### 🔘 Available Options:

- **A**: Metamorphic Obfuscation
- **B**: Polymorphic Encryption
- **C**: Plaintext Hashing
- **D**: Code Signing

> [!SUCCESS]- 🔑 **Show Correct Answer & Exam Breakdown**
> **Correct Answer**: **Option A**
>
> #### 💡 Technical Deep Dive:
> Metamorphic obfuscation completely rewrites binary instruction structures while retaining core program execution.
>
> #### 🚫 Distractor Analysis & Refutations:
>
> - **Option B is incorrect** because Polymorphic encryption encrypts payload with variable keys.
> - **Option C is incorrect** because Hashing generates fixed digests.
> - **Option D is incorrect** because Code Signing validates developer certificates.

---

### 🧩 Question 23 | Scenario Challenge

> [!QUESTION] 📌 **Scenario Context**
> What technology uses isolated decoy environments (running real Windows/Linux kernels) to analyze malware behavior and capture zero-day exploits?

#### 🔘 Available Options:

- **A**: High-Interaction Honeypot / Detonation Sandbox
- **B**: Low-Interaction Honeypot
- **C**: Packet Filter Firewall
- **D**: DNS Server

> [!SUCCESS]- 🔑 **Show Correct Answer & Exam Breakdown**
> **Correct Answer**: **Option A**
>
> #### 💡 Technical Deep Dive:
> High-interaction honeypots allow attackers to interact with actual operating systems to capture deep forensic intelligence.
>
> #### 🚫 Distractor Analysis & Refutations:
>
> - **Option B is incorrect** because Low-Interaction honeypots only emulate port services.
> - **Option C is incorrect** because Packet Filter Firewalls filter IPs/ports.
> - **Option D is incorrect** because DNS Servers resolve hostnames.

---

### 🧩 Question 24 | Scenario Challenge

> [!QUESTION] 📌 **Scenario Context**
> Which WAF detection rule syntax structure monitors incoming HTTP request headers for SQL injection signatures like `' OR '1'='1`?

#### 🔘 Available Options:

- **A**: Regular Expression (Regex) Signature Pattern
- **B**: DHCP Binding Table
- **C**: MAC Address Lookup
- **D**: BGP Path Attribute

> [!SUCCESS]- 🔑 **Show Correct Answer & Exam Breakdown**
> **Correct Answer**: **Option A**
>
> #### 💡 Technical Deep Dive:
> WAFs utilize regex patterns to inspect incoming HTTP payloads for known malicious attack strings.
>
> #### 🚫 Distractor Analysis & Refutations:
>
> - **Option B is incorrect** because DHCP binding maps MACs to IPs.
> - **Option C is incorrect** because MAC lookup maps MACs to ports.
> - **Option D is incorrect** because BGP handles inter-domain routing.

---

### 🧩 Question 25 | Scenario Challenge

> [!QUESTION] 📌 **Scenario Context**
> What is the primary objective of an IDS/Firewall Evasion technique?

#### 🔘 Available Options:

- **A**: To deliver malicious payloads to a target system without triggering security alerts or inline blocking controls
- **B**: To increase network bandwidth speed
- **C**: To format client hard drives
- **D**: To steal physical access badges

> [!SUCCESS]- 🔑 **Show Correct Answer & Exam Breakdown**
> **Correct Answer**: **Option A**
>
> #### 💡 Technical Deep Dive:
> The goal of evasion techniques is to bypass detection engines to successfully deliver payloads.
>
> #### 🚫 Distractor Analysis & Refutations:
>
> - **Option B is incorrect** because evasion does not increase bandwidth.
> - **Option C is incorrect** because formatting drives is destructive malware.
> - **Option D is incorrect** because physical badges relate to physical security.
