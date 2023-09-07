# Raspberrypi Model 4B Low Power Mode
## This is a custom made Low Power Mode for Raspberry pi 4B. Here the code uses an ultrasonic sensor to detect a person at the front for upto 2 meters. If an object is not detected at the front the Raspberry PI 4B shifts to this low power mode.
## On the other hand, if detected the Raspberry pi will turn back on with every functionality enabled!**This is work in Progress!**

- It caps CPU Frequencies to the lowest Possible Safe Frequencies of 600 MHZ.
- It Also uses some basic methods like disabling USB Bus to disabling LED interface to reduce Power!
- To decrease Power even further you can disable other CPUs hence allowing a single CPU to run only! _This code Assumes that (Raspberry pi does not allow disabling CPUs without restart)_
- **_Please feel free to contribute_**
- **lets make a _Low Power Mode for Raspberry Pi_ a reality!**
