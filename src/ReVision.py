import RPi.GPIO as gpio
import threading
import time
from DistanceSensor import DistanceSensor
from Speaker import Speaker


def interpolate(t: float, t_min: float, t_max: float, x_min: float, x_max: float):
    return x_min + (x_max - x_min) * (t - t_min) / (t_max - t_min)


def run_aid(distance_sensor: DistanceSensor, speaker: Speaker):
    distance_sensor.run()
    speaker.run()

    dist_range = [0.2, 1.0]
    speed_range = [1.0, 0]

    try:
        while True:
            speed = 0
            dist = distance_sensor.get_distance()
            if dist < dist_range[0]:
                speed = speed_range[0]
            elif dist > dist_range[1]:
                speed = speed_range[1]
            else:
                speed = interpolate(dist, *dist_range, *speed_range)

            speaker.set_speed(speed)
            time.sleep(1/60)
    except KeyboardInterrupt:
        speaker.stop()
        distance_sensor.stop()


def run():
    gpio.setmode(gpio.BOARD)
    gpio.setwarnings(False)

    #create 2 speaker threads
    aid1 = threading.Thread(target=run_aid, args=(DistanceSensor(11, 12), Speaker(13)))
    aid2 = threading.Thread(target=run_aid, args=(DistanceSensor(15, 16), Speaker(29)))

    aid1.start()
    aid2.start()


if __name__ == '__main__':
    run()

