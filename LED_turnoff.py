import os

def LED_tog(Tog = 1):
    # Turn off the power LED
    os.system(f'echo {Tog} | sudo tee /sys/class/leds/PWR/brightness')