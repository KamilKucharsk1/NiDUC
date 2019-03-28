# Scramlber V.34 with LSFR

def V_34_descrambler(data):
    import numpy as np
    import Wykresy
    import random
    from PIL import Image
    from operator import xor
    import zliczanie_sekwencji



    output = []


    #Potegi wielomianu 1 + x^18 + x^23
    x  = 23
    x2 = 18
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

        XOR_KEY = xor(SYNC[x - 1], SYNC[x2-1])

        XOR2_KEY = xor(data[i], XOR_KEY)
        SYNC.insert(0, SYNC.pop())
        SYNC[0] = data[i]
        # print(SYNC)

        output.append(XOR2_KEY)


    output=[str(i) for i in output]

    return output;



