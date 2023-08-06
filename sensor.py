import os
from LED_turnoff import LED_tog as LED
from Ethernet_toggle import eth_tog as ethernet
from USB_LowPower import usb_shut
from LowPower_cpu import cpu_load as cpu
from turn_offscreen import power as screen_power
from gpiozero import DistanceSensor
from time import sleep

ultrasonic = DistanceSensor(echo=17, trigger=18, max_distance=1)
trig = True
triga = True
while True:
    distance = ultrasonic.distance

    if distance < 0.1:
        print("in range")
        if trig:
            
            cpu()
            screen_power(1)
            usb_shut()
            ethernet()
            sleep(1)
            LED()
            trig = False
            triga = True
            sleep(3)
    else:
        print("out of range")
        if triga:
            screen_power(0)
            usb_shut('0')
            sleep(1)
            LED(0)
            ethernet(0)
            triga = False
            trig = True
            
            cpu(True)
            sleep(3)

    sleep(2)