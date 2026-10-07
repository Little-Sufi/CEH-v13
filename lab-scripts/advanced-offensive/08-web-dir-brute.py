#!/usr/bin/env python3
# LAB-ONLY: Web Directory & File Brute-Forcer
# CEH v13 Master Module 02,04
# STRICTLY FOR AUTHORIZED LAB USE ONLY!
import requests
import sys
from concurrent.futures import ThreadPoolExecutor, as_completed

# -------------------------- EDIT THESE VALUES FOR YOUR LAB --------------------------
LAB_TARGET_URL = "http://192.168.100.10/"  # YOUR lab web target (trailing slash!)
LAB_WORDLIST_PATH = "/usr/share/seclists/Discovery/Web-Content/directory-list-2.3-medium.txt"
LAB_EXTENSIONS = ["", ".php", ".html", ".txt", ".bak", ".old", ".zip", ".sql"]
LAB_THREADS = 20  # Number of threads (don't overload lab!)
LAB_SUCCESS_CODES = [200, 204, 301, 302, 307, 401, 403]
# -----------------------------------------------------------------------------------

def test_path(base, path):
    try:
        full_url = base.rstrip("/") + "/" + path.lstrip("/")
        response = requests.head(full_url, timeout=3, allow_redirects=True, verify=False)
        if response.status_code in LAB_SUCCESS_CODES:
            return (response.status_code, full_url)
        return None
    except:
        return None

def main():
    print("="*80)
    print("LAB-ONLY: Web Directory & File Brute-Forcer")
    print("="*80)
    print(f"Target: {LAB_TARGET_URL}")
    print(f"Extensions: {LAB_EXTENSIONS}")
    print("-"*80)
    try:
        with open(LAB_WORDLIST_PATH, "r", encoding="utf-8", errors="ignore") as f:
            paths = [line.strip() for line in f if line.strip() and not line.startswith("#")]
    except FileNotFoundError:
        print(f"ERROR: Wordlist not found at {LAB_WORDLIST_PATH}! Edit script!")
        sys.exit(1)
    found = []
    print(f"Starting brute-force with {LAB_THREADS} threads on {len(paths)} base paths (+ extensions)...")
    with ThreadPoolExecutor(max_workers=LAB_THREADS) as executor:
        futures = []
        for path in paths:
            for ext in LAB_EXTENSIONS:
                test_p = path + ext
                futures.append(executor.submit(test_path, LAB_TARGET_URL, test_p))
        for i, future in enumerate(as_completed(futures)):
            if i % 250 == 0 and i > 0:
                print(f"Checked {i} paths so far...")
            res = future.result()
            if res:
                found.append(res)
                print(f"âœ… [{res[0]}] {res[1]}")
    print("-"*80)
    print(f"Scan complete! Found {len(found)} paths/files!")

if __name__ == "__main__":
    if not any(prefix in LAB_TARGET_URL for prefix in ["10.", "172.16.", "172.17.", "172.18.", "172.19.", "172.20.", "172.21.", "172.22.", "172.23.", "172.24.", "172.25.", "172.26.", "172.27.", "172.28.", "172.29.", "172.30.", "172.31.", "192.168.", "localhost", "127.0.0.1"]):
        print("ERROR: LAB-ONLY! Private lab targets only!")
        sys.exit(1)
    import urllib3
    urllib3.disable_warnings()
    main()
