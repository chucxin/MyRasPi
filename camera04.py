import RPi.GPIO as GPIO
import picamera
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(16, GPIO.IN, GPIO.PUD_UP)


button1 = 16
buttonState = 0

time_stamp = time.time()

Num = 0

camera = picamera.PiCamera()
camera.start_preview()


def recording(pin):
    global Num
    global buttonState
    if buttonState == 0:
        Num = Num + 1
        camera.start_recording('video' + str(Num) + '.h264')
        print "Recording..."
        buttonState = 1
    elif buttonState == 1:
        camera.stop_recording()
        print 'Video: video' + str(Num) + '.h264'
        buttonState = 0

GPIO.add_event_detect(button1, GPIO.FALLING, recording, 200)


try:
    while 1:
        pass
except KeyboardInterrupt:
    camera.close()

