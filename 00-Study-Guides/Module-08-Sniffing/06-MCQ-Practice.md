# 🎯 Module 08: Sniffing - Exam Scenario Practice Engine

> [!ABSTRACT] 📊 **Interactive Module Scorecard**
>
> - **Target Module**: Module 08: Sniffing
> - **Total Questions**: 25 Ultra-Detailed, 100% Unique Indirect Scenarios
> - **Exam Difficulty Standard**: Senior CEH v13 (Scenario-Driven Logic & Technical Deduction)
> - **Passing Threshold**: 85% Accuracy (22/25 Correct)
> 
> *Instructions: Evaluate the scenario context below. Select your choice, then expand the **Show Correct Answer & Exam Breakdown** callout to verify your answer and review the deep technical analysis and distractor refutations.*

---

### 🧩 Question 01 | Scenario Challenge

> [!QUESTION] 📌 **Scenario Context**
> An attacker executes `macof -i eth0 -n 50000` against an enterprise Layer 2 Ethernet switch. Within seconds, the switch's Content Addressable Memory (CAM) table memory becomes completely saturated with fake MAC addresses, causing the switch to degrade into a "Fail-Open" state.
>
> What network behavior change occurs on the switch as a result of this attack?

#### 🔘 Available Options:

- **A**: The switch acts as a legacy broadcast hub, broadcasting all subsequent unicast frames to every switch port
- **B**: The switch automatically reboots into recovery mode
- **C**: The switch blocks all network traffic and drops all ports into `err-disable` status
- **D**: The switch enables WPA3 Enterprise encryption on all ethernet ports

> [!SUCCESS]- 🔑 **Show Correct Answer & Exam Breakdown**
> **Correct Answer**: **Option A**
>
> #### 💡 Technical Deep Dive:
> When a switch CAM table is flooded and exhausted by tools like `macof`, the switch fails open, behaving like a broadcast hub where all incoming unicast packets are flooded out of all ports, allowing passive packet sniffing.
>
> #### 🚫 Distractor Analysis & Refutations:
>
> - **Option B is incorrect** because switches do not reboot when CAM tables fill up.
> - **Option C is incorrect** because standard unhardened switches fail open, not fail closed (unless Port Security is configured).
> - **Option D is incorrect** because WPA3 is a wireless encryption protocol.

---

### 🧩 Question 02 | Scenario Challenge

> [!QUESTION] 📌 **Scenario Context**
> A penetration tester launches `arpspoof -i eth0 -t 192.168.1.50 192.168.1.1` to position their machine in the communication path between a target workstation (`192.168.1.50`) and the default gateway (`192.168.1.1`).
>
> What specific ARP frame component does the attacker forge to poison the victim's ARP cache?

#### 🔘 Available Options:

- **A**: Unsolicited (Gratuitous) ARP response mapping the gateway IP (`192.168.1.1`) to the attacker's MAC address
- **B**: Encrypted TLS Client Hello packet
- **C**: TCP SYN ACK handshake request
- **D**: ICMP Host Unreachable packet

> [!SUCCESS]- 🔑 **Show Correct Answer & Exam Breakdown**
> **Correct Answer**: **Option A**
>
> #### 💡 Technical Deep Dive:
> ARP Poisoning relies on sending unrequested (Gratuitous) ARP replies that claim the target IP address (Gateway) is associated with the attacker's network MAC address.
>
> #### 🚫 Distractor Analysis & Refutations:
>
> - **Option B is incorrect** because TLS Client Hello is an application layer SSL packet.
> - **Option C is incorrect** because SYN ACK is part of TCP 3-way handshake.
> - **Option D is incorrect** because ICMP Host Unreachable indicates dropped routes.

---

### 🧩 Question 03 | Scenario Challenge

> [!QUESTION] 📌 **Scenario Context**
> Which Cisco switch security feature inspects all incoming ARP packets on untrusted ports and validates them against the DHCP Snooping Binding Database to drop forged ARP responses?

#### 🔘 Available Options:

- **A**: Dynamic ARP Inspection (DAI)
- **B**: Port Security
- **C**: BPDU Guard
- **D**: IP Source Guard

> [!SUCCESS]- 🔑 **Show Correct Answer & Exam Breakdown**
> **Correct Answer**: **Option A**
>
> #### 💡 Technical Deep Dive:
> Dynamic ARP Inspection (DAI) compares incoming ARP packets against trusted DHCP snooping bindings to prevent ARP poisoning attacks.
>
> #### 🚫 Distractor Analysis & Refutations:
>
> - **Option B is incorrect** because Port Security limits the number of MAC addresses on a port.
> - **Option C is incorrect** because BPDU Guard protects Spanning Tree Protocol (STP).
> - **Option D is incorrect** because IP Source Guard filters IP traffic based on IP-to-MAC bindings.

---

### 🧩 Question 04 | Scenario Challenge

> [!QUESTION] 📌 **Scenario Context**
> An attacker uses Yersinia to flood a network with DHCP DISCOVER messages using randomly generated MAC addresses, exhausting all available IP addresses in the pool.
>
> What specific Layer 7 attack vector was executed?

#### 🔘 Available Options:

- **A**: DHCP Starvation Attack
- **B**: Rogue DHCP Server Attack
- **C**: DNS Cache Poisoning
- **D**: MAC Flooding Attack

> [!SUCCESS]- 🔑 **Show Correct Answer & Exam Breakdown**
> **Correct Answer**: **Option A**
>
> #### 💡 Technical Deep Dive:
> A DHCP Starvation attack floods DHCP DISCOVER packets to consume all available IP addresses in the scope pool, causing a Denial of Service for legitimate clients.
>
> #### 🚫 Distractor Analysis & Refutations:
>
> - **Option B is incorrect** because Rogue DHCP Server deploys an unauthorized DHCP server to issue fake default gateways.
> - **Option C is incorrect** because DNS Cache Poisoning targets DNS resolvers.
> - **Option D is incorrect** because MAC Flooding targets switch CAM tables (Layer 2).

---

### 🧩 Question 05 | Scenario Challenge

> [!QUESTION] 📌 **Scenario Context**
> A network engineer configures a packet capture filter in `tcpdump` to capture traffic for host `10.0.0.5` excluding ARP packets.
>
> What is the correct Berkeley Packet Filter (BPF) syntax?

#### 🔘 Available Options:

- **A**: `tcpdump -i eth0 'host 10.0.0.5 and not arp'`
- **B**: `tcpdump -i eth0 'ip.addr == 10.0.0.5 && !arp'`
- **C**: `tcpdump -i eth0 'filter host=10.0.0.5 drop arp'`
- **D**: `tcpdump -i eth0 'deny arp host 10.0.0.5'`

> [!SUCCESS]- 🔑 **Show Correct Answer & Exam Breakdown**
> **Correct Answer**: **Option A**
>
> #### 💡 Technical Deep Dive:
> BPF syntax used by `tcpdump` uses standard primitives like `host 10.0.0.5 and not arp`.
>
> #### 🚫 Distractor Analysis & Refutations:
>
> - **Option B is incorrect** because `ip.addr == 10.0.0.5` is a Wireshark display filter syntax, not a BPF capture filter.
> - **Option C is incorrect** because `filter host=` is invalid syntax.
> - **Option D is incorrect** because `deny arp` is firewall ACL syntax.

---

### 🧩 Question 06 | Scenario Challenge

> [!QUESTION] 📌 **Scenario Context**
> What mode must a network interface card (NIC) be configured in to pass ALL captured Ethernet frames directly to protocol analysis software, regardless of the destination MAC address?

#### 🔘 Available Options:

- **A**: Promiscuous Mode
- **B**: Monitor Mode
- **C**: Managed Mode
- **D**: Full-Duplex Mode

> [!SUCCESS]- 🔑 **Show Correct Answer & Exam Breakdown**
> **Correct Answer**: **Option A**
>
> #### 💡 Technical Deep Dive:
> Promiscuous Mode allows a wired network interface card to accept and pass all data frames it receives to the OS, ignoring MAC address filtering.
>
> #### 🚫 Distractor Analysis & Refutations:
>
> - **Option B is incorrect** because Monitor Mode applies to 802.11 wireless cards capturing raw Wi-Fi frames without associating with an AP.
> - **Option C is incorrect** because Managed Mode is standard wireless client mode.
> - **Option D is incorrect** because Full-Duplex mode allows simultaneous send/receive.

---

### 🧩 Question 07 | Scenario Challenge

> [!QUESTION] 📌 **Scenario Context**
> An analyst reviews Wireshark traffic and wants to isolate all HTTP POST requests containing cleartext authentication data.
>
> Which Wireshark display filter accomplishes this?

#### 🔘 Available Options:

- **A**: `http.request.method == "POST"`
- **B**: `port 80 and post`
- **C**: `tcp.port == 80 and method == POST`
- **D**: `http.method = POST`

> [!SUCCESS]- 🔑 **Show Correct Answer & Exam Breakdown**
> **Correct Answer**: **Option A**
>
> #### 💡 Technical Deep Dive:
> `http.request.method == "POST"` is the exact Wireshark display filter used to isolate HTTP POST requests.
>
> #### 🚫 Distractor Analysis & Refutations:
>
> - **Option B is incorrect** because `port 80 and post` is invalid syntax.
> - **Option C is incorrect** because `method == POST` lacks the `http.request.` prefix.
> - **Option D is incorrect** because Wireshark equality operator requires `==`.

---

### 🧩 Question 08 | Scenario Challenge

> [!QUESTION] 📌 **Scenario Context**
> What switch port configuration feature mirrors internal traffic passing through specified switch ports and forwards duplicate copies to a dedicated analysis port where a network sniffer is connected?

#### 🔘 Available Options:

- **A**: SPAN (Switched Port Analyzer)
- **B**: Trunk Port (802.1Q)
- **C**: Access Port
- **D**: Sub-interface

> [!SUCCESS]- 🔑 **Show Correct Answer & Exam Breakdown**
> **Correct Answer**: **Option A**
>
> #### 💡 Technical Deep Dive:
> SPAN (Switched Port Analyzer) or Port Mirroring duplicates incoming/outgoing traffic from specified ports and forwards it to a designated monitoring port for analysis.
>
> #### 🚫 Distractor Analysis & Refutations:
>
> - **Option B is incorrect** because Trunk Ports carry tagged multi-VLAN traffic between switches.
> - **Option C is incorrect** because Access Ports connect single-VLAN endpoint devices.
> - **Option D is incorrect** because Sub-interfaces handle router-on-a-stick VLAN routing.

---

### 🧩 Question 09 | Scenario Challenge

> [!QUESTION] 📌 **Scenario Context**
> What attack vector involves an attacker deploying an unauthorized DHCP server on a local subnet to issue clients fake default gateway and DNS server IP settings?

#### 🔘 Available Options:

- **A**: Rogue DHCP Server Attack
- **B**: DHCP Starvation
- **C**: DNS Amplification
- **D**: MAC Spoofing

> [!SUCCESS]- 🔑 **Show Correct Answer & Exam Breakdown**
> **Correct Answer**: **Option A**
>
> #### 💡 Technical Deep Dive:
> A Rogue DHCP Server responds faster than legitimate DHCP servers, supplying clients with malicious default gateway and DNS IP addresses to execute MitM attacks.
>
> #### 🚫 Distractor Analysis & Refutations:
>
> - **Option B is incorrect** because DHCP Starvation consumes IP address pools.
> - **Option C is incorrect** because DNS Amplification is a DDoS technique using open resolvers.
> - **Option D is incorrect** because MAC Spoofing modifies NIC physical addresses.

---

### 🧩 Question 10 | Scenario Challenge

> [!QUESTION] 📌 **Scenario Context**
> Which Layer 2 security control limits the maximum number of unique MAC addresses that can be learned on a physical switch port, putting the port into `err-disable` if a violation occurs?

#### 🔘 Available Options:

- **A**: Port Security
- **B**: Dynamic ARP Inspection
- **C**: Spanning Tree Protocol
- **D**: IEEE 802.1X

> [!SUCCESS]- 🔑 **Show Correct Answer & Exam Breakdown**
> **Correct Answer**: **Option A**
>
> #### 💡 Technical Deep Dive:
> Port Security limits the number of MAC addresses learned on a port and shuts down the port (`err-disable`) if MAC flooding (`macof`) is detected.
>
> #### 🚫 Distractor Analysis & Refutations:
>
> - **Option B is incorrect** because DAI inspects ARP packets against DHCP bindings.
> - **Option C is incorrect** because STP prevents switching loops.
> - **Option D is incorrect** because 802.1X provides port-based network access control authentication.

---

### 🧩 Question 11 | Scenario Challenge

> [!QUESTION] 📌 **Scenario Context**
> What hardware component is placed directly in-line between two network devices to passively copy incoming and outgoing physical layer signals to a network monitoring tool without introducing latency?

#### 🔘 Available Options:

- **A**: Network TAP (Terminal Access Point)
- **B**: Network Hub
- **C**: Router
- **D**: Wireless Access Point

> [!SUCCESS]- 🔑 **Show Correct Answer & Exam Breakdown**
> **Correct Answer**: **Option A**
>
> #### 💡 Technical Deep Dive:
> A Network TAP (Test Access Point) is a dedicated hardware device installed directly in-line to create out-of-band copies of network traffic streams.
>
> #### 🚫 Distractor Analysis & Refutations:
>
> - **Option B is incorrect** because Hubs introduce collision domains.
> - **Option C is incorrect** because Routers perform Layer 3 routing.
> - **Option D is incorrect** because WAPs bridge wireless signals.

---

### 🧩 Question 12 | Scenario Challenge

> [!QUESTION] 📌 **Scenario Context**
> What tool is widely used on Linux systems for Layer 2 protocol attacks against DHCP, STP, CDP, and 802.1Q VLAN trunking?

#### 🔘 Available Options:

- **A**: Yersinia
- **B**: Wireshark
- **C**: Metasploit
- **D**: Nmap

> [!SUCCESS]- 🔑 **Show Correct Answer & Exam Breakdown**
> **Correct Answer**: **Option A**
>
> #### 💡 Technical Deep Dive:
> Yersinia is a framework designed to analyze and exploit weaknesses in Layer 2 protocols like DHCP, STP, CDP, and DTP.
>
> #### 🚫 Distractor Analysis & Refutations:
>
> - **Option B is incorrect** because Wireshark is a packet analyzer.
> - **Option C is incorrect** because Metasploit is an exploitation framework.
> - **Option D is incorrect** because Nmap is a port scanner.

---

### 🧩 Question 13 | Scenario Challenge

> [!QUESTION] 📌 **Scenario Context**
> What is the primary difference between a Capture Filter and a Display Filter in Wireshark?

#### 🔘 Available Options:

- **A**: Capture Filters restrict which packets are written to buffer during capture (BPF); Display Filters hide unwanted packets from view post-capture
- **B**: Capture Filters use Wireshark syntax; Display Filters use BPF syntax
- **C**: Capture Filters work only on Wi-Fi; Display Filters work only on Ethernet
- **D**: Display Filters permanently drop packet bytes from the hard drive PCAP file

> [!SUCCESS]- 🔑 **Show Correct Answer & Exam Breakdown**
> **Correct Answer**: **Option A**
>
> #### 💡 Technical Deep Dive:
> Capture filters (BPF) filter incoming traffic before saving to memory/disk, while Display filters apply post-capture to filter the visible packet list view.
>
> #### 🚫 Distractor Analysis & Refutations:
>
> - **Option B is incorrect** because Capture Filters use BPF; Display Filters use Wireshark syntax.
> - **Option C is incorrect** because both filters work across all network interfaces.
> - **Option D is incorrect** because Display Filters do not delete data from the PCAP file.

---

### 🧩 Question 14 | Scenario Challenge

> [!QUESTION] 📌 **Scenario Context**
> What attack vector tricks a local client into resolving `www.bank.com` to an attacker-controlled IP address by sending spoofed DNS response packets before the legitimate DNS server responds?

#### 🔘 Available Options:

- **A**: DNS Spoofing / Poisoning
- **B**: ARP Poisoning
- **C**: MAC Flooding
- **D**: Session Hijacking

> [!SUCCESS]- 🔑 **Show Correct Answer & Exam Breakdown**
> **Correct Answer**: **Option A**
>
> #### 💡 Technical Deep Dive:
> DNS Spoofing injects forged DNS responses into client caches to map target domain names to attacker IP addresses.
>
> #### 🚫 Distractor Analysis & Refutations:
>
> - **Option B is incorrect** because ARP Poisoning maps IP addresses to MAC addresses.
> - **Option C is incorrect** because MAC Flooding exhausts switch CAM tables.
> - **Option D is incorrect** because Session Hijacking steals active user session tokens.

---

### 🧩 Question 15 | Scenario Challenge

> [!QUESTION] 📌 **Scenario Context**
> An administrator executes an active promiscuous mode test by sending an ICMP Echo Request to a fake MAC address (`FF:FF:FF:FF:FF:FE`).
>
> Why does a host running its NIC in promiscuous mode respond to this packet?

#### 🔘 Available Options:

- **A**: Promiscuous mode passes all MAC addresses to the OS driver kernel, which processes the valid IP packet and issues a reply
- **B**: Standard NIC hardware automatically converts fake MAC addresses into valid broadcast frames
- **C**: Promiscuous mode disables the IP stack
- **D**: The router forwards the frame back to the sender

> [!SUCCESS]- 🔑 **Show Correct Answer & Exam Breakdown**
> **Correct Answer**: **Option A**
>
> #### 💡 Technical Deep Dive:
> In promiscuous mode, the NIC controller passes frames with mismatched MACs to the operating system, which evaluates the valid IP header and generates an ICMP response.
>
> #### 🚫 Distractor Analysis & Refutations:
>
> - **Option B is incorrect** because standard hardware drops mismatched MAC frames at the hardware layer.
> - **Option C is incorrect** because promiscuous mode does not disable the IP stack.
> - **Option D is incorrect** because routers do not forward Layer 2 frames with fake MACs.

---

### 🧩 Question 16 | Scenario Challenge

> [!QUESTION] 📌 **Scenario Context**
> What command-line utility provides a powerful Go-based framework for executing modern MitM attacks, ARP poisoning, and credential sniffing?

#### 🔘 Available Options:

- **A**: Bettercap
- **B**: Wireshark
- **C**: Netcat
- **D**: Nbtscan

> [!SUCCESS]- 🔑 **Show Correct Answer & Exam Breakdown**
> **Correct Answer**: **Option A**
>
> #### 💡 Technical Deep Dive:
> Bettercap is a complete, modern command-line tool designed for network MitM attacks, ARP/DNS spoofing, and credential harvesting.
>
> #### 🚫 Distractor Analysis & Refutations:
>
> - **Option B is incorrect** because Wireshark is a GUI protocol analyzer.
> - **Option C is incorrect** because Netcat is a raw networking utility.
> - **Option D is incorrect** because Nbtscan enumerates NetBIOS.

---

### 🧩 Question 17 | Scenario Challenge

> [!QUESTION] 📌 **Scenario Context**
> What IEEE standard provides Layer 2 encryption and data integrity for Ethernet frames between switches and routers (`MACsec`)?

#### 🔘 Available Options:

- **A**: IEEE 802.1AE
- **B**: IEEE 802.11i
- **C**: IEEE 802.3
- **D**: IEEE 802.1Q

> [!SUCCESS]- 🔑 **Show Correct Answer & Exam Breakdown**
> **Correct Answer**: **Option A**
>
> #### 💡 Technical Deep Dive:
> IEEE 802.1AE (MACsec) specifies connectionless data confidentiality and integrity for Layer 2 Ethernet frames.
>
> #### 🚫 Distractor Analysis & Refutations:
>
> - **Option B is incorrect** because 802.11i specifies WPA2 wireless security.
> - **Option C is incorrect** because 802.3 specifies standard Ethernet.
> - **Option D is incorrect** because 802.1Q specifies VLAN tagging.

---

### 🧩 Question 18 | Scenario Challenge

> [!QUESTION] 📌 **Scenario Context**
> What Wireshark feature allows an analyst to right-click a TCP packet and reconstruct the complete unencrypted stream of conversation between a client and server?

#### 🔘 Available Options:

- **A**: Follow TCP Stream
- **B**: Reassemble Frame
- **C**: Export Objects
- **D**: Decode As

> [!SUCCESS]- 🔑 **Show Correct Answer & Exam Breakdown**
> **Correct Answer**: **Option A**
>
> #### 💡 Technical Deep Dive:
> "Follow TCP Stream" reassembles all data payloads transferred across a TCP connection into a single readable text window.
>
> #### 🚫 Distractor Analysis & Refutations:
>
> - **Option B is incorrect** because Reassemble Frame handles IP fragmentation.
> - **Option C is incorrect** because Export Objects extracts transferred files (HTTP/SMB).
> - **Option D is incorrect** because Decode As forces Wireshark to parse custom ports.

---

### 🧩 Question 19 | Scenario Challenge

> [!QUESTION] 📌 **Scenario Context**
> Why are legacy network Hubs inherently vulnerable to passive packet sniffing?

#### 🔘 Available Options:

- **A**: Hubs operate at Layer 1 (Physical) and broadcast all incoming data frames out of every port
- **B**: Hubs use weak WEP encryption
- **C**: Hubs maintain active CAM tables
- **D**: Hubs require user logins

> [!SUCCESS]- 🔑 **Show Correct Answer & Exam Breakdown**
> **Correct Answer**: **Option A**
>
> #### 💡 Technical Deep Dive:
> Network Hubs operate at Layer 1 (Physical layer) and repeat every incoming electrical bit out of all connected ports, allowing any attached host to passively sniff all subnet traffic.
>
> #### 🚫 Distractor Analysis & Refutations:
>
> - **Option B is incorrect** because WEP is a wireless protocol.
> - **Option C is incorrect** because Switches maintain CAM tables, not Hubs.
> - **Option D is incorrect** because Hubs do not manage user logins.

---

### 🧩 Question 20 | Scenario Challenge

> [!QUESTION] 📌 **Scenario Context**
> An attacker sends forged ARP packets containing the target victim's MAC address to a switch, forcing the switch to repeatedly update its port mapping table.
>
> What technique is being executed to intercept targeted unicast traffic?

#### 🔘 Available Options:

- **A**: Switch Port Stealing
- **B**: MAC Flooding
- **C**: DNS Poisoning
- **D**: DHCP Starvation

> [!SUCCESS]- 🔑 **Show Correct Answer & Exam Breakdown**
> **Correct Answer**: **Option A**
>
> #### 💡 Technical Deep Dive:
> Switch Port Stealing involves sending spoofed ARP packets containing the victim's MAC address to force the switch to rebind the victim MAC to the attacker's port.
>
> #### 🚫 Distractor Analysis & Refutations:
>
> - **Option B is incorrect** because MAC Flooding uses random fake MAC addresses.
> - **Option C is incorrect** because DNS Poisoning targets DNS resolvers.
> - **Option D is incorrect** because DHCP Starvation consumes IP leases.

---

### 🧩 Question 21 | Scenario Challenge

> [!QUESTION] 📌 **Scenario Context**
> What parameter must be enabled on a Linux system (`echo 1 > /proc/sys/net/ipv4/ip_forward`) to allow it to route packets between a victim and gateway during an ARP MitM attack?

#### 🔘 Available Options:

- **A**: IP Forwarding
- **B**: Promiscuous Mode
- **C**: IP Spoofing
- **D**: NAT Traversal

> [!SUCCESS]- 🔑 **Show Correct Answer & Exam Breakdown**
> **Correct Answer**: **Option A**
>
> #### 💡 Technical Deep Dive:
> IP Forwarding enables the Linux kernel to act as a router, forwarding captured packets between the victim and gateway so communication is not broken.
>
> #### 🚫 Distractor Analysis & Refutations:
>
> - **Option B is incorrect** because Promiscuous mode controls NIC frame passing.
> - **Option C is incorrect** because IP Spoofing modifies packet headers.
> - **Option D is incorrect** because NAT Traversal bypasses NAT firewalls.

---

### 🧩 Question 22 | Scenario Challenge

> [!QUESTION] 📌 **Scenario Context**
> Which protocol is unencrypted and transmits credentials in cleartext over port 21, making it vulnerable to passive packet sniffing?

#### 🔘 Available Options:

- **A**: FTP
- **B**: SFTP
- **C**: SSH
- **D**: HTTPS

> [!SUCCESS]- 🔑 **Show Correct Answer & Exam Breakdown**
> **Correct Answer**: **Option A**
>
> #### 💡 Technical Deep Dive:
> File Transfer Protocol (FTP) transmits usernames and passwords in cleartext over port 21.
>
> #### 🚫 Distractor Analysis & Refutations:
>
> - **Option B is incorrect** because SFTP encrypts traffic via SSH (port 22).
> - **Option C is incorrect** because SSH encrypts shell access (port 22).
> - **Option D is incorrect** because HTTPS encrypts web traffic via TLS (port 443).

---

### 🧩 Question 23 | Scenario Challenge

> [!QUESTION] 📌 **Scenario Context**
> What utility included in the Wireshark suite allows security analysts to perform command-line packet sniffing and automated analysis via scripts?

#### 🔘 Available Options:

- **A**: TShark
- **B**: Tcpdump
- **C**: Ettercap
- **D**: Ncat

> [!SUCCESS]- 🔑 **Show Correct Answer & Exam Breakdown**
> **Correct Answer**: **Option A**
>
> #### 💡 Technical Deep Dive:
> TShark is the command-line terminal version of Wireshark.
>
> #### 🚫 Distractor Analysis & Refutations:
>
> - **Option B is incorrect** because Tcpdump is an independent command-line sniffer.
> - **Option C is incorrect** because Ettercap is a MitM framework.
> - **Option D is incorrect** because Ncat is a Netcat clone.

---

### 🧩 Question 24 | Scenario Challenge

> [!QUESTION] 📌 **Scenario Context**
> What switch security feature prevents unauthorized DHCP servers from offering malicious IP configurations to clients on untrusted switch ports?

#### 🔘 Available Options:

- **A**: DHCP Snooping
- **B**: Dynamic ARP Inspection
- **C**: BPDU Guard
- **D**: Storm Control

> [!SUCCESS]- 🔑 **Show Correct Answer & Exam Breakdown**
> **Correct Answer**: **Option A**
>
> #### 💡 Technical Deep Dive:
> DHCP Snooping filters untrusted DHCP messages and blocks unauthorized DHCP server responses.
>
> #### 🚫 Distractor Analysis & Refutations:
>
> - **Option B is incorrect** because DAI prevents ARP poisoning.
> - **Option C is incorrect** because BPDU Guard protects STP.
> - **Option D is incorrect** because Storm Control prevents broadcast storms.

---

### 🧩 Question 25 | Scenario Challenge

> [!QUESTION] 📌 **Scenario Context**
> What protocol maps Layer 3 IPv4 addresses to Layer 2 physical MAC addresses on Ethernet networks?

#### 🔘 Available Options:

- **A**: ARP (Address Resolution Protocol)
- **B**: RARP (Reverse ARP)
- **C**: DNS
- **D**: ICMP

> [!SUCCESS]- 🔑 **Show Correct Answer & Exam Breakdown**
> **Correct Answer**: **Option A**
>
> #### 💡 Technical Deep Dive:
> ARP (Address Resolution Protocol) resolves 32-bit IPv4 addresses to 48-bit Ethernet MAC addresses.
>
> #### 🚫 Distractor Analysis & Refutations:
>
> - **Option B is incorrect** because RARP resolves MAC addresses to IP addresses.
> - **Option C is incorrect** because DNS resolves domain names to IP addresses.
> - **Option D is incorrect** because ICMP delivers network diagnostic error messages.
