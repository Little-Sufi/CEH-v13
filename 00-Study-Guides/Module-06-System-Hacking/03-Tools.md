# 03. Tools — System Hacking

> [!TOOL] 🛠️ **Command-Line & GUI System Hacking Software Reference Matrix**
> Direct technical extraction from official CEH v13 Syllabus (Module 06). Covers Mimikatz, Hashcat, John the Ripper, Metasploit, WinPEAS/LinPEAS, and Veil-Evasion.

---

## 🛠️ 1. Primary System Hacking Tools Reference Matrix

> [!TOOL] 📋 **Comprehensive System Hacking Software Reference Matrix**

| Utility Name | Vendor / Developer | Primary Exploitation Purpose | Platform Support |
| :--- | :--- | :--- | :--- |
| **Mimikatz** | Benjamin Delpy | Extracts plaintext passwords, NTLM hashes & Kerberos tickets from LSASS memory | Windows |
| **Hashcat** | Jens Steube | World's fastest GPU-accelerated password hash cracker | Cross-platform |
| **John the Ripper** | Openwall | Open-source CPU-based password hash cracking tool | Cross-platform |
| **Metasploit Framework**| Rapid7 | Premier exploitation & post-exploitation agent platform | Linux, Windows, macOS |
| **WinPEAS / LinPEAS** | Carlos Polop | Privilege escalation audit scripts for Windows and Linux | Windows / Linux |
| **Veil Framework** | Veil-Project | Generates Metasploit payloads that bypass antivirus inspection | Linux |

---

## 💻 2. Command-Line Syntax & Execution Commands

### 2.1 Mimikatz Memory Extraction Commands
- **Extract LSASS Plaintext Passwords & NTLM Hashes**:
  ```cmd
  privilege::debug
  sekurlsa::logonpasswords
  ```
- **Dump Local SAM Database Hashes**:
  ```cmd
  token::elevate
  lsadump::sam
  ```

### 2.2 Hashcat GPU Hash Cracking Commands
- **Crack NTLM hashes using wordlist**:
  ```bash
  hashcat -m 1000 -a 0 hashes.txt rockyou.txt
  ```
- **Crack NetNTLMv2 hashes using rule set**:
  ```bash
  hashcat -m 5600 -a 0 netntlmv2.txt rockyou.txt -r rules/best64.rule
  ```
