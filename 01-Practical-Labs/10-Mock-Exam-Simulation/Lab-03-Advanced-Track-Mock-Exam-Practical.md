![Lab Image](https://images.unsplash.com/photo-1456513080510-7bf3a84b82f8?w=800&h=200&fit=crop)

[⬅️ Previous](Lab-02-Advanced-Track-Mock-Exam-Theory.md) | [🏠 Path Home](Home.md)

---

# Lab 03: Advanced Track - Mock Exam Practical

---


---




---


---

[⬅️ Path Home](Home.md)

---

## 🎯 Lab Objectives
- Prepare for the 20-question, 6-hour CEH Practical Exam.
- Implement exploitation, analysis, and data retrieval in live lab environments.
- Verify shell management, network mapping, and hash recovery skills.

## 🛠️ Required Tools & Setup
- **Attack VM:** Kali Linux.
- **Target Network:** Active Directory and Vulnerable Web servers.
- **Practice Room:** [TryHackMe Attacktive Directory](https://tryhackme.com/room/attacktivedirectory)

## 🚶 Step-by-Step Lab Guide

### Step 1: Executing Host Discovery
Locate active endpoints across the subnet range:
```bash
nmap -sn 10.10.10.0/24
```

### Step 2: Accessing and Exploiting a Service
Locate open SMB shares, list contents, and retrieve the hidden flag:
```bash
smbclient -L //target_ip/ -N
```

---

[⬅️ Path Home](Home.md)

---

[⬅️ Previous](Lab-02-Advanced-Track-Mock-Exam-Theory.md) | [🏠 Path Home](Home.md)
