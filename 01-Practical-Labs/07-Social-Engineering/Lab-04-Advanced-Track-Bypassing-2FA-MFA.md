![Lab Image](https://images.unsplash.com/photo-1544383835-bda2bc66a55d?w=800&h=200&fit=crop)

[⬅️ Previous](Lab-03-Advanced-Track-Gophish-Campaigns.md) | [🏠 Path Home](Home.md) | [Next Lab ➡️](Lab-05-Advanced-Track-Watering-Hole-Attacks.md)

---

# Lab 04: Advanced Track - Bypassing 2FA/MFA Phishing

---


---




---


---

[⬅️ Path Home](Home.md)

---

## 🎯 Lab Objectives
- Understand Reverse Proxy architecture for session interception.
- Analyze how tools like Evilginx capture authentication tokens.
- Implement defense-in-depth protections against MFA bypass phishing.

## 🛠️ Required Tools & Setup
- **Evilginx2 / Evilginx3:** Reverse proxy credential harvester.
- **Phishlets:** Configuration files for specific target platforms.
- **Practice Room:** [TryHackMe Mitigating MFA Bypass](https://tryhackme.com/room/mitigatingmfabypass)

## 🚶 Step-by-Step Lab Guide

### Step 1: Understanding Phishlet Mechanics
Inspect a typical yaml phishlet structure to see how redirect domains and session cookie keys are configured:
```yaml
name: 'custom-oauth'
author: '@ethicalhacker'
min_ver: '3.0.0'
proxy_hosts:
  - {phish_sub: 'login', target_sub: 'login', domain_map: true}
```

### Step 2: Session Hijacking Defense
Explain the importance of deploying FIDO2/WebAuthn security keys which bind the credentials directly to the origin domain, neutralizing reverse-proxy attacks.

---

[⬅️ Path Home](Home.md)

---

[⬅️ Previous](Lab-03-Advanced-Track-Gophish-Campaigns.md) | [🏠 Path Home](Home.md) | [Next Lab ➡️](Lab-05-Advanced-Track-Watering-Hole-Attacks.md)
