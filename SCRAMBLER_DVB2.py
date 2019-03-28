import random
from operator import xor
import numpy as np
import cv2
from PIL import Image
import struct

img=cv2.imread('samolot.jpg') # read the picture
#data = numpy.array(img)
img_str = cv2.imencode('.jpg', img)[1] # load img data as an list not array of matrixes

#img_str = numpy.array(img_str)
print("img_str_data:")
print(img_str)
print("img_str size: ", img_str.size)

#cv2.imshow('image',img)
#cv2.waitKey(30000)
#cv2.destroyAllWindows()

#data = [1,1,0,1,0,1,0,1,1,1,1,0,0,1,1,1,0,0,1,0,1,1,1,1]
output = []
output2 = []

random.seed(9001)

# 1+x^6+x^7
# X'ksy niżej to potęgi przy X'ksach wyżej, oznaczaja one ktore bity bierzemy pod uwage przy XORowaniu
x = 7
x2 = 6

output_bits = []
bit = []

# Ilosc elementow w SYNC dobieramy tak zeby pasowalo do rowaniania, np. x^6 + x^7 potrzebuje tylko 8 bitów, x^4 lub x + x^3 tylko 4 bity. One same mogą byc losowe
SYNC = [0,1,1,1,0,1,0,0] # Seed tbh

# Method for clocking the sync
def sync_clock():
    temp_val = xor(SYNC[x-1], SYNC[x2-1]) # take the 6th and 7th bit 
    SYNC.pop() # delete last element, insert new empty one at begining
    SYNC.insert(0,temp_val) # insert the result of xor
    return temp_val # return the result of xor for data encryption

# Method to convert dec -> bin
def decToBin(n):
    if n==0:
        return ''
    else:
        return decToBin(n//2) + str(n%2)

q = 1 #  temporary variable to store temp_bits as a string
w = 1 # temporary variable to store q as int
temp_bit = [0,0,0,0,0,0,0,0] # temporary array for bits

# Iterate through all array elements from img (each element represent binary number 255 - > 11111111)
for j in range(0,img_str.size):
    bit=str(decToBin(img_str[j])) # convert img_str element to binary, store as string
    # delete not needed symbols from string
    bit = bit.replace('[','')
    bit = bit.replace(']','')
    if bit=='': bit = '00000000' # if bit contains only 0, make it as 8 zeros string
    if len(bit)!=8: # if the format of binary number is wrong (not 8 bits)
       zero_lacks = 8-len(bit) # calculate difference from wanted format (8bits)
       for iterator in range(0,zero_lacks): # add that much 0 as needed at the begining of the number
           bit = '0' + bit
    print(bit)
   # Do xor operation for each of the 8 bits for current element
    for k in range(0,8):
        temp_bit[k] = xor(int(bit[k]),sync_clock()) # XOR current bit with the result of the SYNC XOR and tick the clock again

    # store the result of XOR operation to the new string
    q = str(temp_bit)
    # delete not needed symbols from string
    q = q.replace('[','')
    q = q.replace(']','')
    q = q.replace(',','')
    q = q.replace(' ','')
    print(q)
    # Store q as int
    w = int(q, 2)
    #print(w)
    # replace old element by new, encrypted element
    img_str[j] = w

print(img_str.size)

print("output: ", output)
len(img_str)


wystepowanie_11=5
wystepowanie_111=0
wystepowanie_1111=0
wystepowanie_11111=0
wystepowanie_00=0
wystepowanie_000=0
wystepowanie_0000=0
wystepowanie_00000=0

for pixel in iter(img_str.size):
    if pixel == 1:
        wystepowanie_11+=1
        print(wystepowanie_11)

print(wystepowanie_11)