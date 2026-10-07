# Lab 01: Nmap Basics - Host Discovery

[🏠 Path Home](Home.md) | [Next Lab ➡️](Lab-02-Easy-Track-Nmap-Advanced.md)

---

## 🎯 Lab Objective
Discover live hosts on the network quickly and efficiently.

## 🌐 Direct Lab Access
- HTB Academy: https://academy.hackthebox.com/module/details/19

---

## 🛠️ Required Tools
- Nmap (pre-installed on Kali/Parrot)

---

## 📝 Command Reference

### 1. Ping Sweep (No Port Scan)
```bash
# ICMP Echo, TCP SYN to 443, TCP ACK to 80, ICMP Timestamp
nmap -sn 192.168.1.0/24

# Scan specific range
nmap -sn 192.168.1.10-50

# Scan single IP
nmap -sn 192.168.1.10
```

### 2. No Ping (Assume All Hosts Are Up)
```bash
nmap -Pn 192.168.1.0/24
```

### 3. ARP Scan (Local Network Only)
```bash
sudo nmap -PR 192.168.1.0/24
```

### 4. Output Formats
```bash
# Normal output (-oN)
nmap -sn 192.168.1.0/24 -oN host_discovery.txt

# XML output (-oX)
nmap -sn 192.168.1.0/24 -oX host_discovery.xml

# Grepable output (-oG)
nmap -sn 192.168.1.0/24 -oG host_discovery.gnmap

# All formats (-oA)
nmap -sn 192.168.1.0/24 -oA host_discovery
```

---

## 📊 Expected Output
List of live hosts with IP addresses and MAC addresses (if on local network).

---

## 🔗 Additional Resources
- Nmap Host Discovery: https://nmap.org/book/man-host-discovery.html

---


## 🧪 Hands-On Step-by-Step Exercise
1. **Local Host Discovery Sweep**: Locate live IP addresses in your lab network range:
   ```bash
   nmap -sn 192.168.1.0/24
   ```
2. **Analyze Output**: Observe which hosts responded to the ICMP/TCP probes. Note down their MAC addresses.
3. **ARP-Only Scan**: Scan a local subnet using ARP requests to bypass OS firewalls blocking ICMP:
   ```bash
   sudo nmap -PR -sn 192.168.1.0/24
   ```

---

[🏠 Path Home](Home.md) | [Next Lab ➡️](Lab-02-Easy-Track-Nmap-Advanced.md)
