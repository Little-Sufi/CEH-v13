# Lab 06: Corporate Profiling & Data Breach Hunting

[⬅️ Previous](Lab-05-Intermediate-Track-Amass.md) | [🏠 Path Home](Home.md)

---

## 🎯 Lab Objective
Deep dive into corporate profiling and data breach hunting.

## 🌐 Direct Lab Access
- HackViser OSINT Path: https://hackviser.com/training/paths/osint
- OSINT Framework: https://osintframework.com

---

## 🛠️ Essential Tools & Platforms

### Employee Profiling
| Platform | URL | Purpose |
|----------|-----|---------|
| LinkedIn | https://linkedin.com | Employee roles & connections |
| Hunter.io | https://hunter.io | Email addresses |
| Snov.io | https://snov.io | Email verification |
| HaveIBeenPwned | https://haveibeenpwned.com | Data breach checks |
| Dehashed | https://dehashed.com | Breached credentials |

### Company Information
| Platform | URL | Purpose |
|----------|-----|---------|
| Crunchbase | https://crunchbase.com | Company funding & info |
| Opencorporates | https://opencorporates.com | Company registrations |
| Wayback Machine | https://archive.org/web/ | Historical website data |
| BuiltWith | https://builtwith.com | Technology stack |
| Wappalyzer | https://www.wappalyzer.com | Tech stack detection |

---

## 📝 Step-by-Step Guide

### 1. Employee Discovery
```markdown
1. Search LinkedIn for "Target Company" employees
2. Note job titles, departments, and connections
3. Use Hunter.io to find email formats
4. Check HaveIBeenPwned for breached emails
```

### 2. Technology Stack
```markdown
1. Visit targetdomain.com
2. Use Wappalyzer/BuiltWith to identify:
   - Web server (Apache/Nginx/IIS)
   - CMS (WordPress/Drupal/Joomla)
   - JavaScript frameworks
   - Analytics tools
```

### 3. Historical Data
```markdown
1. Use Wayback Machine to view old versions of targetdomain.com
2. Look for:
   - Old employee pages
   - Removed login portals
   - Exposed documents
```

### 4. Data Breach Hunting
```markdown
1. Check HaveIBeenPwned for target domain
2. Use Dehashed (paid) for detailed breach data
3. Search Pastebin for target mentions:
   - site:pastebin.com "targetdomain.com"
   - site:ghostbin.co "targetdomain.com"
```

---

## 🔗 Additional Resources
- OSINT Framework: https://osintframework.com
- IntelTechniques: https://inteltechniques.com
- Bellingcat: https://www.bellingcat.com

---

[⬅️ Previous](Lab-05-Intermediate-Track-Amass.md) | [🏠 Path Home](Home.md)
