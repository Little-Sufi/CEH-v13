# 04. Countermeasures — Hacking Web Applications

> [!SHIELD] 🏰 **Defensive Hardening Standards & Secure Coding**
> Direct technical extraction from official CEH v13 Syllabus (Module 14). Covers Context-Aware Output Encoding, Content Security Policy (CSP), CSRF Anti-Forgery Tokens, Input Validation Allowlisting, and WAF Enforcement.

---

## 🛡️ 1. Web Application Hardening Standards

### 1.1 Technical Defensive Checklist

1. **Context-Aware Output Encoding**: Encode all user-supplied data prior to rendering in HTML body, HTML attributes, JavaScript context, or CSS rules to prevent XSS.
2. **Content Security Policy (CSP)**: Implement strong HTTP CSP headers to restrict allowed JavaScript execution origins:
   ```http
   Content-Security-Policy: default-src 'self'; script-src 'self' https://trustedscripts.com; object-src 'none'
   ```
3. **CSRF Anti-Forgery Tokens**: Implement the **Synchronizer Token Pattern** where a cryptographically random, unguessable token is validated for every state-changing request (POST/PUT/DELETE).
4. **Input Validation Allowlisting**: Validate input length, data type, and structure using strict allowlists rather than blocklists.
5. **SSRF Mitigation**: Restrict egress HTTP requests from web servers to internal IP ranges (`10.0.0.0/8`, `172.16.0.0/12`, `192.168.0.0/16`, `169.254.169.254`).

> [!SHIELD] 🏰 **📋 Comprehensive Web Application Defense Reference Matrix**

| Vulnerability Vector | Primary Defensive Control | Implementation Standard |
| :--- | :--- | :--- |
| **Cross-Site Scripting (XSS)** | Context-Aware Output Encoding & CSP | HTML entity encoding + strict CSP header |
| **CSRF** | Anti-CSRF Synchronizer Tokens | Unique per-session random token validation |
| **SSRF** | Egress Network Filtering & URL Parsing | Block internal IP subnets & AWS metadata IP |
| **LFI / RFI** | Disable `allow_url_include` & Use Allowlists| Avoid dynamic file inclusion using user input |
