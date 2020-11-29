import RPi.GPIO as GPIO
import time

sensor = 16  # GPIO pin number
led = 18
button = 20

GPIO.setmode(GPIO.BOARD)
GPIO.setup(sensor, GPIO.IN)
GPIO.setup(button, GPIO.IN)
GPIO.setup(led, GPIO.OUT)

GPIO.output(led, False)
print("IR Sensor Ready.....")
print(" ")

try:
    while True:
        if GPIO.input(sensor) and GPIO.input(button):  # checks if both sensor and button output are true
            GPIO.output(led, True)
            print("Object Detected")
            while GPIO.input(sensor) and GPIO.input(button):
                time.sleep(0.2)
        else:
            GPIO.output(led, False)


except KeyboardInterrupt:
    GPIO.cleanup()
