# Pi2Go Motor Test
# Moves: Forward, Reverse, turn Right, turn Left, Stop - then repeat
# Press Ctrl-C to stop
#
# Also demonstrates writing to the LEDs
#
# To check wiring is correct ensure the order of movement as above is correct
# Run using: sudo python motorTest.py


#from pi2go_functions import pi2go
import pi2go_lib as p2g
import time
import sys

p2g.init()

# main loop
time.sleep(10.0)

p2g.turnForward(40,38)
time.sleep(5.000)

p2g.spinLeft(30)
time.sleep(2.000)

print 'Stop'
p2g.stop()
time.sleep (2.0)


p2g.turnForward(40,38)
time.sleep(5.000)

p2g.spinLeft(30)
time.sleep(5.000)

print 'Stop'
p2g.stop()
time.sleep (2.0)


p2g.turnForward(40,38)
time.sleep(5.000)


p2g.spinLeft(30)
time.sleep(5.000)

print 'Stop'
p2g.stop()
time.sleep (2.0)


p2g.turnForward(40,38)
time.sleep(5.000)

print 'Stop'
p2g.stop()
time.sleep (2.0)

p2g.spinRight(30)
time.sleep(5.000)

p2g.turnForward(40,38)
time.sleep(5.000)

p2g.stop()
sys.exit()

