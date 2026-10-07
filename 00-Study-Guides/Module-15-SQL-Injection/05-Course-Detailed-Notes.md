# 05. Course Detailed Notes — SQL Injection

> [!ABSTRACT] 🏛️ **Comprehensive Syllabus Notes & Technical Reference**
> Direct technical extraction from official CEH v13 Syllabus (Module 15). Covers Second-Order SQL Injection, SQLmap Tamper Scripts, and Out-of-Band (OOB) DNS Exfiltration Mechanics.

---

## 📌 1. Advanced SQLi Vectors & Tamper Scripts

### 1.1 Second-Order SQL Injection Mechanics
Second-Order SQLi occurs when an attacker inputs a payload that is safely stored in a database without immediate execution (e.g., during registration with username `' OR 1=1 --`). The payload is later retrieved and executed in a secondary vulnerable query (e.g., password reset logic).

> [!INFO] 📋 **Comprehensive SQLmap Tamper Script Matrix**

| Tamper Script | Evasion Mechanism | Target WAF Filter / Scenario |
| :--- | :--- | :--- |
| **`space2comment.py`** | Replaces space characters with `/**/` inline comments | Bypasses space-blocking WAF regex |
| **`randomcase.py`** | Converts SQL keywords to random casing (`sElEcT`) | Bypasses case-sensitive string match |
| **`between.py`** | Replaces `>` with `NOT BETWEEN 0 AND` | Bypasses comparison operator filters |
