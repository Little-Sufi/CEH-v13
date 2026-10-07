# 04. Countermeasures — Cryptography

> [!SHIELD] 🏰 **Defensive Hardening Standards & Secure Configuration**
> Direct technical extraction from official CEH v13 Syllabus (Module 20). Covers Algorithm Deprecation (MD5/SHA1/DES), Modern Cipher Enforcement (AES-256-GCM), Perfect Forward Secrecy (PFS), Hardware Security Modules (HSM), Certificate Revocation (CRL/OCSP), and Post-Quantum Cryptography (PQC).

---

## 🛡️ 1. Cryptographic Hardening Checklist

### 1.1 Technical Defensive Standards

1. **Deprecate Weak Ciphers & Hashes**: Immediately phase out WEP, RC4, DES, 3DES, MD5, and SHA-1. Mandate **AES-256-GCM** and **SHA-256 / SHA-3**.
2. **Enforce Authenticated Encryption with Associated Data (AEAD)**: Prefer AES Galois/Counter Mode (GCM) over Cipher Block Chaining (CBC) to eliminate Padding Oracle vulnerabilities.
3. **Deploy Perfect Forward Secrecy (PFS)**: Enforce Ephemeral Diffie-Hellman (`ECDHE`) key exchanges in TLS configurations so compromising a server's private key cannot retroactively decrypt past recorded sessions.
4. **Hardware Security Modules (HSMs) & Key Management**: Store root Certificate Authority keys and master encryption keys inside tamper-resistant Hardware Security Modules (HSMs).

> [!SHIELD] 🏰 **📋 Comprehensive Cryptographic Security Hardening Matrix**

| Vulnerability Vector | Insecure Legacy Cipher | Mandatory Hardening Standard |
| :--- | :--- | :--- |
| **Hash Collision Attacks** | MD5 / SHA-1 | Upgrade to SHA-256, SHA-512, or SHA-3 |
| **Padding Oracle Vulnerability**| AES-CBC with PKCS#7 | AES-256-GCM (Authenticated Encryption - AEAD) |
| **Session Decryption Risk** | RSA Key Exchange (Non-PFS) | ECDHE (Elliptic Curve Diffie-Hellman Ephemeral) |
| **Key Theft & Exposure** | Key stored on disk web server | Hardware Security Module (HSM) / Key Vault |
