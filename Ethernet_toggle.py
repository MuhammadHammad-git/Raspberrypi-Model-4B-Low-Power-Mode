import os

def eth_tog(toggle=1):
    if toggle == 1:
        # Enable the Ethernet interface
        os.system('sudo ifconfig eth0 up')
    else:
        # Disable the Ethernet interface
        os.system('sudo ifconfig eth0 down')