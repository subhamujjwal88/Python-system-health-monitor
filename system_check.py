from datetime import datetime
import platform
import os
import psutil

print("===== SYSTEM HEALTH CHECK =====")

print("Operating System:", platform.system())
print("Machine Name:", platform.node())
print("Python Version:", platform.python_version())
print("CPU Cores:", os.cpu_count())

print("\n===== RESOURCE MONITORING =====")

cpu_usage = psutil.cpu_percent(interval=1)
ram = psutil.virtual_memory()

print("CPU Usage:", cpu_usage, "%")
print("RAM Usage:", ram.percent, "%")
print("Total RAM:", round(ram.total / (1024 ** 3), 2), "GB")
print("Available RAM:", round(ram.available / (1024 ** 3), 2), "GB")

disk = psutil.disk_usage('/')

print("\n===== DISK MONITORING =====")
print("Total Disk:", round(disk.total / (1024 ** 3), 2), "GB")
print("Used Disk:", round(disk.used / (1024 ** 3), 2), "GB")
print("Free Disk:", round(disk.free / (1024 ** 3), 2), "GB")
print("Disk Usage:", disk.percent, "%")

print("\n===== SYSTEM ALERTS =====")

if cpu_usage > 80:
    print("WARNING: High CPU Usage!")
else:
    print("CPU Status: Normal")

if ram.percent > 80:
    print("WARNING: High RAM Usage!")
else:
    print("RAM Status: Normal")

if disk.percent > 80:
    print("WARNING: High Disk Usage!")
else:
    print("Disk Status: Normal")

with open("system_health.log", "a") as log:
    log.write(f"\nReport Time: {datetime.now()}\n")
    log.write(f"CPU Usage: {cpu_usage}%\n")
    log.write(f"RAM Usage: {ram.percent}%\n")
    log.write(f"Disk Usage: {disk.percent}%\n")

    log.write(f"CPU Status: {'WARNING' if cpu_usage > 80 else 'Normal'}\n")
    log.write(f"RAM Status: {'WARNING' if ram.percent > 80 else 'Normal'}\n")
    log.write(f"Disk Status: {'WARNING' if disk.percent > 80 else 'Normal'}\n")

    log.write("=" * 40 + "\n")    


print("\nSystem Check Completed!")