# 🎯 Module 09: Social Engineering - Exam Scenario Practice Engine

> [!ABSTRACT] 📊 **Interactive Module Scorecard**
>
> - **Target Module**: Module 09: Social Engineering
> - **Total Questions**: 25 Ultra-Detailed, 100% Unique Indirect Scenarios
> - **Exam Difficulty Standard**: Senior CEH v13 (Scenario-Driven Logic & Technical Deduction)
> - **Passing Threshold**: 85% Accuracy (22/25 Correct)
> 
> *Instructions: Evaluate the scenario context below. Select your choice, then expand the **Show Correct Answer & Exam Breakdown** callout to verify your answer and review the deep technical analysis and distractor refutations.*

---

### 🧩 Question 01 | Scenario Challenge

> [!QUESTION] 📌 **Scenario Context**
> An attacker calls an executive assistant, impersonating the corporate Chief Executive Officer (CEO). The caller claims to be at an airport about to board a flight and urgently demands that the assistant transfer $50,000 to an offshore vendor account within 10 minutes to avoid losing a critical contract.
>
> What combination of psychological triggers is being exploited in this Whaling attack?

#### 🔘 Available Options:

- **A**: Authority and Urgency/Intimidation
- **B**: Social Proof and Reciprocity
- **C**: Scarcity and Liking
- **D**: Consensus and Trust

> [!SUCCESS]- 🔑 **Show Correct Answer & Exam Breakdown**
> **Correct Answer**: **Option A**
>
> #### 💡 Technical Deep Dive:
> The attacker leverages Authority (impersonating the CEO) and Urgency/Intimidation (10-minute time constraint threatening loss of contract) to induce panic and compliance.
>
> #### 🚫 Distractor Analysis & Refutations:
>
> - **Option B is incorrect** because Social Proof relies on group behavior and Reciprocity relies on returning favors.
> - **Option C is incorrect** because Scarcity relies on limited item availability and Liking relies on personal rapport.
> - **Option D is incorrect** because Consensus relies on peer actions.

---

### 🧩 Question 02 | Scenario Challenge

> [!QUESTION] 📌 **Scenario Context**
> A penetration tester walks up to a secure corporate building entrance holding two large coffee trays and a box of donuts. As an employee scans their badge, the tester smiles and asks the employee to hold the door open.
>
> What physical social engineering vector was executed?

#### 🔘 Available Options:

- **A**: Piggybacking
- **B**: Tailgating
- **C**: Pretexting
- **D**: Dumpster Diving

> [!SUCCESS]- 🔑 **Show Correct Answer & Exam Breakdown**
> **Correct Answer**: **Option A**
>
> #### 💡 Technical Deep Dive:
> Piggybacking involves asking an authorized individual to hold a secure door open (often relying on courtesy), whereas Tailgating involves following behind without the target's explicit permission/knowledge.
>
> #### 🚫 Distractor Analysis & Refutations:
>
> - **Option B is incorrect** because Tailgating occurs when an attacker sneaks behind without interacting/asking.
> - **Option C is incorrect** because Pretexting is creating a fake scenario over phone/email.
> - **Option D is incorrect** because Dumpster Diving searches trash bins.

---

### 🧩 Question 03 | Scenario Challenge

> [!QUESTION] 📌 **Scenario Context**
> An attacker compromises a popular online forum frequently visited by industrial control system (ICS) engineers and injects a zero-day browser exploit into the site's JavaScript files to compromise visiting engineers' laptops.
>
> What specific computer-based social engineering attack was executed?

#### 🔘 Available Options:

- **A**: Watering Hole Attack
- **B**: Pharming Attack
- **C**: Spear Phishing Attack
- **D**: Vishing Attack

> [!SUCCESS]- 🔑 **Show Correct Answer & Exam Breakdown**
> **Correct Answer**: **Option A**
>
> #### 💡 Technical Deep Dive:
> A Watering Hole attack compromises a legitimate website known to be frequented by a specific target group to infect their endpoints.
>
> #### 🚫 Distractor Analysis & Refutations:
>
> - **Option B is incorrect** because Pharming manipulates DNS resolution to redirect users.
> - **Option C is incorrect** because Spear Phishing uses targeted emails.
> - **Option D is incorrect** because Vishing uses voice calls.

---

### 🧩 Question 04 | Scenario Challenge

> [!QUESTION] 📌 **Scenario Context**
> What DNS TXT protocol record specifies which IP addresses are authorized to transmit outbound email on behalf of an enterprise domain (`v=spf1 ip4:192.168.1.10 ~all`)?

#### 🔘 Available Options:

- **A**: SPF (Sender Policy Framework)
- **B**: DKIM (DomainKeys Identified Mail)
- **C**: DMARC
- **D**: MX Record

> [!SUCCESS]- 🔑 **Show Correct Answer & Exam Breakdown**
> **Correct Answer**: **Option A**
>
> #### 💡 Technical Deep Dive:
> SPF (Sender Policy Framework) is a DNS TXT record that defines authorized sending IP addresses for a domain.
>
> #### 🚫 Distractor Analysis & Refutations:
>
> - **Option B is incorrect** because DKIM provides cryptographic header signatures.
> - **Option C is incorrect** because DMARC enforces handling policies for SPF/DKIM failures.
> - **Option D is incorrect** because MX records define inbound mail server IPs.

---

### 🧩 Question 05 | Scenario Challenge

> [!QUESTION] 📌 **Scenario Context**
> Which open-source social engineering framework developed by TrustedSec provides automated modules for cloning login web pages, launching spear-phishing campaigns, and embedding Metasploit payloads?

#### 🔘 Available Options:

- **A**: SET (Social-Engineer Toolkit)
- **B**: Maltego
- **C**: Wireshark
- **D**: Nikto

> [!SUCCESS]- 🔑 **Show Correct Answer & Exam Breakdown**
> **Correct Answer**: **Option A**
>
> #### 💡 Technical Deep Dive:
> SET (Social-Engineer Toolkit) created by TrustedSec is the industry-standard framework for automated social engineering testing.
>
> #### 🚫 Distractor Analysis & Refutations:
>
> - **Option B is incorrect** because Maltego is an OSINT mapping tool.
> - **Option C is incorrect** because Wireshark is a packet analyzer.
> - **Option D is incorrect** because Nikto is a web scanner.

---

### 🧩 Question 06 | Scenario Challenge

> [!QUESTION] 📌 **Scenario Context**
> An attacker secretly corrupts a critical database driver on a financial server. Shortly after, the attacker drops fake tech support flyers in the breakroom. When the system administrator calls the number on the flyer, the attacker poses as a technician and requests root credentials to "fix" the issue.
>
> What complex social engineering methodology was executed?

#### 🔘 Available Options:

- **A**: Reverse Social Engineering
- **B**: Waterhole Attack
- **C**: Phishing
- **D**: Dumpster Diving

> [!SUCCESS]- 🔑 **Show Correct Answer & Exam Breakdown**
> **Correct Answer**: **Option A**
>
> #### 💡 Technical Deep Dive:
> Reverse Social Engineering follows a 3-step sequence: Sabotage (cause problem), Advertising (offer help), and Assistance (extract credentials when target calls).
>
> #### 🚫 Distractor Analysis & Refutations:
>
> - **Option B is incorrect** because Waterhole attacks compromise websites.
> - **Option C is incorrect** because Phishing sends emails.
> - **Option D is incorrect** because Dumpster Diving searches trash.

---

### 🧩 Question 07 | Scenario Challenge

> [!QUESTION] 📌 **Scenario Context**
> An employee who was recently passed over for a promotion uses their legitimate administrative credentials to copy confidential patent files to an unencrypted USB drive before resigning.
>
> What type of threat actor does this represent?

#### 🔘 Available Options:

- **A**: Malicious / Disgruntled Insider
- **B**: Careless Insider
- **C**: External Hacktivist
- **D**: Script Kiddie

> [!SUCCESS]- 🔑 **Show Correct Answer & Exam Breakdown**
> **Correct Answer**: **Option A**
>
> #### 💡 Technical Deep Dive:
> A Malicious or Disgruntled Insider is an authorized employee who intentionally misuses access to steal data or sabotage systems.
>
> #### 🚫 Distractor Analysis & Refutations:
>
> - **Option B is incorrect** because Careless Insiders make unintentional security mistakes.
> - **Option C is incorrect** because External Hacktivists lack internal authorized access.
> - **Option D is incorrect** because Script Kiddies use pre-made tools without internal access.

---

### 🧩 Question 08 | Scenario Challenge

> [!QUESTION] 📌 **Scenario Context**
> What DNS authentication record instructs receiving mail servers to reject (`p=reject`) outbound emails that fail both SPF and DKIM checks?

#### 🔘 Available Options:

- **A**: DMARC
- **B**: SPF
- **C**: DKIM
- **D**: PTR

> [!SUCCESS]- 🔑 **Show Correct Answer & Exam Breakdown**
> **Correct Answer**: **Option A**
>
> #### 💡 Technical Deep Dive:
> DMARC (Domain-based Message Authentication, Reporting, and Conformance) allows domain owners to declare how receiver mail servers should handle failed SPF/DKIM emails.
>
> #### 🚫 Distractor Analysis & Refutations:
>
> - **Option B is incorrect** because SPF specifies authorized sending IPs.
> - **Option C is incorrect** because DKIM signs headers.
> - **Option D is incorrect** because PTR records map IP addresses to hostnames.

---

### 🧩 Question 09 | Scenario Challenge

> [!QUESTION] 📌 **Scenario Context**
> An attacker uses a reverse-proxy tool (`Evilginx2`) to proxy traffic between a victim and a real Microsoft 365 login portal. The tool intercepts the victim's session cookies upon login.
>
> What major security control is bypassed by this attack?

#### 🔘 Available Options:

- **A**: Traditional Multi-Factor Authentication (MFA / SMS / TOTP)
- **B**: Disk Encryption (BitLocker)
- **C**: Firewall IP ACLs
- **D**: Antivirus Signatures

> [!SUCCESS]- 🔑 **Show Correct Answer & Exam Breakdown**
> **Correct Answer**: **Option A**
>
> #### 💡 Technical Deep Dive:
> Reverse proxy phishing frameworks like Evilginx2 intercept 2FA tokens and authentication session cookies in real-time, bypassing traditional SMS/TOTP MFA.
>
> #### 🚫 Distractor Analysis & Refutations:
>
> - **Option B is incorrect** because BitLocker encrypts hard drives at rest.
> - **Option C is incorrect** because Firewalls filter IP packets.
> - **Option D is incorrect** because Antivirus checks binaries.

---

### 🧩 Question 10 | Scenario Challenge

> [!QUESTION] 📌 **Scenario Context**
> What authentication standard relies on public-key cryptography and hardware tokens (WebAuthn / FIDO2 Passkeys) to provide complete protection against phishing and 2FA relay attacks?

#### 🔘 Available Options:

- **A**: FIDO2 / Passkeys
- **B**: SMS OTP
- **C**: Push Notifications
- **D**: Security Questions

> [!SUCCESS]- 🔑 **Show Correct Answer & Exam Breakdown**
> **Correct Answer**: **Option A**
>
> #### 💡 Technical Deep Dive:
> FIDO2 / WebAuthn standardizes cryptographic hardware token authentication bound to the exact origin domain, making phishing and reverse-proxy relay attacks impossible.
>
> #### 🚫 Distractor Analysis & Refutations:
>
> - **Option B is incorrect** because SMS OTP is vulnerable to SIM swapping and phishing.
> - **Option C is incorrect** because Push Notifications are vulnerable to MFA fatigue attacks.
> - **Option D is incorrect** because Security Questions can be easily researched via OSINT.

---

### 🧩 Question 11 | Scenario Challenge

> [!QUESTION] 📌 **Scenario Context**
> What term describes phishing conducted via SMS mobile text messages?

#### 🔘 Available Options:

- **A**: Smishing
- **B**: Vishing
- **C**: Pharming
- **D**: Spimming

> [!SUCCESS]- 🔑 **Show Correct Answer & Exam Breakdown**
> **Correct Answer**: **Option A**
>
> #### 💡 Technical Deep Dive:
> Smishing refers to social engineering phishing attacks delivered via SMS text messages.
>
> #### 🚫 Distractor Analysis & Refutations:
>
> - **Option B is incorrect** because Vishing uses voice phone calls.
> - **Option C is incorrect** because Pharming manipulates DNS entries.
> - **Option D is incorrect** because Spimming sends spam via Instant Messaging.

---

### 🧩 Question 12 | Scenario Challenge

> [!QUESTION] 📌 **Scenario Context**
> An attacker registers the domain `g00gle.com` (using zeros instead of 'o's) to set up a fake login portal for credential harvesting.
>
> What domain spoofing technique was used?

#### 🔘 Available Options:

- **A**: Typosquatting / Combosquatting
- **B**: DNS Poisoning
- **C**: IP Hijacking
- **D**: Subdomain Takeover

> [!SUCCESS]- 🔑 **Show Correct Answer & Exam Breakdown**
> **Correct Answer**: **Option A**
>
> #### 💡 Technical Deep Dive:
> Typosquatting relies on registering common misspellings or visually similar domain names to deceive users.
>
> #### 🚫 Distractor Analysis & Refutations:
>
> - **Option B is incorrect** because DNS Poisoning corrupts DNS cache entries.
> - **Option C is incorrect** because IP Hijacking takes over IP prefixes via BGP.
> - **Option D is incorrect** because Subdomain Takeover claims abandoned CNAME records.

---

### 🧩 Question 13 | Scenario Challenge

> [!QUESTION] 📌 **Scenario Context**
> What technique involves searching through corporate recycling bins and trash dumpsters to find discarded sensitive documents, receipts, or internal phone directories?

#### 🔘 Available Options:

- **A**: Dumpster Diving
- **B**: Shoulder Surfing
- **C**: Eavesdropping
- **D**: Pretexting

> [!SUCCESS]- 🔑 **Show Correct Answer & Exam Breakdown**
> **Correct Answer**: **Option A**
>
> #### 💡 Technical Deep Dive:
> Dumpster Diving is looking through corporate trash for sensitive intelligence.
>
> #### 🚫 Distractor Analysis & Refutations:
>
> - **Option B is incorrect** because Shoulder Surfing looks at user screens.
> - **Option C is incorrect** because Eavesdropping listens to conversations.
> - **Option D is incorrect** because Pretexting invents fabricated stories.

---

### 🧩 Question 14 | Scenario Challenge

> [!QUESTION] 📌 **Scenario Context**
> An attacker places a malware-infected USB flash drive labeled "Executive Salary Review Q4" on a table in the employee cafeteria, waiting for a curious employee to plug it into a corporate workstation.
>
> What social engineering attack vector is being executed?

#### 🔘 Available Options:

- **A**: Baiting
- **B**: Waterhole Attack
- **C**: Phishing
- **D**: Pretexting

> [!SUCCESS]- 🔑 **Show Correct Answer & Exam Breakdown**
> **Correct Answer**: **Option A**
>
> #### 💡 Technical Deep Dive:
> Baiting relies on leaving physical media (USB drives) infected with malware in public places to entice curious victims.
>
> #### 🚫 Distractor Analysis & Refutations:
>
> - **Option B is incorrect** because Waterhole attacks target websites.
> - **Option C is incorrect** because Phishing uses digital messaging.
> - **Option D is incorrect** because Pretexting uses verbal/written scenarios.

---

### 🧩 Question 15 | Scenario Challenge

> [!QUESTION] 📌 **Scenario Context**
> What cryptographic email security protocol attaches a digital signature to email headers that receiving servers verify using a public key published in the sender's DNS records?

#### 🔘 Available Options:

- **A**: DKIM (DomainKeys Identified Mail)
- **B**: SPF
- **C**: STARTTLS
- **D**: S/MIME

> [!SUCCESS]- 🔑 **Show Correct Answer & Exam Breakdown**
> **Correct Answer**: **Option A**
>
> #### 💡 Technical Deep Dive:
> DKIM adds a cryptographic digital signature to outbound emails to verify sender authenticity and header integrity.
>
> #### 🚫 Distractor Analysis & Refutations:
>
> - **Option B is incorrect** because SPF validates sending IP addresses.
> - **Option C is incorrect** because STARTTLS upgrades plaintext SMTP connections to TLS.
> - **Option D is incorrect** because S/MIME provides end-to-end email encryption between users.

---

### 🧩 Question 16 | Scenario Challenge

> [!QUESTION] 📌 **Scenario Context**
> What term describes voice phishing executed over telephone lines or VoIP services?

#### 🔘 Available Options:

- **A**: Vishing
- **B**: Smishing
- **C**: Phishing
- **D**: Pharming

> [!SUCCESS]- 🔑 **Show Correct Answer & Exam Breakdown**
> **Correct Answer**: **Option A**
>
> #### 💡 Technical Deep Dive:
> Vishing (Voice Phishing) uses phone calls or VoIP to trick targets into handing over sensitive information.
>
> #### 🚫 Distractor Analysis & Refutations:
>
> - **Option B is incorrect** because Smishing uses SMS.
> - **Option C is incorrect** because Phishing uses emails.
> - **Option D is incorrect** because Pharming redirects web traffic.

---

### 🧩 Question 17 | Scenario Challenge

> [!QUESTION] 📌 **Scenario Context**
> What is the primary operational defense against human-based social engineering attacks?

#### 🔘 Available Options:

- **A**: Continuous Security Awareness Training & Phishing Simulations
- **B**: Installing dual perimeter firewalls
- **C**: Deploying full disk encryption
- **D**: Updating antivirus signatures daily

> [!SUCCESS]- 🔑 **Show Correct Answer & Exam Breakdown**
> **Correct Answer**: **Option A**
>
> #### 💡 Technical Deep Dive:
> Continuous employee security awareness training and phishing simulations train staff to identify and report manipulation tactics.
>
> #### 🚫 Distractor Analysis & Refutations:
>
> - **Option B is incorrect** because firewalls do not block human compliance over phone calls.
> - **Option C is incorrect** because disk encryption protects lost laptops.
> - **Option D is incorrect** because antivirus does not block social engineering calls.

---

### 🧩 Question 18 | Scenario Challenge

> [!QUESTION] 📌 **Scenario Context**
> An attacker observes an employee typing their PIN code into an access control keypad from across the hallway using a telephoto lens.
>
> What attack vector was executed?

#### 🔘 Available Options:

- **A**: Shoulder Surfing
- **B**: Dumpster Diving
- **C**: Tailgating
- **D**: Eavesdropping

> [!SUCCESS]- 🔑 **Show Correct Answer & Exam Breakdown**
> **Correct Answer**: **Option A**
>
> #### 💡 Technical Deep Dive:
> Shoulder Surfing involves visually observing sensitive input (passwords, PINs, keystrokes) directly or from a distance.
>
> #### 🚫 Distractor Analysis & Refutations:
>
> - **Option B is incorrect** because Dumpster Diving searches trash.
> - **Option C is incorrect** because Tailgating follows someone through a door.
> - **Option D is incorrect** because Eavesdropping listens to audio conversations.

---

### 🧩 Question 19 | Scenario Challenge

> [!QUESTION] 📌 **Scenario Context**
> What specific form of spear-phishing targets high-profile corporate executives (e.g., CFO, CEO) to execute financial wire fraud?

#### 🔘 Available Options:

- **A**: Whaling
- **B**: Vishing
- **C**: Smishing
- **D**: Pharming

> [!SUCCESS]- 🔑 **Show Correct Answer & Exam Breakdown**
> **Correct Answer**: **Option A**
>
> #### 💡 Technical Deep Dive:
> Whaling specifically targets high-level "big fish" executives like CEOs and CFOs.
>
> #### 🚫 Distractor Analysis & Refutations:
>
> - **Option B is incorrect** because Vishing is voice phishing.
> - **Option C is incorrect** because Smishing is text phishing.
> - **Option D is incorrect** because Pharming redirects web traffic.

---

### 🧩 Question 20 | Scenario Challenge

> [!QUESTION] 📌 **Scenario Context**
> What attack redirects users from a legitimate web page to a fake phishing website by compromising the local host file or DNS server records without altering the URL in the browser?

#### 🔘 Available Options:

- **A**: Pharming
- **B**: Phishing
- **C**: Vishing
- **D**: Pretexting

> [!SUCCESS]- 🔑 **Show Correct Answer & Exam Breakdown**
> **Correct Answer**: **Option A**
>
> #### 💡 Technical Deep Dive:
> Pharming modifies DNS resolution (DNS cache poisoning or local `hosts` modification) to silently redirect users to fraudulent websites.
>
> #### 🚫 Distractor Analysis & Refutations:
>
> - **Option B is incorrect** because Phishing relies on getting users to click malicious links in messages.
> - **Option C is incorrect** because Vishing uses phone calls.
> - **Option D is incorrect** because Pretexting invents scenarios.

---

### 🧩 Question 21 | Scenario Challenge

> [!QUESTION] 📌 **Scenario Context**
> An attacker invents an elaborate fake story, pretending to be an external IT auditor performing a compliance check, to trick a helpdesk employee into resetting a user's password.
>
> What technique is being practiced?

#### 🔘 Available Options:

- **A**: Pretexting
- **B**: Shoulder Surfing
- **C**: Tailgating
- **D**: Baiting

> [!SUCCESS]- 🔑 **Show Correct Answer & Exam Breakdown**
> **Correct Answer**: **Option A**
>
> #### 💡 Technical Deep Dive:
> Pretexting involves creating a false context or story (pretext) to manipulate targets into handing over information or access.
>
> #### 🚫 Distractor Analysis & Refutations:
>
> - **Option B is incorrect** because Shoulder Surfing looks at screens.
> - **Option C is incorrect** because Tailgating follows people physically.
> - **Option D is incorrect** because Baiting uses infected media.

---

### 🧩 Question 22 | Scenario Challenge

> [!QUESTION] 📌 **Scenario Context**
> What type of insider threat occurs when an employee accidentally exposes sensitive cloud data due to a lack of proper security training?

#### 🔘 Available Options:

- **A**: Careless / Negligent Insider
- **B**: Malicious Insider
- **C**: Disgruntled Employee
- **D**: Saboteur

> [!SUCCESS]- 🔑 **Show Correct Answer & Exam Breakdown**
> **Correct Answer**: **Option A**
>
> #### 💡 Technical Deep Dive:
> Careless or Negligent Insiders expose data unintentionally through human error or poor security hygiene.
>
> #### 🚫 Distractor Analysis & Refutations:
>
> - **Option B is incorrect** because Malicious Insiders act with intentional malice.
> - **Option C is incorrect** because Disgruntled Employees seek revenge.
> - **Option D is incorrect** because Saboteurs intentionally damage systems.

---

### 🧩 Question 23 | Scenario Challenge

> [!QUESTION] 📌 **Scenario Context**
> What physical access control device prevents tailgating by allowing only one person to pass through a physical door at a time via revolving security doors or dual-door airlocks?

#### 🔘 Available Options:

- **A**: Mantrap
- **B**: Smart Card
- **C**: Biometric Reader
- **D**: CCTV Camera

> [!SUCCESS]- 🔑 **Show Correct Answer & Exam Breakdown**
> **Correct Answer**: **Option A**
>
> #### 💡 Technical Deep Dive:
> A Mantrap (airlock) consists of a small room with two interlocking doors where the second door cannot open until the first door closes, preventing tailgating.
>
> #### 🚫 Distractor Analysis & Refutations:
>
> - **Option B is incorrect** because Smart Cards authenticate individuals but do not prevent tailgating.
> - **Option C is incorrect** because Biometric Readers verify identity but do not stop tailgating physically.
> - **Option D is incorrect** because CCTV Cameras record security events passively.

---

### 🧩 Question 24 | Scenario Challenge

> [!QUESTION] 📌 **Scenario Context**
> Which psychological influence principle relies on creating a false sense of limited availability ("Only 2 seats left!") to force targets into fast action?

#### 🔘 Available Options:

- **A**: Scarcity
- **B**: Authority
- **C**: Social Proof
- **D**: Reciprocity

> [!SUCCESS]- 🔑 **Show Correct Answer & Exam Breakdown**
> **Correct Answer**: **Option A**
>
> #### 💡 Technical Deep Dive:
> Scarcity creates a perception of limited supply or time, encouraging victims to act quickly without verifying legitimacy.
>
> #### 🚫 Distractor Analysis & Refutations:
>
> - **Option B is incorrect** because Authority relies on rank.
> - **Option C is incorrect** because Social Proof relies on group behavior.
> - **Option D is incorrect** because Reciprocity relies on returning favors.

---

### 🧩 Question 25 | Scenario Challenge

> [!QUESTION] 📌 **Scenario Context**
> What open-source phishing simulation framework allows security teams to build end-to-end phishing campaigns and track click-through metrics?

#### 🔘 Available Options:

- **A**: GoPhish
- **B**: Wireshark
- **C**: Hashcat
- **D**: OpenVAS

> [!SUCCESS]- 🔑 **Show Correct Answer & Exam Breakdown**
> **Correct Answer**: **Option A**
>
> #### 💡 Technical Deep Dive:
> GoPhish is a widely used open-source phishing simulation framework for testing organizational security awareness.
>
> #### 🚫 Distractor Analysis & Refutations:
>
> - **Option B is incorrect** because Wireshark is a packet analyzer.
> - **Option C is incorrect** because Hashcat is a password cracker.
> - **Option D is incorrect** because OpenVAS is a vulnerability scanner.
