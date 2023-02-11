from time import time

from interface import play
from cryptography.fernet import Fernet

def play_data(data, key):
    
    data = bytes(data, 'utf-8')
    key = bytes(key, 'utf-8')

    sz_data = len(data.hex()).to_bytes(2, 'big').hex()
    sz_key = len(key.hex()).to_bytes(2, 'big').hex()

    stream = sz_data + sz_key + data.hex() + key.hex()

    sec = len(stream)*0.25*1.2837
    print(f"Message is estimated to take {sec:0.2f} seconds")

    start = time()
    for n in stream:
        n = int(n, 16)
        play(n)
    end = time()
    print(f'Time taken {(end - start):0.2f}s')


#if __name__ == '__main__':

    msg = b'1a'
    key = Fernet.generate_key()
    key = b'RtPOTIPFCPDD9kVrOJBYZVHZXnGr9XPbDAi5rD7GBE4='
    fernet = Fernet(key)

    encMsg = fernet.encrypt(msg)
    play_data(encMsg, key)

