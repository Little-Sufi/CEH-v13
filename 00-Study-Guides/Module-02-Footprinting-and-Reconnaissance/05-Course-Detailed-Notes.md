# 05. Course Detailed Notes — Footprinting & Reconnaissance

> [!INFO] 📌 **Comprehensive Syllabus Reference**
> Detailed technical notes extracted directly from official CEH v13 Module 02 PDF.

---

## 📖 1. Advanced Footprinting Terminology & Technical Mechanics

- **Footprinting**: The foundational phase of ethical hacking involving systematic collection of technical, organizational, and personnel data about a target network.
- **Open Source Intelligence (OSINT)**: Data collected legally and ethically from publicly available resources (government records, social networks, search engine indices, WHOIS registries).
- **Autonomous System Number (ASN)**: A unique identifier assigned by Regional Internet Registries (RIRs) to a collection of IP routing prefixes managed by a single network operator using Border Gateway Protocol (BGP).

---

## 📜 2. Regional Internet Registries (RIRs) & Global Allocation

### 2.1 RIR Governance & Database Queries
Global IP address allocation and Autonomous System Number (ASN) assignments are governed by five Regional Internet Registries (RIRs). Security auditors query RIR databases via WHOIS to identify target network ranges and CIDR blocks.

> [!ABSTRACT] 🏛️ **📋 Comprehensive Global RIR Geographic Allocation Reference Matrix**

| Regional Registry | Geographic Coverage Area | Primary Database & Query Utility |
| :--- | :--- | :--- |
| **ARIN** | North America (USA, Canada, parts of Caribbean) | WHOIS ARIN Query Tool |
| **RIPE NCC** | Europe, Middle East, Central Asia | RIPE Database Query |
| **APNIC** | Asia-Pacific region | APNIC WHOIS Database |
| **LACNIC** | Latin America and the Caribbean | LACNIC Registry Query |
| **AFRINIC** | African continent | AFRINIC Database |

---

## 🔍 3. Advanced Footprinting Mechanics & Attack Vectors

- **DNS Zone Transfer (`AXFR`)**: A replication protocol used between primary and secondary DNS servers. If left open, an attacker downloads the entire host map.
- **Email Header Tracking**: Parsing `Received:` headers in email message sources allows security analysts to trace originating SMTP server IP addresses, internal hostnames, and routing hops.
