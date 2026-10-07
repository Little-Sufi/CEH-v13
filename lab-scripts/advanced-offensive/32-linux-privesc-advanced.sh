#!/bin/bash
# LAB-ONLY: Advanced Linux Privilege Escalation Enumeration Script
# CEH v13 Master Module 06
# STRICTLY FOR AUTHORIZED LAB USE ONLY!
# DETAILED EXPLANATION: Enumerates all vectors for Linux privesc!
# -------------------------- EDIT THESE VALUES FOR YOUR LAB --------------------------
LAB_OUTPUT_FILE="linux-privesc-report.txt"
# -----------------------------------------------------------------------------------

echo "="*80 > $LAB_OUTPUT_FILE
echo "LAB-ONLY: Linux Privesc Enumeration Report" >> $LAB_OUTPUT_FILE
echo "="*80 >> $LAB_OUTPUT_FILE
echo >> $LAB_OUTPUT_FILE
echo "[*] 1. Kernel & OS info" >> $LAB_OUTPUT_FILE
uname -a >> $LAB_OUTPUT_FILE
cat /etc/issue >> $LAB_OUTPUT_FILE
cat /etc/*release >> $LAB_OUTPUT_FILE
echo >> $LAB_OUTPUT_FILE
echo "[*] 2. Users & Groups" >> $LAB_OUTPUT_FILE
cat /etc/passwd >> $LAB_OUTPUT_FILE
cat /etc/group >> $LAB_OUTPUT_FILE
echo >> $LAB_OUTPUT_FILE
echo "[*] 3. Sudo permissions" >> $LAB_OUTPUT_FILE
sudo -l >> $LAB_OUTPUT_FILE 2>&1
echo >> $LAB_OUTPUT_FILE
echo "[*] 4. SUID/SGID files" >> $LAB_OUTPUT_FILE
find / -type f \( -perm -4000 -o -perm -2000 \) -exec ls -l {} \; 2>/dev/null >> $LAB_OUTPUT_FILE
echo >> $LAB_OUTPUT_FILE
echo "[*] 5. Capabilities" >> $LAB_OUTPUT_FILE
getcap -r / 2>/dev/null >> $LAB_OUTPUT_FILE
echo >> $LAB_OUTPUT_FILE
echo "[*] 6. Writable files/dirs" >> $LAB_OUTPUT_FILE
find / -writable -type d 2>/dev/null | head -50 >> $LAB_OUTPUT_FILE
echo >> $LAB_OUTPUT_FILE
echo "[*] 7. Processes" >> $LAB_OUTPUT_FILE
ps aux >> $LAB_OUTPUT_FILE
echo >> $LAB_OUTPUT_FILE
echo "[*] 8. Cron jobs" >> $LAB_OUTPUT_FILE
cat /etc/crontab >> $LAB_OUTPUT_FILE
ls -la /etc/cron* >> $LAB_OUTPUT_FILE
echo >> $LAB_OUTPUT_FILE
echo "[*] 9. Network info" >> $LAB_OUTPUT_FILE
ifconfig -a >> $LAB_OUTPUT_FILE 2>&1 || ip a >> $LAB_OUTPUT_FILE
netstat -tuln >> $LAB_OUTPUT_FILE 2>&1 || ss -tuln >> $LAB_OUTPUT_FILE
echo "[+] Report saved to $LAB_OUTPUT_FILE"
