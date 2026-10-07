# 04. Countermeasures — SQL Injection

> [!SHIELD] 🏰 **Defensive Hardening Standards & Secure Coding**
> Direct technical extraction from official CEH v13 Syllabus (Module 15). Covers Parameterized Queries (Prepared Statements), Object-Relational Mapping (ORM), Stored Procedures, Input Validation, and Database Least Privilege.

---

## 🛡️ 1. Defensive Hardening Checklist

### 1.1 Technical Countermeasures

1. **Mandatory Use of Parameterized Queries (Prepared Statements)**: Separates SQL query code from user data parameters. The RDBMS compiles the SQL template first, then inserts user parameters as literal values.
   ```php
   // Secure PHP PDO Prepared Statement
   $stmt = $pdo->prepare('SELECT * FROM users WHERE username = :user AND password = :pass');
   $stmt->execute(['user' => $user, 'pass' => $pass]);
   ```
2. **Use Secure ORM Frameworks**: Leverage ORMs like Hibernate, Entity Framework, or Sequelize that parameterize queries by default.
3. **Database Principle of Least Privilege**: Ensure web applications connect to databases using restricted non-administrator service accounts (`db_datareader`/`db_datawriter`) rather than `sa` or `root`.
4. **Disable Verbose Error Messages**: Configure web servers to display generic custom error pages (`500 Internal Server Error`) to prevent error-based SQLi disclosures.

> [!SHIELD] 🏰 **📋 Comprehensive SQL Injection Defensive Reference Matrix**

| Language / Environment | Secure Implementation Standard | Insecure Vulnerable Anti-Pattern |
| :--- | :--- | :--- |
| **PHP (PDO)** | `$stmt = $pdo->prepare('SELECT * FROM u WHERE id=?');` | `$db->query("SELECT * FROM u WHERE id=$id");` |
| **Java (JDBC)** | `PreparedStatement pstmt = conn.prepareStatement(...);` | `Statement stmt = conn.createStatement(...);` |
| **C# (.NET)** | `SqlCommand cmd = new SqlCommand(sql, conn); cmd.Parameters.Add...` | `SqlCommand cmd = new SqlCommand("... " + input);` |
