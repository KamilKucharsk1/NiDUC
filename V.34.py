# Scramlber V.34 with LSFR

def V34(data, dlugosc):

    import random
    from operator import xor
    data = []
    output = []
    data= open("testb.bin", "rb")


    #Potegi wielomianu 1 + x^6 + x^7
    x  = 7
    x2 = 6

    SYNC = []
    for sync in range(0,x):
        SYNC.append(random.randint(0,1))
        #print("SYNC: ",sync, SYNC)


    print("SYNC: ",SYNC)
    print("DATA:   ", data)

    length_data = dlugosc
    print("Data length: ",length_data)

    length_output = 2^length_data -1 #dlugosc klucza


    for i in range(0,length_data):

        XOR_KEY = xor(SYNC[x-1],SYNC[x-2])

        SYNC.insert(0,SYNC.pop())
        SYNC[0]=XOR_KEY
        #print(SYNC)

        output.append(xor(XOR_KEY,data[i]))

    print("output: ", output)

"""for i in range(length_output):
    output[i]=data[length_data-1]


    if data[x] != data[x2]:
        XOR = 1
    else:
        XOR = 0

    for j in data:
        data[length_data-1-j] = data[length_data-j-2]

    data[0] = XOR

    #print(i)

    print(output[i])


"""






