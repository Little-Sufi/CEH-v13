# 🎯 Module 10: Denial-of-Service - Exam Scenario Practice Engine

> [!ABSTRACT] 📊 **Interactive Module Scorecard**
>
> - **Target Module**: Module 10: Denial-of-Service
> - **Total Questions**: 25 Ultra-Detailed, 100% Unique Indirect Scenarios
> - **Exam Difficulty Standard**: Senior CEH v13 (Scenario-Driven Logic & Technical Deduction)
> - **Passing Threshold**: 85% Accuracy (22/25 Correct)
> 
> *Instructions: Evaluate the scenario context below. Select your choice, then expand the **Show Correct Answer & Exam Breakdown** callout to verify your answer and review the deep technical analysis and distractor refutations.*

---

### 🧩 Question 01 | Scenario Challenge

> [!QUESTION] 📌 **Scenario Context**
> An attacker sends a flood of TCP SYN packets with spoofed source IP addresses to a corporate web server without completing the 3-way handshake. The server's SYN queue becomes completely exhausted, preventing legitimate TCP connections.
>
> What specific protocol attack vector was executed?

#### 🔘 Available Options:

- **A**: TCP SYN Flooding Attack
- **B**: UDP Flooding Attack
- **C**: HTTP GET Flood
- **D**: Smurf Attack

> [!SUCCESS]- 🔑 **Show Correct Answer & Exam Breakdown**
> **Correct Answer**: **Option A**
>
> #### 💡 Technical Deep Dive:
> SYN Flooding sends TCP SYN packets without sending final ACK responses, consuming server connection queues.
>
> #### 🚫 Distractor Analysis & Refutations:
>
> - **Option B is incorrect** because UDP Flooding sends connectionless UDP packets.
> - **Option C is incorrect** because HTTP GET flood operates at Layer 7.
> - **Option D is incorrect** because Smurf attack uses ICMP broadcast replies.

---

### 🧩 Question 02 | Scenario Challenge

> [!QUESTION] 📌 **Scenario Context**
> An attacker sends an ICMP Echo Request to an IP network broadcast address with the source IP address spoofed as the victim's server IP. All hosts on the network respond to the victim server simultaneously.
>
> What attack vector is described?

#### 🔘 Available Options:

- **A**: Smurf Attack
- **B**: Fraggle Attack
- **C**: Slowloris
- **D**: SYN Flood

> [!SUCCESS]- 🔑 **Show Correct Answer & Exam Breakdown**
> **Correct Answer**: **Option A**
>
> #### 💡 Technical Deep Dive:
> A Smurf attack spoofs the victim's IP and sends ICMP Echo requests to a network broadcast address, generating massive ICMP replies to the victim.
>
> #### 🚫 Distractor Analysis & Refutations:
>
> - **Option B is incorrect** because Fraggle attack uses UDP instead of ICMP.
> - **Option C is incorrect** because Slowloris uses HTTP requests.
> - **Option D is incorrect** because SYN flood uses TCP SYN packets.

---

### 🧩 Question 03 | Scenario Challenge

> [!QUESTION] 📌 **Scenario Context**
> Which Layer 7 DDoS attack tool keeps hundreds of HTTP connections open simultaneously by sending partial HTTP headers at slow intervals to exhaust web server thread pools?

#### 🔘 Available Options:

- **A**: Slowloris
- **B**: LOIC
- **C**: HOIC
- **D**: macof

> [!SUCCESS]- 🔑 **Show Correct Answer & Exam Breakdown**
> **Correct Answer**: **Option A**
>
> #### 💡 Technical Deep Dive:
> Slowloris opens multiple HTTP connections to the target web server and sends partial headers slowly to keep connections open until threads are exhausted.
>
> #### 🚫 Distractor Analysis & Refutations:
>
> - **Option B is incorrect** because LOIC floods UDP/TCP packets.
> - **Option C is incorrect** because HOIC floods high-speed HTTP GET/POST requests.
> - **Option D is incorrect** because macof floods switch MAC tables.

---

### 🧩 Question 04 | Scenario Challenge

> [!QUESTION] 📌 **Scenario Context**
> An attacker sends small UDP requests to public NTP servers with a spoofed source IP of the victim. The NTP servers return massive 486-byte responses for 8-byte queries.
>
> What attack vector was executed?

#### 🔘 Available Options:

- **A**: NTP Amplification Attack
- **B**: DNS Poisoning
- **C**: SYN Flooding
- **D**: HTTP POST Flood

> [!SUCCESS]- 🔑 **Show Correct Answer & Exam Breakdown**
> **Correct Answer**: **Option A**
>
> #### 💡 Technical Deep Dive:
> NTP Amplification exploits open NTP servers (using monlist requests) to reflect and amplify traffic back to a victim.
>
> #### 🚫 Distractor Analysis & Refutations:
>
> - **Option B is incorrect** because DNS Poisoning corrupts DNS cache.
> - **Option C is incorrect** because SYN flooding sends TCP SYN packets.
> - **Option D is incorrect** because HTTP POST flood targets web apps.

---

### 🧩 Question 05 | Scenario Challenge

> [!QUESTION] 📌 **Scenario Context**
> What TCP mechanism can be enabled on web servers to mitigate SYN flooding attacks by encoding connection parameters into the SYN-ACK sequence number without allocating memory buffers?

#### 🔘 Available Options:

- **A**: SYN Cookies
- **B**: RST Suppression
- **C**: TCP Windowing
- **D**: Keep-Alive Packets

> [!SUCCESS]- 🔑 **Show Correct Answer & Exam Breakdown**
> **Correct Answer**: **Option A**
>
> #### 💡 Technical Deep Dive:
> SYN Cookies encode initial sequence parameters into SYN-ACK responses, delaying memory allocation until the final ACK is received.
>
> #### 🚫 Distractor Analysis & Refutations:
>
> - **Option B is incorrect** because RST suppression drops reset packets.
> - **Option C is incorrect** because TCP windowing manages flow control.
> - **Option D is incorrect** because Keep-Alive keeps connections active.

---

### 🧩 Question 06 | Scenario Challenge

> [!QUESTION] 📌 **Scenario Context**
> A DDoS attack utilizes 50,000 compromised IoT devices (cameras and routers) controlled remotely via a C2 server to flood a DNS provider with UDP port 53 traffic.
>
> What attack structure does this represent?

#### 🔘 Available Options:

- **A**: Botnet DDoS Attack (e.g., Mirai)
- **B**: Local ARP Poisoning
- **C**: Man-in-the-Middle Attack
- **D**: Session Hijacking

> [!SUCCESS]- 🔑 **Show Correct Answer & Exam Breakdown**
> **Correct Answer**: **Option A**
>
> #### 💡 Technical Deep Dive:
> Botnets like Mirai compromise weak IoT devices to execute coordinated multi-gigabit DDoS attacks managed by C2 servers.
>
> #### 🚫 Distractor Analysis & Refutations:
>
> - **Option B is incorrect** because ARP poisoning is local network attack.
> - **Option C is incorrect** because MitM intercepts traffic.
> - **Option D is incorrect** because Session Hijacking steals active sessions.

---

### 🧩 Question 07 | Scenario Challenge

> [!QUESTION] 📌 **Scenario Context**
> Which DoS attack sends oversized, fragmented IP packets exceeding 65,535 bytes to crash target operating systems during packet reassembly?

#### 🔘 Available Options:

- **A**: Ping of Death
- **B**: Teardrop Attack
- **C**: Land Attack
- **D**: Smurf Attack

> [!SUCCESS]- 🔑 **Show Correct Answer & Exam Breakdown**
> **Correct Answer**: **Option A**
>
> #### 💡 Technical Deep Dive:
> Ping of Death sends oversized ICMP/IP packets (>65,535 bytes) that cause buffer overflows when target OS reassembles them.
>
> #### 🚫 Distractor Analysis & Refutations:
>
> - **Option B is incorrect** because Teardrop sends overlapping fragmented IP packets.
> - **Option C is incorrect** because Land attack spoofs same IP/port for source and dest.
> - **Option D is incorrect** because Smurf uses broadcast ICMP replies.

---

### 🧩 Question 08 | Scenario Challenge

> [!QUESTION] 📌 **Scenario Context**
> What DoS attack vector sends IP packets where the source IP address and port are forged to match the destination IP address and port, causing the target machine to loop endlessly?

#### 🔘 Available Options:

- **A**: Land Attack
- **B**: Teardrop Attack
- **C**: Smurf Attack
- **D**: Fraggle Attack

> [!SUCCESS]- 🔑 **Show Correct Answer & Exam Breakdown**
> **Correct Answer**: **Option A**
>
> #### 💡 Technical Deep Dive:
> Land attack spoofs the source IP and port to be identical to the destination IP and port, forcing the OS into an infinite processing loop.
>
> #### 🚫 Distractor Analysis & Refutations:
>
> - **Option B is incorrect** because Teardrop uses overlapping fragments.
> - **Option C is incorrect** because Smurf uses broadcast ICMP.
> - **Option D is incorrect** because Fraggle uses UDP.

---

### 🧩 Question 09 | Scenario Challenge

> [!QUESTION] 📌 **Scenario Context**
> An attacker sends fragmented IP packets with overlapping payload offset values, preventing the target kernel from properly reassembling the packet structure.
>
> What attack was executed?

#### 🔘 Available Options:

- **A**: Teardrop Attack
- **B**: Ping of Death
- **C**: Land Attack
- **D**: SYN Flood

> [!SUCCESS]- 🔑 **Show Correct Answer & Exam Breakdown**
> **Correct Answer**: **Option A**
>
> #### 💡 Technical Deep Dive:
> Teardrop attacks exploit vulnerabilities in IP stack reassembly routines by sending overlapping fragmented packets.
>
> #### 🚫 Distractor Analysis & Refutations:
>
> - **Option B is incorrect** because Ping of Death sends oversized packets.
> - **Option C is incorrect** because Land attack loops matching IP/ports.
> - **Option D is incorrect** because SYN flood targets TCP SYN queues.

---

### 🧩 Question 10 | Scenario Challenge

> [!QUESTION] 📌 **Scenario Context**
> What type of DoS attack targets application layer business logic (e.g., executing heavy database queries or PDF rendering requests) to exhaust CPU resources?

#### 🔘 Available Options:

- **A**: Application Layer (Layer 7) DDoS
- **B**: Volumetric DDoS
- **C**: Protocol DDoS
- **D**: ICMP Flood

> [!SUCCESS]- 🔑 **Show Correct Answer & Exam Breakdown**
> **Correct Answer**: **Option A**
>
> #### 💡 Technical Deep Dive:
> Application Layer (Layer 7) DDoS attacks send legitimate-looking HTTP requests that consume heavy CPU/RAM/database resources.
>
> #### 🚫 Distractor Analysis & Refutations:
>
> - **Option B is incorrect** because Volumetric DDoS saturates bandwidth.
> - **Option C is incorrect** because Protocol DDoS targets firewall state tables.
> - **Option D is incorrect** because ICMP flood is a network layer attack.

---

### 🧩 Question 11 | Scenario Challenge

> [!QUESTION] 📌 **Scenario Context**
> Which Cloud-based security defense sits in front of web applications to scrub incoming DDoS traffic, block malicious HTTP requests, and challenge bots with CAPTCHA?

#### 🔘 Available Options:

- **A**: Web Application Firewall (WAF) & Scrubbing Center
- **B**: Host Antivirus
- **C**: Local Switch Port Security
- **D**: DNS Resolver

> [!SUCCESS]- 🔑 **Show Correct Answer & Exam Breakdown**
> **Correct Answer**: **Option A**
>
> #### 💡 Technical Deep Dive:
> Cloud WAFs and DDoS Scrubbing Centers absorb and filter volumetric and application layer DDoS attacks before traffic reaches origin servers.
>
> #### 🚫 Distractor Analysis & Refutations:
>
> - **Option B is incorrect** because host antivirus checks local malware files.
> - **Option C is incorrect** because Port Security protects Layer 2 switches.
> - **Option D is incorrect** because DNS Resolvers resolve IP names.

---

### 🧩 Question 12 | Scenario Challenge

> [!QUESTION] 📌 **Scenario Context**
> What command-line tool in Kali Linux allows security testers to send custom TCP/UDP/ICMP packets with forged headers to simulate DoS packet floods?

#### 🔘 Available Options:

- **A**: hping3
- **B**: Wireshark
- **C**: Nmap
- **D**: Metasploit

> [!SUCCESS]- 🔑 **Show Correct Answer & Exam Breakdown**
> **Correct Answer**: **Option A**
>
> #### 💡 Technical Deep Dive:
> hping3 is a versatile packet craft tool used to perform SYN floods, ICMP floods, and custom DoS packet generation (`hping3 -S --flood`).
>
> #### 🚫 Distractor Analysis & Refutations:
>
> - **Option B is incorrect** because Wireshark is a packet analyzer.
> - **Option C is incorrect** because Nmap is a port scanner.
> - **Option D is incorrect** because Metasploit is an exploit framework.

---

### 🧩 Question 13 | Scenario Challenge

> [!QUESTION] 📌 **Scenario Context**
> What parameter in `hping3` enables high-speed packet generation without waiting for incoming response ICMP/TCP packets?

#### 🔘 Available Options:

- **A**: --flood
- **B**: --fast
- **C**: --listen
- **D**: --syn

> [!SUCCESS]- 🔑 **Show Correct Answer & Exam Breakdown**
> **Correct Answer**: **Option A**
>
> #### 💡 Technical Deep Dive:
> The `--flood` flag instructs `hping3` to send packets as fast as possible without displaying incoming reply packets.
>
> #### 🚫 Distractor Analysis & Refutations:
>
> - **Option B is incorrect** because `--fast` sends 10 packets per second.
> - **Option C is incorrect** because `--listen` waits for incoming packets.
> - **Option D is incorrect** because `--syn` sets TCP SYN flag.

---

### 🧩 Question 14 | Scenario Challenge

> [!QUESTION] 📌 **Scenario Context**
> What DoS attack vector floods open UDP ports across a subnet, generating ICMP Destination Unreachable replies that consume bandwidth?

#### 🔘 Available Options:

- **A**: UDP Flood
- **B**: SYN Flood
- **C**: Slowloris
- **D**: HTTP GET Flood

> [!SUCCESS]- 🔑 **Show Correct Answer & Exam Breakdown**
> **Correct Answer**: **Option A**
>
> #### 💡 Technical Deep Dive:
> UDP Flooding sends high volumes of UDP packets to random target ports, forcing the system to check services and issue ICMP unreachable messages.
>
> #### 🚫 Distractor Analysis & Refutations:
>
> - **Option B is incorrect** because SYN flood uses TCP packets.
> - **Option C is incorrect** because Slowloris uses partial HTTP headers.
> - **Option D is incorrect** because HTTP GET flood uses TCP port 80.

---

### 🧩 Question 15 | Scenario Challenge

> [!QUESTION] 📌 **Scenario Context**
> Which metric measures the volume of a DDoS attack in terms of data transfer rate across network transit links?

#### 🔘 Available Options:

- **A**: Bits per Second (Gbps / Tbps)
- **B**: Packets per Minute
- **C**: Transactions per Hour
- **D**: CPU Cycles per Second

> [!SUCCESS]- 🔑 **Show Correct Answer & Exam Breakdown**
> **Correct Answer**: **Option A**
>
> #### 💡 Technical Deep Dive:
> Volumetric DDoS attacks are measured in Gigabits per second (Gbps) or Terabits per second (Tbps).
>
> #### 🚫 Distractor Analysis & Refutations:
>
> - **Option B is incorrect** because Packets per second (PPS) measures packet rate.
> - **Option C is incorrect** because Transactions measure application rate.
> - **Option D is incorrect** because CPU cycles measure processor speed.

---

### 🧩 Question 16 | Scenario Challenge

> [!QUESTION] 📌 **Scenario Context**
> What metric measures the volume of a DDoS attack in terms of network routing equipment forwarding capacity?

#### 🔘 Available Options:

- **A**: Packets per Second (Mpps)
- **B**: Gigabits per Second
- **C**: HTTP Requests per Hour
- **D**: Bytes per File

> [!SUCCESS]- 🔑 **Show Correct Answer & Exam Breakdown**
> **Correct Answer**: **Option A**
>
> #### 💡 Technical Deep Dive:
> Protocol DDoS attacks targeting routers and firewalls are measured in Millions of Packets per Second (Mpps).
>
> #### 🚫 Distractor Analysis & Refutations:
>
> - **Option B is incorrect** because Gbps measures bandwidth throughput.
> - **Option C is incorrect** because Requests per Hour measures web application load.
> - **Option D is incorrect** because Bytes per File measures file size.

---

### 🧩 Question 17 | Scenario Challenge

> [!QUESTION] 📌 **Scenario Context**
> An attacker performs a DNS Amplification attack. What specific protocol feature makes DNS vulnerable to amplification?

#### 🔘 Available Options:

- **A**: DNS over UDP uses unauthenticated request headers where small queries return large TXT/ANY records
- **B**: DNS uses mandatory TLS encryption
- **C**: DNS requires TCP 3-way handshake validation
- **D**: DNS uses static MAC bindings

> [!SUCCESS]- 🔑 **Show Correct Answer & Exam Breakdown**
> **Correct Answer**: **Option A**
>
> #### 💡 Technical Deep Dive:
> DNS uses UDP (connectionless/spoofable) and supports queries (like `ANY` or `TXT`) where response payloads are 20x to 50x larger than request queries.
>
> #### 🚫 Distractor Analysis & Refutations:
>
> - **Option B is incorrect** because TLS encrypts traffic and prevents amplification.
> - **Option C is incorrect** because TCP requires handshake validation.
> - **Option D is incorrect** because MAC bindings apply to Layer 2.

---

### 🧩 Question 18 | Scenario Challenge

> [!QUESTION] 📌 **Scenario Context**
> What technique relies on distributing a network of software agents (zombies) controlled by a central Command-and-Control (C2) server?

#### 🔘 Available Options:

- **A**: Botnet Infrastructure
- **B**: Standalone Virus
- **C**: Rootkit Driver
- **D**: Ransomware Encryptor

> [!SUCCESS]- 🔑 **Show Correct Answer & Exam Breakdown**
> **Correct Answer**: **Option A**
>
> #### 💡 Technical Deep Dive:
> Botnets consist of thousands of infected zombie hosts connected to a C2 infrastructure to perform coordinated attacks.
>
> #### 🚫 Distractor Analysis & Refutations:
>
> - **Option B is incorrect** because standalone viruses operate locally.
> - **Option C is incorrect** because rootkits hide kernel processes.
> - **Option D is incorrect** because ransomware encrypts local files.

---

### 🧩 Question 19 | Scenario Challenge

> [!QUESTION] 📌 **Scenario Context**
> Which HTTP slow-rate DoS tool sends legitimate-looking HTTP POST requests with a large `Content-Length` header value while transmitting body bytes extremely slowly?

#### 🔘 Available Options:

- **A**: R-U-Dead-Yet (RUDY)
- **B**: macof
- **C**: arpspoof
- **D**: Metasploit

> [!SUCCESS]- 🔑 **Show Correct Answer & Exam Breakdown**
> **Correct Answer**: **Option A**
>
> #### 💡 Technical Deep Dive:
> R-U-Dead-Yet (RUDY) targets web applications by submitting long POST requests and sending body fields 1 byte at a time.
>
> #### 🚫 Distractor Analysis & Refutations:
>
> - **Option B is incorrect** because macof floods MAC tables.
> - **Option C is incorrect** because arpspoof poisons ARP tables.
> - **Option D is incorrect** because Metasploit is an exploit suite.

---

### 🧩 Question 20 | Scenario Challenge

> [!QUESTION] 📌 **Scenario Context**
> What network security control limits the rate of incoming ICMP or SYN packets permitted per second on a firewall or router interface?

#### 🔘 Available Options:

- **A**: Rate Limiting / Traffic Policing
- **B**: MAC Address Filtering
- **C**: DNS Round Robin
- **D**: VLAN Tagging

> [!SUCCESS]- 🔑 **Show Correct Answer & Exam Breakdown**
> **Correct Answer**: **Option A**
>
> #### 💡 Technical Deep Dive:
> Rate limiting restricts the maximum number of packets per second allowed through a network interface to prevent resource exhaustion.
>
> #### 🚫 Distractor Analysis & Refutations:
>
> - **Option B is incorrect** because MAC filtering blocks specific physical NICs.
> - **Option C is incorrect** because DNS Round Robin balances load.
> - **Option D is incorrect** because VLAN tagging segments networks.

---

### 🧩 Question 21 | Scenario Challenge

> [!QUESTION] 📌 **Scenario Context**
> What protocol defense on edge routers drops incoming IP packets whose source IP addresses do not match the valid subnet routing table (mitigating IP spoofing)?

#### 🔘 Available Options:

- **A**: Unicast Reverse Path Forwarding (uRPF)
- **B**: Dynamic ARP Inspection
- **C**: Port Security
- **D**: Spanning Tree Protocol

> [!SUCCESS]- 🔑 **Show Correct Answer & Exam Breakdown**
> **Correct Answer**: **Option A**
>
> #### 💡 Technical Deep Dive:
> Unicast Reverse Path Forwarding (uRPF) verifies that packet source IP addresses match reachable interface routing table entries.
>
> #### 🚫 Distractor Analysis & Refutations:
>
> - **Option B is incorrect** because DAI protects local ARP tables.
> - **Option C is incorrect** because Port Security limits MAC addresses on switch ports.
> - **Option D is incorrect** because STP prevents loops.

---

### 🧩 Question 22 | Scenario Challenge

> [!QUESTION] 📌 **Scenario Context**
> An attacker launches an HTTP GET flood against a web application. What metric measures the application layer load generated by this attack?

#### 🔘 Available Options:

- **A**: Requests per Second (RPS)
- **B**: Bits per Second
- **C**: Packets per Hour
- **D**: Bytes per Sector

> [!SUCCESS]- 🔑 **Show Correct Answer & Exam Breakdown**
> **Correct Answer**: **Option A**
>
> #### 💡 Technical Deep Dive:
> Application layer web attacks are measured in Requests per Second (RPS) or Queries per Second (QPS).
>
> #### 🚫 Distractor Analysis & Refutations:
>
> - **Option B is incorrect** because Bits per second measures network bandwidth.
> - **Option C is incorrect** because Packets per hour is an inaccurate rate metric.
> - **Option D is incorrect** because Bytes per sector measures disk storage.

---

### 🧩 Question 23 | Scenario Challenge

> [!QUESTION] 📌 **Scenario Context**
> What type of DoS attack targets stateful firewalls and load balancers by filling up their active TCP connection tracking tables?

#### 🔘 Available Options:

- **A**: State-Exhaustion Attack
- **B**: Volumetric Attack
- **C**: Application Layer Attack
- **D**: Physical Wire Cut

> [!SUCCESS]- 🔑 **Show Correct Answer & Exam Breakdown**
> **Correct Answer**: **Option A**
>
> #### 💡 Technical Deep Dive:
> State-Exhaustion attacks target firewalls and load balancers, consuming connection state tables.
>
> #### 🚫 Distractor Analysis & Refutations:
>
> - **Option B is incorrect** because Volumetric attacks flood network pipes.
> - **Option C is incorrect** because Application Layer attacks target web app servers.
> - **Option D is incorrect** because Physical wire cut is physical damage.

---

### 🧩 Question 24 | Scenario Challenge

> [!QUESTION] 📌 **Scenario Context**
> Which open-source DDoS tool features a simple GUI allowing non-technical users to flood target IP addresses with TCP, UDP, or HTTP requests?

#### 🔘 Available Options:

- **A**: LOIC (Low Orbit Ion Cannon)
- **B**: Wireshark
- **C**: Burp Suite
- **D**: Ghidra

> [!SUCCESS]- 🔑 **Show Correct Answer & Exam Breakdown**
> **Correct Answer**: **Option A**
>
> #### 💡 Technical Deep Dive:
> LOIC is an easy-to-use GUI tool popular among script kiddies for executing basic TCP/UDP/HTTP packet floods.
>
> #### 🚫 Distractor Analysis & Refutations:
>
> - **Option B is incorrect** because Wireshark is a packet analyzer.
> - **Option C is incorrect** because Burp Suite is a web app security proxy.
> - **Option D is incorrect** because Ghidra is a reverse engineering tool.

---

### 🧩 Question 25 | Scenario Challenge

> [!QUESTION] 📌 **Scenario Context**
> What is the primary operational objective of a Denial-of-Service (DoS) attack?

#### 🔘 Available Options:

- **A**: To degrade or completely disrupt the availability of a targeted service or system for legitimate users
- **B**: To steal confidential user passwords
- **C**: To install persistent rootkits in kernel memory
- **D**: To modify database records

> [!SUCCESS]- 🔑 **Show Correct Answer & Exam Breakdown**
> **Correct Answer**: **Option A**
>
> #### 💡 Technical Deep Dive:
> The sole objective of a DoS attack is to compromise Availability within the CIA triad.
>
> #### 🚫 Distractor Analysis & Refutations:
>
> - **Option B is incorrect** because credential theft targets Confidentiality.
> - **Option C is incorrect** because installing rootkits targets System Access.
> - **Option D is incorrect** because modifying records targets Integrity.
