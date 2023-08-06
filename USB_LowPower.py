import subprocess
def usb_shut(usb_power = '1'):
    # Execute the uhubctl command to disable all USB ports
    subprocess.run(['sudo', 'uhubctl', '-l', '1-1', '-a', usb_power])
