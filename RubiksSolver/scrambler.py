import RPi.GPIO as GPIO
import motorOutput
import time
import random

faces = list("FBRLDU")
nums = list("123")

moves = ""

#Get 50 random moves
for i in range(50):
    moves += random.choice(faces)
    moves += random.choice(nums)
    moves += " "

#motorOutput.motorSolve deletes final move because our solver has extra information in the final string
#therefore, must add a final string
moves += "(100f)"

print(moves)
motorOutput.motorSolve(moves)