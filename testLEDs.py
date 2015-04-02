import pi2go, time

pi2go.init()

vsn = pi2go.version()
try:
  if vsn != 1:
    print "This program only runs on the full Pi2Go"
  else:
    while True:
        pi2go.LsetAllLEDs(0, 0, 0) # start with all OFF
        for i in range(3):
            pi2go.LsetLED(i, 1) # set to On
            print 'On'
            time.sleep(0.2)
            pi2go.LsetLED(i, 0) # set to Off
    pi2go.cleanup()
            
except KeyboardInterrupt:
    pi2go.cleanup()
