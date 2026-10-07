# Lab 03: theHarvester - Email & Subdomain Harvesting

[⬅️ Previous](Lab-02-Easy-Track-Google-Dorking.md) | [🏠 Path Home](Home.md) | [Next Lab ➡️](Lab-04-Intermediate-Track-Shodan.md)

---

## 🎯 Lab Objective
Extract emails, subdomains, and employee names from public sources.

## 🌐 Direct Lab Access
- GitHub Repo: https://github.com/laramies/theHarvester
- TryHackMe: https://tryhackme.com/room/osint

---

## 🛠️ Installation
```bash
# Kali/Parrot (pre-installed)
theHarvester -h

# Install via pip
pip3 install theHarvester

# Install from GitHub
git clone https://github.com/laramies/theHarvester.git
cd theHarvester
pip3 install -r requirements.txt
python3 theHarvester.py -h
```

---

## 📝 Command Reference

### Basic Usage
```bash
# Search single source
theHarvester -d targetdomain.com -b google

# Search multiple sources
theHarvester -d targetdomain.com -b google,bing,yahoo

# Limit results
theHarvester -d targetdomain.com -b google -l 500
```

### Full Aggressive Scan
```bash
theHarvester -d targetdomain.com \
  -l 1000 \
  -b google,linkedin,bing,crtsh,duckduckgo,twitter,yahoo \
  -f recon_results.html
```

### All Available Sources
```
all, anubis, baidu, bevigil, binaryedge, bing, bingapi,
bufferoverun, censys, certspotter, crtsh, dnsdumpster,
duckduckgo, fullhunt, github-code, google, hackertarget,
hunter, intelx, netlas, onyphe, otx, pentesttools,
projectdiscovery, qwant, rapiddns, rocketreach, securityTrails,
sitedossier, subdomaincenter, subdomainfinderc99, threatminer,
tomba, twitter, urlscan, virustotal, yahoo, zoomeye
```

---

## 📊 Output Formats
- `-f filename.html` - HTML report
- `-f filename.xml` - XML report
- `-f filename.json` - JSON report

---

## 🔗 Additional Resources
- Hunter.io: https://hunter.io
- Snov.io: https://snov.io

---

[⬅️ Previous](Lab-02-Easy-Track-Google-Dorking.md) | 
## 🧪 Hands-On Step-by-Step Exercise
1. **Automated OSINT Harvesting**: Run `theHarvester` on Kali against a public test domain to extract email directories and subdomains:
   ```bash
   theHarvester -d nmap.org -l 200 -b google,bing
   ```
2. **Analyze Output**: Review the terminal output for discovered email structures (e.g., `first.last@nmap.org`) and host IP addresses.

---

[🏠 Path Home](Home.md) | [Next Lab ➡️](Lab-04-Intermediate-Track-Shodan.md)
