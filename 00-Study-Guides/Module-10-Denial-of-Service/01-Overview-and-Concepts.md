# 01. Overview and Concepts — Denial-of-Service

> [!INFO] 📌 **Module Scope & Core Objectives**
> Direct technical extraction from official CEH v13 Syllabus (Module 10). Covers Denial-of-Service (DoS) and Distributed Denial-of-Service (DDoS) attack categories (Volumetric, Protocol, Application Layer), TCP SYN Flooding mechanics, ICMP Smurf attacks, UDP Flooding, Slow-rate HTTP attacks (Slowloris, RUDY), Amplification Attack vectors (NTP, DNS, SSDP, Memcached), and Botnet Command-and-Control (C2) architectures.

---

## 🧠 1. DoS / DDoS Attack Taxonomies & Categories

### 1.1 The 3 Primary DDoS Attack Categories
Denial-of-Service attacks aim to compromise system availability by overwhelming target network bandwidth, OS protocol stack memory, or application processing threads.

#### 1. Volumetric Attacks
Saturates the target network's Internet transit bandwidth by flooding the link with massive volumes of data traffic.
- **Metric**: Measured in **Bits per Second (Gbps / Tbps)**.
- **Vectors**: UDP Floods, ICMP Floods, NTP/DNS Amplification.

#### 2. Protocol (State-Exhaustion) Attacks
Consumes state table resources present in network infrastructure hardware, such as stateful firewalls, load balancers, and operating system TCP socket connection queues.
- **Metric**: Measured in **Packets per Second (Mpps)**.
- **Vectors**: TCP SYN Flooding, Ping of Death, Smurf Attacks, Fragmented Packet Floods.

#### 3. Application Layer (Layer 7) Attacks
Targets web application logical execution components, database engines, or CPU-intensive operations (e.g., PDF generation, complex SQL searches) with seemingly legitimate HTTP requests.
- **Metric**: Measured in **Requests per Second (RPS)** or **Queries per Second (QPS)**.
- **Vectors**: HTTP GET Floods, HTTP POST Floods, Slowloris, RUDY (R-U-Dead-Yet).

> [!ABSTRACT] 🏛️ **📋 Comprehensive DDoS Attack Category Reference Matrix**

| DDoS Category | Target OSI Layer | Primary Measurement Metric | Dominant Attack Vectors | Hardware Component Impacted |
| :--- | :---: | :--- | :--- | :--- |
| **Volumetric** | Layer 3 / Layer 4 | Bits per Second (Gbps/Tbps) | UDP Flood, NTP/DNS Amplification | ISP Transit Link & Edge Routers |
| **Protocol** | Layer 3 / Layer 4 | Packets per Second (Mpps) | TCP SYN Flood, Smurf, Ping of Death| Firewalls, Load Balancers, OS Kernel |
| **Application Layer**| Layer 7 | Requests per Second (RPS) | HTTP GET/POST Flood, Slowloris, RUDY| Web Servers, App Pools, DB Engines |

---

## ⚡ 2. TCP & Amplification Vector Mechanics

### 2.1 TCP SYN Flooding Mechanics
In a TCP 3-way handshake (`SYN` -> `SYN-ACK` -> `ACK`), the server allocates a memory buffer in its TCP SYN queue upon receiving a `SYN` packet and waits for the final `ACK`.

#### SYN Flood Attack Flow:
1. **Attacker Transmission**: Attacker transmits thousands of TCP `SYN` packets per second with spoofed, non-existent source IP addresses.
2. **Server Memory Allocation**: Target server replies with `SYN-ACK` to the spoofed IPs and allocates memory in its SYN backlog queue.
3. **Queue Exhaustion**: Because the source IPs are spoofed, no final `ACK` is ever returned. The server's SYN queue fills completely, causing all subsequent legitimate incoming TCP connection requests to be dropped.

### 2.2 Amplification & Reflection Attacks
Amplification attacks exploit connectionless protocols (UDP) on open internet servers (NTP, DNS, Memcached) to reflect traffic back to a victim while multiplying packet payload volume.

- **Amplification Factor**: The ratio between the request payload size sent by the attacker and the response payload size reflected back to the victim.
- **NTP Amplification (`monlist`)**: Sending an 8-byte `monlist` command to an open NTP server returns a list of the last 600 clients (up to 486 bytes), yielding an **amplification factor of ~554x**.
- **Memcached Amplification**: Sending UDP requests to port 11211 yields an **amplification factor of up to 50,000x**.

> [!IMPORTANT] 🔄 **📋 Comprehensive Amplification Vector Reference Matrix**

| Protocol Vector | UDP Port | Amplification Command / Query | Typical Amplification Factor | Vulnerability Root Cause |
| :--- | :---: | :--- | :---: | :--- |
| **NTP** | UDP 123 | `monlist` request | ~554x | Enabled legacy diagnostic monitoring command |
| **DNS** | UDP 53 | `ANY` or `TXT` record query | 20x to 50x | Open recursive resolvers allowing unauthenticated UDP |
| **Memcached** | UDP 11211 | `get` request for cached keys | **10,000x – 50,000x** | Unauthenticated caching daemon bound to open internet |
| **SSDP** | UDP 1900 | `M-SEARCH` discovery request | 30x | Universal Plug and Play (UPnP) internet exposure |
