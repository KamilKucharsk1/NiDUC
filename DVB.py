import random
from operator import xor

def dvb(data):

    output = []
    # Potegi wielomianu 1 + x^6 + x^7
    x = 15
    x2 = 14
    random.seed(9001)

    SYNC = []
    for sync in range(0, x):
        SYNC.append(random.randint(0, 1))

    print("SYNC: ", SYNC)
    print("DATA:   ", data)

    length_data = len(data)
    print("Data length: ", length_data)

    length_output = 2 ^ length_data - 1  # dlugosc klucza

    for i in range(0, length_data):
        XOR_KEY = xor(SYNC[x - 1], SYNC[x2 - 1])

        SYNC.insert(0, SYNC.pop())
        SYNC[0] = XOR_KEY

        # print(SYNC)

        output.append(xor(XOR_KEY, data[i]))

    output = [str(i) for i in output]

    print("Po scramblingu: ", output)
    return output