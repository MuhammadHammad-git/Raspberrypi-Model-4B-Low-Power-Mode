import os
import time

def cpu_load(throttle=False):
    if throttle:
        initial_freq = os.popen("cat /sys/devices/system/cpu/cpu0/cpufreq/scaling_cur_freq").read().strip()
            # Update the cpufrequtils configuration file to use the powersave governor
        with open('/etc/default/cpufrequtils', 'a') as file:
            file.write('GOVERNOR="powersave"\n')

        # Restart the cpufrequtils service
        os.system('sudo systemctl restart cpufrequtils')
        # Get the CPU frequency


        # Set the desired CPU frequency (600MHz)
        os.system("echo 600000 > /sys/devices/system/cpu/cpu0/cpufreq/scaling_min_freq")
        os.system("echo 600000 > /sys/devices/system/cpu/cpu0/cpufreq/scaling_max_freq")

        # Wait for the new frequency to take effect
        time.sleep(2)

        # Check the current CPU frequency
        current_freq = os.popen("cat /sys/devices/system/cpu/cpu0/cpufreq/scaling_cur_freq").read().strip()
        print("Initial frequency:", initial_freq)
        print("Current frequency:", current_freq)


    else:
                # Get the CPU frequency
        initial_freq = os.popen("cat /sys/devices/system/cpu/cpu0/cpufreq/scaling_cur_freq").read().strip()
                # Update the cpufrequtils configuration file to use the powersave governor
        with open('/etc/default/cpufrequtils', 'a') as file:
            file.write('GOVERNOR="ondemand"\n')

        # Restart the cpufrequtils service
        os.system('sudo systemctl restart cpufrequtils')


        # Set the default CPU frequency (1.5 GHz)
        os.system("echo 600000 > /sys/devices/system/cpu/cpu0/cpufreq/scaling_min_freq")
        os.system("echo 1500000 > /sys/devices/system/cpu/cpu0/cpufreq/scaling_max_freq")

        # Wait for the new frequency to take effect
        time.sleep(2)

        # Check the current CPU frequency
        current_freq = os.popen("cat /sys/devices/system/cpu/cpu0/cpufreq/scaling_cur_freq").read().strip()
        print("Initial frequency:", initial_freq)
        print("Current frequency:", current_freq)