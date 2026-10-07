#!/usr/bin/env python3
# LAB-ONLY: Advanced Directory Bruteforcer
# CEH v13 Master Module 02
# STRICTLY FOR AUTHORIZED LAB USE ONLY!
# DETAILED EXPLANATION: Brute-forces directories/files with custom wordlists and extensions
import requests
import sys
from queue import Queue
import threading

# -------------------------- EDIT THESE VALUES FOR YOUR LAB --------------------------
LAB_TARGET_URL = "http://192.168.100.10/"
LAB_WORDLIST = ["admin", "backup", "config", "css", "images", "js", "phpmyadmin", "robots.txt", "sitemap.xml", "test", "upload", "wp-admin"]
LAB_EXTENSIONS = ["php", "html", "txt", "bak", "old", "zip"]
LAB_THREADS = 10
# -----------------------------------------------------------------------------------

def worker():
    while not q.empty():
        path = q.get()
        try:
            resp = requests.get(f"{LAB_TARGET_URL}{path}", timeout=5, verify=False)
            if resp.status_code in [200, 301, 302, 403]:
                print(f"[+] Found: {LAB_TARGET_URL}{path} (Status: {resp.status_code})")
        except Exception as e:
            pass
        finally:
            q.task_done()

def main():
    print("="*80)
    print("LAB-ONLY: Advanced Directory Bruteforcer")
    print("="*80")
    print(f"[*] Target: {LAB_TARGET_URL}")
    print("-"*80")
    global q
    q = Queue()
    for word in LAB_WORDLIST:
        q.put(word)
        for ext in LAB_EXTENSIONS:
            q.put(f"{word}.{ext}")
    print(f"[*] Starting {LAB_THREADS} threads...")
    for i in range(LAB_THREADS):
        t = threading.Thread(target=worker)
        t.daemon = True
        t.start()
    q.join()
    print("[*] Done!")

if __name__ == "__main__":
    if not any(prefix in LAB_TARGET_URL for prefix in ["10.", "172.16.", "172.17.", "172.18.", "172.19.", "172.20.", "172.21.", "172.22.", "172.23.", "172.24.", "172.25.", "172.26.", "172.27.", "172.28.", "172.29.", "172.30.", "172.31.", "192.168.", "localhost", "127.0.0.1"]):
        print("ERROR: LAB-ONLY! Use only private lab targets!")
        sys.exit(1)
    import urllib3
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    main()
