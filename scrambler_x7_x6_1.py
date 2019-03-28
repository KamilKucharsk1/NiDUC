

import random
from operator import xor

#cv2.imread(drzewo.png)
data = [1,1,0,1,0,1,0,1,1,1,1,0,0,1,1,1,0,0,1,0,1,1,1,1]
output = []
output2 = []

random.seed(9001)

zeros=0
ones=0
zeros2=0
ones2=0

#Potegi wielomianu 1 + x^6 + x^7
x  = 7
x2 = 6

SYNC = []
for sync in range(0,x):
    SYNC.append(random.randint(0,1))
    #print("SYNC: ",sync, SYNC)

SEED = [1,1,1,1,1,1,1]
print("SYNC: ",SYNC)
print("DATA:         ", data)

length_data = int(len(data))
print("Data length: ",length_data)

#length_output = 2^length_data -1 #dlugosc klucza


for i in range(0,length_data):

    XOR_KEY = xor(SYNC[x-1],SYNC[x-2])

    SYNC.insert(0,SYNC.pop())
    SYNC[0]=XOR_KEY
    #print(SYNC)

    output.append(xor(XOR_KEY,data[i]))
    if output[i] == 0:
        zeros=zeros+1
    else:
        ones=ones+1


print("output:       ", output)



for i in range(0,length_data):
    XOR_KEY = xor(SEED[x-1],SEED[x-2])

    SEED.insert(0,SEED.pop())
    SEED[0]=XOR_KEY

    output2.append(xor(XOR_KEY,data[i]))
    if output2[i] == 0:
        zeros2=zeros2+1
    else:
        ones2=ones2+1

print("output(seed): ", output2)
print("(with random) zeros: ", zeros,"ones: ", ones)
print("(with seed)   zeros: ", zeros2,"ones: ", ones2)


