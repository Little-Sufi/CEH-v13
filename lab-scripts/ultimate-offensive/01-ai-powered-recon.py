#!/usr/bin/env python3
# LAB-ONLY: AI-Powered Target Recon & Analysis
# CEH v13 Ultimate Offensive Script 01
# STRICTLY FOR AUTHORIZED LAB USE ONLY!
import sys
import json
import requests
from datetime import datetime

# -------------------------- EDIT THESE VALUES FOR YOUR LAB --------------------------
LAB_OPENAI_API_KEY = "YOUR_LAB_OPENAI_KEY_HERE"  # Use a test key for lab only!
LAB_TARGET = "192.168.100.10"  # YOUR LAB TARGET
LAB_USE_MOCK_AI = True  # Set to True if you don't have an API key (uses mock responses)
# -----------------------------------------------------------------------------------

def mock_ai_analysis(target):
    """Mock AI analysis for lab use when no API key is available"""
    return f"""
=== AI-Powered Recon Analysis for {target} ===
1. Passive OSINT: 3 subdomains found, 2 open TCP ports (22,80)
2. Vulnerability Hypothesis: Possible outdated Apache server (CVE-2021-41773)
3. Exploit Recommendation: Test path traversal payloads on port 80
4. Next Steps: Run directory brute-force, then test SQLi on login page
"""

def ai_analyze_recon(target):
    if LAB_USE_MOCK_AI:
        print("[*] Using mock AI analysis (LAB mode)")
        return mock_ai_analysis(target)
    try:
        headers = {
            "Authorization": f"Bearer {LAB_OPENAI_API_KEY}",
            "Content-Type": "application/json"
        }
        payload = {
            "model": "gpt-3.5-turbo",
            "messages": [
                {"role": "system", "content": "You are a cybersecurity expert assisting with authorized lab recon only."},
                {"role": "user", "content": f"Analyze this lab target: {target}. Provide recon analysis, vulnerability hypotheses, and exploit recommendations."}
            ]
        }
        response = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=payload, timeout=30)
        return response.json()["choices"][0]["message"]["content"]
    except Exception as e:
        return f"AI analysis failed: {e}, using mock analysis:\n{mock_ai_analysis(target)}"

def main():
    print("="*80)
    print("LAB-ONLY: AI-Powered Target Recon & Analysis")
    print("="*80)
    print(f"[*] Target: {LAB_TARGET}")
    print("-"*80)
    print("[*] Running AI analysis...")
    analysis = ai_analyze_recon(LAB_TARGET)
    print("\n" + analysis)
    print("="*80)

if __name__ == "__main__":
    # LAB validation
    if not (LAB_TARGET.startswith(("10.", "172.16.", "172.17.", "172.18.", "172.19.", "172.20.", "172.21.", "172.22.", "172.23.", "172.24.", "172.25.", "172.26.", "172.27.", "172.28.", "172.29.", "172.30.", "172.31.", "192.168.")) or LAB_TARGET in ["localhost", "127.0.0.1"]):
        print("ERROR: LAB-ONLY! Use private lab targets only!")
        sys.exit(1)
    main()
