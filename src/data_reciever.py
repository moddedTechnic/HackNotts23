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
    
    data = '00c80058674141414141426a35383869305a444976424157435f6b74783030765f5a686c4b6753774a3474494a36383162784148334e63553763394d777065656f31687a6a68744a6957764649324b364a7a6265596c542d4f6870563339737a57414b7051413d3d4433576f664b654e793434776a632d4241526775304c6a5056494f365a614f53526a6178374f4371534a773d'

    recieve_filtered_data(data)