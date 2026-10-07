# Lab 05: Amass - Advanced DNS Enumeration

[⬅️ Previous](Lab-04-Intermediate-Track-Shodan.md) | [🏠 Path Home](Home.md) | [Next Lab ➡️](Lab-06-Advanced-Track-Corporate-OSINT.md)

---

## 🎯 Lab Objective
Aggressive subdomain enumeration with active verification.

## 🌐 Direct Lab Access
- GitHub Repo: https://github.com/owasp-amass/amass
- TryHackMe: https://tryhackme.com/room/subdomainenumeration

---

## 🛠️ Installation
```bash
# Kali/Parrot
sudo apt install amass

# Install via snap
sudo snap install amass

# Install from GitHub
git clone https://github.com/owasp-amass/amass.git
cd amass
go install ./...
```

---

## 📝 Command Reference

### Basic Enumeration
```bash
# Passive enumeration
amass enum -passive -d targetdomain.com

# Active enumeration
amass enum -active -d targetdomain.com

# Aggressive with active verification
amass enum -active -d targetdomain.com -o subdomains.txt
```

### Advanced Enumeration with Wordlists
```bash
# Use custom wordlist
amass enum -d targetdomain.com -w /usr/share/wordlists/dirb/common.txt

# Brute force subdomains
amass enum -brute -d targetdomain.com
```

### Full Enumeration Options
```bash
amass enum -d targetdomain.com \
  -active \
  -brute \
  -w /usr/share/wordlists/seclists/Discovery/DNS/subdomains-top1million-5000.txt \
  -o amass_results.txt \
  -json amass_results.json
```

---

## 🔗 Additional Resources
- OWASP Amass Docs: https://github.com/owasp-amass/amass
- SecLists: https://github.com/danielmiessler/SecLists

---

[⬅️ Previous](Lab-04-Intermediate-Track-Shodan.md) | 
## 🧪 Hands-On Step-by-Step Exercise
1. **Subdomain Enumeration**: Use OWASP Amass to perform active and passive subdomain mapping:
   ```bash
   amass enum -d nmap.org -passive
   ```
2. **Active Discovery**: Perform brute-forcing and DNS resolutions:
   ```bash
   amass enum -d nmap.org -active -brute -src
   ```

---

[🏠 Path Home](Home.md) | [Next Lab ➡️](Lab-06-Advanced-Track-Corporate-OSINT.md)
