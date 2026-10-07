# 03. Tools — Social Engineering

> [!TOOL] 🛠️ **Command-Line & GUI Social Engineering Software Reference Matrix**
> Direct technical extraction from official CEH v13 Syllabus (Module 09). Covers SET (Social Engineering Toolkit), GoPhish, Evilginx2, Maltego, and King Phisher.

---

## 🛠️ 1. Primary Social Engineering Tools Reference Matrix

> [!TOOL] 📋 **Comprehensive Social Engineering Software Reference Matrix**

| Utility Name | Vendor / Developer | Primary Operational Role | Platform Support |
| :--- | :--- | :--- | :--- |
| **SET (Social-Engineer Toolkit)**| TrustedSec | Automated social engineering attack framework | Linux |
| **GoPhish** | Jordan Wright | Open-source enterprise phishing simulation platform | Cross-platform |
| **Evilginx2** | Kuba Gretcky | Man-in-the-Middle reverse proxy phishing framework (2FA bypass)| Linux |
| **Maltego** | Paterva | OSINT relationship mapping & entity footprinting | Cross-platform |
| **King Phisher** | SecureState | Enterprise phishing campaign evaluation suite | Linux |

---

## 💻 2. Execution CLI Commands

### 2.1 Evilginx2 2FA Bypass Reverse Proxy Syntax
- **Configure Phishlet domain**:
  ```bash
  config domain phishdomain.com
  config ip 192.168.1.100
  ```
- **Enable Office365 Phishlet**:
  ```bash
  phishlets enable o365
  lures create o365
  ```
