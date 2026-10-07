![Header](https://images.unsplash.com/photo-1516321318423-f06f85e504b3?w=900&h=150&fit=crop)

# 🔓 Advanced Offensive Scripts (Full Index: 60 Scripts)

[← Lab Scripts Home](../Home.md) | [Vault Home](../../Home.md) | [Full Playbook](../../Tools-Guides/Ultimate-Hacker-Playbook.md)

---

## 📝 Index of Scripts
| # | Name | Type |
|---|------|------|
| 1 | [01-advanced-nmap-enum.py](01-advanced-nmap-enum.py) | Nmap enumeration |
| 2 | [02-error-based-sqli.py](02-error-based-sqli.py) | Error-based SQLi |
| 3 | [03-xss-tester.py](03-xss-tester.py) | XSS testing |
| 4 | [04-lfi-tester.py](04-lfi-tester.py) | LFI testing |
| 5 | [05-cmd-injection-tester.py](05-cmd-injection-tester.py) | Command injection |
| 6 | [06-subdomain-enum.py](06-subdomain-enum.py) | Subdomain enum |
| 7 | [07-ad-enum-helper.py](07-ad-enum-helper.py) | AD enumeration |
| 8 | [08-web-dir-brute.py](08-web-dir-brute.py) | Web directory brute |
| 9 | [09-stealth-scan-wrapper.sh](09-stealth-scan-wrapper.sh) | Stealth scan |
| 10 | [10-xxe-tester.py](10-xxe-tester.py) | XXE testing |
| 11 | [11-hash-crack-helper.sh](11-hash-crack-helper.sh) | Hash cracking |
| 12 | [12-linux-privesc-enum.sh](12-linux-privesc-enum.sh) | Linux privesc enum |
| 13 | [13-windows-privesc-enum.bat](13-windows-privesc-enum.bat) | Windows privesc enum |
| 14 | [14-scapy-sniffer.py](14-scapy-sniffer.py) | Packet sniffer |
| 15 | [15-wireless-scanner.py](15-wireless-scanner.py) | Wireless scanning |
| 16 | [16-time-based-sqli.py](16-time-based-sqli.py) | Time-based SQLi |
| 17 | [17-blind-sqli-extractor.py](17-blind-sqli-extractor.py) | Blind SQLi extract |
| 18 | [18-union-sqli-exploit.py](18-union-sqli-exploit.py) | Union SQLi |
| 19 | [19-xxe-exploit-helper.py](19-xxe-exploit-helper.py) | XXE exploit |
| 20 | [20-command-injection-advanced.py](20-command-injection-advanced.py) | Command injection adv |
| 21 | [21-xss-advanced-tester.py](21-xss-advanced-tester.py) | XSS adv testing |
| 22 | [22-lfi-advanced-tester.py](22-lfi-advanced-tester.py) | LFI adv testing |
| 23 | [23-rfi-tester.py](23-rfi-tester.py) | RFI testing |
| 24 | [24-subdomain-takeover-check.py](24-subdomain-takeover-check.py) | Subdomain takeover |
| 25 | [25-directory-bruteforce-advanced.py](25-directory-bruteforce-advanced.py) | Directory brute adv |
| 26 | [26-port-knocking-helper.py](26-port-knocking-helper.py) | Port knocking |
| 27 | [27-ad-enum-advanced.py](27-ad-enum-advanced.py) | AD enum adv |
| 28 | [28-kerberoasting-helper.py](28-kerberoasting-helper.py) | Kerberoasting |
| 29 | [29-asrep-roasting-helper.py](29-asrep-roasting-helper.py) | AS-REP Roasting |
| 30 | [30-bloodhound-helper.py](30-bloodhound-helper.py) | BloodHound |
| 31 | [31-mimikatz-helper.py](31-mimikatz-helper.py) | Mimikatz |
| 32 | [32-linux-privesc-advanced.sh](32-linux-privesc-advanced.sh) | Linux privesc adv |
| 33 | [33-windows-privesc-advanced.bat](33-windows-privesc-advanced.bat) | Windows privesc adv |
| 34 | [34-scapy-sniffer-advanced.py](34-scapy-sniffer-advanced.py) | Packet sniffer adv |
| 35 | [35-wireless-handshake-capture.sh](35-wireless-handshake-capture.sh) | WPA2 handshake |
| 36 | [36-stealth-scanner.py](36-stealth-scanner.py) | Stealth scanner |
| 37 | [37-reverse-shell-generator.py](37-reverse-shell-generator.py) | Reverse shell generator |
| 38 | [38-web-shell-generator.py](38-web-shell-generator.py) | Web shell generator |
| 39 | [39-exfiltration-helper.py](39-exfiltration-helper.py) | Exfiltration |
| 40 | [40-persistence-helper.py](40-persistence-helper.py) | Persistence |
| 41 | [41-pass-the-hash-helper.py](41-pass-the-hash-helper.py) | PtH |
| 42 | [42-dll-hijacking-helper.py](42-dll-hijacking-helper.py) | DLL hijacking |
| 43 | [43-smb-relay-helper.py](43-smb-relay-helper.py) | SMB relay |
| 44 | [44-arp-poisoning-helper.py](44-arp-poisoning-helper.py) | ARP poisoning |
| 45 | [45-dns-cache-poisoning-helper.py](45-dns-cache-poisoning-helper.py) | DNS poisoning |
| 46 | [46-metasploit-payload-generator.py](46-metasploit-payload-generator.py) | Msfvenom |
| 47 | [47-sqlmap-helper.py](47-sqlmap-helper.py) | sqlmap |
| 48 | [48-wpscan-helper.py](48-wpscan-helper.py) | WPScan |
| 49 | [49-metasploit-listener-helper.py](49-metasploit-listener-helper.py) | Metasploit listener |
| 50 | [50-keylogger-skeleton.py](50-keylogger-skeleton.py) | Keylogger skeleton |
| 51 | [51-buffer-overflow-skeleton.py](51-buffer-overflow-skeleton.py) | Buffer overflow |
| 52 | [52-socat-port-forward-helper.py](52-socat-port-forward-helper.py) | Socat |
| 53 | [53-ssh-pivoting-helper.py](53-ssh-pivoting-helper.py) | SSH pivoting |
| 54 | [54-evil-winrm-helper.py](54-evil-winrm-helper.py) | Evil-WinRM |
| 55 | [55-netcat-reverse-shell-helper.py](55-netcat-reverse-shell-helper.py) | Netcat |
| 56 | [56-hash-identifier-helper.py](56-hash-identifier-helper.py) | Hash ID |
| 57 | [57-ftp-anonymous-login-check.py](57-ftp-anonymous-login-check.py) | FTP anonymous |
| 58 | [58-snmp-enum-helper.py](58-snmp-enum-helper.py) | SNMP enum |
| 59 | [59-wordpress-username-enum.py](59-wordpress-username-enum.py) | WP user enum |
| 60 | [60-crackmapexec-helper.py](60-crackmapexec-helper.py) | CrackMapExec |

