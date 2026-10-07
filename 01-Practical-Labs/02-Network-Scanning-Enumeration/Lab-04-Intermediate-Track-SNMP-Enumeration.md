# Lab 04: SNMP Enumeration (snmpwalk, snmp-check)

[⬅️ Previous](Lab-03-Intermediate-Track-SMB-Enumeration.md) | [🏠 Path Home](Home.md) | [Next Lab ➡️](Lab-05-Intermediate-Track-FTP-SMTP-Enumeration.md)

---

## 🎯 Lab Objective
Extract router/switch/device data via SNMP.

## 🌐 Direct Lab Access
- TryHackMe: https://tryhackme.com/room/networkservices2

---

## 🛠️ Required Tools

| Tool | Purpose | Installation |
|------|---------|--------------|
| snmpwalk | SNMP query tool | `sudo apt install snmp` |
| snmp-check | SNMP enumeration | Pre-installed on Kali |
| onesixtyone | SNMP community string brute force | `sudo apt install onesixtyone` |

---

## 📝 Command Reference

### 1. snmpwalk
```bash
# Using default 'public' community string (v2c)
snmpwalk -v2c -c public 192.168.1.10

# Specific OID
snmpwalk -v2c -c public 192.168.1.10 1.3.6.1.2.1.1  # System info
snmpwalk -v2c -c public 192.168.1.10 1.3.6.1.2.1.25 # Windows processes

# Version 1
snmpwalk -v1 -c public 192.168.1.10
```

### 2. snmp-check
```bash
snmp-check 192.168.1.10
snmp-check 192.168.1.10 -c private
```

### 3. onesixtyone (Community String Brute Force)
```bash
# Create community string list
echo "public" > community.txt
echo "private" >> community.txt
echo "manager" >> community.txt

# Run brute force
onesixtyone -c community.txt 192.168.1.10
```

### 4. Nmap NSE Scripts
```bash
nmap -sU -p 161 --script snmp* 192.168.1.10
```

---

## 📊 Expected Results
- System description
- Uptime
- Network interfaces
- Running processes (Windows)
- Installed software

---

## 🔗 Additional Resources
- SNMP OID Reference: http://www.oid-info.com/

---

[⬅️ Previous](Lab-03-Intermediate-Track-SMB-Enumeration.md) | [🏠 Path Home](Home.md) | [Next Lab ➡️](Lab-05-Intermediate-Track-FTP-SMTP-Enumeration.md)
