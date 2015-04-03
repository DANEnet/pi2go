                         #!/usr/bin/python
#
# Pi2Go Demo Code using the Pi2Go library
#
# Created by Gareth Davies, May 2014
# Copyright 4tronix
#
# This code is in the public domain and may be freely copied and used
# No warranty is provided or implied
#
#======================================================================

import pi2go_lib as p2g 
import time

p2g.init()

vsn = p2g.version()
try:
    p2g.setAllLEDs(0, 0, 0)

    while True:
        light0 = p2g.getLight(0)
        light1 = p2g.getLight(1)
        light2 = p2g.getLight(2)
        light3 = p2g.getLight(3)
        print "Light sensors: ", light0, light1, light2, light3
        time.sleep(1)

except KeyboardInterrupt:
    print

finally:
    p2g.cleanup()
