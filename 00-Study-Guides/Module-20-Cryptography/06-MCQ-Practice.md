# 🎯 Module 20: Cryptography - Exam Scenario Practice Engine

> [!ABSTRACT] 📊 **Interactive Module Scorecard**
>
> - **Target Module**: Module 20: Cryptography
> - **Total Questions**: 25 Ultra-Detailed, 100% Unique Indirect Scenarios
> - **Exam Difficulty Standard**: Senior CEH v13 (Scenario-Driven Logic & Technical Deduction)
> - **Passing Threshold**: 85% Accuracy (22/25 Correct)
> 
> *Instructions: Evaluate the scenario context below. Select your choice, then expand the **Show Correct Answer & Exam Breakdown** callout to verify your answer and review the deep technical analysis and distractor refutations.*

---

### 🧩 Question 01 | Scenario Challenge

> [!QUESTION] 📌 **Scenario Context**
> A network security team captures encrypted TLS traffic sessions recorded from an enterprise web server over six months. An attacker later steals the web server's long-term RSA private key. Despite holding the private key, the attacker CANNOT retroactively decrypt the recorded traffic sessions.
>
> What cryptographic property and key exchange mechanism protected the historical traffic?

#### 🔘 Available Options:

- **A**: Perfect Forward Secrecy (PFS) achieved via Ephemeral Diffie-Hellman (ECDHE) key exchange
- **B**: Using MD5 hash functions
- **C**: Encrypting files using ECB mode
- **D**: Disabling X.509 digital certificates

> [!SUCCESS]- 🔑 **Show Correct Answer & Exam Breakdown**
> **Correct Answer**: **Option A**
>
> #### 💡 Technical Deep Dive:
> Perfect Forward Secrecy (PFS) generates ephemeral session keys per transaction (e.g., via ECDHE) that are never derived from the server's long-term static private key, rendering past recorded sessions unbreakable even if the private key is later stolen.
>
> #### 🚫 Distractor Analysis & Refutations:
>
> - **Option B is incorrect** because MD5 is a broken hashing algorithm, not key exchange.
> - **Option C is incorrect** because ECB mode is an insecure block cipher mode.
> - **Option D is incorrect** because disabling certificates destroys trust verification.

---

### 🧩 Question 02 | Scenario Challenge

> [!QUESTION] 📌 **Scenario Context**
> An attacker attempts to exploit a hash function digest length of 128 bits. The attacker relies on the mathematical probability that finding ANY two distinct random inputs ($x_1 
eq x_2$) that produce the exact same hash output ($H(x_1) = H(x_2)$) requires only approximately $2^{64}$ evaluations.
>
> What cryptanalytic attack methodology is being conducted?

#### 🔘 Available Options:

- **A**: Birthday Attack (Exploiting Birthday Paradox Collision Probability)
- **B**: Padding Oracle Attack
- **C**: Man-in-the-Middle Attack
- **D**: Known-Plaintext Attack

> [!SUCCESS]- 🔑 **Show Correct Answer & Exam Breakdown**
> **Correct Answer**: **Option A**
>
> #### 💡 Technical Deep Dive:
> The Birthday Attack targets hash function collision resistance based on the Birthday Paradox, reducing the effort to find collisions to $2^{n/2}$ where $n$ is the digest length.
>
> #### 🚫 Distractor Analysis & Refutations:
>
> - **Option B is incorrect** because Padding Oracle attacks manipulate CBC cipher padding errors.
> - **Option C is incorrect** because MitM intercepts network communication channels.
> - **Option D is incorrect** because Known-Plaintext compares plaintext/ciphertext samples.

---

### 🧩 Question 03 | Scenario Challenge

> [!QUESTION] 📌 **Scenario Context**
> An organization encrypts sensitive customer bitmap images using AES in Electronic Codebook (ECB) mode. Although the raw image data is encrypted, an observer can clearly discern the high-level visual outlines and patterns of the original image.
>
> Why does ECB mode produce this visual vulnerability?

#### 🔘 Available Options:

- **A**: ECB mode encrypts each plaintext block independently using the exact same key, causing identical plaintext blocks to produce identical ciphertext blocks
- **B**: ECB mode uses a 24-bit static IV
- **C**: ECB mode relies on MD5 hashing
- **D**: ECB mode requires public key certificates

> [!SUCCESS]- 🔑 **Show Correct Answer & Exam Breakdown**
> **Correct Answer**: **Option A**
>
> #### 💡 Technical Deep Dive:
> ECB mode lacks diffusion and initial vectors; identical 16-byte plaintext blocks yield identical ciphertext blocks, preserving structural patterns.
>
> #### 🚫 Distractor Analysis & Refutations:
>
> - **Option B is incorrect** because IVs are used in modes like CBC and CTR, not ECB.
> - **Option C is incorrect** because ECB is a block cipher mode, not a hash algorithm.
> - **Option D is incorrect** because block cipher modes do not mandate PKI certificates.

---

### 🧩 Question 04 | Scenario Challenge

> [!QUESTION] 📌 **Scenario Context**
> What open-source steganography command-line utility allows users to embed secret files inside JPEG, BMP, WAV, or AU carrier files using a passphrase, as well as extract embedded payloads?

#### 🔘 Available Options:

- **A**: Steghide
- **B**: OpenSSL
- **C**: Hashcat
- **D**: VeraCrypt

> [!SUCCESS]- 🔑 **Show Correct Answer & Exam Breakdown**
> **Correct Answer**: **Option A**
>
> #### 💡 Technical Deep Dive:
> Steghide is a popular open-source steganography tool used to embed or extract hidden data within image and audio files.
>
> #### 🚫 Distractor Analysis & Refutations:
>
> - **Option B is incorrect** because OpenSSL performs cryptography, not steganography.
> - **Option C is incorrect** because Hashcat cracks password hashes.
> - **Option D is incorrect** because VeraCrypt provides disk volume encryption.

---

### 🧩 Question 05 | Scenario Challenge

> [!QUESTION] 📌 **Scenario Context**
> An application verifies client requests by calculating `HMAC-SHA256(SecretKey, RequestPayload)`.
>
> What dual security guarantees does HMAC provide?

#### 🔘 Available Options:

- **A**: Message Data Integrity and Message Origin Authentication
- **B**: Public Key Encryption and Non-Repudiation
- **C**: Confidentiality and Anonymity
- **D**: Password Hashing and Key Escrow

> [!SUCCESS]- 🔑 **Show Correct Answer & Exam Breakdown**
> **Correct Answer**: **Option A**
>
> #### 💡 Technical Deep Dive:
> HMAC combines a cryptographic key with a hash function, verifying both that data has not been modified (Integrity) and that it was generated by a holder of the secret key (Authentication).
>
> #### 🚫 Distractor Analysis & Refutations:
>
> - **Option B is incorrect** because HMAC is symmetric and does not use asymmetric public keys.
> - **Option C is incorrect** because HMAC does not encrypt data payload contents.
> - **Option D is incorrect** because HMAC is not designed for password storage hashing.

---

### 🧩 Question 06 | Scenario Challenge

> [!QUESTION] 📌 **Scenario Context**
> A web browser validates a website's X.509 digital certificate in real-time by querying a specialized online responder to check if the certificate has been revoked before expiration, without downloading massive revocation files.
>
> What protocol is the browser utilizing?

#### 🔘 Available Options:

- **A**: Online Certificate Status Protocol (OCSP)
- **B**: Certificate Revocation List (CRL)
- **C**: Simple Mail Transfer Protocol (SMTP)
- **D**: Domain Name System (DNS)

> [!SUCCESS]- 🔑 **Show Correct Answer & Exam Breakdown**
> **Correct Answer**: **Option A**
>
> #### 💡 Technical Deep Dive:
> OCSP provides real-time revocation status checks for X.509 certificates over HTTP without requiring client downloads of large CRL files.
>
> #### 🚫 Distractor Analysis & Refutations:
>
> - **Option B is incorrect** because CRL requires downloading periodically published complete lists.
> - **Option C is incorrect** because SMTP transfers emails.
> - **Option D is incorrect** because DNS resolves domain names.

---

### 🧩 Question 07 | Scenario Challenge

> [!QUESTION] 📌 **Scenario Context**
> What asymmetric encryption standard relies mathematically on the computational difficulty of solving the Elliptic Curve Discrete Logarithm Problem (ECDLP), offering equivalent 3072-bit RSA security with only a 256-bit key length?

#### 🔘 Available Options:

- **A**: Elliptic Curve Cryptography (ECC)
- **B**: Advanced Encryption Standard (AES)
- **C**: Data Encryption Standard (DES)
- **D**: MD5

> [!SUCCESS]- 🔑 **Show Correct Answer & Exam Breakdown**
> **Correct Answer**: **Option A**
>
> #### 💡 Technical Deep Dive:
> ECC provides ultra-strong security with much smaller key sizes compared to RSA due to the hardness of ECDLP.
>
> #### 🚫 Distractor Analysis & Refutations:
>
> - **Option B is incorrect** because AES is a symmetric block cipher.
> - **Option C is incorrect** because DES is an obsolete 56-bit symmetric cipher.
> - **Option D is incorrect** because MD5 is a broken hashing function.

---

### 🧩 Question 08 | Scenario Challenge

> [!QUESTION] 📌 **Scenario Context**
> An attacker intercepts a web application's encrypted session cookie encoded with AES in Cipher Block Chaining (CBC) mode with PKCS#7 padding. By repeatedly modifying the ciphertext bytes and observing distinct HTTP 500 (Padding Error) vs HTTP 200 responses, the attacker decrypts the entire cookie.
>
> What attack vector was executed?

#### 🔘 Available Options:

- **A**: Padding Oracle Attack
- **B**: Birthday Attack
- **C**: Key Logger Attack
- **D**: Rainbow Table Attack

> [!SUCCESS]- 🔑 **Show Correct Answer & Exam Breakdown**
> **Correct Answer**: **Option A**
>
> #### 💡 Technical Deep Dive:
> Padding Oracle attacks exploit side-channel leakage of cryptographic padding validation error messages in CBC mode.
>
> #### 🚫 Distractor Analysis & Refutations:
>
> - **Option B is incorrect** because Birthday attacks target hash collisions.
> - **Option C is incorrect** because Key Loggers record keystrokes.
> - **Option D is incorrect** because Rainbow Tables crack pre-computed password hashes.

---

### 🧩 Question 09 | Scenario Challenge

> [!QUESTION] 📌 **Scenario Context**
> What modern cipher mode provides both data confidentiality and built-in message integrity/authentication (Authenticated Encryption with Associated Data - AEAD) without needing a separate HMAC?

#### 🔘 Available Options:

- **A**: AES-GCM (Galois/Counter Mode)
- **B**: AES-ECB
- **C**: DES-CBC
- **D**: RC4

> [!SUCCESS]- 🔑 **Show Correct Answer & Exam Breakdown**
> **Correct Answer**: **Option A**
>
> #### 💡 Technical Deep Dive:
> AES-GCM combines counter mode encryption with a Galois field authentication tag to provide AEAD protection.
>
> #### 🚫 Distractor Analysis & Refutations:
>
> - **Option B is incorrect** because ECB lacks authentication and IVs.
> - **Option C is incorrect** because DES-CBC lacks authentication.
> - **Option D is incorrect** because RC4 is an unauthenticated stream cipher.

---

### 🧩 Question 10 | Scenario Challenge

> [!QUESTION] 📌 **Scenario Context**
> What dedicated physical hardware device stores master encryption keys and performs high-speed cryptographic operations inside a tamper-evident physical enclosure?

#### 🔘 Available Options:

- **A**: Hardware Security Module (HSM)
- **B**: USB Flash Drive
- **C**: Software Load Balancer
- **D**: Solid State Drive (SSD)

> [!SUCCESS]- 🔑 **Show Correct Answer & Exam Breakdown**
> **Correct Answer**: **Option A**
>
> #### 💡 Technical Deep Dive:
> HSMs are specialized physical computing devices that safeguard and manage digital keys for strong authentication and crypto operations.
>
> #### 🚫 Distractor Analysis & Refutations:
>
> - **Option B is incorrect** because standard USB drives lack tamper protection.
> - **Option C is incorrect** because load balancers distribute web traffic.
> - **Option D is incorrect** because SSDs provide general storage.

---

### 🧩 Question 11 | Scenario Challenge

> [!QUESTION] 📌 **Scenario Context**
> An administrator executes `openssl enc -aes-256-cbc -salt -pbkdf2 -in secret.doc -out secret.enc` on a Linux terminal.
>
> What operation was performed?

#### 🔘 Available Options:

- **A**: Encrypting `secret.doc` using AES-256 in CBC mode with PBKDF2 key derivation
- **B**: Deleting the file permanently
- **C**: Generating an SSL X.509 certificate
- **D**: Cracking a password hash

> [!SUCCESS]- 🔑 **Show Correct Answer & Exam Breakdown**
> **Correct Answer**: **Option A**
>
> #### 💡 Technical Deep Dive:
> `openssl enc` performs symmetric cipher operations; `-aes-256-cbc` specifies the algorithm and mode, and `-pbkdf2` uses password-based key derivation.
>
> #### 🚫 Distractor Analysis & Refutations:
>
> - **Option B is incorrect** because `openssl enc` does not delete files.
> - **Option C is incorrect** because certificate generation uses `openssl req` or `openssl x509`.
> - **Option D is incorrect** because hash cracking requires tools like Hashcat.

---

### 🧩 Question 12 | Scenario Challenge

> [!QUESTION] 📌 **Scenario Context**
> What open-source utility allows users to create transparent, encrypted disk volumes (containers) or encrypt entire hard drives using ciphers like AES, Twofish, and Serpent?

#### 🔘 Available Options:

- **A**: VeraCrypt
- **B**: Steghide
- **C**: Wireshark
- **D**: Airgeddon

> [!SUCCESS]- 🔑 **Show Correct Answer & Exam Breakdown**
> **Correct Answer**: **Option A**
>
> #### 💡 Technical Deep Dive:
> VeraCrypt is a free open-source disk encryption software based on TrueCrypt.
>
> #### 🚫 Distractor Analysis & Refutations:
>
> - **Option B is incorrect** because Steghide is for image/audio steganography.
> - **Option C is incorrect** because Wireshark is a packet sniffer.
> - **Option D is incorrect** because Airgeddon audits Wi-Fi networks.

---

### 🧩 Question 13 | Scenario Challenge

> [!QUESTION] 📌 **Scenario Context**
> Why are SHA-1 and MD5 cryptographic hash functions banned from modern security standards like PCI-DSS and NIST guidelines?

#### 🔘 Available Options:

- **A**: Practical collision attacks have been demonstrated (e.g., SHAttered and Flame malware), allowing two different inputs to generate identical hash digests
- **B**: They run too slowly on modern CPUs
- **C**: They require public key infrastructure
- **D**: They only run on 32-bit hardware

> [!SUCCESS]- 🔑 **Show Correct Answer & Exam Breakdown**
> **Correct Answer**: **Option A**
>
> #### 💡 Technical Deep Dive:
> Collision attacks against MD5 and SHA-1 make them fundamentally insecure for digital signatures and certificates.
>
> #### 🚫 Distractor Analysis & Refutations:
>
> - **Option B is incorrect** because MD5/SHA-1 are actually extremely fast (which makes password hashing with them weak too).
> - **Option C is incorrect** because hash functions do not require PKI.
> - **Option D is incorrect** because hash functions are architecture independent.

---

### 🧩 Question 14 | Scenario Challenge

> [!QUESTION] 📌 **Scenario Context**
> What term describes hiding secret messages or files inside another non-secret medium (such as an image or audio file) so that the very existence of the secret message is concealed?

#### 🔘 Available Options:

- **A**: Steganography
- **B**: Cryptanalysis
- **C**: Encapsulation
- **D**: Compression

> [!SUCCESS]- 🔑 **Show Correct Answer & Exam Breakdown**
> **Correct Answer**: **Option A**
>
> #### 💡 Technical Deep Dive:
> Steganography is the practice of concealing a file, message, image, or video within another medium.
>
> #### 🚫 Distractor Analysis & Refutations:
>
> - **Option B is incorrect** because Cryptanalysis is the study of breaking ciphers.
> - **Option C is incorrect** because Encapsulation wraps network protocol headers.
> - **Option D is incorrect** because Compression reduces file size.

---

### 🧩 Question 15 | Scenario Challenge

> [!QUESTION] 📌 **Scenario Context**
> In a Public Key Infrastructure (PKI), what entity is responsible for verifying identity requests and issuing signed X.509 digital certificates to users or servers?

#### 🔘 Available Options:

- **A**: Certificate Authority (CA)
- **B**: Key Distribution Center (KDC)
- **C**: Domain Name Registrar
- **D**: Web Application Firewall

> [!SUCCESS]- 🔑 **Show Correct Answer & Exam Breakdown**
> **Correct Answer**: **Option A**
>
> #### 💡 Technical Deep Dive:
> A Certificate Authority (CA) acts as the trusted anchor in PKI, issuing and signing digital certificates.
>
> #### 🚫 Distractor Analysis & Refutations:
>
> - **Option B is incorrect** because KDC manages Kerberos authentication tickets.
> - **Option C is incorrect** because Domain Registrars manage domain name registrations.
> - **Option D is incorrect** because WAF filters web traffic.

---

### 🧩 Question 16 | Scenario Challenge

> [!QUESTION] 📌 **Scenario Context**
> What mathematical problem provides the foundational security assumption for the RSA public-key cryptosystem?

#### 🔘 Available Options:

- **A**: Prime Factorization Problem (Difficulty of factoring large prime products $n = p 	imes q$)
- **B**: Elliptic Curve Discrete Logarithm Problem
- **C**: Collision Resistance
- **D**: Linear Feedback Shift Registers

> [!SUCCESS]- 🔑 **Show Correct Answer & Exam Breakdown**
> **Correct Answer**: **Option A**
>
> #### 💡 Technical Deep Dive:
> RSA security relies on the difficulty of factoring the product of two large prime numbers ($n = p \cdot q$).
>
> #### 🚫 Distractor Analysis & Refutations:
>
> - **Option B is incorrect** because ECDLP is the basis of ECC.
> - **Option C is incorrect** because Collision Resistance is a property of hash functions.
> - **Option D is incorrect** because LFSRs are used in stream ciphers.

---

### 🧩 Question 17 | Scenario Challenge

> [!QUESTION] 📌 **Scenario Context**
> An attacker records encrypted data transmissions and later re-sends the exact captured packet sequence to impersonate a legitimate user authentication request.
>
> What attack vector was executed, and what mechanism defends against it?

#### 🔘 Available Options:

- **A**: Replay Attack; defended against using Nonces, Timestamps, and Session Sequence Numbers
- **B**: Padding Oracle Attack; defended against using RSA
- **C**: Birthday Attack; defended against using SHA-1
- **D**: Man-in-the-Middle; defended against using WEP

> [!SUCCESS]- 🔑 **Show Correct Answer & Exam Breakdown**
> **Correct Answer**: **Option A**
>
> #### 💡 Technical Deep Dive:
> Replay attacks involve re-transmitting captured valid packets. Including cryptographic nonces or timestamps invalidates old replayed requests.
>
> #### 🚫 Distractor Analysis & Refutations:
>
> - **Option B is incorrect** because Padding Oracle attacks exploit padding errors.
> - **Option C is incorrect** because Birthday attacks target hash collisions.
> - **Option D is incorrect** because WEP is an obsolete wireless encryption standard.

---

### 🧩 Question 18 | Scenario Challenge

> [!QUESTION] 📌 **Scenario Context**
> What key size options are natively supported by the Advanced Encryption Standard (AES)?

#### 🔘 Available Options:

- **A**: 128, 192, and 256 bits
- **B**: 56, 64, and 128 bits
- **C**: 512, 1024, and 2048 bits
- **D**: 40, 64, and 80 bits

> [!SUCCESS]- 🔑 **Show Correct Answer & Exam Breakdown**
> **Correct Answer**: **Option A**
>
> #### 💡 Technical Deep Dive:
> AES (FIPS 197) specifies key lengths of 128, 192, or 256 bits with a fixed 128-bit block size.
>
> #### 🚫 Distractor Analysis & Refutations:
>
> - **Option B is incorrect** because 56-bit key length belongs to DES.
> - **Option C is incorrect** because 1024/2048-bit keys are used in asymmetric RSA.
> - **Option D is incorrect** because 40-bit key length is legacy export-grade RC4.

---

### 🧩 Question 19 | Scenario Challenge

> [!QUESTION] 📌 **Scenario Context**
> What digital certificate standard defines the structural format for public key certificates, including fields like Subject, Issuer, Validity Period, and Public Key?

#### 🔘 Available Options:

- **A**: X.509
- **B**: POSIX
- **C**: ISO 27001
- **D**: IEEE 802.11

> [!SUCCESS]- 🔑 **Show Correct Answer & Exam Breakdown**
> **Correct Answer**: **Option A**
>
> #### 💡 Technical Deep Dive:
> ITU-T X.509 specifies standard formats for public key certificates and certification path validation.
>
> #### 🚫 Distractor Analysis & Refutations:
>
> - **Option B is incorrect** because POSIX defines operating system API interfaces.
> - **Option C is incorrect** because ISO 27001 is an information security management framework.
> - **Option D is incorrect** because IEEE 802.11 defines Wi-Fi standards.

---

### 🧩 Question 20 | Scenario Challenge

> [!QUESTION] 📌 **Scenario Context**
> What browser-accessible web application, known as the "Cyber Swiss Army Knife", allows security analysts to dynamically perform chaining operations for encoding, decoding, hashing, and encryption?

#### 🔘 Available Options:

- **A**: CyberChef
- **B**: Wireshark
- **C**: Burp Suite
- **D**: Metasploit

> [!SUCCESS]- 🔑 **Show Correct Answer & Exam Breakdown**
> **Correct Answer**: **Option A**
>
> #### 💡 Technical Deep Dive:
> CyberChef (developed by GCHQ) is an open-source web application for analyzing and manipulating data formats, encodings, and ciphers.
>
> #### 🚫 Distractor Analysis & Refutations:
>
> - **Option B is incorrect** because Wireshark is a packet sniffer.
> - **Option C is incorrect** because Burp Suite is a web security testing proxy.
> - **Option D is incorrect** because Metasploit is an exploitation framework.

---

### 🧩 Question 21 | Scenario Challenge

> [!QUESTION] 📌 **Scenario Context**
> What cryptanalytic attack scenario assumes the attacker has acquired access to both the unencrypted original message (plaintext) and its corresponding encrypted output (ciphertext)?

#### 🔘 Available Options:

- **A**: Known-Plaintext Attack (KPA)
- **B**: Ciphertext-Only Attack
- **C**: Rubber Hose Cryptanalysis
- **D**: Social Engineering

> [!SUCCESS]- 🔑 **Show Correct Answer & Exam Breakdown**
> **Correct Answer**: **Option A**
>
> #### 💡 Technical Deep Dive:
> In a Known-Plaintext Attack, the analyst has access to pairs of plaintext and matching ciphertext to reveal secret keys or cipher structures.
>
> #### 🚫 Distractor Analysis & Refutations:
>
> - **Option B is incorrect** because Ciphertext-Only assumes access ONLY to ciphertext.
> - **Option C is incorrect** because Rubber Hose involves coercion/interrogation.
> - **Option D is incorrect** because Social Engineering targets human manipulation.

---

### 🧩 Question 22 | Scenario Challenge

> [!QUESTION] 📌 **Scenario Context**
> Why is RC4 considered an obsolete stream cipher that must be disabled in modern web servers and wireless networks?

#### 🔘 Available Options:

- **A**: Severe keystream biases (such as Fluhrer, Mantin, and Shamir flaws) allow attackers to decrypt traffic by analyzing millions of connections
- **B**: It requires 4096-bit keys
- **C**: It requires hardware chips
- **D**: It only runs on Windows

> [!SUCCESS]- 🔑 **Show Correct Answer & Exam Breakdown**
> **Correct Answer**: **Option A**
>
> #### 💡 Technical Deep Dive:
> RC4 exhibits statistical biases in initial output bytes, leading to practical decryption attacks in WEP and TLS.
>
> #### 🚫 Distractor Analysis & Refutations:
>
> - **Option B is incorrect** because RC4 uses variable key sizes up to 2048 bits.
> - **Option C is incorrect** because RC4 is a pure software stream cipher.
> - **Option D is incorrect** because RC4 is platform independent.

---

### 🧩 Question 23 | Scenario Challenge

> [!QUESTION] 📌 **Scenario Context**
> What emerging field of cryptography focuses on developing algorithms that remain secure against cryptanalytic attacks launched by powerful future Quantum Computers (such as Shor's algorithm)?

#### 🔘 Available Options:

- **A**: Post-Quantum Cryptography (PQC) / Quantum-Resistant Cryptography
- **B**: Symmetric Cryptography
- **C**: Steganography
- **D**: Classical Cryptography

> [!SUCCESS]- 🔑 **Show Correct Answer & Exam Breakdown**
> **Correct Answer**: **Option A**
>
> #### 💡 Technical Deep Dive:
> Post-Quantum Cryptography (PQC) targets mathematical problems (e.g., lattice-based cryptography) that quantum computers running Shor's algorithm cannot solve efficiently.
>
> #### 🚫 Distractor Analysis & Refutations:
>
> - **Option B is incorrect** because symmetric ciphers are classical, though key lengths must double for Grover's algorithm.
> - **Option C is incorrect** because steganography hides data existence.
> - **Option D is incorrect** because classical cryptography includes vulnerable RSA/ECC algorithms.

---

### 🧩 Question 24 | Scenario Challenge

> [!QUESTION] 📌 **Scenario Context**
> What asymmetric key distribution algorithm allows two remote parties with no prior shared secrets to establish a shared secret key over an insecure public channel?

#### 🔘 Available Options:

- **A**: Diffie-Hellman (DH) Key Exchange
- **B**: AES-256
- **C**: MD5
- **D**: SHA-256

> [!SUCCESS]- 🔑 **Show Correct Answer & Exam Breakdown**
> **Correct Answer**: **Option A**
>
> #### 💡 Technical Deep Dive:
> Diffie-Hellman key exchange enables two parties to negotiate a shared secret over an unencrypted channel.
>
> #### 🚫 Distractor Analysis & Refutations:
>
> - **Option B is incorrect** because AES requires a pre-shared key.
> - **Option C is incorrect** because MD5 is a hashing algorithm.
> - **Option D is incorrect** because SHA-256 is a hashing algorithm.

---

### 🧩 Question 25 | Scenario Challenge

> [!QUESTION] 📌 **Scenario Context**
> What technique embeds watermark metadata into digital media files (images, audio, video) to prove intellectual property ownership and track illegal distribution without interfering with normal playback?

#### 🔘 Available Options:

- **A**: Digital Watermarking
- **B**: Full Disk Encryption
- **C**: Password Salting
- **D**: Memory Paging

> [!SUCCESS]- 🔑 **Show Correct Answer & Exam Breakdown**
> **Correct Answer**: **Option A**
>
> #### 💡 Technical Deep Dive:
> Digital Watermarking embeds identification signals directly into digital media for copyright protection.
>
> #### 🚫 Distractor Analysis & Refutations:
>
> - **Option B is incorrect** because Full Disk Encryption encrypts storage drives.
> - **Option C is incorrect** because Password Salting protects password hashes against rainbow tables.
> - **Option D is incorrect** because Memory Paging manages OS virtual memory.
