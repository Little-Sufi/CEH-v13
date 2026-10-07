# 05. Course Detailed Notes — System Hacking

> [!ABSTRACT] 🏛️ **Comprehensive Syllabus Notes & Technical Reference**
> Direct technical extraction from official CEH v13 Syllabus (Module 06). Covers Rootkit Classifications (User-Mode vs Kernel-Mode), Steganography Concepts, and Event Log Anti-Forensics.

---

## 📌 1. Rootkit Architectures & Steganography

### 1.1 Rootkit Classifications & Operational Modes
Rootkits are malicious software programs designed to maintain hidden administrative access to a computer system while actively concealing running processes, network connections, and files from operating system APIs and security monitoring tools.

#### Classifications:
1. **User-Mode Rootkit**: Operates at Ring 3 privilege level. Intercepts standard application API calls (e.g., hooking `kernel32.dll` or `libc`) to hide files and processes. Easily detected by signature scanners.
2. **Kernel-Mode Rootkit**: Operates at Ring 0 privilege level (Kernel level). Modifies system call tables (SSDT) or kernel data structures directly. Can cause System Crash (BSOD) if bugs occur. Extremely difficult to detect.
3. **Hypervisor-Level Rootkit**: Operates as a virtual machine monitor (Ring -1), hosting the target operating system as a virtual machine to intercept hardware calls.
4. **Firmware / BIOS Rootkit**: Installs persistent malicious code inside motherboard BIOS or device firmware chips, surviving hard drive wipes and OS re-installations.

> [!INFO] 📋 **Comprehensive Rootkit Privilege Ring Reference Matrix**

| Rootkit Category | Privilege Level | Operates In | Detection Difficulty |
| :--- | :---: | :--- | :--- |
| **User-Mode** | Ring 3 | Application Space | Moderate (Antivirus / EDR) |
| **Kernel-Mode** | Ring 0 | OS Kernel Space | **High** (Kernel Integrity Checks required) |
| **Hypervisor** | Ring -1 | Virtual Machine Monitor | **Extreme** (Requires hardware-level inspection) |
| **Firmware / BIOS**| Hardware Level | Flash ROM / Chipset | **Extreme** (Survives complete disk replacement) |
