from dataclasses import dataclass, field
from threading import Thread
from time import sleep
from typing import Union

import RPi.GPIO as gpio

from Runnable import Runnable


@dataclass
class Speaker(Runnable):
    pin: int
    speed: float = field(default=0, init=False)
    running: bool = field(default=False, init=False)
    thread: Union[Thread, None] = field(default=None, init=False)

    def __post_init__(self) -> None:
        gpio.setup(self.pin, gpio.OUT)

    def set_speed(self, speed: float) -> None:
        self.speed = speed

    def run(self) -> None:
        self.running = True
        self.thread = Thread(target=self.loop, args=())
        self.thread.start()

    def stop(self) -> None:
        if not self.running:
            return
        self.running = False
        assert self.thread is not None, "Abort time machine"
        self.thread.join()

    def loop(self) -> None:
        while self.running:
            self.buzz()

    def buzz(self) -> None:
        gpio.output(self.pin, gpio.HIGH)
        sleep(self.speed / 2)
        gpio.output(self.pin, gpio.LOW)
        sleep(self.speed / 2)

