# 05. Course Detailed Notes — Evading IDS, Firewalls, and Honeypots

> [!ABSTRACT] 🏛️ **Comprehensive Syllabus Notes & Technical Reference**
> Direct technical extraction from official CEH v13 Syllabus (Module 12). Covers Obfuscation Mechanics, Polymorphic Engines, and Honeypot Detection Techniques.

---

## 📌 1. Polymorphic & Metamorphic Obfuscation

### 1.1 Code Obfuscation Mechanics
- **Polymorphic Code**: Encrypts payload code with a unique key per generation and prepends a variable decryption routine (decryption stub).
- **Metamorphic Code**: Completely rewrites program structure (swapping registers, reordering instructions, inserting NOP dead code) every iteration without changing functionality.

> [!INFO] 📋 **Comprehensive Obfuscation Engine Comparison Matrix**

| Obfuscation Type | Structural Code Changes | Encryption Key Variation | Signature Evasion Effectiveness |
| :--- | :--- | :--- | :--- |
| **Polymorphic** | Decryption stub changes | Variable key per binary | Medium (Stub can be signatured) |
| **Metamorphic** | Entire binary code structure rewrites | No encryption key used | **High** (Defeats static signatures) |
