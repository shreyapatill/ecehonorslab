import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

#define some constants
CW = 1
CCW = 0
SPR = 48 #360/7.5
step_count = SPR #how many steps to turn 90 degrees
delay = 0.0208 #speeeed

#setup all pins
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

#generic spin 90 degrees, will only spin in one direction
def spin90(step, direc):
    GPIO.output(direc, CW)
    for i in range(step_count):
        GPIO.output(step, GPIO.HIGH)
        time.sleep(delay)
        GPIO.output(step, GPIO.LOW)
        time.sleep(delay)

#the code that solves it
def motorSolve(solveString):
    toSolve = solveString.split()
    toSolve = toSolve[:-1] #the last one is how many moves there are, we don't need it
    print("SOLVING: ", end = '')
    print(toSolve)

    for move in toSolve:
        print(move)
        if move[0] == "F":
            step = stepF
            direc = dirF
        if move[0] == "U":
            step = stepU
            direc = dirU
        if move[0] == "B":
            step = stepB
            direc = dirB
        if move[0] == "R":
            step = stepR
            direc = dirR
        if move[0] == "L":
            step = stepL
            direc = dirL
        if move[0] == "D":
            step = stepD
            direc = dirD
        for i in range(int(move[1])):
            spin90(step, direc)