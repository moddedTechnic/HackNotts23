from math import sqrt
from time import sleep

try:
    import RPi.GPIO as gpio
except ImportError:
    import gpio_fallback as gpio

buzzerHigh = 40
period=0.5 / 200
gpio.setmode(gpio.BOARD)
gpio.setup(buzzerHigh, gpio.OUT)

duty_cycle = 0.1
notes = [110 * sqrt(2) ** i for i in range(16)]

def _click(frequency, duration):
    period = 1 / frequency
    on_time = duty_cycle * period
    off_time = (1 - duty_cycle) * period
    for _ in range(int(duration * frequency)):
        gpio.output(buzzerHigh,gpio.HIGH)
        sleep(on_time)
        gpio.output(buzzerHigh,gpio.LOW)
        sleep(off_time)
        

def cleanup():
    gpio.output(buzzerHigh,gpio.LOW)
    gpio.cleanup()


def play(n: int) -> None:
    """Play a tone representing the number `n`, a value from 0x0-0xF"""
    _click(notes[n], 0.25)

