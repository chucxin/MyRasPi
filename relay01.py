

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(16, GPIO.OUT, initial=1)

time.sleep(1)

GPIO.output(16, GPIO.LOW)
time.sleep(2)
GPIO.output(16, GPIO.HIGH)

GPIO.cleanup()
