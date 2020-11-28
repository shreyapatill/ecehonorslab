import RPi.GPIO as GPIO
import time

#define some constants
CW = 1
CCW = 0
SPR = 50 #value found by testing
step_count = SPR
delay = 0.0058 #speeeed

def motorSolve(solveString):
    #input: a string of the moves to perform
    #parses string and executes the moves

    GPIO.setmode(GPIO.BCM)

    #sets up all the pins
    stepF = 2
    dirF = 3
    GPIO.setup(stepF, GPIO.OUT)
    GPIO.setup(dirF, GPIO.OUT)

    stepR = 17
    dirR = 27
    GPIO.setup(stepR, GPIO.OUT)
    GPIO.setup(dirR, GPIO.OUT)

    stepB = 10
    dirB = 22
    GPIO.setup(stepB, GPIO.OUT)
    GPIO.setup(dirB, GPIO.OUT)

    stepL = 5
    dirL = 6
    GPIO.setup(stepL, GPIO.OUT)
    GPIO.setup(dirL, GPIO.OUT)

    stepD = 19
    dirD = 26
    GPIO.setup(stepD, GPIO.OUT)
    GPIO.setup(dirD, GPIO.OUT)

    stepU = 16
    dirU = 20
    GPIO.setup(stepU, GPIO.OUT)
    GPIO.setup(dirU, GPIO.OUT)

    #parse input
    toSolve = solveString.split()
    toSolve = toSolve[:-1] #the last one is how many moves there are, we don't need it
    #print("SOLVING: ", end = '')
    #print(toSolve)

    #moves
    for move in toSolve: #move format: F1, F is face to move, 1 is how many 90 degree turns to make
        #print(move)
        step_count = 50
        #step counts are hard coded because sometimes the faces act weird and must be calibrated individually
        #clock also hard coded because in the future we can change it easier
        if move[0] == "F":
            step = stepF
            direc = dirF
            clock = CCW
            step_count = 50
        if move[0] == "U":
            step = stepU
            direc = dirU
            clock = CCW
            step_count = 50
        if move[0] == "B":
            step = stepB
            direc = dirB
            clock = CCW
            step_count = 50
        if move[0] == "R":
            step = stepR
            direc = dirR
            clock = CCW
            step_count = 50
        if move[0] == "L":
            step = stepL
            direc = dirL
            clock = CCW
            step_count = 50
        if move[0] == "D":
            step = stepD
            direc = dirD
            clock = CCW
            step_count = 50
        for i in range(int(move[1])):
            GPIO.output(direc, clock)
            #spins the motor 90 degrees
            for j in range(step_count):
                GPIO.ouput(step, GPIO.HIGH)
                time.sleep(delay)
                GPIO.output(step, GPIO.LOW)
                time.sleep(delay)

GPIO.cleanup()