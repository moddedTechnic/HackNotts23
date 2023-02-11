from interface import play
from cryptography.fernet import Fernet

def play_data(data, key):

    sz_data = len(data).to_bytes(2, 'big').hex()
    sz_key = len(key).to_bytes(2, 'big').hex()

    stream = sz_data + sz_key + data.hex() + key.hex()

    for n in stream:
        n = int(n, 16)
        play(n)


if __name__ == '__main__':

    msg = b'beep'
    key = Fernet.generate_key()
    fernet = Fernet(key)

    encMsg = fernet.encrypt(msg)
    
    play_data(encMsg, key)
