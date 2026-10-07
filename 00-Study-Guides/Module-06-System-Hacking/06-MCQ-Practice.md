# 🎯 Module 06: System Hacking - Exam Scenario Practice Engine

> [!ABSTRACT] 📊 **Interactive Module Scorecard**
>
> - **Target Module**: Module 06: System Hacking
> - **Total Questions**: 25 Ultra-Detailed, 100% Unique Indirect Scenarios
> - **Exam Difficulty Standard**: Senior CEH v13 (Scenario-Driven Logic & Technical Deduction)
> - **Passing Threshold**: 85% Accuracy (22/25 Correct)
> 
> *Instructions: Evaluate the scenario context below. Select your choice, then expand the **Show Correct Answer & Exam Breakdown** callout to verify your answer and review the deep technical analysis and distractor refutations.*

---

### 🧩 Question 01 | Scenario Challenge

> [!QUESTION] 📌 **Scenario Context**
> During a penetration test, an ethical hacker executes a buffer overflow exploit against a vulnerable C application. By flooding the input memory buffer, the hacker successfully overwrites the CPU register that holds the return memory address for the next instruction.
>
> Which specific CPU register did the hacker overwrite to control program execution flow?

#### 🔘 Available Options:

- **A**: EIP (Extended Instruction Pointer)
- **B**: ESP (Extended Stack Pointer)
- **C**: EBP (Extended Base Pointer)
- **D**: EAX (Extended Accumulator Register)

> [!SUCCESS]- 🔑 **Show Correct Answer & Exam Breakdown**
> **Correct Answer**: **Option A**
>
> #### 💡 Technical Deep Dive:
> The EIP (Extended Instruction Pointer) register contains the memory address of the next CPU instruction to be executed. Overwriting EIP allows an attacker to redirect execution flow to custom shellcode.
>
> #### 🚫 Distractor Analysis & Refutations:
>
> - **Option B is incorrect** because ESP points to the top of the stack.
> - **Option C is incorrect** because EBP points to the base of the current stack frame.
> - **Option D is incorrect** because EAX is a general-purpose arithmetic register.

---

### 🧩 Question 02 | Scenario Challenge

> [!QUESTION] 📌 **Scenario Context**
> An attacker dumps LSASS process memory on a Windows 10 domain workstation and extracts plaintext user credentials and NTLM hashes using the command `sekurlsa::logonpasswords`.
>
> What post-exploitation utility is the attacker operating?

#### 🔘 Available Options:

- **A**: Mimikatz
- **B**: Hashcat
- **C**: John the Ripper
- **D**: Hydra

> [!SUCCESS]- 🔑 **Show Correct Answer & Exam Breakdown**
> **Correct Answer**: **Option A**
>
> #### 💡 Technical Deep Dive:
> Mimikatz (developed by Benjamin Delpy) is the standard post-exploitation tool used to dump credentials, NTLM hashes, and Kerberos tickets directly from Windows LSASS memory.
>
> #### 🚫 Distractor Analysis & Refutations:
>
> - **Option B is incorrect** because Hashcat is an offline password hash cracker.
> - **Option C is incorrect** because John the Ripper is an offline password hash cracker.
> - **Option D is incorrect** because Hydra is an online login brute-forcing tool.

---

### 🧩 Question 03 | Scenario Challenge

> [!QUESTION] 📌 **Scenario Context**
> A penetration tester discovers an unquoted service path on a Windows host: `C:\Program Files\Custom App\service.exe`.
>
> How does Windows attempt to execute files when this service starts, creating a privilege escalation vector?

#### 🔘 Available Options:

- **A**: Windows searches for `C:\Program.exe` first, then `C:\Program Files\Custom.exe`, before executing `service.exe`
- **B**: Windows executes the service using standard user privileges
- **C**: Windows encrypts the executable path with AES-256
- **D**: Windows drops the execution attempt and generates an Event Log alert

> [!SUCCESS]- 🔑 **Show Correct Answer & Exam Breakdown**
> **Correct Answer**: **Option A**
>
> #### 💡 Technical Deep Dive:
> Due to spaces in unquoted service paths, Windows interprets spaces as file argument separators, attempting to execute `C:\Program.exe` first, followed by `C:\Program Files\Custom.exe`.
>
> #### 🚫 Distractor Analysis & Refutations:
>
> - **Option B is incorrect** because unquoted service paths usually run as Local System.
> - **Option C is incorrect** because Windows does not encrypt service paths.
> - **Option D is incorrect** because Windows attempts execution without alerting.

---

### 🧩 Question 04 | Scenario Challenge

> [!QUESTION] 📌 **Scenario Context**
> An attacker hides a malicious executable inside a legitimate text file on an NTFS volume using the command `type payload.exe > report.txt:payload.exe`.
>
> What NTFS file system feature is being exploited to hide the payload?

#### 🔘 Available Options:

- **A**: Alternate Data Streams (ADS)
- **B**: BitLocker Encryption
- **C**: Master File Table (MFT) Corruption
- **D**: Symbolic Links

> [!SUCCESS]- 🔑 **Show Correct Answer & Exam Breakdown**
> **Correct Answer**: **Option A**
>
> #### 💡 Technical Deep Dive:
> NTFS Alternate Data Streams (ADS) allow files to contain multiple streams of data without changing the visible file size or modified date.
>
> #### 🚫 Distractor Analysis & Refutations:
>
> - **Option B is incorrect** because BitLocker provides full disk encryption.
> - **Option C is incorrect** because MFT corruption damages file system metadata.
> - **Option D is incorrect** because Symbolic Links create shortcuts to file paths.

---

### 🧩 Question 05 | Scenario Challenge

> [!QUESTION] 📌 **Scenario Context**
> Which operating system security feature randomizes the memory addresses of the program stack, heap, and libraries in RAM on every system boot to hinder buffer overflow exploits?

#### 🔘 Available Options:

- **A**: ASLR (Address Space Layout Randomization)
- **B**: DEP (Data Execution Prevention)
- **C**: UAC (User Account Control)
- **D**: EFS (Encrypting File System)

> [!SUCCESS]- 🔑 **Show Correct Answer & Exam Breakdown**
> **Correct Answer**: **Option A**
>
> #### 💡 Technical Deep Dive:
> ASLR (Address Space Layout Randomization) randomizes memory space locations for key data areas to prevent attackers from predicting target EIP return addresses.
>
> #### 🚫 Distractor Analysis & Refutations:
>
> - **Option B is incorrect** because DEP marks memory pages as non-executable.
> - **Option C is incorrect** because UAC prompts users before granting administrative privileges.
> - **Option D is incorrect** because EFS encrypts files at rest.

---

### 🧩 Question 06 | Scenario Challenge

> [!QUESTION] 📌 **Scenario Context**
> An ethical hacker wants to prepended a series of `0x90` CPU instructions before shellcode in a buffer overflow payload to ensure execution succeeds even if memory offset calculations drift slightly.
>
> What is this sequence of `0x90` bytes called?

#### 🔘 Available Options:

- **A**: NOP Sled
- **B**: Canary Value
- **C**: Return-Oriented Primitive (ROP)
- **D**: Shellcode Stub

> [!SUCCESS]- 🔑 **Show Correct Answer & Exam Breakdown**
> **Correct Answer**: **Option A**
>
> #### 💡 Technical Deep Dive:
> A NOP Sled is a sequence of No-Operation (`0x90`) instructions that slides CPU execution smoothly into shellcode payload memory addresses.
>
> #### 🚫 Distractor Analysis & Refutations:
>
> - **Option B is incorrect** because Stack Canaries detect buffer overflows before function return.
> - **Option C is incorrect** because ROP bypasses DEP by chaining existing binary instructions.
> - **Option D is incorrect** because shellcode stub is the raw payload code.

---

### 🧩 Question 07 | Scenario Challenge

> [!QUESTION] 📌 **Scenario Context**
> What type of rootkit operates at Ring 0 privilege level, modifying kernel data structures and system call tables directly?

#### 🔘 Available Options:

- **A**: Kernel-Mode Rootkit
- **B**: User-Mode Rootkit
- **C**: Hypervisor Rootkit
- **D**: Application Rootkit

> [!SUCCESS]- 🔑 **Show Correct Answer & Exam Breakdown**
> **Correct Answer**: **Option A**
>
> #### 💡 Technical Deep Dive:
> Kernel-Mode Rootkits operate at Ring 0, hooking system calls and modifying kernel memory structures to hide processes and files.
>
> #### 🚫 Distractor Analysis & Refutations:
>
> - **Option B is incorrect** because User-Mode rootkits operate at Ring 3 in application space.
> - **Option C is incorrect** because Hypervisor rootkits operate at Ring -1.
> - **Option D is incorrect** because application rootkits replace user binaries.

---

### 🧩 Question 08 | Scenario Challenge

> [!QUESTION] 📌 **Scenario Context**
> An attacker uses a command-line script to alter file creation, last access, and last modification timestamps to mislead forensic investigators.
>
> What anti-forensics technique is being executed?

#### 🔘 Available Options:

- **A**: Timestomping
- **B**: Log Cleansing
- **C**: Steganography
- **D**: Memory Scavenging

> [!SUCCESS]- 🔑 **Show Correct Answer & Exam Breakdown**
> **Correct Answer**: **Option A**
>
> #### 💡 Technical Deep Dive:
> Timestomping modifies MAC (Modified, Accessed, Created) file timestamps to disrupt forensic chronological timelines.
>
> #### 🚫 Distractor Analysis & Refutations:
>
> - **Option B is incorrect** because Log Cleansing purges event log files.
> - **Option C is incorrect** because Steganography hides data inside media files.
> - **Option D is incorrect** because Memory Scavenging extracts data from RAM remnants.

---

### 🧩 Question 09 | Scenario Challenge

> [!QUESTION] 📌 **Scenario Context**
> What Windows native command utility allows an administrator or attacker to clear system and security event logs via command prompt using `wevtutil cl Security`?

#### 🔘 Available Options:

- **A**: `wevtutil`
- **B**: `netsh`
- **C**: `sc.exe`
- **D**: `tasklist`

> [!SUCCESS]- 🔑 **Show Correct Answer & Exam Breakdown**
> **Correct Answer**: **Option A**
>
> #### 💡 Technical Deep Dive:
> `wevtutil` is the Windows Event Commandline Utility used to query and clear event logs (`wevtutil cl LogName`).
>
> #### 🚫 Distractor Analysis & Refutations:
>
> - **Option B is incorrect** because `netsh` configures network firewall settings.
> - **Option C is incorrect** because `sc.exe` manages Windows services.
> - **Option D is incorrect** because `tasklist` displays running processes.

---

### 🧩 Question 10 | Scenario Challenge

> [!QUESTION] 📌 **Scenario Context**
> What hardware/kernel security feature marks memory stack and heap regions as non-executable (`NX`), preventing CPU execution of shellcode injected into data buffers?

#### 🔘 Available Options:

- **A**: DEP (Data Execution Prevention)
- **B**: ASLR
- **C**: BitLocker
- **D**: TPM

> [!SUCCESS]- 🔑 **Show Correct Answer & Exam Breakdown**
> **Correct Answer**: **Option A**
>
> #### 💡 Technical Deep Dive:
> DEP (Data Execution Prevention) enforces the NX (No-Execute) bit on stack and heap memory pages to prevent execution of injected code.
>
> #### 🚫 Distractor Analysis & Refutations:
>
> - **Option B is incorrect** because ASLR randomizes memory addresses.
> - **Option C is incorrect** because BitLocker encrypts disk drives.
> - **Option D is incorrect** because TPM provides cryptographic hardware keys.

---

### 🧩 Question 11 | Scenario Challenge

> [!QUESTION] 📌 **Scenario Context**
> Which password cracking attack leverages pre-computed lookup tables of hashes combined with reduction functions to achieve near-instantaneous offline hash recovery?

#### 🔘 Available Options:

- **A**: Rainbow Table Attack
- **B**: Dictionary Attack
- **C**: Hybrid Attack
- **D**: Rule-Based Attack

> [!SUCCESS]- 🔑 **Show Correct Answer & Exam Breakdown**
> **Correct Answer**: **Option A**
>
> #### 💡 Technical Deep Dive:
> Rainbow Table attacks trade storage space for speed by using pre-computed hash chain lookup tables.
>
> #### 🚫 Distractor Analysis & Refutations:
>
> - **Option B is incorrect** because Dictionary attacks compute hashes sequentially from a wordlist.
> - **Option C is incorrect** because Hybrid attacks modify wordlist entries on the fly.
> - **Option D is incorrect** because Rule-Based attacks apply complex transformation rules during computation.

---

### 🧩 Question 12 | Scenario Challenge

> [!QUESTION] 📌 **Scenario Context**
> An attacker uses a privilege escalation exploit (`JuicyPotato`) against a Windows service account that possesses the `SeImpersonatePrivilege` rights.
>
> What elevated privilege account does the attacker achieve?

#### 🔘 Available Options:

- **A**: `NT AUTHORITY\SYSTEM`
- **B**: Guest Account
- **C**: Network Service
- **D**: Local Service

> [!SUCCESS]- 🔑 **Show Correct Answer & Exam Breakdown**
> **Correct Answer**: **Option A**
>
> #### 💡 Technical Deep Dive:
> Potato exploits leverage token impersonation privileges (`SeImpersonatePrivilege`) to escalate from service accounts to full `NT AUTHORITY\SYSTEM` privileges.
>
> #### 🚫 Distractor Analysis & Refutations:
>
> - **Option B is incorrect** because Guest is an unprivileged account.
> - **Option C is incorrect** because Network Service is a low-privilege service account.
> - **Option D is incorrect** because Local Service is a low-privilege account.

---

### 🧩 Question 13 | Scenario Challenge

> [!QUESTION] 📌 **Scenario Context**
> What feature in Windows 10/11 uses virtualization-based security (VBS) to isolate LSASS process memory, rendering tools like Mimikatz unable to extract NTLM hashes?

#### 🔘 Available Options:

- **A**: Windows Credential Guard
- **B**: Windows Defender Firewall
- **C**: SmartScreen
- **D**: AppLocker

> [!SUCCESS]- 🔑 **Show Correct Answer & Exam Breakdown**
> **Correct Answer**: **Option A**
>
> #### 💡 Technical Deep Dive:
> Windows Credential Guard uses Hyper-V virtualization to isolate LSASS memory in an isolated container, protecting secrets from Mimikatz.
>
> #### 🚫 Distractor Analysis & Refutations:
>
> - **Option B is incorrect** because Defender Firewall filters network traffic.
> - **Option C is incorrect** because SmartScreen checks web downloads.
> - **Option D is incorrect** because AppLocker controls application execution policies.

---

### 🧩 Question 14 | Scenario Challenge

> [!QUESTION] 📌 **Scenario Context**
> What fast GPU-accelerated password cracking utility is operated using the syntax `hashcat -m 1000 -a 0 hashes.txt rockyou.txt`?

#### 🔘 Available Options:

- **A**: Hashcat
- **B**: Hydra
- **C**: Medusa
- **D**: Ncrack

> [!SUCCESS]- 🔑 **Show Correct Answer & Exam Breakdown**
> **Correct Answer**: **Option A**
>
> #### 💡 Technical Deep Dive:
> Hashcat is the leading GPU-accelerated password recovery utility. `-m 1000` specifies NTLM hash format.
>
> #### 🚫 Distractor Analysis & Refutations:
>
> - **Option B is incorrect** because Hydra is an online brute-forcer.
> - **Option C is incorrect** because Medusa is an online brute-forcer.
> - **Option D is incorrect** because Ncrack is an online network authentication tool.

---

### 🧩 Question 15 | Scenario Challenge

> [!QUESTION] 📌 **Scenario Context**
> A Linux system administrator discovers a binary with file permissions set to `-rwsr-xr-x` owned by `root`.
>
> What special Linux permission bit is set, enabling any user executing this binary to run with root privileges?

#### 🔘 Available Options:

- **A**: SUID (Set User ID) Bit
- **B**: SGID (Set Group ID) Bit
- **C**: Sticky Bit
- **D**: Executable Bit

> [!SUCCESS]- 🔑 **Show Correct Answer & Exam Breakdown**
> **Correct Answer**: **Option A**
>
> #### 💡 Technical Deep Dive:
> The SUID bit (`chmod u+s`, indicated by `s` in the owner permission field) allows a binary to execute with the file owner's privileges (`root`).
>
> #### 🚫 Distractor Analysis & Refutations:
>
> - **Option B is incorrect** because SGID executes with group privileges (`chmod g+s`).
> - **Option C is incorrect** because Sticky Bit restricts file deletion in shared directories (`/tmp`).
> - **Option D is incorrect** because standard executable bit (`x`) runs with the caller's privileges.

---

### 🧩 Question 16 | Scenario Challenge

> [!QUESTION] 📌 **Scenario Context**
> Which technique embeds secret malicious payload data inside innocent digital media files (such as `.png` images or `.wav` audio files) without causing visual or audible distortion?

#### 🔘 Available Options:

- **A**: Steganography
- **B**: Polymorphic Encryption
- **C**: Code Obfuscation
- **D**: Alternate Data Streams

> [!SUCCESS]- 🔑 **Show Correct Answer & Exam Breakdown**
> **Correct Answer**: **Option A**
>
> #### 💡 Technical Deep Dive:
> Steganography conceals secret payload data inside carrier files (images, audio, video) without altering their outward appearance.
>
> #### 🚫 Distractor Analysis & Refutations:
>
> - **Option B is incorrect** because polymorphic encryption changes key signatures.
> - **Option C is incorrect** because code obfuscation scrambles source code readability.
> - **Option D is incorrect** because ADS attaches data streams to NTFS files.

---

### 🧩 Question 17 | Scenario Challenge

> [!QUESTION] 📌 **Scenario Context**
> What CPU register points to the top of the current memory stack frame?

#### 🔘 Available Options:

- **A**: ESP
- **B**: EIP
- **C**: EBP
- **D**: EAX

> [!SUCCESS]- 🔑 **Show Correct Answer & Exam Breakdown**
> **Correct Answer**: **Option A**
>
> #### 💡 Technical Deep Dive:
> ESP (Extended Stack Pointer) dynamically tracks the top of the stack frame.
>
> #### 🚫 Distractor Analysis & Refutations:
>
> - **Option B is incorrect** because EIP points to the next instruction address.
> - **Option C is incorrect** because EBP points to the base of the frame.
> - **Option D is incorrect** because EAX is an accumulator.

---

### 🧩 Question 18 | Scenario Challenge

> [!QUESTION] 📌 **Scenario Context**
> Which tool script automatically checks a target Linux system for misconfigurations, SUID binaries, and sudo rights to find privilege escalation paths?

#### 🔘 Available Options:

- **A**: LinPEAS
- **B**: WinPEAS
- **C**: Nikto
- **D**: BloodHound

> [!SUCCESS]- 🔑 **Show Correct Answer & Exam Breakdown**
> **Correct Answer**: **Option A**
>
> #### 💡 Technical Deep Dive:
> LinPEAS (Linux Privilege Escalation Awesome Script) automates Linux privilege escalation enumeration.
>
> #### 🚫 Distractor Analysis & Refutations:
>
> - **Option B is incorrect** because WinPEAS targets Windows systems.
> - **Option C is incorrect** because Nikto is a web scanner.
> - **Option D is incorrect** because BloodHound maps Active Directory graphs.

---

### 🧩 Question 19 | Scenario Challenge

> [!QUESTION] 📌 **Scenario Context**
> What Windows default password hash format uses an MD4 hash of the UTF-16LE password string and is vulnerable to Pass-the-Hash attacks?

#### 🔘 Available Options:

- **A**: NTLM Hash
- **B**: LM Hash
- **C**: SHA-256
- **D**: bcrypt

> [!SUCCESS]- 🔑 **Show Correct Answer & Exam Breakdown**
> **Correct Answer**: **Option A**
>
> #### 💡 Technical Deep Dive:
> NTLM (NT LAN Manager) stores password hashes as MD4 digests of UTF-16LE encoded passwords in the Windows SAM database and LSASS memory.
>
> #### 🚫 Distractor Analysis & Refutations:
>
> - **Option B is incorrect** because LM Hash is a legacy DES-based hash.
> - **Option C is incorrect** because SHA-256 is a general cryptographic hash.
> - **Option D is incorrect** because bcrypt is a salted key derivation function.

---

### 🧩 Question 20 | Scenario Challenge

> [!QUESTION] 📌 **Scenario Context**
> An attacker replaces a legitimate DLL required by a application with a malicious payload DLL in an application directory that gets loaded prior to the system directory.
>
> What privilege escalation technique was executed?

#### 🔘 Available Options:

- **A**: DLL Hijacking
- **B**: Unquoted Service Path
- **C**: Token Impersonation
- **D**: Kernel Exploit

> [!SUCCESS]- 🔑 **Show Correct Answer & Exam Breakdown**
> **Correct Answer**: **Option A**
>
> #### 💡 Technical Deep Dive:
> DLL Hijacking relies on exploiting the Windows DLL search order to force applications to load malicious DLLs.
>
> #### 🚫 Distractor Analysis & Refutations:
>
> - **Option B is incorrect** because Unquoted Service Paths exploit unquoted executable strings.
> - **Option C is incorrect** because Token Impersonation steals user tokens.
> - **Option D is incorrect** because Kernel Exploits target OS kernel bugs.

---

### 🧩 Question 21 | Scenario Challenge

> [!QUESTION] 📌 **Scenario Context**
> What persistent agent framework allows an attacker to generate executable payloads that evade traditional antivirus detection engines?

#### 🔘 Available Options:

- **A**: Veil Framework
- **B**: Wireshark
- **C**: Snort
- **D**: Nmap

> [!SUCCESS]- 🔑 **Show Correct Answer & Exam Breakdown**
> **Correct Answer**: **Option A**
>
> #### 💡 Technical Deep Dive:
> The Veil Framework generates Metasploit payloads wrapped in obfuscated code designed to bypass antivirus signatures.
>
> #### 🚫 Distractor Analysis & Refutations:
>
> - **Option B is incorrect** because Wireshark is a packet capture tool.
> - **Option C is incorrect** because Snort is an IDS.
> - **Option D is incorrect** because Nmap is a port scanner.

---

### 🧩 Question 22 | Scenario Challenge

> [!QUESTION] 📌 **Scenario Context**
> What phase of the System Hacking methodology involves deploying backdoors, RATs, and scheduled tasks to retain access across system reboots?

#### 🔘 Available Options:

- **A**: Phase 3: Maintaining Access
- **B**: Phase 1: Gaining Access
- **C**: Phase 2: Escalating Privileges
- **D**: Phase 4: Clearing Tracks

> [!SUCCESS]- 🔑 **Show Correct Answer & Exam Breakdown**
> **Correct Answer**: **Option A**
>
> #### 💡 Technical Deep Dive:
> Phase 3 (Maintaining Access) focuses on establishing persistent remote administrative backdoors.
>
> #### 🚫 Distractor Analysis & Refutations:
>
> - **Option B is incorrect** because Phase 1 is initial exploitation.
> - **Option C is incorrect** because Phase 2 is privilege escalation.
> - **Option D is incorrect** because Phase 4 is log wiping.

---

### 🧩 Question 23 | Scenario Challenge

> [!QUESTION] 📌 **Scenario Context**
> Which password cracking technique applies rule sets (such as prepending years, appending special characters, or applying leetspeak) to dictionary words?

#### 🔘 Available Options:

- **A**: Rule-Based Attack
- **B**: Simple Dictionary Attack
- **C**: Brute-Force Attack
- **D**: Rainbow Table Attack

> [!SUCCESS]- 🔑 **Show Correct Answer & Exam Breakdown**
> **Correct Answer**: **Option A**
>
> #### 💡 Technical Deep Dive:
> Rule-Based attacks apply programmatic transformation rules to words in a dictionary list.
>
> #### 🚫 Distractor Analysis & Refutations:
>
> - **Option B is incorrect** because Simple Dictionary attacks test raw words without rules.
> - **Option C is incorrect** because Brute-Force tests all character permutations.
> - **Option D is incorrect** because Rainbow Table uses pre-computed tables.

---

### 🧩 Question 24 | Scenario Challenge

> [!QUESTION] 📌 **Scenario Context**
> What ring architecture level represents the Hardware/Virtual Machine Monitor level for hypervisor-level rootkits?

#### 🔘 Available Options:

- **A**: Ring -1
- **B**: Ring 0
- **C**: Ring 3
- **D**: Ring 1

> [!SUCCESS]- 🔑 **Show Correct Answer & Exam Breakdown**
> **Correct Answer**: **Option A**
>
> #### 💡 Technical Deep Dive:
> Ring -1 represents hypervisor-level virtualization hardware mode. Ring 0 is Kernel mode, and Ring 3 is User Application mode.
>
> #### 🚫 Distractor Analysis & Refutations:
>
> - **Option B is incorrect** because Ring 0 is OS Kernel mode.
> - **Option C is incorrect** because Ring 3 is User mode.
> - **Option D is incorrect** because Ring 1/2 are legacy ring modes.

---

### 🧩 Question 25 | Scenario Challenge

> [!QUESTION] 📌 **Scenario Context**
> What post-exploitation feature in Meterpreter modifies file MAC timestamps to defeat forensic timeline analysis?

#### 🔘 Available Options:

- **A**: `timestomp`
- **B**: `clearev`
- **C**: `hashdump`
- **D**: `sysinfo`

> [!SUCCESS]- 🔑 **Show Correct Answer & Exam Breakdown**
> **Correct Answer**: **Option A**
>
> #### 💡 Technical Deep Dive:
> `timestomp` is Meterpreter's built-in anti-forensic command used to modify file modification, access, and creation timestamps.
>
> #### 🚫 Distractor Analysis & Refutations:
>
> - **Option B is incorrect** because `clearev` clears event logs.
> - **Option C is incorrect** because `hashdump` extracts SAM hashes.
> - **Option D is incorrect** because `sysinfo` displays target OS details.
