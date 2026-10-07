#!/usr/bin/env python3
# LAB-ONLY: Cloud Infrastructure Enumeration (AWS/Azure/GCP)
# CEH v13 Ultimate Offensive Script 02
# STRICTLY FOR AUTHORIZED LAB USE ONLY!
import sys
import subprocess

# -------------------------- EDIT THESE VALUES FOR YOUR LAB --------------------------
LAB_CLOUD_PROVIDER = "AWS"  # AWS, Azure, or GCP
LAB_TARGET_ACCOUNT_ID = "123456789012"  # YOUR LAB ACCOUNT ID
LAB_REGION = "us-east-1"
# -----------------------------------------------------------------------------------

def enum_aws():
    print("[*] Enumerating AWS lab account...")
    commands = [
        "aws sts get-caller-identity",
        "aws s3 ls",
        "aws ec2 describe-instances --region " + LAB_REGION,
        "aws iam list-users",
        "aws lambda list-functions --region " + LAB_REGION
    ]
    for cmd in commands:
        print(f"\n--- Executing: {cmd} ---")
        try:
            result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
            print(result.stdout)
            if result.stderr:
                print("STDERR:", result.stderr)
        except Exception as e:
            print(f"Error: {e}")

def enum_azure():
    print("[*] Enumerating Azure lab account...")
    commands = [
        "az account show",
        "az resource list",
        "az vm list",
        "az storage account list"
    ]
    for cmd in commands:
        print(f"\n--- Executing: {cmd} ---")
        try:
            result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
            print(result.stdout)
        except Exception as e:
            print(f"Error: {e}")

def enum_gcp():
    print("[*] Enumerating GCP lab account...")
    commands = [
        "gcloud config list",
        "gcloud compute instances list",
        "gcloud storage ls",
        "gcloud iam service-accounts list"
    ]
    for cmd in commands:
        print(f"\n--- Executing: {cmd} ---")
        try:
            result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
            print(result.stdout)
        except Exception as e:
            print(f"Error: {e}")

def main():
    print("="*80)
    print("LAB-ONLY: Cloud Infrastructure Enumeration")
    print("="*80)
    print(f"[*] Provider: {LAB_CLOUD_PROVIDER}")
    print("-"*80)
    if LAB_CLOUD_PROVIDER == "AWS":
        enum_aws()
    elif LAB_CLOUD_PROVIDER == "Azure":
        enum_azure()
    elif LAB_CLOUD_PROVIDER == "GCP":
        enum_gcp()
    else:
        print("ERROR: Invalid provider! Choose AWS/Azure/GCP!")

if __name__ == "__main__":
    print("WARNING: This script is for LAB USE ONLY with your own cloud accounts!")
    main()
