# 01. Overview and Concepts — Cloud Computing

> [!INFO] 📌 **Module Scope & Core Objectives**
> Direct technical extraction from official CEH v13 Syllabus (Module 19). Covers Cloud Service Models (IaaS, PaaS, SaaS, FaaS/Serverless), Cloud Deployment Models (Public, Private, Hybrid, Community), Shared Responsibility Model, Cloud Security Alliance (CSA) Treacherous Twelve / Egregious Eleven, IAM Misconfigurations, Cloud Storage Bucket Security (AWS S3, Azure Blob, GCP Storage), Container & Kubernetes Security, and Cloud Hardening.

---

## 🧠 1. Cloud Architecture & Shared Responsibility

### 1.1 Cloud Service Models Matrix
Cloud computing abstracts computing infrastructure across distinct service delivery tiers.

- **Infrastructure as a Service (IaaS)**: Customer manages OS, runtime, middleware, data, applications (e.g., AWS EC2, Azure VMs). Provider manages physical hardware, hypervisor, datacenter networking.
- **Platform as a Service (PaaS)**: Customer manages application code and data. Provider manages OS, runtime environment, databases, hypervisor, physical infrastructure (e.g., AWS Elastic Beanstalk, Heroku).
- **Software as a Service (SaaS)**: Customer configures application settings and manages user access. Provider manages entire software stack, code, infrastructure (e.g., Microsoft 365, Salesforce).
- **Function as a Service (FaaS / Serverless)**: Event-driven execution model where cloud providers dynamically manage server allocation (e.g., AWS Lambda, Azure Functions).

> [!ABSTRACT] 🏛️ **📋 Comprehensive Cloud Shared Responsibility Matrix**

| Cloud Architecture Tier | Physical Datacenter | Virtualization Hypervisor | OS & Kernel | Middleware / Runtime | Application Code | Data & IAM |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **IaaS (Infrastructure)**| CSP | CSP | **Customer** | **Customer** | **Customer** | **Customer** |
| **PaaS (Platform)** | CSP | CSP | CSP | CSP | **Customer** | **Customer** |
| **SaaS (Software)** | CSP | CSP | CSP | CSP | CSP | **Customer** |

---

## ⚡ 2. Cloud Threat Taxonomies & Container Security

### 2.1 CSA Cloud Top Vulnerabilities (Egregious Eleven / Treacherous Twelve)
1. **Data Breaches**: Unauthorized exfiltration of sensitive cloud data.
2. **Misconfiguration & Inadequate Change Control**: Unsecured S3 buckets (`All Users` read/write permissions), permissive security groups (`0.0.0.0/0` SSH access).
3. **Lack of Cloud Security Architecture and Strategy**: Migrating applications without cloud-native security controls.
4. **Insecure Interfaces and APIs**: Vulnerable REST/SOAP management APIs exposing control planes.
5. **Account Hijacking**: Compromised IAM access keys, missing MFA, credential stuffing.
6. **Malicious Insiders**: Rogue administrators or compromised internal accounts.
7. **Advanced Persistent Threats (APTs)**: Stealthy long-term cloud access.

### 2.2 Container & Kubernetes Security Architecture
- **Docker Security**: Unprivileged container execution, restricting `root` container users, preventing Docker socket (`/var/run/docker.sock`) mounting into unprivileged containers.
- **Kubernetes (K8s)**: Managing Role-Based Access Control (RBAC), securing Kubelet API (`port 10250`), disabling unauthenticated API server access, isolating pod namespaces.

> [!IMPORTANT] 🔄 **📋 Comprehensive Cloud Storage Security Matrix**

| Cloud Provider | Storage Service | Common Misconfiguration | Exploitation Tool | Defensive Mitigation |
| :--- | :--- | :--- | :--- | :--- |
| **AWS** | S3 Bucket | Public ACLs / `AllUsers` Policy | AWS CLI (`aws s3 ls`), S3Scanner | Block Public Access flag + KMS Encryption |
| **Azure** | Blob Storage | Public Container Access Level | MicroBurst / AzCopy | Private access level + SAS token expiration |
| **GCP** | Cloud Storage | `allUsers` / `allAuthenticatedUsers` IAM | gsutil (`gsutil ls`) | Uniform Bucket-Level Access + KMS |
