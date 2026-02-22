import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT)

for i in range (4):
        GPIO.output(17, GPIO.HIGH)
        time.sleep(1)
        print("On")
        GPIO.output(17, GPIO.LOW)
        time.sleep(1)
        print("Off")
