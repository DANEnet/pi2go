#!/usr/bin/python
#
# Python Module to externalise all Pi2Go specific hardware
#
# Created by Gareth Davies and Zachary Igielman, May 2014
# Updated June 2014 to include Pi2Go-Lite within same framework
# Copyright 4tronix
#
# This code is in the public domain and may be freely copied and used
# No warranty is provided or implied
#
# limited to motor functions only
#
#======================================================================


#======================================================================
# General Functions
# (Both versions)
#
# init(). Initialises GPIO pins, switches motors and LEDs Off, etc
# cleanup(). Sets all motors and LEDs off and sets GPIO to standard values
# version(). Returns 1 for Full Pi2Go, and 2 for Pi2Go-Lite. Invalid until after init() has been called
#======================================================================


#======================================================================
# Motor Functions
# (Both Versions)
#
# stop(): Stops both motors
# forward(speed): Sets both motors to move forward at speed. 0 <= speed <= 100
# reverse(speed): Sets both motors to reverse at speed. 0 <= speed <= 100
# spinLeft(speed): Sets motors to turn opposite directions at speed. 0 <= speed <= 100
# spinRight(speed): Sets motors to turn opposite directions at speed. 0 <= speed <= 100
# turnForward(leftSpeed, rightSpeed): Moves forwards in an arc by setting different speeds. 0 <= leftSpeed,rightSpeed <= 100
# turnreverse(leftSpeed, rightSpeed): Moves backwards in an arc by setting different speeds. 0 <= leftSpeed,rightSpeed <= 100
# go(leftSpeed, rightSpeed): controls motors in both directions independently using different positive/negative speeds. -100<= leftSpeed,rightSpeed <= 100
# go(speed): controls motors in both directions together with positive/negative speed parameter. -100<= speed <= 100
#======================================================================


# Import all necessary libraries
import RPi.GPIO as GPIO, sys, threading, time, os
from Adafruit_PWM_Servo_Driver import PWM
from sgh_PCF8591P import sgh_PCF8591P

# Define Type of Pi2Go
PGLite = 2
PGType = PGLite # Set to None until we find out which during init()

# Pins 24, 26 Left Motor
# Pins 19, 21 Right Motor
L1 = 26
L2 = 24
R1 = 19
R2 = 21

# lineRight = 13
# lineLeft = 12

# Global variables for wheel sensor counting
running = True
countL = 0
countR = 0

#leftCount = 0
#rightCount = 0
#lastL = 0
#lastR = 0

#======================================================================
# General Functions
#
# init(). Initialises GPIO pins, switches motors and LEDs Off, etc
def init():
    global p, q, a, b, pwm, pcfADC, PGType
    # PGType = PGFull
    # Initialise the PCA9685 PWM device using the default address
    try:
        pwm = PWM(0x40, debug = False)
        pwm.setPWMFreq(60)  # Set frequency to 60 Hz
    except:
        PGType = PGLite # No PCA9685 so set to Pi2Go-Lite

    #use physical pin numbering
    GPIO.setmode(GPIO.BOARD)

    #use pwm on inputs so motors don't go too fast
    GPIO.setup(L1, GPIO.OUT)
    p = GPIO.PWM(L1, 20)
    p.start(0)

    GPIO.setup(L2, GPIO.OUT)
    q = GPIO.PWM(L2, 20)
    q.start(0)

    GPIO.setup(R1, GPIO.OUT)
    a = GPIO.PWM(R1, 20)
    a.start(0)

    GPIO.setup(R2, GPIO.OUT)
    b = GPIO.PWM(R2, 20)
    b.start(0)

    # Initalise the ADC
    pcfADC = None # ADC object
    try:
        pcfADC = sgh_PCF8591P(1) #i2c, 0x48)
    except:
        PGType = PGLite

    # initialise wheel counters if Pi2Go-Lite
    if PGType == PGLite:
        threadC = threading.Thread(target = wheelCount)
        threadC.start()
        running = True


# cleanup(). Sets all motors and LEDs off and sets GPIO to standard values
def cleanup():
    global running
    running = False
    stop()
    time.sleep(1)
    GPIO.cleanup()


# version(). Returns 1 for Full Pi2Go, and 2 for Pi2Go-Lite. Invalid until after init() has been called
def version():
    return PGType

# End of General Functions
#======================================================================


#======================================================================
# Motor Functions
# (both versions)
#
# stop(): Stops both motors
def stop():
    p.ChangeDutyCycle(0)
    q.ChangeDutyCycle(0)
    a.ChangeDutyCycle(0)
    b.ChangeDutyCycle(0)
    
# forward(speed): Sets both motors to move forward at speed. 0 <= speed <= 100
def forward(speed):
    p.ChangeDutyCycle(speed)
    q.ChangeDutyCycle(0)
    a.ChangeDutyCycle(speed)
    b.ChangeDutyCycle(0)
    p.ChangeFrequency(speed + 5)
    a.ChangeFrequency(speed + 5)
    
# reverse(speed): Sets both motors to reverse at speed. 0 <= speed <= 100
def reverse(speed):
    p.ChangeDutyCycle(0)
    q.ChangeDutyCycle(speed)
    a.ChangeDutyCycle(0)
    b.ChangeDutyCycle(speed)
    q.ChangeFrequency(speed + 5)
    b.ChangeFrequency(speed + 5)

# spinLeft(speed): Sets motors to turn opposite directions at speed. 0 <= speed <= 100
def spinLeft(speed):
    p.ChangeDutyCycle(0)
    q.ChangeDutyCycle(speed)
    a.ChangeDutyCycle(speed)
    b.ChangeDutyCycle(0)
    q.ChangeFrequency(speed + 5)
    a.ChangeFrequency(speed + 5)
    
# spinRight(speed): Sets motors to turn opposite directions at speed. 0 <= speed <= 100
def spinRight(speed):
    p.ChangeDutyCycle(speed)
    q.ChangeDutyCycle(0)
    a.ChangeDutyCycle(0)
    b.ChangeDutyCycle(speed)
    p.ChangeFrequency(speed + 5)
    b.ChangeFrequency(speed + 5)
    
# turnForward(leftSpeed, rightSpeed): Moves forwards in an arc by setting different speeds. 0 <= leftSpeed,rightSpeed <= 100
def turnForward(leftSpeed, rightSpeed):
    p.ChangeDutyCycle(leftSpeed)
    q.ChangeDutyCycle(0)
    a.ChangeDutyCycle(rightSpeed)
    b.ChangeDutyCycle(0)
    p.ChangeFrequency(leftSpeed + 5)
    a.ChangeFrequency(rightSpeed + 5)
    
# turnReverse(leftSpeed, rightSpeed): Moves backwards in an arc by setting different speeds. 0 <= leftSpeed,rightSpeed <= 100
def turnReverse(leftSpeed, rightSpeed):
    p.ChangeDutyCycle(0)
    q.ChangeDutyCycle(leftSpeed)
    a.ChangeDutyCycle(0)
    b.ChangeDutyCycle(rightSpeed)
    q.ChangeFrequency(leftSpeed + 5)
    b.ChangeFrequency(rightSpeed + 5)

# go(leftSpeed, rightSpeed): controls motors in both directions independently using different positive/negative speeds. -100<= leftSpeed,rightSpeed <= 100
def go(leftSpeed, rightSpeed):
    if leftSpeed<0:
        p.ChangeDutyCycle(0)
        q.ChangeDutyCycle(abs(leftSpeed))
        q.ChangeFrequency(abs(leftSpeed) + 5)
    else:
        q.ChangeDutyCycle(0)
        p.ChangeDutyCycle(leftSpeed)
        p.ChangeFrequency(leftSpeed + 5)
    if rightSpeed<0:
        a.ChangeDutyCycle(0)
        b.ChangeDutyCycle(abs(rightSpeed))
        p.ChangeFrequency(abs(rightSpeed) + 5)
    else:
        b.ChangeDutyCycle(0)
        a.ChangeDutyCycle(rightSpeed)
        p.ChangeFrequency(rightSpeed + 5)

# go(speed): controls motors in both directions together with positive/negative speed parameter. -100<= speed <= 100
def goBoth(speed):
    if speed<0:
        reverse(abs(speed))
    else:
        forward(speed)

# End of Motor Functions
#======================================================================


#======================================================================
# Wheel Sensor Functions
# (Pi2Go-Lite only)

def stopL():
    p.ChangeDutyCycle(0)
    q.ChangeDutyCycle(0)

def stopR():
    a.ChangeDutyCycle(0)
    b.ChangeDutyCycle(0)

def wheelCount():
    global running, countL, countR
    lastValidL = 2
    lastValidR = 2
    # lastL = GPIO.input(lineLeft)
    # lastR = GPIO.input(lineRight)
    # while running:
    # time.sleep(0.002)
    # val = GPIO.input(lineLeft)
    # if val == lastL and val != lastValidL:
    #     countL += 1
    #     lastValidL = val
    # lastL = val
    # val = GPIO.input(lineRight)
    # if val == lastR and val != lastValidR:
    #     countR += 1
    #     lastValidR = val
    # lastR = val


# stepForward(speed, steps): Moves forward specified number of counts, then stops
def stepForward(speed, counts):
    global countL, countR
    countL = 0
    countR = 0
    runL = True
    runR = True
    turnForward(speed, speed)
    while runL or runR:
        time.sleep(0.002)
        if countL >= counts:
            stopL()
            runL = False
        if countR >= counts:
            stopR()
            runR = False
            
# stepReverse(speed, steps): Moves backward specified number of counts, then stops
def stepReverse(speed, counts):
    global countL, countR
    countL = 0
    countR = 0
    runL = True
    runR = True
    turnReverse(speed, speed)
    while runL or runR:
        time.sleep(0.002)
        if countL >= counts:
            stopL()
            runL = False
        if countR >= counts:
            stopR()
            runR = False
            
# stepSpinL(speed, steps): Spins left specified number of counts, then stops
def stepSpinL(speed, counts):
    global countL, countR
    countL = 0
    countR = 0
    spinLeft(speed)
    while countL<counts or countR<counts:
        time.sleep(0.002)
        if countL >= counts:
            stopL()
        if countR >= counts:
            stopR()
            
# stepSpinR(speed, steps): Spins right specified number of counts, then stops
def stepSpinR(speed, counts):
    global countL, countR
    countL = 0
    countR = 0
    spinRight(speed)
    while countL<counts or countR<counts:
        time.sleep(0.002)
        if countL >= counts:
            stopL()
        if countR >= counts:
            stopR()



# End of Motor Functions
#======================================================================


