@echo off
REM LAB-ONLY: Advanced Windows Privilege Escalation Enumeration Script
REM CEH v13 Master Module 06
REM STRICTLY FOR AUTHORIZED LAB USE ONLY!
REM -------------------------- EDIT THESE VALUES FOR YOUR LAB --------------------------
set LAB_OUTPUT_FILE=windows-privesc-report.txt
REM -----------------------------------------------------------------------------------

echo ================================================================================ > %LAB_OUTPUT_FILE%
echo LAB-ONLY: Windows Privesc Enumeration Report >> %LAB_OUTPUT_FILE%
echo ================================================================================ >> %LAB_OUTPUT_FILE%
echo. >> %LAB_OUTPUT_FILE%
echo [*] 1. System info >> %LAB_OUTPUT_FILE%
systeminfo >> %LAB_OUTPUT_FILE%
echo. >> %LAB_OUTPUT_FILE%
echo [*] 2. Users & Groups >> %LAB_OUTPUT_FILE%
net user >> %LAB_OUTPUT_FILE%
net localgroup >> %LAB_OUTPUT_FILE%
echo. >> %LAB_OUTPUT_FILE%
echo [*] 3. Privileges >> %LAB_OUTPUT_FILE%
whoami /priv >> %LAB_OUTPUT_FILE%
echo. >> %LAB_OUTPUT_FILE%
echo [*] 4. Services >> %LAB_OUTPUT_FILE%
sc query state= all >> %LAB_OUTPUT_FILE%
echo. >> %LAB_OUTPUT_FILE%
echo [*] 5. Registry >> %LAB_OUTPUT_FILE%
reg query "HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Winlogon" >> %LAB_OUTPUT_FILE%
echo. >> %LAB_OUTPUT_FILE%
echo [*] 6. Scheduled Tasks >> %LAB_OUTPUT_FILE%
schtasks /query /fo list /v >> %LAB_OUTPUT_FILE%
echo [+] Report saved to %LAB_OUTPUT_FILE%
