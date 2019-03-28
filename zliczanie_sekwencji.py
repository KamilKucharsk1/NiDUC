

def zlicz(lista):

    import matplotlib.pyplot as plt
    """sekwencja_00=0
    sekwencja_000=0
    sekwencja_0000=0
    sekwencja_00000=0
    sekwencja_000000=0
    sekwencja_0000000=0
    sekwencja_00000000=0
    sekwencja_11=0
    sekwencja_111=0
    sekwencja_1111=0
    sekwencja_11111=0
    sekwencja_111111=0
    sekwencja_1111111=0
    sekw"""

    sekwencje=[]

    sekwencja=0
    licznik = 0
    while licznik<len(lista)-1:
        if lista[licznik] == '1' and lista[licznik + 1] == '1':
            licznik = licznik + 2
            sekwencja += 1
        else:
            licznik = licznik+1

    print("ilosc wystapien sekwencji '11' :       ", sekwencja)
    sekwencje.append(sekwencja)

    sekwencja = 0
    licznik = 0
    while licznik < len(lista) - 2:
        if lista[licznik] == '1' and lista[licznik + 1] == '1' and lista[licznik + 2] == '1':
            licznik = licznik + 3
            sekwencja += 1
        else:
            licznik = licznik + 1

    print("ilosc wystapien sekwencji '111' :      ", sekwencja)
    sekwencje.append(sekwencja)

    sekwencja = 0
    licznik = 0
    while licznik < len(lista) - 3:
        if lista[licznik] == '1' and lista[licznik + 1] == '1' and lista[licznik + 2] == '1' and lista[licznik + 3] == '1':
            licznik = licznik + 4
            sekwencja += 1
        else:
            licznik = licznik + 1

    print("ilosc wystapien sekwencji '1111' :     ", sekwencja)
    sekwencje.append(sekwencja)

    sekwencja = 0
    licznik = 0
    while licznik < len(lista) - 4:
        if lista[licznik] == '1' and lista[licznik + 1] == '1' and lista[licznik + 2] == '1' and lista[licznik + 3] == '1' and lista[licznik + 4] == '1':
            licznik = licznik + 5
            sekwencja += 1
        else:
            licznik = licznik + 1

    print("ilosc wystapien sekwencji '11111' :    ", sekwencja)
    sekwencje.append(sekwencja)

    sekwencja = 0
    licznik = 0
    while licznik < len(lista) - 5:
        if lista[licznik] == '1' and lista[licznik + 1] == '1' and lista[licznik + 2] == '1' and lista[licznik + 3] == '1' and lista[licznik + 4] == '1' and lista[licznik + 5] == '1':
            licznik = licznik + 6
            sekwencja += 1
        else:
            licznik = licznik + 1

    print("ilosc wystapien sekwencji '111111' :   ", sekwencja)
    sekwencje.append(sekwencja)

    sekwencja = 0
    licznik = 0
    while licznik < len(lista) - 6:
        if lista[licznik] == '1' and lista[licznik + 1] == '1' and lista[licznik + 2] == '1' and lista[licznik + 3] == '1' and lista[licznik + 4] == '1' and lista[licznik + 5] == '1' and lista[licznik + 6] == '1':
            licznik = licznik + 7
            sekwencja += 1
        else:
            licznik = licznik + 1

    print("ilosc wystapien sekwencji '1111111' :  ", sekwencja)
    sekwencje.append(sekwencja)

    sekwencja = 0
    licznik = 0
    while licznik < len(lista) - 7:
        if lista[licznik] == '1' and lista[licznik + 1] == '1' and lista[licznik + 2] == '1' and lista[licznik + 3] == '1' and lista[licznik + 4] == '1' and lista[licznik + 5] == '1' and lista[licznik + 6] == '1' and lista[licznik + 7] == '1':
            licznik = licznik + 8
            sekwencja += 1
        else:
            licznik = licznik + 1

    print("ilosc wystapien sekwencji '11111111' : ", sekwencja)
    sekwencje.append(sekwencja)

    sekwencja = 0
    licznik = 0
    while licznik < len(lista) - 1:
        if lista[licznik] == '0' and lista[licznik + 1] == '0':
            licznik = licznik + 2
            sekwencja += 1
        else:
            licznik = licznik + 1

    print("ilosc wystapien sekwencji '00' :       ", sekwencja)
    sekwencje.append(sekwencja)

    sekwencja = 0
    licznik = 0
    while licznik < len(lista) - 2:
        if lista[licznik] == '0' and lista[licznik + 1] == '0' and lista[licznik + 2] == '0':
            licznik = licznik + 3
            sekwencja += 1
        else:
            licznik = licznik + 1

    print("ilosc wystapien sekwencji '000' :      ", sekwencja)
    sekwencje.append(sekwencja)

    sekwencja = 0
    licznik = 0
    while licznik < len(lista) - 3:
        if lista[licznik] == '0' and lista[licznik + 1] == '0' and lista[licznik + 2] == '0' and lista[
            licznik + 3] == '0':
            licznik = licznik + 4
            sekwencja += 1
        else:
            licznik = licznik + 1

    print("ilosc wystapien sekwencji '0000' :     ", sekwencja)
    sekwencje.append(sekwencja)

    sekwencja = 0
    licznik = 0
    while licznik < len(lista) - 4:
        if lista[licznik] == '0' and lista[licznik + 1] == '0' and lista[licznik + 2] == '0' and lista[
            licznik + 3] == '0' and lista[licznik + 4] == '0':
            licznik = licznik + 5
            sekwencja += 1
        else:
            licznik = licznik + 1

    print("ilosc wystapien sekwencji '00000' :    ", sekwencja)
    sekwencje.append(sekwencja)

    sekwencja = 0
    licznik = 0
    while licznik < len(lista) - 5:
        if lista[licznik] == '0' and lista[licznik + 1] == '0' and lista[licznik + 2] == '0' and lista[
            licznik + 3] == '0' and lista[licznik + 4] == '0' and lista[licznik + 5] == '0':
            licznik = licznik + 6
            sekwencja += 1
        else:
            licznik = licznik + 1

    print("ilosc wystapien sekwencji '000000' :   ", sekwencja)
    sekwencje.append(sekwencja)

    sekwencja = 0
    licznik = 0
    while licznik < len(lista) - 6:
        if lista[licznik] == '0' and lista[licznik + 1] == '0' and lista[licznik + 2] == '0' and lista[
            licznik + 3] == '0' and lista[licznik + 4] == '0' and lista[licznik + 5] == '0' and lista[
            licznik + 6] == '0':
            licznik = licznik + 7
            sekwencja += 1
        else:
            licznik = licznik + 1

    print("ilosc wystapien sekwencji '0000000' :  ", sekwencja)
    sekwencje.append(sekwencja)

    sekwencja = 0
    licznik = 0
    while licznik < len(lista) - 7:
        if lista[licznik] == '0' and lista[licznik + 1] == '0' and lista[licznik + 2] == '0' and lista[
            licznik + 3] == '0' and lista[licznik + 4] == '0' and lista[licznik + 5] == '0' and lista[
            licznik + 6] == '0' and lista[licznik + 7] == '0':
            licznik = licznik + 8
            sekwencja += 1
        else:
            licznik = licznik + 1

    print("ilosc wystapien sekwencji '00000000' : ", sekwencja)
    sekwencje.append(sekwencja)


    licznik=0
    jedynki=0
    zera=0

    while licznik<len(lista)-1:
        if lista[licznik] == '0':
            zera = zera +1
        else:
            jedynki = jedynki +1
        licznik= licznik+1

    print("ilosc jedynek: ", jedynki)
    print("ilosc zer: ", zera)

    x=[00, 000, 0000, 00000, 000000, 0000000, 00000000, 11, 111, 1111, 11111, 111111, 1111111, 11111111]
    y=sekwencje


