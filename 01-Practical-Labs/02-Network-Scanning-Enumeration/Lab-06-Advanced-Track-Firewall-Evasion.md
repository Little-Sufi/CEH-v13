# Lab 06: Firewall Evasion Techniques

[⬅️ Previous](Lab-05-Intermediate-Track-FTP-SMTP-Enumeration.md) | [🏠 Path Home](Home.md)

---

## 🎯 Lab Objective
Evade firewalls and IDS/IPS systems during scanning.

## 🌐 Direct Lab Access
- Nmap Reference: https://nmap.org/book/man-bypass-firewalls-ids.html

---

## 🛠️ Required Tools
- Nmap
- hping3

---

## 📝 Nmap Evasion Techniques

### 1. Fragment Packets (-f)
```bash
sudo nmap -f 192.168.1.10

# 8-byte fragments
sudo nmap -f -f 192.168.1.10
```

### 2. Decoys (-D)
```bash
# Use random decoy IPs
sudo nmap -D RND:5 192.168.1.10

# Use specific decoy IPs
sudo nmap -D 192.168.1.1,192.168.1.2,192.168.1.3 192.168.1.10
```

### 3. Spoof MAC Address (--spoof-mac)
```bash
# Random MAC
sudo nmap --spoof-mac 0 192.168.1.10

# Specific MAC
sudo nmap --spoof-mac 00:11:22:33:44:55 192.168.1.10

# Vendor MAC
sudo nmap --spoof-mac Apple 192.168.1.10
```

### 4. Append Random Data (--data-length)
```bash
sudo nmap --data-length 24 192.168.1.10
```

### 5. Randomize Host Order (--randomize-hosts)
```bash
nmap --randomize-hosts 192.168.1.0/24
```

### 6. Source Port Spoofing (-g / --source-port)
```bash
sudo nmap -g 53 192.168.1.10  # DNS port
sudo nmap -g 80 192.168.1.10  # HTTP port
sudo nmap -g 443 192.168.1.10 # HTTPS port
```

### 7. Slow Timing (-T0 / -T1)
```bash
nmap -T0 192.168.1.10
nmap -T1 192.168.1.10
```

### 8. Full Evasion Scan
```bash
sudo nmap -f -D RND:10 --spoof-mac 0 --data-length 24 -g 53 -T1 -p- 192.168.1.10
```

---

## 📝 hping3
```bash
# Send TCP SYN packets
sudo hping3 -S -p 80 192.168.1.10

# Send fragmented packets
sudo hping3 -f -S -p 80 192.168.1.10
```

---

## 🔗 Additional Resources
- Nmap Firewall Evasion: https://nmap.org/book/man-bypass-firewalls-ids.html

---

[⬅️ Previous](Lab-05-Intermediate-Track-FTP-SMTP-Enumeration.md) | [🏠 Path Home](Home.md)
