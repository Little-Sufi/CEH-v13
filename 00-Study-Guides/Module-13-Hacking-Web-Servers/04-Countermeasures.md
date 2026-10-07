# 04. Countermeasures — Hacking Web Servers

> [!SHIELD] 🏰 **Defensive Hardening Standards & Secure Configurations**
> Direct technical extraction from official CEH v13 Syllabus (Module 13). Covers Web Server Banner Suppression, WebDAV Disabling, Service Account Least Privilege, and HTTP Header Hardening.

---

## 🛡️ 1. Web Server Hardening Checklist

### 1.1 Technical Defensive Standards

1. **Banner Suppression**:
   - **Apache (`httpd.conf`)**: Set `ServerTokens Prod` and `ServerSignature Off`.
   - **PHP (`php.ini`)**: Set `expose_php = Off`.
   - **IIS**: Use URL Rewrite module to strip `Server` and `X-Powered-By` headers.
2. **Disable Directory Browsing**:
   - **Apache**: Remove `Indexes` from `Options` directive (`Options -Indexes`).
   - **IIS**: Disable Directory Browsing in IIS Manager.
3. **Disable Unnecessary HTTP Methods & WebDAV**: Block `PUT`, `DELETE`, `TRACE`, `TRACK`, and `MOVE` methods in web server configuration.
4. **Least Privilege Service Isolation**: Run web server daemon processes under unprivileged, dedicated service accounts (e.g., `www-data` in Linux, `IIS_IUSRS` / Managed Service Accounts in Windows).

> [!SHIELD] 🏰 **📋 Comprehensive Web Server Hardening Reference Matrix**

| Defensive Control | Apache Directive / IIS Config | Security Hardening Outcome |
| :--- | :--- | :--- |
| **Suppress Server Banner** | `ServerTokens Prod` | Prevents automated version fingerprinting |
| **Disable Directory Listing**| `Options -Indexes` | Blocks unauthorized file browsing |
| **Restrict HTTP Methods** | `<LimitExcept GET POST HEAD>` | Blocks WebDAV `PUT`/`DELETE` arbitrary uploads |
| **Patch Bash Kernel** | `apt update && apt install bash` | Fixes Shellshock (CVE-2014-6271) RCE vulnerability |
