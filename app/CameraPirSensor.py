#!/usr/bin/python3.2

from gpiozero import LED, MotionSensor, Button
from time import sleep
from datetime import datetime
import picamera
import os
from subprocess import call


class CameraPirSensor(object):

    def __init__(self):
        self.pc = picamera.PiCamera()
        self.pir = MotionSensor(4)
        self.led1 = LED(17)
        self.btn1 = Button(27)
        self.imgCounter = 0
        self.imgCounterMax = 150
    
    def run(self):
#         btnState = False
#         while True:
#             btnState = self.btn1.is_pressed
#             if btnState:
#                 print("Button pressed!")
#                 self.picture()
#                 btnState = False

        print("Waiting for PIR to start")
        self.pir.wait_for_no_motion()
        while True:
            print("Ready")
            self.pir.wait_for_motion()
            print("Motion detected!")
            
            # Take Picture
            self.picture()
            # Take Video
            self.takeVideo()
            
            

    def picture(self):
        counterStr = self.imageCounter()
        self.pc.capture("/home/pi/workspace/gpio-pi-camera/img/img-" + counterStr + ".jpg")
#         self.led1.on()
#         sleep(1)
#         self.led1.off()
#         sleep(1)
#         self.led1.on()
#         sleep(1)
#         self.led1.off()
        
    def takeVideo(self):
        counterStr = self.imageCounter()
        videoH264 = "/home/pi/workspace/gpio-pi-camera/vid/vid-" + counterStr + ".h264"
        videoMp4 = "/home/pi/workspace/gpio-pi-camera/vid/vid-" + counterStr + ".mp4"
        self.pc.start_recording(videoH264)
        # self.pir.when_motion = self.led1.on
        # self.pir.when_no_motion = self.led1.off
        self.led1.on()
        sleep(1)
        self.led1.off()
        sleep(1)
        self.led1.on()
        sleep(1)
        self.led1.off()
        # self.pir.wait_for_no_motion()
        sleep(7)
        self.pc.stop_recording()
        # os.rename(videoH264, videoMp4)
        self.convertVideo(videoH264, videoMp4)

    def convertVideo(self, videoH264, videoMp4):
        call(["MP4Box", "-add", videoH264, videoMp4])
        call(["rm", videoH264])
        
    def imageCounter(self):
        counterStr = "0000"
        try:
            with open('/home/pi/workspace/gpio-pi-camera/app/config.cfg', 'r+') as f:
                if (self.imgCounter == 0):
                    counterStr = f.read()
                    print("counterStr - read: " + counterStr + ";")
                    self.imgCounter = 1 if (counterStr == None or counterStr == "") else int(counterStr) + (10-int(counterStr)%10) 
                else:
                    self.imgCounter = 1 if (self.imgCounter >= self.imgCounterMax) else (self.imgCounter + 1)
                
                counterStr = '{0:04d}'.format(self.imgCounter)
                print("counterStr - after: " + counterStr + ";")
                if ((self.imgCounter % 10) == 0):
                    position = f.seek(0, 0)
                    f.write(counterStr)
        except IOError as e:
            print(e)
            with open('/home/pi/workspace/gpio-pi-camera/app/config.cfg', 'w+') as f:
                f.write("0001")
            
        return counterStr
    
if __name__ == '__main__':
    c = CameraPirSensor()
    c.run()
