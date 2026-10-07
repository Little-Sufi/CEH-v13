# Lab 02: AWS Security & Misconfigurations

[⬅️ Previous](Lab-02-Intermediate-Track-Mobile-Security.md) | [🏠 Path Home](Home.md) | [Next Lab ➡️](Lab-04-Advanced-Track-Azure-Security.md)

---

## 🎯 Lab Objective
Exploit AWS misconfigurations.

## 🌐 Direct Lab Access
- TryHackMe (S3cret Santa): https://tryhackme.com/room/s3cretsanta
- Flaws.cloud Game: http://flaws.cloud/
- HackTricks Cloud AWS: https://cloud.hacktricks.xyz/pentesting-cloud/aws-security

---

## 🛠️ Required Tools
- AWS CLI: `sudo apt install awscli`
- Pacu: https://github.com/RhinoSecurityLabs/pacu

---

## 📝 AWS CLI Commands

### Configure Credentials
```bash
aws configure
```

### Check Identity
```bash
aws sts get-caller-identity
```

### List S3 Buckets
```bash
aws s3api list-buckets
```

### List Bucket Contents
```bash
aws s3 ls s3://bucket-name --recursive
```

### Download Files
```bash
aws s3 cp s3://bucket-name/file.txt .
```

---

## 📝 Common Misconfigurations
- Public S3 buckets
- Exposed IAM credentials
- Misconfigured IAM policies
- Public AMIs

---

## 🔗 Additional Resources
- Rhino Security Labs AWS: https://rhinosecuritylabs.com/aws/

---

[⬅️ Previous](Lab-02-Intermediate-Track-Mobile-Security.md) | [🏠 Path Home](Home.md) | [Next Lab ➡️](Lab-04-Advanced-Track-Azure-Security.md)
