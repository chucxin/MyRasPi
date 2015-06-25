import picamera
import time


camera = picamera.PiCamera()

camera.capture("image.jpg")

camera.hflip = True
camera.vflip = True

camera.start_preview()
time.sleep(4)
camera.stop_preview()

