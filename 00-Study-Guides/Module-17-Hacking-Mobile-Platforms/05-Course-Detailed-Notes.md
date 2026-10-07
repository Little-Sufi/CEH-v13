# 05. Course Detailed Notes — Hacking Mobile Platforms

> [!ABSTRACT] 🏛️ **Comprehensive Syllabus Notes & Technical Reference**
> Direct technical extraction from official CEH v13 Syllabus (Module 17). Covers Android Manifest Permission Models, Android Intent Interception, and BYOD Containerization.

---

## 📌 1. Android Component Security & BYOD Frameworks

### 1.1 Android Four Core Components
1. **Activities**: UI screens presented to users.
2. **Services**: Background processing tasks without direct UI.
3. **Broadcast Receivers**: Listens for system-wide or app-specific broadcast messages.
4. **Content Providers**: Manages and shares structured relational app datasets (`sqlite`).

> [!INFO] 📋 **Comprehensive Android Permission Model Matrix**

| Permission Level | Enforcement Standard | User Prompt Mechanism |
| :--- | :--- | :--- |
| **Normal** | Automatically granted at install | No user interaction required |
| **Dangerous** | Requires explicit user consent | Runtime popup dialog (e.g., Camera, Location) |
| **Signature** | Granted only if signed with same certificate | Automatic silently |
