# 05. Course Detailed Notes — Scanning Networks

> [!ABSTRACT] 🏛️ **Comprehensive Syllabus Notes & Technical Reference**
> Direct technical extraction from official CEH v13 Syllabus (Module 03). Covers Port States, Service Enumeration Protocols, and Network Architecture Mapping.

---

## 📌 1. Nmap Port States & RFC Standards

### 1.1 Technical Classification of Nmap Port States
Nmap categorizes scanned ports into six distinct operational states based on the network responses received:

1. **Open**: An application daemon actively accepts TCP connections, UDP datagrams, or SCTP associations on the port.
2. **Closed**: A port is accessible (receives and responds to Nmap probe packets), but no application daemon is listening on it. Closed ports return a TCP `RST` or ICMP Port Unreachable packet.
3. **Filtered**: Nmap cannot determine whether the port is open because firewalls, network filters, or router ACLs block probe packets from reaching the port.
4. **Unfiltered**: The port is accessible, but Nmap cannot determine whether it is open or closed (returned by ACK scans).
5. **Open|Filtered**: Nmap cannot determine whether a port is open or filtered (common in UDP, Null, FIN, and Xmas scans when no response is returned).
6. **Closed|Filtered**: Nmap cannot determine whether a port is closed or filtered (returned by IP ID Idle scans).

> [!INFO] 📋 **Comprehensive Nmap Port State Reference Matrix**

| Port State | Operational Meaning | Typical Packet Response Received |
| :--- | :--- | :--- |
| **Open** | Application daemon is listening | `SYN/ACK` (TCP) or UDP response |
| **Closed** | No app listening, port accessible | `RST` (TCP) or ICMP Type 3 Code 3 (UDP) |
| **Filtered** | Firewall / ACL blocking probes | No response (dropped) or ICMP Type 3 Code 1/2/9/10/13 |
| **Unfiltered** | Accessible, state unknown | `RST` response from ACK scan (`-sA`) |
| **Open\|Filtered** | Open or Filtered (State ambiguous) | No response received for UDP/Xmas/FIN/Null scans |
| **Closed\|Filtered** | Closed or Filtered (State ambiguous) | Returned during Idle Scan (`-sI`) ambiguity |
