import platform
import psutil
import time
import subprocess
import cpuinfo

def fetch():
    # get CPU
    cpu_model = cpuinfo.get_cpu_info() or "Unknown CPU, or cpuinfo is not installed"

    # uptime
    boot_time = psutil.boot_time()
    uptime_seconds = time.time() - boot_time
    days, rem = divmod(uptime_seconds, 86400)
    hours, rem = divmod(rem, 3600)
    minutes, _ = divmod(rem, 60)
    uptime_str = f"{int(days)}d {int(hours)}h {int(minutes)}m"

    # get GPU
    gpu_model = "Unknown GPU"
    system = platform.system()
    try:
        if system == "Windows":
            output = subprocess.check_output(
                "wmic path win32_VideoController get Name",
                shell=True
            ).decode(errors="ignore").splitlines()
            gpus = [line.strip() for line in output if line.strip() and "Name" not in line]
            if gpus:
                gpu_model = ", ".join(gpus)
        elif system == "Linux":
            output = subprocess.check_output(
                "lspci | grep -i vga",
                shell=True
            ).decode(errors="ignore").strip()
            if output:
                gpu_model = output.split(":", 1)[-1].strip()
        elif system == "Darwin":
            output = subprocess.check_output(
                "system_profiler SPDisplaysDataType | grep 'Chipset Model'",
                shell=True
            ).decode(errors="ignore").strip()
            if output:
                gpu_model = output.split(":")[-1].strip()
    except Exception:
        pass

    # memory and disk
    mem = psutil.virtual_memory()
    memory_str = f"{mem.used // (1024**2)}MB / {mem.total // (1024**2)}MB"

    partitions = psutil.disk_partitions()
    disks = [p.device for p in partitions]
    disks_str = ", ".join(disks)

    # output
    print("==MythFetch=======================================")
    print(f"OS:     Myth 3.14.0 {cpu_model['arch']}")
    print(f"CPU:    {cpu_model['brand_raw']}")
    print(f"Uptime: {uptime_str}")
    print(f"GPU:    {gpu_model}")
    print(f"Memory: {memory_str}")
    print(f"Disks:  {disks_str}")
