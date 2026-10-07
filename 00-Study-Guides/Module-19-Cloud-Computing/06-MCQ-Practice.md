# 🎯 Module 19: Cloud Computing - Exam Scenario Practice Engine

> [!ABSTRACT] 📊 **Interactive Module Scorecard**
>
> - **Target Module**: Module 19: Cloud Computing
> - **Total Questions**: 25 Ultra-Detailed, 100% Unique Indirect Scenarios
> - **Exam Difficulty Standard**: Senior CEH v13 (Scenario-Driven Logic & Technical Deduction)
> - **Passing Threshold**: 85% Accuracy (22/25 Correct)
> 
> *Instructions: Evaluate the scenario context below. Select your choice, then expand the **Show Correct Answer & Exam Breakdown** callout to verify your answer and review the deep technical analysis and distractor refutations.*

---

### 🧩 Question 01 | Scenario Challenge

> [!QUESTION] 📌 **Scenario Context**
> An attacker exploits a Server-Side Request Forgery (SSRF) flaw in a web application hosted on an AWS EC2 instance by issuing a GET request to `http://169.254.169.254/latest/meta-data/iam/security-credentials/AdminRole`. The application returns an `AccessKeyId`, `SecretAccessKey`, and `Token`.
>
> What cloud defense mechanism specifically prevents this metadata credential theft?

#### 🔘 Available Options:

- **A**: Enforcing AWS Instance Metadata Service Version 2 (IMDSv2) requiring a session token header
- **B**: Enabling AWS S3 Bucket Versioning
- **C**: Configuring Azure Blob Storage SAS tokens
- **D**: Increasing EC2 CPU allocation

> [!SUCCESS]- 🔑 **Show Correct Answer & Exam Breakdown**
> **Correct Answer**: **Option A**
>
> #### 💡 Technical Deep Dive:
> AWS IMDSv2 mitigates SSRF metadata exploitation by requiring a session token obtained via an initial HTTP `PUT` request (`X-aws-ec2-metadata-token`), which standard SSRF payloads cannot forge.
>
> #### 🚫 Distractor Analysis & Refutations:
>
> - **Option B is incorrect** because S3 Versioning manages bucket file revisions.
> - **Option C is incorrect** because Azure Blob Storage is a Microsoft cloud service.
> - **Option D is incorrect** because CPU allocation does not affect HTTP metadata security.

---

### 🧩 Question 02 | Scenario Challenge

> [!QUESTION] 📌 **Scenario Context**
> Under the Cloud Security Alliance (CSA) Shared Responsibility Model, which security layer remains the SOLE responsibility of the customer across ALL service models (IaaS, PaaS, and SaaS)?

#### 🔘 Available Options:

- **A**: Data Governance, Classification, and Access Management (IAM)
- **B**: Physical Datacenter Security
- **C**: Hypervisor Patching
- **D**: Hardware Router Configuration

> [!SUCCESS]- 🔑 **Show Correct Answer & Exam Breakdown**
> **Correct Answer**: **Option A**
>
> #### 💡 Technical Deep Dive:
> Data security, data classification, and Identity and Access Management (IAM) are always the customer's responsibility regardless of whether IaaS, PaaS, or SaaS is deployed.
>
> #### 🚫 Distractor Analysis & Refutations:
>
> - **Option B is incorrect** because physical datacenter security is always managed by the CSP.
> - **Option C is incorrect** because hypervisor patching is the CSP's duty in PaaS and SaaS.
> - **Option D is incorrect** because hardware network infrastructure is maintained by the CSP.

---

### 🧩 Question 03 | Scenario Challenge

> [!QUESTION] 📌 **Scenario Context**
> A penetration tester uses the command `aws s3 ls s3://company-financial-backups --no-sign-request` and successfully downloads confidential CSV spreadsheets without providing any AWS credentials.
>
> What misconfiguration allowed this unauthenticated access?

#### 🔘 Available Options:

- **A**: The S3 bucket Access Control List (ACL) or Bucket Policy was misconfigured to allow public read permissions to `AllUsers`
- **B**: The EC2 instance was missing an elastic IP
- **C**: The CloudWatch logging service was disabled
- **D**: The bucket was encrypted with KMS

> [!SUCCESS]- 🔑 **Show Correct Answer & Exam Breakdown**
> **Correct Answer**: **Option A**
>
> #### 💡 Technical Deep Dive:
> `AllUsers` or public read bucket policies allow unauthenticated anonymous requests (`--no-sign-request`) to list and download bucket contents over the internet.
>
> #### 🚫 Distractor Analysis & Refutations:
>
> - **Option B is incorrect** because EC2 Elastic IPs do not dictate S3 bucket permissions.
> - **Option C is incorrect** because logging tracks activity, but does not block public access.
> - **Option D is incorrect** because KMS encryption protects data at rest, but public policies permit decryption if misconfigured.

---

### 🧩 Question 04 | Scenario Challenge

> [!QUESTION] 📌 **Scenario Context**
> A company deploys an application onto AWS Elastic Beanstalk where the cloud provider manages the OS, web server runtime, database engine, and hypervisor, leaving the company responsible only for application code and data.
>
> Which cloud service model is deployed?

#### 🔘 Available Options:

- **A**: Platform as a Service (PaaS)
- **B**: Infrastructure as a Service (IaaS)
- **C**: Software as a Service (SaaS)
- **D**: Function as a Service (FaaS)

> [!SUCCESS]- 🔑 **Show Correct Answer & Exam Breakdown**
> **Correct Answer**: **Option A**
>
> #### 💡 Technical Deep Dive:
> PaaS provides a pre-configured platform (OS, runtime, DB) where developers deploy their application code without managing underlying infrastructure.
>
> #### 🚫 Distractor Analysis & Refutations:
>
> - **Option B is incorrect** because IaaS requires customers to manage the OS and middleware.
> - **Option C is incorrect** because SaaS provides a complete vendor-managed application (e.g., Office 365).
> - **Option D is incorrect** because FaaS runs individual event-driven serverless functions.

---

### 🧩 Question 05 | Scenario Challenge

> [!QUESTION] 📌 **Scenario Context**
> An attacker mounts the host system's Docker socket (`/var/run/docker.sock`) into an unprivileged container and executes commands via the Docker API to spawn a new privileged container attached to the root filesystem.
>
> What attack vector was executed?

#### 🔘 Available Options:

- **A**: Docker Container Escape / Host Takeover
- **B**: SQL Injection
- **C**: Bluejacking
- **D**: BGP Route Hijacking

> [!SUCCESS]- 🔑 **Show Correct Answer & Exam Breakdown**
> **Correct Answer**: **Option A**
>
> #### 💡 Technical Deep Dive:
> Mounting `/var/run/docker.sock` inside a container grants full access to the Docker daemon, allowing attackers to escape the container and compromise the host host OS as `root`.
>
> #### 🚫 Distractor Analysis & Refutations:
>
> - **Option B is incorrect** because SQLi manipulates database queries.
> - **Option C is incorrect** because Bluejacking targets Bluetooth devices.
> - **Option D is incorrect** because BGP hijacking manipulates internet routing tables.

---

### 🧩 Question 06 | Scenario Challenge

> [!QUESTION] 📌 **Scenario Context**
> What open-source post-exploitation framework written in Python allows penetration testers to automate privilege escalation, IAM permission scanning, and data exfiltration specifically within AWS environments?

#### 🔘 Available Options:

- **A**: Pacu
- **B**: Nikto
- **C**: Wireshark
- **D**: Aircrack-ng

> [!SUCCESS]- 🔑 **Show Correct Answer & Exam Breakdown**
> **Correct Answer**: **Option A**
>
> #### 💡 Technical Deep Dive:
> Pacu is the premier open-source AWS exploitation framework created by Rhino Security Labs for post-exploitation testing.
>
> #### 🚫 Distractor Analysis & Refutations:
>
> - **Option B is incorrect** because Nikto is a web vulnerability scanner.
> - **Option C is incorrect** because Wireshark is a packet sniffer.
> - **Option D is incorrect** because Aircrack-ng audits Wi-Fi.

---

### 🧩 Question 07 | Scenario Challenge

> [!QUESTION] 📌 **Scenario Context**
> What multi-cloud security auditing tool assesses AWS, Azure, GCP, and Alibaba Cloud environments to generate interactive HTML security risk reports based on configuration APIs?

#### 🔘 Available Options:

- **A**: Scout Suite
- **B**: John the Ripper
- **C**: Reaver
- **D**: Ettercap

> [!SUCCESS]- 🔑 **Show Correct Answer & Exam Breakdown**
> **Correct Answer**: **Option A**
>
> #### 💡 Technical Deep Dive:
> Scout Suite is an open-source multi-cloud security auditing tool that queries cloud provider APIs to identify security misconfigurations.
>
> #### 🚫 Distractor Analysis & Refutations:
>
> - **Option B is incorrect** because John the Ripper is a password cracker.
> - **Option C is incorrect** because Reaver attacks WPS PINs.
> - **Option D is incorrect** because Ettercap is an ARP spoofing tool.

---

### 🧩 Question 08 | Scenario Challenge

> [!QUESTION] 📌 **Scenario Context**
> What cloud deployment model combines a private corporate datacenter with a public cloud provider, allowing workloads to burst into the public cloud during peak traffic demands via secure VPN links?

#### 🔘 Available Options:

- **A**: Hybrid Cloud
- **B**: Public Cloud
- **C**: Community Cloud
- **D**: Serverless Cloud

> [!SUCCESS]- 🔑 **Show Correct Answer & Exam Breakdown**
> **Correct Answer**: **Option A**
>
> #### 💡 Technical Deep Dive:
> Hybrid Cloud connects private infrastructure (on-premises) with public cloud infrastructure, enabling workload portability and cloud bursting.
>
> #### 🚫 Distractor Analysis & Refutations:
>
> - **Option B is incorrect** because Public Cloud relies entirely on third-party infrastructure.
> - **Option C is incorrect** because Community Cloud is shared among multiple organizations with shared concerns.
> - **Option D is incorrect** because Serverless is an execution model, not a deployment model.

---

### 🧩 Question 09 | Scenario Challenge

> [!QUESTION] 📌 **Scenario Context**
> An attacker discovers an open Kubernetes API server on TCP port `10250` that allows unauthenticated request execution.
>
> What component in Kubernetes was left exposed?

#### 🔘 Available Options:

- **A**: Kubelet API
- **B**: Docker Daemon
- **C**: etcd Database
- **D**: AWS S3

> [!SUCCESS]- 🔑 **Show Correct Answer & Exam Breakdown**
> **Correct Answer**: **Option A**
>
> #### 💡 Technical Deep Dive:
> Kubelet runs on each node listening on port 10250; unauthenticated access to the Kubelet API allows attackers to run commands inside any pod.
>
> #### 🚫 Distractor Analysis & Refutations:
>
> - **Option B is incorrect** because Docker daemon defaults to socket `/var/run/docker.sock` or port 2375.
> - **Option C is incorrect** because etcd defaults to port 2379.
> - **Option D is incorrect** because AWS S3 is an AWS storage service.

---

### 🧩 Question 10 | Scenario Challenge

> [!QUESTION] 📌 **Scenario Context**
> What automated tool specializes in scanning container images, file systems, and Infrastructure as Code (IaC) Terraform templates for known security vulnerabilities and secrets?

#### 🔘 Available Options:

- **A**: Trivy
- **B**: SQLmap
- **C**: Hashcat
- **D**: Aircrack-ng

> [!SUCCESS]- 🔑 **Show Correct Answer & Exam Breakdown**
> **Correct Answer**: **Option A**
>
> #### 💡 Technical Deep Dive:
> Trivy (by Aqua Security) is a comprehensive vulnerability and misconfiguration scanner for containers, git repositories, and IaC files.
>
> #### 🚫 Distractor Analysis & Refutations:
>
> - **Option B is incorrect** because SQLmap automates SQL injection.
> - **Option C is incorrect** because Hashcat is a password cracker.
> - **Option D is incorrect** because Aircrack-ng audits Wi-Fi.

---

### 🧩 Question 11 | Scenario Challenge

> [!QUESTION] 📌 **Scenario Context**
> What IAM misconfiguration practice allows an attacker who compromises a developer's access key to escalate privileges to full administrator access in AWS?

#### 🔘 Available Options:

- **A**: Wildcard Permission Policies (`"Action": "*", "Resource": "*"`) attached to developer roles
- **B**: Enforcing Multi-Factor Authentication (MFA)
- **C**: Using IMDSv2
- **D**: Enabling CloudTrail logs

> [!SUCCESS]- 🔑 **Show Correct Answer & Exam Breakdown**
> **Correct Answer**: **Option A**
>
> #### 💡 Technical Deep Dive:
> Assigning wildcard policies (`"Action": "*"`) grants unrestricted administrative privileges to any user or service holding that role.
>
> #### 🚫 Distractor Analysis & Refutations:
>
> - **Option B is incorrect** because MFA prevents unauthorized password reuse.
> - **Option C is incorrect** because IMDSv2 protects instance metadata.
> - **Option D is incorrect** because CloudTrail logs audit events.

---

### 🧩 Question 12 | Scenario Challenge

> [!QUESTION] 📌 **Scenario Context**
> What Cloud Security Alliance (CSA) threat classification describes vulnerabilities arising from unauthorized access keys embedded in public GitHub repositories?

#### 🔘 Available Options:

- **A**: Account Hijacking / Insecure Credentials
- **B**: Hardware Component Failure
- **C**: Hypervisor Crash
- **D**: Natural Disaster

> [!SUCCESS]- 🔑 **Show Correct Answer & Exam Breakdown**
> **Correct Answer**: **Option A**
>
> #### 💡 Technical Deep Dive:
> Hardcoding cloud credentials in source code repositories leads to account hijacking and compromise of cloud control planes.
>
> #### 🚫 Distractor Analysis & Refutations:
>
> - **Option B is incorrect** because component failure is hardware related.
> - **Option C is incorrect** because hypervisor crashes affect host software.
> - **Option D is incorrect** because natural disasters affect physical datacenters.

---

### 🧩 Question 13 | Scenario Challenge

> [!QUESTION] 📌 **Scenario Context**
> What Cloud Native Computing Foundation (CNCF) database component stores the configuration state and cluster secrets for a Kubernetes cluster?

#### 🔘 Available Options:

- **A**: etcd
- **B**: MySQL
- **C**: Redis
- **D**: PostgreSQL

> [!SUCCESS]- 🔑 **Show Correct Answer & Exam Breakdown**
> **Correct Answer**: **Option A**
>
> #### 💡 Technical Deep Dive:
> `etcd` is the strongly consistent, distributed key-value store used by Kubernetes as its primary data store for all cluster data.
>
> #### 🚫 Distractor Analysis & Refutations:
>
> - **Option B is incorrect** because MySQL is a relational database.
> - **Option C is incorrect** because Redis is an in-memory cache.
> - **Option D is incorrect** because PostgreSQL is a relational database.

---

### 🧩 Question 14 | Scenario Challenge

> [!QUESTION] 📌 **Scenario Context**
> An attacker uses a PowerShell toolkit named `MicroBurst` during a penetration test. What cloud platform is specifically targeted by MicroBurst?

#### 🔘 Available Options:

- **A**: Microsoft Azure
- **B**: Amazon Web Services (AWS)
- **C**: Google Cloud Platform (GCP)
- **D**: IBM Cloud

> [!SUCCESS]- 🔑 **Show Correct Answer & Exam Breakdown**
> **Correct Answer**: **Option A**
>
> #### 💡 Technical Deep Dive:
> MicroBurst is a suite of PowerShell scripts designed for Azure security auditing and post-exploitation.
>
> #### 🚫 Distractor Analysis & Refutations:
>
> - **Option B is incorrect** because AWS is targeted by tools like Pacu.
> - **Option C is incorrect** because GCP uses tools like Hayai/GCP-IAM-Collector.
> - **Option D is incorrect** because IBM Cloud is an independent CSP.

---

### 🧩 Question 15 | Scenario Challenge

> [!QUESTION] 📌 **Scenario Context**
> What execution model allows developers to run event-triggered code snippets (e.g., AWS Lambda) without provisioning, managing, or patching underlying virtual machines?

#### 🔘 Available Options:

- **A**: Function as a Service (FaaS) / Serverless
- **B**: Infrastructure as a Service (IaaS)
- **C**: Storage as a Service
- **D**: Bare Metal Hosting

> [!SUCCESS]- 🔑 **Show Correct Answer & Exam Breakdown**
> **Correct Answer**: **Option A**
>
> #### 💡 Technical Deep Dive:
> Serverless / FaaS executes functions in ephemeral containers managed dynamically by the cloud provider.
>
> #### 🚫 Distractor Analysis & Refutations:
>
> - **Option B is incorrect** because IaaS requires provisioned VMs.
> - **Option C is incorrect** because Storage as a Service provides object/block storage.
> - **Option D is incorrect** because Bare Metal provides dedicated physical servers.

---

### 🧩 Question 16 | Scenario Challenge

> [!QUESTION] 📌 **Scenario Context**
> What AWS service continuously logs, monitors, and retains account activity related to actions across your AWS infrastructure (API calls, console logins)?

#### 🔘 Available Options:

- **A**: AWS CloudTrail
- **B**: AWS S3
- **C**: AWS EC2
- **D**: AWS Route 53

> [!SUCCESS]- 🔑 **Show Correct Answer & Exam Breakdown**
> **Correct Answer**: **Option A**
>
> #### 💡 Technical Deep Dive:
> AWS CloudTrail provides auditing, security monitoring, and operational troubleshooting by logging all API actions.
>
> #### 🚫 Distractor Analysis & Refutations:
>
> - **Option B is incorrect** because S3 is object storage.
> - **Option C is incorrect** because EC2 provides virtual servers.
> - **Option D is incorrect** because Route 53 is a DNS service.

---

### 🧩 Question 17 | Scenario Challenge

> [!QUESTION] 📌 **Scenario Context**
> An administrator configures an AWS S3 bucket to encrypt objects automatically before storing them on disk using keys managed by AWS Key Management Service.
>
> What security principle is applied?

#### 🔘 Available Options:

- **A**: Data Encryption at Rest (Server-Side Encryption / SSE-KMS)
- **B**: Data Encryption in Transit
- **C**: Data Masking
- **D**: Session Hijacking

> [!SUCCESS]- 🔑 **Show Correct Answer & Exam Breakdown**
> **Correct Answer**: **Option A**
>
> #### 💡 Technical Deep Dive:
> SSE-KMS encrypts data at rest on disk before storing it in S3 buckets.
>
> #### 🚫 Distractor Analysis & Refutations:
>
> - **Option B is incorrect** because Encryption in Transit uses TLS during wire transfer.
> - **Option C is incorrect** because Data Masking obfuscates UI text.
> - **Option D is incorrect** because Session Hijacking is an attack vector.

---

### 🧩 Question 18 | Scenario Challenge

> [!QUESTION] 📌 **Scenario Context**
> What tool performs CIS Benchmark security assessment checks specifically against AWS cloud environments?

#### 🔘 Available Options:

- **A**: Prowler
- **B**: Wireshark
- **C**: John the Ripper
- **D**: Aircrack-ng

> [!SUCCESS]- 🔑 **Show Correct Answer & Exam Breakdown**
> **Correct Answer**: **Option A**
>
> #### 💡 Technical Deep Dive:
> Prowler is an open-source security tool for AWS (and Azure/GCP) aligned with CIS Benchmarks.
>
> #### 🚫 Distractor Analysis & Refutations:
>
> - **Option B is incorrect** because Wireshark is a packet sniffer.
> - **Option C is incorrect** because John the Ripper is a password cracker.
> - **Option D is incorrect** because Aircrack-ng audits Wi-Fi.

---

### 🧩 Question 19 | Scenario Challenge

> [!QUESTION] 📌 **Scenario Context**
> What cloud storage security misconfiguration in Google Cloud Platform allows any user authenticated with ANY Google account to read bucket files?

#### 🔘 Available Options:

- **A**: Assigning `allAuthenticatedUsers` access permissions to the bucket
- **B**: Enabling KMS Encryption
- **C**: Disabling HTTP port 80
- **D**: Using Cloud CDN

> [!SUCCESS]- 🔑 **Show Correct Answer & Exam Breakdown**
> **Correct Answer**: **Option A**
>
> #### 💡 Technical Deep Dive:
> In GCP, `allAuthenticatedUsers` grants access to anyone logged into ANY valid Google account worldwide, not just users in the target organization.
>
> #### 🚫 Distractor Analysis & Refutations:
>
> - **Option B is incorrect** because KMS encryption protects data at rest.
> - **Option C is incorrect** because disabling HTTP improves security.
> - **Option D is incorrect** because Cloud CDN caches content.

---

### 🧩 Question 20 | Scenario Challenge

> [!QUESTION] 📌 **Scenario Context**
> What security solution category continuously monitors multi-cloud infrastructure to detect misconfigurations, compliance violations, and unhardened cloud resources?

#### 🔘 Available Options:

- **A**: Cloud Security Posture Management (CSPM)
- **B**: Virtual Private Network (VPN)
- **C**: Domain Name System (DNS)
- **D**: Intrusion Prevention System (IPS)

> [!SUCCESS]- 🔑 **Show Correct Answer & Exam Breakdown**
> **Correct Answer**: **Option A**
>
> #### 💡 Technical Deep Dive:
> CSPM tools continuously audit cloud resource configurations against security standards and compliance baselines.
>
> #### 🚫 Distractor Analysis & Refutations:
>
> - **Option B is incorrect** because VPN provides encrypted tunnels.
> - **Option C is incorrect** because DNS resolves hostnames.
> - **Option D is incorrect** because IPS filters network packets.

---

### 🧩 Question 21 | Scenario Challenge

> [!QUESTION] 📌 **Scenario Context**
> What feature in AWS Virtual Private Cloud (VPC) acts as a stateless virtual firewall controlling inbound and outbound traffic at the subnet level?

#### 🔘 Available Options:

- **A**: Network Access Control List (NACL)
- **B**: Security Group
- **C**: Internet Gateway
- **D**: Route Table

> [!SUCCESS]- 🔑 **Show Correct Answer & Exam Breakdown**
> **Correct Answer**: **Option A**
>
> #### 💡 Technical Deep Dive:
> NACLs are stateless sub-net level firewalls in AWS VPCs that require explicit rules for both inbound and outbound traffic.
>
> #### 🚫 Distractor Analysis & Refutations:
>
> - **Option B is incorrect** because Security Groups are stateful firewalls attached at the instance (ENI) level.
> - **Option C is incorrect** because Internet Gateways provide internet connectivity.
> - **Option D is incorrect** because Route Tables direct network traffic.

---

### 🧩 Question 22 | Scenario Challenge

> [!QUESTION] 📌 **Scenario Context**
> An attacker uses `s3scanner search --bucket target-company` to discover publicly accessible cloud storage locations across multiple domains.
>
> What open-source Python tool was executed?

#### 🔘 Available Options:

- **A**: S3Scanner
- **B**: Metasploit
- **C**: Wireshark
- **D**: Hashcat

> [!SUCCESS]- 🔑 **Show Correct Answer & Exam Breakdown**
> **Correct Answer**: **Option A**
>
> #### 💡 Technical Deep Dive:
> S3Scanner is a tool that scans for open AWS S3 buckets and dumps their contents.
>
> #### 🚫 Distractor Analysis & Refutations:
>
> - **Option B is incorrect** because Metasploit is an exploitation framework.
> - **Option C is incorrect** because Wireshark sniffs network traffic.
> - **Option D is incorrect** because Hashcat cracks passwords.

---

### 🧩 Question 23 | Scenario Challenge

> [!QUESTION] 📌 **Scenario Context**
> What cloud architecture deployment model is shared by several organizations with common security, compliance, or mission requirements (e.g., joint military or university research facilities)?

#### 🔘 Available Options:

- **A**: Community Cloud
- **B**: Public Cloud
- **C**: Private Cloud
- **D**: Single-Tenant IaaS

> [!SUCCESS]- 🔑 **Show Correct Answer & Exam Breakdown**
> **Correct Answer**: **Option A**
>
> #### 💡 Technical Deep Dive:
> Community Cloud infrastructure is shared among organizations that have shared concerns (mission, security requirements, compliance).
>
> #### 🚫 Distractor Analysis & Refutations:
>
> - **Option B is incorrect** because Public Cloud is open to the general public.
> - **Option C is incorrect** because Private Cloud is dedicated to a single organization.
> - **Option D is incorrect** because Single-Tenant IaaS is dedicated private infrastructure.

---

### 🧩 Question 24 | Scenario Challenge

> [!QUESTION] 📌 **Scenario Context**
> What Docker runtime flag prevents a compromised container process from gaining root privileges on the host system even if the container user ID is `0`?

#### 🔘 Available Options:

- **A**: Running containers with User Namespaces enabled (`--userns-remap`)
- **B**: Mounting `/var/run/docker.sock`
- **C**: Disabling SELinux
- **D**: Using `--privileged` flag

> [!SUCCESS]- 🔑 **Show Correct Answer & Exam Breakdown**
> **Correct Answer**: **Option A**
>
> #### 💡 Technical Deep Dive:
> User Namespaces (`--userns-remap`) maps container root (`UID 0`) to an unprivileged high-numbered UID on the host OS, preventing root host compromise.
>
> #### 🚫 Distractor Analysis & Refutations:
>
> - **Option B is incorrect** because mounting docker.sock leads to container escape.
> - **Option C is incorrect** because disabling SELinux reduces security.
> - **Option D is incorrect** because `--privileged` grants full host capabilities to the container.

---

### 🧩 Question 25 | Scenario Challenge

> [!QUESTION] 📌 **Scenario Context**
> What is the primary operational objective of implementing cloud-native Web Application Firewalls (such as AWS WAF or Azure WAF) at the edge ingress layer?

#### 🔘 Available Options:

- **A**: To inspect inbound HTTP/HTTPS web traffic and block common application-layer attacks (SQLi, XSS, SSRF) before reaching backend cloud instances
- **B**: To format EC2 hard drives
- **C**: To generate SSH keys
- **D**: To assign internal IP addresses

> [!SUCCESS]- 🔑 **Show Correct Answer & Exam Breakdown**
> **Correct Answer**: **Option A**
>
> #### 💡 Technical Deep Dive:
> WAFs inspect Layer 7 web traffic at edge locations to filter out malicious payloads targeting web applications.
>
> #### 🚫 Distractor Analysis & Refutations:
>
> - **Option B is incorrect** because WAFs do not format hard drives.
> - **Option C is incorrect** because SSH keys are generated by PKI/ssh-keygen.
> - **Option D is incorrect** because IP assignment is handled by VPC DHCP.
