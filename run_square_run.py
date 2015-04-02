# Pi2Go Motor Test
# Moves: Forward, Reverse, turn Right, turn Left, Stop - then repeat
# Press Ctrl-C to stop
#
# Also demonstrates writing to the LEDs
#
# To check wiring is correct ensure the order of movement as above is correct
# Run using: sudo python motorTest.py


#from pi2go_functions import pi2go
import pi2go_functions
import time
import sys

pi2go_functions.init()

# main loop
time.sleep(10.0)

pi2go_functions.turnForward(40,38)
time.sleep(5.000)

pi2go_functions.spinLeft(30)
time.sleep(2.000)

print 'Stop'
pi2go_functions.stop()
time.sleep (2.0)


pi2go_functions.turnForward(40,38)
time.sleep(5.000)

pi2go_functions.spinLeft(30)
time.sleep(5.000)

print 'Stop'
pi2go_functions.stop()
time.sleep (2.0)


pi2go_functions.turnForward(40,38)
time.sleep(5.000)


pi2go_functions.spinLeft(30)
time.sleep(5.000)

print 'Stop'
pi2go_functions.stop()
time.sleep (2.0)


pi2go_functions.turnForward(40,38)
time.sleep(5.000)

print 'Stop'
pi2go_functions.stop()
time.sleep (2.0)

pi2go_functions.spinRight(30)
time.sleep(5.000)

pi2go_functions.turnForward(40,38)
time.sleep(5.000)

pi2go_functions.stop()
sys.exit()

