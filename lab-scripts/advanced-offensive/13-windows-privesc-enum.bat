@echo off
:: LAB-ONLY: Windows Privilege Escalation Enumeration Helper
:: CEH v13 Master Module 06
:: STRICTLY FOR AUTHORIZED LAB USE ONLY!

REM -------------------------- EDIT THESE VALUES FOR YOUR LAB --------------------------
set LAB_OUTPUT_DIR=C:\Windows\Temp\lab-privesc
REM -----------------------------------------------------------------------------------

mkdir "%LAB_OUTPUT_DIR%" 2>nul
set TIMESTAMP=%date:~-4%%date:~4,2%%date:~7,2%_%time:~0,2%%time:~3,2%%time:~6,2%
set OUTFILE=%LAB_OUTPUT_DIR%\lab-privesc-enum-%TIMESTAMP%.txt

echo ================================================ >> "%OUTFILE%"
echo LAB-ONLY: Windows PrivEsc Enumeration >> "%OUTFILE%"
echo ================================================ >> "%OUTFILE%"

echo 1. System Info... >> "%OUTFILE%"
systeminfo >> "%OUTFILE%"
echo. >> "%OUTFILE%"

echo 2. Users and Groups... >> "%OUTFILE%"
net user >> "%OUTFILE%"
net localgroup administrators >> "%OUTFILE%"
echo. >> "%OUTFILE%"

echo 3. Services... >> "%OUTFILE%"
sc query state= all >> "%OUTFILE%"
echo. >> "%OUTFILE%"

echo Done! Output saved to %OUTFILE%
pause
