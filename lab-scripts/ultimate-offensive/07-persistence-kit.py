#!/usr/bin/env python3
# LAB-ONLY: Post-Exploitation Persistence Mechanism Toolkit
# CEH v13 Ultimate Offensive Script 07
# STRICTLY FOR AUTHORIZED LAB USE ONLY!
#
# PURPOSE: Enumerates existing persistence mechanisms on the target system,
# and can DEPLOY or REMOVE lab-safe persistence entries for testing
# detection capabilities. Supports Windows (Registry, Tasks, WMI) and
# Linux (cron, systemd, bashrc, authorized_keys).
import sys
import os
import platform
import subprocess
import json
import argparse
from datetime import datetime

# ═══════════════════════════════════════════════════════════════════════════════
# CONFIGURATION
# ═══════════════════════════════════════════════════════════════════════════════
LAB_MARKER = "CEH_V13_LAB_PERSISTENCE"  # All entries are tagged for easy cleanup

# ═══════════════════════════════════════════════════════════════════════════════
# PERSISTENCE ENGINE
# ═══════════════════════════════════════════════════════════════════════════════

class PersistenceKit:
    def __init__(self):
        self.system = platform.system()
        self.findings = []
        self.deployed = []

    def log(self, action, method, detail, status="INFO"):
        icon = {"FOUND": "🔍", "DEPLOYED": "⚡", "REMOVED": "🧹", "INFO": "ℹ️", "ERROR": "❌"}
        entry = {"action": action, "method": method, "detail": detail, "status": status,
                 "timestamp": datetime.now().isoformat()}
        self.findings.append(entry)
        print(f"  {icon.get(status, '⚪')} [{status}] {method}: {detail}")

    # ═══════════════════════════════════════════════════════════════════════════
    # ENUMERATION MODE — Find existing persistence
    # ═══════════════════════════════════════════════════════════════════════════

    def enum_windows_registry(self):
        """Scan Windows registry Run keys for persistence entries"""
        if self.system != "Windows":
            return
        print("\n[1/7] Registry Run Keys...")
        try:
            import winreg
            locations = [
                (winreg.HKEY_CURRENT_USER, r"Software\Microsoft\Windows\CurrentVersion\Run", "HKCU\\Run"),
                (winreg.HKEY_CURRENT_USER, r"Software\Microsoft\Windows\CurrentVersion\RunOnce", "HKCU\\RunOnce"),
                (winreg.HKEY_LOCAL_MACHINE, r"SOFTWARE\Microsoft\Windows\CurrentVersion\Run", "HKLM\\Run"),
                (winreg.HKEY_LOCAL_MACHINE, r"SOFTWARE\Microsoft\Windows\CurrentVersion\RunOnce", "HKLM\\RunOnce"),
                (winreg.HKEY_CURRENT_USER, r"Software\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders", "HKCU\\Shell Folders"),
            ]
            for hive, path, label in locations:
                try:
                    key = winreg.OpenKey(hive, path, 0, winreg.KEY_READ)
                    i = 0
                    while True:
                        try:
                            name, value, _ = winreg.EnumValue(key, i)
                            is_lab = LAB_MARKER in str(value)
                            self.log("ENUM", f"Registry: {label}",
                                     f"{name} = {value}" + (" [LAB ENTRY]" if is_lab else ""),
                                     "FOUND")
                            i += 1
                        except OSError:
                            break
                    winreg.CloseKey(key)
                except FileNotFoundError:
                    pass
        except ImportError:
            self.log("ENUM", "Registry", "winreg not available", "ERROR")

    def enum_windows_tasks(self):
        """Scan scheduled tasks"""
        if self.system != "Windows":
            return
        print("\n[2/7] Scheduled Tasks...")
        try:
            result = subprocess.run(
                ["schtasks", "/query", "/fo", "csv", "/v"],
                capture_output=True, text=True, timeout=15
            )
            for line in result.stdout.split("\n"):
                if LAB_MARKER in line:
                    self.log("ENUM", "Scheduled Task", line.strip()[:100], "FOUND")
                elif "\\Microsoft\\Windows\\" not in line and line.strip() and not line.startswith('"TaskName"'):
                    parts = line.split('","')
                    if len(parts) > 1:
                        task_name = parts[0].strip('"')
                        if task_name and not task_name.startswith("\\Microsoft"):
                            self.log("ENUM", "Scheduled Task", task_name, "FOUND")
        except Exception as e:
            self.log("ENUM", "Scheduled Tasks", str(e), "ERROR")

    def enum_windows_services(self):
        """Scan for unusual services"""
        if self.system != "Windows":
            return
        print("\n[3/7] Windows Services...")
        try:
            result = subprocess.run(
                ["sc", "query", "type=", "service", "state=", "all"],
                capture_output=True, text=True, timeout=15
            )
            services = result.stdout.split("SERVICE_NAME: ")
            non_ms = [s.split("\n")[0].strip() for s in services
                       if s.strip() and LAB_MARKER in s]
            for svc in non_ms:
                self.log("ENUM", "Service", svc, "FOUND")
        except Exception as e:
            self.log("ENUM", "Services", str(e), "ERROR")

    def enum_windows_startup(self):
        """Check startup folder"""
        if self.system != "Windows":
            return
        print("\n[4/7] Startup Folder...")
        startup_dirs = [
            os.path.expanduser(r"~\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup"),
            r"C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Startup",
        ]
        for d in startup_dirs:
            if os.path.exists(d):
                for f in os.listdir(d):
                    self.log("ENUM", "Startup Folder", os.path.join(d, f), "FOUND")

    def enum_linux_cron(self):
        """Scan crontabs"""
        if self.system != "Linux":
            return
        print("\n[1/7] Cron Jobs...")
        try:
            result = subprocess.run(["crontab", "-l"], capture_output=True, text=True, timeout=5)
            if result.returncode == 0:
                for line in result.stdout.split("\n"):
                    if line.strip() and not line.startswith("#"):
                        is_lab = LAB_MARKER in line
                        self.log("ENUM", "User Crontab", line.strip() + (" [LAB]" if is_lab else ""), "FOUND")
        except Exception:
            pass
        # System cron
        for cron_dir in ["/etc/cron.d", "/etc/cron.daily", "/etc/cron.hourly"]:
            if os.path.exists(cron_dir):
                for f in os.listdir(cron_dir):
                    self.log("ENUM", f"System Cron ({cron_dir})", f, "FOUND")

    def enum_linux_systemd(self):
        """Scan user systemd services"""
        if self.system != "Linux":
            return
        print("\n[2/7] Systemd User Services...")
        user_systemd = os.path.expanduser("~/.config/systemd/user/")
        if os.path.exists(user_systemd):
            for f in os.listdir(user_systemd):
                if f.endswith(".service") or f.endswith(".timer"):
                    is_lab = LAB_MARKER in f
                    self.log("ENUM", "Systemd User Unit", f + (" [LAB]" if is_lab else ""), "FOUND")

    def enum_linux_bashrc(self):
        """Check shell RC files for persistence"""
        if self.system != "Linux":
            return
        print("\n[3/7] Shell RC Files...")
        rc_files = [
            os.path.expanduser("~/.bashrc"),
            os.path.expanduser("~/.bash_profile"),
            os.path.expanduser("~/.profile"),
            os.path.expanduser("~/.zshrc"),
        ]
        for rc in rc_files:
            if os.path.exists(rc):
                try:
                    with open(rc, "r") as f:
                        content = f.read()
                    if LAB_MARKER in content:
                        self.log("ENUM", "Shell RC", f"{rc} contains LAB persistence entry", "FOUND")
                    # Check for suspicious patterns
                    suspicious = ["nc -e", "bash -i >& /dev/tcp", "python -c", "curl | bash", "wget -O - |"]
                    for pat in suspicious:
                        if pat in content:
                            self.log("ENUM", "Shell RC", f"{rc} contains suspicious: '{pat}'", "FOUND")
                except PermissionError:
                    pass

    def enum_linux_ssh_keys(self):
        """Check authorized_keys for persistence"""
        if self.system != "Linux":
            return
        print("\n[4/7] SSH Authorized Keys...")
        auth_keys = os.path.expanduser("~/.ssh/authorized_keys")
        if os.path.exists(auth_keys):
            try:
                with open(auth_keys, "r") as f:
                    keys = [l.strip() for l in f.readlines() if l.strip() and not l.startswith("#")]
                for key in keys:
                    comment = key.split()[-1] if len(key.split()) >= 3 else "no-comment"
                    is_lab = LAB_MARKER in key
                    self.log("ENUM", "SSH Key", f"{comment}" + (" [LAB]" if is_lab else ""), "FOUND")
            except PermissionError:
                pass

    # ═══════════════════════════════════════════════════════════════════════════
    # DEPLOY MODE — Install lab-safe persistence (tagged for cleanup)
    # ═══════════════════════════════════════════════════════════════════════════

    def deploy_windows_registry(self):
        if self.system != "Windows":
            return
        try:
            import winreg
            key = winreg.OpenKey(winreg.HKEY_CURRENT_USER,
                                r"Software\Microsoft\Windows\CurrentVersion\Run",
                                0, winreg.KEY_SET_VALUE)
            winreg.SetValueEx(key, LAB_MARKER, 0, winreg.REG_SZ,
                              f"cmd.exe /c echo {LAB_MARKER} > NUL")
            winreg.CloseKey(key)
            self.log("DEPLOY", "Registry Run Key", f"HKCU\\Run\\{LAB_MARKER}", "DEPLOYED")
        except Exception as e:
            self.log("DEPLOY", "Registry Run Key", str(e), "ERROR")

    def deploy_windows_task(self):
        if self.system != "Windows":
            return
        try:
            subprocess.run([
                "schtasks", "/create", "/tn", LAB_MARKER,
                "/tr", f"cmd.exe /c echo {LAB_MARKER}",
                "/sc", "ONLOGON", "/f"
            ], capture_output=True, text=True, timeout=10)
            self.log("DEPLOY", "Scheduled Task", LAB_MARKER, "DEPLOYED")
        except Exception as e:
            self.log("DEPLOY", "Scheduled Task", str(e), "ERROR")

    def deploy_linux_cron(self):
        if self.system != "Linux":
            return
        try:
            result = subprocess.run(["crontab", "-l"], capture_output=True, text=True)
            existing = result.stdout if result.returncode == 0 else ""
            if LAB_MARKER not in existing:
                new_cron = existing + f"\n# {LAB_MARKER}\n@reboot echo '{LAB_MARKER}' > /dev/null\n"
                proc = subprocess.run(["crontab", "-"], input=new_cron, capture_output=True, text=True)
                self.log("DEPLOY", "Cron Job", f"@reboot entry with marker {LAB_MARKER}", "DEPLOYED")
        except Exception as e:
            self.log("DEPLOY", "Cron Job", str(e), "ERROR")

    def deploy_linux_bashrc(self):
        if self.system != "Linux":
            return
        bashrc = os.path.expanduser("~/.bashrc")
        try:
            with open(bashrc, "r") as f:
                content = f.read()
            if LAB_MARKER not in content:
                with open(bashrc, "a") as f:
                    f.write(f"\n# {LAB_MARKER} — Lab persistence test (safe to remove)\n")
                    f.write(f"# echo '{LAB_MARKER} persistence active'\n")
                self.log("DEPLOY", "Bashrc", f"Appended marker comment to {bashrc}", "DEPLOYED")
        except Exception as e:
            self.log("DEPLOY", "Bashrc", str(e), "ERROR")

    # ═══════════════════════════════════════════════════════════════════════════
    # CLEANUP MODE — Remove all LAB entries
    # ═══════════════════════════════════════════════════════════════════════════

    def cleanup_windows(self):
        if self.system != "Windows":
            return
        try:
            import winreg
            key = winreg.OpenKey(winreg.HKEY_CURRENT_USER,
                                r"Software\Microsoft\Windows\CurrentVersion\Run",
                                0, winreg.KEY_SET_VALUE)
            try:
                winreg.DeleteValue(key, LAB_MARKER)
                self.log("CLEANUP", "Registry", f"Removed {LAB_MARKER} from HKCU\\Run", "REMOVED")
            except FileNotFoundError:
                pass
            winreg.CloseKey(key)
        except Exception:
            pass
        try:
            subprocess.run(["schtasks", "/delete", "/tn", LAB_MARKER, "/f"],
                           capture_output=True, timeout=10)
            self.log("CLEANUP", "Scheduled Task", f"Removed {LAB_MARKER}", "REMOVED")
        except Exception:
            pass

    def cleanup_linux(self):
        if self.system != "Linux":
            return
        # Clean crontab
        try:
            result = subprocess.run(["crontab", "-l"], capture_output=True, text=True)
            if result.returncode == 0 and LAB_MARKER in result.stdout:
                cleaned = "\n".join(l for l in result.stdout.split("\n") if LAB_MARKER not in l)
                subprocess.run(["crontab", "-"], input=cleaned, capture_output=True, text=True)
                self.log("CLEANUP", "Cron", f"Removed {LAB_MARKER} entries", "REMOVED")
        except Exception:
            pass
        # Clean bashrc
        bashrc = os.path.expanduser("~/.bashrc")
        try:
            with open(bashrc, "r") as f:
                lines = f.readlines()
            cleaned = [l for l in lines if LAB_MARKER not in l]
            if len(cleaned) < len(lines):
                with open(bashrc, "w") as f:
                    f.writelines(cleaned)
                self.log("CLEANUP", "Bashrc", f"Removed {LAB_MARKER} lines", "REMOVED")
        except Exception:
            pass

    # ═══════════════════════════════════════════════════════════════════════════
    # MAIN
    # ═══════════════════════════════════════════════════════════════════════════

    def run(self, mode="enum"):
        print("=" * 80)
        print("  🔐 POST-EXPLOITATION PERSISTENCE TOOLKIT")
        print("  LAB-ONLY — CEH v13 Ultimate Offensive Script 07")
        print("=" * 80)
        print(f"  System: {platform.platform()}")
        print(f"  User:   {os.environ.get('USER', os.environ.get('USERNAME', 'unknown'))}")
        print(f"  Mode:   {mode.upper()}")
        print(f"  Marker: {LAB_MARKER}")
        print("=" * 80)

        if mode == "enum":
            if self.system == "Windows":
                self.enum_windows_registry()
                self.enum_windows_tasks()
                self.enum_windows_services()
                self.enum_windows_startup()
            else:
                self.enum_linux_cron()
                self.enum_linux_systemd()
                self.enum_linux_bashrc()
                self.enum_linux_ssh_keys()

        elif mode == "deploy":
            print("\n  ⚠️  DEPLOYING lab-safe persistence entries...")
            print(f"  All entries are tagged with: {LAB_MARKER}")
            if self.system == "Windows":
                self.deploy_windows_registry()
                self.deploy_windows_task()
            else:
                self.deploy_linux_cron()
                self.deploy_linux_bashrc()

        elif mode == "cleanup":
            print(f"\n  🧹 Removing all entries tagged with: {LAB_MARKER}")
            if self.system == "Windows":
                self.cleanup_windows()
            else:
                self.cleanup_linux()

        # Summary
        print(f"\n{'=' * 80}")
        print(f"  📊 {len(self.findings)} actions performed")
        print(f"{'=' * 80}")

        report_file = f"persistence-{mode}-{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        try:
            with open(report_file, "w") as f:
                json.dump({"mode": mode, "system": self.system, "findings": self.findings}, f, indent=2)
            print(f"  📄 Report: {report_file}")
        except Exception:
            pass


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="LAB-ONLY Persistence Toolkit")
    parser.add_argument("--mode", choices=["enum", "deploy", "cleanup"], default="enum",
                        help="enum=scan for persistence, deploy=install lab entries, cleanup=remove lab entries")
    args = parser.parse_args()

    kit = PersistenceKit()
    kit.run(mode=args.mode)
