# 04. Countermeasures — System Hacking

> [!SHIELD] 🏰 **Defensive Security Controls & System Hardening**
> Direct technical extraction from official CEH v13 Syllabus (Module 04). Covers Memory Protections (DEP, ASLR), Credential Guard, Account Lockout Policies, and Log Integrity Monitoring.

---

## 🛡️ 1. Operating System Hardening & Memory Protections

### 1.1 Exploit Mitigation Mechanisms
Modern operating systems deploy hardware and compiler security mitigations to prevent buffer overflow exploitation:

- **DEP (Data Execution Prevention)**: Marks memory stack and heap regions as non-executable (NX/XD bit), preventing the CPU from executing shellcode injected into data buffers.
- **ASLR (Address Space Layout Randomization)**: Randomizes the memory locations of program executable code, stack, heap, and libraries (DLLs) in RAM on every boot, making return address prediction for EIP difficult.
- **Windows Credential Guard**: Uses virtualization-based security (VBS) to isolate LSASS memory, preventing Mimikatz from extracting NTLM hashes or Kerberos tickets.

> [!SHIELD] 🏰 **📋 Comprehensive Memory & System Protection Reference Matrix**

| Protection Mechanism | Type of Protection | Technical Evasion Resistance | Primary Defensive Utility |
| :--- | :--- | :--- | :--- |
| **DEP / NX Bit** | Hardware / Kernel Memory | Prevents executing code on stack/heap | Windows Defender Exploit Guard |
| **ASLR** | Kernel Memory Layout | Randomizes DLL & stack memory addresses | Windows / Linux Kernel ASLR |
| **Credential Guard** | Virtualization (VBS) | Isolates LSASS process memory | Windows 10/11 Enterprise |
| **Account Lockout** | Active Directory Policy | Locks account after 5 failed login attempts | Group Policy Management |
