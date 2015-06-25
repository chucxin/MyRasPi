import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(16, GPIO.OUT)
GPIO.setup(18, GPIO.IN)



v = 343

def measure():
    GPIO.output(TRIGGER_PIN, GPIO.HIGH)
    time.sleep(0.00001)

    GPIO.output(TRIGGER_PIN, GPIO.LOW)
    pulse_start = time.time()

    while GPIO.input(ECHO_PIN) == 0:
        pulse_start = time.time()

    while GPIO.input(ECHO_PIN) == 1:
        pulse_end = time.time()

    t = pulse_end - pulse_start

    d = t * v

    d = d / 2

    return d * 100


TRIGGER_PIN = 16
ECHO_PIN = 18

while True:
    print measure()
