# 04. Countermeasures — Cloud Computing

> [!SHIELD] 🏰 **Defensive Hardening Standards & Secure Configurations**
> Direct technical extraction from official CEH v13 Syllabus (Module 19). Covers AWS IMDSv2 Migration, Block Public Access for S3/Blob, Least Privilege IAM Policies, Cloud Security Posture Management (CSPM), Multi-Factor Authentication (MFA), and Container Hardening.

---

## 🛡️ 1. Cloud Security Hardening Standards

### 1.1 Technical Defensive Checklist

1. **Enforce AWS Instance Metadata Service Version 2 (IMDSv2)**: Mandate session-oriented token requests (`X-aws-ec2-metadata-token`) to mitigate SSRF metadata credential theft.
2. **Enable Global Block Public Access on Cloud Storage**: Enforce AWS "Block Public Access", Azure "Private Container", and GCP "Uniform Bucket-Level Access" to block accidental public data leaks.
3. **Strict IAM Least Privilege & Mandatory MFA**: Require MFA for all cloud console logins and root accounts. Avoid wildcards (`"Action": "*"`) in IAM policies.
4. **Deploy Cloud Security Posture Management (CSPM)**: Continuously scan cloud configurations against CIS Benchmarks using tools like AWS Security Hub, Azure Security Center, Prowler, or Scout Suite.

> [!SHIELD] 🏰 **📋 Comprehensive Cloud Hardening Reference Matrix**

| Vulnerability Vector | Insecure Legacy State | Mandatory Hardening Countermeasure |
| :--- | :--- | :--- |
| **SSRF IMDS Exfiltration** | IMDSv1 enabled (`http://169.254...`) | Require IMDSv2 (PUT token header required) |
| **Public Storage Buckets** | Public S3 / Blob Access enabled | AWS Block Public Access + KMS Key Encryption |
| **IAM Over-privilege** | `"Action": "*", "Resource": "*"` | Least Privilege IAM roles + Condition Keys |
| **Container Breakout** | Container running as `root` user | Non-root container user + Read-only root filesystem |
