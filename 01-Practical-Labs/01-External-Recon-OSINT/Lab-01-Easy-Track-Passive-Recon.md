![Passive Recon Header](https://images.unsplash.com/photo-1460925895917-afdab827c52f?w=800&h=200&fit=crop)

[🏠 Path Home](Home.md) | [Next Lab ➡️](Lab-02-Easy-Track-Google-Dorking.md)

---

# Lab 01: Passive Reconnaissance (DNS, WHOIS)

---


---


---

---


---

## 🎯 Lab Objective
Master DNS dumping, WHOIS lookup, and basic OSINT without actively touching the target.

## 🌐 Direct Lab Access
[![TryHackMe - Passive Recon](https://images.unsplash.com/photo-1516321318423-f06f85e504b3?w=150&h=50&fit=crop)](https://tryhackme.com/room/passiverecon)

---

## 🛠️ Required Tools

| Tool | Purpose | Installation |
|------|---------|--------------|
| whois | Domain registration info | Pre-installed on Kali/Parrot |
| nslookup | DNS query tool | Pre-installed |
| dig | Advanced DNS query | Pre-installed |
| dnsrecon | DNS reconnaissance | `sudo apt install dnsrecon` |
| dnsenum | DNS enumeration | `sudo apt install dnsenum` |

---

## 📝 Step-by-Step Command Guide

### 1. WHOIS Lookup
```bash
# Basic domain WHOIS
whois targetdomain.com

# Check for domain history (requires whoisxmlapi or similar)
# Manual check via https://www.whois.com/whois/targetdomain.com
```

### 2. DNS Lookup with nslookup
```bash
# Interactive mode
nslookup
> server 8.8.8.8
> targetdomain.com
> set type=MX
> targetdomain.com
> set type=NS
> targetdomain.com
> set type=TXT
> targetdomain.com
> exit

# Non-interactive
nslookup -type=A targetdomain.com
nslookup -type=AAAA targetdomain.com
nslookup -type=MX targetdomain.com
nslookup -type=NS targetdomain.com
nslookup -type=TXT targetdomain.com
nslookup -type=SOA targetdomain.com
```

### 3. Advanced DNS with dig
```bash
# All records
dig targetdomain.com ANY

# Specific records
dig targetdomain.com A
dig targetdomain.com MX
dig targetdomain.com NS
dig targetdomain.com TXT
dig targetdomain.com SOA

# Reverse lookup
dig -x 192.168.1.10

# Zone transfer attempt (may fail)
dig @ns1.targetdomain.com targetdomain.com AXFR
```

### 4. DNSRecon
```bash
# Standard enumeration
dnsrecon -d targetdomain.com

# Zone transfer check
dnsrecon -d targetdomain.com -t axfr

# Brute force subdomains
dnsrecon -d targetdomain.com -t brt -D /usr/share/wordlists/dnsmap.txt
```

### 5. DNSEnum
```bash
# Full enumeration
dnsenum targetdomain.com

# With wordlist
dnsenum -f /usr/share/wordlists/dnsmap.txt targetdomain.com
```

---

## 📊 Expected Results
- Domain registrar information
- Name servers
- Mail servers
- Subdomains
- TXT records (may contain API keys, SPF info)

---

## 🔗 Additional Resources
- [DNS Dumpster](https://dnsdumpster.com)
- [VirusTotal](https://www.virustotal.com)
- [Censys](https://censys.io)

---


## 🧪 Hands-On Step-by-Step Exercise
1. **Target Identification**: Let's pick a legal testing domain (e.g., `scanme.nmap.org` or a target specified in your TryHackMe/HTB sandbox).
2. **Execute WHOIS**: Open your Kali terminal and query the domain's registration records:
   ```bash
   whois scanme.nmap.org
   ```
   Identify the registrar (e.g., Namecheap), domain creation date, and listed name servers.
3. **Analyze DNS Records**: Use `dig` to perform a query for all records:
   ```bash
   dig scanme.nmap.org ANY
   ```
   Note that many DNS servers disable the `ANY` query response to prevent amplification attacks. If empty, perform explicit queries:
   ```bash
   dig scanme.nmap.org A
   dig scanme.nmap.org MX
   dig scanme.nmap.org NS
   ```
4. **Attempt Zone Transfer (AXFR)**: Identify the authoritative name servers from the previous step, then attempt a zone transfer against each:
   ```bash
   dig @shared-ns.cloudflare.com scanme.nmap.org AXFR
   ```
   Verify if the transfer is correctly blocked (responds with `Transfer failed` or `REFUSED`).

---

[🏠 Path Home](Home.md) | [Next Lab ➡️](Lab-02-Easy-Track-Google-Dorking.md)
