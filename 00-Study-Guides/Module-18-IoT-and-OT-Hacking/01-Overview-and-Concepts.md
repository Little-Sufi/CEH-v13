# 01. Overview and Concepts — IoT and OT Hacking

> [!INFO] 📌 **Module Scope & Core Objectives**
> Direct technical extraction from official CEH v13 Syllabus (Module 18). Covers Internet of Things (IoT) Architecture (Sensors, Gateways, Cloud), Operational Technology (OT) & ICS Architecture (Purdue Model, SCADA, PLCs, RTUs, DCS), IoT/OT Protocols (MQTT, CoAP, Zigbee, Z-Wave, Modbus, DNP3, BACnet), IoT/OT Vulnerability Taxonomies, and Hardware Interface Analysis (UART, JTAG, SPI, I2C).

---

## 🧠 1. IoT & OT Architectural Models

### 1.1 IoT Architecture & Component Layers
The Internet of Things (IoT) connects embedded physical devices to IP networks for data collection and control.
- **Edge / Sensing Layer**: Sensors, actuators, RFID tags, smart devices collecting physical telemetry.
- **Gateway / Network Layer**: Aggregates edge data using lightweight protocols (Zigbee, LoRaWAN, BLE, MQTT) and routes it over cellular/Ethernet to cloud servers.
- **Cloud / Application Layer**: Big data analytics, remote management dashboards, and API integrations.

### 1.2 Operational Technology (OT) & Purdue Model (ICS/SCADA)
Operational Technology (OT) monitors and controls physical industrial infrastructure (power grids, water treatment, manufacturing).

> [!ABSTRACT] 🏛️ **📋 Comprehensive Purdue Model for Industrial Control Systems (ICS)**

| Purdue Level | Functional Classification | Typical Hardware / Software Systems | Security Control Focus |
| :--- | :--- | :--- | :--- |
| **Level 4/5** | Enterprise Network | ERP systems, Business IT, Internet Gateway | Perimeter Firewalls, IT/OT DMZ |
| **Level 3** | Operations Management | Historian databases, SCADA Control Servers | OT Monitoring, Anomaly Detection |
| **Level 2** | Control Systems | Human-Machine Interfaces (HMIs), Engineering Workstations | Operator Authentication, Air-Gapping |
| **Level 1** | Direct Process Control | Programmable Logic Controllers (PLCs), RTUs, DCS | Modbus/DNP3 Integrity Monitoring |
| **Level 0** | Physical Process Layer | Actuators, Valves, Motors, Sensors | Physical Tamper Prevention |

---

## ⚡ 2. IoT & OT Communication Protocol Taxonomies

### 2.1 Protocol Classification
- **MQTT (Message Queuing Telemetry Transport)**: Lightweight publish/subscribe messaging protocol operating over TCP (port 1883/8883) utilizing a central **Broker**. Vulnerable to cleartext eavesdropping and unauthenticated topic subscription (`#`).
- **CoAP (Constrained Application Protocol)**: UDP-based (port 5683) web transfer protocol using RESTful GET/POST/PUT methods designed for constrained nodes.
- **Modbus (Modbus TCP)**: Legacy industrial protocol operating over TCP port 502. Completely lacks authentication, encryption, or integrity checks, allowing arbitrary coil/register overrides.
- **DNP3 (Distributed Network Protocol 3)**: Used in electric and water utilities; legacy versions lack authentication.

> [!IMPORTANT] 🔄 **📋 Comprehensive IoT & OT Protocol Security Comparison Matrix**

| Protocol | OSI Layer | Transport | Default Port | Native Authentication / Encryption | Primary Security Flaw |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **MQTT** | Application | TCP | 1883 / 8883 | Optional (TLS / Auth Credentials) | Unauthenticated topic wildcard (`#`) eavesdropping |
| **CoAP** | Application | UDP | 5683 / 5684 | Optional (DTLS) | UDP amplification DoS / No auth |
| **Modbus TCP**| Application | TCP | 502 | None | Cleartext command injection / Coil tampering |
| **DNP3** | Application | TCP/UDP | 20000 | None (Legacy) | Unauthenticated command execution |
| **Zigbee** | Network/App | 802.15.4 | 2.4 GHz | Symmetric Pre-Shared Key | Master key extraction via side-channel |
