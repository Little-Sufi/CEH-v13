# 05. Course Detailed Notes — Hacking Web Servers

> [!ABSTRACT] 🏛️ **Comprehensive Syllabus Notes & Technical Reference**
> Direct technical extraction from official CEH v13 Syllabus (Module 13). Covers IIS Application Pool Isolation, HTTP Request Smuggling Mechanics, and Virtual Host Bruteforcing.

---

## 📌 1. HTTP Request Smuggling & IIS Isolation

### 1.1 HTTP Request Smuggling Mechanics (CL.TE vs TE.CL)
Request Smuggling desynchronizes front-end reverse proxy servers and backend web servers due to conflicting handling of dual `Content-Length` and `Transfer-Encoding` headers.
- **CL.TE Desync**: Front-end uses `Content-Length`, Back-end uses `Transfer-Encoding`.
- **TE.CL Desync**: Front-end uses `Transfer-Encoding`, Back-end uses `Content-Length`.

> [!INFO] 📋 **Comprehensive Web Server Architecture Comparison Matrix**

| Web Server Software | Default Web Root Path | Main Configuration File | Process Isolation Model |
| :--- | :--- | :--- | :--- |
| **Apache HTTP Server**| `/var/www/html/` | `/etc/apache2/apache2.conf` | Multi-Processing Modules (MPM) |
| **Microsoft IIS** | `C:\inetpub\wwwroot\` | `C:\Windows\System32\inetsrv\config\applicationHost.config` | IIS Application Pools (`w3wp.exe`) |
| **Nginx** | `/usr/share/nginx/html/` | `/etc/nginx/nginx.conf` | Asynchronous Master / Worker Processes |
