import RPi.GPIO as gpio
from dataclasses import dataclass
from time import sleep,time
from Runnable import Runnable
from threading import Thread
 
@dataclass
class DistanceSensor:

    tx_pin: int
    rx_pin: int

    Sound_Air=343
    running = False

    def __post__init(self):
        #gpio.setmode(gpio.BOARD)
        gpio.setup(self.tx_pin,gpio.OUT)
        gpio.setup(self.rx_pin,gpio.OUT)

    def run(self): 
        self.running=True
        t = Thread(target=self.get_distance,args=())
        t.start()
        t.join()

    def stop(self):
        self.running=False


    def get_distance(self) -> float:
        while self.running:
            gpio.output(self.tx_pin,gpio.HIGH)
            time.sleep(10/10_000_000)
            gpio.output(self.tx_pin,gpio.LOW)

            while not gpio.output(self.rx_pin,gpio.LOW):
                pass
            startTime=time.time()
            while gpio.output(self.rx_pin,gpio.HIGH):
                pass
            stopTime=time.time()
            diffTime=stopTime-startTime
            distance = diffTime*self.Sound_Air//2


            return distance #distance in meters