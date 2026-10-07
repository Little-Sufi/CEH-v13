# 02. Attack Techniques — Hacking Mobile Platforms

> [!WARNING] ⚡ **Exploitation Methodologies & Execution Scenarios**
> Direct extraction from official CEH v13 Syllabus (Module 17). Covers APK Decompilation & Reverse Engineering, Frida Dynamic Instrumentation, SSL Pinning Bypass, Trojanized APK Repackaging, and Mobile MitM Proxying.

---

## ⚔️ 1. Primary Mobile Exploitation Workflows

### 1.1 Android APK Reverse Engineering & Repackaging Workflow

#### Step 1: Decompile APK with Apktool / Jadx
```bash
# Decompile APK into Smali bytecode and resources
apktool d target_app.apk -o decompiled_app/

# View decompiled Java source code using Jadx GUI
jadx-gui target_app.apk
```

#### Step 2: Inject Malicious Smali / Trojan Payload
Edit `decompiled_app/smali/` code to insert hooks or reverse shell code.

#### Step 3: Rebuild, Sign, and Align Modified APK
```bash
# Rebuild modified APK directory
apktool b decompiled_app/ -o modified_app.apk

# Generate keystore and sign modified APK
keytool -genkey -v -keystore my-release-key.keystore -alias alias_name -keyalg RSA -keysize 2048 -validity 10000
apksigner sign --ks my-release-key.keystore modified_app.apk
```

### 1.2 Dynamic Instrumentation & SSL Pinning Bypass with Frida
```bash
# Spawn target application and attach Frida SSL Pinning bypass script
frida -U -f com.example.app -l ssl_pinning_bypass.js
```

> [!DANGER] 🛡️ **📋 Comprehensive Mobile Attack Execution Matrix**

| Attack Type | Target Platform | Command / Tool Syntax | Technical Outcome |
| :--- | :--- | :--- | :--- |
| **APK Decompilation** | Android | `jadx-gui app.apk` | Discloses hardcoded keys & logic |
| **SSL Pinning Bypass** | Android / iOS | `frida -U -f com.app -l script.js` | Intercepts HTTPS in Burp Suite |
| **Trojan Repackaging**| Android | `apktool b app_dir/` & `apksigner` | Distributes malicious cloned app |
| **Intent Injection** | Android | `adb shell am start -n com.app/.Target` | Bypasses activity authentication |
