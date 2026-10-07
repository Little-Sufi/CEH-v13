# Lab 03: Responder - LLMNR/NBT-NS Poisoning

[⬅️ Previous](Lab-02-Easy-Track-Wireshark.md) | [🏠 Path Home](Home.md) | [Next Lab ➡️](Lab-04-Intermediate-Track-Impacket.md)

---

## 🎯 Lab Objective
Capture NTLMv2 hashes via LLMNR/NBT-NS poisoning.

## 🌐 Direct Lab Access
- TryHackMe: https://tryhackme.com/room/responder
- Responder GitHub: https://github.com/lgandx/Responder

---

## 🛠️ Installation
```bash
# Pre-installed on Kali/Parrot
responder -h
```

---

## 📝 Responder Commands

### Listen on Interface
```bash
sudo responder -I tun0 -dwv
```

### Capture Hashes
Hashes will be saved to `/usr/share/responder/logs/`

### Crack NTLMv2 Hashes
```bash
hashcat -m 5600 hashes.txt /usr/share/wordlists/rockyou.txt
```

---

## 🔗 Additional Resources
- PayloadsAllTheThings: https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/Methodology%20and%20Resources/Windows%20-%20LLMNR%20-%20NBTNS.md

---

[⬅️ Previous](Lab-02-Easy-Track-Wireshark.md) | [🏠 Path Home](Home.md) | [Next Lab ➡️](Lab-04-Intermediate-Track-Impacket.md)
