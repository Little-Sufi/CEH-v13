# Lab 02: Advanced Google Dorking

[⬅️ Previous](Lab-01-Easy-Track-Passive-Recon.md) | [🏠 Path Home](Home.md) | [Next Lab ➡️](Lab-03-Easy-Track-theHarvester.md)

---

## 🎯 Lab Objective
Master advanced search engine exploitation to find sensitive information.

## 🌐 Direct Lab Access
- TryHackMe Room: https://tryhackme.com/room/googledorking
- Google Hacking Database: https://www.exploit-db.com/google-hacking-database

---

## 🛠️ Required Tools
- Web browser (Chrome/Firefox)
- Google Search

---

## 📝 Essential Dorks

### File Type Dorks
```
site:targetdomain.com filetype:pdf
site:targetdomain.com filetype:doc
site:targetdomain.com filetype:xls
site:targetdomain.com filetype:docx
site:targetdomain.com filetype:txt
site:targetdomain.com filetype:bak
site:targetdomain.com filetype:sql
site:targetdomain.com filetype:conf
site:targetdomain.com filetype:env
```

### Directory & Login Pages
```
site:targetdomain.com intitle:"index of"
site:targetdomain.com intitle:"admin"
site:targetdomain.com intitle:"login"
site:targetdomain.com inurl:admin
site:targetdomain.com inurl:login
site:targetdomain.com inurl:wp-admin
```

### Sensitive Information
```
site:targetdomain.com "password"
site:targetdomain.com "api_key"
site:targetdomain.com "secret"
site:targetdomain.com "database"
site:targetdomain.com "credentials"
site:targetdomain.com "@targetdomain.com"
```

### Web Vulnerabilities
```
site:targetdomain.com inurl:php?id=
site:targetdomain.com inurl:asp?id=
site:targetdomain.com inurl:jsp?id=
site:targetdomain.com inurl:file=
site:targetdomain.com inurl:path=
```

### Employee Profiles
```
site:linkedin.com company:"Target Company"
site:github.com "targetdomain.com"
site:twitter.com "targetdomain.com"
```

---

## 📋 Practical Exercise
1. Use Google Dorks on your test domain
2. Document all findings
3. Check Exploit-DB for new dorks
4. Use https://pentest-tools.com/google-hacking for automated scanning

---

## 🔗 Additional Resources
- Exploit-DB GHDB: https://www.exploit-db.com/google-hacking-database
- Google Advanced Search: https://www.google.com/advanced_search

---

[⬅️ Previous](Lab-01-Easy-Track-Passive-Recon.md) | 
## 🧪 Hands-On Step-by-Step Exercise
1. **Directory Listing Discovery**: Search for servers exposing index listings on target domains:
   ```text
   site:scanme.nmap.org intitle:"index of"
   ```
2. **Document Exfiltration search**: Query public search engines for leaked PDF or DOCX documentation containing corporate configurations:
   ```text
   site:nmap.org filetype:pdf OR filetype:doc OR filetype:xls
   ```
3. **Exposed Configuration Files**: Look for generic database backups or setup logs containing credentials:
   ```text
   filetype:sql "insert into" "password"
   filetype:log intext:"database connection failed"
   ```

---

[🏠 Path Home](Home.md) | [Next Lab ➡️](Lab-03-Easy-Track-theHarvester.md)
