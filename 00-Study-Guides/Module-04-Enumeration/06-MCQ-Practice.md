# 🎯 Module 04: Enumeration - Exam Scenario Practice Engine

> [!ABSTRACT] 📊 **Interactive Module Scorecard**
>
> - **Target Module**: Module 04: Enumeration
> - **Total Questions**: 25 Ultra-Detailed, 100% Unique Indirect Scenarios
> - **Exam Difficulty Standard**: Senior CEH v13 (Scenario-Driven Logic & Technical Deduction)
> - **Passing Threshold**: 85% Accuracy (22/25 Correct)
> 
> *Instructions: Evaluate the scenario context below. Select your choice, then expand the **Show Correct Answer & Exam Breakdown** callout to verify your answer and review the deep technical analysis and distractor refutations.*

---

### 🧩 Question 01 | Scenario Challenge

> [!QUESTION] 📌 **Scenario Context**
> An ethical hacker executes `nbtstat -A 192.168.1.50` against a Windows file server and observes a NetBIOS table entry containing `<20>` next to the registered machine name.
>
> What specific service is running on the target machine based on this NetBIOS suffix code?

#### 🔘 Available Options:

- **A**: Server Service (File and Print Sharing / SMB enabled)
- **B**: Domain Master Browser
- **C**: Messenger Service
- **D**: Workstation Service Name

> [!SUCCESS]- 🔑 **Show Correct Answer & Exam Breakdown**
> **Correct Answer**: **Option A**
>
> #### 💡 Technical Deep Dive:
> The NetBIOS `<20>` suffix code denotes the Server Service (File and Print Sharing), indicating that SMB file sharing is active on the target system.
>
> #### 🚫 Distractor Analysis & Refutations:
>
> - **Option B is incorrect** because `<1B>` represents the Domain Master Browser.
> - **Option C is incorrect** because `<03>` represents the Messenger Service.
> - **Option D is incorrect** because `<00>` represents the Workstation Service Name.

---

### 🧩 Question 02 | Scenario Challenge

> [!QUESTION] 📌 **Scenario Context**
> A penetration tester establishes an unauthenticated session to a legacy Windows domain controller using the command `net use \\10.0.0.5\IPC$ "" /user:""`.
>
> What specific technique is being demonstrated, and what vulnerability allows it?

#### 🔘 Available Options:

- **A**: SMB NULL Session Exploitation; allowed by unconfigured `RestrictAnonymous` registry settings
- **B**: Kerberos Golden Ticket Attack; allowed by compromised KRBTGT hashes
- **C**: LDAP Pass-the-Hash; allowed by unencrypted NTLM authentication
- **D**: SNMP Community String Brute-Forcing

> [!SUCCESS]- 🔑 **Show Correct Answer & Exam Breakdown**
> **Correct Answer**: **Option A**
>
> #### 💡 Technical Deep Dive:
> Connecting to `IPC$` with empty credentials establishes an SMB NULL Session. If `RestrictAnonymous` is set to 0, unauthenticated users can enumerate SIDs, domain accounts, and shares.
>
> #### 🚫 Distractor Analysis & Refutations:
>
> - **Option B is incorrect** because Golden Ticket attacks require forging Kerberos TGT tickets using the KRBTGT NTLM hash.
> - **Option C is incorrect** because Pass-the-Hash uses NTLM hashes to authenticate as an administrative user.
> - **Option D is incorrect** because SNMP uses UDP ports 161/162, not SMB IPC$ shares.

---

### 🧩 Question 03 | Scenario Challenge

> [!QUESTION] 📌 **Scenario Context**
> An auditor queries an SNMP agent using `snmpwalk -v2c -c public 192.168.1.1 1.3.6.1.4.1.77.1.2.25`.
>
> What specific enterprise intelligence is extracted by querying this MIB OID path?

#### 🔘 Available Options:

- **A**: List of local Windows user account names
- **B**: Installed operating system version description (`sysDescr`)
- **C**: Active network interface ARP routing table
- **D**: List of running process executable names

> [!SUCCESS]- 🔑 **Show Correct Answer & Exam Breakdown**
> **Correct Answer**: **Option A**
>
> #### 💡 Technical Deep Dive:
> The OID `1.3.6.1.4.1.77.1.2.25` in the LANManager MIB tree specifically enumerates local Windows user accounts.
>
> #### 🚫 Distractor Analysis & Refutations:
>
> - **Option B is incorrect** because `sysDescr` is located at `1.3.6.1.2.1.1.1`.
> - **Option C is incorrect** because IP routing tables use `1.3.6.1.2.1.4.21`.
> - **Option D is incorrect** because running software process lists use `1.3.6.1.2.1.25.4.2.1.2`.

---

### 🧩 Question 04 | Scenario Challenge

> [!QUESTION] 📌 **Scenario Context**
> During an internal security assessment, a tester runs `rpcclient -U "" 10.0.0.15` and issues the command `queryuser 0x1f4`.
>
> Which user account is being queried based on the hex Relative Identifier (RID) `0x1f4`?

#### 🔘 Available Options:

- **A**: Built-in Administrator Account (RID 500)
- **B**: Built-in Guest Account (RID 501)
- **C**: KRBTGT Account (RID 502)
- **D**: Domain Admins Group (RID 512)

> [!SUCCESS]- 🔑 **Show Correct Answer & Exam Breakdown**
> **Correct Answer**: **Option A**
>
> #### 💡 Technical Deep Dive:
> Converting hex `0x1f4` to decimal yields `500`. RID `500` is universally assigned to the built-in Administrator account on Windows systems.
>
> #### 🚫 Distractor Analysis & Refutations:
>
> - **Option B is incorrect** because RID 501 (hex `0x1f5`) is the Guest account.
> - **Option C is incorrect** because RID 502 (hex `0x1f6`) is the KRBTGT account.
> - **Option D is incorrect** because RID 512 (hex `0x200`) is the Domain Admins group.

---

### 🧩 Question 05 | Scenario Challenge

> [!QUESTION] 📌 **Scenario Context**
> A penetration tester connects to an internal mail server via Telnet on port 25 and issues `VRFY jsmith`. The mail server responds with `250 2.1.5 John Smith <jsmith@corp.com>`.
>
> What information does the `VRFY` SMTP command disclose?

#### 🔘 Available Options:

- **A**: Verifies that a specific user mailbox exists on the mail server
- **B**: Expands a mailing list to reveal all members
- **C**: Transmits an encrypted email message payload
- **D**: Authenticates an SMTP admin session using NTLM

> [!SUCCESS]- 🔑 **Show Correct Answer & Exam Breakdown**
> **Correct Answer**: **Option A**
>
> #### 💡 Technical Deep Dive:
> The SMTP `VRFY` command requests the mail server to verify whether a specific username or mailbox address exists.
>
> #### 🚫 Distractor Analysis & Refutations:
>
> - **Option B is incorrect** because the `EXPN` command expands mailing lists.
> - **Option C is incorrect** because `DATA` transmits email message content.
> - **Option D is incorrect** because `AUTH LOGIN` authenticates sessions.

---

### 🧩 Question 06 | Scenario Challenge

> [!QUESTION] 📌 **Scenario Context**
> What default community string is used for unauthenticated, read-only access to SNMP v1 and v2c agents?

#### 🔘 Available Options:

- **A**: `public`
- **B**: `private`
- **C**: `admin`
- **D**: `secret`

> [!SUCCESS]- 🔑 **Show Correct Answer & Exam Breakdown**
> **Correct Answer**: **Option A**
>
> #### 💡 Technical Deep Dive:
> `public` is the universal default read-only community string for SNMP v1/v2c. `private` is the default read-write string.
>
> #### 🚫 Distractor Analysis & Refutations:
>
> - **Option B is incorrect** because `private` provides read-write access.
> - **Option C is incorrect** because `admin` is not an SNMP default string.
> - **Option D is incorrect** because `secret` is an arbitrary string.

---

### 🧩 Question 07 | Scenario Challenge

> [!QUESTION] 📌 **Scenario Context**
> Which Windows registry setting should be configured to `2` to completely disable SMB NULL session enumeration?

#### 🔘 Available Options:

- **A**: `RestrictAnonymous`
- **B**: `EnableLua`
- **C**: `NtfsDisable8dot3NameCreation`
- **D**: `AutoShareWks`

> [!SUCCESS]- 🔑 **Show Correct Answer & Exam Breakdown**
> **Correct Answer**: **Option A**
>
> #### 💡 Technical Deep Dive:
> Setting `HKLM\System\CurrentControlSet\Control\Lsa\RestrictAnonymous` to `2` completely restricts anonymous users from accessing IPC$ shares and enumerating accounts.
>
> #### 🚫 Distractor Analysis & Refutations:
>
> - **Option B is incorrect** because `EnableLua` controls User Account Control (UAC).
> - **Option C is incorrect** because `NtfsDisable8dot3NameCreation` controls short file names.
> - **Option D is incorrect** because `AutoShareWks` manages administrative hidden shares.

---

### 🧩 Question 08 | Scenario Challenge

> [!QUESTION] 📌 **Scenario Context**
> Which open-source Linux utility wraps `rpcclient`, `net`, and `nmblookup` to perform comprehensive automated SMB enumeration against Windows hosts?

#### 🔘 Available Options:

- **A**: `enum4linux`
- **B**: `theHarvester`
- **C**: `Nmap`
- **D**: `Nikto`

> [!SUCCESS]- 🔑 **Show Correct Answer & Exam Breakdown**
> **Correct Answer**: **Option A**
>
> #### 💡 Technical Deep Dive:
> `enum4linux` is a dedicated tool written in Perl that automates SMB enumeration against Windows and Samba hosts.
>
> #### 🚫 Distractor Analysis & Refutations:
>
> - **Option B is incorrect** because `theHarvester` is an OSINT email harvester.
> - **Option C is incorrect** because Nmap is a general network port scanner.
> - **Option D is incorrect** because Nikto is a web server vulnerability scanner.

---

### 🧩 Question 09 | Scenario Challenge

> [!QUESTION] 📌 **Scenario Context**
> What secure protocol version of SNMP encrypts community strings and payload traffic using AES and enforces SHA authentication?

#### 🔘 Available Options:

- **A**: SNMP v3
- **B**: SNMP v2c
- **C**: SNMP v1
- **D**: SNMP SEC

> [!SUCCESS]- 🔑 **Show Correct Answer & Exam Breakdown**
> **Correct Answer**: **Option A**
>
> #### 💡 Technical Deep Dive:
> SNMP v3 introduces the User-based Security Model (USM), providing cryptographic authentication (HMAC-SHA) and privacy encryption (AES).
>
> #### 🚫 Distractor Analysis & Refutations:
>
> - **Option B is incorrect** because SNMP v2c transmits community strings in cleartext.
> - **Option C is incorrect** because SNMP v1 lacks encryption.
> - **Option D is incorrect** because SNMP SEC is not a recognized protocol standard.

---

### 🧩 Question 10 | Scenario Challenge

> [!QUESTION] 📌 **Scenario Context**
> Which GUI tool included with Windows Server allows administrators and auditors to connect, search, and browse LDAP directory trees in Active Directory?

#### 🔘 Available Options:

- **A**: `ldp.exe`
- **B**: `regedit.exe`
- **C**: `eventvwr.msc`
- **D**: `compmgmt.msc`

> [!SUCCESS]- 🔑 **Show Correct Answer & Exam Breakdown**
> **Correct Answer**: **Option A**
>
> #### 💡 Technical Deep Dive:
> `ldp.exe` is the native Windows graphical LDAP client used to perform search, bind, and modification operations against Active Directory.
>
> #### 🚫 Distractor Analysis & Refutations:
>
> - **Option B is incorrect** because `regedit.exe` edits the Windows Registry.
> - **Option C is incorrect** because `eventvwr.msc` views Event Logs.
> - **Option D is incorrect** because `compmgmt.msc` opens Computer Management.

---

### 🧩 Question 11 | Scenario Challenge

> [!QUESTION] 📌 **Scenario Context**
> An attacker uses `ldapsearch -x -h 10.0.0.5 -b "dc=corp,dc=com"` to extract Active Directory objects. What parameter does `-x` specify?

#### 🔘 Available Options:

- **A**: Simple authentication (bind without SASL)
- **B**: XML output format
- **C**: Encrypted SSL connection
- **D**: Extended schema dump

> [!SUCCESS]- 🔑 **Show Correct Answer & Exam Breakdown**
> **Correct Answer**: **Option A**
>
> #### 💡 Technical Deep Dive:
> In `ldapsearch`, the `-x` flag specifies simple authentication instead of SASL authentication.
>
> #### 🚫 Distractor Analysis & Refutations:
>
> - **Option B is incorrect** because `-x` does not control XML formatting.
> - **Option C is incorrect** because `-H ldaps://` specifies SSL/TLS.
> - **Option D is incorrect** because `-b` specifies the search base.

---

### 🧩 Question 12 | Scenario Challenge

> [!QUESTION] 📌 **Scenario Context**
> Which Active Directory tool uses graph theory to visually map privilege escalation paths, domain admin relationships, and misconfigured ACLs?

#### 🔘 Available Options:

- **A**: BloodHound
- **B**: Wireshark
- **C**: Cain & Abel
- **D**: John the Ripper

> [!SUCCESS]- 🔑 **Show Correct Answer & Exam Breakdown**
> **Correct Answer**: **Option A**
>
> #### 💡 Technical Deep Dive:
> BloodHound uses graph theory to reveal hidden relationships and attack paths within an Active Directory environment.
>
> #### 🚫 Distractor Analysis & Refutations:
>
> - **Option B is incorrect** because Wireshark analyzes network traffic.
> - **Option C is incorrect** because Cain & Abel is a legacy password recovery tool.
> - **Option D is incorrect** because John the Ripper is an offline password cracker.

---

### 🧩 Question 13 | Scenario Challenge

> [!QUESTION] 📌 **Scenario Context**
> What standard port is used for secure encrypted LDAP (LDAPS)?

#### 🔘 Available Options:

- **A**: TCP 636
- **B**: TCP 389
- **C**: TCP 445
- **D**: UDP 161

> [!SUCCESS]- 🔑 **Show Correct Answer & Exam Breakdown**
> **Correct Answer**: **Option A**
>
> #### 💡 Technical Deep Dive:
> LDAPS (LDAP over SSL/TLS) operates over TCP port 636. Unencrypted LDAP operates over TCP port 389.
>
> #### 🚫 Distractor Analysis & Refutations:
>
> - **Option B is incorrect** because TCP 389 is cleartext LDAP.
> - **Option C is incorrect** because TCP 445 is SMB.
> - **Option D is incorrect** because UDP 161 is SNMP.

---

### 🧩 Question 14 | Scenario Challenge

> [!QUESTION] 📌 **Scenario Context**
> An auditor executes `ntpq -p 192.168.1.1`. What network service is being queried?

#### 🔘 Available Options:

- **A**: Network Time Protocol (NTP)
- **B**: Network File System (NFS)
- **C**: NetBIOS Name Service
- **D**: Name Server Query

> [!SUCCESS]- 🔑 **Show Correct Answer & Exam Breakdown**
> **Correct Answer**: **Option A**
>
> #### 💡 Technical Deep Dive:
> `ntpq` is an NTP query utility used to monitor NTP daemon operation and enumerate connected time server peers.
>
> #### 🚫 Distractor Analysis & Refutations:
>
> - **Option B is incorrect** because NFS uses RPC/portmap.
> - **Option C is incorrect** because NetBIOS uses `nbtstat`.
> - **Option D is incorrect** because DNS uses `dig` or `nslookup`.

---

### 🧩 Question 15 | Scenario Challenge

> [!QUESTION] 📌 **Scenario Context**
> Which Relative Identifier (RID) is assigned by default to the Kerberos Ticket Granting Ticket (KRBTGT) account in Windows Active Directory?

#### 🔘 Available Options:

- **A**: 502
- **B**: 500
- **C**: 501
- **D**: 512

> [!SUCCESS]- 🔑 **Show Correct Answer & Exam Breakdown**
> **Correct Answer**: **Option A**
>
> #### 💡 Technical Deep Dive:
> RID 502 is reserved for the KRBTGT service account in Windows Active Directory domains.
>
> #### 🚫 Distractor Analysis & Refutations:
>
> - **Option B is incorrect** because RID 500 is Administrator.
> - **Option C is incorrect** because RID 501 is Guest.
> - **Option D is incorrect** because RID 512 is Domain Admins.

---

### 🧩 Question 16 | Scenario Challenge

> [!QUESTION] 📌 **Scenario Context**
> What command-line tool allows an attacker to connect to SMB shares without providing a password if anonymous access is permitted?

#### 🔘 Available Options:

- **A**: `smbclient -L //192.168.1.10 -N`
- **B**: `nmap -sS 192.168.1.10`
- **C**: `hping3 -S 192.168.1.10`
- **D**: `dig AXFR 192.168.1.10`

> [!SUCCESS]- 🔑 **Show Correct Answer & Exam Breakdown**
> **Correct Answer**: **Option A**
>
> #### 💡 Technical Deep Dive:
> `smbclient -N` instructs smbclient to suppress password prompts and attempt a null connection.
>
> #### 🚫 Distractor Analysis & Refutations:
>
> - **Option B is incorrect** because Nmap performs port scanning.
> - **Option C is incorrect** because Hping3 creates custom TCP packets.
> - **Option D is incorrect** because Dig performs DNS queries.

---

### 🧩 Question 17 | Scenario Challenge

> [!QUESTION] 📌 **Scenario Context**
> What NetBIOS suffix code indicates that a host acts as a Windows Domain Controller (`<1C>`)?

#### 🔘 Available Options:

- **A**: `<1C>`
- **B**: `<20>`
- **C**: `<00>`
- **D**: `<1B>`

> [!SUCCESS]- 🔑 **Show Correct Answer & Exam Breakdown**
> **Correct Answer**: **Option A**
>
> #### 💡 Technical Deep Dive:
> Suffix code `<1C>` registers a Domain Controller group name under NetBIOS.
>
> #### 🚫 Distractor Analysis & Refutations:
>
> - **Option B is incorrect** because `<20>` is Server Service (SMB).
> - **Option C is incorrect** because `<00>` is Workstation Name.
> - **Option D is incorrect** because `<1B>` is Domain Master Browser.

---

### 🧩 Question 18 | Scenario Challenge

> [!QUESTION] 📌 **Scenario Context**
> What SMTP command is used to expand mailing lists and reveal all subscribed recipient email addresses?

#### 🔘 Available Options:

- **A**: `EXPN`
- **B**: `VRFY`
- **C**: `HELO`
- **D**: `MAIL FROM`

> [!SUCCESS]- 🔑 **Show Correct Answer & Exam Breakdown**
> **Correct Answer**: **Option A**
>
> #### 💡 Technical Deep Dive:
> The SMTP `EXPN` command expands a mailing list alias to display individual member email addresses.
>
> #### 🚫 Distractor Analysis & Refutations:
>
> - **Option B is incorrect** because `VRFY` verifies single usernames.
> - **Option C is incorrect** because `HELO` initiates the SMTP conversation.
> - **Option D is incorrect** because `MAIL FROM` specifies the sender address.

---

### 🧩 Question 19 | Scenario Challenge

> [!QUESTION] 📌 **Scenario Context**
> An auditor wants to scan a network range specifically to discover open SNMP agents listening on UDP port 161 using community string `public`. Which utility is specifically designed for high-speed SNMP community string scanning?

#### 🔘 Available Options:

- **A**: `onesixtyone`
- **B**: `wireshark`
- **C**: `john`
- **D**: `hydra`

> [!SUCCESS]- 🔑 **Show Correct Answer & Exam Breakdown**
> **Correct Answer**: **Option A**
>
> #### 💡 Technical Deep Dive:
> `onesixtyone` is an efficient SNMP scanner that sends parallel queries for community strings across IP ranges.
>
> #### 🚫 Distractor Analysis & Refutations:
>
> - **Option B is incorrect** because Wireshark is a packet analyzer.
> - **Option C is incorrect** because John is a password cracker.
> - **Option D is incorrect** because Hydra is a multi-protocol online password brute-forcer.

---

### 🧩 Question 20 | Scenario Challenge

> [!QUESTION] 📌 **Scenario Context**
> Which Windows user account RID represents the default local Guest account?

#### 🔘 Available Options:

- **A**: 501
- **B**: 500
- **C**: 502
- **D**: 513

> [!SUCCESS]- 🔑 **Show Correct Answer & Exam Breakdown**
> **Correct Answer**: **Option A**
>
> #### 💡 Technical Deep Dive:
> RID 501 is assigned to the built-in Guest account on Windows systems.
>
> #### 🚫 Distractor Analysis & Refutations:
>
> - **Option B is incorrect** because RID 500 is Administrator.
> - **Option C is incorrect** because RID 502 is KRBTGT.
> - **Option D is incorrect** because RID 513 is Domain Users.

---

### 🧩 Question 21 | Scenario Challenge

> [!QUESTION] 📌 **Scenario Context**
> What port is used by default for Microsoft SMB over TCP without NetBIOS transport wrapper?

#### 🔘 Available Options:

- **A**: TCP 445
- **B**: TCP 139
- **C**: UDP 137
- **D**: TCP 389

> [!SUCCESS]- 🔑 **Show Correct Answer & Exam Breakdown**
> **Correct Answer**: **Option A**
>
> #### 💡 Technical Deep Dive:
> Direct SMB over TCP operates over port 445. Legacy SMB over NetBIOS operates over TCP port 139.
>
> #### 🚫 Distractor Analysis & Refutations:
>
> - **Option B is incorrect** because TCP 139 is NetBIOS Session Service.
> - **Option C is incorrect** because UDP 137 is NetBIOS Name Service.
> - **Option D is incorrect** because TCP 389 is LDAP.

---

### 🧩 Question 22 | Scenario Challenge

> [!QUESTION] 📌 **Scenario Context**
> What administrative tool allows an attacker to issue `enumdomusers` to extract user account names via RPC calls?

#### 🔘 Available Options:

- **A**: `rpcclient`
- **B**: `ping`
- **C**: `traceroute`
- **D**: `nslookup`

> [!SUCCESS]- 🔑 **Show Correct Answer & Exam Breakdown**
> **Correct Answer**: **Option A**
>
> #### 💡 Technical Deep Dive:
> `rpcclient` executes MS-RPC functions like `enumdomusers` to dump domain user lists.
>
> #### 🚫 Distractor Analysis & Refutations:
>
> - **Option B is incorrect** because `ping` tests network connectivity.
> - **Option C is incorrect** because `traceroute` traces network hops.
> - **Option D is incorrect** because `nslookup` performs DNS queries.

---

### 🧩 Question 23 | Scenario Challenge

> [!QUESTION] 📌 **Scenario Context**
> An organization wants to prevent attackers from using LDAP queries to read Active Directory user lists over unencrypted channels. What defensive policy should be enforced?

#### 🔘 Available Options:

- **A**: Require LDAP Signing and Channel Binding (LDAPS / Port 636)
- **B**: Disable DNSSEC
- **C**: Allow SMB NULL sessions
- **D**: Enable NetBIOS over TCP/IP

> [!SUCCESS]- 🔑 **Show Correct Answer & Exam Breakdown**
> **Correct Answer**: **Option A**
>
> #### 💡 Technical Deep Dive:
> Enforcing LDAP signing and channel binding (LDAPS over TLS port 636) prevents cleartext LDAP enumeration and Man-in-the-Middle credential interception.
>
> #### 🚫 Distractor Analysis & Refutations:
>
> - **Option B is incorrect** because disabling DNSSEC weakens DNS security.
> - **Option C is incorrect** because allowing SMB NULL sessions exposes user accounts.
> - **Option D is incorrect** because NetBIOS enables legacy enumeration vectors.

---

### 🧩 Question 24 | Scenario Challenge

> [!QUESTION] 📌 **Scenario Context**
> What MIB OID path is queried to retrieve the host system description (`sysDescr`) via SNMP?

#### 🔘 Available Options:

- **A**: `1.3.6.1.2.1.1.1`
- **B**: `1.3.6.1.4.1.77`
- **C**: `1.3.6.1.2.1.25`
- **D**: `1.3.6.1.2.1.6`

> [!SUCCESS]- 🔑 **Show Correct Answer & Exam Breakdown**
> **Correct Answer**: **Option A**
>
> #### 💡 Technical Deep Dive:
> The OID `1.3.6.1.2.1.1.1` points to `sysDescr` in the MIB-II tree.
>
> #### 🚫 Distractor Analysis & Refutations:
>
> - **Option B is incorrect** because `1.3.6.1.4.1.77` is the LANManager tree.
> - **Option C is incorrect** because `1.3.6.1.2.1.25` is the Host Resources MIB.
> - **Option D is incorrect** because `1.3.6.1.2.1.6` is the TCP MIB.

---

### 🧩 Question 25 | Scenario Challenge

> [!QUESTION] 📌 **Scenario Context**
> An attacker connects to port 25 of a mail gateway and issues `RCPT TO: admin@corp.com`. The server responds with `250 2.1.5 Recipient OK`.
>
> What technique has the attacker demonstrated?

#### 🔘 Available Options:

- **A**: SMTP Mailbox Enumeration via RCPT TO probing
- **B**: SQL Injection payload delivery
- **C**: DNS Zone Transfer
- **D**: Kerberos Pre-authentication Bypass

> [!SUCCESS]- 🔑 **Show Correct Answer & Exam Breakdown**
> **Correct Answer**: **Option A**
>
> #### 💡 Technical Deep Dive:
> Probing `RCPT TO` addresses during an SMTP transaction determines whether recipient email accounts are valid based on server response codes (`250 OK` vs `550 User unknown`).
>
> #### 🚫 Distractor Analysis & Refutations:
>
> - **Option B is incorrect** because SQL injection targets database query parameters.
> - **Option C is incorrect** because DNS Zone Transfers query DNS AXFR records.
> - **Option D is incorrect** because Kerberos Pre-auth attacks target AS-REP requests on port 88.
