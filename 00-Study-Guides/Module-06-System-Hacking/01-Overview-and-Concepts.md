# 01. Overview and Concepts — System Hacking

> [!INFO] 📌 **Module Scope & Core Objectives**
> Direct technical extraction from official CEH v13 Syllabus (Module 06). Covers CEH System Hacking Methodology (Gaining Access, Escalating Privileges, Maintaining Access, Clearing Tracks), Password Cracking Attacks (NTLM, Kerberos, Rainbow Tables), Buffer Overflow Architecture, Privilege Escalation Vectors (Windows/Linux), Rootkit Mechanics, and Anti-Forensics (Log Wiping, NTFS Alternate Data Streams).

---

## 🧠 1. The 4-Phase System Hacking Methodology

### 1.1 Detailed Analysis of System Hacking Phases
System Hacking is the fifth core phase of ethical hacking. Once an attacker completes footprinting, scanning, and vulnerability assessment, they launch direct exploitation probes against target operating systems and endpoints to achieve system compromise.

#### 1. Phase 1: Gaining Access (Exploitation)
Translating identified vulnerabilities into active system entry points. Attackers execute exploits (e.g., buffer overflows, web exploits, password cracking, client-side phishing) to execute arbitrary code and establish an initial unprivileged or privileged shell (e.g., Meterpreter, PowerShell session).

#### 2. Phase 2: Escalating Privileges
Leveraging local system misconfigurations, unpatched kernel vulnerabilities, elevated privileges (SUID binaries, Unquoted Service Paths), or token impersonation (JuicyPotato, RoguePotato) to elevate access from a standard low-privilege user account to `NT AUTHORITY\SYSTEM` (Windows) or `root` (Linux).

#### 3. Phase 3: Maintaining Access (Persistence)
Deploying persistent backdoors, Remote Access Trojans (RATs), rootkits, keyloggers, or scheduled tasks (`cron`, Windows Task Scheduler) to ensure long-term, unauthenticated remote access across system reboots.

#### 4. Phase 4: Clearing Tracks (Anti-Forensics)
Disabling event auditing, wiping event logs (`wevtutil`), scrubbing shell histories (`.bash_history`), hiding files using NTFS Alternate Data Streams (ADS) or steganography, and modifying file timestamps (Timestomping) to evade forensic attribution.

> [!ABSTRACT] 🏛️ **📋 Comprehensive System Hacking Methodology Reference Matrix**

| System Hacking Phase | Operational Objective | Dominant Attack Vectors | Key Tools & Utilities |
| :--- | :--- | :--- | :--- |
| **1. Gaining Access** | Execute exploit & obtain initial shell | Buffer overflow, password cracking, web RCE | Metasploit, Hydra, Mimikatz |
| **2. Escalating Privileges**| Elevate to `SYSTEM` or `root` | SUID binaries, Unquoted paths, Token impersonation | LinPEAS, WinPEAS, Potato exploits |
| **3. Maintaining Access** | Establish persistent backdoor control | RATs, user/kernel rootkits, scheduled tasks | Meterpreter, Cobalt Strike, Netcat |
| **4. Clearing Tracks** | Wipe forensic audit evidence | Clearing event logs, hiding files via ADS, timestomping | `wevtutil`, Meterpreter `timestomp` |

---

## ⚡ 2. Password Cracking Mechanics & Authentication Protocols

### 2.1 Password Hash Types & Attack Classifications

#### Authentication Protocols & Hashes:
- **NTLM (NT LAN Manager)**: Windows default password hash format (MD4 hash of UTF-16LE password). Highly vulnerable to Pass-the-Hash and offline rainbow table attacks.
- **Kerberos**: Default Active Directory authentication protocol using Ticket Granting Tickets (TGT) and Service Tickets (ST). Vulnerable to Kerberoasting and AS-REP Roasting.
- **LM (LAN Manager)**: Legacy Windows hash format that breaks passwords into two 7-character chunks, converted to uppercase. Extremely weak.

#### Password Cracking Attack Types:
1. **Dictionary Attack**: Tests a pre-compiled wordlist of common passwords against target hashes.
2. **Brute-Force Attack**: Systematically tries every possible combination of characters up to a specified length.
3. **Hybrid Attack**: Combines dictionary words with character variations (e.g., `Password123!`).
4. **Rainbow Table Attack**: Uses pre-computed tables of plaintext-hash pairs combined with reduction functions to achieve near-instantaneous offline hash lookup.
5. **Rule-Based Attack**: Applies complex transformation rules (leetspeak, prepending/appending years) to dictionary words using tools like Hashcat.

> [!IMPORTANT] 🔄 **📋 Comprehensive Password Cracking Attack Type Reference Matrix**

| Attack Type | Operational Mechanism | Time Efficiency | Dominant Countermeasure |
| :--- | :--- | :---: | :--- |
| **Dictionary** | Probes list of known passwords | Extremely Fast | Enforce long complex passphrase policies |
| **Brute-Force** | Tries all possible character combinations | Slow (CPU/GPU dependent) | Account lockout thresholds & Rate limiting |
| **Hybrid** | Appends numbers/symbols to dictionary words | Fast to Moderate | Avoid predictable word-number combinations |
| **Rainbow Table** | Looks up hashes in pre-computed tables | Instantaneous | Enforce salted password hashing (`bcrypt`/`Argon2`) |
| **Rule-Based** | Applies regex transformation rules | Highly Efficient | Strong multi-factor authentication (MFA) |
