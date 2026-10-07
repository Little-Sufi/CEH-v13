# 02. Attack Techniques — Social Engineering

> [!WARNING] ⚡ **Attack Methodologies, Insider Threats & Identity Theft**
> Direct extraction from official CEH v13 Syllabus (Module 09). Covers Phishing Mechanics, Insider Threat Taxonomy, Social Engineering Toolkit (SET) Execution, and Email Header Spoofing.

---

## ⚔️ 1. Insider Threats & Identity Theft Architecture

### 1.1 Insider Threat Taxonomies
An Insider Threat is a current or former employee, contractor, or business partner who has authorized access to an organization's network and intentionally or unintentionally misuses that access to harm the organization.

#### 4 Insider Threat Types:
1. **Malicious Insider**: An employee who intentionally steals data, sabotages systems, or sells corporate secrets for financial gain or revenge.
2. **Careless / Negligent Insider**: An employee who unintentionally exposes sensitive data due to poor security hygiene (e.g., clicking phishing links, using weak passwords, misconfiguring S3 buckets).
3. **Compromised Insider**: An employee whose legitimate credentials or endpoint device have been breached by external threat actors without their knowledge.
4. **Disgruntled Employee**: An employee seeking revenge against the organization following termination or missed promotions.

> [!DANGER] 🛡️ **📋 Comprehensive Insider Threat Reference Matrix**

| Insider Category | Motivation / Trigger | Typical Technical Actions | Detection Indicator |
| :--- | :--- | :--- | :--- |
| **Malicious** | Financial greed / Corporate espionage | Mass exfiltration of database records to USB | Unscheduled off-hours data transfers |
| **Careless** | Lack of security awareness | Falling for phishing emails, using public Wi-Fi | Repeated security policy violations |
| **Compromised** | External malware infection | Credential theft via keylogger/stealer | Login attempts from abnormal locations |
| **Disgruntled** | Resentment / Termination | Logical bomb deployment, deleting backup files | Unauthorized access to HR files |

---

## 🛡️ 2. Technical Phishing Frameworks & SET Execution

### 2.1 Social Engineering Toolkit (SET) Workflow
The Social Engineering Toolkit (SET) created by TrustedSec is an open-source Python framework designed for executing automated social engineering attacks:

```bash
# Launch Social Engineering Toolkit (SET)
sudo setoolkit
```

#### Core SET Attack Modules:
1. **Spear-Phishing Attack Vector**: Generates custom emails attached with malicious PDF/Word payloads.
2. **Website Attack Vectors**:
   - **Java Applet Attack**: Hosts malicious Java applets.
   - **Credential Harvester Attack**: Clones target login pages (e.g., Office365, Google) and logs submitted credentials.
   - **Metasploit Browser Exploit**: Launches automated browser exploits against visiting targets.

> [!SHIELD] 🏰 **📋 Comprehensive SET Module Reference Matrix**

| SET Module | Operational Mechanism | Target Output | Primary Evasion Vector |
| :--- | :--- | :--- | :--- |
| **Credential Harvester**| Clones target login web page | Intercepts cleartext username & password | Spoofed look-alike domain (Typosquatting) |
| **Mass Mailer** | Sends bulk phishing emails via SMTP | Delivers malicious links to thousands | Bypasses basic spam filters via open relays |
| **Payload Generator** | Generates executable Trojans wrapped in code | Establishes persistent shell callback | Obfuscates Metasploit payloads |
