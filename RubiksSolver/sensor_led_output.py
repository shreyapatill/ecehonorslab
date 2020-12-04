import RPi.GPIO as GPIO
import time

def waitForSafety():
    #pin numbers
    sensor = 21
    led = 18
    button = 15

    #set up all the pins
    GPIO.setmove(GPIO.BCM)
    GPIO.setup(sensor, GPIO.IN)
    GPIO.setup(button, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) #required for button usage
    GPIO.setup(led, GPIO.OUT)

    GPIO.output(led, False) #start with LED off
    print("Performing safety checks...")
    print(" ")

    while True:
        if (not GPIO.input(sensor)) and GPIO.input(button) == GPIO.HIGH:
            GPIO.output(led, True)
            print('Safety checks complete. Starting in 3s.')
            time.sleep(3)
            GPIO.cleanup()
            break
        else:
            GPIO.output(led, False)