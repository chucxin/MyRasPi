import picamera
import time
import PIL



camera = picamera.PiCamera()


camera.hflip = True
camera.vflip = True



camera.start_recording('photos/video.h264')
camera.wait_recording(10)
camera.stop_recording()


#for x in range(100):
#    filename = "photos/image" + str(x) + ".jpg"
#    camera.capture(filename)
#    time.sleep(1)


