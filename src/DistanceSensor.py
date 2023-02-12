from typing import Union
import RPi.GPIO as gpio
from dataclasses import dataclass, field
from time import sleep, time
from Runnable import Runnable
from threading import Thread


SOUND_SPEED = 343

 
@dataclass
class DistanceSensor:
    tx_pin: int
    rx_pin: int

    distance: float = field(default=0, init=False)

    running: bool = field(default=False, init=False)
    thread: Union[Thread, None] = field(default=None, init=False)

    def __post_init__(self):
        gpio.setup(self.tx_pin,gpio.OUT)
        gpio.setup(self.rx_pin,gpio.IN)

    def run(self): 
        self.running = True
        self.thread = Thread(target=self.loop, args=())
        self.thread.start()

    def stop(self):
        if not self.running:
            return
        self.running = False
        assert self.thread is not None, 'Abort time machine'
        self.thread.join()

    def loop(self) -> None:
        while self.running:
            self.recalculate_distance()

    def recalculate_distance(self) -> None:
        while self.running:
            gpio.output(self.tx_pin,gpio.HIGH)
            sleep(10/10_000_000)
            gpio.output(self.tx_pin,gpio.LOW)

            while not gpio.input(self.rx_pin,gpio.LOW):
                pass
            startTime=time()
            while gpio.input(self.rx_pin,gpio.HIGH):
                pass
            stopTime=time()
            diffTime=stopTime-startTime
            self.distance = diffTime * SOUND_SPEED / 2

    def get_distance(self) -> float:
        return self.distance

