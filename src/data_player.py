from interface import play

def play_data(data):

    for n in data.hex():
        n = int(n, 16)
        play(n)


if __name__ == '__main__':

    msg = b'beep'
    play_data(msg)
