# -*- coding: UTF-8 -*-
# Copyright (c) 2025 Alex's GlowCity Studio.

import sys
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

RELAY_DELAY = random.randint(1, 3)
LAUNCH_CODE = "CPE1704TKS"

partone = "V E H S J J B"
parttwo = "19:37:42"

try:
    print("PART ONE: " + partone)
    print("PART TWO: " + parttwo)
    print("")

    time.sleep(1)

    stdbik("MISSILES ENABLED" + "\n")
    stdbik("----------------" + "\n\n")

    time.sleep(1)

    print("TARGET SELECTION:         ", end="")
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

    print("C H A N G E S   L O C K E D   O U T")
    print("-----------------------------------" + "\n")

    print("LAUNCH TIME: ", end="")
    stdbik(">> AWAITING CODES <<")
    print("\n\n\n\n\n")

    time.sleep(10)
except KeyboardInterrupt:
    print("\n-- LAUNCH COMMAND TERMINATED --")
    sys.exit()
