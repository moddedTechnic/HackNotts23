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
        self.click(55 * self.speed, self.speed)

    duty_cycle = 0.75

    def click(self, frequency: float, duration: float) -> None:
        frequency = max(frequency, 1)
        duration = max(duration, 0.1)
        period = 1 / frequency
        on_time = self.duty_cycle * period
        off_time = (1 - self.duty_cycle) * period
        for _ in range(int(duration * frequency) + 1):
            gpio.output(self.pin,gpio.HIGH)
            sleep(on_time)
            gpio.output(self.pin,gpio.LOW)
            sleep(off_time)

    def play(self):
        self.click(110,0.25)

