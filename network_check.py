import psutil
import platform
from datetime import datetime

print("=" * 40)
print("       NETWORK MONITORING")
print("=" * 40)

# System Information
print("\n===== SYSTEM INFORMATION =====")
print("Operating System:", platform.system())
print("Machine Name:", platform.node())

# Network Statistics
network = psutil.net_io_counters()

sent = network.bytes_sent / (1024 ** 2)
received = network.bytes_recv / (1024 ** 2)

print("\n===== NETWORK STATISTICS =====")
print("Data Sent:", round(sent, 2), "MB")
print("Data Received:", round(received, 2), "MB")
print("Total Data:", round(sent + received, 2), "MB")

# Network Interfaces
print("\n===== NETWORK INTERFACES =====")

interfaces = psutil.net_if_addrs()

for interface, addresses in interfaces.items():
    print("\nInterface:", interface)

    for address in addresses:
        if address.family == 2:
            print("IPv4 Address:", address.address)

# Network Status
stats = psutil.net_if_stats()

print("\n===== NETWORK STATUS =====")

for interface, status in stats.items():
    print(interface, ":", "UP" if status.isup else "DOWN")

# Report Time
print("\nReport Time:", datetime.now())
print("\nNetwork Check Completed!")
print("=" * 40)