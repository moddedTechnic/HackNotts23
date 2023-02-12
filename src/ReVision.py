import RPi.GPIO as gpio
import threading
import time
import DistanceSensor
import Speaker


def interpolate(t: float, t_min: float, t_max: float, x_min: float, x_max: float):
    return x_min + (x_max - x_min) * (t - t_min) / (t_max - t_min)


def run_aid():
    sensor = DistanceSensor.DistanceSensor(11,12)
    sensor.run()

    speaker = Speaker.Speaker(13)
    speaker.run()

    dist_range = [0.2, 1.0]
    speed_range = [1.0, 0]

    try:
        while True:
            speed = 0
            dist = sensor.get_distance()
            # print(dist)
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
        sensor.stop()


def run():
    gpio.setmode(gpio.BOARD)
    gpio.setwarnings(False)

    #create 2 speaker threads
    aid1 = threading.Thread(target=run_aid)
    #aid2 = threading.Thread(target=run_aid)

    aid1.start()
    #aid2.start()

if __name__ == '__main__':
    run()

