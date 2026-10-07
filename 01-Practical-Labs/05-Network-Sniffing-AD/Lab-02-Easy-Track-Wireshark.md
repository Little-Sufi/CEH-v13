# Lab 02: Wireshark - Traffic Analysis

[⬅️ Previous](Lab-01-Easy-Track-Tcpdump-Tshark.md) | [🏠 Path Home](Home.md) | [Next Lab ➡️](Lab-03-Intermediate-Track-Responder.md)

---

## 🎯 Lab Objective
Analyze captured network traffic with Wireshark.

## 🌐 Direct Lab Access
- TryHackMe: https://tryhackme.com/room/wiresharkthebasics
- Wireshark Docs: https://www.wireshark.org/docs/

---

## 📝 Essential Wireshark Display Filters

| Filter | Purpose |
|--------|---------|
| `http` | HTTP traffic |
| `ftp` | FTP traffic |
| `telnet` | Telnet traffic |
| `smb` | SMB traffic |
| `kerberos` | Kerberos traffic |
| `ip.addr == 192.168.1.10` | Specific IP |
| `tcp.port == 80` | Specific port |
| `http.request.method == POST` | HTTP POST requests |

---

## 📝 Extract Credentials
1. FTP: Search for `ftp.request.command == PASS`
2. Telnet: Follow TCP stream
3. HTTP POST: Follow TCP stream or look at http.file_data

---

## 🔗 Additional Resources
- Wireshark Display Filter Reference: https://www.wireshark.org/docs/dfref/

---

[⬅️ Previous](Lab-01-Easy-Track-Tcpdump-Tshark.md) | [🏠 Path Home](Home.md) | [Next Lab ➡️](Lab-03-Intermediate-Track-Responder.md)
