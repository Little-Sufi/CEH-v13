#!/bin/bash
# LAB-ONLY: Linux PrivEsc Enumeration Wrapper
# CEH v13 Master Module 06
# STRICTLY FOR AUTHORIZED LAB USE ONLY!

# -------------------------- EDIT THESE VALUES FOR YOUR LAB --------------------------
LAB_OUTPUT_DIR="$HOME/lab-privesc-enum"
# -----------------------------------------------------------------------------------

mkdir -p "$LAB_OUTPUT_DIR"
TIMESTAMP=$(date +%Y%m%d_%H%M%S)
OUTFILE="$LAB_OUTPUT_DIR/lab-privesc-enum-$TIMESTAMP.log"

echo "================================================" | tee -a "$OUTFILE"
echo "LAB-ONLY: Linux Privilege Escalation Enumeration" | tee -a "$OUTFILE"
echo "================================================" | tee -a "$OUTFILE"

echo "1. Checking kernel/OS version..." | tee -a "$OUTFILE"
uname -a >> "$OUTFILE" 2>&1
cat /etc/os-release >> "$OUTFILE" 2>&1
echo "" | tee -a "$OUTFILE"

echo "2. Checking SUID/SGID binaries..." | tee -a "$OUTFILE"
find / -perm -4000 -type f 2>/dev/null >> "$OUTFILE"
find / -perm -2000 -type f 2>/dev/null >> "$OUTFILE"
echo "" | tee -a "$OUTFILE"

echo "3. Checking writable directories/files..." | tee -a "$OUTFILE"
find / -writable -type f 2>/dev/null | head -50 >> "$OUTFILE"
echo "" | tee -a "$OUTFILE"

echo "4. Checking cron jobs..." | tee -a "$OUTFILE"
ls -la /etc/cron* >> "$OUTFILE" 2>&1
cat /etc/crontab >> "$OUTFILE" 2>&1
echo "" | tee -a "$OUTFILE"

echo "Done! Full log saved to $OUTFILE"
