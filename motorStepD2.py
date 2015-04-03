# Pi2Go Motor Test
# Moves: Forward, Reverse, turn Right, turn Left, Stop - then repeat
# Press Ctrl-C to stop
#
# Also demonstrates writing to the LEDs
#
# To check wiring is correct ensure the order of movement as above is correct
# Run using: sudo python motorTest.py


import pi2go as p2g 
import time

p2g.init()

# main loop

print 'Forward'
speed = 20
print speed
p2g.forward(speed)
time.sleep(1.00)

print 'Reverse'
p2g.reverse(speed)
time.sleep(1.00)

print 'Spin Right'
p2g.spinRight(speed)
time.sleep(1.00)

print 'Spin Left'
p2g.spinLeft(speed)
time.sleep(1.00)

print 'Turn Right'
p2g.turnForward(40, 15)
time.sleep(1.00)

print 'Turn Left'
p2g.turnForward(15, 40)
time.sleep(1.00)

print 'Reverse Right'
p2g.turnReverse(40, 15)
time.sleep(1.00)

print 'Reverse Left'
p2g.turnReverse(15, 40)
time.sleep(1.00)

print 'Stop'
p2g.stop()

p2g.cleanup()


