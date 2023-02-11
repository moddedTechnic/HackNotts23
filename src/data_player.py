from interface import play
from cryptography.fernet import Fernet

def play_data(data, key):
    
    print(data)

    sz_data = len(data.hex()).to_bytes(2, 'big').hex()
    sz_key = len(key.hex()).to_bytes(2, 'big').hex()

    stream = sz_data + sz_key + data.hex() + key.hex()

    print(stream)

    for n in stream:
        n = int(n, 16)
        play(n)


if __name__ == '__main__':

    msg = b'beep'
    #key = Fernet.generate_key()
    key = b'RtPOTIPFCPDD9kVrOJBYZVHZXnGr9XPbDAi5rD7GBE4='
    fernet = Fernet(key)

    encMsg = fernet.encrypt(msg)
    
    play_data(encMsg, key)
