#!/usr/bin/python3
from picamera import PiCamera
from time import sleep
camera=PiCamera()
camera.rotation=180
camera.resolution=(1920,1080)
camera.framerate=15
camera.start_preview()
camera.start_recording('/home/pi/Videos/video.h264')
sleep(10)
camera.stop_recording()
camera.stop_preview()
