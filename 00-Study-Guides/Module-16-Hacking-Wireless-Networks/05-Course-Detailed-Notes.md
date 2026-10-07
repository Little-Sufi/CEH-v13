# 05. Course Detailed Notes — Hacking Wireless Networks

> [!ABSTRACT] 🏛️ **Comprehensive Syllabus Notes & Technical Reference**
> Direct technical extraction from official CEH v13 Syllabus (Module 16). Covers 802.11 Frame Architecture, 802.11w Management Frame Protection, and EAP Authentication Protocols.

---

## 📌 1. 802.11 Protocol Architecture & EAP Frameworks

### 1.1 802.11 Frame Classification
- **Management Frames**: Beacon, Probe Request/Response, Authentication, Deauthentication, Association.
- **Control Frames**: Request to Send (RTS), Clear to Send (CTS), Acknowledgment (ACK).
- **Data Frames**: Carries actual payload upper-layer IP data packets.

> [!INFO] 📋 **Comprehensive Extensible Authentication Protocol (EAP) Matrix**

| EAP Type | Outer Encryption Tunnel | Client Authentication Method | Security Rating |
| :--- | :--- | :--- | :--- |
| **EAP-TLS** | TLS Tunnel | X.509 Digital Certificates (Both Sides) | Maximum Security |
| **PEAP-MSCHAPv2** | TLS Tunnel | Username & Password Password Hash | Vulnerable to Rogue RADIUS |
| **EAP-TTLS** | TLS Tunnel | Flexible Inner Auth (PAP/CHAP/MSCHAP) | High Security |
