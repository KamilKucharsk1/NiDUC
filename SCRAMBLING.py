import numpy
import numpy as np
import cv2

import zliczanie_sekwencji
import scrambler1_x6_x7
import descrambler1_x6_x7
import scrambler_x43_1
import descrambler_x43_1
import asynchro_x_25_1
import asynchro_desc_x_25_1
import synchro_x_17_x_10_1
import V_34
import V_34_descrambler
import DVB
import zlicz
import histogramy

img=cv2.imread("profile_default.jpg",0)         #wczytanie obrazu jako tablica tablic [0...255]
data = numpy.array(img)
img_str = cv2.imencode('.jpg', img)[1]
img_str = numpy.array(img_str)


#print(" Tablica tablic:", img)
#print(" Lista zamiast tablicy tablic: ", img_str)

def decToBin(n):
    if n==0:
        return ''
    else:
        return decToBin(n//2) + str(n%2)


for i in range(0,img_str.size):             #zamiana listy bajtow na bity
    byte=str(decToBin(img_str[i]))
    byte=byte.replace('[','')
    byte=byte.replace(']','')
    if byte == '':
        byte='00000000'
    if len(byte)!=8:
        zero_lacks=8-len(byte)
        for iterator in range(0,zero_lacks):
            byte= '0' + byte
    print(byte)


print("------MACIERZ---WEJSCIOWA------")
print("dlugosc macierzy: ",len(img_str))

lista=[1]                   # lista do ktorej zostana sklejone elementy macierzy jako jeden długi string

lista=np.unpackbits(img_str).astype('U1').view(f'U{img_str.size*img_str.dtype.itemsize*8}').item(0)
print("------PO-ZAMIANIE-NA-LISTE-BITOW")
print(lista)
print("dlugosc listy: ", len(lista))

print('\n')
print("Lista przed scramblingiem: ", lista)
zliczanie_sekwencji.zlicz(lista)



#---------------------------------SCRAMBLING-----------------------------------------



print('\n')
lista=[int(i) for i in lista]
lista=scrambler1_x6_x7.x6_x7(lista)
print("Lista po scramblingu multiplikatywnym 1 + x^6 + x^7: ", )
zliczanie_sekwencji.zlicz(lista)
licznik = 0
lista_bajtow = []

zlicz.bit(lista)
"""histogramy.hist(zlicz.bit.all) """






print('\n')
lista=[int(i) for i in lista]
lista=descrambler1_x6_x7.x6_x7(lista)
print("Lista po descramblingu 1 + x^6 + x+7: ", )
zliczanie_sekwencji.zlicz(lista)

#------------------------------------------------------------------------------------
print('\n')
lista=[int(i) for i in lista]
lista=DVB.dvb(lista)
print("Lista po scramblingu DVB: ", )
zliczanie_sekwencji.zlicz(lista)


print('\n')
lista=[int(i) for i in lista]
lista=DVB.dvb(lista)
print("Lista po descramblingu DVB: ", )
zliczanie_sekwencji.zlicz(lista)

#------------------------------------------------------------------------------------

print('\n')
lista=[int(i) for i in lista]
lista=V_34.V34(lista)
print("Lista po scramblingu multiplikatywnym V.34: ", )
zliczanie_sekwencji.zlicz(lista)


print('\n')
lista=[int(i) for i in lista]
lista=V_34_descrambler.V_34_descrambler(lista)
print("Lista po descramblingu multiplikatywnym V.34: ", )
zliczanie_sekwencji.zlicz(lista)



#------------------------------------------------------------------------------------

print('\n')
lista=[int(i) for i in lista]
lista=scrambler_x43_1.x43_1(lista)
print("Lista po scramblingu x^43 + 1: ", )
zliczanie_sekwencji.zlicz(lista)


print('\n')
lista=[int(i) for i in lista]
lista=descrambler_x43_1.descrambler_x43_1(lista)
print("Lista po descramblingu x^43 + 1: ", )
zliczanie_sekwencji.zlicz(lista)

#------------------------------------------------------------------------------------

print('\n')
lista=[int(i) for i in lista]
lista=scrambler1_x6_x7.x6_x7(lista)
lista=[int(i) for i in lista]
lista=scrambler_x43_1.x43_1(lista)
print("Lista po descramblingu 1+ x^6 +x^7 oraz x^43 + 1: ", )
zliczanie_sekwencji.zlicz(lista)


print('\n')
lista=[int(i) for i in lista]
lista=descrambler1_x6_x7.x6_x7(lista)
lista=[int(i) for i in lista]
lista=descrambler_x43_1.descrambler_x43_1(lista)
print("Lista po descramblingu 1+ x^6 +x^7 oraz x^43 + 1: ", )
zliczanie_sekwencji.zlicz(lista)

#------------------------------------------------------------------------------------

print('\n')
lista=[int(i) for i in lista]
lista=asynchro_x_25_1.x25_1(lista)
print("Lista po scramblingu asynchronicznym x^25+1: ", )
zliczanie_sekwencji.zlicz(lista)


print('\n')
lista=[int(i) for i in lista]
lista=asynchro_desc_x_25_1.desc_x25_1(lista)
print("Lista po descramblingu asynchronicznym x^25+1: ", )
zliczanie_sekwencji.zlicz(lista)

#------------------------------------------------------------------------------------

print('\n')
lista=[int(i) for i in lista]
lista=synchro_x_17_x_10_1.x_17_x_10_1(lista)
print("Lista po scramblingu synchronicznym x^17+x^10+1: ", )
zliczanie_sekwencji.zlicz(lista)


print('\n')
lista=[int(i) for i in lista]
lista=synchro_x_17_x_10_1.x_17_x_10_1(lista)
print("Lista po descramblingu synchronicznym x^17+x^10+1: ", )
zliczanie_sekwencji.zlicz(lista)


zlicz.bit(lista)


print("to koniec")
