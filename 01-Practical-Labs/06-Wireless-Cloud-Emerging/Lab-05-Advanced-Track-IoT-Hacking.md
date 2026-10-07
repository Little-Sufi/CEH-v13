![Lab Image](https://images.unsplash.com/photo-1558494949-ef010cbdcc31?w=800&h=200&fit=crop)

[⬅️ Previous](Lab-04-Advanced-Track-Azure-Security.md) | [🏠 Path Home](Home.md) | [Next Lab ➡️](Lab-06-Advanced-Track-OT-SCADA-Security.md)

---

# Lab 05: Advanced Track - IoT Hacking

---


---




---


---

[⬅️ Path Home](Home.md)

---

## 🎯 Lab Objectives
- Understand IoT architecture, protocols, and vulnerabilities.
- Perform firmware extraction, analysis, and vulnerability finding.
- Simulate IoT device exploitation using firmware analysis frameworks.

## 🛠️ Required Tools & Setup
- **Firmadyne / Firmwalker:** Firmware analysis frameworks.
- **Binwalk:** Firmware extraction utility.
- **QEMU:** Processor emulator for firmware emulation.
- **Resource Link:** [Binwalk GitHub Repository](https://github.com/ReFirmLabs/binwalk)
- **Practice Room:** [TryHackMe IoT Hacking Basics](https://tryhackme.com/room/iothackingbasics)

## 🚶 Step-by-Step Lab Guide

### Step 1: Firmware Extraction with Binwalk
Extract filesystems from a target IoT firmware binary:
```bash
binwalk -e target_firmware.bin
```
Inspect the extracted directories for private keys, plain-text passwords, and configuration files.

### Step 2: Emulating Firmware with QEMU
Run the extracted firmware locally to analyze dynamic behaviors:
```bash
qemu-system-arm -M vexpress-a9 -kernel zImage -drive file=rootfs.ext2
```

---

[⬅️ Path Home](Home.md)

---

[⬅️ Previous](Lab-04-Advanced-Track-Azure-Security.md) | [🏠 Path Home](Home.md) | [Next Lab ➡️](Lab-06-Advanced-Track-OT-SCADA-Security.md)
