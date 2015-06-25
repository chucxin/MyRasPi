import picamera
import time


camera = picamera.PiCamera()

camera.capture("photos/image.jpg")

camera.hflip = True
camera.vflip = True

camera.start_preview()
time.sleep(30)
camera.stop_preview()

