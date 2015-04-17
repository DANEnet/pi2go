#
# Python module to perform acceptance test on a newly built pi2go
# 04/04/2015 - written by Mike Ricker for DANEnet
#
#======================================================================
#
# initialize
# init(). Initialises GPIO pins, switches motors and LEDs Off, etc
#
# cleanup
# cleanup(). Sets all motors and LEDs off and sets GPIO to standard values
#

import DN_pi2go_lib as ptg

ptg.init()

# step(left wheel speed, left wheel steps, right wheel speed, right wheel steps
# go speed 90, left wheel only, for 8 steps (1 wheel revolution)
ptg.step(90,8, 0, 0)

# go speed 90, both wheels, for 8 steps (1 wheel revolution)
ptg.step(90, 8, 90, 8)

# curve to the right 90 left, 60 right, for left 40 steps right 30 steps 
ptg.step(90, 40, 60, 30)

# cleanup(). Sets all motors and LEDs off and sets GPIO to standard values
#print("cleanup")
ptg.cleanup()


