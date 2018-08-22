from gpiozero import LED, MotionSensor
from time import sleep



class PirSensor(object):

    def __init__(self):
        pass
        
    def run(self):
        led1 = LED(17)
        pir = MotionSensor(4)
        
        print("Waiting for PIR to start")
        pir.wait_for_no_motion()
        
        while True:
            print("Ready")
            pir.wait_for_motion()
            print("Motion detected!")
            led1.on()
            sleep(1)
            led1.off()
            sleep(1)
            led1.on()
            sleep(1)
            led1.off()
        

if __name__ == '__main__':
    pir = PirSensor()
    pir.run()