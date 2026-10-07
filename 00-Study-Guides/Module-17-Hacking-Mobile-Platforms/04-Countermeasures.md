# 04. Countermeasures — Hacking Mobile Platforms

> [!SHIELD] 🏰 **Defensive Hardening Standards & Secure Coding**
> Direct technical extraction from official CEH v13 Syllabus (Module 17). Covers Code Obfuscation (ProGuard / R8), Anti-Tampering & Root Detection, SSL/TLS Pinning, Secure Storage (KeyStore / Keychain), and MDM Enforcements.

---

## 🛡️ 1. Mobile Hardening Checklist

### 1.1 Technical Defensive Standards

1. **Code Obfuscation & Shrinking**: Use **ProGuard** or **R8** to strip debug symbols, rename class/method names, and obfuscate control flow to hinder reverse engineering.
2. **Implement Root / Jailbreak & Anti-Tampering Detection**: Check for root binaries (`/system/xbin/su`), Cydia paths, and verify APK signature integrity at startup using Google Play Integrity API or iOS DeviceCheck.
3. **SSL / TLS Certificate Pinning**: Pin public key hashes (`SPKI`) within app code to block MitM proxy interception even if custom CA certificates are installed on the device.
4. **Secure Data Storage**: Never store sensitive tokens or passwords in SharedPreferences, SQLite, or plist files in cleartext. Always use **Android KeyStore** or **iOS Keychain**.

> [!SHIELD] 🏰 **📋 Comprehensive Mobile Security Hardening Reference Matrix**

| Vulnerability Vector | Insecure Code Implementation | Secure Countermeasure Standard |
| :--- | :--- | :--- |
| **Cleartext Storage** | SharedPreferences / plist text storage | Android KeyStore / iOS Keychain encrypted storage |
| **Reverse Engineering** | Unobfuscated DEX bytecode | ProGuard / R8 / DexGuard bytecode obfuscation |
| **MitM Proxying** | Standard OS Trust Store | Public Key Pinning (Network Security Config) |
| **Trojan Repackaging**| No signature verification | Google Play Integrity API / Signature Validation |
