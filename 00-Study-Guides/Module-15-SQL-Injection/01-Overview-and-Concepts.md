# 01. Overview and Concepts — SQL Injection

> [!INFO] 📌 **Module Scope & Core Objectives**
> Direct technical extraction from official CEH v13 Syllabus (Module 15). Covers SQL Injection (SQLi) Taxonomies (In-Band / Classic, Inferential / Blind, Out-of-Band), UNION-based, Error-based, Boolean-based, Time-based, Second-Order SQLi, Database Dialect Variations (MySQL, MSSQL, PostgreSQL, Oracle), SQLmap automation, and Parameterized Query Countermeasures.

---

## 🧠 1. SQL Injection Taxonomies & Dialect Mechanics

### 1.1 SQL Injection Classification Hierarchy
SQL Injection occurs when untrusted user inputs are concatenated directly into dynamic SQL query strings without sanitization or parameterization.

#### 1. In-Band (Classic) SQLi
Data exfiltration occurs over the same network channel used to inject the payload.
- **UNION-Based SQLi**: Combines the results of the original query with an attacker-crafted `UNION SELECT` query to dump arbitrary database tables.
- **Error-Based SQLi**: Triggers database engine error messages (e.g., `CONCAT()`, `extractvalue()`, `CAST()`) that disclose sensitive data within the error string itself.

#### 2. Inferential (Blind) SQLi
The server does not output query results or error messages in the HTTP response. Attackers infer database content by observing application behavior.
- **Boolean-Based Blind SQLi**: Evaluates True/False conditional statements (`AND 1=1` vs `AND 1=2`) and observes differences in HTTP response content/length.
- **Time-Based Blind SQLi**: Injects database sleep commands (`SLEEP(5)` or `WAITFOR DELAY '0:0:5'`) and measures HTTP response delays to reconstruct data character by character.

#### 3. Out-of-Band (OOB) SQLi
Executed when in-band results are hidden and server performance is too unstable for time-based blind attacks. Requires database features that initiate external DNS or SMB requests (e.g., MSSQL `xp_dirtree` or Oracle `UTL_HTTP`).

> [!ABSTRACT] 🏛️ **📋 Comprehensive SQL Injection Classification Comparison Matrix**

| SQLi Category | Sub-Category | Primary Data Exfiltration Channel | Execution Speed | Response Dependency |
| :--- | :--- | :--- | :--- | :--- |
| **In-Band** | UNION-Based | HTTP Response Body | Extremely Fast | Direct query output |
| **In-Band** | Error-Based | Database Error Messages | Fast | Verbose error output |
| **Inferential** | Boolean-Based | HTTP Page Content / Status Code | Slow (Bit-by-Bit) | Page structure changes |
| **Inferential** | Time-Based | HTTP Response Time Delay | Very Slow | Server delay execution |
| **Out-of-Band** | OOB (DNS/SMB)| External Attacker DNS Server | Fast | External DNS/SMB egress |

---

## ⚡ 2. Database Engine Dialect Differences

### 2.1 Syntax Variations Across Relational Database Engines
Different Relational Database Management Systems (RDBMS) utilize unique syntax for version queries, string concatenation, and comments.

> [!IMPORTANT] 🔄 **📋 Comprehensive RDBMS Dialect Cheat Sheet Matrix**

| RDBMS Engine | Version Query Payload | Comment Syntax | String Concatenation | Time Delay Payload |
| :--- | :--- | :--- | :--- | :--- |
| **MySQL** | `SELECT @@version` | `-- `, `#`, `/*` | `CONCAT('a', 'b')` | `SLEEP(5)` |
| **Microsoft SQL** | `SELECT @@version` | `--`, `/*` | `'a' + 'b'` | `WAITFOR DELAY '0:0:5'` |
| **PostgreSQL** | `SELECT version()` | `--`, `/*` | `'a' \|\| 'b'` | `pg_sleep(5)` |
| **Oracle** | `SELECT * FROM v$version` | `--` | `'a' \|\| 'b'` | `DBMS_PIPE.RECEIVE_MESSAGE('a', 5)` |
