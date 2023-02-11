import RPi.GPIO as gpio
from dataclasses import dataclass
from time import sleep,time
 
@dataclass
class DistanceSensor:

    tx_pin: int
    rx_pin: int

    Sound_Air=343

    def __post__init():
        #gpio.setmode(gpio.BOARD)
        gpio.setup(tx_pin,gpio.OUT)
        gpio.setup(rx_pin,gpio.OUT)


    def get_distance() -> float:
        gpio.output(tx_pin,gpio.HIGH)
        time.sleep(10/10_000_000)
        gpio.output(tx_pin,gpio.LOW)

        while not gpio.output(rx_pin,gpio.LOW):
            pass
        startTime=time.time()
        while gpio.output(rx_pin,gpio.HIGH):
            pass
        stopTime=time.time()
        diffTime=stopTime-startTime
        distance = diffTime*Sound_Air//2


        return distance #distance in meters