#!/usr/bin/env python3
# LAB-ONLY: Forensic Artifact Enumerator & Anti-Forensics Awareness Tool
# CEH v13 Ultimate Offensive Script 19
# STRICTLY FOR AUTHORIZED LAB USE ONLY! USE ONLY ON YOUR OWN LAB SYSTEMS!
#
# PURPOSE: Enumerates ALL forensic artifacts present on the system that a
# forensic investigator would examine. Does NOT delete anything — it reports
# what exists and how an attacker might try to cover tracks. Blue teams use
# this to verify their artifact collection coverage.
import sys
import os
import platform
import subprocess
import glob
import json
from datetime import datetime

# ═══════════════════════════════════════════════════════════════════════════════
# FORENSIC ARTIFACT ENUMERATOR
# ═══════════════════════════════════════════════════════════════════════════════

class ForensicArtifactEnumerator:
    def __init__(self):
        self.artifacts = []
        self.system = platform.system()

    def found(self, category, name, path, size_bytes=0, detail=""):
        self.artifacts.append({
            "category": category,
            "name": name,
            "path": path,
            "size_bytes": size_bytes,
            "detail": detail,
            "timestamp": datetime.now().isoformat()
        })
        size_str = f" ({self._human_size(size_bytes)})" if size_bytes else ""
        print(f"  📄 [{category}] {name}{size_str}")
        if detail:
            print(f"      → {detail}")

    @staticmethod
    def _human_size(nbytes):
        for unit in ["B", "KB", "MB", "GB"]:
            if abs(nbytes) < 1024:
                return f"{nbytes:.1f} {unit}"
            nbytes /= 1024
        return f"{nbytes:.1f} TB"

    # ─── Windows Artifacts ────────────────────────────────────────────────────
    def scan_windows_event_logs(self):
        print("\n[1/10] Windows Event Logs...")
        log_dir = r"C:\Windows\System32\winevt\Logs"
        if not os.path.exists(log_dir):
            print("  ⏭️  Not a Windows system or no access")
            return
        try:
            for evtx in glob.glob(os.path.join(log_dir, "*.evtx")):
                size = os.path.getsize(evtx)
                if size > 0:
                    name = os.path.basename(evtx)
                    self.found("Event Log", name, evtx, size,
                              f"Wiper cmd: wevtutil cl {name.replace('.evtx','')}")
        except PermissionError:
            print("  🔒 Permission denied — run as Administrator")

    def scan_prefetch(self):
        print("\n[2/10] Prefetch Files (program execution evidence)...")
        prefetch_dir = r"C:\Windows\Prefetch"
        if not os.path.exists(prefetch_dir):
            return
        try:
            pf_files = glob.glob(os.path.join(prefetch_dir, "*.pf"))
            for pf in pf_files[:20]:  # Limit output
                size = os.path.getsize(pf)
                name = os.path.basename(pf)
                self.found("Prefetch", name, pf, size,
                          f"Shows execution of: {name.split('-')[0]}")
            if len(pf_files) > 20:
                print(f"      ... and {len(pf_files) - 20} more prefetch files")
        except PermissionError:
            print("  🔒 Permission denied")

    def scan_recent_files(self):
        print("\n[3/10] Recent Files & Jump Lists...")
        recent_dir = os.path.expanduser(r"~\AppData\Roaming\Microsoft\Windows\Recent")
        if os.path.exists(recent_dir):
            files = os.listdir(recent_dir)
            for f in files[:15]:
                path = os.path.join(recent_dir, f)
                size = os.path.getsize(path) if os.path.isfile(path) else 0
                self.found("Recent Files", f, path, size)
            if len(files) > 15:
                print(f"      ... and {len(files) - 15} more recent files")

    def scan_registry_artifacts(self):
        print("\n[4/10] Registry Run Keys & Persistence...")
        if self.system != "Windows":
            return
        try:
            import winreg
            persistence_keys = [
                (winreg.HKEY_CURRENT_USER, r"Software\Microsoft\Windows\CurrentVersion\Run", "HKCU Run"),
                (winreg.HKEY_LOCAL_MACHINE, r"SOFTWARE\Microsoft\Windows\CurrentVersion\Run", "HKLM Run"),
                (winreg.HKEY_CURRENT_USER, r"Software\Microsoft\Windows\CurrentVersion\RunOnce", "HKCU RunOnce"),
            ]
            for hive, key_path, label in persistence_keys:
                try:
                    key = winreg.OpenKey(hive, key_path)
                    i = 0
                    while True:
                        try:
                            name, value, _ = winreg.EnumValue(key, i)
                            self.found("Registry Persistence", f"{label}: {name}", key_path, detail=f"Value: {value}")
                            i += 1
                        except OSError:
                            break
                    winreg.CloseKey(key)
                except FileNotFoundError:
                    pass
        except ImportError:
            print("  ⏭️  winreg not available")

    def scan_scheduled_tasks(self):
        print("\n[5/10] Scheduled Tasks...")
        if self.system != "Windows":
            return
        try:
            result = subprocess.run(
                ["schtasks", "/query", "/fo", "csv", "/nh"],
                capture_output=True, text=True, timeout=15
            )
            tasks = [l for l in result.stdout.strip().split("\n") if l.strip()]
            for task in tasks[:10]:
                parts = task.split(",")
                if len(parts) >= 2:
                    name = parts[0].strip('"')
                    self.found("Scheduled Task", name, "Task Scheduler", detail=f"Status: {parts[-1].strip('\"')}")
            if len(tasks) > 10:
                print(f"      ... and {len(tasks) - 10} more scheduled tasks")
        except Exception as e:
            print(f"  ⚠️  Could not query tasks: {e}")

    # ─── Linux Artifacts ──────────────────────────────────────────────────────
    def scan_linux_logs(self):
        print("\n[6/10] System Logs...")
        if self.system != "Linux":
            return
        log_files = [
            "/var/log/auth.log", "/var/log/syslog", "/var/log/messages",
            "/var/log/kern.log", "/var/log/secure", "/var/log/cron",
            "/var/log/lastlog", "/var/log/wtmp", "/var/log/btmp",
            "/var/log/faillog", "/var/log/apache2/access.log",
            "/var/log/nginx/access.log",
        ]
        for log in log_files:
            if os.path.exists(log):
                try:
                    size = os.path.getsize(log)
                    self.found("System Log", os.path.basename(log), log, size,
                              f"Wiper cmd: truncate -s 0 {log}")
                except PermissionError:
                    self.found("System Log", os.path.basename(log), log, detail="Exists but cannot read")

    def scan_shell_history(self):
        print("\n[7/10] Shell History Files...")
        home = os.path.expanduser("~")
        history_files = [
            ".bash_history", ".zsh_history", ".python_history",
            ".mysql_history", ".psql_history", ".node_repl_history",
            ".lesshst", ".viminfo", ".wget-hsts",
        ]
        for hf in history_files:
            path = os.path.join(home, hf)
            if os.path.exists(path):
                try:
                    size = os.path.getsize(path)
                    lines = sum(1 for _ in open(path, errors="ignore"))
                    self.found("Shell History", hf, path, size,
                              f"{lines} commands recorded")
                except (PermissionError, UnicodeDecodeError):
                    self.found("Shell History", hf, path, detail="Exists but cannot read")

    def scan_ssh_artifacts(self):
        print("\n[8/10] SSH Artifacts...")
        ssh_dir = os.path.expanduser("~/.ssh")
        if os.path.exists(ssh_dir):
            for f in os.listdir(ssh_dir):
                path = os.path.join(ssh_dir, f)
                size = os.path.getsize(path) if os.path.isfile(path) else 0
                detail = ""
                if f == "known_hosts":
                    try:
                        hosts = sum(1 for _ in open(path, errors="ignore"))
                        detail = f"{hosts} known hosts (shows lateral movement history)"
                    except Exception:
                        pass
                elif f == "authorized_keys":
                    detail = "⚠️ Persistence vector — attacker can add their public key"
                elif f.endswith(".pub"):
                    detail = "Public key"
                elif f in ["id_rsa", "id_ed25519", "id_ecdsa"]:
                    detail = "⚠️ Private key — high-value credential"
                self.found("SSH", f, path, size, detail)

    def scan_cron_persistence(self):
        print("\n[9/10] Cron Jobs & Systemd Timers...")
        if self.system != "Linux":
            return
        # User crontab
        try:
            result = subprocess.run(["crontab", "-l"], capture_output=True, text=True, timeout=5)
            if result.returncode == 0 and result.stdout.strip():
                jobs = [l for l in result.stdout.strip().split("\n") if l and not l.startswith("#")]
                for job in jobs:
                    self.found("Cron Job", "User crontab", "crontab -l", detail=job[:80])
        except Exception:
            pass
        # System cron directories
        for cron_dir in ["/etc/cron.d", "/etc/cron.daily", "/etc/cron.hourly"]:
            if os.path.exists(cron_dir):
                for f in os.listdir(cron_dir):
                    path = os.path.join(cron_dir, f)
                    self.found("Cron Persistence", f, path)

    # ─── Cross-Platform ──────────────────────────────────────────────────────
    def scan_browser_artifacts(self):
        print("\n[10/10] Browser Artifacts...")
        home = os.path.expanduser("~")
        browser_paths = {
            "Chrome History": os.path.join(home, "AppData", "Local", "Google", "Chrome", "User Data", "Default", "History") if self.system == "Windows"
                            else os.path.join(home, ".config", "google-chrome", "Default", "History"),
            "Firefox Profiles": os.path.join(home, "AppData", "Roaming", "Mozilla", "Firefox", "Profiles") if self.system == "Windows"
                               else os.path.join(home, ".mozilla", "firefox"),
            "Edge History": os.path.join(home, "AppData", "Local", "Microsoft", "Edge", "User Data", "Default", "History"),
        }
        for name, path in browser_paths.items():
            if os.path.exists(path):
                if os.path.isfile(path):
                    size = os.path.getsize(path)
                    self.found("Browser", name, path, size, "Contains URLs, downloads, and search history")
                elif os.path.isdir(path):
                    self.found("Browser", name, path, detail=f"{len(os.listdir(path))} profiles found")

    # ─── Run all scans ───────────────────────────────────────────────────────
    def run(self):
        print("=" * 80)
        print("  🔎 FORENSIC ARTIFACT ENUMERATOR (READ-ONLY)")
        print("  LAB-ONLY — CEH v13 Ultimate Offensive Script 19")
        print("=" * 80)
        print(f"  System:   {platform.platform()}")
        print(f"  User:     {os.environ.get('USER', os.environ.get('USERNAME', 'unknown'))}")
        print(f"  Hostname: {platform.node()}")
        print(f"  Time:     {datetime.now().isoformat()}")
        print("=" * 80)
        print("  ℹ️  This tool ENUMERATES artifacts. It does NOT delete anything.")

        if self.system == "Windows":
            self.scan_windows_event_logs()
            self.scan_prefetch()
            self.scan_recent_files()
            self.scan_registry_artifacts()
            self.scan_scheduled_tasks()
        else:
            self.scan_linux_logs()

        self.scan_shell_history()
        self.scan_ssh_artifacts()
        self.scan_cron_persistence()
        self.scan_browser_artifacts()

        # ─── Summary ─────────────────────────────────────────────────────────
        print("\n" + "=" * 80)
        print("  📊 ARTIFACT SUMMARY")
        print("=" * 80)
        categories = {}
        for a in self.artifacts:
            categories[a["category"]] = categories.get(a["category"], 0) + 1
        for cat, count in sorted(categories.items(), key=lambda x: -x[1]):
            print(f"  {cat:25s}: {count} artifacts")
        total_size = sum(a["size_bytes"] for a in self.artifacts)
        print(f"\n  Total artifacts found: {len(self.artifacts)}")
        print(f"  Total artifact size:   {self._human_size(total_size)}")
        print("\n  ⚠️  A forensic investigator can reconstruct attacker activity")
        print("     from these artifacts. Red teams must understand what traces")
        print("     their actions leave behind.")

        # Save report
        report_file = f"forensic-artifacts-{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        try:
            with open(report_file, "w") as f:
                json.dump({"scan_time": datetime.now().isoformat(), "system": platform.platform(),
                           "total_artifacts": len(self.artifacts), "artifacts": self.artifacts}, f, indent=2)
            print(f"\n  📄 Report saved to: {report_file}")
        except Exception as e:
            print(f"\n  ⚠️  Could not save report: {e}")


if __name__ == "__main__":
    enumerator = ForensicArtifactEnumerator()
    enumerator.run()
