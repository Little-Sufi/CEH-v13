# 03. Tools — Footprinting & Reconnaissance

> [!TOOL] 🛠️ **Comprehensive Reconnaissance & OSINT Tool Suite**
> Direct extraction from official CEH v13 Syllabus (Module 02 Section 3). Detailed operational reference matrix covering GUI and CLI reconnaissance software, OSINT frameworks, WHOIS utilities, and DNS mapping suites.

---

## 🧰 1. Reconnaissance Tool Suite & Operational Analysis

### 1.1 Industry-Standard OSINT & Footprinting Utilities
Ethical hackers utilize a specialized suite of tools to automate intelligence gathering across search engines, domain registries, DNS servers, certificate transparency logs, and internet-connected device databases.

- **Maltego**: A powerful interactive graphical OSINT software that visualizes complex relationships between domains, IP address blocks, WHOIS records, email addresses, social network profiles, and physical infrastructure.
- **Recon-ng**: A modular command-line web reconnaissance framework written in Python. Operates similarly to Metasploit, allowing testers to load specialized modules for domain enumeration, WHOIS queries, contact harvesting, and vulnerability scanning.
- **theHarvester**: A CLI Python utility designed to harvest emails, subdomains, open ports, employee names, and IP addresses from over 30 public search engine backends and threat intelligence APIs.
- **Shodan**: An Internet-of-Things (IoT) and device search engine that continuously scans the global IPv4 address space, indexing open ports, service banners, operating systems, and web application headers.

> [!TOOL] 🛠️ **📋 Comprehensive Footprinting & OSINT Utilities Reference Matrix**

| Utility Name | Tool Category & Type | Operational Focus & Primary Features | Key Command / Usage Syntax |
| :--- | :--- | :--- | :--- |
| **Maltego** | Interactive OSINT / GUI | Visualizes relationships between domains, IPs, emails, people | GUI Transform execution |
| **Recon-ng** | CLI OSINT Framework | Modular web reconnaissance framework with API integrations | `recon-ng`, `modules load` |
| **theHarvester** | CLI Python OSINT | Harvests emails, subdomains, IPs from 30+ search engines | `theHarvester -d target.com -b all` |
| **Shodan** | IoT / Internet Scanner | Searches internet-connected devices, open ports & banners | `shodan search hostname:target.com` |
| **Censys** | Attack Surface Management| Aggregates internet device data, SSL certificates & hosts | Web UI / API Query |
| **Sublist3r** | Subdomain Enumeration | Enumerates subdomains via search engines & Netcraft | `sublist3r -d target.com` |
| **OWASP Amass** | Attack Surface Mapping | In-depth DNS enumeration, scraping & ASN mapping | `amass enum -d target.com` |
| **Netcraft** | Web Survey & OSINT | Analyzes web server tech stacks, hosting history & SSL | Web UI (`sitereport.netcraft.com`) |
| **CentralOps** | Online Network Utility | Integrated WHOIS, nslookup, ping, and traceroute portal | Web UI (`centralops.net`) |
| **Exiftool** | Metadata Extraction | Extracts EXIF metadata (GPS, author, camera) from files | `exiftool image.jpg` / `document.pdf` |

---

## 📡 2. DNS Command-Line Utilities Mechanics

### 2.1 Active & Passive DNS Enumeration Syntax
Command-line utilities enable ethical hackers to interact directly with DNS resolvers and authoritative name servers:

- **`nslookup`**: Standard cross-platform utility used to query specific DNS records (e.g., `nslookup -type=mx target.com`).
- **`dig` (Domain Information Groper)**: Powerful Linux CLI tool providing detailed DNS query outputs, flags, and exact responses from authoritative name servers.
- **DNS Zone Transfer (`AXFR`)**: Executing `dig target.com AXFR @ns1.target.com` attempts to copy the entire zone file. If allowed, it reveals every registered hostname and IP under the target domain.

> [!IMPORTANT] 🔄 **📋 Comprehensive DNS Reconnaissance Execution Reference Matrix**

| Utility | Command Syntax Example | Operational Purpose |
| :--- | :--- | :--- |
| **nslookup** | `nslookup -type=mx target.com` | Queries specific DNS records (MX, NS, SOA, A) |
| **dig** | `dig target.com AXFR @ns1.target.com` | Performs DNS Zone Transfer request against authoritative NS |
| **dnsrecon** | `dnsrecon -d target.com -t axfr` | Automates DNS record enumeration & zone transfer checks |
| **fierce** | `fierce --domain target.com` | Locates non-contiguous IP space & subdomains via brute force |
