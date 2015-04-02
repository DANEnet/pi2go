#
# test_m2 - test ability to recognize switch position
#

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

Lswitch = 23

GPIO.setup(Lswitch, GPIO.IN)

while True:

    value = GPIO.input(Lswitch)
    
    if value == 0:
        print "switch is OFF"
    else:
        print "switch is ON"
        
    time.sleep(1.0)

    
