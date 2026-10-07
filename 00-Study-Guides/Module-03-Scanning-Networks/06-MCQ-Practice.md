# 🎯 Module 03: Scanning Networks - Exam Scenario Practice Engine

> [!ABSTRACT] 📊 **Interactive Module Scorecard**
>
> - **Target Module**: Module 03: Scanning Networks
> - **Total Questions**: 25 Ultra-Detailed, 100% Unique Indirect Scenarios
> - **Exam Difficulty Standard**: Senior CEH v13 (Scenario-Driven Logic & Technical Deduction)
> - **Passing Threshold**: 85% Accuracy (22/25 Correct)
> 
> *Instructions: Evaluate the scenario context below. Select your choice, then expand the **Show Correct Answer & Exam Breakdown** callout to verify your answer and review the deep technical analysis and distractor refutations.*

---

### 🧩 Question 01 | Scenario Challenge

> [!QUESTION] 📌 **Scenario Context**
> A penetration tester is attempting to discover open ports on a hardened Linux web server behind a stateless firewall. The tester wants to execute a scan that does NOT complete a TCP 3-way handshake and sets the FIN, URG, and PSH flags simultaneously.
> 
> Which Nmap scan type is the tester executing, and how will a closed port respond per RFC 793?

#### 🔘 Available Options:

- **A**: TCP Xmas Scan (`-sX`); a closed port will return a TCP `RST` packet
- **B**: TCP Stealth SYN Scan (`-sS`); a closed port will return a TCP `SYN/ACK` packet
- **C**: Null Scan (`-sN`); a closed port will return no response
- **D**: ACK Scan (`-sA`); a closed port will return an ICMP Destination Unreachable message

> [!SUCCESS]- 🔑 **Show Correct Answer & Exam Breakdown**
> **Correct Answer**: **Option A**
>
> #### 💡 Technical Deep Dive:
> The Xmas scan (`nmap -sX`) sets the FIN, URG, and PSH flags simultaneously. According to RFC 793, if a target port is closed, it MUST respond with a TCP `RST` packet. If the port is open or filtered by a firewall, it will drop the packet silently without returning a response.
>
> #### 🚫 Distractor Analysis & Refutations:
>
> - **Option B is incorrect** because a SYN scan sets only the SYN flag; open ports respond with SYN/ACK, while closed ports respond with RST.
> - **Option C is incorrect** because Null scans set zero flags, but closed ports still return an RST packet per RFC 793.
> - **Option D is incorrect** because ACK scans set only the ACK flag and return RST packets from both open and closed ports to map firewall filtering rules.

---

### 🧩 Question 02 | Scenario Challenge

> [!QUESTION] 📌 **Scenario Context**
> A network security analyst examines firewall logs and notices an incoming probe consisting of TCP packets where ONLY the `SYN` flag is set. For open ports, the scanner immediately sends a `RST` packet as soon as it receives a `SYN/ACK` from the target, without completing the final `ACK` step.
>
> Which port scanning method is being executed?

#### 🔘 Available Options:

- **A**: TCP Stealth SYN Scan (Half-Open Scan, `-sS`)
- **B**: TCP Full Connect Scan (`-sT`)
- **C**: UDP Scan (`-sU`)
- **D**: Idle/Zombie Scan (`-sI`)

> [!SUCCESS]- 🔑 **Show Correct Answer & Exam Breakdown**
> **Correct Answer**: **Option A**
>
> #### 💡 Technical Deep Dive:
> Stealth SYN scanning (`-sS`) is called "half-open" because it tears down the connection with a `RST` packet immediately after receiving `SYN/ACK`, avoiding the completion of the 3-way handshake and bypassing application-layer logging.
>
> #### 🚫 Distractor Analysis & Refutations:
>
> - **Option B is incorrect** because full connect scans complete the full 3-way handshake (`SYN` -> `SYN/ACK` -> `ACK`).
> - **Option C is incorrect** because UDP scans use connectionless UDP datagrams without TCP control flags.
> - **Option D is incorrect** because Idle scans spoof the IP of an idle zombie host.

---

### 🧩 Question 03 | Scenario Challenge

> [!QUESTION] 📌 **Scenario Context**
> An ethical hacker wants to scan a target network without revealing her actual IP address in the target firewall logs. She uses Nmap to mix her real IP address with 10 fake, randomly generated IP addresses in the packet header.
>
> Which Nmap flag and syntax achieves this evasion technique?

#### 🔘 Available Options:

- **A**: `nmap -D RND:10 target_ip`
- **B**: `nmap -f target_ip`
- **C**: `nmap -sV target_ip`
- **D**: `nmap -O target_ip`

> [!SUCCESS]- 🔑 **Show Correct Answer & Exam Breakdown**
> **Correct Answer**: **Option A**
>
> #### 💡 Technical Deep Dive:
> The `-D` flag enables Decoy scanning. `nmap -D RND:10` generates 10 random decoy IP addresses mixed with the attacker's real IP, confounding IDS/firewall log analysis.
>
> #### 🚫 Distractor Analysis & Refutations:
>
> - **Option B is incorrect** because `-f` performs IP packet fragmentation.
> - **Option C is incorrect** because `-sV` performs service version detection.
> - **Option D is incorrect** because `-O` performs OS fingerprinting.

---

### 🧩 Question 04 | Scenario Challenge

> [!QUESTION] 📌 **Scenario Context**
> During a security audit, an analyst executes `nmap -f 192.168.1.50` against a target host.
>
> What technical modification does the `-f` option apply to outbound IP packets?

#### 🔘 Available Options:

- **A**: Fragments IP packet headers into small 8-byte chunks to evade simple packet inspection firewalls
- **B**: Spoofs the MAC address of the network interface card
- **C**: Forces Nmap to execute in fast scan mode
- **D**: Sets the TCP FIN flag on all packets

> [!SUCCESS]- 🔑 **Show Correct Answer & Exam Breakdown**
> **Correct Answer**: **Option A**
>
> #### 💡 Technical Deep Dive:
> The `-f` flag causes Nmap to split raw IP header packets into tiny 8-byte fragments, making it difficult for stateless firewalls and simple IDS devices to reassemble and detect signatures.
>
> #### 🚫 Distractor Analysis & Refutations:
>
> - **Option B is incorrect** because `--spoof-mac` spoofs MAC addresses.
> - **Option C is incorrect** because `-F` enables fast scan mode.
> - **Option D is incorrect** because `-sF` sets the FIN flag.

---

### 🧩 Question 05 | Scenario Challenge

> [!QUESTION] 📌 **Scenario Context**
> A penetration tester executes `hping3 -S -p 80 10.0.0.1`.
>
> What specific custom packet is `hping3` crafting and transmitting to port 80 of the target host?

#### 🔘 Available Options:

- **A**: TCP SYN packet directed to port 80
- **B**: ICMP Echo Request packet
- **C**: UDP packet directed to port 80
- **D**: TCP FIN packet directed to port 80

> [!SUCCESS]- 🔑 **Show Correct Answer & Exam Breakdown**
> **Correct Answer**: **Option A**
>
> #### 💡 Technical Deep Dive:
> `hping3` is a command-line custom packet generator. `-S` specifies the TCP SYN flag, and `-p 80` specifies destination port 80.
>
> #### 🚫 Distractor Analysis & Refutations:
>
> - **Option B is incorrect** because `-1` or `--icmp` crafts ICMP packets.
> - **Option C is incorrect** because `-2` or `--udp` crafts UDP packets.
> - **Option D is incorrect** because `-F` crafts TCP FIN packets.

---

### 🧩 Question 06 | Scenario Challenge

> [!QUESTION] 📌 **Scenario Context**
> Which Nmap scan mode executes a completely blind port scan by spoofing an idle third-party host's IP address and analyzing IP ID sequence numbers?

#### 🔘 Available Options:

- **A**: Idle / Zombie Scan (`-sI`)
- **B**: Full Connect Scan (`-sT`)
- **C**: Bounce Scan (`-b`)
- **D**: SCTP INIT Scan (`-sY`)

> [!SUCCESS]- 🔑 **Show Correct Answer & Exam Breakdown**
> **Correct Answer**: **Option A**
>
> #### 💡 Technical Deep Dive:
> The Idle Scan (`-sI`) is an advanced blind scan technique that utilizes an idle third-party host ("zombie") and monitors IP ID increments to infer port states without sending a single packet with the attacker's real IP address.
>
> #### 🚫 Distractor Analysis & Refutations:
>
> - **Option B is incorrect** because Full Connect scans disclose the attacker's IP.
> - **Option C is incorrect** because FTP Bounce scans (`-b`) use FTP proxying.
> - **Option D is incorrect** because SCTP INIT scans target SCTP protocol endpoints.

---

### 🧩 Question 07 | Scenario Challenge

> [!QUESTION] 📌 **Scenario Context**
> An ethical hacker attempts a UDP port scan (`nmap -sU`) against a network host. The scan proceeds extremely slowly compared to TCP SYN scanning.
>
> Why do UDP port scans execute significantly slower than TCP scans?

#### 🔘 Available Options:

- **A**: Target operating systems enforce rate limiting on ICMP Port Unreachable (Type 3, Code 3) error responses
- **B**: UDP packets require a 4-way cryptographic handshake
- **C**: Nmap must wait for TCP `ACK` confirmations on every UDP port
- **D**: UDP scans require root privileges that degrade CPU speed

> [!SUCCESS]- 🔑 **Show Correct Answer & Exam Breakdown**
> **Correct Answer**: **Option A**
>
> #### 💡 Technical Deep Dive:
> Closed UDP ports return ICMP Port Unreachable messages (Type 3, Code 3). To prevent denial of service, OS kernels (like Linux) strictly rate-limit the generation of ICMP error responses, causing Nmap to slow down automatically.
>
> #### 🚫 Distractor Analysis & Refutations:
>
> - **Option B is incorrect** because UDP is a connectionless protocol with zero handshake.
> - **Option C is incorrect** because UDP does not use TCP ACK confirmations.
> - **Option D is incorrect** because root privileges do not slow down CPU processing.

---

### 🧩 Question 08 | Scenario Challenge

> [!QUESTION] 📌 **Scenario Context**
> What response will a closed port return when probed with an Nmap Null Scan (`nmap -sN`) on an RFC 793 compliant system?

#### 🔘 Available Options:

- **A**: TCP RST packet
- **B**: No response (Silent drop)
- **C**: TCP SYN/ACK packet
- **D**: ICMP Echo Reply

> [!SUCCESS]- 🔑 **Show Correct Answer & Exam Breakdown**
> **Correct Answer**: **Option A**
>
> #### 💡 Technical Deep Dive:
> Per RFC 793, any TCP packet sent to a closed port without the SYN, ACK, or RST bits set will cause the closed port to respond with a TCP `RST` packet.
>
> #### 🚫 Distractor Analysis & Refutations:
>
> - **Option B is incorrect** because open/filtered ports silently drop Null scan packets.
> - **Option C is incorrect** because closed ports never return SYN/ACK.
> - **Option D is incorrect** because ICMP Echo Replies respond to ICMP pings.

---

### 🧩 Question 09 | Scenario Challenge

> [!QUESTION] 📌 **Scenario Context**
> A security engineer wants to test whether an outbound firewall rule allows DNS traffic. He executes Nmap setting the source port explicitly to 53.
>
> What flag syntax achieves source port manipulation in Nmap?

#### 🔘 Available Options:

- **A**: `nmap --source-port 53 target_ip` (or `-g 53`)
- **B**: `nmap -p 53 target_ip`
- **C**: `nmap -sV --port 53 target_ip`
- **D**: `nmap -D 53 target_ip`

> [!SUCCESS]- 🔑 **Show Correct Answer & Exam Breakdown**
> **Correct Answer**: **Option A**
>
> #### 💡 Technical Deep Dive:
> `--source-port 53` (or `-g 53`) instructs Nmap to send scan probes originating from source port 53, bypassing firewalls that misconfigure rules to trust traffic from DNS ports.
>
> #### 🚫 Distractor Analysis & Refutations:
>
> - **Option B is incorrect** because `-p 53` sets the destination port to 53.
> - **Option C is incorrect** because `-sV` performs version detection.
> - **Option D is incorrect** because `-D` specifies decoy IP addresses.

---

### 🧩 Question 10 | Scenario Challenge

> [!QUESTION] 📌 **Scenario Context**
> During an active network scan, a tester captures a response packet with an initial Time-To-Live (TTL) value of 128 and a TCP Window Size of 64240.
>
> What operating system is most likely running on the target machine based on passive stack analysis?

#### 🔘 Available Options:

- **A**: Microsoft Windows OS
- **B**: Linux Kernel 5.x
- **C**: Cisco IOS Router
- **D**: FreeBSD Server

> [!SUCCESS]- 🔑 **Show Correct Answer & Exam Breakdown**
> **Correct Answer**: **Option A**
>
> #### 💡 Technical Deep Dive:
> Standard initial IP TTL values for Windows operating systems default to `128`. Linux/Unix defaults to `64`, and Cisco devices default to `255`.
>
> #### 🚫 Distractor Analysis & Refutations:
>
> - **Option B is incorrect** because Linux kernels default to TTL 64.
> - **Option C is incorrect** because Cisco IOS defaults to TTL 255.
> - **Option D is incorrect** because FreeBSD defaults to TTL 64.

---

### 🧩 Question 11 | Scenario Challenge

> [!QUESTION] 📌 **Scenario Context**
> Which high-speed network scanner is designed to scan the entire public Internet in under 6 minutes by transmitting up to 10 million packets per second?

#### 🔘 Available Options:

- **A**: Masscan
- **B**: Nmap
- **C**: Wireshark
- **D**: Zenmap

> [!SUCCESS]- 🔑 **Show Correct Answer & Exam Breakdown**
> **Correct Answer**: **Option A**
>
> #### 💡 Technical Deep Dive:
> Masscan is an ultra-fast internet-scale port scanner capable of transmitting up to 10 million packets per second using an asynchronous custom TCP/IP stack.
>
> #### 🚫 Distractor Analysis & Refutations:
>
> - **Option B is incorrect** because Nmap is designed for detailed host scanning, not ultra-high-speed internet sweeps.
> - **Option C is incorrect** because Wireshark is a packet analyzer.
> - **Option D is incorrect** because Zenmap is Nmap's GUI frontend.

---

### 🧩 Question 12 | Scenario Challenge

> [!QUESTION] 📌 **Scenario Context**
> What TCP control flag is set in a packet to demand that queued data be pushed immediately to the receiving application layer without buffering?

#### 🔘 Available Options:

- **A**: PSH (Push)
- **B**: URG (Urgent)
- **C**: SYN (Synchronize)
- **D**: FIN (Finish)

> [!SUCCESS]- 🔑 **Show Correct Answer & Exam Breakdown**
> **Correct Answer**: **Option A**
>
> #### 💡 Technical Deep Dive:
> The `PSH` (Push) flag informs the receiving TCP stack to push data directly to the receiving application without waiting for buffers to fill.
>
> #### 🚫 Distractor Analysis & Refutations:
>
> - **Option B is incorrect** because `URG` indicates urgent pointer data.
> - **Option C is incorrect** because `SYN` synchronizes sequence numbers for connection establishment.
> - **Option D is incorrect** because `FIN` initiates connection termination.

---

### 🧩 Question 13 | Scenario Challenge

> [!QUESTION] 📌 **Scenario Context**
> An ethical hacker wants to map firewall filtering rules without attempting to open connections. She executes `nmap -sA 192.168.1.1`.
>
> How do both open and closed unfiltered ports respond to a TCP ACK scan?

#### 🔘 Available Options:

- **A**: Both open and closed unfiltered ports respond with a TCP `RST` packet
- **B**: Open ports respond with `SYN/ACK`; closed ports respond with `RST`
- **C**: Open ports respond with `ACK`; closed ports drop the packet
- **D**: Both open and closed ports silently drop the packet

> [!SUCCESS]- 🔑 **Show Correct Answer & Exam Breakdown**
> **Correct Answer**: **Option A**
>
> #### 💡 Technical Deep Dive:
> ACK scans (`-sA`) send packets with only the ACK flag set. Because no connection exists, both open and closed unfiltered ports return a `RST` packet, allowing Nmap to differentiate filtered vs unfiltered ports.
>
> #### 🚫 Distractor Analysis & Refutations:
>
> - **Option B is incorrect** because SYN scans elicit SYN/ACK from open ports.
> - **Option C is incorrect** because ports do not respond with ACK to an unestablished ACK packet.
> - **Option D is incorrect** because filtered ports drop ACK packets.

---

### 🧩 Question 14 | Scenario Challenge

> [!QUESTION] 📌 **Scenario Context**
> What defensive technology deploys decoy IP addresses or fake vulnerable services to lure attackers, detect scanning probes, and record malicious activities?

#### 🔘 Available Options:

- **A**: Honeypot / Deception System
- **B**: Web Application Firewall
- **C**: Proxy Server
- **D**: NAT Router

> [!SUCCESS]- 🔑 **Show Correct Answer & Exam Breakdown**
> **Correct Answer**: **Option A**
>
> #### 💡 Technical Deep Dive:
> Honeypots (such as Dionaea or Honeyd) are security deception systems designed to lure attackers away from production assets, detect unauthorized scanning, and capture exploit payloads.
>
> #### 🚫 Distractor Analysis & Refutations:
>
> - **Option B is incorrect** because WAFs filter HTTP/HTTPS traffic.
> - **Option C is incorrect** because Proxy Servers relay client requests.
> - **Option D is incorrect** because NAT Routers translate IP address spaces.

---

### 🧩 Question 15 | Scenario Challenge

> [!QUESTION] 📌 **Scenario Context**
> What Nmap parameter enables OS detection, service version detection, script scanning, and traceroute simultaneously?

#### 🔘 Available Options:

- **A**: `-A` (Aggressive Scan)
- **B**: `-sS`
- **C**: `-T4`
- **D**: `-Pn`

> [!SUCCESS]- 🔑 **Show Correct Answer & Exam Breakdown**
> **Correct Answer**: **Option A**
>
> #### 💡 Technical Deep Dive:
> The `-A` flag enables aggressive scanning options in Nmap: OS detection (`-O`), version scanning (`-sV`), script scanning (`-sC`), and traceroute (`--traceroute`).
>
> #### 🚫 Distractor Analysis & Refutations:
>
> - **Option B is incorrect** because `-sS` enables SYN stealth scan only.
> - **Option C is incorrect** because `-T4` sets aggressive timing template.
> - **Option D is incorrect** because `-Pn` disables ping host discovery.

---

### 🧩 Question 16 | Scenario Challenge

> [!QUESTION] 📌 **Scenario Context**
> An analyst executes `nmap -Pn target_ip`. What operational step does `-Pn` instruct Nmap to skip?

#### 🔘 Available Options:

- **A**: Skips ICMP Host Discovery (assumes host is online)
- **B**: Skips port scanning completely
- **C**: Skips DNS resolution
- **D**: Skips service version detection

> [!SUCCESS]- 🔑 **Show Correct Answer & Exam Breakdown**
> **Correct Answer**: **Option A**
>
> #### 💡 Technical Deep Dive:
> `-Pn` instructs Nmap to skip host discovery (ping sweep) and proceed directly to port scanning all specified targets, assuming they are online.
>
> #### 🚫 Distractor Analysis & Refutations:
>
> - **Option B is incorrect** because `-sn` skips port scanning.
> - **Option C is incorrect** because `-n` disables DNS resolution.
> - **Option D is incorrect** because version detection is controlled by `-sV`.

---

### 🧩 Question 17 | Scenario Challenge

> [!QUESTION] 📌 **Scenario Context**
> What custom Hping3 command performs an ICMP ping sweep against an IP range?

#### 🔘 Available Options:

- **A**: `hping3 -1 192.168.1.x`
- **B**: `hping3 -S 192.168.1.x`
- **C**: `hping3 -8 192.168.1.x`
- **D**: `hping3 -9 192.168.1.x`

> [!SUCCESS]- 🔑 **Show Correct Answer & Exam Breakdown**
> **Correct Answer**: **Option A**
>
> #### 💡 Technical Deep Dive:
> `-1` (or `--icmp`) sets Hping3 to ICMP mode, sending ICMP Echo Requests for ping sweeps.
>
> #### 🚫 Distractor Analysis & Refutations:
>
> - **Option B is incorrect** because `-S` sets TCP SYN mode.
> - **Option C is incorrect** because `-8` enables scan mode.
> - **Option D is incorrect** because `-9` enables listen mode.

---

### 🧩 Question 18 | Scenario Challenge

> [!QUESTION] 📌 **Scenario Context**
> What packet response is returned by a closed port when targeted with a TCP FIN Scan (`nmap -sF`) on an RFC 793 system?

#### 🔘 Available Options:

- **A**: TCP RST packet
- **B**: TCP ACK packet
- **C**: TCP SYN/ACK packet
- **D**: No response

> [!SUCCESS]- 🔑 **Show Correct Answer & Exam Breakdown**
> **Correct Answer**: **Option A**
>
> #### 💡 Technical Deep Dive:
> RFC 793 specifies that a closed port must return a TCP `RST` packet in response to an unexpected `FIN` packet.
>
> #### 🚫 Distractor Analysis & Refutations:
>
> - **Option B is incorrect** because closed ports do not send ACK packets.
> - **Option C is incorrect** because SYN/ACK is returned by open ports in response to SYN packets.
> - **Option D is incorrect** because open ports ignore FIN packets silently.

---

### 🧩 Question 19 | Scenario Challenge

> [!QUESTION] 📌 **Scenario Context**
> An analyst wants to execute Nmap using the fastest built-in timing template without causing network flooding. Which timing template flag represents "Aggressive" speed?

#### 🔘 Available Options:

- **A**: `-T4`
- **B**: `-T0`
- **C**: `-T1`
- **D**: `-T5`

> [!SUCCESS]- 🔑 **Show Correct Answer & Exam Breakdown**
> **Correct Answer**: **Option A**
>
> #### 💡 Technical Deep Dive:
> Nmap timing templates range from `-T0` (Paranoid) to `-T5` (Insane). `-T4` is Aggressive timing, optimized for fast reliable networks.
>
> #### 🚫 Distractor Analysis & Refutations:
>
> - **Option B is incorrect** because `-T0` is Paranoid (extremely slow for IDS evasion).
> - **Option C is incorrect** because `-T1` is Sneaky.
> - **Option D is incorrect** because `-T5` is Insane (can flood networks and drop packets).

---

### 🧩 Question 20 | Scenario Challenge

> [!QUESTION] 📌 **Scenario Context**
> What parameter option in Nmap spoofs the hardware MAC address of the scanner to bypass layer-2 MAC address filtering?

#### 🔘 Available Options:

- **A**: `--spoof-mac`
- **B**: `-S`
- **C**: `-e`
- **D**: `-g`

> [!SUCCESS]- 🔑 **Show Correct Answer & Exam Breakdown**
> **Correct Answer**: **Option A**
>
> #### 💡 Technical Deep Dive:
> `--spoof-mac` allows users to specify a spoofed MAC address (or vendor name like Apple, Cisco) for layer-2 network interface bypass.
>
> #### 🚫 Distractor Analysis & Refutations:
>
> - **Option B is incorrect** because `-S` spoofs source IP addresses.
> - **Option C is incorrect** because `-e` specifies the network interface name.
> - **Option D is incorrect** because `-g` sets source ports.

---

### 🧩 Question 21 | Scenario Challenge

> [!QUESTION] 📌 **Scenario Context**
> Which TCP control flag is set during the first step of the TCP 3-way handshake?

#### 🔘 Available Options:

- **A**: SYN
- **B**: ACK
- **C**: FIN
- **D**: RST

> [!SUCCESS]- 🔑 **Show Correct Answer & Exam Breakdown**
> **Correct Answer**: **Option A**
>
> #### 💡 Technical Deep Dive:
> Step 1 of the 3-way handshake sends a TCP packet with the `SYN` (Synchronize) flag set to initiate a session.
>
> #### 🚫 Distractor Analysis & Refutations:
>
> - **Option B is incorrect** because `ACK` is sent in step 2 (with SYN) and step 3.
> - **Option C is incorrect** because `FIN` terminates connections.
> - **Option D is incorrect** because `RST` resets connections.

---

### 🧩 Question 22 | Scenario Challenge

> [!QUESTION] 📌 **Scenario Context**
> An administrator configures Snort IDS rules to alert whenever more than 20 TCP SYN packets per second originate from a single IP. What scanning technique is being targeted for detection?

#### 🔘 Available Options:

- **A**: SYN Flood / SYN Port Sweep
- **B**: Passive OSINT
- **C**: WHOIS Lookup
- **D**: DNS Zone Transfer

> [!SUCCESS]- 🔑 **Show Correct Answer & Exam Breakdown**
> **Correct Answer**: **Option A**
>
> #### 💡 Technical Deep Dive:
> High-frequency SYN packets from a single source IP trigger IDS alerts for SYN port sweeps and SYN flood probes.
>
> #### 🚫 Distractor Analysis & Refutations:
>
> - **Option B is incorrect** because passive OSINT generates no direct packets.
> - **Option C is incorrect** because WHOIS queries port 43 or web APIs.
> - **Option D is incorrect** because DNS Zone Transfers use AXFR queries on port 53.

---

### 🧩 Question 23 | Scenario Challenge

> [!QUESTION] 📌 **Scenario Context**
> What Nmap scan option performs banner grabbing and service version determination?

#### 🔘 Available Options:

- **A**: `-sV`
- **B**: `-O`
- **C**: `-sn`
- **D**: `-sU`

> [!SUCCESS]- 🔑 **Show Correct Answer & Exam Breakdown**
> **Correct Answer**: **Option A**
>
> #### 💡 Technical Deep Dive:
> `-sV` probes open ports to determine exact service names and software version banners.
>
> #### 🚫 Distractor Analysis & Refutations:
>
> - **Option B is incorrect** because `-O` performs OS detection.
> - **Option C is incorrect** because `-sn` performs ping sweeps only.
> - **Option D is incorrect** because `-sU` performs UDP scanning.

---

### 🧩 Question 24 | Scenario Challenge

> [!QUESTION] 📌 **Scenario Context**
> During a TCP 4-way connection teardown, which flag is sent first to initiate graceful session closure?

#### 🔘 Available Options:

- **A**: FIN
- **B**: SYN
- **C**: URG
- **D**: PSH

> [!SUCCESS]- 🔑 **Show Correct Answer & Exam Breakdown**
> **Correct Answer**: **Option A**
>
> #### 💡 Technical Deep Dive:
> Connection teardown begins when a host sends a packet with the `FIN` (Finish) flag set.
>
> #### 🚫 Distractor Analysis & Refutations:
>
> - **Option B is incorrect** because SYN initiates connections.
> - **Option C is incorrect** because URG marks urgent data.
> - **Option D is incorrect** because PSH forces data pushing.

---

### 🧩 Question 25 | Scenario Challenge

> [!QUESTION] 📌 **Scenario Context**
> What Nmap execution parameter appends random data padding to scan packets to evade payload size inspection rules?

#### 🔘 Available Options:

- **A**: `--data-length`
- **B**: `-f`
- **C**: `--spoof-mac`
- **D**: `-Pn`

> [!SUCCESS]- 🔑 **Show Correct Answer & Exam Breakdown**
> **Correct Answer**: **Option A**
>
> #### 💡 Technical Deep Dive:
> `--data-length <number>` appends random payload bytes to scan packets, altering standard packet size signatures to evade IDS detection.
>
> #### 🚫 Distractor Analysis & Refutations:
>
> - **Option B is incorrect** because `-f` fragments IP headers.
> - **Option C is incorrect** because `--spoof-mac` spoofs MAC addresses.
> - **Option D is incorrect** because `-Pn` skips host ping discovery.
