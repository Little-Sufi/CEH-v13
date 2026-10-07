# Lab 04: Mobile Security (MobSF, APK Analysis)

[⬅️ Previous](Lab-01-Easy-Track-Wireless-Hacking.md) | [🏠 Path Home](Home.md) | [Next Lab ➡️](Lab-03-Advanced-Track-AWS-Security.md)

---

## 🎯 Lab Objective
Analyze Android APKs for vulnerabilities.

## 🌐 Direct Lab Access
- TryHackMe: https://tryhackme.com/room/androidanalysis
- MobSF GitHub: https://github.com/MobSF/Mobile-Security-Framework-MobSF

---

## 🛠️ Setup MobSF

### Docker
```bash
docker pull opensecurity/mobile-security-framework-mobsf
docker run -d -p 8000:8000 opensecurity/mobile-security-framework-mobsf
# Access at http://localhost:8000
```

---

## 📝 APK Analysis
1. Upload APK to MobSF
2. Analyze static report for:
   - Hardcoded API keys
   - Insecure permissions
   - Insecure Firebase DB
   - Exported activities

---

## 🔗 Additional Resources
- OWASP Mobile Security Testing Guide: https://owasp.org/www-project-mobile-security-testing-guide/

---

[⬅️ Previous](Lab-01-Easy-Track-Wireless-Hacking.md) | [🏠 Path Home](Home.md) | [Next Lab ➡️](Lab-03-Advanced-Track-AWS-Security.md)
