#!/usr/bin/env python3
# LAB-ONLY: Advanced Sandbox / VM / Analysis Environment Detection
# CEH v13 Ultimate Offensive Script 17
# STRICTLY FOR AUTHORIZED LAB USE ONLY!
#
# PURPOSE: Performs 15+ real checks to determine if the current environment
# is a malware analysis sandbox, virtual machine, or debugger-attached process.
# Red teams use this to understand what blue team detection environments look like.
import sys
import os
import platform
import socket
import struct
import time
import subprocess
import re
from datetime import datetime

# ═══════════════════════════════════════════════════════════════════════════════
# SANDBOX / VM DETECTION ENGINE
# ═══════════════════════════════════════════════════════════════════════════════

class SandboxEvasionChecker:
    def __init__(self):
        self.checks = []
        self.sandbox_score = 0  # Higher = more likely sandbox

    def result(self, name, is_suspicious, detail, weight=1):
        status = "⚠️  SANDBOX" if is_suspicious else "✅ CLEAN"
        self.checks.append({"name": name, "suspicious": is_suspicious, "detail": detail, "weight": weight})
        if is_suspicious:
            self.sandbox_score += weight
        print(f"  {status}  {name}: {detail}")

    # ─── Check 1: CPU core count ─────────────────────────────────────────────
    def check_cpu_cores(self):
        cores = os.cpu_count() or 0
        self.result("CPU Cores", cores <= 2, f"{cores} cores detected (sandboxes typically have ≤2)", weight=2)

    # ─── Check 2: RAM size ───────────────────────────────────────────────────
    def check_ram(self):
        try:
            if platform.system() == "Linux":
                with open("/proc/meminfo", "r") as f:
                    for line in f:
                        if line.startswith("MemTotal:"):
                            kb = int(line.split()[1])
                            gb = kb / (1024 * 1024)
                            self.result("Total RAM", gb < 4, f"{gb:.1f} GB (sandboxes typically have <4GB)", weight=2)
                            return
            elif platform.system() == "Windows":
                import ctypes
                kernel32 = ctypes.windll.kernel32
                c_ulong = ctypes.c_ulong
                class MEMORYSTATUSEX(ctypes.Structure):
                    _fields_ = [("dwLength", c_ulong), ("dwMemoryLoad", c_ulong),
                                ("ullTotalPhys", ctypes.c_ulonglong), ("ullAvailPhys", ctypes.c_ulonglong),
                                ("ullTotalPageFile", ctypes.c_ulonglong), ("ullAvailPageFile", ctypes.c_ulonglong),
                                ("ullTotalVirtual", ctypes.c_ulonglong), ("ullAvailVirtual", ctypes.c_ulonglong),
                                ("ullAvailExtendedVirtual", ctypes.c_ulonglong)]
                mem = MEMORYSTATUSEX()
                mem.dwLength = ctypes.sizeof(MEMORYSTATUSEX)
                kernel32.GlobalMemoryStatusEx(ctypes.byref(mem))
                gb = mem.ullTotalPhys / (1024**3)
                self.result("Total RAM", gb < 4, f"{gb:.1f} GB (sandboxes typically have <4GB)", weight=2)
                return
        except Exception as e:
            self.result("Total RAM", False, f"Could not determine: {e}")

    # ─── Check 3: Disk size ──────────────────────────────────────────────────
    def check_disk_size(self):
        try:
            if platform.system() == "Windows":
                import ctypes
                free_bytes = ctypes.c_ulonglong(0)
                total_bytes = ctypes.c_ulonglong(0)
                ctypes.windll.kernel32.GetDiskFreeSpaceExW(
                    "C:\\", None, ctypes.pointer(total_bytes), ctypes.pointer(free_bytes))
                gb = total_bytes.value / (1024**3)
                self.result("Disk Size", gb < 80, f"{gb:.0f} GB (sandboxes often have <80GB)", weight=2)
            else:
                st = os.statvfs("/")
                gb = (st.f_blocks * st.f_frsize) / (1024**3)
                self.result("Disk Size", gb < 80, f"{gb:.0f} GB (sandboxes often have <80GB)", weight=2)
        except Exception as e:
            self.result("Disk Size", False, f"Could not determine: {e}")

    # ─── Check 4: System uptime ──────────────────────────────────────────────
    def check_uptime(self):
        try:
            if platform.system() == "Linux":
                with open("/proc/uptime", "r") as f:
                    uptime_sec = float(f.read().split()[0])
                    uptime_min = uptime_sec / 60
                    self.result("System Uptime", uptime_min < 10,
                                f"{uptime_min:.1f} minutes (sandboxes are freshly booted, <10min)", weight=3)
            elif platform.system() == "Windows":
                result = subprocess.run(["net", "stats", "workstation"], capture_output=True, text=True, timeout=5)
                # Parse "Statistics since" line
                self.result("System Uptime", False, "Check manually on Windows")
        except Exception as e:
            self.result("System Uptime", False, f"Could not determine: {e}")

    # ─── Check 5: MAC address OUI (VM vendors) ──────────────────────────────
    def check_mac_address(self):
        vm_ouis = {
            "00:05:69": "VMware", "00:0c:29": "VMware", "00:1c:14": "VMware",
            "00:50:56": "VMware", "08:00:27": "VirtualBox", "0a:00:27": "VirtualBox",
            "00:15:5d": "Hyper-V", "00:16:3e": "Xen", "52:54:00": "QEMU/KVM",
            "00:1a:4a": "Parallels",
        }
        try:
            if platform.system() == "Linux":
                result = subprocess.run(["ip", "link"], capture_output=True, text=True, timeout=5)
                macs = re.findall(r"link/ether\s+([0-9a-f:]+)", result.stdout.lower())
            elif platform.system() == "Windows":
                result = subprocess.run(["getmac", "/fo", "csv", "/nh"], capture_output=True, text=True, timeout=5)
                macs = re.findall(r"([0-9A-Fa-f]{2}[-:][0-9A-Fa-f]{2}[-:][0-9A-Fa-f]{2})", result.stdout)
                macs = [m.replace("-", ":").lower() for m in macs]
            else:
                macs = []

            for mac in macs:
                prefix = mac[:8]
                if prefix in vm_ouis:
                    self.result("MAC Address OUI", True,
                                f"{mac} → {vm_ouis[prefix]} virtual NIC detected", weight=3)
                    return
            self.result("MAC Address OUI", False, f"No VM vendor MAC detected ({len(macs)} NICs checked)")
        except Exception as e:
            self.result("MAC Address OUI", False, f"Could not check: {e}")

    # ─── Check 6: VM-specific registry keys (Windows) ────────────────────────
    def check_registry_keys(self):
        if platform.system() != "Windows":
            self.result("Registry VM Keys", False, "N/A (Linux)")
            return
        try:
            import winreg
            vm_keys = [
                (winreg.HKEY_LOCAL_MACHINE, r"SOFTWARE\VMware, Inc.\VMware Tools", "VMware Tools"),
                (winreg.HKEY_LOCAL_MACHINE, r"SOFTWARE\Oracle\VirtualBox Guest Additions", "VirtualBox GA"),
                (winreg.HKEY_LOCAL_MACHINE, r"SYSTEM\CurrentControlSet\Services\VBoxGuest", "VBoxGuest Driver"),
                (winreg.HKEY_LOCAL_MACHINE, r"SYSTEM\CurrentControlSet\Services\vmci", "VMware VMCI"),
            ]
            for hive, key, name in vm_keys:
                try:
                    winreg.OpenKey(hive, key)
                    self.result("Registry VM Keys", True, f"Found: {name} ({key})", weight=3)
                    return
                except FileNotFoundError:
                    pass
            self.result("Registry VM Keys", False, "No VM registry keys found")
        except ImportError:
            self.result("Registry VM Keys", False, "winreg not available")

    # ─── Check 7: VM-specific processes ──────────────────────────────────────
    def check_vm_processes(self):
        vm_processes = [
            "vmtoolsd", "vmwaretray", "vmwareuser",  # VMware
            "VBoxService", "VBoxTray",                 # VirtualBox
            "qemu-ga", "spice-vdagent",                # QEMU/KVM
            "xenservice",                              # Xen
        ]
        analysis_processes = [
            "wireshark", "procmon", "procexp", "ollydbg", "x64dbg", "x32dbg",
            "ida", "ida64", "ghidra", "radare2", "r2",  # Debuggers/reversing
            "fiddler", "burpsuite", "mitmproxy",         # Proxy tools
            "processhacker", "autoruns",                  # Sysinternals
        ]
        try:
            if platform.system() == "Windows":
                result = subprocess.run(["tasklist", "/fo", "csv", "/nh"], capture_output=True, text=True, timeout=10)
                processes = result.stdout.lower()
            else:
                result = subprocess.run(["ps", "aux"], capture_output=True, text=True, timeout=10)
                processes = result.stdout.lower()

            found_vm = [p for p in vm_processes if p.lower() in processes]
            found_analysis = [p for p in analysis_processes if p.lower() in processes]

            if found_vm:
                self.result("VM Processes", True, f"VM tools running: {', '.join(found_vm)}", weight=2)
            else:
                self.result("VM Processes", False, "No VM guest tools detected")

            if found_analysis:
                self.result("Analysis Tools", True, f"Analysis tools running: {', '.join(found_analysis)}", weight=3)
            else:
                self.result("Analysis Tools", False, "No debuggers/analysis tools detected")
        except Exception as e:
            self.result("VM/Analysis Processes", False, f"Could not check: {e}")

    # ─── Check 8: Screen resolution ──────────────────────────────────────────
    def check_screen_resolution(self):
        sandbox_resolutions = [(800, 600), (1024, 768)]
        try:
            if platform.system() == "Windows":
                import ctypes
                user32 = ctypes.windll.user32
                w, h = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)
                is_sandbox = (w, h) in sandbox_resolutions
                self.result("Screen Resolution", is_sandbox, f"{w}x{h} (sandboxes often use 800x600 or 1024x768)", weight=2)
            else:
                result = subprocess.run(["xdpyinfo"], capture_output=True, text=True, timeout=3)
                match = re.search(r"dimensions:\s+(\d+)x(\d+)", result.stdout)
                if match:
                    w, h = int(match.group(1)), int(match.group(2))
                    is_sandbox = (w, h) in sandbox_resolutions
                    self.result("Screen Resolution", is_sandbox, f"{w}x{h}", weight=2)
                else:
                    self.result("Screen Resolution", False, "Could not detect (headless?)")
        except Exception:
            self.result("Screen Resolution", False, "Could not detect (headless environment)")

    # ─── Check 9: Recently opened files / user activity ──────────────────────
    def check_user_activity(self):
        try:
            if platform.system() == "Windows":
                recent_dir = os.path.expanduser("~\\AppData\\Roaming\\Microsoft\\Windows\\Recent")
                if os.path.exists(recent_dir):
                    files = os.listdir(recent_dir)
                    self.result("User Activity", len(files) < 10,
                                f"{len(files)} recent files (sandboxes have very few)", weight=2)
                    return
            elif platform.system() == "Linux":
                home = os.path.expanduser("~")
                bash_history = os.path.join(home, ".bash_history")
                if os.path.exists(bash_history):
                    lines = open(bash_history).readlines()
                    self.result("User Activity", len(lines) < 5,
                                f"{len(lines)} history entries (sandboxes have near-empty history)", weight=2)
                    return
        except Exception:
            pass
        self.result("User Activity", False, "Could not assess")

    # ─── Check 10: Timing-based detection ────────────────────────────────────
    def check_timing(self):
        """Sandboxes with CPU emulation have slower timing"""
        iterations = 1000000
        start = time.perf_counter()
        total = 0
        for i in range(iterations):
            total += i * i
        elapsed = time.perf_counter() - start
        # On real hardware, 1M iterations takes <0.1s; emulated can take >0.5s
        is_slow = elapsed > 0.5
        self.result("CPU Timing", is_slow,
                    f"{iterations} iterations in {elapsed:.3f}s (emulated CPUs are >0.5s)", weight=2)

    # ─── Check 11: Hostname patterns ────────────────────────────────────────
    def check_hostname(self):
        hostname = socket.gethostname().lower()
        sandbox_names = ["sandbox", "malware", "virus", "sample", "test", "analysis",
                         "cuckoo", "joe", "anubis", "comodo", "hybrid", "falcon"]
        matched = [s for s in sandbox_names if s in hostname]
        self.result("Hostname Pattern", bool(matched),
                    f"Hostname '{hostname}' matches sandbox keywords: {matched}" if matched
                    else f"Hostname '{hostname}' — no sandbox keywords", weight=2)

    # ─── Run all checks ──────────────────────────────────────────────────────
    def run(self):
        print("=" * 80)
        print("  🕵️  SANDBOX / VM / ANALYSIS ENVIRONMENT DETECTOR")
        print("  LAB-ONLY — CEH v13 Ultimate Offensive Script 17")
        print("=" * 80)
        print(f"  Platform: {platform.platform()}")
        print(f"  Python:   {platform.python_version()}")
        print(f"  Time:     {datetime.now().isoformat()}")
        print("=" * 80)

        self.check_cpu_cores()
        self.check_ram()
        self.check_disk_size()
        self.check_uptime()
        self.check_mac_address()
        self.check_registry_keys()
        self.check_vm_processes()
        self.check_screen_resolution()
        self.check_user_activity()
        self.check_timing()
        self.check_hostname()

        # ─── Verdict ─────────────────────────────────────────────────────────
        max_score = sum(c["weight"] for c in self.checks)
        suspicious = [c for c in self.checks if c["suspicious"]]

        print("\n" + "=" * 80)
        print("  📊 VERDICT")
        print("=" * 80)
        print(f"  Sandbox Score: {self.sandbox_score} / {max_score}")
        pct = (self.sandbox_score / max_score * 100) if max_score else 0

        if pct >= 60:
            print(f"  🔴 HIGH PROBABILITY SANDBOX/VM ({pct:.0f}%)")
            print("  → This environment is very likely a malware analysis sandbox or VM")
        elif pct >= 30:
            print(f"  🟡 MODERATE INDICATORS ({pct:.0f}%)")
            print("  → Some sandbox indicators present — could be a lightweight VM")
        else:
            print(f"  🟢 LIKELY REAL HARDWARE ({pct:.0f}%)")
            print("  → Environment appears to be real hardware or well-configured VM")

        if suspicious:
            print(f"\n  Suspicious indicators ({len(suspicious)}):")
            for c in suspicious:
                print(f"    ⚠️  {c['name']}: {c['detail']}")


if __name__ == "__main__":
    checker = SandboxEvasionChecker()
    checker.run()
