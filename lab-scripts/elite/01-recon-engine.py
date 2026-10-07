#!/usr/bin/env python3
"""
╔══════════════════════════════════════════════════════════════════════════════╗
║  ELITE RECON ENGINE v1.0 — CEH v13 Lab Arsenal                            ║
║  Full-spectrum target reconnaissance & attack surface mapping              ║
║  LAB-ONLY — AUTHORIZED TESTING ONLY                                       ║
╚══════════════════════════════════════════════════════════════════════════════╝
"""
import sys, os, socket, ssl, struct, json, re, time, argparse, hashlib
import concurrent.futures
from datetime import datetime
from urllib.parse import urlparse
try:
    import requests
    HAS_REQUESTS = True
except ImportError:
    HAS_REQUESTS = False

# ═══════════════════════════════════════════════════════════════════════════════
# CONFIGURATION
# ═══════════════════════════════════════════════════════════════════════════════
COMMON_PORTS = [21,22,23,25,53,80,110,111,135,139,143,443,445,993,995,
                1433,1521,3306,3389,5432,5900,5985,6379,8000,8080,8443,
                8888,9090,9200,9300,27017,27018]
TOP_1000 = list(range(1,1024)) + [1080,1433,1521,2049,2121,3306,3389,
           4443,5432,5900,5985,6379,7001,8000,8080,8443,8888,9090,9200,27017]
FULL_RANGE = range(1, 65536)

BANNER_PROBES = {
    b"": 5,  # Null probe — many services send banner on connect
    b"HEAD / HTTP/1.1\r\nHost: {host}\r\n\r\n": 3,
    b"EHLO recon\r\n": 2,
    b"\x00\x00\x00\xa4\xff\x53\x4d\x42": 2,  # SMB negotiate
}

TECH_SIGNATURES = {
    "Apache": r"Apache[/ ](\d+\.\d+\.\d+)",
    "Nginx": r"nginx[/ ](\d+\.\d+\.\d+)",
    "IIS": r"Microsoft-IIS[/ ](\d+\.\d+)",
    "OpenSSH": r"OpenSSH[_/ ](\d+\.\d+)",
    "MySQL": r"(\d+\.\d+\.\d+).*?mysql",
    "PostgreSQL": r"PostgreSQL (\d+\.\d+)",
    "Redis": r"redis_version:(\d+\.\d+\.\d+)",
    "MongoDB": r"MongoDB (\d+\.\d+)",
    "Tomcat": r"Apache Tomcat[/ ](\d+\.\d+)",
    "PHP": r"PHP[/ ](\d+\.\d+\.\d+)",
    "WordPress": r"WordPress[/ ](\d+\.\d+)",
    "Joomla": r"Joomla",
    "Drupal": r"Drupal",
    "ASP.NET": r"X-AspNet-Version: ([\d.]+)",
    "Express": r"Express",
    "Flask": r"Werkzeug",
    "Django": r"djangoproject|csrfmiddlewaretoken",
    "Laravel": r"laravel_session",
    "Spring": r"X-Application-Context",
    "vsFTPd": r"vsFTPd (\d+\.\d+\.\d+)",
    "ProFTPD": r"ProFTPD (\d+\.\d+\.\d+)",
    "Exim": r"Exim (\d+\.\d+)",
    "Postfix": r"Postfix",
    "Dovecot": r"Dovecot",
}

SUBDOMAIN_WORDLIST = [
    "www","mail","ftp","admin","blog","dev","staging","api","app","portal",
    "test","beta","demo","support","help","shop","store","cdn","static",
    "media","assets","img","images","upload","uploads","files","backup",
    "db","database","sql","mysql","postgres","redis","elastic","kibana",
    "jenkins","gitlab","git","svn","ci","cd","docker","k8s","kubernetes",
    "monitor","grafana","prometheus","nagios","zabbix","vpn","remote",
    "internal","intranet","extranet","webmail","owa","exchange","sso",
    "auth","login","signin","signup","register","dashboard","panel",
    "control","manage","manager","cms","wp","joomla","drupal","magento",
    "phpmyadmin","adminer","cpanel","whm","plesk","webmin","tomcat",
    "proxy","gateway","lb","loadbalancer","ns1","ns2","mx","smtp","pop",
    "imap","calendar","wiki","docs","jira","confluence","slack","teams",
    "s3","storage","vault","secrets","config","status","health",
]

# ═══════════════════════════════════════════════════════════════════════════════
# SCANNER ENGINE
# ═══════════════════════════════════════════════════════════════════════════════

class ReconEngine:
    def __init__(self, target, args):
        self.target = target
        self.args = args
        self.results = {
            "target": target, "scan_time": datetime.now().isoformat(),
            "open_ports": [], "services": {}, "technologies": [],
            "subdomains": [], "ssl_info": {}, "http_headers": {},
            "vulnerabilities": [], "dns_records": {}
        }
        self.timeout = args.timeout

    def c(self, color, text):
        """Colored output"""
        colors = {"R":"\033[91m","G":"\033[92m","Y":"\033[93m","B":"\033[94m",
                  "M":"\033[95m","C":"\033[96m","W":"\033[97m","0":"\033[0m"}
        if not self.args.no_color:
            return f"{colors.get(color,'')}{text}{colors['0']}"
        return text

    # ─── Phase 1: Port Scanning ──────────────────────────────────────────────
    def scan_port(self, port):
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(self.timeout)
            result = sock.connect_ex((self.target, port))
            if result == 0:
                # Grab banner
                banner = ""
                try:
                    sock.settimeout(2)
                    for probe, wait in BANNER_PROBES.items():
                        try:
                            if probe:
                                sock.send(probe.replace(b"{host}", self.target.encode()))
                            sock.settimeout(wait)
                            data = sock.recv(4096)
                            if data:
                                banner = data.decode("utf-8", errors="replace").strip()[:500]
                                break
                        except (socket.timeout, ConnectionResetError, BrokenPipeError):
                            continue
                except Exception:
                    pass
                sock.close()
                return (port, banner)
            sock.close()
        except (socket.timeout, ConnectionRefusedError, OSError):
            pass
        return None

    def phase_port_scan(self):
        print(f"\n{self.c('C','[Phase 1]')} Port Scanning — {self.target}")
        print("─" * 70)

        if self.args.ports == "full":
            ports = list(FULL_RANGE)
            print(f"  Scanning all 65535 ports...")
        elif self.args.ports == "top1000":
            ports = TOP_1000
        else:
            ports = COMMON_PORTS

        found = []
        total = len(ports)
        done = 0
        start = time.time()

        with concurrent.futures.ThreadPoolExecutor(max_workers=self.args.threads) as executor:
            futures = {executor.submit(self.scan_port, p): p for p in ports}
            for future in concurrent.futures.as_completed(futures):
                done += 1
                if done % 500 == 0 or done == total:
                    elapsed = time.time() - start
                    rate = done / elapsed if elapsed > 0 else 0
                    sys.stdout.write(f"\r  Progress: {done}/{total} ({rate:.0f} ports/s)")
                    sys.stdout.flush()
                result = future.result()
                if result:
                    found.append(result)

        print(f"\r  Scanned {total} ports in {time.time()-start:.1f}s" + " " * 30)

        # Sort and display
        found.sort(key=lambda x: x[0])
        service_names = {
            21:"FTP",22:"SSH",23:"Telnet",25:"SMTP",53:"DNS",80:"HTTP",
            110:"POP3",111:"RPCBind",135:"MSRPC",139:"NetBIOS",143:"IMAP",
            443:"HTTPS",445:"SMB",993:"IMAPS",995:"POP3S",1433:"MSSQL",
            1521:"Oracle",3306:"MySQL",3389:"RDP",5432:"PostgreSQL",
            5900:"VNC",5985:"WinRM",6379:"Redis",8080:"HTTP-Proxy",
            8443:"HTTPS-Alt",9090:"WebConsole",9200:"Elasticsearch",
            27017:"MongoDB",
        }

        if found:
            print(f"\n  {self.c('G',f'✓ {len(found)} open ports found:')}")
            print(f"  {'PORT':>7}  {'SERVICE':12} {'BANNER'}")
            print(f"  {'─'*7}  {'─'*12} {'─'*45}")
            for port, banner in found:
                svc = service_names.get(port, "unknown")
                # Detect service from banner
                for tech, pattern in TECH_SIGNATURES.items():
                    if re.search(pattern, banner, re.IGNORECASE):
                        svc = tech
                        break
                banner_short = banner.replace("\n"," ").replace("\r","")[:45]
                print(f"  {port:>7}  {svc:12} {banner_short}")
                self.results["open_ports"].append(port)
                self.results["services"][str(port)] = {"service": svc, "banner": banner[:200]}
        else:
            print(f"  {self.c('R','✗ No open ports found')}")
        return found

    # ─── Phase 2: Technology Detection ───────────────────────────────────────
    def phase_tech_detection(self):
        if 80 not in self.results["open_ports"] and 443 not in self.results["open_ports"] and 8080 not in self.results["open_ports"]:
            return
        if not HAS_REQUESTS:
            print(f"\n{self.c('Y','[!]')} requests library not installed — skipping HTTP analysis")
            return

        print(f"\n{self.c('C','[Phase 2]')} Technology Detection")
        print("─" * 70)

        schemes = []
        if 443 in self.results["open_ports"] or 8443 in self.results["open_ports"]:
            schemes.append("https")
        if 80 in self.results["open_ports"] or 8080 in self.results["open_ports"]:
            schemes.append("http")

        for scheme in schemes:
            port = 443 if scheme == "https" else 80
            if port not in self.results["open_ports"]:
                port = 8443 if scheme == "https" else 8080
            url = f"{scheme}://{self.target}:{port}/"
            try:
                resp = requests.get(url, timeout=self.timeout, verify=False,
                                    allow_redirects=True,
                                    headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"})

                # Headers analysis
                print(f"\n  {self.c('B','HTTP Headers')} ({url}):")
                security_headers = {
                    "X-Frame-Options": "Clickjacking protection",
                    "X-Content-Type-Options": "MIME sniffing protection",
                    "X-XSS-Protection": "XSS filter",
                    "Strict-Transport-Security": "HSTS",
                    "Content-Security-Policy": "CSP",
                    "Referrer-Policy": "Referrer control",
                    "Permissions-Policy": "Feature control",
                }
                for header, desc in security_headers.items():
                    val = resp.headers.get(header)
                    if val:
                        print(f"    {self.c('G','✓')} {header}: {val[:60]}")
                    else:
                        print(f"    {self.c('R','✗')} {header} — MISSING ({desc})")
                        self.results["vulnerabilities"].append({
                            "type": "Missing Security Header",
                            "detail": f"{header} not set — {desc}",
                            "severity": "LOW", "url": url
                        })

                self.results["http_headers"][url] = dict(resp.headers)

                # Server header
                server = resp.headers.get("Server", "")
                powered = resp.headers.get("X-Powered-By", "")
                if server:
                    print(f"\n  Server: {self.c('Y',server)}")
                    self.results["technologies"].append({"name": server, "source": "Server header"})
                if powered:
                    print(f"  X-Powered-By: {self.c('Y',powered)}")
                    self.results["technologies"].append({"name": powered, "source": "X-Powered-By"})
                    self.results["vulnerabilities"].append({
                        "type": "Information Disclosure",
                        "detail": f"X-Powered-By header reveals: {powered}",
                        "severity": "LOW", "url": url
                    })

                # Body technology detection
                body = resp.text[:50000]
                print(f"\n  {self.c('B','Technology Fingerprints')}:")
                for tech, pattern in TECH_SIGNATURES.items():
                    match = re.search(pattern, body + server + powered, re.IGNORECASE)
                    if match:
                        version = match.group(1) if match.lastindex else ""
                        print(f"    {self.c('G','→')} {tech} {version}")
                        self.results["technologies"].append({"name": tech, "version": version, "source": "fingerprint"})

                # Cookie analysis
                cookies = resp.cookies
                if cookies:
                    print(f"\n  {self.c('B','Cookies')}:")
                    for c in cookies:
                        flags = []
                        if c.secure: flags.append("Secure")
                        if "httponly" in str(c._rest).lower(): flags.append("HttpOnly")
                        if not c.secure:
                            self.results["vulnerabilities"].append({
                                "type": "Insecure Cookie",
                                "detail": f"Cookie '{c.name}' missing Secure flag",
                                "severity": "MEDIUM", "url": url
                            })
                        print(f"    {c.name} = {str(c.value)[:30]}... [{', '.join(flags) or 'NO FLAGS'}]")

            except requests.exceptions.SSLError:
                self.results["vulnerabilities"].append({
                    "type": "SSL/TLS Issue", "detail": "SSL certificate error",
                    "severity": "MEDIUM", "url": url
                })
            except Exception as e:
                print(f"  {self.c('R','✗')} Error: {e}")

    # ─── Phase 3: SSL/TLS Analysis ──────────────────────────────────────────
    def phase_ssl_analysis(self):
        if 443 not in self.results["open_ports"] and 8443 not in self.results["open_ports"]:
            return

        print(f"\n{self.c('C','[Phase 3]')} SSL/TLS Certificate Analysis")
        print("─" * 70)

        port = 443 if 443 in self.results["open_ports"] else 8443
        try:
            ctx = ssl.create_default_context()
            ctx.check_hostname = False
            ctx.verify_mode = ssl.CERT_NONE
            with socket.create_connection((self.target, port), timeout=self.timeout) as sock:
                with ctx.wrap_socket(sock, server_hostname=self.target) as ssock:
                    cert = ssock.getpeercert(binary_form=True)
                    # Decode with ssl
                    cert_info = ssl.DER_cert_to_PEM_cert(cert)
                    cipher = ssock.cipher()
                    version = ssock.version()

                    print(f"  Protocol:  {self.c('G',version) if version != 'TLSv1' else self.c('R',version)}")
                    print(f"  Cipher:    {cipher[0]} ({cipher[2]} bits)")

                    if cipher[2] < 128:
                        self.results["vulnerabilities"].append({
                            "type": "Weak Cipher", "detail": f"{cipher[0]} uses only {cipher[2]} bits",
                            "severity": "HIGH"
                        })
                        print(f"    {self.c('R','⚠ WEAK CIPHER — less than 128 bits')}")

                    # Try to get parsed cert
                    try:
                        with ctx.wrap_socket(socket.create_connection((self.target, port), timeout=self.timeout),
                                            server_hostname=self.target) as ssock2:
                            pass
                    except ssl.SSLCertVerificationError as e:
                        print(f"  Cert:      {self.c('R','INVALID')} — {str(e)[:60]}")
                        self.results["vulnerabilities"].append({
                            "type": "Invalid SSL Certificate",
                            "detail": str(e)[:100], "severity": "MEDIUM"
                        })
                    except Exception:
                        pass

                    self.results["ssl_info"] = {
                        "protocol": version, "cipher": cipher[0],
                        "bits": cipher[2], "cert_hash": hashlib.sha256(cert).hexdigest()[:16]
                    }
        except Exception as e:
            print(f"  {self.c('R','✗')} SSL analysis failed: {e}")

    # ─── Phase 4: Subdomain Enumeration ──────────────────────────────────────
    def phase_subdomain_enum(self):
        if not self.args.subdomains:
            return

        print(f"\n{self.c('C','[Phase 4]')} Subdomain Enumeration")
        print("─" * 70)

        base_domain = self.target
        found = []

        def check_subdomain(sub):
            fqdn = f"{sub}.{base_domain}"
            try:
                answers = socket.getaddrinfo(fqdn, None, socket.AF_INET)
                ips = list(set(a[4][0] for a in answers))
                return (fqdn, ips)
            except (socket.gaierror, socket.herror):
                return None

        with concurrent.futures.ThreadPoolExecutor(max_workers=self.args.threads) as executor:
            futures = {executor.submit(check_subdomain, s): s for s in SUBDOMAIN_WORDLIST}
            for future in concurrent.futures.as_completed(futures):
                result = future.result()
                if result:
                    found.append(result)

        if found:
            found.sort(key=lambda x: x[0])
            print(f"  {self.c('G',f'✓ {len(found)} subdomains found:')}")
            for fqdn, ips in found:
                print(f"    {fqdn:40s} → {', '.join(ips)}")
                self.results["subdomains"].append({"fqdn": fqdn, "ips": ips})
        else:
            print(f"  {self.c('Y','ℹ No subdomains found (try a larger wordlist)')}")

    # ─── Phase 5: Quick Vulnerability Checks ─────────────────────────────────
    def phase_vuln_checks(self):
        if not HAS_REQUESTS:
            return

        print(f"\n{self.c('C','[Phase 5]')} Quick Vulnerability Checks")
        print("─" * 70)

        scheme = "https" if 443 in self.results["open_ports"] else "http"
        port = 443 if scheme == "https" else 80
        if port not in self.results["open_ports"]:
            port = 8443 if scheme == "https" else 8080
        base = f"{scheme}://{self.target}:{port}"

        checks = [
            # (path, description, match_pattern, severity)
            ("/.env", "Environment file exposure", r"(DB_PASSWORD|APP_KEY|SECRET)", "CRITICAL"),
            ("/.git/config", "Git repository exposure", r"\[core\]", "CRITICAL"),
            ("/robots.txt", "Robots.txt recon", r"(Disallow|Allow)", "INFO"),
            ("/.htaccess", ".htaccess exposure", r"(RewriteRule|AuthType)", "HIGH"),
            ("/wp-login.php", "WordPress login", r"(wp-login|wordpress)", "INFO"),
            ("/phpmyadmin/", "phpMyAdmin exposed", r"(phpMyAdmin|pma)", "HIGH"),
            ("/server-status", "Apache server-status", r"(Server Version|Current Time)", "MEDIUM"),
            ("/server-info", "Apache server-info", r"(Server Settings|Module)", "MEDIUM"),
            ("/actuator/health", "Spring Boot Actuator", r'"status"', "MEDIUM"),
            ("/api/swagger.json", "Swagger API docs", r'"swagger"|"openapi"', "LOW"),
            ("/graphql", "GraphQL endpoint", r'"errors"|"data"', "LOW"),
            ("/.well-known/security.txt", "Security policy", r"Contact:", "INFO"),
            ("/elmah.axd", "ELMAH error log", r"Error Log", "HIGH"),
            ("/trace", "Spring trace endpoint", r'"timestamp"', "HIGH"),
            ("/debug/vars", "Go debug vars", r'"cmdline"', "HIGH"),
            ("/backup.sql", "SQL backup exposed", r"(CREATE TABLE|INSERT INTO)", "CRITICAL"),
            ("/backup.zip", "Backup archive", None, "HIGH"),
            ("/config.php.bak", "PHP config backup", r"(password|database)", "CRITICAL"),
        ]

        for path, desc, pattern, severity in checks:
            try:
                resp = requests.get(f"{base}{path}", timeout=3, verify=False,
                                    headers={"User-Agent": "Mozilla/5.0"},
                                    allow_redirects=False)
                if resp.status_code == 200:
                    matched = False
                    if pattern:
                        matched = bool(re.search(pattern, resp.text[:5000], re.IGNORECASE))
                    else:
                        matched = len(resp.content) > 100  # Non-empty response

                    if matched:
                        sev_color = {"CRITICAL":"R","HIGH":"R","MEDIUM":"Y","LOW":"B","INFO":"W"}
                        print(f"  {self.c(sev_color.get(severity,'W'),f'[{severity}]')} {desc}: {path}")
                        self.results["vulnerabilities"].append({
                            "type": desc, "detail": f"{base}{path} accessible",
                            "severity": severity, "url": f"{base}{path}",
                            "status_code": resp.status_code
                        })
            except Exception:
                pass

        vuln_count = len(self.results["vulnerabilities"])
        print(f"\n  Total findings: {vuln_count}")

    # ─── Run Full Scan ───────────────────────────────────────────────────────
    def run(self):
        print(f"""
{'='*70}
  ⚡ ELITE RECON ENGINE v1.0
  Target:  {self.target}
  Threads: {self.args.threads}
  Timeout: {self.timeout}s
  Ports:   {self.args.ports}
{'='*70}""")

        self.phase_port_scan()
        self.phase_tech_detection()
        self.phase_ssl_analysis()
        self.phase_subdomain_enum()
        self.phase_vuln_checks()

        # ─── Final Report ────────────────────────────────────────────────────
        print(f"\n{'='*70}")
        print(f"  📊 SCAN COMPLETE")
        print(f"{'='*70}")
        print(f"  Open ports:     {len(self.results['open_ports'])}")
        print(f"  Technologies:   {len(self.results['technologies'])}")
        print(f"  Subdomains:     {len(self.results['subdomains'])}")
        print(f"  Vulnerabilities: {len(self.results['vulnerabilities'])}")

        # Vuln severity breakdown
        sevs = {}
        for v in self.results["vulnerabilities"]:
            sevs[v["severity"]] = sevs.get(v["severity"], 0) + 1
        for s in ["CRITICAL", "HIGH", "MEDIUM", "LOW", "INFO"]:
            if s in sevs:
                c = {"CRITICAL":"R","HIGH":"R","MEDIUM":"Y","LOW":"B","INFO":"W"}[s]
                print(f"    {self.c(c, f'{s}: {sevs[s]}')}")

        # Save JSON report
        report_file = self.args.output or f"recon-{self.target}-{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        with open(report_file, "w") as f:
            json.dump(self.results, f, indent=2, default=str)
        print(f"\n  📄 Report: {report_file}")


# ═══════════════════════════════════════════════════════════════════════════════
# CLI
# ═══════════════════════════════════════════════════════════════════════════════
if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Elite Recon Engine — Full-spectrum target reconnaissance",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s 192.168.1.1                       # Quick scan (common ports)
  %(prog)s 192.168.1.1 -p top1000 -t 200     # Top 1000 ports, 200 threads
  %(prog)s 192.168.1.1 -p full -t 500        # Full 65535 port scan
  %(prog)s target.lab -s -t 100              # Include subdomain enumeration
  %(prog)s 10.0.0.1 -o report.json           # Save to specific file
        """)
    parser.add_argument("target", help="Target IP or hostname")
    parser.add_argument("-p", "--ports", choices=["common","top1000","full"], default="common", help="Port range (default: common)")
    parser.add_argument("-t", "--threads", type=int, default=100, help="Thread count (default: 100)")
    parser.add_argument("-T", "--timeout", type=float, default=2.0, help="Connection timeout in seconds (default: 2)")
    parser.add_argument("-s", "--subdomains", action="store_true", help="Enable subdomain enumeration")
    parser.add_argument("-o", "--output", help="Output JSON file path")
    parser.add_argument("--no-color", action="store_true", help="Disable colored output")

    args = parser.parse_args()

    # Lab validation
    target = args.target
    try:
        ip = socket.gethostbyname(target)
    except socket.gaierror:
        ip = target

    engine = ReconEngine(target, args)
    engine.run()
