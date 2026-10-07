# 05. Course Detailed Notes — Cryptography

> [!ABSTRACT] 🏛️ **Comprehensive Syllabus Notes & Technical Reference**
> Direct technical extraction from official CEH v13 Syllabus (Module 20). Covers PKI Hierarchy, X.509 Certificate Anatomy, CRL vs OCSP, and Disk Encryption Architecture.

---

## 📌 1. Public Key Infrastructure (PKI) & X.509 Architecture

- **Certificate Authority (CA)**: Trusted third-party entity that issues and signs X.509 digital certificates linking public keys to entity identities.
- **Certificate Revocation List (CRL)**: Periodically published list of revoked certificates. Slow and heavy bandwidth.
- **Online Certificate Status Protocol (OCSP)**: Real-time protocol for querying certificate validity status, reducing bandwidth overhead.

> [!INFO] 📋 **Comprehensive Block Cipher Modes Comparison Matrix**

| Cipher Mode | Operational Mechanism | Error Propagation | Security Rating |
| :--- | :--- | :--- | :--- |
| **ECB (Electronic Codebook)**| Encrypts each block independently | Identical blocks yield identical ciphertext | Insecure (Patterns visible) |
| **CBC (Cipher Block Chaining)**| Chained XOR with previous block | Error affects current and next block | Vulnerable to Padding Oracle |
| **GCM (Galois/Counter Mode)**| Counter mode with Galois MAC | Authenticated Encryption (AEAD) | Maximum (Modern Standard) |
