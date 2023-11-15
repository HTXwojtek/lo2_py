import math
# podzial liczby na cyferki
def cyferki(liczba):
    napis=str(liczba)
    suma=0
    for literka in napis:
        suma+=int(literka)
    return suma

#czy w liczbie sa te same cyferki
def same_cyferki(liczba):
    koniec=liczba%10
    while liczba>0:
        if koniec!=liczba%10:
            return 0
        liczba=liczba//10
    return 1

# czy w liczbie cyferki rosna
def rosnaca(liczba):
    koniec=liczba%10
    liczba=liczba/10
    while liczba>0:
        if not koniec>liczba%10:
            return 0
        koniec=liczba%10
        liczba=liczba//10
    return 1