#!/bin/bash
# LAB-ONLY: Hash Cracking Helper
# CEH v13 Master Module 06,07
# STRICTLY FOR AUTHORIZED LAB USE ONLY!

# -------------------------- EDIT THESE VALUES FOR YOUR LAB --------------------------
LAB_HASHES_FILE="$HOME/lab-hashes.txt"         # YOUR hashes file
LAB_WORDLIST="/usr/share/wordlists/rockyou.txt" # YOUR wordlist
LAB_HASHTYPE="0"  # 0 = MD5, 1000 = NTLM, 1400 = SHA256, 500 = MD5Crypt (see hashcat --help)
# -----------------------------------------------------------------------------------

echo "================================================"
echo "LAB-ONLY: Hash Cracking Helper"
echo "Hashes file: $LAB_HASHES_FILE"
echo "Wordlist: $LAB_WORDLIST"
echo "Hash type (hashcat mode): $LAB_HASHTYPE"
echo "================================================"
echo "1. Trying hashcat first..."
hashcat -m "$LAB_HASHTYPE" -a 0 -O "$LAB_HASHES_FILE" "$LAB_WORDLIST"
echo " "
echo "2. If hashcat didn't work, trying John the Ripper..."
john --format=raw-md5 --wordlist="$LAB_WORDLIST" "$LAB_HASHES_FILE"  # Edit format as needed
echo " "
echo "3. Showing John results..."
john --show "$LAB_HASHES_FILE"
echo "================================================"
