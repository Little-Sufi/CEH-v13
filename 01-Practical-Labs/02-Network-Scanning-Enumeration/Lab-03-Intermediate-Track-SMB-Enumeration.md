# Lab 03: SMB Enumeration (Enum4Linux, smbclient)

[⬅️ Previous](Lab-02-Easy-Track-Nmap-Advanced.md) | [🏠 Path Home](Home.md) | [Next Lab ➡️](Lab-04-Intermediate-Track-SNMP-Enumeration.md)

---

## 🎯 Lab Objective
Extract user lists, machine names, share permissions, and password policies from SMB/Samba.

## 🌐 Direct Lab Access
- TryHackMe: https://tryhackme.com/room/networkservices

---

## 🛠️ Required Tools

| Tool | Purpose | Installation |
|------|---------|--------------|
| enum4linux | SMB enumeration | Pre-installed on Kali |
| enum4linux-ng | Improved enum4linux | `git clone https://github.com/cddmp/enum4linux-ng.git` |
| smbclient | SMB client | Pre-installed |
| smbmap | SMB share mapping | `sudo apt install smbmap` |
| crackmapexec | Swiss army knife for Windows | `sudo apt install crackmapexec` |

---

## 📝 Command Reference

### 1. enum4linux
```bash
# Full enumeration
enum4linux -a 192.168.1.10

# Specific options
enum4linux -U 192.168.1.10  # User enumeration
enum4linux -M 192.168.1.10  # Machine enumeration
enum4linux -S 192.168.1.10  # Share enumeration
enum4linux -P 192.168.1.10  # Password policy
enum4linux -G 192.168.1.10  # Groups
```

### 2. enum4linux-ng
```bash
cd enum4linux-ng
python3 enum4linux-ng.py 192.168.1.10 -A
```

### 3. smbclient
```bash
# List shares (null session)
smbclient -L //192.168.1.10 -N

# Connect to a share
smbclient //192.168.1.10/share_name -N

# With credentials
smbclient //192.168.1.10/share_name -U username%password
```

### 4. smbmap
```bash
# List shares with permissions
smbmap -H 192.168.1.10

# With credentials
smbmap -H 192.168.1.10 -u username -p password

# List files in share
smbmap -H 192.168.1.10 -u username -p password -r share_name
```

### 5. CrackMapExec
```bash
# SMB enumeration
crackmapexec smb 192.168.1.10 --shares
crackmapexec smb 192.168.1.10 --users
crackmapexec smb 192.168.1.10 --groups
```

---

## 📊 Expected Results
- List of users
- List of shares and permissions
- Password policy information
- Machine accounts

---

## 🔗 Additional Resources
- Samba Documentation: https://www.samba.org/samba/docs/

---

[⬅️ Previous](Lab-02-Easy-Track-Nmap-Advanced.md) | [🏠 Path Home](Home.md) | [Next Lab ➡️](Lab-04-Intermediate-Track-SNMP-Enumeration.md)
