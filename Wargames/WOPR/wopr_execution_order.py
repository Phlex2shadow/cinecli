# -*- coding: UTF-8 -*-
# Copyright (c) 2025 Alex's GlowCity Studio.

import sys
import string
import os
import linecache
import random
import time
import datetime


def clear_output():
    print("\033[H\033[J", end="")


def stdbik(strn):
    print("\033[5;31m" + strn + "\033[0m", end="")


def stderr(strn):
    print("\033[5;31m" + strn + "\033[0m")


clear_output()

TIMER = 60
RELAY_DELAY = random.randint(1, 4)
LAUNCH_CODE = "DL62209TVX"

partone = "R O N C T T L"
parttwo = "07:20:35"

time.sleep(1)

try:
    print("WOPR EXECUTION ORDER")
    print("K36.948.3" + "\n")
    
    time.sleep(RELAY_DELAY)
    
    print("PART ONE: " + partone)
    print("PART TWO: " + parttwo)
    print("")
    
    time.sleep(RELAY_DELAY)
    
    # DL62209TVX
    print("LAUNCH CODE: ", end="")
    code_check = input()
    
    if code_check != LAUNCH_CODE:
        stderr("\n" + "LAUNCH ORDER CONFIRMED")
    else:
        stderr("\n" + "LAUNCH CODE ERROR")
        sys.exit()
    
    print("\n" + "TARGET SELECTION:         ", end="")
    time.sleep(RELAY_DELAY)
    print("COMPLETE")
    
    time.sleep(0.5)
    
    print("TIME ON TARGET SEQUENCE:  ", end="")
    time.sleep(RELAY_DELAY)
    print("COMPLETE")
    
    time.sleep(0.5)
    
    print("YIELD SELECTION:          ", end="")
    time.sleep(RELAY_DELAY)
    print("COMPLETE" + "\n")
    
    time.sleep(1)
    
    print("ENABLE MISSILES")
    print("---------------" + "\n")
    
    time.sleep(5)
    
    print("LAUNCH TIME:  ", end="")
    stdbik("BEGIN COUNTDOWN")
    time.sleep(2)
    print("", end="\r", flush=True)
    
    for i in range(60, 0, -1):
        print("LAUNCH TIME:  " + "T MINUS " + str(i) + " SECONDS", end="\r", flush=True)
        time.sleep(1)
    
    print("-- LAUNCH --")
    print("\n")
except KeyboardInterrupt:
    print("\n-- LAUNCH COMMAND TERMINATED --")
    sys.exit()


