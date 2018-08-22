from gpiozero import Button, LED
from signal import pause
from time import sleep


class LedControl(object):

    def __init__(self):
        pass
    
    def run(self, repeat=1, slp=1):
        btn1 = Button(4)
        led1 = LED(17)
        led2 = LED(27)
  
        while not btn1.is_pressed:
             pass
        print("Button pressed!")
         
        for i in range(0, repeat):
            led1.on()
            led2.on()
            sleep(slp)
            led1.off()
            led2.off()
            sleep(slp)
            


if __name__ == '__main__':
    lc = LedControl()
    lc.run(7, 1)
    