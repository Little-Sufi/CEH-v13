![Lab Image](https://images.unsplash.com/photo-1526374965328-7f61d4dc18c5?w=800&h=200&fit=crop)

[⬅️ Previous](Lab-05-Advanced-Track-IoT-Hacking.md) | [🏠 Path Home](Home.md)

---

# Lab 06: Advanced Track - OT & SCADA Security

---


---




---


---

[⬅️ Path Home](Home.md)

---

## 🎯 Lab Objectives
- Understand Operational Technology (OT) and SCADA environments.
- Analyze Modbus TCP protocol communication.
- Perform simulation-based SCADA network scanning and register modification.

## 🛠️ Required Tools & Setup
- **Wireshark:** Modbus TCP packet capture and analysis.
- **Nmap:** Identifying Modbus ports (502/tcp).
- **ModbusPal:** Modbus simulator.
- **Practice Room:** [TryHackMe Intro to SCADA](https://tryhackme.com/room/introtoscada)

## 🚶 Step-by-Step Lab Guide

### Step 1: Modbus Port Discovery
Scan the simulation network for active Modbus slave devices:
```bash
nmap -p 502 --script modbus-discover target_ip
```

### Step 2: Analyzing Modbus Traffic in Wireshark
Filter for Modbus protocol packets:
```text
modbus
```
Observe transaction IDs, function codes, and holding register data.

---

[⬅️ Path Home](Home.md)

---

[⬅️ Previous](Lab-05-Advanced-Track-IoT-Hacking.md) | [🏠 Path Home](Home.md)
