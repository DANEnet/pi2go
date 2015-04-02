#
# test_m1 - test ability to set LEDs on and off
#

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

frontLED = 15
backLED = 16

value = 0

GPIO.setup(frontLED, GPIO.OUT)
GPIO.setup(backLED, GPIO.OUT)

while True:
    value = 1 - value

    if value == 0:
        print "set LED to off"
    else:
        print "set LED to on"
        
    GPIO.output(frontLED, value)
    GPIO.output(backLED, value)

    time.sleep(1.0)

    
