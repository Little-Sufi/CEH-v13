# 04. Countermeasures — Social Engineering

> [!SHIELD] 🏰 **Defensive Security Controls & Email Authentication Standards**
> Direct technical extraction from official CEH v13 Syllabus (Module 09). Covers Email Security Protocols (SPF, DKIM, DMARC), Multi-Factor Authentication (MFA), FIDO2 Passkeys, and Physical Access Defenses.

---

## 🛡️ 1. Email Security Protocols (SPF, DKIM, DMARC)

### 1.1 Preventing Email Header Spoofing
To block attackers from sending emails with spoofed corporate domain headers (`sender@company.com`), organizations implement three DNS authentication protocols:

1. **SPF (Sender Policy Framework)**: A DNS TXT record that specifies which mail server IP addresses are authorized to send email on behalf of a domain.
   - Example: `v=spf1 ip4:192.168.1.10 include:_spf.google.com ~all`
2. **DKIM (DomainKeys Identified Mail)**: Adds a cryptographic digital signature to outbound email headers. Receiving mail servers verify the signature using the sender's public key published in DNS.
3. **DMARC (Domain-based Message Authentication, Reporting, and Conformance)**: Uses SPF and DKIM validation to tell receiving mail servers how to handle emails that fail authentication (`p=none`, `p=quarantine`, or `p=reject`).

> [!SHIELD] 🏰 **📋 Comprehensive Email Security Standard Reference Matrix**

| Protocol Standard | Technical Mechanism | DNS Record Type | Defensive Function |
| :--- | :--- | :---: | :--- |
| **SPF** | Lists authorized sending IP addresses | TXT | Prevents IP address spoofing in email headers |
| **DKIM** | Cryptographically signs email headers | TXT | Ensures email content integrity & authenticity |
| **DMARC** | Enforces policy on SPF/DKIM failures | TXT | Instructs servers to reject spoofed emails (`p=reject`) |
| **FIDO2 / Passkeys**| WebAuthn hardware token authentication | Hardware | Eliminates phishing 2FA bypass attacks |
