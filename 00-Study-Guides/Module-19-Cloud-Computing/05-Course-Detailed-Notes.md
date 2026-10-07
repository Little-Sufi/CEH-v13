# 05. Course Detailed Notes — Cloud Computing

> [!ABSTRACT] 🏛️ **Comprehensive Syllabus Notes & Technical Reference**
> Direct technical extraction from official CEH v13 Syllabus (Module 19). Covers Serverless Security Mechanics, Cloud Encryption at Rest / in Transit, and Cloud DMZ Architecture.

---

## 📌 1. Serverless & Cloud Encryption Mechanics

- **AWS KMS / Azure Key Vault**: Centralized Hardware Security Module (HSM) services managing envelope encryption keys (`Customer Managed Keys - CMK`).
- **Serverless (FaaS) Security**: Lambda functions require isolated execution environments, tight IAM role permissions, and short execution timeouts to prevent persistent backdoor attachment.

> [!INFO] 📋 **Comprehensive Cloud Deployment Model Matrix**

| Deployment Model | Infrastructure Ownership | Data Access Scope | Typical Use Case |
| :--- | :--- | :--- | :--- |
| **Public Cloud** | Third-party CSP (AWS/Azure/GCP) | Multi-tenant shared | Scalable web apps, public services |
| **Private Cloud** | Single Organization / On-Prem | Dedicated single-tenant | Highly regulated banking / government |
| **Hybrid Cloud** | Combined Public & Private | Shared via secure VPN / DirectConnect | Bursting workloads, legacy integration |
| **Community Cloud**| Shared by multiple allied orgs | Restricted industry group | Healthcare research, university consortia |
