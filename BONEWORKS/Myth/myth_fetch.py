# -*- coding: utf-8 -*-
# Copyright (c) 2025 Alex's GlowCity Studio.

import platform
import psutil
import time
from datetime import datetime, timedelta
import subprocess
import cpuinfo


def fetch():
    cpu_model = cpuinfo.get_cpu_info() or "Unknown CPU, or cpuinfo is not installed"

    boot_time = psutil.boot_time()
    uptime_seconds = time.time() - boot_time
    uptime_timedelta = timedelta(seconds=uptime_seconds)
    days = uptime_timedelta.days
    hours, remainder = divmod(uptime_timedelta.seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    uptime = f"{days} days, {hours:02} hours, {minutes:02} mins"

    mem = psutil.virtual_memory()
    total = round(mem.total / (1024**2), 2)
    available = round(mem.available / (1024**2), 2)
    used = round(mem.used / (1024**2), 2)

    fetch_output = f"""OS:     Myth {platform.python_version()} {cpu_model["arch"]}
CPU:    {cpu_model["brand_raw"]}
Uptime: {uptime}
Memory: {used}MB / {total}MB"""

    lines = fetch_output.splitlines()
    max_length = 0
    for line in lines:
        current_length = len(line)
        if current_length > max_length:
            max_length = current_length

    print("==Mythfetch" + ("=" * (max_length - 11)))
    print(fetch_output)
