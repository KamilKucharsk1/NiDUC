def bit(lista):
    licznik=0
    all=[]
    print()
    print()
    print("###################      bit COUNTER     ###########################")
    while licznik < len(lista) - 1:
        wyraz=0
        if lista[licznik]   ==  '1': wyraz += 1
        if lista[licznik+1] == '1': wyraz += 2
        if lista[licznik+2] == '1': wyraz += 4
        if lista[licznik+3] == '1': wyraz += 8
        if lista[licznik+4] == '1': wyraz += 16
        if lista[licznik+5] == '1': wyraz += 32
        if lista[licznik+6] == '1': wyraz += 64
        if lista[licznik+7] == '1': wyraz += 128
        licznik+=8
        all.append(wyraz)
    print(lista)
    print(all)
    '''W tabeli all zapisane są dziesętnie liczby bitów'''
    return all