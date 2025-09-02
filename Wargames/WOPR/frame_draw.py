# -*- coding: UTF-8 -*-
# Copyright 2025 (c) Alex's GlowCity Studio.


import sys
import os
import random
import time
import datetime


# ┏━━━┓
# ┃   ┃
# ┗━━━┛
cursor_x = 0
cursor_y = 0

columns, lines = 0, 0
columns, lines = shutil.get_terminal_size()
columns = int(os.getenv("COLUMNS", columns))
lines = int(os.getenv("LINES", lines))

if columns < 80 or lines < 24:
    print("警告: 终端大小至少为 80 x 24，当前尺寸为", columns, "x", lines)
    sys.exit(1)

is_draw_end = False


def sigint_handler(sig, frame):
    endDraw()
    sys.exit(0)


signal.signal(signal.SIGINT, sigint_handler)


width = columns - 4
height = lines - 2


def clear(mutex=True):
    global cursor_x, cursor_y
    cursor_x = 1
    cursor_y = 1
    print("\033[2J", end="")


def move(x, y, update_cursor=True, mutex=True):
    global cursor_x, cursor_y
    print("\033[%d;%dH" % (y, x), end="")
    sys.stdout.flush()
    if update_cursor:
        cursor_x = x
        cursor_y = y


def endDraw():
    global is_draw_end
    is_draw_end = True
    clear(False)
    move(1, 1, False, False)


def drawFrame():
    move(1, 1)
    print("┏" + "━" * width + "┓")
    for _ in range(height - 2):
        print("┃" + " " * width + "┃")
    print("┗" + "━" * width + "┛")
    move(2, 2)
    sys.stdout.flush()
    time.sleep(3)


clear()
drawFrame()
move(2, 2)
endDraw()

