#!/usr/bin/env python
#Simply prints the state of the line follower sensors

# Must be run as root - sudo python .py 

import time, 
import pi2go_lib as p2g

p2g.init()

vsn = p2g.version()
if vsn == 1:
  print "Running on Pi2Go"
else:
  print "Running on Pi2Go-Lite"


try:
    while True:
        print 'Left:', p2g.irLeftLine()
        print 'Right:', p2g.irRightLine()
        print
        time.sleep(1)
                          
except KeyboardInterrupt:
    print

finally:
    p2g.cleanup()
