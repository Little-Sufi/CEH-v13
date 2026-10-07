# Lab 06: Password Cracking (Hashcat, John)

[⬅️ Previous](Lab-03-Intermediate-Track-Meterpreter-Post.md) | [🏠 Path Home](Home.md) | [Next Lab ➡️](Lab-05-Advanced-Track-Linux-Privesc.md)

---

## 🎯 Lab Objective
Crack password hashes.

## 🌐 Direct Lab Access
- TryHackMe: https://tryhackme.com/room/hydra
- Hashcat Wiki: https://hashcat.net/wiki/

---

## 🛠️ Required Tools
- Hashcat
- John the Ripper
- Hydra
- RockYou wordlist: `/usr/share/wordlists/rockyou.txt`

---

## 📝 Hashcat Commands

### Identify Hash Type
```bash
hashcat --help | grep -i "hash type"
```

### Common Hash Modes
| Hash Type | Mode |
|-----------|------|
| MD5 | 0 |
| SHA1 | 100 |
| SHA256 | 1400 |
| NTLM | 1000 |
| SHA512 | 1700 |
| WPA/WPA2 | 2500 |

### Crack NTLM (Windows)
```bash
hashcat -m 1000 -a 0 hashes.txt /usr/share/wordlists/rockyou.txt
```

### Crack SHA256
```bash
hashcat -m 1400 -a 0 hashes.txt /usr/share/wordlists/rockyou.txt
```

---

## 📝 John the Ripper Commands

### Crack Linux Shadow
```bash
unshadow /etc/passwd /etc/shadow > unshadowed.txt
john --wordlist=/usr/share/wordlists/rockyou.txt unshadowed.txt
```

### Show Cracked Passwords
```bash
john --show unshadowed.txt
```

---

## 📝 Hydra (Brute Force)

### SSH
```bash
hydra -l username -P /usr/share/wordlists/rockyou.txt ssh://192.168.1.10
```

### FTP
```bash
hydra -l username -P /usr/share/wordlists/rockyou.txt ftp://192.168.1.10
```

### HTTP POST
```bash
hydra -l username -P /usr/share/wordlists/rockyou.txt 192.168.1.10 http-post-form "/login.php:username=^USER^&password=^PASS^:Invalid credentials"
```

---

## 🔗 Additional Resources
- Hashcat Example Hashes: https://hashcat.net/wiki/doku.php?id=example_hashes

---

[⬅️ Previous](Lab-03-Intermediate-Track-Meterpreter-Post.md) | [🏠 Path Home](Home.md) | [Next Lab ➡️](Lab-05-Advanced-Track-Linux-Privesc.md)
