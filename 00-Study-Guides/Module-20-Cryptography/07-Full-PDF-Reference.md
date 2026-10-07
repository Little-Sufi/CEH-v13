# 📜 07. Full PDF Reference — Cryptography

> [!INFO] 🏛️ **Official CEH v13 PDF Source Master Repository**
> Cleaned, high-readability technical text extraction directly from official CEH v13 Syllabus PDF (`CEH_v13__Module_20_Cryptography.pdf`). Formatted as structured Markdown prose with proper paragraphs, section headers, and key term highlights.

---

## 📊 Syllabus Metadata & Source Breakdown

> [!ABSTRACT] 📋 **Comprehensive PDF Syllabus Metadata Reference Matrix**

| Metadata Attribute | Syllabus Parameter Value |
| :--- | :--- |
| **Course Module** | **Module 20: Cryptography** |
| **Source PDF File** | `CEH_v13__Module_20_Cryptography.pdf` |
| **Total Extracted Pages** | `73 Pages` |
| **Formatting Standard** | Ultra-Readable Markdown Prose & Structured Headings |
| **Extraction Status** | 100% Complete / Verified Text Flow |

---

## 📑 Structured & Readable Syllabus Reference

> [!NOTE]- 📄 **Pages 1 to 5 Syllabus Content**
>
> ### 📍 Page 1
>
> 
> #### 🔹 ✒
> 
> 
> 
> #### 🔹 Cryptography
> 
> 
> 
> #### 🔹 Cryptography
> 
> 
> 
> #### 🔹 📋Module Overview
> 
> 
> This module covers cryptographic principles, encryption algorithms, practical applications, and cryptanalysis techniques, including
> 
> 
> #### 🔹 symmetric and asymmetric encryption, hashing, PKI, digital
> 
> 
> 
> #### 🔹 signatures, and comprehensive offensive and defensive
> 
> 
> cryptographic implementations.
> 
> 
> #### 🔹 1. Cryptography Concepts
> 
> 
> 
> #### 🔹 1.1 Introduction to Cryptography
> 
> 
> 
> #### 🔹 🔐Cryptography
> 
> 
> The science of protecting information by transforming it into a secure format that prevents unauthorized access, ensuring confidentiality, integrity, authentication, and non-repudiation.
> 
> 
> #### 🔹 Four Core Security Goals:
> 
> 
> 
> #### 🔹 Confidentiality
> 
> 
> 
> #### 🔹 Preventing unauthorized access to information
> 
>
> ---
>
> ### 📍 Page 2
>
> 
> #### 🔹 Integrity
> 
> 
> 
> #### 🔹 Ensuring data hasn't been altered
> 
> 
> 
> #### 🔹 Authentication
> 
> 
> 
> #### 🔹 Verifying identity of users and systems
> 
> 
> 
> #### 🔹 Non-Repudiation
> 
> 
> 
> #### 🔹 Proof of origin that cannot be denied
> 
> 
> 
> #### 🔹 Cryptography Components:
> 
> 
> 
> #### 🔹 Algorithms
> 
> 
> 
> #### 🔹 Mathematical procedures for encryption/decryption
> 
> 
> 
> #### 🔹 Keys
> 
> 
> 
> #### 🔹 Secret values used with algorithms
> 
> 
> 
> #### 🔹 Protocols
> 
> 
> 
> #### 🔹 Rules governing cryptographic operations
> 
> 
> 
> #### 🔹 Plaintext
> 
> 
> 
> #### 🔹 Original readable data
> 
> 
> 
> #### 🔹 Ciphertext
> 
> 
> 
> #### 🔹 Encrypted unreadable data
> 
> 
> 
> #### 🔹 Encryption
> 
> 
> 
> #### 🔹 Converting plaintext to ciphertext
> 
> 
> 
> #### 🔹 Decryption
> 
> 
> 
> #### 🔹 Converting ciphertext back to plaintext
> 
> 
> 
> #### 🔹 1.2 Government Access to Keys (GAK)
> 
> 
> 
> #### 🔹 ⚠Key Escrow & Government Backdoors
> 
> 
> 
> #### 🔹 Government-mandated creation of key escrow systems allowing
> 
> 
> authorities to access encrypted data raises significant security and privacy concerns.
> 
> 
> #### 🔹 Key Escrow Concerns:
> 
>
> ---
>
> ### 📍 Page 3
>
> 
> #### 🔹 Security Weaknesses
> 
> 
> Backdoors create vulnerabilities exploitable by any attacker
> 
> 
> #### 🔹 Privacy Violations
> 
> 
> 
> #### 🔹 Undermines fundamental privacy rights
> 
> 
> 
> #### 🔹 Single Point of Failure
> 
> 
> 
> #### 🔹 Centralized key storage becomes high-value target
> 
> 
> 
> #### 🔹 International Issues
> 
> 
> 
> #### 🔹 Different jurisdictions with conflicting requirements
> 
> 
> 
> #### 🔹 Trust Erosion
> 
> 
> 
> #### 🔹 Weakens confidence in cryptographic systems
> 
> 
> 
> #### 🔹 Historical Examples:
> 
> 
> 
> #### 🔹 Clipper Chip 1990s)
> 
> 
> 
> #### 🔹 Dual_EC_DRBG backdoor controversy
> 
> 
> 
> #### 🔹 Ongoing encryption debates
> 
> 
> 
> #### 🔹 1.3 Cipher Types
> 
> 
> 
> #### 🔹 Cipher Classifications:
> 
> 
> 
> #### 🔹 Substitution Ciphers
> 
> 
> 
> #### 🔹 Definition:
> 
> 
> 
> #### 🔹 Replace characters with other characters
> 
> 
> 
> #### 🔹 Examples:
> 
> 
> 
> #### 🔹 Caesar cipher (shift by n)
> 
> 
> 
> #### 🔹 Monoalphabetic substitution
> 
> 
> 
> #### 🔹 Polyalphabetic Vigenère)
> 
> 
> 
> #### 🔹 Weakness:
> 
> 
> 
> #### 🔹 Vulnerable to frequency analysis
> 
> 
> 
> #### 🔹 Transposition Ciphers
> 
> 
> 
> #### 🔹 Definition:
> 
>
> ---
>
> ### 📍 Page 4
>
> 
> #### 🔹 Rearrange character positions without changing them
> 
> 
> 
> #### 🔹 Examples:
> 
> 
> 
> #### 🔹 Rail fence cipher
> 
> 
> 
> #### 🔹 Columnar transposition
> 
> 
> 
> #### 🔹 Route cipher
> 
> 
> 
> #### 🔹 Weakness:
> 
> 
> 
> #### 🔹 Patterns can be analyzed
> 
> 
> 
> #### 🔹 Cipher Modes
> 
> 
> 
> #### 🔹 Block Ciphers
> 
> 
> 
> #### 🔹 Encrypt fixed-size blocks (typically 64 or 128 bits)
> 
> 
> 
> #### 🔹 Examples: AES, DES, 3DES
> 
> 
> 
> #### 🔹 Requires padding for incomplete blocks
> 
> 
> 
> #### 🔹 Stream Ciphers
> 
> 
> 
> #### 🔹 Encrypt bit-by-bit or byte-by-byte
> 
> 
> 
> #### 🔹 Examples: RC4, ChaCha20
> 
> 
> 
> #### 🔹 No padding needed
> 
> 
> 
> #### 🔹 Typically faster for streaming data
> 
> 
> 
> #### 🔹 1.4 Symmetric Encryption Algorithms
> 
> 
> 
> #### 🔹 🔑Symmetric Encryption
> 
> 
> Single shared secret key used for both encryption and decryption. Fast and efficient but requires secure key distribution.
> 
> 
> #### 🔹 Characteristics:
> 
> 
> 
> #### 🔹 Same key for encryption and decryption
> 
> 
> 
> #### 🔹 Fast performance
> 
> 
> 
> #### 🔹 Key distribution challenge
> 
> 
> 
> #### 🔹 Suited for bulk encryption
> 
>
> ---
>
> ### 📍 Page 5
>
> 
> #### 🔹 1.4.1 Data Encryption Standard (DES)
> 
> 
> 
> #### 🔹 ❌DES  DEPRECATED
> 
> 
> Do not use DES. It is cryptographically broken and can be brute- forced in hours.
> 
> 
> #### 🔹 DES Specifications:
> 
> 
> 
> #### 🔹 Key size: 56 bits 64 bits with parity)
> 
> 
> 
> #### 🔹 Block size: 64 bits
> 
> 
> 
> #### 🔹 Rounds: 16 Feistel rounds
> 
> 
> 
> #### 🔹 Status: Broken by brute force
> 
> 
> 
> #### 🔹 Replacement: AES
> 
> 
> 
> #### 🔹 Why DES Failed:
> 
> 
> 
> #### 🔹 56-bit keyspace too small 2^56 combinations)
> 
> 
> 
> #### 🔹 Vulnerable to brute-force attacks
> 
> 
> 
> #### 🔹 EFF's Deep Crack machine cracked DES in 56 hours 1998
> 
> 
> 
> #### 🔹 1.4.2 Triple DES (3DES)
> 
> 
> 
> #### 🔹 3DES Specifications:
> 
> 
> 
> #### 🔹 Key size: 112 or 168 bits (three 56-bit keys)
> 
> 
> 
> #### 🔹 Block size: 64 bits
> 
> 
> 
> #### 🔹 Operation: Encrypt-Decrypt-Encrypt with DES
> 
> 
> 
> #### 🔹 Status: Deprecated (phasing out by 2023
> 
> 
> 
> #### 🔹 3DES Modes:
> 
> 
> 
> #### 🔹 3DESEDE2 Two-Key)
> 
> 
> 
> #### 🔹 K1  K3, effective 112-bit security
> 
> 
> 
> #### 🔹 3DESEDE3 Three-Key)
> 
> 
> 
> #### 🔹 All keys different, effective 168-bit security
> 
> 
> 
> #### 🔹 Limitations:
> 
>
> ---
>

> [!NOTE]- 📄 **Pages 6 to 10 Syllabus Content**
>
> ### 📍 Page 6
>
> 
> #### 🔹 Slower than AES
> 
> 
> 
> #### 🔹 Small block size 64-bit)
> 
> 
> 
> #### 🔹 Being replaced by AES
> 
> 
> 
> #### 🔹 1.4.3 Advanced Encryption Standard (AES)
> 
> 
> 
> #### 🔹 ✅AES  Industry Standard
> 
> 
> AES is the current symmetric encryption standard, providing strong security, high performance, and widespread adoption across all platforms.
> 
> 
> #### 🔹 AES Specifications:
> 
> 
> 
> #### 🔹 Key sizes: 128, 192, or 256 bits
> 
> 
> 
> #### 🔹 Block size: 128 bits
> 
> 
> 
> #### 🔹 Rounds: 10 AES128, 12 AES192, 14 AES256
> 
> 
> 
> #### 🔹 Algorithm: Substitution-Permutation Network
> 
> 
> 
> #### 🔹 Status: Current standard, no practical attacks
> 
> 
> 
> #### 🔹 AES Advantages:
> 
> 
> 
> #### 🔹 Fast
> 
> 
> 
> #### 🔹 AES Advantages:
> 
> 
> 
> #### 🔹 Fast in both hardware and software
> 
> 
> 
> #### 🔹 Secure against all known practical attacks
> 
> 
> 
> #### 🔹 Widely supported and standardized
> 
> 
> 
> #### 🔹 Suitable for high-performance applications
> 
> 
> 
> #### 🔹 AES Use Cases:
> 
> 
> 
> #### 🔹 TLS/SSL encryption
> 
> 
> 
> #### 🔹 VPN connections IPsec)
> 
> 
> 
> #### 🔹 Disk encryption BitLocker, FileVault)
> 
> 
> 
> #### 🔹 File encryption
> 
>
> ---
>
> ### 📍 Page 7
>
> 
> #### 🔹 Database encryption
> 
> 
> 
> #### 🔹 1.4.4 RC Algorithms
> 
> 
> 
> #### 🔹 RC4 Rivest Cipher 4
> 
> 
> 
> #### 🔹 Stream cipher
> 
> 
> 
> #### 🔹 Variable key size 402048 bits)
> 
> 
> 
> #### 🔹 Status: DEPRECATED
> 
> 
> 
> #### 🔹 Vulnerabilities: Biases in keystream, WEP attacks
> 
> 
> 
> #### 🔹 Do not use
> 
> 
> 
> #### 🔹 RC5
> 
> 
> 
> #### 🔹 Block cipher
> 
> 
> 
> #### 🔹 Variable block size, key size, rounds
> 
> 
> 
> #### 🔹 Simple design
> 
> 
> 
> #### 🔹 Not widely adopted
> 
> 
> 
> #### 🔹 RC6
> 
> 
> 
> #### 🔹 AES competition finalist
> 
> 
> 
> #### 🔹 Based on RC5
> 
> 
> 
> #### 🔹 Not selected as AES
> 
> 
> 
> #### 🔹 1.4.5 Blowfish
> 
> 
> 
> #### 🔹 Blowfish Specifications:
> 
> 
> 
> #### 🔹 Key size: 32448 bits (variable)
> 
> 
> 
> #### 🔹 Block size: 64 bits
> 
> 
> 
> #### 🔹 Rounds: 16
> 
> 
> 
> #### 🔹 Status: Secure but aging
> 
> 
> 
> #### 🔹 Characteristics:
> 
> 
> 
> #### 🔹 Fast
> 
> 
> 
> #### 🔹 Free (public domain)
> 
> 
> 
> #### 🔹 Widely used in password hashing tools
> 
>
> ---
>
> ### 📍 Page 8
>
> 
> #### 🔹 Small block size limits throughput
> 
> 
> 
> #### 🔹 1.4.6 Twofish
> 
> 
> 
> #### 🔹 Twofish Specifications:
> 
> 
> 
> #### 🔹 Key size: 128, 192, or 256 bits
> 
> 
> 
> #### 🔹 Block size: 128 bits
> 
> 
> 
> #### 🔹 Rounds: 16
> 
> 
> 
> #### 🔹 Status: Secure, AES finalist
> 
> 
> 
> #### 🔹 Advantages:
> 
> 
> 
> #### 🔹 No known practical attacks
> 
> 
> 
> #### 🔹 Public domain
> 
> 
> 
> #### 🔹 Flexible design
> 
> 
> 
> #### 🔹 1.4.7 Threefish
> 
> 
> 
> #### 🔹 Threefish Specifications:
> 
> 
> 
> #### 🔹 Key sizes: 256, 512, or 1024 bits
> 
> 
> 
> #### 🔹 Block size: Matches key size
> 
> 
> 
> #### 🔹 Used in: Skein hash function
> 
> 
> 
> #### 🔹 1.4.8 Serpent
> 
> 
> 
> #### 🔹 Serpent Specifications:
> 
> 
> 
> #### 🔹 Key size: 128, 192, or 256 bits
> 
> 
> 
> #### 🔹 Block size: 128 bits
> 
> 
> 
> #### 🔹 Rounds: 32 (very conservative)
> 
> 
> 
> #### 🔹 Status: AES finalist, very secure
> 
> 
> 
> #### 🔹 Characteristics:
> 
> 
> 
> #### 🔹 Extremely secure design
> 
> 
> 
> #### 🔹 Slower than AES
> 
> 
> 
> #### 🔹 Conservative approach with many rounds
> 
>
> ---
>
> ### 📍 Page 9
>
> 
> #### 🔹 1.4.9 TEA (Tiny Encryption Algorithm)
> 
> 
> 
> #### 🔹 TEA Specifications:
> 
> 
> 
> #### 🔹 Key size: 128 bits
> 
> 
> 
> #### 🔹 Block size: 64 bits
> 
> 
> 
> #### 🔹 Rounds: 64 32 cycles)
> 
> 
> 
> #### 🔹 Issues:
> 
> 
> 
> #### 🔹 Susceptible to related-key attacks
> 
> 
> 
> #### 🔹 Equivalent keys problem
> 
> 
> 
> #### 🔹 Do not use for new applications
> 
> 
> 
> #### 🔹 1.4.10 CAST-128
> 
> 
> 
> #### 🔹 CAST128 Specifications:
> 
> 
> 
> #### 🔹 Key size: 40128 bits
> 
> 
> 
> #### 🔹 Block size: 64 bits
> 
> 
> 
> #### 🔹 Used in: Some PGP implementations
> 
> 
> 
> #### 🔹 1.4.11 GOST Block Cipher
> 
> 
> 
> #### 🔹 GOST Specifications:
> 
> 
> 
> #### 🔹 Key size: 256 bits
> 
> 
> 
> #### 🔹 Block size: 64 bits
> 
> 
> 
> #### 🔹 Standard: Russian encryption standard
> 
> 
> 
> #### 🔹 Issues:
> 
> 
> 
> #### 🔹 Several insecure implementations exist
> 
> 
> 
> #### 🔹 Varied security across versions
> 
> 
> 
> #### 🔹 1.4.12 Camellia
> 
> 
> 
> #### 🔹 Camellia Specifications:
> 
> 
> 
> #### 🔹 Key size: 128, 192, or 256 bits
> 
> 
> 
> #### 🔹 Block size: 128 bits
> 
> 
> 
> #### 🔹 Performance: Comparable to AES
> 
>
> ---
>
> ### 📍 Page 10
>
> 
> #### 🔹 Status: Secure, ISO/IEC standardized
> 
> 
> 
> #### 🔹 Characteristics:
> 
> 
> 
> #### 🔹 Similar security to AES
> 
> 
> 
> #### 🔹 Used in TLS/SSL
> 
> 
> 
> #### 🔹 Popular in Japan
> 
> 
> 
> #### 🔹 1.4.13 ChaCha20
> 
> 
> 
> #### 🔹 ChaCha20 Specifications:
> 
> 
> 
> #### 🔹 Type: Stream cipher
> 
> 
> 
> #### 🔹 Key size: 256 bits
> 
> 
> 
> #### 🔹 Status: Modern, secure alternative to AES
> 
> 
> 
> #### 🔹 Advantages:
> 
> 
> 
> #### 🔹 Excellent software performance
> 
> 
> 
> #### 🔹 Resistant to timing attacks
> 
> 
> 
> #### 🔹 Used in TLS 1.3
> 
> 
> 
> #### 🔹 Google's alternative to RC4
> 
> 
> 
> #### 🔹 1.5 Asymmetric Encryption Algorithms
> 
> 
> 
> #### 🔹 🔐Asymmetric Encryption Public-Key Cryptography)
> 
> 
> Uses mathematically related key pairs: public key for encryption, private key for decryption. Slower than symmetric but solves key distribution problem.
> 
> 
> #### 🔹 Characteristics:
> 
> 
> 
> #### 🔹 Public key (shareable)
> 
> 
> 
> #### 🔹 Private key (kept secret)
> 
> 
> Mathematically related but computationally infeasible to derive private from
> 
> 
> #### 🔹 public
> 
> 
> 
> #### 🔹 Used for key exchange and digital signatures
> 
>
> ---
>

> [!NOTE]- 📄 **Pages 11 to 15 Syllabus Content**
>
> ### 📍 Page 11
>
> 
> #### 🔹 Much slower than symmetric encryption
> 
> 
> 
> #### 🔹 Common Use:
> 
> 
> 
> #### 🔹 Encrypt symmetric key with public key
> 
> 
> 
> #### 🔹 Decrypt symmetric key with private key
> 
> 
> Use symmetric key for bulk data encryption (hybrid cryptosystem)
> 
> 
> #### 🔹 1.5.1 DSA (Digital Signature Algorithm)
> 
> 
> 
> #### 🔹 DSA Purpose:
> 
> 
> 
> #### 🔹 Digital signatures only (not encryption)
> 
> 
> 
> #### 🔹 Authentication
> 
> 
> 
> #### 🔹 Non-repudiation
> 
> 
> 
> #### 🔹 DSA Specifications:
> 
> 
> 
> #### 🔹 Key sizes: 1024, 2048, or 3072 bits
> 
> 
> 
> #### 🔹 Used in: SSH, PGP, SSL/TLS
> 
> 
> 
> #### 🔹 1.5.2 RSA (Rivest-Shamir-Adleman)
> 
> 
> 
> #### 🔹 🔑RSA  Most Widely Used Asymmetric Algorithm
> 
> 
> RSA supports both encryption and digital signatures, based on the mathematical difficulty of factoring large prime numbers.
> 
> 
> #### 🔹 RSA Specifications:
> 
> 
> 
> #### 🔹 Key sizes: 10244096 bits 2048 recommended)
> 
> 
> 
> #### 🔹 Security basis: Integer factorization problem
> 
> 
> 
> #### 🔹 Uses: Encryption, signing, key exchange
> 
> 
> 
> #### 🔹 RSA Key Sizes:
> 
> 
> 
> #### 🔹 1024-bit: Deprecated (vulnerable)
> 
> 
> 
> #### 🔹 2048-bit: Current minimum standard
> 
> 
> 
> #### 🔹 3072-bit: Equivalent to AES128 security
> 
> 
> 
> #### 🔹 4096-bit: High security applications
> 
>
> ---
>
> ### 📍 Page 12
>
> 
> #### 🔹 RSA Applications:
> 
> 
> 
> #### 🔹 SSL/TLS certificates
> 
> 
> 
> #### 🔹 SSH authentication
> 
> 
> 
> #### 🔹 PGP/GPG email encryption
> 
> 
> 
> #### 🔹 Code signing
> 
> 
> 
> #### 🔹 Digital signatures
> 
> 
> 
> #### 🔹 RSA Weakness:
> 
> 
> 
> #### 🔹 Vulnerable to quantum computing Shor's algorithm)
> 
> 
> 
> #### 🔹 1.5.3 Diffie-Hellman Key Exchange
> 
> 
> 
> #### 🔹 🤝Diffie-Hellman
> 
> 
> Algorithm allowing two parties to establish a shared secret over an insecure channel without prior secrets.
> 
> 
> #### 🔹 Purpose:
> 
> 
> 
> #### 🔹 Secure key exchange
> 
> 
> 
> #### 🔹 Establish shared secret
> 
> 
> 
> #### 🔹 Foundation for many protocols
> 
> 
> 
> #### 🔹 Vulnerability:
> 
> 
> 
> #### 🔹 Man-in-the-Middle MITM if not authenticated
> 
> 
> Solution: Combine with authentication (certificates, signatures)
> 
> 
> #### 🔹 Variants:
> 
> 
> 
> #### 🔹 Static Diffie-Hellman: Fixed keys
> 
> 
> Ephemeral Diffie-Hellman DHE/ECDHE Temporary keys for forward
> 
> 
> #### 🔹 secrecy
> 
> 
> 
> #### 🔹 1.5.4 Elliptic Curve Cryptography (ECC)
> 
>
> ---
>
> ### 📍 Page 13
>
> 
> #### 🔹 📈ECC  Modern High-Efficiency Cryptography
> 
> 
> Provides equivalent security to RSA with much smaller key sizes, ideal for mobile devices and IoT.
> 
> 
> #### 🔹 ECC Advantages:
> 
> 
> 
> #### 🔹 Smaller keys: 256-bit ECC  3072-bit RSA
> 
> 
> 
> #### 🔹 Faster: Less computational overhead
> 
> 
> 
> #### 🔹 Lower power consumption
> 
> 
> 
> #### 🔹 Smaller certificates
> 
> 
> 
> #### 🔹 Security Comparison:
> 
> 
> 
> #### 🔹 256-bit ECC = 3072-bit RSA = 128-bit AES
> 
> 
> 
> #### 🔹 384-bit ECC = 7680-bit RSA = 192-bit AES
> 
> 
> 
> #### 🔹 Popular Curves:
> 
> 
> 
> #### 🔹 Curve25519 Modern, secure, fast
> 
> 
> 
> #### 🔹 secp256r1 P256 NIST standard
> 
> 
> 
> #### 🔹 secp384r1 P384 Higher security
> 
> 
> 
> #### 🔹 Ed25519 EdDSA signature scheme
> 
> 
> 
> #### 🔹 ECC Use Cases:
> 
> 
> 
> #### 🔹 Mobile devices
> 
> 
> 
> #### 🔹 IoT devices
> 
> 
> 
> #### 🔹 Modern TLS ECDHE
> 
> 
> 
> #### 🔹 Cryptocurrency Bitcoin, Ethereum)
> 
> 
> 
> #### 🔹 SSH (ed25519 keys)
> 
> 
> 
> #### 🔹 ECC Weakness:
> 
> 
> 
> #### 🔹 Also vulnerable to quantum computing
> 
> 
> 
> #### 🔹 1.5.5 YAK Protocol
> 
> 
> 
> #### 🔹 YAK Yet Another Key Agreement Protocol):
> 
> 
> 
> #### 🔹 Authenticated Diffie-Hellman variant
> 
>
> ---
>
> ### 📍 Page 14
>
> 
> #### 🔹 Prevents man-in-the-middle attacks
> 
> 
> 
> #### 🔹 Provides mutual authentication
> 
> 
> 
> #### 🔹 1.6 Hash Functions
> 
> 
> 
> #### 🔹 󾠬Cryptographic Hash Functions
> 
> 
> One-way mathematical functions that convert input of any size into fixed-size output (digest/hash), used for integrity verification.
> 
> 
> #### 🔹 Hash Function Properties:
> 
> 
> 
> #### 🔹 Deterministic
> 
> 
> 
> #### 🔹 Same input always produces same hash
> 
> 
> 
> #### 🔹 Fast Computation
> 
> 
> 
> #### 🔹 Quick to calculate hash
> 
> 
> 
> #### 🔹 Pre-image Resistance
> 
> 
> 
> #### 🔹 Infeasible to reverse hash to original input
> 
> 
> 
> #### 🔹 Small Change  Large Difference
> 
> 
> 
> #### 🔹 Avalanche effect (one bit change affects entire hash)
> 
> 
> 
> #### 🔹 Collision Resistance
> 
> 
> 
> #### 🔹 Infeasible to find two inputs with same hash
> 
> 
> 
> #### 🔹 Fixed Output Size
> 
> 
> 
> #### 🔹 Hash length constant regardless of input size
> 
> 
> 
> #### 🔹 1.6.1 MD5 (Message Digest 5)
> 
> 
> 
> #### 🔹 ❌MD5  BROKEN
> 
> 
> MD5 is cryptographically broken with practical collision attacks. Do not use for any security purpose.
> 
> 
> #### 🔹 MD5 Specifications:
> 
> 
> 
> #### 🔹 Output: 128 bits 32 hex characters)
> 
>
> ---
>
> ### 📍 Page 15
>
> 
> #### 🔹 Status: BROKEN
> 
> 
> 
> #### 🔹 Collision attacks: Practical since 2004
> 
> 
> 
> #### 🔹 Use case: Checksums only (not security)
> 
> 
> 
> #### 🔹 Why MD5 Failed:
> 
> 
> Collision attacks (create two different files with same hash)
> 
> 
> #### 🔹 Not suitable for certificates, passwords, or integrity
> 
> 
> 
> #### 🔹 MD6
> 
> 
> 
> #### 🔹 Designed as MD5 successor
> 
> 
> 
> #### 🔹 Never standardized
> 
> 
> 
> #### 🔹 Deprecated
> 
> 
> 
> #### 🔹 1.6.2 Secure Hash Algorithms (SHA Family)
> 
> 
> 
> #### 🔹 SHA0 1993
> 
> 
> 
> #### 🔹 Output: 160 bits
> 
> 
> 
> #### 🔹 Status: Withdrawn before release
> 
> 
> 
> #### 🔹 SHA1 1995
> 
> 
> 
> #### 🔹 ⚠SHA1  DEPRECATED
> 
> 
> SHA1 is broken with practical collision attacks. Deprecated for digital signatures and certificates since 2017.
> 
> 
> #### 🔹 Output: 160 bits
> 
> 
> 
> #### 🔹 Status: BROKEN (collision attack 2017
> 
> 
> 
> #### 🔹 Do not use
> 
> 
> 
> #### 🔹 SHA2 Family Current Standard)
> 
> 
> 
> #### 🔹 ✅SHA2  Current Standard
> 
> 
> SHA2 family SHA256, SHA384, SHA512 is the current secure standard for cryptographic hashing.
>
> ---
>

> [!NOTE]- 📄 **Pages 16 to 20 Syllabus Content**
>
> ### 📍 Page 16
>
> 
> #### 🔹 SHA224
> 
> 
> 
> #### 🔹 Output: 224 bits
> 
> 
> 
> #### 🔹 Use: Truncated SHA256
> 
> 
> 
> #### 🔹 SHA256
> 
> 
> 
> #### 🔹 Output: 256 bits
> 
> 
> 
> #### 🔹 Most common
> 
> 
> 
> #### 🔹 Used in: TLS, Bitcoin, certificates
> 
> 
> 
> #### 🔹 SHA384
> 
> 
> 
> #### 🔹 Output: 384 bits
> 
> 
> 
> #### 🔹 Use: Truncated SHA512
> 
> 
> 
> #### 🔹 SHA512
> 
> 
> 
> #### 🔹 Output: 512 bits
> 
> 
> 
> #### 🔹 Use: High-security applications
> 
> 
> 
> #### 🔹 SHA2 Applications:
> 
> 
> 
> #### 🔹 Digital signatures
> 
> 
> 
> #### 🔹 SSL/TLS certificates
> 
> 
> 
> #### 🔹 Password storage (with salt)
> 
> 
> 
> #### 🔹 Blockchain
> 
> 
> 
> #### 🔹 File integrity verification
> 
> 
> 
> #### 🔹 SHA3 Keccak)  2015
> 
> 
> 
> #### 🔹 SHA3 Family:
> 
> 
> 
> #### 🔹 SHA3224, SHA3256, SHA3384, SHA3512
> 
> 
> 
> #### 🔹 Different internal structure from SHA2
> 
> 
> 
> #### 🔹 Not replacing SHA2, but alternative
> 
> 
> 
> #### 🔹 Status: Secure, modern standard
> 
> 
> 
> #### 🔹 SHA3 Advantages:
> 
> 
> 
> #### 🔹 Different design (sponge construction)
> 
> 
> 
> #### 🔹 Resistant to length-extension attacks
> 
>
> ---
>
> ### 📍 Page 17
>
> 
> #### 🔹 Future-proof alternative
> 
> 
> 
> #### 🔹 1.6.3 RIPEMD-160
> 
> 
> 
> #### 🔹 RIPEMD160 Specifications:
> 
> 
> 
> #### 🔹 Output: 160 bits
> 
> 
> 
> #### 🔹 Status: Secure against known attacks
> 
> 
> 
> #### 🔹 Used in: Bitcoin address generation
> 
> 
> 
> #### 🔹 Less common than SHA family
> 
> 
> 
> #### 🔹 1.6.4 HMAC (Hash-Based Message Authentication Code)
> 
> 
> 
> #### 🔹 🔐HMAC
> 
> 
> 
> #### 🔹 Keyed cryptographic hash providing both data integrity and
> 
> 
> authentication using a secret key with a hash function.
> 
> 
> #### 🔹 HMAC Purpose:
> 
> 
> 
> #### 🔹 Message authentication
> 
> 
> 
> #### 🔹 Integrity verification
> 
> 
> 
> #### 🔹 Authenticated encryption
> 
> 
> 
> #### 🔹 HMAC Construction:
> 
> 
> 
> #### 🔹 HMACK, m)  H(K ⊕ opad) || HK ⊕ ipad) || m))
> 
> 
> 
> #### 🔹 Common Variants:
> 
> 
> 
> #### 🔹 HMACMD5 (legacy)
> 
> 
> 
> #### 🔹 HMACSHA1 (legacy)
> 
> 
> 
> #### 🔹 HMACSHA256 (recommended)
> 
> 
> 
> #### 🔹 HMACSHA512 (high security)
> 
> 
> 
> #### 🔹 HMAC Applications:
> 
> 
> 
> #### 🔹 TLS/SSL
> 
> 
> 
> #### 🔹 IPsec
> 
>
> ---
>
> ### 📍 Page 18
>
> 
> #### 🔹 JWT JSON Web Tokens)
> 
> 
> 
> #### 🔹 API authentication
> 
> 
> 
> #### 🔹 Message authentication
> 
> 
> 
> #### 🔹 1.6.5 CHAP (Challenge-Handshake Authentication Protocol)
> 
> 
> 
> #### 🔹 CHAP Authentication:
> 
> 
> 
> #### 🔹 Uses one-way hash for authentication
> 
> 
> 
> #### 🔹 Challenge-response mechanism
> 
> 
> 
> #### 🔹 Periodic re-authentication
> 
> 
> 
> #### 🔹 Used in PPP connections
> 
> 
> 
> #### 🔹 1.6.6 EAP (Extensible Authentication Protocol)
> 
> 
> 
> #### 🔹 EAP Framework:
> 
> 
> 
> #### 🔹 Authentication framework
> 
> 
> 
> #### 🔹 Used in wireless networks WPA/WPA2Enterprise)
> 
> 
> 
> #### 🔹 Point-to-point connections
> 
> 
> 
> #### 🔹 Multiple EAP methods EAPTLS, EAPTTLS, PEAP
> 
> 
> 
> #### 🔹 1.6.7 GOST Hash Function
> 
> 
> 
> #### 🔹 GOST R 34.1194
> 
> 
> 
> #### 🔹 Output: 256 bits
> 
> 
> 
> #### 🔹 Standard: Russian national standard
> 
> 
> 
> #### 🔹 Status: Secure
> 
> 
> 
> #### 🔹 1.6.8 Hash Calculation Tools
> 
> 
> 
> #### 🔹 Command-Line Tools:
> 
> 
> 
> #### 🔹 Linux/macOS
> 
> 
> 
> #### 🔹 # MD5
> 
> 
> 
> #### 🔹 md5sum file.txt
> 
> 
> 
> #### 🔹 md5 file.txt
> 
>
> ---
>
> ### 📍 Page 19
>
> 
> #### 🔹 # SHA256
> 
> 
> 
> #### 🔹 sha256sum file.txt
> 
> 
> 
> #### 🔹 shasum -a 256 file.txt
> 
> 
> 
> #### 🔹 # SHA512
> 
> 
> 
> #### 🔹 sha512sum file.txt
> 
> 
> 
> #### 🔹 Windows:
> 
> 
> 
> #### 🔹 # CertUtil
> 
> 
> 
> #### 🔹 certutil -hashfile file.txt MD5
> 
> 
> 
> #### 🔹 certutil -hashfile file.txt SHA256
> 
> 
> 
> #### 🔹 certutil -hashfile file.txt SHA512
> 
> 
> 
> #### 🔹 GUI Tools:
> 
> 
> 
> #### 🔹 HashCalc Windows)
> 
> 
> 
> #### 🔹 HashTab Windows Explorer integration)
> 
> 
> 
> #### 🔹 md5deep / hashdeep Cross-platform)
> 
> 
> 
> #### 🔹 Online Hash Calculators:
> 
> 
> 
> #### 🔹 Hash ToolKit
> 
> 
> 
> #### 🔹 Online Hash Crack
> 
> 
> 
> #### 🔹 Various online tools (not recommended for sensitive data)
> 
> 
> 
> #### 🔹 1.7 Hardware-Based Encryption
> 
> 
> 
> #### 🔹 🔐Hardware Security Modules
> 
> 
> Dedicated physical devices providing tamper-resistant cryptographic processing and secure key storage.
> 
> 
> #### 🔹 Hardware Encryption Solutions:
> 
> 
> 
> #### 🔹 TPM (Trusted Platform Module)
> 
> 
> 
> #### 🔹 TPM Specifications:
> 
> 
> 
> #### 🔹 Dedicated crypto processor
> 
>
> ---
>
> ### 📍 Page 20
>
> 
> #### 🔹 Secure key storage
> 
> 
> 
> #### 🔹 Hardware random number generator
> 
> 
> 
> #### 🔹 Platform integrity measurement
> 
> 
> 
> #### 🔹 TPM Uses:
> 
> 
> 
> #### 🔹 BitLocker encryption
> 
> 
> 
> #### 🔹 Measured boot
> 
> 
> 
> #### 🔹 Credential protection
> 
> 
> 
> #### 🔹 Device attestation
> 
> 
> 
> #### 🔹 HSM (Hardware Security Module)
> 
> 
> 
> #### 🔹 HSM Characteristics:
> 
> 
> 
> #### 🔹 Physical tamper-resistant device
> 
> 
> 
> #### 🔹 High-performance cryptographic operations
> 
> 
> 
> #### 🔹 Secure key generation and storage
> 
> 
> 
> #### 🔹 FIPS 1402 Level 3/4 compliance
> 
> 
> 
> #### 🔹 HSM Use Cases:
> 
> 
> 
> #### 🔹 Certificate authorities
> 
> 
> 
> #### 🔹 Payment processing
> 
> 
> 
> #### 🔹 Database encryption
> 
> 
> 
> #### 🔹 PKI operations
> 
> 
> 
> #### 🔹 Smart Cards
> 
> 
> 
> #### 🔹 Smart Card Features:
> 
> 
> 
> #### 🔹 Embedded microprocessor
> 
> 
> 
> #### 🔹 Cryptographic capabilities
> 
> 
> 
> #### 🔹 Secure key storage
> 
> 
> 
> #### 🔹 PIN protection
> 
> 
> 
> #### 🔹 Applications:
> 
> 
> 
> #### 🔹 Physical access control
> 
>
> ---
>

> [!NOTE]- 📄 **Pages 21 to 25 Syllabus Content**
>
> ### 📍 Page 21
>
> 
> #### 🔹 Two-factor authentication
> 
> 
> 
> #### 🔹 Digital signatures
> 
> 
> 
> #### 🔹 Payment cards EMV
> 
> 
> 
> #### 🔹 Secure Enclaves
> 
> 
> 
> #### 🔹 Secure Enclave Technologies:
> 
> 
> 
> #### 🔹 Intel SGX Software Guard Extensions)
> 
> 
> 
> #### 🔹 Isolated execution environment
> 
> 
> 
> #### 🔹 Memory encryption
> 
> 
> 
> #### 🔹 Attestation capabilities
> 
> 
> 
> #### 🔹 ARM TrustZone
> 
> 
> 
> #### 🔹 Secure world vs normal world
> 
> 
> 
> #### 🔹 Hardware isolation
> 
> 
> 
> #### 🔹 Mobile device security
> 
> 
> 
> #### 🔹 Apple Secure Enclave
> 
> 
> 
> #### 🔹 Biometric data protection
> 
> 
> 
> #### 🔹 Key storage
> 
> 
> 
> #### 🔹 Secure boot
> 
> 
> 
> #### 🔹 1.8 Quantum Cryptography
> 
> 
> 
> #### 🔹 ⚛Quantum Cryptography
> 
> 
> Cryptographic systems using quantum mechanical properties for secure communication, offering theoretically unbreakable encryption.
> 
> 
> #### 🔹 Quantum Key Distribution (QKD)
> 
> 
> 
> #### 🔹 QKD Principles:
> 
> 
> 
> #### 🔹 Heisenberg Uncertainty Principle
> 
> 
> 
> #### 🔹 Observation changes quantum state
> 
> 
> 
> #### 🔹 Quantum Entanglement
> 
>
> ---
>
> ### 📍 Page 22
>
> 
> #### 🔹 Correlated particle pairs
> 
> 
> 
> #### 🔹 No-Cloning Theorem
> 
> 
> 
> #### 🔹 Cannot copy unknown quantum state
> 
> 
> 
> #### 🔹 QKD Security:
> 
> 
> 
> #### 🔹 Any interception disturbs quantum states
> 
> 
> 
> #### 🔹 Eavesdropping is detectable
> 
> 
> 
> #### 🔹 Theoretically unbreakable
> 
> 
> 
> #### 🔹 QKD Protocols:
> 
> 
> 
> #### 🔹 BB84 First QKD protocol
> 
> 
> 
> #### 🔹 E91 Entanglement-based
> 
> 
> 
> #### 🔹 SARG04 Improved BB84
> 
> 
> 
> #### 🔹 QKD Limitations:
> 
> 
> 
> #### 🔹 Distance limitations
> 
> 
> 
> #### 🔹 Expensive infrastructure
> 
> 
> 
> #### 🔹 Requires dedicated fiber
> 
> 
> 
> #### 🔹 Not yet widely deployed
> 
> 
> 
> #### 🔹 1.9 Other Encryption Techniques
> 
> 
> 
> #### 🔹 Homomorphic Encryption
> 
> 
> 
> #### 🔹 🔢Homomorphic Encryption
> 
> 
> Allows computation on encrypted data without decrypting it, enabling secure cloud processing.
> 
> 
> #### 🔹 Types:
> 
> 
> 
> #### 🔹 Partially Homomorphic: Limited operations
> 
> 
> 
> #### 🔹 Somewhat Homomorphic: Limited depth
> 
> 
> 
> #### 🔹 Fully Homomorphic: Any computation
> 
> 
> 
> #### 🔹 Use Cases:
> 
>
> ---
>
> ### 📍 Page 23
>
> 
> #### 🔹 Privacy-preserving cloud computing
> 
> 
> 
> #### 🔹 Secure machine learning
> 
> 
> 
> #### 🔹 Private information retrieval
> 
> 
> 
> #### 🔹 Encrypted database queries
> 
> 
> 
> #### 🔹 Steganographic Encryption
> 
> 
> 
> #### 🔹 Steganography:
> 
> 
> 
> #### 🔹 Hide encrypted data within other files
> 
> 
> 
> #### 🔹 Combines encryption with steganography
> 
> 
> 
> #### 🔹 Images, audio, video, text
> 
> 
> 
> #### 🔹 Tools:
> 
> 
> 
> #### 🔹 OpenStego
> 
> 
> 
> #### 🔹 Steghide
> 
> 
> 
> #### 🔹 OutGuess
> 
> 
> 
> #### 🔹 Format-Preserving Encryption (FPE)
> 
> 
> 
> #### 🔹 FPE Characteristics:
> 
> 
> 
> #### 🔹 Encrypted data maintains original format
> 
> 
> 
> #### 🔹 Useful for legacy systems
> 
> 
> 
> #### 🔹 Database compatibility
> 
> 
> 
> #### 🔹 Example:
> 
> 
> 
> #### 🔹 Credit card: 1234567890123456
> 
> 
> 
> #### 🔹 Encrypted: 8901234567890123 (same format)
> 
> 
> 
> #### 🔹 1.10 Cipher Modes of Operation
> 
> 
> 
> #### 🔹 🔄Block Cipher Modes
> 
> 
> Methods for encrypting data larger than a single block, each with different security properties and use cases.
>
> ---
>
> ### 📍 Page 24
>
> 
> #### 🔹 Mode Comparison Table
> 
> 
> 
> #### 🔹 Mode Description IV Required Parallelizable Security
> 
> 
> 
> #### 🔹 ECB
> 
> 
> 
> #### 🔹 Encrypt each
> 
> 
> 
> #### 🔹 block
> 
> 
> 
> #### 🔹 independently
> 
> 
> 
> #### 🔹 No Yes Insecure – do
> 
> 
> 
> #### 🔹 not use
> 
> 
> 
> #### 🔹 CBC
> 
> 
> 
> #### 🔹 Chain blocks
> 
> 
> 
> #### 🔹 with XOR and
> 
> 
> 
> #### 🔹 IV
> 
> 
> 
> #### 🔹 Yes (random) No (encryption)Secure if IV is
> 
> 
> 
> #### 🔹 random
> 
> 
> 
> #### 🔹 CFB
> 
> 
> 
> #### 🔹 Convert block
> 
> 
> 
> #### 🔹 cipher to
> 
> 
> 
> #### 🔹 stream
> 
> 
> 
> #### 🔹 Yes No Secure, self-
> 
> 
> 
> #### 🔹 synchronizing
> 
> 
> 
> #### 🔹 OFB Output
> 
> 
> 
> #### 🔹 feedback modeYes (unique) No Secure if IV
> 
> 
> 
> #### 🔹 unique
> 
> 
> 
> #### 🔹 CTR Counter mode Yes (nonce) Yes Secure, fast,
> 
> 
> 
> #### 🔹 parallel
> 
> 
> 
> #### 🔹 ECB (Electronic Codebook) Mode
> 
> 
> 
> #### 🔹 ❌ECB  INSECURE
> 
> 
> Do not use ECB mode. Identical plaintext blocks produce identical ciphertext blocks, revealing patterns.
> 
> 
> #### 🔹 ECB Problems:
> 
> 
> 
> #### 🔹 No diffusion across blocks
> 
> 
> 
> #### 🔹 Patterns visible
> 
> 
> 
> #### 🔹 Deterministic
> 
> 
> 
> #### 🔹 Vulnerable to known plaintext attacks
> 
> 
> 
> #### 🔹 Famous Example:
> 
> 
> 
> #### 🔹 ECB-encrypted images show original patterns
> 
> 
> 
> #### 🔹 CBC (Cipher Block Chaining) Mode
> 
> 
> 
> #### 🔹 CBC Operation:
> 
> 
> 
> #### 🔹  XOR plaintext block with previous ciphertext (or IV
> 
> 
> 
> #### 🔹 2 4
> 
>
> ---
>
> ### 📍 Page 25
>
> 
> #### 🔹  Encrypt result
> 
> 
> 
> #### 🔹  Output becomes next IV
> 
> 
> 
> #### 🔹 CBC Requirements:
> 
> 
> 
> #### 🔹 Random IV for each message
> 
> 
> 
> #### 🔹 Unique IV prevents pattern detection
> 
> 
> 
> #### 🔹 CBC Vulnerabilities:
> 
> 
> 
> #### 🔹 Padding oracle attack if padding not validated properly
> 
> 
> 
> #### 🔹 BEAST attack on SSL/TLS (mitigated)
> 
> 
> 
> #### 🔹 CBC Use Cases:
> 
> 
> 
> #### 🔹 File encryption
> 
> 
> 
> #### 🔹 Disk encryption (with ESSIV
> 
> 
> 
> #### 🔹 Historical TLS versions
> 
> 
> 
> #### 🔹 CFB (Cipher Feedback) Mode
> 
> 
> 
> #### 🔹 CFB Characteristics:
> 
> 
> 
> #### 🔹 Converts block cipher to stream cipher
> 
> 
> 
> #### 🔹 Self-synchronizing
> 
> 
> 
> #### 🔹 Error propagation limited
> 
> 
> 
> #### 🔹 OFB (Output Feedback) Mode
> 
> 
> 
> #### 🔹 OFB Characteristics:
> 
> 
> 
> #### 🔹 Stream cipher mode
> 
> 
> 
> #### 🔹 No error propagation
> 
> 
> 
> #### 🔹 Must not reuse IV
> 
> 
> 
> #### 🔹 CTR (Counter) Mode
> 
> 
> 
> #### 🔹 CTR Advantages:
> 
> 
> 
> #### 🔹 Parallelizable encryption and decryption
> 
> 
> 
> #### 🔹 Random access
> 
> 
> 
> #### 🔹 No padding needed
> 
>
> ---
>

> [!NOTE]- 📄 **Pages 26 to 30 Syllabus Content**
>
> ### 📍 Page 26
>
> 
> #### 🔹 Fast performance
> 
> 
> 
> #### 🔹 CTR Requirements:
> 
> 
> 
> #### 🔹 Unique nonce for each message
> 
> 
> 
> #### 🔹 Never reuse nonce with same key
> 
> 
> 
> #### 🔹 CTR Use Cases:
> 
> 
> 
> #### 🔹 Disk encryption
> 
> 
> 
> #### 🔹 IPsec
> 
> 
> 
> #### 🔹 High-performance applications
> 
> 
> 
> #### 🔹 1.11 Authenticated Encryption Modes
> 
> 
> 
> #### 🔹 🔒Authenticated Encryption with Associated Data AEAD
> 
> 
> Modes providing both confidentiality and authenticity, preventing unauthorized modification.
> 
> 
> #### 🔹 GCM (Galois/Counter Mode)
> 
> 
> 
> #### 🔹 GCM Characteristics:
> 
> 
> 
> #### 🔹 Most widely used AEAD mode
> 
> 
> 
> #### 🔹 Combines CTR mode encryption with GMAC authentication
> 
> 
> 
> #### 🔹 High performance
> 
> 
> 
> #### 🔹 Parallelizable
> 
> 
> 
> #### 🔹 GCM Components:
> 
> 
> 
> #### 🔹 Encryption: CTR mode
> 
> 
> 
> #### 🔹 Authentication: GMAC Galois MAC
> 
> 
> 
> #### 🔹 GCM Use Cases:
> 
> 
> 
> #### 🔹 TLS 1.2/1.3 (primary mode)
> 
> 
> 
> #### 🔹 IPsec
> 
> 
> 
> #### 🔹 SSH
> 
> 
> 
> #### 🔹 Disk encryption
> 
>
> ---
>
> ### 📍 Page 27
>
> 
> #### 🔹 GCM Requirements:
> 
> 
> 
> #### 🔹 Never reuse nonce with same key
> 
> 
> 
> #### 🔹 Nonce reuse catastrophic
> 
> 
> 
> #### 🔹 Other AEAD Modes
> 
> 
> 
> #### 🔹 EAX Mode
> 
> 
> 
> #### 🔹 Simple design
> 
> 
> 
> #### 🔹 Patent-free
> 
> 
> 
> #### 🔹 Two-pass operation
> 
> 
> 
> #### 🔹 CCM Counter with CBCMAC
> 
> 
> 
> #### 🔹 Used in WPA2, IEEE 802.11i
> 
> 
> 
> #### 🔹 Two-pass operation
> 
> 
> 
> #### 🔹 Pre-computed message length
> 
> 
> 
> #### 🔹 OCB Offset Codebook)
> 
> 
> 
> #### 🔹 Single-pass
> 
> 
> 
> #### 🔹 Very fast
> 
> 
> 
> #### 🔹 Patent concerns (now expired)
> 
> 
> 
> #### 🔹 ChaCha20Poly1305
> 
> 
> 
> #### 🔹 Stream cipher  MAC
> 
> 
> 
> #### 🔹 Used in TLS 1.3
> 
> 
> 
> #### 🔹 Excellent software performance
> 
> 
> 
> #### 🔹 1.12 Cryptography Tools
> 
> 
> 
> #### 🔹 Encryption Software:
> 
> 
> 
> #### 🔹 OpenSSL
> 
> 
> 
> #### 🔹 Comprehensive crypto library
> 
> 
> 
> #### 🔹 Command-line tool
> 
> 
> 
> #### 🔹 Certificate management
> 
> 
> 
> #### 🔹 Widely used
> 
>
> ---
>
> ### 📍 Page 28
>
> 
> #### 🔹 # Symmetric encryption
> 
> 
> 
> #### 🔹 openssl enc -aes-256-cbc -in file.txt -out file.enc
> 
> 
> 
> #### 🔹 openssl enc -aes-256-cbc -d -in file.enc -out file.txt
> 
> 
> 
> #### 🔹 # Generate keys
> 
> 
> 
> #### 🔹 openssl genrsa -out private.pem 2048
> 
> 
> 
> #### 🔹 openssl rsa -in private.pem -pubout -out public.pem
> 
> 
> 
> #### 🔹 # Hash files
> 
> 
> 
> #### 🔹 openssl dgst -sha256 file.txt
> 
> 
> 
> #### 🔹 GPG/PGP
> 
> 
> 
> #### 🔹 Email encryption
> 
> 
> 
> #### 🔹 File signing
> 
> 
> 
> #### 🔹 Web of trust
> 
> 
> 
> #### 🔹 VeraCrypt
> 
> 
> 
> #### 🔹 Disk encryption
> 
> 
> 
> #### 🔹 Container creation
> 
> 
> 
> #### 🔹 Successor to TrueCrypt
> 
> 
> 
> #### 🔹 BitLocker Windows)
> 
> 
> 
> #### 🔹 Full disk encryption
> 
> 
> 
> #### 🔹 TPM integration
> 
> 
> 
> #### 🔹 Enterprise management
> 
> 
> 
> #### 🔹 FileVault (macOS
> 
> 
> 
> #### 🔹 Full disk encryption
> 
> 
> 
> #### 🔹 XTSAES128
> 
> 
> 
> #### 🔹 LUKS/dm-crypt Linux)
> 
> 
> 
> #### 🔹 Disk encryption
> 
> 
> 
> #### 🔹 Multiple key slots
> 
> 
> 
> #### 🔹 TrueCrypt
> 
>
> ---
>
> ### 📍 Page 29
>
> 
> #### 🔹 Deprecated – use VeraCrypt instead
> 
> 
> 
> #### 🔹 Development abandoned 2014
> 
> 
> 
> #### 🔹 Password Cracking:
> 
> 
> 
> #### 🔹 Hashcat
> 
> 
> 
> #### 🔹 GPU-accelerated
> 
> 
> 
> #### 🔹 300 hash types
> 
> 
> 
> #### 🔹 Dictionary, brute-force, hybrid attacks
> 
> 
> 
> #### 🔹 John the Ripper
> 
> 
> 
> #### 🔹 CPU-based
> 
> 
> 
> #### 🔹 Format detection
> 
> 
> 
> #### 🔹 Custom rules
> 
> 
> 
> #### 🔹 2. Public Key Infrastructure (PKI)
> 
> 
> 
> #### 🔹 2.1 Introduction to PKI
> 
> 
> 
> #### 🔹 🏛PKI Public Key Infrastructure)
> 
> 
> Framework of policies, procedures, hardware, software, and people to create, manage, distribute, use, store, and revoke digital certificates.
> 
> 
> #### 🔹 PKI Components:
> 
> 
> 
> #### 🔹 Certificate Authority CA
> 
> 
> 
> #### 🔹 Issues and manages digital certificates
> 
> 
> 
> #### 🔹 Registration Authority RA
> 
> 
> 
> #### 🔹 Verifies identity before certificate issuance
> 
> 
> 
> #### 🔹 Certificate Repository
> 
> 
> 
> #### 🔹 Stores and distributes certificates
> 
> 
> 
> #### 🔹 Certificate Revocation List CRL
> 
> 
> 
> #### 🔹 Lists revoked certificates
> 
>
> ---
>
> ### 📍 Page 30
>
> 
> #### 🔹 OCSP Online Certificate Status Protocol)
> 
> 
> 
> #### 🔹 Real-time certificate validation
> 
> 
> 
> #### 🔹 End Entities
> 
> 
> 
> #### 🔹 Users and devices with certificates
> 
> 
> 
> #### 🔹 Certificate Policies
> 
> 
> 
> #### 🔹 Rules governing PKI operations
> 
> 
> 
> #### 🔹 2.2 Certification Authorities (CAs)
> 
> 
> 
> #### 🔹 CA Hierarchy:
> 
> 
> 
> #### 🔹 Root CA
> 
> 
> 
> #### 🔹 Top of trust chain
> 
> 
> 
> #### 🔹 Self-signed certificate
> 
> 
> 
> #### 🔹 Offline and highly secure
> 
> 
> 
> #### 🔹 Intermediate CA
> 
> 
> 
> #### 🔹 Subordinate to Root CA
> 
> 
> 
> #### 🔹 Issues end-entity certificates
> 
> 
> 
> #### 🔹 Can be revoked without affecting root
> 
> 
> 
> #### 🔹 CA Responsibilities:
> 
> 
> 
> #### 🔹 Identity verification
> 
> 
> 
> #### 🔹 Certificate issuance
> 
> 
> 
> #### 🔹 Certificate revocation
> 
> 
> 
> #### 🔹 CRL/OCSP management
> 
> 
> 
> #### 🔹 X.509 Digital Certificates
> 
> 
> 
> #### 🔹 X.509 Certificate Contents:
> 
> 
> 
> #### 🔹 Version: X.509 v3
> 
> 
> 
> #### 🔹 Serial Number: Unique identifier
> 
> 
> 
> #### 🔹 Signature Algorithm: Algorithm used to sign
> 
> 
> 
> #### 🔹 Issuer: CA identity
> 
>
> ---
>

> [!NOTE]- 📄 **Pages 31 to 35 Syllabus Content**
>
> ### 📍 Page 31
>
> 
> #### 🔹 Validity Period: Not before / not after dates
> 
> 
> 
> #### 🔹 Subject: Certificate holder identity
> 
> 
> 
> #### 🔹 Public Key: Subject's public key
> 
> 
> 
> #### 🔹 Extensions: Additional information
> 
> 
> 
> #### 🔹 Signature: CA's digital signature
> 
> 
> 
> #### 🔹 Certificate Types
> 
> 
> 
> #### 🔹 Signed Certificates CAIssued)
> 
> 
> 
> #### 🔹 Trusted by browsers
> 
> 
> 
> #### 🔹 Validated identity
> 
> 
> 
> #### 🔹 Chain of trust
> 
> 
> 
> #### 🔹 Used for public websites
> 
> 
> 
> #### 🔹 Self-Signed Certificates
> 
> 
> 
> #### 🔹 No CA validation
> 
> 
> 
> #### 🔹 Browser warnings
> 
> 
> 
> #### 🔹 Free but untrusted
> 
> 
> 
> #### 🔹 Used for development, internal systems
> 
> 
> 
> #### 🔹 Certificate Validation Levels:
> 
> 
> 
> #### 🔹 Domain Validated DV
> 
> 
> 
> #### 🔹 Proves domain control
> 
> 
> 
> #### 🔹 Automated issuance
> 
> 
> 
> #### 🔹 No organization validation
> 
> 
> 
> #### 🔹 Organization Validated OV
> 
> 
> 
> #### 🔹 Verifies organization identity
> 
> 
> 
> #### 🔹 Manual validation
> 
> 
> 
> #### 🔹 More trust
> 
> 
> 
> #### 🔹 Extended Validation EV
> 
> 
> 
> #### 🔹 Highest validation level
> 
>
> ---
>
> ### 📍 Page 32
>
> 
> #### 🔹 Rigorous verification
> 
> 
> 
> #### 🔹 Green address bar (legacy browsers)
> 
> 
> 
> #### 🔹 2.3 Digital Signatures
> 
> 
> 
> #### 🔹 ✍Digital Signatures
> 
> 
> Cryptographic technique providing authentication, integrity, and non- repudiation using asymmetric cryptography.
> 
> 
> #### 🔹 Digital Signature Process:
> 
> 
> 
> #### 🔹 Signing:
> 
> 
> 
> #### 🔹  Hash the message SHA256
> 
> 
> 
> #### 🔹  Encrypt hash with sender's private key
> 
> 
> 
> #### 🔹  Attach signature to message
> 
> 
> 
> #### 🔹 Verification:
> 
> 
> 
> #### 🔹  Decrypt signature with sender's public key
> 
> 
> 
> #### 🔹  Hash the received message
> 
> 
> 
> #### 🔹  Compare decrypted hash with calculated hash
> 
> 
> 
> #### 🔹  Match = authentic and unmodified
> 
> 
> 
> #### 🔹 Digital Signature Provides:
> 
> 
> 
> #### 🔹 Authentication
> 
> 
> 
> #### 🔹 Proves sender identity
> 
> 
> 
> #### 🔹 Integrity
> 
> 
> 
> #### 🔹 Detects any modification
> 
> 
> 
> #### 🔹 Non-Repudiation
> 
> 
> 
> #### 🔹 Sender cannot deny signing
> 
> 
> 
> #### 🔹 Signature Algorithms:
> 
> 
> 
> #### 🔹 RSA Most common
> 
> 
> 
> #### 🔹 DSA Digital Signature Algorithm
> 
>
> ---
>
> ### 📍 Page 33
>
> 
> #### 🔹 ECDSA Elliptic Curve DSA
> 
> 
> 
> #### 🔹 EdDSA Modern Ed25519
> 
> 
> 
> #### 🔹 Use Cases:
> 
> 
> 
> #### 🔹 Code signing
> 
> 
> 
> #### 🔹 Email signing S/MIME
> 
> 
> 
> #### 🔹 Document signing PDF
> 
> 
> 
> #### 🔹 Software updates
> 
> 
> 
> #### 🔹 Financial transactions
> 
> 
> 
> #### 🔹 2.4 SSL/TLS
> 
> 
> 
> #### 🔹 SSL (Secure Sockets Layer)
> 
> 
> 
> #### 🔹 ❌SSL  DEPRECATED
> 
> 
> All versions of SSL 1.0, 2.0, 3.0 are deprecated due to serious vulnerabilities. Do not use SSL.
> 
> 
> #### 🔹 SSL Vulnerabilities:
> 
> 
> 
> #### 🔹 POODLE SSLv3
> 
> 
> 
> #### 🔹 BEAST SSL/TLS 1.0
> 
> 
> 
> #### 🔹 CRIME (compression)
> 
> 
> 
> #### 🔹 Weak ciphers
> 
> 
> 
> #### 🔹 SSL History:
> 
> 
> 
> #### 🔹 SSL 1.0 Never released
> 
> 
> 
> #### 🔹 SSL 2.0 Released 1995, broken
> 
> 
> 
> #### 🔹 SSL 3.0 Released 1996, broken POODLE 2014
> 
> 
> 
> #### 🔹 TLS (Transport Layer Security)
> 
>
> ---
>
> ### 📍 Page 34
>
> 
> #### 🔹 ✅TLS  Current Standard
> 
> 
> 
> #### 🔹 TLS 1.2 minimum, TLS 1.3 strongly recommended for secure
> 
> 
> communication.
> 
> 
> #### 🔹 TLS Versions:
> 
> 
> 
> #### 🔹 TLS 1.0 1999
> 
> 
> 
> #### 🔹 Status: Deprecated 2020
> 
> 
> 
> #### 🔹 Vulnerable to BEAST
> 
> 
> 
> #### 🔹 TLS 1.1 2006
> 
> 
> 
> #### 🔹 Status: Deprecated 2020
> 
> 
> 
> #### 🔹 Limited improvements
> 
> 
> 
> #### 🔹 TLS 1.2 2008
> 
> 
> 
> #### 🔹 Status: Current minimum standard
> 
> 
> 
> #### 🔹 Strong cipher suites available
> 
> 
> 
> #### 🔹 Widely supported
> 
> 
> 
> #### 🔹 TLS 1.3 2018
> 
> 
> 
> #### 🔹 Status: Recommended
> 
> 
> 
> #### 🔹 Faster handshake 1RTT
> 
> 
> 
> #### 🔹 0RTT resumption
> 
> 
> 
> #### 🔹 Removed weak ciphers
> 
> 
> 
> #### 🔹 Mandatory forward secrecy
> 
> 
> 
> #### 🔹 Simplified design
> 
> 
> 
> #### 🔹 TLS 1.3 Improvements:
> 
> 
> 
> #### 🔹 Faster connection establishment
> 
> 
> 
> #### 🔹 Better security (no RSA key exchange)
> 
> 
> 
> #### 🔹 Forward secrecy mandatory ECDHE
> 
> 
> 
> #### 🔹 Removed legacy ciphers
> 
> 
> 
> #### 🔹 Encrypted Server Hello
> 
>
> ---
>
> ### 📍 Page 35
>
> 
> #### 🔹 TLS Use Cases:
> 
> 
> 
> #### 🔹 HTTPS (websites)
> 
> 
> 
> #### 🔹 Email SMTPS, IMAPS
> 
> 
> 
> #### 🔹 VPN OpenVPN
> 
> 
> 
> #### 🔹 API communications
> 
> 
> 
> #### 🔹 2.5 Cryptography Toolkits and Libraries
> 
> 
> 
> #### 🔹 Programming Libraries:
> 
> 
> 
> #### 🔹 OpenSSL C
> 
> 
> 
> #### 🔹 Most widely used
> 
> 
> 
> #### 🔹 Comprehensive functionality
> 
> 
> 
> #### 🔹 Command-line tools
> 
> 
> 
> #### 🔹 BouncyCastle Java/C#)
> 
> 
> 
> #### 🔹 Pure Java/C# implementation
> 
> 
> 
> #### 🔹 No native dependencies
> 
> 
> 
> #### 🔹 Extensive algorithm support
> 
> 
> 
> #### 🔹 Libsodium
> 
> 
> 
> #### 🔹 Modern crypto library
> 
> 
> 
> #### 🔹 Easy to use correctly
> 
> 
> 
> #### 🔹 High-level API
> 
> 
> 
> #### 🔹 NaCl Networking and Cryptography library) fork
> 
> 
> 
> #### 🔹 cryptography Python)
> 
> 
> 
> #### 🔹 Python cryptographic recipes
> 
> 
> 
> #### 🔹 High and low-level APIs
> 
> 
> 
> #### 🔹 Microsoft CryptoAPI / CNG
> 
> 
> 
> #### 🔹 Windows native crypto
> 
> 
> 
> #### 🔹 FIPS compliant
> 
>
> ---
>

> [!NOTE]- 📄 **Pages 36 to 40 Syllabus Content**
>
> ### 📍 Page 36
>
> 
> #### 🔹 2.6 PGP & GPG
> 
> 
> 
> #### 🔹 🔐PGP Pretty Good Privacy)
> 
> 
> 
> #### 🔹 Hybrid cryptosystem combining symmetric and asymmetric
> 
> 
> encryption for email and file security, using a web of trust model.
> 
> 
> #### 🔹 PGP/GPG Architecture
> 
> 
> 
> #### 🔹 Hybrid Cryptosystem:
> 
> 
> 
> #### 🔹  Generate random symmetric key (session key)
> 
> 
> 
> #### 🔹  Encrypt message with symmetric key (fast)
> 
> 
> 
> #### 🔹  Encrypt session key with recipient's public key
> 
> 
> 
> #### 🔹  Send both encrypted message and encrypted key
> 
> 
> 
> #### 🔹 PGP Components:
> 
> 
> 
> #### 🔹 Symmetric encryption: Message AES
> 
> 
> 
> #### 🔹 Asymmetric encryption: Session key RSA/ECC
> 
> 
> 
> #### 🔹 Hash function: Signature SHA2
> 
> 
> 
> #### 🔹 Compression: Optional ZIP
> 
> 
> 
> #### 🔹 GPG (GNU Privacy Guard)
> 
> 
> 
> #### 🔹 GPG Characteristics:
> 
> 
> 
> #### 🔹 Open-source PGP implementation
> 
> 
> 
> #### 🔹 Free software
> 
> 
> 
> #### 🔹 GPL licensed
> 
> 
> 
> #### 🔹 Command-line and GUI tools
> 
> 
> 
> #### 🔹 GPG Commands:
> 
> 
> 
> #### 🔹 # Generate key pair
> 
> 
> 
> #### 🔹 gpg --gen-key
> 
> 
> 
> #### 🔹 gpg --full-generate-key
> 
> 
> 
> #### 🔹 # List keys
> 
>
> ---
>
> ### 📍 Page 37
>
> 
> #### 🔹 gpg --list-keys
> 
> 
> 
> #### 🔹 gpg --list-secret-keys
> 
> 
> 
> #### 🔹 # Export public key
> 
> 
> 
> #### 🔹 gpg --export --armor user@email.com > pubkey.asc
> 
> 
> 
> #### 🔹 # Import public key
> 
> 
> 
> #### 🔹 gpg --import pubkey.asc
> 
> 
> 
> #### 🔹 # Encrypt file
> 
> 
> 
> #### 🔹 gpg --encrypt --recipient user@email.com file.txt
> 
> 
> 
> #### 🔹 # Decrypt file
> 
> 
> 
> #### 🔹 gpg --decrypt file.txt.gpg > file.txt
> 
> 
> 
> #### 🔹 # Sign file
> 
> 
> 
> #### 🔹 gpg --sign file.txt
> 
> 
> 
> #### 🔹 # Verify signature
> 
> 
> 
> #### 🔹 gpg --verify file.txt.gpg
> 
> 
> 
> #### 🔹 # Encrypt and sign
> 
> 
> 
> #### 🔹 gpg --encrypt --sign --recipient user@email.com file.txt
> 
> 
> 
> #### 🔹 2.7 Web of Trust
> 
> 
> 
> #### 🔹 🕸Web of Trust Model
> 
> 
> Decentralized trust model where users sign each other's public keys to verify identity, building a network of trusted relationships without central authority.
> 
> 
> #### 🔹 Web of Trust vs PKI
> 
> 
> 
> #### 🔹 Web of Trust PGP/GPG
> 
> 
> 
> #### 🔹 Decentralized
> 
> 
> 
> #### 🔹 Peer-to-peer verification
> 
>
> ---
>
> ### 📍 Page 38
>
> 
> #### 🔹 User decides whom to trust
> 
> 
> 
> #### 🔹 Key signing parties
> 
> 
> 
> #### 🔹 No central authority
> 
> 
> 
> #### 🔹 PKI X.509/CA
> 
> 
> 
> #### 🔹 Centralized
> 
> 
> 
> #### 🔹 Trusted third-party CA
> 
> 
> 
> #### 🔹 Hierarchical trust
> 
> 
> 
> #### 🔹 Automated validation
> 
> 
> 
> #### 🔹 Certificate authorities
> 
> 
> 
> #### 🔹 Trust Levels:
> 
> 
> 
> #### 🔹 Unknown: No trust information
> 
> 
> 
> #### 🔹 None: Explicitly not trusted
> 
> 
> 
> #### 🔹 Marginal: Some trust
> 
> 
> 
> #### 🔹 Full: Completely trusted
> 
> 
> 
> #### 🔹 2.8 Email Encryption
> 
> 
> 
> #### 🔹 Email Encryption Standards:
> 
> 
> 
> #### 🔹 S/MIME (Secure/Multipurpose Internet Mail Extensions)
> 
> 
> 
> #### 🔹 S/MIME Characteristics:
> 
> 
> 
> #### 🔹 PKI-based X.509 certificates)
> 
> 
> 
> #### 🔹 Integrated in enterprise email
> 
> 
> 
> #### 🔹 CA-issued certificates
> 
> 
> 
> #### 🔹 S/MIME Support:
> 
> 
> 
> #### 🔹 Microsoft Outlook
> 
> 
> 
> #### 🔹 Apple Mail
> 
> 
> 
> #### 🔹 Mozilla Thunderbird
> 
> 
> 
> #### 🔹 OpenPGP / GPG Email
> 
>
> ---
>
> ### 📍 Page 39
>
> 
> #### 🔹 PGP Email Encryption:
> 
> 
> 
> #### 🔹 Web of trust model
> 
> 
> 
> #### 🔹 Free certificates
> 
> 
> 
> #### 🔹 Requires plugin/extension
> 
> 
> 
> #### 🔹 Plugins:
> 
> 
> 
> #### 🔹 Enigmail Thunderbird)
> 
> 
> 
> #### 🔹 Mailvelope Webmail)
> 
> 
> 
> #### 🔹 GPG Suite (macOS
> 
> 
> 
> #### 🔹 ProtonMail
> 
> 
> 
> #### 🔹 Features:
> 
> 
> 
> #### 🔹 Built-in end-to-end encryption
> 
> 
> 
> #### 🔹 Zero-access encryption
> 
> 
> 
> #### 🔹 No plugin required
> 
> 
> 
> #### 🔹 PGP compatible
> 
> 
> 
> #### 🔹 2.9 Disk Encryption
> 
> 
> 
> #### 🔹 💽Full Disk Encryption FDE
> 
> 
> Encrypts entire disk or partition, protecting data at rest from unauthorized physical access.
> 
> 
> #### 🔹 Disk Encryption Solutions:
> 
> 
> 
> #### 🔹 BitLocker (Windows)
> 
> 
> 
> #### 🔹 Features:
> 
> 
> 
> #### 🔹 Full disk encryption
> 
> 
> 
> #### 🔹 TPM integration
> 
> 
> 
> #### 🔹 Pre-boot authentication
> 
> 
> 
> #### 🔹 Recovery key
> 
>
> ---
>
> ### 📍 Page 40
>
> 
> #### 🔹 BitLocker Commands:
> 
> 
> 
> #### 🔹 # Enable BitLocker
> 
> 
> 
> #### 🔹 manage-bde -on C RecoveryPassword
> 
> 
> 
> #### 🔹 # Check status
> 
> 
> 
> #### 🔹 manage-bde -status C
> 
> 
> 
> #### 🔹 # Unlock drive
> 
> 
> 
> #### 🔹 manage-bde -unlock C RecoveryPassword [password]
> 
> 
> 
> #### 🔹 FileVault (macOS)
> 
> 
> 
> #### 🔹 Features:
> 
> 
> 
> #### 🔹 XTSAES128 encryption
> 
> 
> 
> #### 🔹 Recovery key
> 
> 
> 
> #### 🔹 iCloud recovery option
> 
> 
> 
> #### 🔹 Instant wipe capability
> 
> 
> 
> #### 🔹 VeraCrypt (Cross-Platform)
> 
> 
> 
> #### 🔹 Features:
> 
> 
> 
> #### 🔹 TrueCrypt successor
> 
> 
> 
> #### 🔹 Container files or full disk
> 
> 
> 
> #### 🔹 Plausible deniability (hidden volumes)
> 
> 
> 
> #### 🔹 Pre-boot authentication
> 
> 
> 
> #### 🔹 Supported Algorithms:
> 
> 
> 
> #### 🔹 AES
> 
> 
> 
> #### 🔹 Serpent
> 
> 
> 
> #### 🔹 Twofish
> 
> 
> 
> #### 🔹 Cascaded combinations
> 
> 
> 
> #### 🔹 LUKS/dm-crypt (Linux)
> 
> 
> 
> #### 🔹 Features:
> 
>
> ---
>

> [!NOTE]- 📄 **Pages 41 to 45 Syllabus Content**
>
> ### 📍 Page 41
>
> 
> #### 🔹 Linux standard
> 
> 
> 
> #### 🔹 Multiple key slots
> 
> 
> 
> #### 🔹 Header backup
> 
> 
> 
> #### 🔹 Various ciphers supported
> 
> 
> 
> #### 🔹 # Create encrypted volume
> 
> 
> 
> #### 🔹 cryptsetup luksFormat /dev/sdX
> 
> 
> 
> #### 🔹 # Open encrypted volume
> 
> 
> 
> #### 🔹 cryptsetup open /dev/sdX myvolume
> 
> 
> 
> #### 🔹 # Close encrypted volume
> 
> 
> 
> #### 🔹 cryptsetup close myvolume
> 
> 
> 
> #### 🔹 2.10 Blockchain Cryptography
> 
> 
> 
> #### 🔹 ⛓Blockchain
> 
> 
> Distributed ledger using cryptographic hashing and digital signatures to ensure integrity, immutability, and trust without central authority.
> 
> 
> #### 🔹 Cryptography in Blockchain:
> 
> 
> 
> #### 🔹 Hash Functions
> 
> 
> 
> #### 🔹 Block integrity SHA256 in Bitcoin)
> 
> 
> 
> #### 🔹 Merkle trees for transaction verification
> 
> 
> 
> #### 🔹 Proof-of-Work
> 
> 
> 
> #### 🔹 Public Key Cryptography
> 
> 
> 
> #### 🔹 Wallet addresses (public key hash)
> 
> 
> 
> #### 🔹 Transaction signing (private key)
> 
> 
> 
> #### 🔹 Identity verification
> 
> 
> 
> #### 🔹 Digital Signatures
> 
> 
> 
> #### 🔹 Transaction authentication
> 
> 
> 
> #### 🔹 4 1
> 
>
> ---
>
> ### 📍 Page 42
>
> 
> #### 🔹 Non-repudiation
> 
> 
> 
> #### 🔹 ECDSA (secp256k1 for Bitcoin)
> 
> 
> 
> #### 🔹 Consensus Algorithms:
> 
> 
> 
> #### 🔹 Proof of Work PoW Computational puzzles
> 
> 
> 
> #### 🔹 Proof of Stake PoS Stake-based validation
> 
> 
> 
> #### 🔹 Blockchain Use Cases:
> 
> 
> 
> #### 🔹 Cryptocurrencies: Bitcoin, Ethereum
> 
> 
> 
> #### 🔹 Smart contracts: Automated agreements
> 
> 
> 
> #### 🔹 Supply chain: Product tracking
> 
> 
> 
> #### 🔹 Identity management: Self-sovereign identity
> 
> 
> 
> #### 🔹 Digital assets: NFTs
> 
> 
> 
> #### 🔹 3. Cryptanalysis
> 
> 
> 
> #### 🔹 3.1 Introduction to Cryptanalysis
> 
> 
> 
> #### 🔹 🔍Cryptanalysis
> 
> 
> The study of analyzing and breaking cryptographic systems, finding weaknesses in ciphers, protocols, or implementations.
> 
> 
> #### 🔹 Cryptanalysis Goals:
> 
> 
> 
> #### 🔹 Recover plaintext
> 
> 
> 
> #### 🔹 Recover encryption key
> 
> 
> 
> #### 🔹 Find algorithm weaknesses
> 
> 
> 
> #### 🔹 Identify implementation flaws
> 
> 
> 
> #### 🔹 Cryptanalysis Methods
> 
> 
> 
> #### 🔹 Linear Cryptanalysis
> 
> 
> 
> #### 🔹 Statistical linear approximations
> 
>
> ---
>
> ### 📍 Page 43
>
> 
> #### 🔹 Requires many plaintext-ciphertext pairs
> 
> 
> 
> #### 🔹 Effective against DES
> 
> 
> 
> #### 🔹 Differential Cryptanalysis
> 
> 
> 
> #### 🔹 Analyze difference between input pairs
> 
> 
> 
> #### 🔹 Track difference propagation
> 
> 
> 
> #### 🔹 Block cipher analysis
> 
> 
> 
> #### 🔹 Algebraic Attacks
> 
> 
> 
> #### 🔹 Express cipher as algebraic equations
> 
> 
> 
> #### 🔹 Solve equation system
> 
> 
> 
> #### 🔹 Brute-Force
> 
> 
> 
> #### 🔹 Try every possible key
> 
> 
> 
> #### 🔹 Guaranteed but computationally expensive
> 
> 
> 
> #### 🔹 Statistical Analysis
> 
> 
> 
> #### 🔹 Frequency analysis
> 
> 
> 
> #### 🔹 Pattern recognition
> 
> 
> 
> #### 🔹 Cipher-specific attacks
> 
> 
> 
> #### 🔹 3.2 Cryptographic Attack Types
> 
> 
> 
> #### 🔹 Attack Classifications:
> 
> 
> 
> #### 🔹 Ciphertext-Only Attack
> 
> 
> 
> #### 🔹 Attacker Has:
> 
> 
> 
> #### 🔹 Multiple ciphertexts
> 
> 
> 
> #### 🔹 Goal:
> 
> 
> 
> #### 🔹 Recover plaintexts or key
> 
> 
> 
> #### 🔹 Difficulty: Hardest attack type
> 
> 
> 
> #### 🔹 Known-Plaintext Attack
> 
> 
> 
> #### 🔹 Attacker Has:
> 
>
> ---
>
> ### 📍 Page 44
>
> 
> #### 🔹 Plaintext-ciphertext pairs
> 
> 
> 
> #### 🔹 Goal:
> 
> 
> 
> #### 🔹 Recover key or decrypt other ciphertexts
> 
> 
> 
> #### 🔹 Historical Success:
> 
> 
> 
> #### 🔹 Breaking Enigma WWII
> 
> 
> 
> #### 🔹 Chosen-Plaintext Attack
> 
> 
> 
> #### 🔹 Attacker Can:
> 
> 
> 
> #### 🔹 Choose plaintexts to encrypt
> 
> 
> 
> #### 🔹 Observe resulting ciphertexts
> 
> 
> 
> #### 🔹 Goal:
> 
> 
> 
> #### 🔹 Recover key
> 
> 
> 
> #### 🔹 Example:
> 
> 
> 
> #### 🔹 Attacking block ciphers
> 
> 
> 
> #### 🔹 ECB mode oracle attacks
> 
> 
> 
> #### 🔹 Chosen-Ciphertext Attack
> 
> 
> 
> #### 🔹 Attacker Can:
> 
> 
> 
> #### 🔹 Choose ciphertexts to decrypt
> 
> 
> 
> #### 🔹 Observe resulting plaintexts
> 
> 
> 
> #### 🔹 Goal:
> 
> 
> 
> #### 🔹 Recover key or plaintext
> 
> 
> 
> #### 🔹 Example:
> 
> 
> 
> #### 🔹 Padding oracle attack CBC
> 
> 
> 
> #### 🔹 Adaptive Chosen-Ciphertext Attack
> 
> 
> 
> #### 🔹 Attacker Can:
> 
> 
> 
> #### 🔹 Iteratively choose ciphertexts based on previous results
> 
> 
> 
> #### 🔹 Most powerful attack model
> 
>
> ---
>
> ### 📍 Page 45
>
> 
> #### 🔹 3.3 Code Breaking Methodologies
> 
> 
> 
> #### 🔹 Analysis Techniques:
> 
> 
> 
> #### 🔹 Frequency Analysis
> 
> 
> 
> #### 🔹 Method:
> 
> 
> 
> #### 🔹 Analyze character/word frequencies
> 
> 
> 
> #### 🔹 Compare to known language statistics
> 
> 
> 
> #### 🔹 Identify common patterns
> 
> 
> 
> #### 🔹 Effective Against:
> 
> 
> 
> #### 🔹 Substitution ciphers
> 
> 
> 
> #### 🔹 Classical ciphers
> 
> 
> 
> #### 🔹 Weak encryption
> 
> 
> 
> #### 🔹 Pattern Recognition
> 
> 
> 
> #### 🔹 Look For:
> 
> 
> 
> #### 🔹 Repeating sequences
> 
> 
> 
> #### 🔹 Word patterns
> 
> 
> 
> #### 🔹 Structural weaknesses
> 
> 
> 
> #### 🔹 Side-Channel Analysis
> 
> 
> 
> #### 🔹 Types:
> 
> 
> 
> #### 🔹 Timing attacks: Measure execution time
> 
> 
> 
> #### 🔹 Power analysis: Monitor power consumption
> 
> 
> 
> #### 🔹 Electromagnetic analysis: EM radiation
> 
> 
> 
> #### 🔹 Acoustic analysis: Sound from components
> 
> 
> 
> #### 🔹 Cache attacks: CPU cache timing
> 
> 
> 
> #### 🔹 3.4 Brute-Force Attack
> 
>
> ---
>

> [!NOTE]- 📄 **Pages 46 to 50 Syllabus Content**
>
> ### 📍 Page 46
>
> 
> #### 🔹 💪Brute-Force Attack
> 
> 
> Systematically trying every possible key until the correct one is found. Effectiveness depends on key length and computational power.
> 
> 
> #### 🔹 Brute-Force Characteristics:
> 
> 
> 
> #### 🔹 Guaranteed Success
> 
> 
> 
> #### 🔹 Will eventually find key (given enough time)
> 
> 
> 
> #### 🔹 Computationally Expensive
> 
> 
> 
> #### 🔹 Time increases exponentially with key length
> 
> 
> 
> #### 🔹 Key Length Importance:
> 
> 
> 
> #### 🔹 56-bit DES Broken in hours
> 
> 
> 
> #### 🔹 128-bit: 3.4  10³⁸ combinations
> 
> 
> 
> #### 🔹 256-bit: 1.1  10⁷⁷ combinations
> 
> 
> 
> #### 🔹 Countermeasure:
> 
> 
> 
> #### 🔹 Use sufficiently long keys 128 bits for symmetric)
> 
> 
> 
> #### 🔹 Birthday Attack
> 
> 
> 
> #### 🔹 🎂Birthday Attack
> 
> 
> Exploits the birthday paradox to find hash collisions faster than brute force, requiring only √n attempts instead of n.
> 
> 
> #### 🔹 Birthday Paradox:
> 
> 
> 
> #### 🔹 23 people  50% chance of shared birthday
> 
> 
> 
> #### 🔹 70 people  99.9% chance
> 
> 
> 
> #### 🔹 Cryptographic Application:
> 
> 
> 
> #### 🔹 Finding hash collisions
> 
> 
> 
> #### 🔹 Attack complexity: √(2^n) instead of 2^n
> 
> 
> 
> #### 🔹 For 256-bit hash: 2^128 operations (instead of 2^256
> 
> 
> 
> #### 🔹 Implications:
> 
>
> ---
>
> ### 📍 Page 47
>
> 
> #### 🔹 Hash functions need double the security bits
> 
> 
> 
> #### 🔹 256-bit hash provides 128-bit security
> 
> 
> 
> #### 🔹 512-bit hash provides 256-bit security
> 
> 
> 
> #### 🔹 Countermeasure:
> 
> 
> 
> #### 🔹 Use hash functions with sufficient output size
> 
> 
> 
> #### 🔹 3.5 Brute-Forcing VeraCrypt
> 
> 
> 
> #### 🔹 VeraCrypt Cracking:
> 
> 
> 
> #### 🔹 Tools:
> 
> 
> 
> #### 🔹 Hashcat: GPU-accelerated
> 
> 
> 
> #### 🔹 John the Ripper: CPU-based
> 
> 
> 
> #### 🔹 Passware: Commercial solution
> 
> 
> 
> #### 🔹 Hashcat VeraCrypt:
> 
> 
> 
> #### 🔹 # Extract hash
> 
> 
> 
> #### 🔹 john --format=veracrypt volume.hc
> 
> 
> 
> #### 🔹 # Brute-force with Hashcat
> 
> 
> 
> #### 🔹 hashcat -m 13711 -a 0 hash.txt wordlist.txt
> 
> 
> 
> #### 🔹 # VeraCrypt modes:
> 
> 
> 
> #### 🔹 # 13711 VeraCrypt PBKDF2HMACRIPEMD160  XTS 512 bit
> 
> 
> 
> #### 🔹 # 13712 VeraCrypt PBKDF2HMACRIPEMD160  XTS 1024 bit
> 
> 
> 
> #### 🔹 # 13713 VeraCrypt PBKDF2HMACRIPEMD160  XTS 1536 bit
> 
> 
> 
> #### 🔹 Challenges:
> 
> 
> 
> #### 🔹 Key derivation: 500,000 iterations PBKDF2
> 
> 
> 
> #### 🔹 Multiple algorithms: AES, Serpent, Twofish
> 
> 
> 
> #### 🔹 Cascaded encryption: Further complexity
> 
> 
> 
> #### 🔹 No header: Plausible deniability
> 
> 
> 
> #### 🔹 Defense:
> 
> 
> 
> #### 🔹 Long, complex passphrase
> 
>
> ---
>
> ### 📍 Page 48
>
> 
> #### 🔹 Keyfile in addition to password
> 
> 
> 
> #### 🔹 PIM Personal Iterations Multiplier)
> 
> 
> 
> #### 🔹 3.6 Meet-in-the-Middle Attack
> 
> 
> 
> #### 🔹 🔀Meet-in-the-Middle Attack
> 
> 
> Cryptanalytic technique attacking double encryption by computing from both ends and finding the middle, reducing effective security.
> 
> 
> #### 🔹 Attack on Double Encryption:
> 
> 
> 
> #### 🔹 2DES (theoretical):
> 
> 
> 
> #### 🔹 Two DES encryptions: E_K2E_K1P
> 
> 
> 
> #### 🔹 Expected security: 112 bits 5656
> 
> 
> 
> #### 🔹 Actual security: 57 bits (only 2 better than DES
> 
> 
> 
> #### 🔹 MITM Attack Process:
> 
> 
> 
> #### 🔹  Encrypt plaintext with all K1 values  Store results
> 
> 
> 
> #### 🔹  Decrypt ciphertext with all K2 values  Store results
> 
> 
> 
> #### 🔹  Find matching intermediate value
> 
> 
> 
> #### 🔹  Discovered K1 and K2
> 
> 
> 
> #### 🔹 Why 3DES is Secure:
> 
> 
> 
> #### 🔹 MITM attack less effective on 3DES
> 
> 
> 
> #### 🔹 3DESEDE3 Effective 112-bit security
> 
> 
> 
> #### 🔹 Attack requires 2^56 memory (impractical)
> 
> 
> 
> #### 🔹 3.7 Side-Channel Attacks
> 
> 
> 
> #### 🔹 📡Side-Channel Attacks
> 
> 
> Exploiting physical implementation characteristics (timing, power, EM
> 
> 
> #### 🔹 radiation) rather than algorithmic weaknesses to extract
> 
> 
> cryptographic secrets.
>
> ---
>
> ### 📍 Page 49
>
> 
> #### 🔹 Timing Attacks
> 
> 
> 
> #### 🔹 Method:
> 
> 
> 
> #### 🔹 Measure execution time
> 
> 
> 
> #### 🔹 Correlate timing with secret data
> 
> 
> 
> #### 🔹 Statistical analysis
> 
> 
> 
> #### 🔹 Vulnerable Operations:
> 
> 
> 
> #### 🔹 Conditional branches based on secret
> 
> 
> 
> #### 🔹 Variable-time operations
> 
> 
> 
> #### 🔹 Cache hits/misses
> 
> 
> 
> #### 🔹 Examples:
> 
> 
> 
> #### 🔹 RSA private key recovery
> 
> 
> 
> #### 🔹 AES key extraction
> 
> 
> 
> #### 🔹 Countermeasure:
> 
> 
> 
> #### 🔹 Constant-time implementations
> 
> 
> 
> #### 🔹 No secret-dependent branches
> 
> 
> 
> #### 🔹 Power Analysis
> 
> 
> 
> #### 🔹 Simple Power Analysis SPA
> 
> 
> 
> #### 🔹 Direct observation of power traces
> 
> 
> 
> #### 🔹 Identify operations visually
> 
> 
> 
> #### 🔹 Differential Power Analysis DPA
> 
> 
> 
> #### 🔹 Statistical analysis of many traces
> 
> 
> 
> #### 🔹 Correlate power with hypothetical intermediates
> 
> 
> 
> #### 🔹 Correlation Power Analysis CPA
> 
> 
> 
> #### 🔹 Advanced statistical methods
> 
> 
> 
> #### 🔹 Very effective
> 
> 
> 
> #### 🔹 Countermeasures:
> 
> 
> 
> #### 🔹 Power consumption randomization
> 
>
> ---
>
> ### 📍 Page 50
>
> 
> #### 🔹 Masking techniques
> 
> 
> 
> #### 🔹 Hardware countermeasures
> 
> 
> 
> #### 🔹 Electromagnetic Analysis
> 
> 
> 
> #### 🔹 Method:
> 
> 
> 
> #### 🔹 Capture EM emissions during crypto operations
> 
> 
> 
> #### 🔹 Similar to power analysis
> 
> 
> 
> #### 🔹 Can be performed remotely (near-field)
> 
> 
> 
> #### 🔹 Countermeasures:
> 
> 
> 
> #### 🔹 EM shielding
> 
> 
> 
> #### 🔹 Filtered power supply
> 
> 
> 
> #### 🔹 Randomization
> 
> 
> 
> #### 🔹 Acoustic Cryptanalysis
> 
> 
> 
> #### 🔹 Method:
> 
> 
> 
> #### 🔹 Analyze sounds from:
> 
> 
> 
> #### 🔹 CPU operations
> 
> 
> 
> #### 🔹 Keyboard typing (keystrokes)
> 
> 
> 
> #### 🔹 Mechanical components
> 
> 
> 
> #### 🔹 Example:
> 
> 
> 
> #### 🔹 RSA key extraction from laptop sounds
> 
> 
> 
> #### 🔹 Cache Timing Attacks
> 
> 
> 
> #### 🔹 Method:
> 
> 
> 
> #### 🔹 Exploit CPU cache behavior
> 
> 
> 
> #### 🔹 Measure cache hits vs misses
> 
> 
> 
> #### 🔹 Infer secret data access patterns
> 
> 
> 
> #### 🔹 Famous Attacks:
> 
> 
> 
> #### 🔹 Spectre: Speculative execution
> 
> 
> 
> #### 🔹 Meltdown: Out-of-order execution
> 
>
> ---
>

> [!NOTE]- 📄 **Pages 51 to 55 Syllabus Content**
>
> ### 📍 Page 51
>
> 
> #### 🔹 FLUSHRELOAD Cache timing
> 
> 
> 
> #### 🔹 Countermeasures:
> 
> 
> 
> #### 🔹 Cache-oblivious algorithms
> 
> 
> 
> #### 🔹 Hardware mitigations
> 
> 
> 
> #### 🔹 Microcode updates
> 
> 
> 
> #### 🔹 3.8 Hash Collision Attacks
> 
> 
> 
> #### 🔹 💥Collision Attack
> 
> 
> Finding two different inputs that produce the same hash output, breaking the collision-resistance property of hash functions.
> 
> 
> #### 🔹 Collision Attack Success:
> 
> 
> 
> #### 🔹 MD5 BROKEN
> 
> 
> 
> #### 🔹 First collision: 2004
> 
> 
> 
> #### 🔹 Practical collisions: Minutes on modern hardware
> 
> 
> 
> #### 🔹 Impact: Cannot be used for security
> 
> 
> 
> #### 🔹 SHA1 BROKEN
> 
> 
> 
> #### 🔹 First theoretical collision: 2005
> 
> 
> 
> #### 🔹 First practical collision SHAttered): 2017
> 
> 
> 
> #### 🔹 Impact: Deprecated for certificates and signatures
> 
> 
> 
> #### 🔹 Collision Attack Applications:
> 
> 
> 
> #### 🔹 Malicious Certificates
> 
> 
> 
> #### 🔹 Create fake SSL certificate with same hash as legitimate
> 
> 
> 
> #### 🔹 File Integrity Bypass
> 
> 
> 
> #### 🔹 Replace legitimate file with malicious one (same hash)
> 
> 
> 
> #### 🔹 Digital Signature Forgery
> 
> 
> 
> #### 🔹 Create different document with same signature
> 
> 
> 
> #### 🔹 Countermeasure:
> 
>
> ---
>
> ### 📍 Page 52
>
> 
> #### 🔹 Use SHA256 or SHA3
> 
> 
> 
> #### 🔹 Collision resistance proven
> 
> 
> 
> #### 🔹 3.9 DUHK Attack
> 
> 
> 
> #### 🔹 DUHK Don't Use Hard-coded Keys) Attack:
> 
> 
> 
> #### 🔹 Target:
> 
> 
> 
> #### 🔹 Predictable random number generators
> 
> 
> 
> #### 🔹 Dual_EC_DRBG NSA backdoor)
> 
> 
> 
> #### 🔹 Attack:
> 
> 
> 
> #### 🔹 Recover encryption keys from predictable RNG
> 
> 
> 
> #### 🔹 Decrypt TLS/VPN traffic
> 
> 
> 
> #### 🔹 Vulnerable Systems:
> 
> 
> 
> #### 🔹 Some VPN implementations
> 
> 
> 
> #### 🔹 Networking equipment
> 
> 
> 
> #### 🔹 Countermeasure:
> 
> 
> 
> #### 🔹 Use strong RNGs Fortuna, /dev/urandom)
> 
> 
> 
> #### 🔹 Avoid Dual_EC_DRBG
> 
> 
> 
> #### 🔹 3.10 DROWN Attack
> 
> 
> ⚓DROWN Decrypting RSA with Obsolete and Weakened eNcryption) Cross-protocol attack allowing decryption of TLS sessions by exploiting SSLv2 support, even if not actively used.
> 
> 
> #### 🔹 DROWN Attack:
> 
> 
> 
> #### 🔹 Requirements:
> 
> 
> 
> #### 🔹 Server supports SSLv2 (even if unused)
> 
> 
> 
> #### 🔹 Shares RSA key with TLS 1.2 server
> 
> 
> 
> #### 🔹 Attack Process:
> 
>
> ---
>
> ### 📍 Page 53
>
> 
> #### 🔹  Capture TLS 1.2 handshake
> 
> 
> 
> #### 🔹  Exploit SSLv2 vulnerabilities
> 
> 
> 
> #### 🔹  Decrypt TLS session key
> 
> 
> 
> #### 🔹  Decrypt TLS 1.2 traffic
> 
> 
> 
> #### 🔹 Impact:
> 
> 
> 
> #### 🔹 33% of HTTPS servers vulnerable 2016
> 
> 
> 
> #### 🔹 Can decrypt past recorded traffic
> 
> 
> 
> #### 🔹 Countermeasure:
> 
> 
> 
> #### 🔹 Disable SSLv2 completely
> 
> 
> 
> #### 🔹 Disable SSLv3
> 
> 
> 
> #### 🔹 Unique keys per service
> 
> 
> 
> #### 🔹 3.11 Rainbow Table Attack
> 
> 
> 
> #### 🔹 🌈Rainbow Tables
> 
> 
> Precomputed hash lookup tables enabling rapid password cracking by trading computation time for storage space.
> 
> 
> #### 🔹 Rainbow Table Concept:
> 
> 
> 
> #### 🔹 Precomputation:
> 
> 
> 
> #### 🔹  Generate password candidates
> 
> 
> 
> #### 🔹  Hash each password
> 
> 
> 
> #### 🔹  Store in optimized lookup table
> 
> 
> 
> #### 🔹  Use hash chains (reduce storage)
> 
> 
> 
> #### 🔹 Attack Process:
> 
> 
> 
> #### 🔹  Obtain password hash
> 
> 
> 
> #### 🔹  Lookup hash in rainbow table
> 
> 
> 
> #### 🔹  Retrieve plaintext password
> 
> 
> 
> #### 🔹  Nearly instant cracking
> 
>
> ---
>
> ### 📍 Page 54
>
> 
> #### 🔹 Rainbow Table Characteristics:
> 
> 
> 
> #### 🔹 Time-memory trade-off
> 
> 
> 
> #### 🔹 One-time generation (reusable)
> 
> 
> 
> #### 🔹 Fast lookups (seconds)
> 
> 
> 
> #### 🔹 Large storage GB to TB
> 
> 
> 
> #### 🔹 Available Rainbow Tables:
> 
> 
> 
> #### 🔹 LM hashes Windows legacy)
> 
> 
> 
> #### 🔹 NTLM hashes
> 
> 
> 
> #### 🔹 MD5 (common passwords)
> 
> 
> 
> #### 🔹 SHA1
> 
> 
> 
> #### 🔹 Defense: Salt
> 
> 
> 
> #### 🔹 🧂Password Salting
> 
> 
> Adding unique random data to each password before hashing, making rainbow tables ineffective by requiring separate tables for each salt.
> 
> 
> #### 🔹 Salt Implementation:
> 
> 
> 
> #### 🔹 hash  SHA256(password + salt)
> 
> 
> 
> #### 🔹 store: salt, hash
> 
> 
> 
> #### 🔹 Salt Benefits:
> 
> 
> 
> #### 🔹 Unique hash per user (even for same password)
> 
> 
> 
> #### 🔹 Rainbow tables useless (need table per salt)
> 
> 
> 
> #### 🔹 Prevents parallel cracking of multiple hashes
> 
> 
> 
> #### 🔹 Salt Requirements:
> 
> 
> 
> #### 🔹 Cryptographically random
> 
> 
> 
> #### 🔹 Unique per password
> 
> 
> 
> #### 🔹 Sufficient length 16 bytes)
> 
> 
> 
> #### 🔹 Stored alongside hash (not secret)
> 
>
> ---
>
> ### 📍 Page 55
>
> 
> #### 🔹 Key Stretching Additional Defense):
> 
> 
> 
> #### 🔹 Purpose:
> 
> 
> 
> #### 🔹 Slow down brute-force attacks
> 
> 
> 
> #### 🔹 Methods:
> 
> 
> 
> #### 🔹 PBKDF2 Iterate hash function 10,000 iterations)
> 
> 
> 
> #### 🔹 bcrypt: Adaptive cost factor
> 
> 
> 
> #### 🔹 scrypt: Memory-hard function
> 
> 
> 
> #### 🔹 Argon2 Winner of Password Hashing Competition
> 
> 
> 
> #### 🔹 Example (bcrypt):
> 
> 
> 
> #### 🔹 hash = bcrypt(password, cost=12
> 
> 
> 
> #### 🔹 # cost=12 means 2^12  4096 iterations
> 
> 
> 
> #### 🔹 3.12 Related-Key Attack
> 
> 
> 
> #### 🔹 Related-Key Attack:
> 
> 
> 
> #### 🔹 Method:
> 
> 
> 
> #### 🔹 Exploit relationships between different encryption keys
> 
> 
> 
> #### 🔹 Observe encryption with related keys
> 
> 
> 
> #### 🔹 Target:
> 
> 
> 
> #### 🔹 Some AES256 modes
> 
> 
> 
> #### 🔹 Key schedules
> 
> 
> 
> #### 🔹 Mitigation:
> 
> 
> 
> #### 🔹 Avoid related keys in protocol design
> 
> 
> 
> #### 🔹 Use different keys for different purposes
> 
> 
> 
> #### 🔹 3.13 Padding Oracle Attack
> 
>
> ---
>

> [!NOTE]- 📄 **Pages 56 to 60 Syllabus Content**
>
> ### 📍 Page 56
>
> 
> #### 🔹 🔓Padding Oracle Attack
> 
> 
> Exploiting improper validation of CBC mode padding to decrypt ciphertexts without knowing the key.
> 
> 
> #### 🔹 Attack Target:
> 
> 
> 
> #### 🔹 CBC mode encryption
> 
> 
> 
> #### 🔹 Systems revealing padding errors
> 
> 
> 
> #### 🔹 Attack Process:
> 
> 
> 
> #### 🔹  Send modified ciphertext
> 
> 
> 
> #### 🔹  Observe padding error vs other error
> 
> 
> 
> #### 🔹  Deduce plaintext byte-by-byte
> 
> 
> 
> #### 🔹  Full plaintext recovery
> 
> 
> 
> #### 🔹 Vulnerable Systems:
> 
> 
> 
> #### 🔹 Web applications ASP.NET
> 
> 
> 
> #### 🔹 Some TLS implementations
> 
> 
> 
> #### 🔹 XML encryption
> 
> 
> 
> #### 🔹 Defense:
> 
> 
> 
> #### 🔹 Authenticated encryption GCM
> 
> 
> 
> #### 🔹 Constant-time validation
> 
> 
> 
> #### 🔹 Same error for all failures
> 
> 
> 
> #### 🔹 MAC-then-encrypt or AEAD
> 
> 
> 
> #### 🔹 3.14 Attacks on Blockchain
> 
> 
> 
> #### 🔹 Blockchain Attack Vectors:
> 
> 
> 
> #### 🔹 51% Attack
> 
>
> ---
>
> ### 📍 Page 57
>
> 
> #### 🔹 ⚠51% Attack
> 
> 
> Controlling majority of network's mining/validation power to manipulate blockchain, reverse transactions, or double-spend.
> 
> 
> #### 🔹 Attack Capabilities:
> 
> 
> 
> #### 🔹 Reverse own transactions (double-spend)
> 
> 
> 
> #### 🔹 Prevent transaction confirmations
> 
> 
> 
> #### 🔹 Prevent other miners from mining
> 
> 
> 
> #### 🔹 Not Possible:
> 
> 
> 
> #### 🔹 Steal others' coins
> 
> 
> 
> #### 🔹 Alter past blocks deeply
> 
> 
> 
> #### 🔹 Create coins from nothing
> 
> 
> 
> #### 🔹 Vulnerable:
> 
> 
> 
> #### 🔹 Small cryptocurrencies
> 
> 
> 
> #### 🔹 Low hash rate networks
> 
> 
> 
> #### 🔹 Sybil Attack
> 
> 
> 
> #### 🔹 Method:
> 
> 
> 
> #### 🔹 Create many fake identities
> 
> 
> 
> #### 🔹 Control large portion of network
> 
> 
> 
> #### 🔹 Manipulate consensus
> 
> 
> 
> #### 🔹 Defense:
> 
> 
> 
> #### 🔹 Proof of Work
> 
> 
> 
> #### 🔹 Proof of Stake
> 
> 
> 
> #### 🔹 Identity verification
> 
> 
> 
> #### 🔹 Double Spending
> 
> 
> 
> #### 🔹 Scenario:
> 
> 
> 
> #### 🔹 Spend coins in Transaction A
> 
>
> ---
>
> ### 📍 Page 58
>
> 
> #### 🔹 Simultaneously broadcast Transaction B (same coins)
> 
> 
> 
> #### 🔹 Attempt to confirm both
> 
> 
> 
> #### 🔹 Prevention:
> 
> 
> 
> #### 🔹 Wait for multiple confirmations 6 for Bitcoin)
> 
> 
> 
> #### 🔹 Proof of Work difficulty
> 
> 
> 
> #### 🔹 Selfish Mining
> 
> 
> 
> #### 🔹 Method:
> 
> 
> 
> #### 🔹 Withhold mined blocks
> 
> 
> 
> #### 🔹 Release strategically
> 
> 
> 
> #### 🔹 Gain unfair advantage
> 
> 
> 
> #### 🔹 Impact:
> 
> 
> 
> #### 🔹 Reduced network security
> 
> 
> 
> #### 🔹 Centralization risk
> 
> 
> 
> #### 🔹 3.15 Quantum Computing Threats
> 
> 
> 
> #### 🔹 ⚛Quantum Computing Threat
> 
> 
> Quantum computers pose existential threat to current asymmetric cryptography RSA, ECC, requiring post-quantum algorithms.
> 
> 
> #### 🔹 Quantum Algorithms:
> 
> 
> 
> #### 🔹 Shor's Algorithm
> 
> 
> 
> #### 🔹 Breaks:
> 
> 
> 
> #### 🔹 RSA (integer factorization)
> 
> 
> 
> #### 🔹 ECC (discrete logarithm)
> 
> 
> 
> #### 🔹 Diffie-Hellman
> 
> 
> 
> #### 🔹 Impact:
> 
> 
> 
> #### 🔹 All current public-key cryptography
> 
>
> ---
>
> ### 📍 Page 59
>
> 
> #### 🔹 Digital signatures
> 
> 
> 
> #### 🔹 Key exchange
> 
> 
> 
> #### 🔹 TLS/SSL
> 
> 
> 
> #### 🔹 Timeline:
> 
> 
> 
> #### 🔹 Large-scale quantum computers: 530 years (estimates vary)
> 
> 
> 
> #### 🔹 "Store now, decrypt later" threat
> 
> 
> 
> #### 🔹 Grover's Algorithm
> 
> 
> 
> #### 🔹 Weakens:
> 
> 
> 
> #### 🔹 Symmetric encryption
> 
> 
> 
> #### 🔹 Hash functions
> 
> 
> 
> #### 🔹 Impact:
> 
> 
> 
> #### 🔹 Effective key length halved
> 
> 
> 
> #### 🔹 AES128  64-bit security
> 
> 
> 
> #### 🔹 AES256  128-bit security
> 
> 
> 
> #### 🔹 Mitigation:
> 
> 
> 
> #### 🔹 Use AES256 instead of AES128
> 
> 
> 
> #### 🔹 Post-Quantum Cryptography:
> 
> 
> 
> #### 🔹 NIST Post-Quantum Standards:
> 
> 
> 
> #### 🔹 Key Encapsulation:
> 
> 
> 
> #### 🔹 CRYSTALSKyber (selected 2022
> 
> 
> 
> #### 🔹 Digital Signatures:
> 
> 
> 
> #### 🔹 CRYSTALSDilithium
> 
> 
> 
> #### 🔹 FALCON
> 
> 
> 
> #### 🔹 SPHINCS
> 
> 
> 
> #### 🔹 Algorithm Types:
> 
> 
> 
> #### 🔹 Lattice-based Kyber, Dilithium)
> 
> 
> 
> #### 🔹 Hash-based SPHINCS
> 
>
> ---
>
> ### 📍 Page 60
>
> 
> #### 🔹 Code-based
> 
> 
> 
> #### 🔹 Multivariate polynomial
> 
> 
> 
> #### 🔹 Transition Strategy:
> 
> 
> 
> #### 🔹 Crypto-agility: Design systems for algorithm updates
> 
> 
> 
> #### 🔹 Hybrid mode: Use both classical and post-quantum
> 
> 
> 
> #### 🔹 Inventory: Identify all cryptographic usage
> 
> 
> 
> #### 🔹 Plan migration: Timeline for updates
> 
> 
> 
> #### 🔹 3.16 Cryptanalysis Tools
> 
> 
> 
> #### 🔹 Password Cracking:
> 
> 
> 
> #### 🔹 Hashcat
> 
> 
> 
> #### 🔹 Features:
> 
> 
> 
> #### 🔹 GPU-accelerated
> 
> 
> 
> #### 🔹 300 hash algorithms
> 
> 
> 
> #### 🔹 Multiple attack modes
> 
> 
> 
> #### 🔹 Attack Modes:
> 
> 
> 
> #### 🔹 # Dictionary attack
> 
> 
> 
> #### 🔹 hashcat -m 0 -a 0 hashes.txt wordlist.txt
> 
> 
> 
> #### 🔹 # Brute-force
> 
> 
> 
> #### 🔹 hashcat -m 0 -a 3 hashes.txt ?a?a?a?a?a?a?a?a
> 
> 
> 
> #### 🔹 # Combinator
> 
> 
> 
> #### 🔹 hashcat -m 0 -a 1 hashes.txt dict1.txt dict2.txt
> 
> 
> 
> #### 🔹 # Rule-based
> 
> 
> hashcat -m 0 -a 0 hashes.txt wordlist.txt -r rules/best64.rule
> 
> 
> #### 🔹 Common Hash Modes:
> 
> 
> -m 0 MD5 -m 100 SHA1
>
> ---
>

> [!NOTE]- 📄 **Pages 61 to 65 Syllabus Content**
>
> ### 📍 Page 61
>
> -m 1000 NTLM -m 1800 SHA512Unix) -m 3200: bcrypt -m 22000 WPAPBKDF2PMKIDEAPOL
> 
> 
> #### 🔹 John the Ripper
> 
> 
> 
> #### 🔹 Features:
> 
> 
> 
> #### 🔹 CPU-based cracking
> 
> 
> 
> #### 🔹 Automatic hash detection
> 
> 
> 
> #### 🔹 Custom rules
> 
> 
> 
> #### 🔹 # Auto-detect and crack
> 
> 
> 
> #### 🔹 john hashes.txt
> 
> 
> 
> #### 🔹 # Wordlist attack
> 
> 
> 
> #### 🔹 john --wordlist=rockyou.txt hashes.txt
> 
> 
> 
> #### 🔹 # Specific format
> 
> 
> 
> #### 🔹 john --format=NT hashes.txt
> 
> 
> 
> #### 🔹 # Show cracked passwords
> 
> 
> 
> #### 🔹 john --show hashes.txt
> 
> 
> 
> #### 🔹 Other Cracking Tools
> 
> 
> 
> #### 🔹 Cain & Abel Windows)
> 
> 
> 
> #### 🔹 Network sniffing
> 
> 
> 
> #### 🔹 Password recovery
> 
> 
> 
> #### 🔹 ARP poisoning
> 
> 
> 
> #### 🔹 Hydra
> 
> 
> 
> #### 🔹 Network login cracker
> 
> 
> 
> #### 🔹 Multiple protocols SSH, FTP, HTTP, etc.)
> 
> 
> 
> #### 🔹 Aircrack-ng
> 
>
> ---
>
> ### 📍 Page 62
>
> 
> #### 🔹 Wireless network cracking
> 
> 
> 
> #### 🔹 WEP/WPA/WPA2
> 
> 
> 
> #### 🔹 RainbowCrack
> 
> 
> 
> #### 🔹 Rainbow table generator and cracker
> 
> 
> 
> #### 🔹 3.17 Online Hash Cracking
> 
> 
> 
> #### 🔹 Online Hash Lookup Services:
> 
> 
> 
> #### 🔹 CrackStation
> 
> 
> 
> #### 🔹 Massive hash database
> 
> 
> 
> #### 🔹 MD5, SHA1, SHA256
> 
> 
> 
> #### 🔹 Free lookups
> 
> 
> 
> #### 🔹 HashKiller
> 
> 
> 
> #### 🔹 Community-driven
> 
> 
> 
> #### 🔹 Submit and crack
> 
> 
> 
> #### 🔹 md5decrypt.net
> 
> 
> 
> #### 🔹 MD5 focus
> 
> 
> 
> #### 🔹 Large database
> 
> 
> 
> #### 🔹 OnlineHashCrack
> 
> 
> 
> #### 🔹 Multiple algorithms
> 
> 
> 
> #### 🔹 Free and paid tiers
> 
> 
> 
> #### 🔹 Limitations:
> 
> 
> 
> #### 🔹 Only works for unsalted hashes
> 
> 
> 
> #### 🔹 Limited to common passwords
> 
> 
> 
> #### 🔹 Dictionary-based
> 
> 
> 
> #### 🔹 4. Cryptography Countermeasures
> 
> 
> 
> #### 🔹 4.1 Defending Against Cryptographic Attacks
> 
>
> ---
>
> ### 📍 Page 63
>
> 
> #### 🔹 🛡Cryptographic Defense Strategy
> 
> 
> Implement defense-in-depth with strong algorithms, proper key management, secure implementation, and continuous monitoring.
> 
> 
> #### 🔹 Defense Best Practices:
> 
> 
> 
> #### 🔹 Use Modern Algorithms
> 
> 
> 
> #### 🔹 Symmetric Encryption:
> 
> 
> 
> #### 🔹 AES256 (primary choice)
> 
> 
> 
> #### 🔹 ChaCha20 (alternative)
> 
> 
> 
> #### 🔹 Avoid: DES, 3DES, RC4
> 
> 
> 
> #### 🔹 Asymmetric Encryption:
> 
> 
> 
> #### 🔹 RSA3072 or RSA4096 (transitional)
> 
> 
> 
> #### 🔹 ECC P384 or Curve25519 (preferred)
> 
> 
> 
> #### 🔹 Post-quantum algorithms (future)
> 
> 
> 
> #### 🔹 Hash Functions:
> 
> 
> 
> #### 🔹 SHA256 or SHA512 SHA2 family)
> 
> 
> 
> #### 🔹 SHA3 (alternative)
> 
> 
> 
> #### 🔹 Avoid: MD5, SHA1
> 
> 
> 
> #### 🔹 TLS Versions:
> 
> 
> 
> #### 🔹 TLS 1.3 (strongly recommended)
> 
> 
> 
> #### 🔹 TLS 1.2 (minimum acceptable)
> 
> 
> 
> #### 🔹 Disable: SSL, TLS 1.0, TLS 1.1
> 
> 
> 
> #### 🔹 Strong Key Sizes
> 
> 
> 
> #### 🔹 Minimum Recommendations:
> 
> 
> 
> #### 🔹 AES 256-bit
> 
> 
> 
> #### 🔹 RSA 2048-bit 3072 recommended)
> 
> 
> 
> #### 🔹 ECC 256-bit P256 or better)
> 
>
> ---
>
> ### 📍 Page 64
>
> 
> #### 🔹 Hash: 256-bit output minimum
> 
> 
> 
> #### 🔹 Key Length vs Security:
> 
> 
> 
> #### 🔹 Symmetric RSA ECC Security Bits
> 
> 
> 
> #### 🔹 AES128 3072 256 128
> 
> 
> 
> #### 🔹 AES192 7680 384 192
> 
> 
> 
> #### 🔹 AES256 15360 512 256
> 
> 
> 
> #### 🔹 Password Security
> 
> 
> 
> #### 🔹 Salt Every Password:
> 
> 
> 
> #### 🔹 hash  PBKDF2(password, salt, iterations)
> 
> 
> 
> #### 🔹 Key Derivation Functions:
> 
> 
> 
> #### 🔹 Argon2 (recommended  PHC winner)
> 
> 
> 
> #### 🔹 bcrypt (good for passwords)
> 
> 
> 
> #### 🔹 scrypt (memory-hard)
> 
> 
> 
> #### 🔹 PBKDF2 (minimum acceptable)
> 
> 
> 
> #### 🔹 Iteration Counts:
> 
> 
> 
> #### 🔹 PBKDF2 600,000 iterations 2023 OWASP
> 
> 
> 
> #### 🔹 bcrypt: Cost factor 12
> 
> 
> 
> #### 🔹 Argon2 Adjust based on resources
> 
> 
> 
> #### 🔹 Key Management
> 
> 
> 
> #### 🔹 Key Lifecycle:
> 
> 
> 
> #### 🔹 Generation: Use cryptographically secure RNG
> 
> 
> 
> #### 🔹 Storage: Hardware security modules HSM
> 
> 
> 
> #### 🔹 Distribution: Secure channels only
> 
> 
> 
> #### 🔹 Rotation: Regular key changes
> 
> 
> 
> #### 🔹 Destruction: Secure deletion
> 
> 
> 
> #### 🔹 Key Storage:
> 
>
> ---
>
> ### 📍 Page 65
>
> 
> #### 🔹 Never hardcode keys in source code
> 
> 
> 
> #### 🔹 HSM or TPM for sensitive keys
> 
> 
> 
> #### 🔹 Encrypted storage for less critical keys
> 
> 
> 
> #### 🔹 Environment variables (better than code)
> 
> 
> 
> #### 🔹 Secrets management: HashiCorp Vault, AWS KMS
> 
> 
> 
> #### 🔹 Disable Deprecated Protocols
> 
> 
> 
> #### 🔹 Disable Completely:
> 
> 
> 
> #### 🔹 SSL 2.0, 3.0
> 
> 
> 
> #### 🔹 TLS 1.0, 1.1
> 
> 
> 
> #### 🔹 RC4 cipher
> 
> 
> 
> #### 🔹 MD5 signatures
> 
> 
> 
> #### 🔹 DES, 3DES
> 
> 
> 
> #### 🔹 SHA1 signatures
> 
> 
> 
> #### 🔹 Export-grade ciphers
> 
> 
> 
> #### 🔹 Server Configuration:
> 
> 
> 
> #### 🔹 # Apache
> 
> 
> 
> #### 🔹 SSLProtocol all SSLv2 SSLv3 TLSv1 TLSv1.1
> 
> 
> 
> #### 🔹 SSLCipherSuite HIGH!aNULL!MD5!3DES
> 
> 
> 
> #### 🔹 # Nginx
> 
> 
> 
> #### 🔹 ssl_protocols TLSv1.2 TLSv1.3;
> 
> 
> 
> #### 🔹 ssl_ciphers 'ECDHEECDSAAES128GCMSHA256...';
> 
> 
> 
> #### 🔹 Use Authenticated Encryption
> 
> 
> 
> #### 🔹 AEAD Modes:
> 
> 
> 
> #### 🔹 AESGCM (most common)
> 
> 
> 
> #### 🔹 ChaCha20Poly1305
> 
> 
> 
> #### 🔹 AESCCM
> 
> 
> 
> #### 🔹 Benefits:
> 
>
> ---
>

> [!NOTE]- 📄 **Pages 66 to 70 Syllabus Content**
>
> ### 📍 Page 66
>
> 
> #### 🔹 Confidentiality  Integrity
> 
> 
> 
> #### 🔹 Prevents tampering
> 
> 
> 
> #### 🔹 Protects against padding oracle
> 
> 
> 
> #### 🔹 Proper Padding Validation
> 
> 
> 
> #### 🔹 Constant-Time Validation:
> 
> 
> 
> #### 🔹 No timing differences
> 
> 
> 
> #### 🔹 Same error for all failures
> 
> 
> 
> #### 🔹 Prevents padding oracle
> 
> 
> 
> #### 🔹 Certificate Management
> 
> 
> 
> #### 🔹 Certificate Best Practices:
> 
> 
> 
> #### 🔹 Short validity periods 90 days with automation)
> 
> 
> 
> #### 🔹 Monitor revocations OCSP, CRL
> 
> 
> 
> #### 🔹 Certificate transparency monitoring
> 
> 
> 
> #### 🔹 Automated renewal Let's Encrypt, ACME
> 
> 
> 
> #### 🔹 Prepare for Post-Quantum
> 
> 
> 
> #### 🔹 PQC Strategy:
> 
> 
> 
> #### 🔹 Monitor NIST standards
> 
> 
> 
> #### 🔹 Test PQC algorithms
> 
> 
> 
> #### 🔹 Plan migration timeline
> 
> 
> 
> #### 🔹 Crypto-agility in design
> 
> 
> 
> #### 🔹 Hybrid classical+PQC during transition
> 
> 
> 
> #### 🔹 4.2 Key Stretching
> 
> 
> 
> #### 🔹 🔑Key Stretching / Key Derivation Functions
> 
> 
> Strengthening weak passwords by applying computationally intensive functions, making brute-force attacks significantly slower.
>
> ---
>
> ### 📍 Page 67
>
> 
> #### 🔹 Password Hashing Functions
> 
> 
> 
> #### 🔹 PBKDF2 (Password-Based Key Derivation Function 2)
> 
> 
> 
> #### 🔹 Specifications:
> 
> 
> 
> #### 🔹 Standard: PKCS #5, RFC 2898
> 
> 
> 
> #### 🔹 Method: Iterative HMAC
> 
> 
> 
> #### 🔹 Iterations: 600,000 OWASP 2023
> 
> 
> 
> #### 🔹 Usage:
> 
> 
> 
> #### 🔹 from hashlib import pbkdf2_hmac
> 
> 
> 
> #### 🔹 hash = pbkdf2_hmac(
> 
> 
> 
> #### 🔹 'sha256',           # Hash function
> 
> 
> 
> #### 🔹 password.encode(),  # Password
> 
> 
> 
> #### 🔹 salt,               # Salt 16 bytes)
> 
> 
> 
> #### 🔹 600000              # Iterations
> 
> 
> 
> #### 🔹 )
> 
> 
> 
> #### 🔹 Pros:
> 
> 
> 
> #### 🔹 Widely supported
> 
> 
> 
> #### 🔹 FIPS approved
> 
> 
> 
> #### 🔹 Configurable iterations
> 
> 
> 
> #### 🔹 Cons:
> 
> 
> 
> #### 🔹 Not memory-hard
> 
> 
> 
> #### 🔹 GPU-friendly (can be parallelized)
> 
> 
> 
> #### 🔹 bcrypt
> 
> 
> 
> #### 🔹 Specifications:
> 
> 
> 
> #### 🔹 Based on: Blowfish cipher
> 
> 
> 
> #### 🔹 Cost factor: 2^n iterations (n=1016
> 
> 
> 
> #### 🔹 Recommended: cost  12
> 
> 
> 
> #### 🔹 Usage:
> 
>
> ---
>
> ### 📍 Page 68
>
> 
> #### 🔹 import bcrypt
> 
> 
> 
> #### 🔹 # Hash password
> 
> 
> 
> #### 🔹 salt = bcrypt.gensalt(rounds=12
> 
> 
> 
> #### 🔹 hash = bcrypt.hashpw(password.encode(), salt)
> 
> 
> 
> #### 🔹 # Verify
> 
> 
> 
> #### 🔹 bcrypt.checkpw(password.encode(), hash)
> 
> 
> 
> #### 🔹 Pros:
> 
> 
> 
> #### 🔹 Designed specifically for passwords
> 
> 
> 
> #### 🔹 Adaptive (increase cost over time)
> 
> 
> 
> #### 🔹 Resistant to GPU cracking
> 
> 
> 
> #### 🔹 Cons:
> 
> 
> 
> #### 🔹 Limited parallelization
> 
> 
> 
> #### 🔹 Maximum password length 72 bytes)
> 
> 
> 
> #### 🔹 scrypt
> 
> 
> 
> #### 🔹 Specifications:
> 
> 
> 
> #### 🔹 Memory-hard function
> 
> 
> Parameters: N CPU/memory cost), r (block size), p (parallelization)
> 
> 
> #### 🔹 Recommended: N2^14, r=8, p=1
> 
> 
> 
> #### 🔹 Usage:
> 
> 
> 
> #### 🔹 from hashlib import scrypt
> 
> 
> 
> #### 🔹 hash = scrypt(
> 
> 
> 
> #### 🔹 password.encode(),
> 
> 
> 
> #### 🔹 salt=salt,
> 
> 
> 
> #### 🔹 n=16384,  # 2^14
> 
> 
> 
> #### 🔹 r=8,
> 
> 
> 
> #### 🔹 p=1,
> 
>
> ---
>
> ### 📍 Page 69
>
> 
> #### 🔹 dklen=32
> 
> 
> 
> #### 🔹 )
> 
> 
> 
> #### 🔹 Pros:
> 
> 
> 
> #### 🔹 Memory-hard (resistant to GPUs/ASICs)
> 
> 
> 
> #### 🔹 Configurable parameters
> 
> 
> 
> #### 🔹 Strong resistance to parallel attacks
> 
> 
> 
> #### 🔹 Cons:
> 
> 
> 
> #### 🔹 More complex to configure
> 
> 
> 
> #### 🔹 Can cause DoS if parameters too high
> 
> 
> 
> #### 🔹 Argon2
> 
> 
> 
> #### 🔹 🏆Argon2  RECOMMENDED
> 
> 
> Winner of the Password Hashing Competition 2015, currently the best choice for password hashing with superior resistance to GPU/ASIC attacks.
> 
> 
> #### 🔹 Variants:
> 
> 
> 
> #### 🔹 Argon2d: Faster, data-dependent GPU-resistant)
> 
> 
> 
> #### 🔹 Argon2i: Slower, data-independent (side-channel resistant)
> 
> 
> 
> #### 🔹 Argon2id: Hybrid (recommended for passwords)
> 
> 
> 
> #### 🔹 Parameters:
> 
> 
> 
> #### 🔹 Memory: m KB
> 
> 
> 
> #### 🔹 Iterations: t
> 
> 
> 
> #### 🔹 Parallelism: p
> 
> 
> 
> #### 🔹 Recommended Settings:
> 
> 
> 
> #### 🔹 from argon2 import PasswordHasher
> 
> 
> 
> #### 🔹 ph  PasswordHasher(
> 
> 
> 
> #### 🔹 time_cost=3,        # iterations
> 
>
> ---
>
> ### 📍 Page 70
>
> 
> #### 🔹 memory_cost=65536,  # 64 MB
> 
> 
> 
> #### 🔹 parallelism=4       # threads
> 
> 
> 
> #### 🔹 )
> 
> 
> 
> #### 🔹 hash = ph.hash(password)
> 
> 
> 
> #### 🔹 ph.verify(hash, password)
> 
> 
> 
> #### 🔹 Pros:
> 
> 
> 
> #### 🔹 Memory-hard and CPU-hard
> 
> 
> 
> #### 🔹 Highly resistant to GPUs/ASICs
> 
> 
> 
> #### 🔹 Configurable for different scenarios
> 
> 
> 
> #### 🔹 Side-channel resistant Argon2i/id)
> 
> 
> 
> #### 🔹 PHC winner (industry vetted)
> 
> 
> 
> #### 🔹 Cons:
> 
> 
> 
> #### 🔹 Newer (less legacy support)
> 
> 
> 
> #### 🔹 Requires careful parameter tuning
> 
> 
> 
> #### 🔹 Parameter Selection Guide
> 
> 
> 
> #### 🔹 Target: 0.51 second hashing time per password
> 
> 
> 
> #### 🔹 Low-Resource Devices:
> 
> 
> 
> #### 🔹 PBKDF2 600,000 iterations
> 
> 
> 
> #### 🔹 bcrypt: cost=10
> 
> 
> 
> #### 🔹 Argon2 lower memory 1632 MB
> 
> 
> 
> #### 🔹 Standard Systems:
> 
> 
> 
> #### 🔹 PBKDF2 600,000 iterations
> 
> 
> 
> #### 🔹 bcrypt: cost=12
> 
> 
> 
> #### 🔹 Argon2id: 64 MB memory, 3 iterations
> 
> 
> 
> #### 🔹 High-Security:
> 
> 
> 
> #### 🔹 PBKDF2 1,200,000 iterations
> 
> 
> 
> #### 🔹 bcrypt: cost=14
> 
> 
> 
> #### 🔹 7 0
> 
>
> ---
>

> [!NOTE]- 📄 **Pages 71 to 73 Syllabus Content**
>
> ### 📍 Page 71
>
> 
> #### 🔹 Argon2id: 256 MB memory, 4 iterations
> 
> 
> 
> #### 🔹 Increase Over Time:
> 
> 
> 
> #### 🔹 Moore's Law: Increase cost factor every 2 years
> 
> 
> 
> #### 🔹 Verify login performance
> 
> 
> 
> #### 🔹 Balance security vs usability
> 
>
> ---
>
> ### 📍 Page 72
>
> 
> #### 🔹 ✅Module Summary
> 
> 
> This module covered comprehensive cryptographic principles and
> 
> 
> #### 🔹 practices:
> 
> 
> 
> #### 🔹 Key Takeaways:
> 
> 
> 
> #### 🔹 Cryptography Fundamentals  Confidentiality, integrity,
> 
> 
> 
> #### 🔹 authentication, non-repudiation; symmetric vs asymmetric
> 
> 
> 
> #### 🔹 encryption
> 
> 
> 
> #### 🔹 Symmetric Algorithms  AES (industry standard), DES/3DES
> 
> 
> 
> #### 🔹 (deprecated), Blowfish/Twofish, ChaCha20, cipher modes ECB
> 
> 
> 
> #### 🔹 insecure, CBC, CTR, GCM recommended)
> 
> 
> 
> #### 🔹 Asymmetric Algorithms  RSA 2048 bits), ECC 256 bits),
> 
> 
> 
> #### 🔹 Diffie-Hellman key exchange, post-quantum threats
> 
> 
> Hash Functions  MD5/SHA1 broken, SHA2 (current standard),
> 
> 
> #### 🔹 SHA3 (alternative), HMAC for authentication
> 
> 
> 
> #### 🔹 PKI & Digital Certificates  Certificate authorities, X.509
> 
> 
> certificates, digital signatures, chain of trust, certificate validation
> 
> 
> #### 🔹 SSL/TLS  SSL deprecated, TLS 1.2 minimum, TLS 1.3
> 
> 
> 
> #### 🔹 recommended, forward secrecy, authenticated encryption
> 
> 
> 
> #### 🔹 Cryptographic Applications  PGP/GPG email encryption,
> 
> 
> S/MIME, disk encryption BitLocker, FileVault, VeraCrypt, LUKS,
> 
> 
> #### 🔹 blockchain
> 
> 
> Cryptanalysis Attacks  Brute-force, rainbow tables (defense: salt + key stretching), birthday attacks, side-channel attacks,
> 
> 
> #### 🔹 padding oracle, hash collisions
> 
> 
> 
> #### 🔹 Advanced Threats  Quantum computing Shor's algorithm
> 
> 
> 
> #### 🔹 breaks RSA/ECC, DROWN, DUHK, related-key attacks, timing
> 
> 
> 
> #### 🔹 attacks
> 
> 
> 
> #### 🔹 Password Security  Argon2 (recommended), bcrypt, scrypt,
> 
> 
> 
> #### 🔹 PBKDF2, salt requirements (random, unique, 16 bytes), key
> 
> 
> 
> #### 🔹 stretching (slow down brute-force)
> 
> 
> 
> #### 🔹 Key Management  Secure generation, HSM/TPM storage,
> 
> 
> 
> #### 🔹 regular rotation, secure distribution, proper destruction
> 
>
> ---
>
> ### 📍 Page 73
>
> 
> #### 🔹 Best Practices  Use AES256, SHA256, TLS 1.3,
> 
> 
> authenticated encryption GCM, disable deprecated protocols SSL, TLS 1.0/1.1, strong key sizes, constant-time implementations
> 
> 
> #### 🔹 Cryptanalysis Tools  Hashcat GPU, John the Ripper CPU,
> 
> 
> 
> #### 🔹 rainbow table generators, online hash crackers
> 
> 
> 
> #### 🔹 Post-Quantum Cryptography  NIST standards CRYSTALS
> 
> 
> Kyber, Dilithium, FALCON, hybrid mode during transition, crypto-
> 
> 
> #### 🔹 agility
> 
> 
> Cryptography is the foundation of information security, providing confidentiality, integrity, authentication, and non-repudiation. Effective cryptographic implementation requires selecting proven algorithms, using sufficient key lengths, proper key management, secure random number generation, and regular updates to address
> 
> 
> #### 🔹 emerging threats. The quantum computing threat necessitates
> 
> 
> planning for post-quantum cryptography migration. Organizations must balance security with performance, follow industry standards NIST, OWASP, implement defense-in-depth, and maintain crypto- agility for future algorithm transitions.
> 
> 
> #### 🔹 7 3
> 
>
> ---
>
