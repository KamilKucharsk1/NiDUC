# Scramlber V.34 with LSFR

def x25_1(data):
    import numpy as np
    import Wykresy
    import random
    from PIL import Image
    from operator import xor
    import zliczanie_sekwencji



    output = []


    #Potegi wielomianu 1 + x^18 + x^23
    x  = 25
    #random.seed(9001)

    SYNC = []
    for sync in range(0,x):
        SYNC.append(0)

    print("SYNC: ",SYNC)
    print("DATA:   ", data)

    length_data = len(data)
    print("Data length: ",length_data)

    length_output = 2^length_data -1    #dlugosc klucza


    for i in range(0,length_data):

        XOR_KEY = xor(SYNC[x - 1], data[i])

        SYNC.insert(0, SYNC.pop())
        SYNC[0] = XOR_KEY
        # print(SYNC)

        output.append(XOR_KEY)


    output=[str(i) for i in output]

    return output;



