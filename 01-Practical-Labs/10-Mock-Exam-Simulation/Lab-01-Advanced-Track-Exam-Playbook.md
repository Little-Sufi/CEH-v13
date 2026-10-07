![Lab Header](https://images.unsplash.com/photo-1526374965328-7f61d4dc18c5?w=800&h=150&fit=crop)

[🏠 Path Home](Home.md) | [Next Lab ➡️](Lab-02-Advanced-Track-Mock-Exam-Theory.md)

---

# Lab 01: Advanced Track - 6-Hour Practical Exam Playbook

---


---


[Path Home](Home.md)
---

---


---

## 🎯 Objective
Execute a structured checklist to identify, exploit, and document targets under a simulated 6-hour time limit.

## 📝 Playbook Guide
### Step 1: Subnet Discovery
```bash
# Identify live hosts using Nmap Ping sweep
nmap -sn 10.10.10.0/24 -oG ping_sweep.txt
```

### Step 2: Full Port Sweep
```bash
# Port scan all discovered targets
nmap -p- -sV -sC -T4 -iL ping_sweep.txt -oA full_port_audit
```

### Step 3: Web App Enumeration
Inspect web portals running on ports 80/443/8080/8443:
```bash
gobuster dir -u http://10.10.10.15:8080 -w /usr/share/wordlists/dirb/common.txt
nikto -h http://10.10.10.15:8080
```



---
[Path Home](Home.md)

---

[🏠 Path Home](Home.md) | [Next Lab ➡️](Lab-02-Advanced-Track-Mock-Exam-Theory.md)
