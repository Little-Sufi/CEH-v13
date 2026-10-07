# 04. Countermeasures — Session Hijacking

> [!SHIELD] 🏰 **Defensive Security Controls & Session Hardening**
> Direct technical extraction from official CEH v13 Syllabus (Module 11). Covers Cookie Attribute Hardening, HSTS Header Enforcement, Post-Login Session Regeneration, and Server-Side Session Invalidation.

---

## 🛡️ 1. Defensive Hardening Standards

### 1.1 Technical Hardening Checklist

1. **Session Regeneration**: Always invalidate pre-login session IDs and issue a new cryptographic session ID immediately after successful authentication.
2. **Set Defensive Cookie Attributes**:
   ```http
   Set-Cookie: SID=xyz123; Secure; HttpOnly; SameSite=Strict; Path=/; Domain=example.com
   ```
3. **Enforce HSTS (HTTP Strict Transport Security)**:
   ```http
   Strict-Transport-Security: max-age=31536000; includeSubDomains; preload
   ```
4. **Server-Side Session Timeout & Termination**: Implement idle timeouts (e.g., 15 minutes) and invalidate server-side session stores upon user logout.

> [!SHIELD] 🏰 **📋 Comprehensive Session Hardening Reference Matrix**

| Defensive Control | Implementation Layer | Target Vulnerability Vector | Security Standard |
| :--- | :--- | :--- | :--- |
| **Session ID Regeneration**| Web App Logic | Session Fixation | Issue new ID immediately post-auth |
| **`HttpOnly` + `Secure`** | HTTP Headers | XSS Cookie Theft & Sniffing | Block JS access & force HTTPS |
| **HSTS Header** | Web Server Config | SSL / TLS Stripping | Force HTTPS connections for 1 year |
| **CSPRNG Session IDs** | App Framework | Session ID Brute-force / Prediction | Generate >=128-bit random entropy |
