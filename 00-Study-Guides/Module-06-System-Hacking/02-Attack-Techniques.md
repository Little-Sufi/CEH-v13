# 02. Attack Techniques — System Hacking

> [!WARNING] ⚡ **Offensive Exploitation & Escalation Methodologies**
> Direct extraction from official CEH v13 Syllabus (Module 06). Covers Memory Buffer Overflows (Stack Frame Architecture), Windows/Linux Privilege Escalation, Rootkit Operations, and Anti-Forensic Techniques (NTFS ADS & Timestomping).

---

## ⚔️ 1. Buffer Overflow Vulnerability Mechanics

### 1.1 Stack Architecture & Memory Layout
A Buffer Overflow occurs when an application writes more data to a fixed-size memory buffer on the stack than the buffer was allocated to hold, overwriting adjacent memory registers.

#### CPU Register Definitions:
- **ESP (Extended Stack Pointer)**: Points to the top of the current memory stack frame.
- **EBP (Extended Base Pointer)**: Points to the base of the current stack frame.
- **EIP (Extended Instruction Pointer)**: Points to the memory address of the next CPU instruction to be executed. **Primary exploitation target**.

#### Buffer Overflow Execution Steps:
1. **Overflow Buffer**: Send excessive data (`AAAA...`) to flood the stack memory buffer.
2. **Overwrite EBP & Control EIP**: Overwrite the EBP and replace the return address stored in the `EIP` register with a specific memory address pointing to malicious shellcode.
3. **NOP Sled Insertion**: Prepend a sequence of No-Operation instructions (`0x90` NOP sled) before the shellcode to ensure successful CPU execution even if memory offsets shift slightly.
4. **Shellcode Execution**: The CPU slides down the NOP sled and executes the reverse shell payload in memory.

> [!DANGER] 🛡️ **📋 Comprehensive Buffer Overflow Memory Register Reference Matrix**

| CPU Register | Register Purpose | Exploitation Function | Attack Target Value |
| :---: | :--- | :--- | :--- |
| **ESP** | Top of Stack Pointer | Holds shellcode payload memory address | Points to NOP Sled / Payload |
| **EBP** | Base of Stack Frame | Separates stack frame function calls | Overwritten during overflow |
| **EIP** | Instruction Pointer | Controls next CPU instruction address | **Overwritten with JMP ESP address** |
| **NOP Sled** | `0x90` Instruction | Provides execution landing pad for shellcode | Prepend to shellcode payload |

---

## 🛡️ 2. Privilege Escalation & Anti-Forensics

### 2.1 Windows & Linux Privilege Escalation Vectors

#### Windows Escalation Vectors:
- **Unquoted Service Paths**: Windows services with spaces in their file paths without surrounding quotation marks (e.g., `C:\Program Files\My Service\service.exe`). Windows attempts to execute `C:\Program.exe` or `C:\Program Files\My.exe` first, allowing attackers to place malicious executables.
- **DLL Hijacking**: Replacing a missing or vulnerable dynamic-link library (`.dll`) loaded by a privileged application with a malicious payload DLL.
- **Token Impersonation (Potato Attacks)**: Exploiting `SeImpersonatePrivilege` or `SeAssignPrimaryTokenPrivilege` (JuicyPotato, RoguePotato, PrintSpoofer) to escalate from service accounts to `NT AUTHORITY\SYSTEM`.

#### Anti-Forensics & Hiding Files:
- **NTFS Alternate Data Streams (ADS)**: Attaching hidden executable files to legitimate files on NTFS file systems without altering the visible file size or timestamp.
  - **Hide File**: `type malicious.exe > innocent.txt:malicious.exe`
  - **Execute Hidden Stream**: `start innocent.txt:malicious.exe`
- **Timestomping**: Modifying file creation, access, and modification (MAC) timestamps using tools like Meterpreter `timestomp` to evade forensic timeline analysis.

> [!SHIELD] 🏰 **📋 Comprehensive Privilege Escalation & Anti-Forensic Reference Matrix**

| Technique Category | Specific Vector | Operational Mechanic | Defensive Mitigation |
| :--- | :--- | :--- | :--- |
| **Windows PrivEsc** | Unquoted Service Path | Exploit spaces in service paths to drop executable | Enclose service paths in quotes |
| **Windows PrivEsc** | Token Impersonation | Exploit `SeImpersonatePrivilege` via Potato exploits | Remove privilege from service accounts |
| **Linux PrivEsc** | SUID Binaries | Execute SUID permission binaries (`chmod u+s`) | Audit SUID files (`find / -perm -4000`) |
| **Anti-Forensics** | NTFS ADS | Hide payloads inside Alternate Data Streams | Use PowerShell `Get-Item -Stream *` |
| **Anti-Forensics** | Timestomping | Manipulate file MAC timestamps to evade logs | Enable file system auditing (sysmon) |
