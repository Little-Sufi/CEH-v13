# 02. Attack Techniques — Denial-of-Service

> [!WARNING] ⚡ **Exploitation Methodologies & Execution Scenarios**
> Direct extraction from official CEH v13 Syllabus (Module 10). Covers Packet Flooding, Slow-Rate HTTP Attacks (Slowloris/RUDY), Botnet C2 Control Protocols, ICMP Smurf Attacks, and `hping3` Execution Commands.

---

## ⚔️ 1. Slow-Rate HTTP & Malformed Packet Exploitation

### 1.1 Slow-Rate Application Layer Attacks

#### 1. Slowloris
Slowloris opens thousands of persistent HTTP connections to a target web server and transmits incomplete HTTP headers (e.g., sending `User-Agent: Mozilla/5.0
` without the final closing `

`) at periodic intervals (e.g., every 15 seconds).
- **Impact**: Web servers (like Apache) allocate a dedicated worker thread for each connection, quickly exhausting max worker thread limits (`MaxRequestWorkers`), bringing down web availability while utilizing minimal attacker bandwidth.

#### 2. RUDY (R-U-Dead-Yet)
RUDY targets HTTP `POST` submission forms. It sends a legitimate `POST` header specifying a large `Content-Length` header (e.g., `Content-Length: 10000`), but transmits the actual POST body data 1 byte at a time every few seconds.

### 1.2 Malformed Packet Attacks

#### 1. Ping of Death
Sends fragmented ICMP packets exceeding the maximum legal IP packet size of 65,535 bytes. When the victim OS reassembles the fragmented IP payload, it triggers a kernel buffer overflow, resulting in a Blue Screen of Death (BSOD) or system crash.

#### 2. Teardrop Attack
Sends IP fragments with overlapping offset fields. The target OS kernel reassembly routines fail to parse the overlapping offset boundaries, causing memory corruption and crash.

#### 3. Land Attack
Sends IP packets where the source IP address and port are forged to match the destination IP address and port. The victim OS loops endlessly attempting to respond to itself.

> [!DANGER] 🛡️ **📋 Comprehensive Malformed Packet & Slow-Rate Reference Matrix**

| Attack Type | Target Component | Malformed Header / Data Payload | Primary Technical Effect |
| :--- | :--- | :--- | :--- |
| **Slowloris** | Web Server Threads | Incomplete HTTP header termination (`
`) | Exhausts web worker threads |
| **RUDY** | HTTP POST Forms | Large `Content-Length`, 1-byte body updates | Holds web connection threads open |
| **Ping of Death**| IP Reassembly Stack | Oversized payload (>65,535 bytes) | Memory buffer overflow crash |
| **Teardrop** | IP Fragment Assembly | Overlapping fragment offset fields | OS kernel crash / memory fault |
| **Land Attack** | Network Socket Stack | Source IP/Port == Destination IP/Port | Infinite loop connection hang |

---

## 🛡️ 2. Execution CLI Commands (`hping3`)

### 2.1 Hping3 Command-Line Packet Crafting

```bash
# 1. Execute SYN Flood with Spoofed Random Source IPs
hping3 -S --flood --rand-source -p 80 192.168.1.50

# 2. Execute UDP Flood against Target Port 53
hping3 --udp --flood --rand-source -p 53 192.168.1.50

# 3. Execute ICMP Flood (Smurf Simulation)
hping3 --icmp --flood --rand-source 192.168.1.50

# 4. Execute Land Attack (Source IP == Target IP)
hping3 -S -p 80 -a 192.168.1.50 192.168.1.50
```

> [!SHIELD] 🏰 **📋 Comprehensive Hping3 Syntax Reference Matrix**

| Parameter Flag | Operational Function | Security Testing Purpose |
| :--- | :--- | :--- |
| `-S` | Sets TCP `SYN` flag | Simulates TCP SYN queue exhaustion |
| `--flood` | Sends packets at maximum speed | Tests firewalls and server rate limiting |
| `--rand-source` | Generates random spoofed source IPs | Bypasses simple single-IP firewall blocks |
| `-a <IP>` | Sets custom spoofed source IP address | Executes Land or Reflection attack simulations |
