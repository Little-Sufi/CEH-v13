# 05. Course Detailed Notes — Sniffing

> [!ABSTRACT] 🏛️ **Comprehensive Syllabus Notes & Technical Reference**
> Direct technical extraction from official CEH v13 Syllabus (Module 08). Covers Promiscuous Mode Detection, Hardware Taps, and Hardware Sniffers.

---

## 📌 1. Promiscuous Mode Detection & Hardware Taps

### 1.1 Identifying Sniffers on the Network
Network administrators employ specific active probing techniques to detect NICs operating in promiscuous mode across the local subnet:

- **ICMP Request Latency Test**: Sending an ICMP echo request with a fake MAC address (`FF:FF:FF:FF:FF:FE`). Standard NICs ignore the packet, but promiscuous mode NICs pass it to the OS kernel, which responds with an ICMP Echo Reply.
- **Hardware Network Taps**: Physical devices installed directly in-line between a switch and a router to duplicate network traffic streams to an out-of-band monitoring appliance without introducing latency.

> [!INFO] 📋 **Comprehensive Promiscuous Mode Detection Reference Matrix**

| Detection Method | Operational Technique | Probe Signature | Expected Target Response |
| :--- | :--- | :--- | :--- |
| **ICMP Ping Test** | Sends unicast IP ping to fake MAC | `FF:FF:FF:FF:FF:FE` MAC | Promiscuous host replies with ICMP Echo |
| **DNS Request Test** | Sends broadcast DNS request | Nonsense broadcast MAC | Promiscuous host resolves IP request |
| **ARP Request Test** | Sends ARP request with fake MAC | Non-matching MAC address | Promiscuous host updates ARP cache |
