# 02. Attack Techniques — Cryptography

> [!WARNING] ⚡ **Exploitation Methodologies & Execution Scenarios**
> Direct extraction from official CEH v13 Syllabus (Module 20). Covers Cryptanalysis, Hash Collision Attacks, OpenSSL Command Execution, Steganography Extraction, and Password Hash Cracking.

---

## ⚔️ 1. Primary Cryptographic Exploitation Workflows

### 1.1 OpenSSL Cryptographic Operation Syntax
```bash
# 1. Generate RSA 4096-bit Private Key
openssl genrsa -out private.key 4096

# 2. Extract Public Key from Private Key
openssl rsa -in private.key -pubout -out public.key

# 3. Encrypt file using AES-256-CBC with password PBKDF2 key derivation
openssl enc -aes-256-cbc -salt -pbkdf2 -in confidential.txt -out confidential.enc

# 4. Decrypt encrypted file using OpenSSL
openssl enc -d -aes-256-cbc -pbkdf2 -in confidential.enc -out decrypted.txt
```

### 1.2 Steganography Payload Concealment & Extraction
Steganography hides secret data inside carrier files (images, audio) without altering visual appearance (e.g., Least Significant Bit - LSB insertion).

```bash
# Embed hidden file inside image using Steghide
steghide embed -cf carrier.jpg -ef secret.txt -sf stego_image.jpg -p Password123

# Extract hidden payload from stego image
steghide extract -sf stego_image.jpg -p Password123
```

> [!DANGER] 🛡️ **📋 Comprehensive Cryptographic Attack Execution Matrix**

| Attack Type | Target Component | Command / Tool Syntax | Technical Outcome |
| :--- | :--- | :--- | :--- |
| **Stego Extraction** | Carrier JPEG | `steghide extract -sf image.jpg` | Recovers hidden text files |
| **Hash Cracking** | NTLM / SHA-256 | `hashcat -m 1000 hashes.txt wordlist.txt` | Discloses cleartext passwords |
| **Padding Oracle** | CBC Ciphers | `padbuster http://target/page.aspx ...` | Decrypts ciphertext block-by-block |
| **Rogue CA Spoofing**| X.509 Certificates | Compromised Private Key of Sub-CA | Man-in-the-Middle TLS inspection |
