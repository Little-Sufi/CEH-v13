# 🎯 Module 02: Footprinting & Reconnaissance - Exam Scenario Practice Engine

> [!ABSTRACT] 📊 **Interactive Module Scorecard**
>
> - **Target Module**: Module 02: Footprinting & Reconnaissance
> - **Total Questions**: 25 Ultra-Detailed, 100% Unique Indirect Scenarios
> - **Exam Difficulty Standard**: Senior CEH v13 (Scenario-Driven Logic & Technical Deduction)
> - **Passing Threshold**: 85% Accuracy (22/25 Correct)
> 
> *Instructions: Evaluate the intricate scenario context below. Select your choice, then expand the **Show Correct Answer & Exam Breakdown** callout to verify your answer and review the deep technical analysis and distractor refutations.*

---

### 🧩 Question 01 | Scenario Challenge

> [!QUESTION] 📌 **Scenario Context**
> A penetration testing team is conducting a passive reconnaissance phase against a financial institution. During their initial OSINT gathering, the lead tester wants to map the organization's public attack surface and subdomains without sending a single packet directly to the target institution's infrastructure. She decides to leverage search engine index data, SSL/TLS certificate transparency logs, and public DNS registries.
>
> Which of the following execution methodologies strictly satisfies this passive constraint?

#### 🔘 Available Options:

- **A**: Executing `nmap -sS -p 80,443 target.com` against the main domain IP range
- **B**: Querying Certificate Transparency logs (`crt.sh`) and utilizing `theHarvester -b google,bing,duckduckgo`
- **C**: Running `dnsrecon -d target.com -t axfr` against the primary name server
- **D**: Sending an HTTP OPTIONS request to `https://www.target.com` using Curl

> [!SUCCESS]- 🔑 **Show Correct Answer & Exam Breakdown**
> **Correct Answer**: **Option B**
>
> #### 💡 Technical Deep Dive:
> Passive footprinting strictly requires gathering information without sending direct network packets to the target asset. Certificate Transparency logs (`crt.sh`) and `theHarvester` (when using search engine backends) aggregate data from public third-party indexers, leaving zero footprint on the victim's firewalls or IDS.
>
> #### 🚫 Distractor Analysis & Refutations:
>
> - **Option A is incorrect** because SYN stealth scanning (`nmap -sS`) sends direct TCP probes to target IP addresses, constituting active reconnaissance.
> - **Option C is incorrect** because attempting a DNS Zone Transfer (`AXFR`) connects directly to the target's authoritative name server.
> - **Option D is incorrect** because issuing an HTTP OPTIONS request makes a direct HTTP connection to the victim web server.

---

### 🧩 Question 02 | Scenario Challenge

> [!QUESTION] 📌 **Scenario Context**
> During a targeted intelligence gathering campaign, an adversary attempts to locate unindexed administrative login portals on a target enterprise website `example.com`. The attacker enters the following string into a Google search bar: `site:example.com inurl:admin intitle:"login"`.
>
> What specific technique is the attacker demonstrating, and what is its primary operational mechanic?

#### 🔘 Available Options:

- **A**: DNS Cache Poisoning; forcing Google to resolve admin URLs
- **B**: Google Dorking; leveraging advanced search operators to filter indexed web server URLs
- **C**: Web Scraping via Automated Python Requests
- **D**: SQL Injection probing via web crawler parameter tampering

> [!SUCCESS]- 🔑 **Show Correct Answer & Exam Breakdown**
> **Correct Answer**: **Option B**
>
> #### 💡 Technical Deep Dive:
> Google Dorking (also known as Google Hacking) involves using specialized search operators (such as `site:`, `inurl:`, `intitle:`, `filetype:`) to locate specific technical artifacts, exposed web pages, sensitive files, or administrative portals indexed by Google's web crawlers.
>
> #### 🚫 Distractor Analysis & Refutations:
>
> - **Option A is incorrect** because DNS Cache Poisoning manipulates DNS resolver caches, not search engine query syntax.
> - **Option C is incorrect** because Google Dorking relies on Google's index, not direct automated web scraping of the target web server.
> - **Option D is incorrect** because SQL Injection involves submitting database payload strings into input parameters, not using search operators.

---

### 🧩 Question 03 | Scenario Challenge

> [!QUESTION] 📌 **Scenario Context**
> A security engineer is analyzing DNS security configurations for `corporate-bank.com`. She opens a terminal and issues the command `dig corporate-bank.com AXFR @ns1.corporate-bank.com`. The command returns a complete dump of all hostnames, internal subdomains, IP addresses, and MX records registered under the zone.
>
> What vulnerability exists on `ns1.corporate-bank.com`, and what is the primary countermeasure to remediate it?

#### 🔘 Available Options:

- **A**: Unrestricted DNS Zone Transfer; remediate by restricting AXFR requests to trusted secondary DNS IP addresses
- **B**: DNS Amplification Vulnerability; remediate by enabling DNSSEC
- **C**: Subdomain Takeover Vulnerability; remediate by updating CNAME alias records
- **D**: Reverse DNS Poisoning; remediate by disabling PTR record lookups

> [!SUCCESS]- 🔑 **Show Correct Answer & Exam Breakdown**
> **Correct Answer**: **Option A**
>
> #### 💡 Technical Deep Dive:
> The `AXFR` query type requests a full DNS Zone Transfer. When a DNS server is misconfigured to allow unrestricted AXFR requests from any client, it discloses its entire internal host mapping database. The primary countermeasure is to restrict zone transfers strictly to authorized secondary name server IP addresses.
>
> #### 🚫 Distractor Analysis & Refutations:
>
> - **Option B is incorrect** because DNS Amplification exploits open recursive resolvers for DDoS attacks, not zone transfer disclosure.
> - **Option C is incorrect** because Subdomain Takeover occurs when a CNAME points to a defunct third-party cloud resource.
> - **Option D is incorrect** because PTR records map IPs to hostnames; zone transfers deal with zone database replication.

---

### 🧩 Question 04 | Scenario Challenge

> [!QUESTION] 📌 **Scenario Context**
> An ethical hacker extracts a JPEG image attached to a public corporate blog post published by an executive target. After running `exiftool executive_photo.jpg`, the hacker uncovers the exact latitude/longitude GPS coordinates of the executive's residence, the camera serial number, and the internal Windows username `corp\jdoe` who exported the image.
>
> Which phase of footprinting produced this intelligence, and how should the organization prevent future disclosures?

#### 🔘 Available Options:

- **A**: Network Footprinting; prevent by implementing WAF media filtering
- **B**: File Metadata Extraction / Website Footprinting; prevent by stripping EXIF metadata prior to public file publication
- **C**: Active OS Fingerprinting; prevent by blocking ICMP Timestamp requests
- **D**: Social Engineering Footprinting; prevent by enforcing email attachment encryption

> [!SUCCESS]- 🔑 **Show Correct Answer & Exam Breakdown**
> **Correct Answer**: **Option B**
>
> #### 💡 Technical Deep Dive:
> Digital photos and Office documents contain hidden EXIF and XML metadata (author names, software versions, local file paths, GPS coordinates). Extracting metadata using tools like `Exiftool` is part of website footprinting. The countermeasure is enforcing an automated metadata stripping policy before publishing files publicly.
>
> #### 🚫 Distractor Analysis & Refutations:
>
> - **Option A is incorrect** because network footprinting discovers IP subnets and routing, not file metadata.
> - **Option C is incorrect** because OS fingerprinting probes active network stack behaviors (TCP/IP flags).
> - **Option D is incorrect** because social engineering relies on human interaction, not static image metadata analysis.

---

### 🧩 Question 05 | Scenario Challenge

> [!QUESTION] 📌 **Scenario Context**
> A penetration tester is tasked with finding the official Autonomous System Number (ASN) and public IP address ranges allocated to a major European telecommunications operator. She queries `whois.ripe.net` and receives detailed records showing netblocks, administrative contacts, and abuse reporting emails.
>
> Which Regional Internet Registry (RIR) manages IP address allocations for Europe, the Middle East, and Central Asia?

#### 🔘 Available Options:

- **A**: ARIN (American Registry for Internet Numbers)
- **B**: RIPE NCC (Réseaux IP Européens Network Coordination Centre)
- **C**: APNIC (Asia-Pacific Network Information Centre)
- **D**: LACNIC (Latin America and Caribbean Network Information Centre)

> [!SUCCESS]- 🔑 **Show Correct Answer & Exam Breakdown**
> **Correct Answer**: **Option B**
>
> #### 💡 Technical Deep Dive:
> RIPE NCC is the Regional Internet Registry (RIR) responsible for allocating IP addresses and ASNs across Europe, the Middle East, and parts of Central Asia. ARIN manages North America, APNIC manages Asia-Pacific, and LACNIC manages Latin America.
>
> #### 🚫 Distractor Analysis & Refutations:
>
> - **Option A is incorrect** because ARIN manages IP allocations for North America (USA, Canada, parts of Caribbean).
> - **Option C is incorrect** because APNIC manages IP allocations for the Asia-Pacific region.
> - **Option D is incorrect** because LACNIC manages IP allocations for Latin America and the Caribbean.

---

### 🧩 Question 06 | Scenario Challenge

> [!QUESTION] 📌 **Scenario Context**
> An analyst receives a suspicious email claiming to be an urgent password reset notification from Microsoft 365. To trace the originating server, the analyst examines the raw email header and identifies the following top `Received:` field: `Received: from mail.attacker-spoof.com (198.51.100.45) by mx.targetcompany.com with ESMTP`.
>
> What technical component in the email header reveals the actual originating IP address of the relaying mail server?

#### 🔘 Available Options:

- **A**: The `To:` header line
- **B**: The bottom-most or initial `Received:` header line added by the originating mail transfer agent (MTA)
- **C**: The `Message-ID:` cryptographic hash string
- **D**: The `X-Mailer:` client user-agent string

> [!SUCCESS]- 🔑 **Show Correct Answer & Exam Breakdown**
> **Correct Answer**: **Option B**
>
> #### 💡 Technical Deep Dive:
> Email headers accumulate `Received:` tags sequentially as the message passes through mail transfer agents (MTAs). The bottom-most `Received:` line represents the initial entry hop into the email routing chain, revealing the true originating IP address.
>
> #### 🚫 Distractor Analysis & Refutations:
>
> - **Option A is incorrect** because the `To:` header line can be easily spoofed and indicates only the recipient.
> - **Option C is incorrect** because `Message-ID:` is generated by the client and does not specify network hop IPs.
> - **Option D is incorrect** because `X-Mailer:` shows the client software name, which can be forged.

---

### 🧩 Question 07 | Scenario Challenge

> [!QUESTION] 📌 **Scenario Context**
> An attacker uses Shodan to search for internet-connected industrial control systems (ICS) and exposed webcams. He enters the search query `port:502 country:US`.
>
> What specific protocol standard runs by default on TCP port 502, making it a frequent target for industrial SCADA footprinting?

#### 🔘 Available Options:

- **A**: Modbus TCP protocol used in Industrial Control Systems
- **B**: RDP (Remote Desktop Protocol)
- **C**: BACnet Building Automation protocol
- **D**: SNMP Network Management protocol

> [!SUCCESS]- 🔑 **Show Correct Answer & Exam Breakdown**
> **Correct Answer**: **Option A**
>
> #### 💡 Technical Deep Dive:
> TCP port 502 is the standard well-known port for Modbus TCP, a widely deployed industrial protocol used in SCADA and Industrial Control Systems (ICS).
>
> #### 🚫 Distractor Analysis & Refutations:
>
> - **Option B is incorrect** because RDP runs on TCP port 3389.
> - **Option C is incorrect** because BACnet typically uses UDP port 47808.
> - **Option D is incorrect** because SNMP uses UDP ports 161 and 162.

---

### 🧩 Question 08 | Scenario Challenge

> [!QUESTION] 📌 **Scenario Context**
> A penetration tester wants to view historical snapshots of a target company's website from 5 years ago to discover forgotten subdomains, old employee email directories, and retired web applications.
>
> Which OSINT web archive platform provides this historical snapshot functionality?

#### 🔘 Available Options:

- **A**: Shodan Device Search
- **B**: The Wayback Machine (Archive.org)
- **C**: Netcraft Web Survey
- **D**: Censys Search Engine

> [!SUCCESS]- 🔑 **Show Correct Answer & Exam Breakdown**
> **Correct Answer**: **Option B**
>
> #### 💡 Technical Deep Dive:
> The Wayback Machine (hosted by Archive.org) continuously crawls and archives historical versions of public websites over time, enabling testers to inspect deprecated endpoints and historical disclosures.
>
> #### 🚫 Distractor Analysis & Refutations:
>
> - **Option A is incorrect** because Shodan indexes active open ports and banners, not historical site snapshots.
> - **Option C is incorrect** because Netcraft provides hosting provider tech stack reports.
> - **Option D is incorrect** because Censys scans active SSL certificates and IP endpoints.

---

### 🧩 Question 09 | Scenario Challenge

> [!QUESTION] 📌 **Scenario Context**
> During passive OSINT gathering, an auditor queries the DNS `TXT` record for `targetcorp.com` and retrieves the string `v=spf1 include:_spf.google.com ~all`.
>
> What security protocol is defined by this record, and what is its defensive purpose?

#### 🔘 Available Options:

- **A**: Sender Policy Framework (SPF); specifies authorized mail servers allowed to send email on behalf of the domain
- **B**: DomainKeys Identified Mail (DKIM); provides asymmetric cryptographic signature verification for emails
- **C**: DMARC Policy; specifies how receivers should handle unauthenticated emails
- **D**: DNSSEC Verification; validates DNS response integrity using public key cryptography

> [!SUCCESS]- 🔑 **Show Correct Answer & Exam Breakdown**
> **Correct Answer**: **Option A**
>
> #### 💡 Technical Deep Dive:
> The `v=spf1` string defines an SPF (Sender Policy Framework) record published in DNS TXT records. It explicitly lists the IP addresses or third-party mail gateways authorized to send outbound email for the domain, mitigating spoofing.
>
> #### 🚫 Distractor Analysis & Refutations:
>
> - **Option B is incorrect** because DKIM records contain public keys (`k=rsa; p=...`) for email digital signatures.
> - **Option C is incorrect** because DMARC records begin with `v=DMARC1; p=reject;`.
> - **Option D is incorrect** because DNSSEC uses RRSIG and DNSKEY record types.

---

### 🧩 Question 10 | Scenario Challenge

> [!QUESTION] 📌 **Scenario Context**
> A red team operator wants to perform passive subdomain discovery using a Python command-line utility that scrapes over 30 public search engine backends, threat intelligence APIs, and Certificate Transparency logs.
>
> Which utility in the ethical hacker's arsenal is designed for this specific operational requirement?

#### 🔘 Available Options:

- **A**: `theHarvester`
- **B**: `Nmap`
- **C**: `Hping3`
- **D**: `John the Ripper`

> [!SUCCESS]- 🔑 **Show Correct Answer & Exam Breakdown**
> **Correct Answer**: **Option A**
>
> #### 💡 Technical Deep Dive:
> `theHarvester` is an open-source Python OSINT tool specifically designed to harvest emails, subdomains, hosts, employee names, and open ports from public search engines and threat APIs passively.
>
> #### 🚫 Distractor Analysis & Refutations:
>
> - **Option B is incorrect** because Nmap is an active network scanner.
> - **Option C is incorrect** because Hping3 is a packet generator and active ping utility.
> - **Option D is incorrect** because John the Ripper is an offline password cracker.

---

### 🧩 Question 11 | Scenario Challenge

> [!QUESTION] 📌 **Scenario Context**
> A company wants to prevent attackers from using WHOIS lookup queries to discover the personal contact details, home address, and personal phone number of the domain administrator.
>
> Which domain registrar service should be enabled to solve this privacy issue?

#### 🔘 Available Options:

- **A**: WHOIS Privacy Protection / Proxy Registration
- **B**: DNSSEC Enforcement
- **C**: Split-Horizon DNS Deployment
- **D**: BGP Route Filtering

> [!SUCCESS]- 🔑 **Show Correct Answer & Exam Breakdown**
> **Correct Answer**: **Option A**
>
> #### 💡 Technical Deep Dive:
> WHOIS Privacy Protection (also known as Privacy Guard or Proxy Registration) replaces the registrant's personal contact details with proxy information provided by the registrar, masking administrative contact data.
>
> #### 🚫 Distractor Analysis & Refutations:
>
> - **Option B is incorrect** because DNSSEC signs DNS responses against spoofing; it does not redact WHOIS records.
> - **Option C is incorrect** because Split-Horizon DNS separates internal vs. external DNS resolution.
> - **Option D is incorrect** because BGP Route Filtering manages Autonomous System network routing rules.

---

### 🧩 Question 12 | Scenario Challenge

> [!QUESTION] 📌 **Scenario Context**
> An ethical hacker wants to identify the operating system of a target server without sending any active probes. He captures a passive TCP `SYN/ACK` packet originating from the target server and observes an initial Time-To-Live (TTL) value of `64`.
>
> What operating system family is most likely running on the target host based on this standard default TTL value?

#### 🔘 Available Options:

- **A**: Linux / Unix OS Kernel
- **B**: Microsoft Windows Server 2022 (TTL 128)
- **C**: Cisco IOS Enterprise Router (TTL 255)
- **D**: Legacy Windows XP System (TTL 32)

> [!SUCCESS]- 🔑 **Show Correct Answer & Exam Breakdown**
> **Correct Answer**: **Option A**
>
> #### 💡 Technical Deep Dive:
> Standard default IP Time-To-Live (TTL) values differ across operating systems: Linux/Unix kernels use a default initial TTL of `64`, Microsoft Windows systems use `128`, and Cisco network devices use `255`.
>
> #### 🚫 Distractor Analysis & Refutations:
>
> - **Option B is incorrect** because Windows systems default to TTL 128.
> - **Option C is incorrect** because Cisco network devices default to TTL 255.
> - **Option D is incorrect** because legacy Windows systems use TTL 128 (or older ICMP defaults of 32 for specific old stacks).

---

### 🧩 Question 13 | Scenario Challenge

> [!QUESTION] 📌 **Scenario Context**
> An adversary enters `site:linkedin.com/in/ "Target Corp" "DevOps Engine"` into Google to profile key IT personnel and tech stacks.
>
> Which category of footprinting is the adversary performing?

#### 🔘 Available Options:

- **A**: Social Network OSINT / Human Resource Footprinting
- **B**: Active DNS Enumeration
- **C**: Network Infrastructure Footprinting
- **D**: Physical Perimeter Reconnaissance

> [!SUCCESS]- 🔑 **Show Correct Answer & Exam Breakdown**
> **Correct Answer**: **Option A**
>
> #### 💡 Technical Deep Dive:
> Profiling corporate employees, job titles, technologies, and team structures via LinkedIn or social media platforms is part of Social Network OSINT / Human Resource Footprinting.
>
> #### 🚫 Distractor Analysis & Refutations:
>
> - **Option B is incorrect** because DNS enumeration queries DNS servers directly.
> - **Option C is incorrect** because network infrastructure footprinting targets IP blocks and routers.
> - **Option D is incorrect** because physical perimeter reconnaissance involves inspecting physical buildings.

---

### 🧩 Question 14 | Scenario Challenge

> [!QUESTION] 📌 **Scenario Context**
> An organization wants to prevent adversaries from resolving internal corporate hostnames (`hr-server.corp.internal`) from the internet while maintaining proper external DNS resolution for public web servers.
>
> What architectural DNS control should be deployed?

#### 🔘 Available Options:

- **A**: Split-Horizon DNS (Split-Brain DNS) Architecture
- **B**: Primary DNS Zone Replication (`AXFR`)
- **C**: Dynamic DNS Update (DDNS)
- **D**: DNS Wildcard Record Masking

> [!SUCCESS]- 🔑 **Show Correct Answer & Exam Breakdown**
> **Correct Answer**: **Option A**
>
> #### 💡 Technical Deep Dive:
> Split-Horizon DNS deploys two separate DNS servers: an external DNS resolving public IPs for outside users, and an internal DNS resolving private RFC 1918 IPs for internal employees, concealing internal hostnames from external attackers.
>
> #### 🚫 Distractor Analysis & Refutations:
>
> - **Option B is incorrect** because DNS zone replication copies records between DNS servers.
> - **Option C is incorrect** because Dynamic DNS automatically updates DNS records when IP addresses change.
> - **Option D is incorrect** because DNS wildcard records match any non-existent subdomain request.

---

### 🧩 Question 15 | Scenario Challenge

> [!QUESTION] 📌 **Scenario Context**
> A penetration tester uses a web scraping utility to download a target company's entire public website structure offline for offline inspection.
>
> Which utility is specifically designed for offline website mirroring and directory cloning?

#### 🔘 Available Options:

- **A**: HTTrack
- **B**: Wireshark
- **C**: Metasploit
- **D**: OpenVAS

> [!SUCCESS]- 🔑 **Show Correct Answer & Exam Breakdown**
> **Correct Answer**: **Option A**
>
> #### 💡 Technical Deep Dive:
> HTTrack is an open-source website copier utility that allows users to download a World Wide Web site from the Internet to a local directory for offline analysis.
>
> #### 🚫 Distractor Analysis & Refutations:
>
> - **Option B is incorrect** because Wireshark is a network packet analyzer.
> - **Option C is incorrect** because Metasploit is an exploitation framework.
> - **Option D is incorrect** because OpenVAS is a network vulnerability scanner.

---

### 🧩 Question 16 | Scenario Challenge

> [!QUESTION] 📌 **Scenario Context**
> An attacker enters `filetype:pcf "GroupName"` into a search engine query bar.
>
> What specific sensitive asset is the attacker attempting to discover?

#### 🔘 Available Options:

- **A**: Cisco VPN Configuration Files containing encrypted connection group profiles
- **B**: Microsoft Password Configuration Files
- **C**: PostgreSQL Connection Logs
- **D**: Apache Web Server SSL Certificates

> [!SUCCESS]- 🔑 **Show Correct Answer & Exam Breakdown**
> **Correct Answer**: **Option A**
>
> #### 💡 Technical Deep Dive:
> The `.pcf` file extension denotes Cisco VPN Client configuration files, which contain VPN gateway IP addresses, group names, and pre-shared key (PSK) hashes.
>
> #### 🚫 Distractor Analysis & Refutations:
>
> - **Option B is incorrect** because Windows password configurations do not use `.pcf` files.
> - **Option C is incorrect** because PostgreSQL logs use `.log` extensions.
> - **Option D is incorrect** because Apache SSL certificates use `.crt` or `.pem` extensions.

---

### 🧩 Question 17 | Scenario Challenge

> [!QUESTION] 📌 **Scenario Context**
> Which Regional Internet Registry (RIR) manages public IP address allocations and Autonomous System Numbers (ASNs) for North America?

#### 🔘 Available Options:

- **A**: ARIN (American Registry for Internet Numbers)
- **B**: AFRINIC
- **C**: RIPE NCC
- **D**: APNIC

> [!SUCCESS]- 🔑 **Show Correct Answer & Exam Breakdown**
> **Correct Answer**: **Option A**
>
> #### 💡 Technical Deep Dive:
> ARIN (American Registry for Internet Numbers) manages IP address space allocation across the United States, Canada, and parts of the Caribbean.
>
> #### 🚫 Distractor Analysis & Refutations:
>
> - **Option B is incorrect** because AFRINIC manages Africa.
> - **Option C is incorrect** because RIPE NCC manages Europe/Middle East.
> - **Option D is incorrect** because APNIC manages Asia-Pacific.

---

### 🧩 Question 18 | Scenario Challenge

> [!QUESTION] 📌 **Scenario Context**
> An OSINT analyst runs `nslookup -type=soa targetdomain.com`.
>
> What critical administrative intelligence is returned in a Start of Authority (SOA) record?

#### 🔘 Available Options:

- **A**: Primary authoritative name server, administrator email address, zone serial number, and refresh/retry timers
- **B**: BGP routing table autonomous numbers
- **C**: Web application firewall ruleset version
- **D**: User password hashes

> [!SUCCESS]- 🔑 **Show Correct Answer & Exam Breakdown**
> **Correct Answer**: **Option A**
>
> #### 💡 Technical Deep Dive:
> The Start of Authority (SOA) DNS record specifies the primary authoritative name server, contact email of the domain administrator, zone serial number, and zone transfer timers.
>
> #### 🚫 Distractor Analysis & Refutations:
>
> - **Option B is incorrect** because BGP routing is managed by Autonomous Systems, not SOA records.
> - **Option C is incorrect** because WAF rules are application-level parameters.
> - **Option D is incorrect** because password hashes are stored in identity databases, not DNS SOA records.

---

### 🧩 Question 19 | Scenario Challenge

> [!QUESTION] 📌 **Scenario Context**
> A penetration tester uses `CeWL` against a target company's public website.
>
> What is the primary operational objective of executing `CeWL`?

#### 🔘 Available Options:

- **A**: Generates custom wordlists by spidering website text for password cracking attacks
- **B**: Executes automated SQL injection probes
- **C**: Scans for open SSH ports
- **D**: Cracks WPA2 Wi-Fi handshakes

> [!SUCCESS]- 🔑 **Show Correct Answer & Exam Breakdown**
> **Correct Answer**: **Option A**
>
> #### 💡 Technical Deep Dive:
> `CeWL` (Custom Word List generator) is a Ruby application that spiders a target URL to a specified depth and returns a dictionary of words used to build custom password cracking wordlists.
>
> #### 🚫 Distractor Analysis & Refutations:
>
> - **Option B is incorrect** because SQLmap executes SQL injection probes.
> - **Option C is incorrect** because Nmap scans open ports.
> - **Option D is incorrect** because Aircrack-ng cracks Wi-Fi handshakes.

---

### 🧩 Question 20 | Scenario Challenge

> [!QUESTION] 📌 **Scenario Context**
> What search operator restricts Google search results strictly to a specific domain name?

#### 🔘 Available Options:

- **A**: `site:`
- **B**: `inurl:`
- **C**: `intitle:`
- **D**: `filetype:`

> [!SUCCESS]- 🔑 **Show Correct Answer & Exam Breakdown**
> **Correct Answer**: **Option A**
>
> #### 💡 Technical Deep Dive:
> The `site:` operator restricts search queries to a designated domain (e.g., `site:target.com`).
>
> #### 🚫 Distractor Analysis & Refutations:
>
> - **Option B is incorrect** because `inurl:` searches within URL path strings.
> - **Option C is incorrect** because `intitle:` searches within webpage title tags.
> - **Option D is incorrect** because `filetype:` filters by file extension.

---

### 🧩 Question 21 | Scenario Challenge

> [!QUESTION] 📌 **Scenario Context**
> An auditor monitors code repositories on GitHub and pastes on Pastebin for an enterprise client.
>
> What risk is the auditor attempting to detect?

#### 🔘 Available Options:

- **A**: Inadvertent leakage of API keys, database credentials, and source code secrets
- **B**: BGP route hijacking
- **C**: Physical mantrap breaches
- **D**: ARP spoofing attacks

> [!SUCCESS]- 🔑 **Show Correct Answer & Exam Breakdown**
> **Correct Answer**: **Option A**
>
> #### 💡 Technical Deep Dive:
> Developers frequently commit hardcoded API keys, passwords, and private SSH keys to public GitHub repositories or Pastebin, exposing cloud infrastructure.
>
> #### 🚫 Distractor Analysis & Refutations:
>
> - **Option B is incorrect** because BGP hijacking affects network routing.
> - **Option C is incorrect** because mantraps are physical security controls.
> - **Option D is incorrect** because ARP spoofing is a local network layer-2 attack.

---

### 🧩 Question 22 | Scenario Challenge

> [!QUESTION] 📌 **Scenario Context**
> An attacker registers a domain name that is visually almost identical to a target bank's domain (`pnc-bank.com` vs `pncbank.com`) to conduct credential phishing.
>
> What social engineering / footprinting technique is demonstrated?

#### 🔘 Available Options:

- **A**: Typosquatting / Combo-squatting
- **B**: DNS Zone Transfer
- **C**: Session Hijacking
- **D**: Buffer Overflow

> [!SUCCESS]- 🔑 **Show Correct Answer & Exam Breakdown**
> **Correct Answer**: **Option A**
>
> #### 💡 Technical Deep Dive:
> Typosquatting / Combo-squatting involves registering misspelled or visually confusing domain names identical to legitimate corporate brands to trick users during phishing attacks.
>
> #### 🚫 Distractor Analysis & Refutations:
>
> - **Option B is incorrect** because DNS Zone Transfer replicates DNS database files.
> - **Option C is incorrect** because Session Hijacking steals active session cookies.
> - **Option D is incorrect** because Buffer Overflow exploits memory management flaws.

---

### 🧩 Question 23 | Scenario Challenge

> [!QUESTION] 📌 **Scenario Context**
> Which DNS record type maps an IP address back to a domain name (Reverse DNS Lookup)?

#### 🔘 Available Options:

- **A**: PTR Record
- **B**: A Record
- **C**: MX Record
- **D**: CNAME Record

> [!SUCCESS]- 🔑 **Show Correct Answer & Exam Breakdown**
> **Correct Answer**: **Option A**
>
> #### 💡 Technical Deep Dive:
> PTR (Pointer) records resolve IP addresses to domain hostnames during reverse DNS lookups.
>
> #### 🚫 Distractor Analysis & Refutations:
>
> - **Option B is incorrect** because A records map hostnames to IPv4 addresses.
> - **Option C is incorrect** because MX records specify mail servers.
> - **Option D is incorrect** because CNAME records specify domain aliases.

---

### 🧩 Question 24 | Scenario Challenge

> [!QUESTION] 📌 **Scenario Context**
> An OSINT researcher uses `Maltego` during an investigation.
>
> What is the primary visual strength of `Maltego`?

#### 🔘 Available Options:

- **A**: Graphically visualizes complex relationships between domains, IP netblocks, emails, and personnel using interactive transform graphs
- **B**: Automatically launches automated Metasploit exploits
- **C**: Decrypts WPA3 Wi-Fi passwords
- **D**: Compiles C++ malware binaries

> [!SUCCESS]- 🔑 **Show Correct Answer & Exam Breakdown**
> **Correct Answer**: **Option A**
>
> #### 💡 Technical Deep Dive:
> Maltego is an interactive graphical link-analysis tool that renders relationships between IP addresses, domain names, WHOIS records, and people on an interactive node graph.
>
> #### 🚫 Distractor Analysis & Refutations:
>
> - **Option B is incorrect** because Maltego is an OSINT visualization platform, not an exploit launcher.
> - **Option C is incorrect** because Maltego does not perform wireless cracking.
> - **Option D is incorrect** because Maltego is not a C++ compiler.

---

### 🧩 Question 25 | Scenario Challenge

> [!QUESTION] 📌 **Scenario Context**
> What search operator finds web pages containing specific strings within the page body text?

#### 🔘 Available Options:

- **A**: `intext:`
- **B**: `filetype:`
- **C**: `site:`
- **D**: `link:`

> [!SUCCESS]- 🔑 **Show Correct Answer & Exam Breakdown**
> **Correct Answer**: **Option A**
>
> #### 💡 Technical Deep Dive:
> The `intext:` operator forces Google to return web pages containing the specified term within the body text.
>
> #### 🚫 Distractor Analysis & Refutations:
>
> - **Option B is incorrect** because `filetype:` filters by file extension.
> - **Option C is incorrect** because `site:` restricts search to a specific domain.
> - **Option D is incorrect** because `link:` finds pages linking to a target URL.
