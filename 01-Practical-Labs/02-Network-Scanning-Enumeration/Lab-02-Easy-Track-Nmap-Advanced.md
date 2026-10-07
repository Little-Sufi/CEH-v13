# Lab 02: Nmap Advanced - Port Scanning & Service Detection

[⬅️ Previous](Lab-01-Easy-Track-Nmap-Basics.md) | [🏠 Path Home](Home.md) | [Next Lab ➡️](Lab-03-Intermediate-Track-SMB-Enumeration.md)

---

## 🎯 Lab Objective
Perform detailed port scanning, version detection, OS detection, and script scanning.

## 🌐 Direct Lab Access
- HTB Academy: https://academy.hackthebox.com/module/details/19

---

## 🛠️ Required Tools
- Nmap

---

## 📝 Command Reference

### 1. TCP Connect Scan (-sT)
```bash
nmap -sT 192.168.1.10
```

### 2. SYN Stealth Scan (-sS) [Default for root]
```bash
sudo nmap -sS 192.168.1.10
```

### 3. UDP Scan (-sU)
```bash
sudo nmap -sU 192.168.1.10
```

### 4. Port Specification
```bash
# Scan specific ports
nmap -p 22,80,443 192.168.1.10

# Scan all 65535 ports
nmap -p- 192.168.1.10

# Scan top 100 ports
nmap --top-ports 100 192.168.1.10
```

### 5. Service Version Detection (-sV)
```bash
nmap -sV 192.168.1.10

# Aggressive version detection
nmap -sV --version-intensity 9 192.168.1.10
```

### 6. OS Detection (-O)
```bash
sudo nmap -O 192.168.1.10
```

### 7. Default Script Scan (-sC)
```bash
nmap -sC 192.168.1.10
```

### 8. Full Aggressive Scan (-A)
```bash
# Equivalent to -sV -sC -O --traceroute
sudo nmap -A 192.168.1.10
```

### 9. Detailed Targeted Scan (Recommended)
```bash
sudo nmap -p- -sV -sC -O -T4 192.168.1.10 -oN full_tcp_scan.txt
```

### 10. Timing Templates (-T0 to -T5)
```bash
# Paranoid (very slow, evasion)
nmap -T0 192.168.1.10

# Sneaky
nmap -T1 192.168.1.10

# Polite
nmap -T2 192.168.1.10

# Normal (default)
nmap -T3 192.168.1.10

# Aggressive (fast)
nmap -T4 192.168.1.10

# Insane (very fast, may miss ports)
nmap -T5 192.168.1.10
```

---

## 📊 Expected Output
- Open/closed/filtered ports
- Service versions
- OS guess
- Script results

---

## 🔗 Additional Resources
- Nmap Port Scanning: https://nmap.org/book/man-port-scanning-techniques.html
- Nmap Scripting Engine: https://nmap.org/book/nse.html

---

[⬅️ Previous](Lab-01-Easy-Track-Nmap-Basics.md) | 
## 🧪 Hands-On Step-by-Step Exercise
1. **Stealth Port Scan**: Execute a SYN stealth scan against open ports:
   ```bash
   sudo nmap -sS -p 1-1000 -T4 10.0.2.15
   ```
2. **Version and OS Detection**: Audit the running services and operating system family:
   ```bash
   sudo nmap -sS -sV -O 10.0.2.15
   ```
3. **Comprehensive Vulnerability Check**: Run vulnerability detection scripts:
   ```bash
   sudo nmap --script vuln 10.0.2.15
   ```

---

[🏠 Path Home](Home.md) | [Next Lab ➡️](Lab-03-Intermediate-Track-SMB-Enumeration.md)
