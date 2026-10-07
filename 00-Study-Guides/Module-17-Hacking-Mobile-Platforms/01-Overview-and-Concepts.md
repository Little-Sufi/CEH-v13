# 01. Overview and Concepts — Hacking Mobile Platforms

> [!INFO] 📌 **Module Scope & Core Objectives**
> Direct technical extraction from official CEH v13 Syllabus (Module 17). Covers Android Security Architecture (Linux Kernel, ART, App Sandbox, APK Structure), iOS Security Architecture (Secure Enclave, Secure Boot Chain, App Sandbox, IPA Structure), Mobile Vulnerability Taxonomies (OWASP Mobile Top 10), Rooting & Jailbreaking Mechanics, and Mobile Device Management (MDM) / BYOD Security.

---

## 🧠 1. Mobile Operating System Architectures & OWASP Framework

### 1.1 Android OS Architecture & Security Model
Android is an open-source, Linux-kernel-based operating system enforcing process isolation via Linux user IDs (UIDs).

- **Android Runtime (ART)**: Replaced Dalvik VM; compiles DEX bytecode into native machine code (Ahead-Of-Time / AOT compilation).
- **Application Sandbox**: Assigns a unique Linux UID to every installed application, restricting filesystem access to its assigned data folder (`/data/data/com.example.app/`).
- **APK Package Structure**:
  - `AndroidManifest.xml`: Defines app permissions, intent filters, activities, services, receivers.
  - `classes.dex`: Compiled Dalvik/ART executable bytecode.
  - `resources.arsc` & `res/`: Precompiled resources (strings, UI layouts).
  - `META-INF/`: Digital signatures (`CERT.RSA`, `CERT.SF`, `MANIFEST.MF`).

### 1.2 iOS OS Architecture & Security Model
Apple iOS is a closed-source operating system built on the Darwin kernel with hardware-enforced root-of-trust security.

- **Secure Enclave Processor (SEP)**: Dedicated coprocessor with encrypted memory managing biometric data (Face ID / Touch ID) and cryptographic keys.
- **Secure Boot Chain**: Verifies digital signatures sequentially: Boot ROM -> Low-Level Bootloader (LLB) -> iBoot -> iOS Kernel -> Apps.
- **Keychain Services**: Encrypted database storing passwords, keys, and session tokens.

> [!ABSTRACT] 🏛️ **📋 Comprehensive OWASP Mobile Top 10 Vulnerability Matrix**

| Vulnerability Risk | Category Description | Technical Exploitation Mechanism | Primary Impact |
| :--- | :--- | :--- | :--- |
| **M1: Improper Credential Usage**| Hardcoded API keys / credentials | Reversing APK/IPA source code | Cloud API Account Takeover |
| **M2: Inadequate Supply Chain** | Malicious dependencies / SDKs | Repackaging APKs with trojans | Mass User Surveillance |
| **M3: Insecure Authentication** | Local PIN/Biometric bypass | Hooking authentication functions (Frida) | Privilege Escalation |
| **M4: Insufficient Input Validation**| SQLi, Path Traversal in IPC/Intents | Sending malformed Android Intents | Arbitrary Data Disclosure |
| **M5: Insecure Communication** | Cleartext HTTP / SSL validation failure| MitM interposing via Burp Suite proxy | Session Token Hijacking |
| **M7: Insufficient Binary Protection**| Missing anti-debugging & obfuscation | Decompiling using Jadx / Ghidra | Intellectual Property Theft |

---

## ⚡ 2. Rooting, Jailbreaking & MDM Architecture

### 2.1 Android Rooting vs iOS Jailbreaking
- **Android Rooting**: Unlocking the bootloader and flashing custom superuser binaries (e.g., Magisk) to gain root (`UID 0`) privileges.
- **iOS Jailbreaking**: Exploiting kernel vulnerabilities (e.g., checkm8 hardware exploit) to disable Code Signing, Sandbox enforcement, and ASLR, installing package managers like Cydia or Sileo.

> [!IMPORTANT] 🔄 **📋 Comprehensive Rooting vs Jailbreaking Comparison Matrix**

| Attribute Feature | Android Rooting | iOS Jailbreaking |
| :--- | :--- | :--- |
| **Primary Method** | Bootloader unlock & Magisk flash | Kernel vulnerability exploitation |
| **Hardware Root of Trust** | OEM Unlock setting dependent | Bypasses Secure Boot Chain |
| **Defensive Detection** | SafetyNet / Play Integrity API | Jailbreak detection hooks (File checks) |
| **Privilege Achieved** | Full `root` access (`UID 0`) | Disables Code Signing & Sandbox |
