import RPi.GPIO as GPIO
import picamera
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(16, GPIO.IN, GPIO.PUD_UP)


button1 = 16
time_stamp = time.time()

Num = 0

camera = picamera.PiCamera()
camera.start_preview()

def button():
    global time_stamp
    global Num
    if GPIO.input(button1) == False:
        if (time.time() - time_stamp) >= 0.3:
            Num = Num + 1
            camera.capture('photos/image'+str(Num)+'.jpg')
            print "you took a picture: image"+str(Num)+".jpg"
            time_stamp = time.time()
        
try:
    while 1:
        button()
except KeyboardInterrupt:
    camera.close()

