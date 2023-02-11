import RPi.GPIO as gpio
from math import sqrt
from time import sleep
buzzerHigh = 40
period=0.5 / 200
#gpio.setwarnings(False)
gpio.setmode(gpio.BOARD)
gpio.setup(buzzerHigh,gpio.OUT)

duty_cycle = 0.1
notes = [110 * sqrt(2) ** i for i in range(16)]

def click(frequency, duration):
    period = 1 / frequency
    on_time = duty_cycle * period
    off_time = (1 - duty_cycle) * period
    for _ in range(int(duration * frequency)):
        gpio.output(buzzerHigh,gpio.HIGH)
        sleep(period)
        gpio.output(buzzerHigh,gpio.LOW)
        sleep(period)
        
def play(datum: int):
    click(notes[datum], 0.25)
        
for i in range(16):
    print(notes[i])
    play(i)

gpio.output(buzzerHigh,gpio.LOW)
gpio.cleanup()
