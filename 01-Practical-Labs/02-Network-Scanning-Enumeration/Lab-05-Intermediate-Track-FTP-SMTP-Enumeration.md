# Lab 05: FTP & SMTP Enumeration

[⬅️ Previous](Lab-04-Intermediate-Track-SNMP-Enumeration.md) | [🏠 Path Home](Home.md) | [Next Lab ➡️](Lab-06-Advanced-Track-Firewall-Evasion.md)

---

## 🎯 Lab Objective
Enumerate FTP and SMTP services.

## 🌐 Direct Lab Access
- TryHackMe: https://tryhackme.com/room/networkservices
- TryHackMe: https://tryhackme.com/room/networkservices2

---

## 🛠️ Required Tools
- ftp
- telnet/nc
- Nmap
- Hydra

---

## 📝 FTP Enumeration

### 1. Basic FTP Connection
```bash
ftp 192.168.1.10
# Try anonymous login with username 'anonymous' and any password
```

### 2. Nmap NSE Scripts
```bash
nmap -p 21 --script ftp* 192.168.1.10
nmap -p 21 --script ftp-anon 192.168.1.10
nmap -p 21 --script ftp-bounce 192.168.1.10
```

### 3. Hydra FTP Brute Force
```bash
hydra -l username -P /usr/share/wordlists/rockyou.txt ftp://192.168.1.10
```

---

## 📝 SMTP Enumeration

### 1. Manual Connection with Telnet/nc
```bash
telnet 192.168.1.10 25
# OR
nc 192.168.1.10 25

# Commands after connecting:
HELO test.com
VRFY root
VRFY admin
VRFY user
EXPN list
QUIT
```

### 2. Nmap NSE Scripts
```bash
nmap -p 25 --script smtp* 192.168.1.10
nmap -p 25 --script smtp-enum-users 192.168.1.10
nmap -p 25 --script smtp-open-relay 192.168.1.10
```

### 3. smtp-user-enum
```bash
smtp-user-enum -M VRFY -U /usr/share/wordlists/metasploit/unix_users.txt -t 192.168.1.10
```

---

## 📊 Expected Results
- FTP: Anonymous access, directory listing
- SMTP: Valid user accounts, open relay check

---

## 🔗 Additional Resources
- FTP RFC: https://datatracker.ietf.org/doc/html/rfc959
- SMTP RFC: https://datatracker.ietf.org/doc/html/rfc5321

---

[⬅️ Previous](Lab-04-Intermediate-Track-SNMP-Enumeration.md) | [🏠 Path Home](Home.md) | [Next Lab ➡️](Lab-06-Advanced-Track-Firewall-Evasion.md)
