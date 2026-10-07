# 05. Course Detailed Notes — Denial-of-Service

> [!ABSTRACT] 🏛️ **Comprehensive Syllabus Notes & Technical Reference**
> Direct technical extraction from official CEH v13 Syllabus (Module 10). Covers Mirai Botnet Architecture, C2 Protocols, and SLA Traffic Scrubbing Metrics.

---

## 📌 1. Botnet Architecture & Mirai Malware Analysis

### 1.1 Mirai Botnet Mechanics
Mirai scans the IPv4 internet for IoT devices (security cameras, DVRs, routers) protected by factory-default telnet usernames and passwords (e.g., `root:admin`, `admin:12345`).

#### Mirai Attack Sequence:
1. **Scanning Phase**: Infected devices scan random IP addresses on TCP port 23/2323.
2. **Brute-Force Phase**: Attempts login using a hardcoded dictionary of 62 default credential pairs.
3. **Reporter & Loader**: Upon successful login, credentials are reported to a central loader server, which downloads the architecture-specific Mirai payload into device RAM.
4. **C2 Execution**: Infected IoT device connects to C2 server, awaiting attack commands (UDP flood, HTTP flood, ACK flood).

> [!INFO] 📋 **Comprehensive Botnet Command Architecture Matrix**

| Botnet Phase | Infrastructure Component | Communication Protocol | Operational Function |
| :---: | :--- | :--- | :--- |
| **Infection** | Scanner Module | Telnet (TCP 23) | Identifies weak default IoT credentials |
| **Payload Delivery**| Loader Server | HTTP / TFTP | Injects binary into target device RAM |
| **Command & Control**| C2 Master Server | IRC / HTTP / Custom Binary | Issues attack targets and flood methods |
