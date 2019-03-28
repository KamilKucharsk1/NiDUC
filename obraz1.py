import numpy
import numpy as np
import PIL
from PIL import Image
import cv2
import random
from operator import xor

img = PIL.Image.open("samolot.jpg").convert('1')    #ladowanie obrazu
imgarr = numpy.array(img)
im_g=cv2.imread("samolot.jpg",0)

f = open("testb.txt", "wb")
f.writelines(imgarr)
pilimg = Image.fromarray(imgarr)

licznik_calosci=0
licznik_0=0
licznik_1=0
for pixel in iter(img.getdata()):                   #zamiana 255 na 1 oraz wypisanie DATA
    if pixel == 255:
        pixel=1
    print(pixel)
    if pixel ==1:
        licznik_1+=1
    else:
        licznik_0+=1
    licznik_calosci+=1
print("liczba elementow: ",licznik_calosci, '\n', "liczba 0: ",licznik_0,'\n', "liczba 1:" , licznik_1)


f.close()
#-----------------------------------------ZLICZANIE-POWTARZAJACYCH-SIE-SEKWENCJI---------------------------------------

f = open("testb.txt", "rb")
wystepowanie_11=0
wystepowanie_111=0
wystepowanie_1111=0
wystepowanie_11111=0
wystepowanie_00=0
wystepowanie_000=0
wystepowanie_0000=0
wystepowanie_00000=0

for line in f:
    if 255 in line:
        print("znalezionio cokolwiek")
        wystepowanie_11 = wystepowanie_11 +1
print(wystepowanie_11)
len(imgarr)


print(im_g)
f.close()
