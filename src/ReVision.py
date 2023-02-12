import RPi.GPIO as gpio
import threading
import DistanceSensor
import Speaker

def run_aid():
    sensor = DistanceSensor.DistanceSensor(11,12)
    sensor.run()

    speaker = Speaker.Speaker(7)
    speaker.run()

    dist_range = [0.2, 1.0]
    speed_range = [0.2, 1.0]

    try:
        while True:
            speed = 0
            dist = sensor.get_distance()
            if dist < dist_range[0]:
                speed = speed_range[0]
            elif dist > dist_range[1]:
                speed = speed_range[1]
            else:
                speed = dist

            speaker.set_speed(speed)
            print(f'Speed: {speed}')
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

