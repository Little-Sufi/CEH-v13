#!/usr/bin/env python3
# LAB-ONLY: DLL Hijacking Discovery Helper
# CEH v13 Master Module 06
# STRICTLY FOR AUTHORIZED LAB USE ONLY!
# DETAILED EXPLANATION: Finds writable directories in PATH and generates DLL hijacking candidates
import os
import sys
import platform

# -------------------------- EDIT THESE VALUES FOR YOUR LAB --------------------------
LAB_TARGET_DLL_NAME = "mydll.dll"
LAB_PAYLOAD_DLL_PATH = "payload.dll"  # Your malicious DLL path
# -----------------------------------------------------------------------------------

def find_writable_path_dirs():
    print("="*80)
    print("LAB-ONLY: DLL Hijacking Helper")
    print("="*80)
    path_dirs = os.environ["PATH"].split(os.pathsep)
    writable = []
    for d in path_dirs:
        if not os.path.exists(d):
            continue
        try:
            test_file = os.path.join(d, "test.tmp")
            open(test_file, "w").close()
            os.remove(test_file)
            writable.append(d)
            print(f"✅ Writable: {d}")
        except:
            pass
    print()
    if writable:
        print("Suggest placing payload DLL here and naming it a DLL the target app tries to load!")

if __name__ == "__main__":
    if platform.system() != "Windows":
        print("ERROR: This is for Windows targets (LAB ONLY!)")
        sys.exit(1)
    find_writable_path_dirs()
