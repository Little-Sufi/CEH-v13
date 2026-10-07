# 01. Overview and Concepts — Hacking Web Servers

> [!INFO] 📌 **Module Scope & Core Objectives**
> Direct technical extraction from official CEH v13 Syllabus (Module 13). Covers Web Server Architecture (Apache, Nginx, IIS), Web Server Attack Vectors (Directory Traversal, Shellshock, HTTP Response Splitting, WebDAV exploitation, HTTP Request Smuggling), Web Server Reconnaissance, and Web Server Hardening standards.

---

## 🧠 1. Web Server Architectures & Attack Taxonomies

### 1.1 Web Server Infrastructure & Core Components
Web servers process incoming HTTP/HTTPS requests from clients, execute application code (PHP, ASP.NET, Python), and serve dynamic or static content.
- **Apache HTTP Server**: Modular architecture utilizing `.htaccess` files for directory-level configuration. Uses `mod_php`, `mod_ssl`, and worker/event MPMs.
- **Microsoft Internet Information Services (IIS)**: Uses `web.config` for configuration settings, `Application Pools` for process isolation, and `inetpub\wwwroot` as default document root.
- **Nginx**: Asynchronous, event-driven reverse proxy and web server optimized for high concurrency.

### 1.2 Web Server Attack Vectors
1. **Directory Traversal (Path Traversal)**: Exploits unsanitized file path inputs to access files outside the web root directory (`../../../../etc/passwd` or `..\..\..\boot.ini`).
2. **Shellshock (GNU Bash RCE)**: Exploits vulnerable Bash versions (CVE-2014-6271) via HTTP request headers (e.g., `User-Agent`) when CGI scripts process environment variables containing trailing function definitions: `() { :;}; /bin/bash -c "id"`.
3. **WebDAV Exploitation**: Misconfigured WebDAV (Web Distributed Authoring and Versioning) enables HTTP methods like `PUT`, `DELETE`, `MOVE`, allowing attackers to upload webshells directly to web roots.
4. **HTTP Response Splitting**: Injects `CRLF` sequence (`\r\n` or `%0d%0a`) into HTTP response headers, allowing attackers to split HTTP responses and execute XSS or Cache Poisoning.
5. **HTTP Request Smuggling**: Exploits desynchronization between front-end proxy servers and backend web servers evaluating `Content-Length` (CL) vs `Transfer-Encoding` (TE) headers.

> [!ABSTRACT] 🏛️ **📋 Comprehensive Web Server Attack Vector Matrix**

| Attack Vector | Primary Vulnerability Target | Exploitation Payload / Mechanism | Primary Impact |
| :--- | :--- | :--- | :--- |
| **Directory Traversal** | Unsanitized file path input | `../../../../etc/passwd` | Arbitrary File Disclosure |
| **Shellshock (CGI RCE)**| Vulnerable GNU Bash kernel | `User-Agent: () { :;}; echo; /bin/id` | Unauthenticated RCE |
| **WebDAV PUT Method** | Misconfigured HTTP permissions | `davtest -url http://target/dav/` | Web Shell Upload & Execution |
| **HTTP Request Smuggling**| Front-end / Back-end CL.TE desync | Discrepancy between CL and TE headers | Cache Poisoning & Request Hijack |

---

## ⚡ 2. Reconnaissance & WebDAV Architecture

### 2.1 Web Server Reconnaissance & Footprinting
Attacker methodology begins with identifying web server software versions, enabled modules, virtual hosts, and administrative subdirectories.
- **Banner Grabbing**: Querying HTTP response headers (`Server: Apache/2.4.41 (Ubuntu)`) using `Netcat`, `curl -I`, or `Nmap`.
- **HTTP Header Enumeration**: Analyzing security headers (`X-Powered-By`, `X-Frame-Options`, `Strict-Transport-Security`).

> [!IMPORTANT] 🔄 **📋 Comprehensive HTTP Security Header Reference Matrix**

| Security Header | Mandatory Configuration | Primary Defense Mechanism |
| :--- | :--- | :--- |
| **`Server`** | Suppress / Obfuscate (`ServerTokens Prod`) | Hides web server OS and version banner |
| **`X-Powered-By`** | Remove completely | Hides backend framework details (e.g., PHP/5.6, ASP.NET) |
| **`X-Content-Type-Options`**| `nosniff` | Blocks MIME-type sniffing attacks |
| **`Strict-Transport-Security`**| `max-age=31536000; includeSubDomains` | Enforces mandatory HTTPS communication |
