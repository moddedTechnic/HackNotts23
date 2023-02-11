from dataclasses import dataclass, field

import RPi.GPIO as gpio


@dataclass
class Speaker:
    pin: int
    speed: float = field(default=0, init=False)
    running: bool = False

    def __post_init__(self) -> None:
        gpio.setup(self.pin, gpio.OUT)

    def set_speed(self, speed: float) -> None:
        self.speed = speed

    def run(self) -> None:
        self.running = True

    def stop(self) -> None:
        self.running = False

    def loop(self) -> None:
        while self.running:
            self.buzz()

    def buzz(self) -> None:
        raise NotImplemented()

