# Pi2Go Motor Test
# Moves: Forward, Reverse, turn Right, turn Left, Stop - then repeat
# Press Ctrl-C to stop
#
# Also demonstrates writing to the LEDs
#
# To check wiring is correct ensure the order of movement as above is correct
# Run using: sudo python motorTest.py


import pi2go, time

pi2go.init()

# main loop

print 'Forward'
speed = 20
print speed
pi2go.forward(speed)
time.sleep(1.00)

print 'Reverse'
pi2go.reverse(speed)
time.sleep(1.00)

print 'Spin Right'
pi2go.spinRight(speed)
time.sleep(1.00)

print 'Spin Left'
pi2go.spinLeft(speed)
time.sleep(1.00)

print 'Turn Right'
pi2go.turnForward(40, 15)
time.sleep(1.00)

print 'Turn Left'
pi2go.turnForward(15, 40)
time.sleep(1.00)

print 'Reverse Right'
pi2go.turnReverse(40, 15)
time.sleep(1.00)

print 'Reverse Left'
pi2go.turnReverse(15, 40)
time.sleep(1.00)

print 'Stop'
pi2go.stop()

pi2go.cleanup()


