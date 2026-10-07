# 02. Attack Techniques — Sniffing

> [!WARNING] ⚡ **Man-in-the-Middle (MitM) & Protocol Exploitation Methods**
> Direct extraction from official CEH v13 Syllabus (Module 08). Covers ARP Poisoning Execution, Gratuitous ARP Injections, DHCP Rogue Server Deployment, DNS Spoofing, and Port Stealing.

---

## ⚔️ 1. ARP Poisoning & Man-in-the-Middle (MitM) Mechanics

### 1.1 Gratuitous ARP Exploitation
Address Resolution Protocol (ARP) resolves 32-bit IP addresses to 48-bit MAC addresses. ARP is stateless and lacks authentication; hosts accept and update their local ARP cache upon receiving unrequested (Gratuitous) ARP responses.

#### ARP Poisoning Execution Walkthrough:
1. **Victim Target**: Target Host `192.168.1.50` (`MAC_A`) and Default Gateway `192.168.1.1` (`MAC_GW`).
2. **Attacker Machine**: `192.168.1.100` (`MAC_ATTACKER`).
3. **Poisoning Step 1**: Attacker transmits forged ARP response to Victim: *"192.168.1.1 is at MAC_ATTACKER"*.
4. **Poisoning Step 2**: Attacker transmits forged ARP response to Gateway: *"192.168.1.50 is at MAC_ATTACKER"*.
5. **MitM Interception**: All traffic between Victim and Gateway flows through Attacker machine, enabling full packet inspection and credential harvest.

```bash
# Enable IP Forwarding on Linux
echo 1 > /proc/sys/net/ipv4/ip_forward

# Poison Victim ARP Cache
arpspoof -i eth0 -t 192.168.1.50 192.168.1.1

# Poison Gateway ARP Cache
arpspoof -i eth0 -t 192.168.1.1 192.168.1.50
```

> [!DANGER] 🛡️ **📋 Comprehensive MitM Attack Vector Reference Matrix**

| Attack Type | Target Component | Exploitation Mechanism | Impact on Communication |
| :--- | :--- | :--- | :--- |
| **ARP Poisoning** | Local Switch Subnet | Injects forged ARP replies mapping IP to attacker MAC | Full MitM packet interception |
| **DHCP Rogue Server** | DHCP Clients | Offers malicious Gateway IP & DNS server IP to clients | Redirects all outbound subnet traffic |
| **DNS Spoofing** | DNS Resolver | Responds faster than legitimate DNS server with fake IP | Redirects users to phishing web pages |
| **Switch Port Stealing**| Switch Port Table | Sends ARP packets with victim MAC to flip switch port mapping | Intercepts targeted unicast traffic |

---

## 🛡️ 2. Protocol Analysis & Wireshark Capture Syntax

### 2.1 BPF & Wireshark Filter Specifications

#### Berkeley Packet Filters (BPF / Capture Filters):
Used during raw packet capture (`tcpdump`, Wireshark capture options):
- `host 192.168.1.50`: Capture traffic to/from specific host.
- `port 80 or port 443`: Capture HTTP and HTTPS traffic.
- `net 10.0.0.0/24`: Capture traffic across subnet.
- `not arp and not icmp`: Exclude ARP and ICMP noise packets.

#### Wireshark Display Filters:
Used after capturing packets to filter displayed output:
- `ip.addr == 192.168.1.50`: Filter by IP address.
- `http.request.method == "POST"`: Display HTTP POST login attempts.
- `tcp.flags.syn == 1 and tcp.flags.ack == 0`: Display TCP SYN scan packets.

> [!SHIELD] 🏰 **📋 Comprehensive Packet Filter Syntax Reference Matrix**

| Analysis Engine | Filter Category | Command Example | Filter Objective |
| :--- | :--- | :--- | :--- |
| **Tcpdump / BPF** | Capture Filter | `tcpdump -i eth0 'tcp port 80 and host 10.0.0.5'` | Captures HTTP traffic for specific IP |
| **Wireshark** | Display Filter | `http.authorization contains "Basic"` | Isolates cleartext HTTP Basic Auth headers |
| **Wireshark** | Display Filter | `dns.flags.response == 0` | Isolates outbound DNS query requests |
| **TShark** | CLI Capture | `tshark -i eth0 -f "port 53" -n` | Captures DNS queries from command line |
