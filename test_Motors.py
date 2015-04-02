# testMotors - motors through pi2go

import testPi2Go, time
import sys
import tty
import termios

def readchar():
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    if ch == '0x03':
        raise KeyboardInterrupt
    return ch

def readkey(getchar_fn=None):
    getchar = getchar_fn or readchar
    c1 = getchar()
    if ord(c1) != 0x1b:
        return c1
    c2 = getchar()
    if ord(c2) != 0x5b:
        return c1
    c3 = getchar()
    return chr(0x10 + ord(c3) - 65)  # 16=Up, 17=Down, 18=Right, 19=Left arrows

# End of single character reading

speed = 30

testPi2Go.init()

# main loop
try:
    while True:
        keyp = readkey()
        if keyp == 'w' or ord(keyp) == 16:
            testPi2Go.forward(speed)
            print 'Forward', speed
        elif keyp == 'z' or ord(keyp) == 17:
            testPi2Go.reverse(speed)
            print 'Reverse', speed
        elif keyp == 's' or ord(keyp) == 18:
            testPi2Go.spinRight(speed)
            print 'Spin Right', speed
        elif keyp == 'a' or ord(keyp) == 19:
            testPi2Go.spinLeft(speed)
            print 'Spin Left', speed
        elif keyp == '.' or keyp == '>':
            speed = min(100, speed+10)
            print 'Speed+', speed
        elif keyp == ',' or keyp == '<':
            speed = max (0, speed-10)
            print 'Speed-', speed
        elif keyp == ' ':
            testPi2Go.stop()
            print 'Stop'
        elif ord(keyp) == 3:
            break

except KeyboardInterrupt:
    print

finally:
    testPi2Go.cleanup()
    

