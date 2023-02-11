from cryptography.fernet import Fernet

def recieve_filtered_data(data):

    data_size = int(data[0:4], 16)
    key_size = int(data[4:8], 16)

    if len(data) != 8 + data_size + key_size:
        print('Fucked up')
        return

    encMsg = bytes.fromhex(data[8:data_size+8])
    key = bytes.fromhex(data[data_size+8:])

    fernet = Fernet(key)
    msg = fernet.decrypt(encMsg).decode('utf-8')

    print(msg)
    

if __name__ == '__main__':
    
    data = '00c80058674141414141426a3539574b79506949653835466e544d3438673646325a76643369586b705f50353875745149436d554333496b62735065796b5479374b635f487972363934315f5f4e45416c4764767a5f38376f3945764f6e6a38367879616c513d3d5274504f5449504643504444396b56724f4a42595a56485a586e47723958506244416935724437474245343d'

    recieve_filtered_data(data)