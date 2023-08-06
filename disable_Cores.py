import os

# Disable all CPU cores except CPU0
os.system(f"echo 0 | sudo tee /sys/devices/system/cpu/online")

online_status = os.popen(f"cat /sys/devices/system/cpu/online").read().strip()
print(f"CPU online status: {online_status}")