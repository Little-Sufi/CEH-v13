# 04. Countermeasures — Denial-of-Service

> [!SHIELD] 🏰 **Defensive Security Controls & DDoS Mitigation Standards**
> Direct technical extraction from official CEH v13 Syllabus (Module 10). Covers SYN Cookies, Rate Limiting, Unicast Reverse Path Forwarding (uRPF), Cloud WAF & Scrubbing Centers, and Router ACLs.

---

## 🛡️ 1. Defensive Hardening & Mitigations

### 1.1 Technical Defenses Against DoS / DDoS

#### 1. SYN Cookies
Configuring SYN Cookies (`net.ipv4.tcp_syncookies = 1`) allows Linux servers to encode TCP connection parameters directly into the initial sequence number of the `SYN-ACK` packet without allocating server memory buffers until the final `ACK` is received.

#### 2. Unicast Reverse Path Forwarding (uRPF)
Configured on edge routers to prevent IP address spoofing. uRPF checks every incoming packet's source IP against the router's Routing Information Base (RIB). If the packet arrives on an interface different from the route back to the source IP, the router drops the packet.

#### 3. Cloud WAF & Scrubbing Centers (Cloudflare, Akamai)
Redirects domain DNS traffic through cloud BGP Anycast scrubbing centers. Incoming volumetric traffic is scrubbed using behavioral heuristics, dropping malicious botnet traffic while forwarding clean traffic to origin servers.

> [!SHIELD] 🏰 **📋 Comprehensive DDoS Mitigation Technology Reference Matrix**

| Defensive Technology | Implementation Layer | Attack Vector Mitigated | Technical Mechanism |
| :--- | :--- | :--- | :--- |
| **SYN Cookies** | OS Kernel (Layer 4) | TCP SYN Flooding | Delays TCP memory allocation until ACK |
| **uRPF** | Edge Routers (Layer 3) | Spoofed IP Amplification / Floods | Verifies valid reverse path routing interface |
| **Rate Limiting** | Firewall / Load Balancer| HTTP GET/POST Floods | Limits maximum requests per IP per second |
| **Cloud Scrubbing Center**| Edge BGP Anycast | Multi-Gigabit Volumetric DDoS | Scrubs botnet traffic before reaching origin |
