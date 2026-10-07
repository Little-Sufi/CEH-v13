# 02. Attack Techniques — Footprinting & Reconnaissance

> [!WARNING] ⚡ **Offensive Methodologies & Reconnaissance Vectors**
> Direct extraction from official CEH v13 Syllabus (Module 02 Section 2). Covers Search Engine Footprinting, Advanced Google Dorking, Social Media OSINT, Website Footprinting, Email Header Tracking, WHOIS, DNS Footprinting, and Network Topology Mapping.

---

## 🔄 1. The 10-Step Footprinting Methodology

### 1.1 Operational Execution Workflow
The CEH official methodology structures footprinting into a disciplined, 10-step sequential framework. Ethical hackers move systematically from broad passive intelligence gathering to specific technical host mapping, ensuring maximum coverage of the target's attack surface.

> [!IMPORTANT] 🔄 **📋 Comprehensive 10-Step Footprinting Execution Reference Matrix**

| Step # | Footprinting Phase | Primary Operational Focus | Technical Execution & Vectors |
| :---: | :--- | :--- | :--- |
| **Step 1** | **Search Engine Recon** | Harvest search engine index data, cached pages & dorks | Google Dorks, Bing, DuckDuckGo, Baidu |
| **Step 2** | **Advanced Google Dorking** | Uncover sensitive files, admin portals & exposed DBs | `filetype:`, `inurl:`, `site:`, `intitle:`, `index of` |
| **Step 3** | **Social Network OSINT** | Profile organizational hierarchy & key personnel | LinkedIn, Twitter/X, Facebook, Instagram, Reddit |
| **Step 4** | **Website Footprinting** | Analyze web technologies, hidden dirs & file metadata | Wappalyzer, HTTrack, CeWL, Exiftool, Robots.txt |
| **Step 5** | **Email Header Tracking** | Trace originating mail servers, internal IPs & hops | Email Header Parsing, Received: headers, SPF/DKIM |
| **Step 6** | **Competitive Intelligence** | Profile corporate acquisitions, financial reports & stacks | EDGAR database, Dun & Bradstreet, Hoovers |
| **Step 7** | **WHOIS Reconnaissance** | Harvest domain registrar records & contact details | ARIN, RIPE, APNIC, LACNIC, AFRINIC registries |
| **Step 8** | **DNS Footprinting** | Map subdomains, zone transfers & mail servers | `nslookup`, `dig`, `dnsrecon`, Zone Transfer (`AXFR`) |
| **Step 9** | **Network Footprinting** | Discover active IP ranges, netblocks & hop routes | `traceroute`, `tracert`, Autonomous Systems (ASN) |
| **Step 10** | **Social Engineering** | Extract internal information via human interaction | Eavesdropping, Shoulder Surfing, Phishing, Vishing |

---

## 🔍 2. Advanced Google Dorking & Search Operator Mechanics

### 2.1 Google Hacking & Index Exploitation
Google Dorking (also known as Google Hacking) leverages specialized search operators to query Google's massive web crawler index. Web crawlers index everything publicly reachable, including inadvertently exposed configuration files, backup databases (`.bak`, `.sql`), unindexed administrative panels, and vulnerable web interfaces.

By crafting precise search strings using operators like `site:`, `filetype:`, `inurl:`, `intitle:`, and `intext:`, security auditors can instantly discover high-risk data leakage without directly touching target web application endpoints.

> [!DANGER] 🛡️ **📋 Comprehensive Google Dorking Operator Reference Matrix**

| Dork Operator | Functional Description | Real-World Attack Scenario Dork |
| :--- | :--- | :--- |
| **`site:`** | Restricts search results strictly to a specific domain | `site:target.com` |
| **`filetype:`** / **`ext:`** | Filters search results by specific file extension | `site:target.com filetype:pdf pass` |
| **`inurl:`** | Searches for specific string inside URL paths | `inurl:admin/login.php` |
| **`intitle:`** | Searches for specific terms inside webpage title tags | `intitle:"index of /" "parent directory"` |
| **`intext:`** | Searches for specific keywords within page body text | `intext:"sql syntax error" site:target.com` |
| **`link:`** | Finds web pages that link to a specific target domain | `link:www.target.com` |

---

## 📡 3. Domain Name System (DNS) Footprinting

### 3.1 DNS Architecture & Attack Surface Mapping
The Domain Name System (DNS) acts as the phonebook of the Internet, translating human-readable domain hostnames (`vpn.target.com`) into numerical IPv4/IPv6 addresses. DNS footprinting allows security auditors to map an organization's complete network infrastructure by enumerating authoritative name servers, mail exchangers, service aliases, and internal host mappings.

Key record types provide distinct intelligence:
- **A & AAAA Records**: Map primary hostnames to IPv4 and IPv6 addresses.
- **MX Records**: Identify corporate mail servers, revealing email security gateways (e.g., Proofpoint, Mimecast).
- **NS Records**: Identify authoritative DNS servers hosting the target's zone configuration.
- **TXT Records**: Contain SPF, DKIM, and DMARC email authentication records, along with cloud service verification strings (e.g., Google Workspace, Microsoft 365).

> [!NOTE] 🔍 **📋 Comprehensive DNS Record Reference Matrix**

| Record Type | Full Record Name | Technical Reconnaissance Significance |
| :---: | :--- | :--- |
| **A** | Host Address | Maps hostname directly to 32-bit IPv4 address |
| **AAAA** | IPv6 Host Address | Maps hostname directly to 128-bit IPv6 address |
| **MX** | Mail Exchange | Identifies primary & backup corporate mail server hostnames |
| **NS** | Name Server | Identifies authoritative DNS servers for the domain |
| **CNAME** | Canonical Name | Identifies domain aliases (canonical hostnames) |
| **SOA** | Start of Authority | Contains zone transfer parameters, primary NS, admin email |
| **TXT** | Text Record | Contains SPF, DKIM, DMARC records, verification strings |
| **PTR** | Pointer Record | Maps IP address back to hostname (Reverse DNS Lookup) |
