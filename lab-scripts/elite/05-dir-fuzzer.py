#!/usr/bin/env python3
"""
╔══════════════════════════════════════════════════════════════════════════════╗
║  ELITE DIRECTORY & ENDPOINT FUZZER v1.0 — CEH v13 Lab Arsenal             ║
║  Multi-threaded web content discovery with recursive scanning              ║
║  LAB-ONLY — AUTHORIZED TESTING ONLY                                       ║
╚══════════════════════════════════════════════════════════════════════════════╝
"""
import sys, os, re, json, time, argparse, string, random
import concurrent.futures
from datetime import datetime
from urllib.parse import urljoin, urlparse
try:
    import requests
    requests.packages.urllib3.disable_warnings()
except ImportError:
    print("FATAL: pip install requests"); sys.exit(1)

# Built-in wordlists
WORDLISTS = {
    "common": [
        "admin","login","dashboard","panel","api","upload","uploads","images","img",
        "css","js","static","assets","media","files","backup","backups","config",
        "configuration","test","testing","dev","development","staging","demo",
        "wp-admin","wp-login","wp-content","wp-includes","administrator",
        "phpmyadmin","phpinfo","server-status","server-info",".env",".git",
        ".htaccess",".htpasswd","robots.txt","sitemap.xml","crossdomain.xml",
        "web.config","package.json","composer.json","Gruntfile.js","gulpfile.js",
        "console","debug","trace","actuator","health","metrics","info","status",
        "swagger","docs","api-docs","graphql","graphiql","playground",
        "cgi-bin","bin","scripts","includes","inc","lib","vendor","node_modules",
        "tmp","temp","cache","log","logs","error","errors","old","new","bak",
        "backup.sql","dump.sql","database","db","data","export","import",
        "user","users","account","accounts","profile","profiles","register",
        "signup","signin","logout","forgot","reset","password","auth",
        "token","session","oauth","sso","saml","callback","redirect",
        "search","query","filter","sort","page","index","home","main",
        "about","contact","help","support","faq","terms","privacy","legal",
        "blog","post","article","news","feed","rss","atom","sitemap",
        "image","photo","video","audio","document","pdf","download","file",
        "report","reports","analytics","stats","statistics","monitor",
        "manage","manager","management","control","settings","options",
        "install","setup","update","upgrade","patch","deploy","release",
        "secret","secrets","key","keys","token","tokens","credential",
        "internal","private","restricted","secure","protected","hidden",
        "v1","v2","v3","api/v1","api/v2","rest","soap","wsdl","xml",
        "json","yaml","yml","csv","txt","html","htm","php","asp","aspx",
        "jsp","cgi","pl","py","rb","java","class","jar","war","ear",
    ],
    "extensions": [
        "",".php",".html",".htm",".asp",".aspx",".jsp",".py",".rb",".pl",
        ".txt",".xml",".json",".yml",".yaml",".conf",".cfg",".ini",".env",
        ".bak",".old",".orig",".save",".swp",".log",".sql",".gz",".tar",
        ".zip",".rar",".7z",".pdf",".doc",".xls",
    ],
    "api": [
        "api","api/v1","api/v2","api/v3","rest","graphql","graphiql",
        "swagger.json","openapi.json","api-docs","swagger-ui",
        "api/users","api/user","api/admin","api/login","api/register",
        "api/token","api/auth","api/config","api/settings",
        "api/upload","api/download","api/export","api/import",
        "api/search","api/query","api/health","api/status",
        "api/debug","api/test","api/internal",
    ],
}

class DirFuzzer:
    def __init__(self, args):
        self.args = args
        self.target = args.target.rstrip("/")
        self.found = []
        self.stats = {"requests": 0, "found": 0, "errors": 0, "filtered": 0}
        self.session = requests.Session()
        self.session.verify = False
        self.session.headers["User-Agent"] = args.user_agent or "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
        if args.proxy:
            self.session.proxies = {"http": args.proxy, "https": args.proxy}
        if args.cookie:
            for c in args.cookie.split(";"):
                k, v = c.strip().split("=", 1)
                self.session.cookies.set(k.strip(), v.strip())

        # Get baseline for filtering
        self._baseline_size = None
        self._baseline_words = None

    def c(self, color, text):
        colors = {"R":"\033[91m","G":"\033[92m","Y":"\033[93m","B":"\033[94m",
                  "C":"\033[96m","W":"\033[97m","0":"\033[0m"}
        if not self.args.no_color:
            return f"{colors.get(color,'')}{text}{colors['0']}"
        return text

    def _get_baseline(self):
        """Get response for non-existent path to filter false positives"""
        random_path = "".join(random.choices(string.ascii_lowercase, k=20))
        try:
            resp = self.session.get(f"{self.target}/{random_path}", timeout=self.args.timeout, allow_redirects=False)
            self._baseline_size = len(resp.text)
            self._baseline_words = len(resp.text.split())
            self._baseline_status = resp.status_code
        except Exception:
            self._baseline_size = 0
            self._baseline_words = 0
            self._baseline_status = 404

    def _is_interesting(self, resp, path):
        """Filter false positives"""
        if resp.status_code in [404, 400, 405, 501, 502, 503]:
            return False

        # Filter by status code
        if self.args.status_filter:
            allowed = [int(s) for s in self.args.status_filter.split(",")]
            if resp.status_code not in allowed:
                self.stats["filtered"] += 1
                return False

        # Filter by size (same as 404 page = false positive)
        if self._baseline_size and abs(len(resp.text) - self._baseline_size) < 10:
            self.stats["filtered"] += 1
            return False

        # Filter by hide options
        if self.args.hide_size:
            sizes = [int(s) for s in self.args.hide_size.split(",")]
            if len(resp.text) in sizes:
                return False

        if self.args.hide_status:
            statuses = [int(s) for s in self.args.hide_status.split(",")]
            if resp.status_code in statuses:
                return False

        return True

    def _fuzz_path(self, path):
        url = f"{self.target}/{path}"
        self.stats["requests"] += 1
        try:
            if self.args.delay > 0:
                time.sleep(self.args.delay)
            resp = self.session.get(url, timeout=self.args.timeout, allow_redirects=False)

            if self._is_interesting(resp, path):
                size = len(resp.text)
                status = resp.status_code
                redirect = resp.headers.get("Location", "")

                # Color by status
                if 200 <= status < 300:
                    sc = self.c("G", str(status))
                elif 300 <= status < 400:
                    sc = self.c("B", str(status))
                elif status == 403:
                    sc = self.c("Y", str(status))
                else:
                    sc = self.c("R", str(status))

                result = {"url": url, "status": status, "size": size, "redirect": redirect, "path": path}
                self.found.append(result)
                self.stats["found"] += 1

                redir = f" → {redirect[:40]}" if redirect else ""
                print(f"  {sc}  {size:>8} bytes  /{path}{redir}")
                return result
        except requests.exceptions.ConnectionError:
            self.stats["errors"] += 1
        except requests.exceptions.Timeout:
            self.stats["errors"] += 1
        except Exception:
            self.stats["errors"] += 1
        return None

    def run(self):
        print(f"""
{'='*70}
  ⚡ ELITE DIRECTORY & ENDPOINT FUZZER v1.0
  Target:  {self.target}
  Threads: {self.args.threads}
  Proxy:   {self.args.proxy or 'None'}
{'='*70}""")

        # Get baseline
        self._get_baseline()
        print(f"  Baseline: {self._baseline_status} ({self._baseline_size} bytes)")

        # Build wordlist
        if self.args.wordlist and os.path.exists(self.args.wordlist):
            with open(self.args.wordlist, "r") as f:
                words = [l.strip() for l in f if l.strip() and not l.startswith("#")]
        else:
            wl_name = self.args.builtin_wordlist or "common"
            words = WORDLISTS.get(wl_name, WORDLISTS["common"])

        # Apply extensions
        extensions = [""]
        if self.args.extensions:
            extensions = self.args.extensions.split(",")
        elif not self.args.no_extensions:
            extensions = ["", ".php", ".html", ".txt", ".bak", ".json"]

        paths = []
        for word in words:
            for ext in extensions:
                paths.append(f"{word}{ext}")

        print(f"  Wordlist: {len(words)} words × {len(extensions)} extensions = {len(paths)} paths")
        print(f"\n  {'STATUS':>6}  {'SIZE':>8}       PATH")
        print(f"  {'─'*6}  {'─'*8}  {'─'*50}")

        start = time.time()
        with concurrent.futures.ThreadPoolExecutor(max_workers=self.args.threads) as executor:
            list(executor.map(self._fuzz_path, paths))
        elapsed = time.time() - start

        # Recursive scanning
        if self.args.recursive and self.found:
            dirs = [f["path"] for f in self.found if f["status"] in [200, 301, 302, 403]]
            if dirs:
                print(f"\n  {self.c('C','[Recursive]')} Scanning {len(dirs)} discovered directories...")
                for d in dirs[:10]:  # Limit recursion
                    sub_paths = [f"{d}/{w}" for w in words[:50]]
                    with concurrent.futures.ThreadPoolExecutor(max_workers=self.args.threads) as executor:
                        list(executor.map(self._fuzz_path, sub_paths))

        # Summary
        print(f"\n{'='*70}")
        print(f"  📊 FUZZING COMPLETE in {elapsed:.1f}s")
        print(f"{'='*70}")
        print(f"  Requests:  {self.stats['requests']}")
        print(f"  Found:     {self.c('G', str(self.stats['found']))}")
        print(f"  Filtered:  {self.stats['filtered']}")
        print(f"  Errors:    {self.stats['errors']}")
        print(f"  Speed:     {self.stats['requests']/elapsed:.0f} req/s" if elapsed > 0 else "")

        if self.found:
            # Highlight interesting findings
            criticals = [f for f in self.found if any(p in f["path"].lower()
                for p in [".env",".git","backup","config","admin","phpmyadmin","debug","actuator"])]
            if criticals:
                print(f"\n  {self.c('R','⚠ HIGH-VALUE FINDINGS:')}")
                for f in criticals:
                    print(f"    → [{f['status']}] {f['url']}")

        report = self.args.output or f"dirfuzz-{urlparse(self.target).netloc}-{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        with open(report, "w") as f:
            json.dump({"target": self.target, "found": self.found, "stats": self.stats}, f, indent=2)
        print(f"\n  📄 Report: {report}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Elite Directory & Endpoint Fuzzer",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s http://192.168.1.1/                              # Common wordlist
  %(prog)s http://target/ -w /usr/share/wordlists/dir.txt   # Custom wordlist
  %(prog)s http://target/ -b api -t 50                      # API endpoint fuzzing
  %(prog)s http://target/ -e .php,.html,.bak -t 100         # Custom extensions
  %(prog)s http://target/ -r                                # Recursive mode
  %(prog)s http://target/ --proxy http://127.0.0.1:8080     # Through Burp
  %(prog)s http://target/ --hide-status 403,301             # Hide 403/301 responses
        """)
    parser.add_argument("target", help="Target URL")
    parser.add_argument("-w", "--wordlist", help="Path to custom wordlist file")
    parser.add_argument("-b", "--builtin-wordlist", choices=["common","api"], help="Built-in wordlist")
    parser.add_argument("-e", "--extensions", help="Comma-separated extensions (e.g., .php,.html,.bak)")
    parser.add_argument("--no-extensions", action="store_true", help="Don't append extensions")
    parser.add_argument("-t", "--threads", type=int, default=30, help="Thread count (default: 30)")
    parser.add_argument("-r", "--recursive", action="store_true", help="Recursively scan discovered dirs")
    parser.add_argument("--timeout", type=float, default=5, help="Request timeout")
    parser.add_argument("--delay", type=float, default=0, help="Delay between requests")
    parser.add_argument("--proxy", help="HTTP proxy")
    parser.add_argument("--cookie", help="Cookie string")
    parser.add_argument("--user-agent", help="Custom User-Agent")
    parser.add_argument("--status-filter", help="Only show these status codes (e.g., 200,301)")
    parser.add_argument("--hide-status", help="Hide these status codes")
    parser.add_argument("--hide-size", help="Hide responses with these sizes")
    parser.add_argument("-o", "--output", help="Output JSON file")
    parser.add_argument("--no-color", action="store_true")

    args = parser.parse_args()
    fuzzer = DirFuzzer(args)
    fuzzer.run()
