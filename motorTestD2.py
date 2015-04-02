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
time.sleep(30.0)
print 'Forward'
for speed in range(40, 10, -5):
    pi2go.forward(speed)
    print speed
    time.sleep(3.000)

print 'Reverse'
for speed in range(30, 15, -5):
    pi2go.reverse(speed)
    print speed
    time.sleep(3.000)

print 'Spin Right'
for speed in range(30, 15, -5):
    pi2go.spinRight(speed)
    print speed
    time.sleep(3.000)

print 'Spin Left'
for speed in range(30, 15, -5):
    pi2go.spinLeft(speed)
    print speed
    time.sleep(3.000)

print 'Stop'
pi2go.stop()

