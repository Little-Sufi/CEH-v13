# 01. Overview and Concepts — Social Engineering

> [!INFO] 📌 **Module Scope & Core Objectives**
> Direct technical extraction from official CEH v13 Syllabus (Module 09). Covers Psychological Triggers of Social Engineering (Authority, Urgency, Scarcity, Social Proof, Liking), Human-Based vs Computer-Based Attacks, Insider Threat Classifications, Identity Theft Mechanics, and Defensive Authentication Protocols (SPF, DKIM, DMARC, FIDO2).

---

## 🧠 1. Psychological Triggers of Social Engineering

### 1.1 Detailed Analysis of Influence Tactics
Social Engineering is the art of exploiting human psychology, trust, and cognitive biases to manipulate individuals into disclosing confidential information, granting unauthorized physical/logical access, or executing actions that compromise organizational security.

#### 6 Core Psychological Triggers:
1. **Authority**: Posing as an executive, law enforcement officer, or IT administrator. Victims naturally comply with orders from perceived authority figures.
2. **Urgency / Intimidation**: Creating artificial time constraints ("Your account will be suspended in 15 minutes!") or threatening legal consequences to induce panic and bypass critical thinking.
3. **Consensus / Social Proof**: Tricking victims into believing that peers or colleagues have already performed the requested action ("Everyone in your department has already verified their password").
4. **Scarcity**: Creating a false sense of limited availability ("Only 3 gift cards remaining!") to motivate immediate compliance.
5. **Liking / Trust**: Establishing rapport through charm, shared interests, or flattery to make the victim willing to grant favors.
6. **Reciprocity**: Offering a small favor or gift first, inducing a psychological obligation in the victim to return the favor.

> [!ABSTRACT] 🏛️ **📋 Psychological Influence Principle Reference Matrix**

| Influence Trigger | Psychological Mechanism | Classic Social Engineering Scenario | Defensive Countermeasure |
| :--- | :--- | :--- | :--- |
| **Authority** | Compliance with hierarchy & status | Fake C-suite executive demanding urgent wire transfer | Strict dual-authorization procedures |
| **Urgency** | Panic-induced decision making | Phishing email warning of immediate account deletion | Out-of-band identity verification |
| **Social Proof** | Conforming to group behavior | Fake IT notice claiming "all staff must update credentials"| Mandatory security awareness training |
| **Reciprocity** | Obligation to return a favor | Attacker gives free USB drive, asks for building tour | Clean desk & badge policy enforcement |

---

## ⚡ 2. Social Engineering Attack Vector Taxonomies

### 2.1 Human-Based vs. Computer-Based Attack Vectors

#### 1. Human-Based Social Engineering
- **Pretexting**: Inventing a fabricated scenario (pretext) to trick a target into releasing information or performing an action (e.g., impersonating an external auditor).
- **Tailgating**: Following an authorized employee through a secure physical door without presenting a valid access badge.
- **Piggybacking**: Asking an authorized employee to hold the secure door open ("I forgot my badge, can you hold the door?").
- **Shoulder Surfing**: Secretly observing a victim's screen or keypad to capture passwords or PINs.
- **Dumpster Diving**: Searching through corporate trash bins for sensitive documents, invoices, or network diagrams.

#### 2. Computer-Based Social Engineering
- **Phishing**: Mass email campaigns using spoofed domain headers to trick users into clicking malicious links.
- **Spear Phishing**: Highly customized, targeted phishing emails directed at a specific individual or organization based on OSINT research.
- **Whaling**: Spear phishing targeted specifically at high-profile C-suite executives (CEO, CFO).
- **Pharming**: Redirecting web traffic from legitimate websites to fraudulent phishing sites by compromising DNS servers or local `hosts` files.
- **Watering Hole Attack**: Compromising a legitimate website frequently visited by target employees to infect visitors with zero-day exploits.

> [!IMPORTANT] 🔄 **📋 Comprehensive Social Engineering Attack Vector Reference Matrix**

| Attack Category | Specific Attack Vector | Vector Operational Mechanism | Primary Target / Impact |
| :--- | :--- | :--- | :--- |
| **Human-Based** | Tailgating / Piggybacking | Physical entry behind authorized employee | Unauthorized physical facility breach |
| **Human-Based** | Pretexting | Fabricated identity scenario over phone/in-person | Confidential data disclosure |
| **Computer-Based**| Spear Phishing | Custom targeted email based on OSINT | Initial network access / Trojan drop |
| **Computer-Based**| Whaling | High-level executive wire transfer extortion | Massive financial wire fraud |
| **Computer-Based**| Watering Hole | Compromises trusted industry news/blog site | Corporate endpoint infection |
| **Mobile / Voice**| Vishing / Smishing | Voice phishing (VoIP) or SMS text phishing | Credential & 2FA token theft |
