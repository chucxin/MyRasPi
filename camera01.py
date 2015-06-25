import picamera
import time


camera = picamera.PiCamera()

camera.start_recording('photos/video.h264')
time.sleep(5)
camera.stop_recording()


#for x in range(100):
#    filename = "photos/image" + str(x) + ".jpg"
#    camera.capture(filename)
#    time.sleep(1)

camera.hflip = True
camera.vflip = True

