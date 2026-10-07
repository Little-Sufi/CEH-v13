# Lab 01: Tcpdump & Tshark - Packet Capture

[🏠 Path Home](Home.md) | [Next Lab ➡️](Lab-02-Easy-Track-Wireshark.md)

---

## 🎯 Lab Objective
Capture and analyze network traffic from command line.

## 🌐 Direct Lab Access
- Tcpdump Docs: https://www.tcpdump.org/docs/
- Tshark Docs: https://www.wireshark.org/docs/man-pages/tshark.html

---

## 📝 Tcpdump Commands

### Capture on Interface
```bash
sudo tcpdump -i eth0
sudo tcpdump -i tun0
```

### Capture and Save to File
```bash
sudo tcpdump -i eth0 -w capture.pcap
```

### Read from File
```bash
tcpdump -r capture.pcap
```

### Filter Traffic
```bash
sudo tcpdump -i eth0 port 21  # FTP
sudo tcpdump -i eth0 port 23  # Telnet
sudo tcpdump -i eth0 port 80  # HTTP
sudo tcpdump -i eth0 host 192.168.1.10
```

---

## 📝 Tshark Commands

### Basic Capture
```bash
sudo tshark -i eth0
```

### Save to File
```bash
sudo tshark -i eth0 -w capture.pcap
```

### Read from File
```bash
tshark -r capture.pcap
```

### Extract HTTP POST Data
```bash
tshark -r capture.pcap -Y "http.request.method == POST" -T fields -e http.file_data
```

### Display Specific Fields
```bash
tshark -r capture.pcap -T fields -e ip.src -e ip.dst -e tcp.srcport -e tcp.dstport
```

---

## 🔗 Additional Resources
- PacketLife Cheat Sheets: https://packetlife.net/library/cheat-sheets/

---

[🏠 Path Home](Home.md) | [Next Lab ➡️](Lab-02-Easy-Track-Wireshark.md)
