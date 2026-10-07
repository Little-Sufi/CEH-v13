# 🎯 Module 13: Hacking Web Servers - Exam Scenario Practice Engine

> [!ABSTRACT] 📊 **Interactive Module Scorecard**
>
> - **Target Module**: Module 13: Hacking Web Servers
> - **Total Questions**: 25 Ultra-Detailed, 100% Unique Indirect Scenarios
> - **Exam Difficulty Standard**: Senior CEH v13 (Scenario-Driven Logic & Technical Deduction)
> - **Passing Threshold**: 85% Accuracy (22/25 Correct)
> 
> *Instructions: Evaluate the scenario context below. Select your choice, then expand the **Show Correct Answer & Exam Breakdown** callout to verify your answer and review the deep technical analysis and distractor refutations.*

---

### 🧩 Question 01 | Scenario Challenge

> [!QUESTION] 📌 **Scenario Context**
> An attacker sends a specially crafted HTTP request containing a custom `User-Agent` string (`User-Agent: () { :;}; echo Content-Type: text/plain; echo; /bin/cat /etc/passwd`) to a web server running CGI scripts. The server executes the command and dumps `/etc/passwd`.
>
> What vulnerability was exploited?

#### 🔘 Available Options:

- **A**: Shellshock (GNU Bash RCE)
- **B**: Heartbleed
- **C**: Dirty COW
- **D**: EternalBlue

> [!SUCCESS]- 🔑 **Show Correct Answer & Exam Breakdown**
> **Correct Answer**: **Option A**
>
> #### 💡 Technical Deep Dive:
> Shellshock (CVE-2014-6271) exploits a flaw in GNU Bash where trailing commands attached to function definitions in environment variables are executed when Bash subshells initialize.
>
> #### <ctrl42> Distractor Analysis & Refutations:
>
> - **Option B is incorrect** because Heartbleed is an OpenSSL memory disclosure flaw.
> - **Option C is incorrect** because Dirty COW is a Linux kernel privilege escalation flaw.
> - **Option D is incorrect** because EternalBlue targets SMBv1.

---

### 🧩 Question 02 | Scenario Challenge

> [!QUESTION] 📌 **Scenario Context**
> A penetration tester uses the tool `davtest` against an IIS web server and discovers that HTTP `PUT` and `MOVE` methods are enabled on an unauthenticated virtual directory.
>
> What attack scenario does this configuration directly enable?

#### 🔘 Available Options:

- **A**: Arbitrary Web Shell Upload and Remote Code Execution
- **B**: Cross-Site Request Forgery
- **C**: SQL Injection
- **D**: MAC Address Spoofing

> [!SUCCESS]- 🔑 **Show Correct Answer & Exam Breakdown**
> **Correct Answer**: **Option A**
>
> #### 💡 Technical Deep Dive:
> Insecure WebDAV configurations with enabled `PUT` and `MOVE` methods allow attackers to upload executable scripts (ASPX/PHP webshells) directly into web root directories.
>
> #### 🚫 Distractor Analysis & Refutations:
>
> - **Option B is incorrect** because CSRF targets user browser actions.
> - **Option C is incorrect** because SQLi targets database queries.
> - **Option D is incorrect** because MAC spoofing operates at Layer 2.

---

### 🧩 Question 03 | Scenario Challenge

> [!QUESTION] 📌 **Scenario Context**
> An attacker inputs `http://example.com/download.php?file=../../../../etc/shadow` into a web application, receiving the Linux hashed password file in response.
>
> What vulnerability is present?

#### 🔘 Available Options:

- **A**: Directory Traversal / Path Traversal
- **B**: Cross-Site Scripting
- **C**: Command Injection
- **D**: Buffer Overflow

> [!SUCCESS]- 🔑 **Show Correct Answer & Exam Breakdown**
> **Correct Answer**: **Option A**
>
> #### 💡 Technical Deep Dive:
> Directory Traversal vulnerabilities occur when web applications fail to sanitize dot-dot-slash (`../`) sequences in file path parameters.
>
> #### 🚫 Distractor Analysis & Refutations:
>
> - **Option B is incorrect** because XSS executes scripts in browsers.
> - **Option C is incorrect** because Command Injection executes OS shell commands.
> - **Option D is incorrect** because Buffer Overflow overwrites memory buffers.

---

### 🧩 Question 04 | Scenario Challenge

> [!QUESTION] 📌 **Scenario Context**
> What Apache HTTP configuration directive must a system administrator set to suppress detailed web server version banners (`Server: Apache/2.4.41 (Ubuntu)`) from HTTP response headers?

#### 🔘 Available Options:

- **A**: ServerTokens Prod
- **B**: ServerSignature On
- **C**: Options +Indexes
- **D**: KeepAlive Off

> [!SUCCESS]- 🔑 **Show Correct Answer & Exam Breakdown**
> **Correct Answer**: **Option A**
>
> #### 💡 Technical Deep Dive:
> Setting `ServerTokens Prod` configures Apache to return only `Server: Apache` without revealing detailed minor version numbers or operating system OS identifiers.
>
> #### 🚫 Distractor Analysis & Refutations:
>
> - **Option B is incorrect** because `ServerSignature On` adds footer lines to server-generated pages.
> - **Option C is incorrect** because `Options +Indexes` enables directory listing.
> - **Option D is incorrect** because `KeepAlive Off` disables persistent HTTP connections.

---

### 🧩 Question 05 | Scenario Challenge

> [!QUESTION] 📌 **Scenario Context**
> What PHP configuration setting in `php.ini` hides the `X-Powered-By: PHP/7.4.3` header from HTTP responses?

#### 🔘 Available Options:

- **A**: expose_php = Off
- **B**: display_errors = On
- **C**: allow_url_fopen = On
- **D**: safe_mode = On

> [!SUCCESS]- 🔑 **Show Correct Answer & Exam Breakdown**
> **Correct Answer**: **Option A**
>
> #### 💡 Technical Deep Dive:
> `expose_php = Off` stops PHP from broadcasting its version in the `X-Powered-By` HTTP response header.
>
> #### 🚫 Distractor Analysis & Refutations:
>
> - **Option B is incorrect** because `display_errors = On` shows PHP runtime errors.
> - **Option C is incorrect** because `allow_url_fopen = On` enables remote file includes.
> - **Option D is incorrect** because `safe_mode` is a deprecated legacy feature.

---

### 🧩 Question 06 | Scenario Challenge

> [!QUESTION] 📌 **Scenario Context**
> An attacker injects `%0d%0aSet-Cookie: admin=true` into an input parameter that is reflected directly into an HTTP response header, successfully creating a new cookie on the victim's browser.
>
> What attack vector was executed?

#### 🔘 Available Options:

- **A**: HTTP Response Splitting (CRLF Injection)
- **B**: HTTP Request Smuggling
- **C**: Cross-Site Scripting
- **D**: SQL Injection

> [!SUCCESS]- 🔑 **Show Correct Answer & Exam Breakdown**
> **Correct Answer**: **Option A**
>
> #### 💡 Technical Deep Dive:
> HTTP Response Splitting occurs when CRLF bytes (`%0d%0a`) are injected into response headers, allowing attackers to inject arbitrary headers or split responses.
>
> #### 🚫 Distractor Analysis & Refutations:
>
> - **Option B is incorrect** because HTTP Request Smuggling targets proxy/backend desync.
> - **Option C is incorrect** because XSS executes script in DOM.
> - **Option D is incorrect** because SQLi targets database statements.

---

### 🧩 Question 07 | Scenario Challenge

> [!QUESTION] 📌 **Scenario Context**
> What command-line tool provides interactive WebDAV file management capabilities (allowing security analysts to upload, delete, and inspect files over HTTP)?

#### 🔘 Available Options:

- **A**: Cadaver
- **B**: Nikto
- **C**: Nmap
- **D**: Wireshark

> [!SUCCESS]- 🔑 **Show Correct Answer & Exam Breakdown**
> **Correct Answer**: **Option A**
>
> #### 💡 Technical Deep Dive:
> Cadaver is a command-line WebDAV client for Unix systems supporting upload, download, and file manipulation.
>
> #### 🚫 Distractor Analysis & Refutations:
>
> - **Option B is incorrect** because Nikto is a web scanner.
> - **Option C is incorrect** because Nmap is a network scanner.
> - **Option D is incorrect** because Wireshark is a packet sniffer.

---

### 🧩 Question 08 | Scenario Challenge

> [!QUESTION] 📌 **Scenario Context**
> Which open-source web server scanner automatically tests web servers for over 6,700 dangerous files, outdated server versions, and server misconfigurations?

#### 🔘 Available Options:

- **A**: Nikto
- **B**: Hashcat
- **C**: John the Ripper
- **D**: Aircrack-ng

> [!SUCCESS]- 🔑 **Show Correct Answer & Exam Breakdown**
> **Correct Answer**: **Option A**
>
> #### 💡 Technical Deep Dive:
> Nikto is a comprehensive command-line web server scanner designed to perform automated vulnerability checks.
>
> #### 🚫 Distractor Analysis & Refutations:
>
> - **Option B is incorrect** because Hashcat is a password cracker.
> - **Option C is incorrect** because John the Ripper is a password cracker.
> - **Option D is incorrect** because Aircrack-ng is a wireless cracking tool.

---

### 🧩 Question 09 | Scenario Challenge

> [!QUESTION] 📌 **Scenario Context**
> What Windows IIS process handles incoming web requests for a specific IIS Application Pool?

#### 🔘 Available Options:

- **A**: w3wp.exe
- **B**: svchost.exe
- **C**: lsass.exe
- **D**: explorer.exe

> [!SUCCESS]- 🔑 **Show Correct Answer & Exam Breakdown**
> **Correct Answer**: **Option A**
>
> #### 💡 Technical Deep Dive:
> `w3wp.exe` is the worker process that executes web applications running within a specific IIS Application Pool.
>
> #### 🚫 Distractor Analysis & Refutations:
>
> - **Option B is incorrect** because svchost.exe hosts generic Windows services.
> - **Option C is incorrect** because lsass.exe handles local security authentication.
> - **Option D is incorrect** because explorer.exe is the graphical shell.

---

### 🧩 Question 10 | Scenario Challenge

> [!QUESTION] 📌 **Scenario Context**
> What HTTP method should be disabled on production web servers to prevent attackers from using HTTP trace requests to capture sensitive cookies (including `HttpOnly` cookies)?

#### 🔘 Available Options:

- **A**: TRACE / TRACK
- **B**: GET
- **C**: POST
- **D**: HEAD

> [!SUCCESS]- 🔑 **Show Correct Answer & Exam Breakdown**
> **Correct Answer**: **Option A**
>
> #### 💡 Technical Deep Dive:
> The `TRACE` method echoes back the received request payload, enabling Cross-Site Tracing (XST) attacks that extract sensitive HTTP headers.
>
> #### 🚫 Distractor Analysis & Refutations:
>
> - **Option B is incorrect** because GET retrieves web pages.
> - **Option C is incorrect** because POST submits web data.
> - **Option D is incorrect** because HEAD fetches response headers.

---

### 🧩 Question 11 | Scenario Challenge

> [!QUESTION] 📌 **Scenario Context**
> An attacker uses Nmap with the script flag `nmap -p 80 --script=http-enum 192.168.1.50`. What information does this script discover?

#### 🔘 Available Options:

- **A**: Common administrative web directories, backup files, and vulnerable CGI scripts
- **B**: Wireless WPA2 pre-shared keys
- **C**: Windows NTLM password hashes
- **D**: Router BGP routing tables

> [!SUCCESS]- 🔑 **Show Correct Answer & Exam Breakdown**
> **Correct Answer**: **Option A**
>
> #### 💡 Technical Deep Dive:
> The Nmap `http-enum` script performs directory bruteforcing against web servers to discover hidden paths and management portals.
>
> #### 🚫 Distractor Analysis & Refutations:
>
> - **Option B is incorrect** because `http-enum` does not scan wireless keys.
> - **Option C is incorrect** because `http-enum` does not dump NTLM hashes.
> - **Option D is incorrect** because `http-enum` does not query BGP tables.

---

### 🧩 Question 12 | Scenario Challenge

> [!QUESTION] 📌 **Scenario Context**
> What configuration file in Apache allows directory-level override of security policies, URL rewrites, and access controls?

#### 🔘 Available Options:

- **A**: .htaccess
- **B**: web.config
- **C**: nginx.conf
- **D**: php.ini

> [!SUCCESS]- 🔑 **Show Correct Answer & Exam Breakdown**
> **Correct Answer**: **Option A**
>
> #### 💡 Technical Deep Dive:
> `.htaccess` files provide directory-level configuration overrides on Apache web servers.
>
> #### 🚫 Distractor Analysis & Refutations:
>
> - **Option B is incorrect** because `web.config` is used by Microsoft IIS.
> - **Option C is incorrect** because `nginx.conf` is used by Nginx.
> - **Option D is incorrect** because `php.ini` configures PHP runtime.

---

### 🧩 Question 13 | Scenario Challenge

> [!QUESTION] 📌 **Scenario Context**
> What configuration file in Microsoft IIS contains application settings, authentication rules, and HTTP module definitions?

#### 🔘 Available Options:

- **A**: web.config
- **B**: .htaccess
- **C**: httpd.conf
- **D**: my.cnf

> [!SUCCESS]- 🔑 **Show Correct Answer & Exam Breakdown**
> **Correct Answer**: **Option A**
>
> #### 💡 Technical Deep Dive:
> `web.config` is the XML configuration file used by Microsoft IIS to define website settings and module handlers.
>
> #### 🚫 Distractor Analysis & Refutations:
>
> - **Option B is incorrect** because `.htaccess` is used by Apache.
> - **Option C is incorrect** because `httpd.conf` is used by Apache.
> - **Option D is incorrect** because `my.cnf` configures MySQL.

---

### 🧩 Question 14 | Scenario Challenge

> [!QUESTION] 📌 **Scenario Context**
> What vulnerability arises when a front-end load balancer and a back-end web server interpret `Content-Length` and `Transfer-Encoding` headers differently, allowing attackers to tamper with request boundaries?

#### 🔘 Available Options:

- **A**: HTTP Request Smuggling
- **B**: HTTP Response Splitting
- **C**: Cross-Site Scripting
- **D**: SQL Injection

> [!SUCCESS]- 🔑 **Show Correct Answer & Exam Breakdown**
> **Correct Answer**: **Option A**
>
> #### 💡 Technical Deep Dive:
> HTTP Request Smuggling exploits discrepancies between front-end and back-end HTTP parser implementations (CL.TE or TE.CL).
>
> #### 🚫 Distractor Analysis & Refutations:
>
> - **Option B is incorrect** because HTTP Response Splitting injects CRLF into responses.
> - **Option C is incorrect** because XSS executes scripts in browsers.
> - **Option D is incorrect** because SQLi manipulates DB queries.

---

### 🧩 Question 15 | Scenario Challenge

> [!QUESTION] 📌 **Scenario Context**
> What command banner grabbing syntax (`nc -vv 192.168.1.50 80`) allows a security analyst to manually query a web server's HTTP header response?

#### 🔘 Available Options:

- **A**: HEAD / HTTP/1.1
- **B**: GET / EVERYTHING
- **C**: SCAN / HTTP/2.0
- **D**: CONNECT / PORT80

> [!SUCCESS]- 🔑 **Show Correct Answer & Exam Breakdown**
> **Correct Answer**: **Option A**
>
> #### 💡 Technical Deep Dive:
> Sending `HEAD / HTTP/1.1` returns HTTP response headers (including Server banner) without downloading the full message body.
>
> #### 🚫 Distractor Analysis & Refutations:
>
> - **Option B is incorrect** because `GET / EVERYTHING` is invalid HTTP syntax.
> - **Option C is incorrect** because `SCAN` is not an HTTP method.
> - **Option D is incorrect** because `CONNECT` is used for proxy tunneling.

---

### 🧩 Question 16 | Scenario Challenge

> [!QUESTION] 📌 **Scenario Context**
> Which dedicated scanner specializes in enumerating WordPress plugins, themes, timthumb scripts, and weak user passwords?

#### 🔘 Available Options:

- **A**: WPScan
- **B**: Nikto
- **C**: Davtest
- **D**: SQLmap

> [!SUCCESS]- 🔑 **Show Correct Answer & Exam Breakdown**
> **Correct Answer**: **Option A**
>
> #### 💡 Technical Deep Dive:
> WPScan is a security scanner crafted specifically for auditing WordPress installations.
>
> #### 🚫 Distractor Analysis & Refutations:
>
> - **Option B is incorrect** because Nikto is a generic web server scanner.
> - **Option C is incorrect** because Davtest tests WebDAV permissions.
> - **Option D is incorrect** because SQLmap automates SQL injection.

---

### 🧩 Question 17 | Scenario Challenge

> [!QUESTION] 📌 **Scenario Context**
> Why should a web server's default installation files (e.g., Apache manual pages, sample CGI scripts, IIS welcome pages) be removed immediately upon deployment?

#### 🔘 Available Options:

- **A**: Default files disclose web server software versions and may contain known vulnerable sample scripts
- **B**: Default files slow down CPU processing
- **C**: Default files corrupt SSL certificates
- **D**: Default files disable firewall rules

> [!SUCCESS]- 🔑 **Show Correct Answer & Exam Breakdown**
> **Correct Answer**: **Option A**
>
> #### 💡 Technical Deep Dive:
> Default files provide attackers with precise version identification and known attack paths via unpatched sample CGIs.
>
> #### 🚫 Distractor Analysis & Refutations:
>
> - **Option B is incorrect** because default files have negligible CPU overhead.
> - **Option C is incorrect** because default files do not affect SSL certs.
> - **Option D is incorrect** because default files do not alter firewalls.

---

### 🧩 Question 18 | Scenario Challenge

> [!QUESTION] 📌 **Scenario Context**
> What principle of security architecture mandates that web server processes (`httpd`, `nginx`, `w3wp.exe`) run under isolated accounts with minimum required operating system permissions?

#### 🔘 Available Options:

- **A**: Principle of Least Privilege
- **B**: Defense in Depth
- **C**: Separation of Duties
- **D**: Fail-Safe Defaults

> [!SUCCESS]- 🔑 **Show Correct Answer & Exam Breakdown**
> **Correct Answer**: **Option A**
>
> #### 💡 Technical Deep Dive:
> The Principle of Least Privilege ensures that if a web server process is compromised, the attacker cannot access underlying OS files.
>
> #### 🚫 Distractor Analysis & Refutations:
>
> - **Option B is incorrect** because Defense in Depth uses layered controls.
> - **Option C is incorrect** because Separation of Duties divides administrative tasks.
> - **Option D is incorrect** because Fail-Safe Defaults default to secure states on failure.

---

### 🧩 Question 19 | Scenario Challenge

> [!QUESTION] 📌 **Scenario Context**
> An attacker uses a web application vulnerability to upload a file named `shell.php.jpeg` to an Apache server, which executes it as a PHP script due to double extension handling rules.
>
> What configuration flaw allowed this execution?

#### 🔘 Available Options:

- **A**: Apache MIME-type misconfiguration / Double Extension execution
- **B**: SQL Injection
- **C**: Heartbleed
- **D**: Shellshock

> [!SUCCESS]- 🔑 **Show Correct Answer & Exam Breakdown**
> **Correct Answer**: **Option A**
>
> #### 💡 Technical Deep Dive:
> Apache servers misconfigured with `AddHandler application/x-httpd-php .php` execute files containing `.php` anywhere in the extension list.
>
> #### 🚫 Distractor Analysis & Refutations:
>
> - **Option B is incorrect** because SQLi manipulates SQL queries.
> - **Option C is incorrect** because Heartbleed is an OpenSSL bug.
> - **Option D is incorrect** because Shellshock targets Bash environment variables.

---

### 🧩 Question 20 | Scenario Challenge

> [!QUESTION] 📌 **Scenario Context**
> What defensive web server setting prevents users from viewing directory file indices when accessing an unindexed directory URL (`http://example.com/images/`)?

#### 🔘 Available Options:

- **A**: Disabling Directory Browsing (`Options -Indexes` in Apache)
- **B**: Enabling HTTP Trace
- **C**: Enabling WebDAV
- **D**: Setting ServerTokens Full

> [!SUCCESS]- 🔑 **Show Correct Answer & Exam Breakdown**
> **Correct Answer**: **Option A**
>
> #### 💡 Technical Deep Dive:
> Disabling directory browsing ensures web servers return `403 Forbidden` instead of listing directory contents.
>
> #### 🚫 Distractor Analysis & Refutations:
>
> - **Option B is incorrect** because HTTP Trace enables XST attacks.
> - **Option C is incorrect** because WebDAV allows file modification.
> - **Option D is incorrect** because ServerTokens Full reveals server details.

---

### 🧩 Question 21 | Scenario Challenge

> [!QUESTION] 📌 **Scenario Context**
> What open-source vulnerability scanner is designed to test WebDAV implementations by automatically attempting to upload test files across various extensions?

#### 🔘 Available Options:

- **A**: Davtest
- **B**: Wireshark
- **C**: John the Ripper
- **D**: Aircrack-ng

> [!SUCCESS]- 🔑 **Show Correct Answer & Exam Breakdown**
> **Correct Answer**: **Option A**
>
> #### 💡 Technical Deep Dive:
> Davtest checks WebDAV-enabled servers by attempting file uploads and reporting execution permissions.
>
> #### 🚫 Distractor Analysis & Refutations:
>
> - **Option B is incorrect** because Wireshark is a packet analyzer.
> - **Option C is incorrect** because John the Ripper cracks passwords.
> - **Option D is incorrect** because Aircrack-ng audits Wi-Fi.

---

### 🧩 Question 22 | Scenario Challenge

> [!QUESTION] 📌 **Scenario Context**
> Which HTTP security header instructs web browsers to block pages from loading inside `<frame>`, `<iframe>`, or `<object>` elements, protecting websites from Clickjacking attacks?

#### 🔘 Available Options:

- **A**: X-Frame-Options: DENY / SAMEORIGIN
- **B**: Strict-Transport-Security
- **C**: X-Content-Type-Options: nosniff
- **D**: Server: Apache

> [!SUCCESS]- 🔑 **Show Correct Answer & Exam Breakdown**
> **Correct Answer**: **Option A**
>
> #### 💡 Technical Deep Dive:
> `X-Frame-Options` prevents clickjacking by restricting framing permissions.
>
> #### 🚫 Distractor Analysis & Refutations:
>
> - **Option B is incorrect** because HSTS enforces HTTPS.
> - **Option C is incorrect** because `nosniff` prevents MIME-sniffing.
> - **Option D is incorrect** because `Server` header shows version details.

---

### 🧩 Question 23 | Scenario Challenge

> [!QUESTION] 📌 **Scenario Context**
> An attacker uses a web proxy to alter an HTTP GET parameter `http://store.com/item.php?price=100` to `price=1` before transmitting the request to the web server.
>
> What attack was executed?

#### 🔘 Available Options:

- **A**: Parameter Tampering
- **B**: Directory Traversal
- **C**: Shellshock
- **D**: SQL Injection

> [!SUCCESS]- 🔑 **Show Correct Answer & Exam Breakdown**
> **Correct Answer**: **Option A**
>
> #### 💡 Technical Deep Dive:
> Parameter Tampering involves modifying request parameters (URL query, form fields, cookies) to bypass business logic.
>
> #### 🚫 Distractor Analysis & Refutations:
>
> - **Option B is incorrect** because Directory Traversal accesses files.
> - **Option C is incorrect** because Shellshock executes Bash commands.
> - **Option D is incorrect** because SQLi alters database queries.

---

### 🧩 Question 24 | Scenario Challenge

> [!QUESTION] 📌 **Scenario Context**
> What vulnerability in IIS 6.0 enabled unauthenticated Remote Code Execution via a buffer overflow in the WebDAV `PROPFIND` header handling routine (CVE-2017-7269)?

#### 🔘 Available Options:

- **A**: ScStoragePathFromUrl WebDAV Buffer Overflow
- **B**: Shellshock
- **C**: Heartbleed
- **D**: EternalBlue

> [!SUCCESS]- 🔑 **Show Correct Answer & Exam Breakdown**
> **Correct Answer**: **Option A**
>
> #### 💡 Technical Deep Dive:
> CVE-2017-7269 is a famous buffer overflow in IIS 6.0 WebDAV service processing `PROPFIND` requests.
>
> #### 🚫 Distractor Analysis & Refutations:
>
> - **Option B is incorrect** because Shellshock targets Bash.
> - **Option C is incorrect** because Heartbleed targets OpenSSL.
> - **Option D is incorrect** because EternalBlue targets SMBv1.

---

### 🧩 Question 25 | Scenario Challenge

> [!QUESTION] 📌 **Scenario Context**
> What is the primary objective of web server footprinting and banner grabbing during the initial phase of an ethical hacking assessment?

#### 🔘 Available Options:

- **A**: To identify the web server software type, version, enabled modules, and OS platform to search for known exploits
- **B**: To crack user database passwords
- **C**: To format web server storage drives
- **D**: To launch a distributed SYN flood attack

> [!SUCCESS]- 🔑 **Show Correct Answer & Exam Breakdown**
> **Correct Answer**: **Option A**
>
> #### 💡 Technical Deep Dive:
> Banner grabbing gathers specific software and version information to match against known CVE exploit databases.
>
> #### 🚫 Distractor Analysis & Refutations:
>
> - **Option B is incorrect** because banner grabbing does not crack databases.
> - **Option C is incorrect** because banner grabbing is non-destructive reconnaissance.
> - **Option D is incorrect** because SYN floods are DoS attacks.
