import RPi.GPIO as GPIO
import picamera
import time

Num = 0

GPIO.setmode(GPIO.BOARD)
GPIO.setup(16, GPIO.IN, GPIO.PUD_UP)


def capture(pin):
    global Num
    Num = Num + 1
    camera.capture('photos/image'+str(Num)+'.jpg')
    print "take a pic"

GPIO.add_event_detect(16, GPIO.FALLING, capture, 200)



camera = picamera.PiCamera()

camera.start_preview()

try:
    while 1:
        pass
except KeyboardInterrupt:
    camera.close()

