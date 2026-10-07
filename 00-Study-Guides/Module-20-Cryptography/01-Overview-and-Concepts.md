# 01. Overview and Concepts — Cryptography

> [!INFO] 📌 **Module Scope & Core Objectives**
> Direct technical extraction from official CEH v13 Syllabus (Module 20). Covers Symmetric Encryption Ciphers (DES, 3DES, AES, Blowfish, RC4, ChaCha20), Asymmetric Encryption Algorithms (RSA, ECC, Diffie-Hellman, DSA), Hashing Functions & Message Digests (MD5, SHA-1, SHA-2, SHA-3, HMAC), Public Key Infrastructure (PKI / X.509 CAs), Cryptanalytic Attacks (Known-Plaintext, Chosen-Ciphertext, Birthday Attack, Collision Attacks), and Post-Quantum Cryptography (PQC).

---

## 🧠 1. Cryptographic Algorithms & Cipher Architecture

### 1.1 Symmetric vs Asymmetric Encryption
- **Symmetric Encryption**: Uses a single pre-shared key for both encryption and decryption. High speed; suitable for bulk data encryption. Block ciphers (AES, DES) or stream ciphers (RC4, ChaCha20).
- **Asymmetric Encryption**: Uses a mathematically linked keypair—a **Public Key** for encryption/verification and a **Private Key** for decryption/signing. Solves key distribution challenges.

> [!ABSTRACT] 🏛️ **📋 Comprehensive Symmetric vs Asymmetric Algorithm Matrix**

| Cryptographic Standard | Encryption Family | Key Length Options | Block / Stream Type | Primary Application / Purpose |
| :--- | :--- | :--- | :--- | :--- |
| **AES (Rijndael)** | Symmetric | 128, 192, 256 bits | 128-bit Block | Government / Enterprise Data at Rest |
| **DES / 3DES** | Symmetric | 56 bits / 168 bits | 64-bit Block | Obsolete legacy financial transactions |
| **RC4** | Symmetric | 40 - 2048 bits | Stream Cipher | Deprecated stream cipher (WEP/TLS 1.0) |
| **RSA** | Asymmetric | 2048, 4096 bits | Prime Factorization | Digital Signatures & Key Exchange |
| **ECC (Elliptic Curve)**| Asymmetric | 256, 384, 521 bits | Elliptic Curve Discrete Log | High-performance Mobile / TLS Handshakes |
| **Diffie-Hellman (DH)** | Key Exchange | 2048+ bits | Discrete Logarithm | Perfect Forward Secrecy (PFS) session key setup |

---

## ⚡ 2. Hashing, Message Authentication & PKI Architecture

### 2.1 Cryptographic Hash Functions & HMAC
Hash functions take arbitrary-length input data and produce a fixed-length deterministic output digest. Properties: Pre-image resistance, Second pre-image resistance, Collision resistance.

- **MD5**: 128-bit digest length. Broken by collision attacks (Flame malware).
- **SHA-1**: 160-bit digest length. Obsolete due to SHAttered collision attack.
- **SHA-2 / SHA-3**: SHA-256, SHA-512 (SHA-2) and Keccak-based SHA-3 standard.
- **HMAC (Hash-based Message Authentication Code)**: Combines a secret key with a cryptographic hash function (e.g., HMAC-SHA256) to ensure message integrity and authenticity.

> [!IMPORTANT] 🔄 **📋 Comprehensive Cryptanalytic Attack Matrix**

| Cryptanalytic Attack | Target Mechanism | Technical Attack Vector | Defensive Countermeasure |
| :--- | :--- | :--- | :--- |
| **Birthday Attack** | Hash Functions | Exploits probability of collision ($2^{n/2}$) | Use $\ge 256$-bit hash digests (SHA-256) |
| **Known-Plaintext** | Block Ciphers | Attacker possesses sample plaintext and ciphertext pairs | Avoid weak ECB mode / Use AES-GCM |
| **Padding Oracle** | CBC Block Ciphers | Interrogates PKCS#7 padding error responses | Authenticated Encryption (AEAD / GCM) |
| **Replay Attack** | Authentication | Re-transmits captured valid session tokens | Nonces, Timestamps, Sequence numbers |
