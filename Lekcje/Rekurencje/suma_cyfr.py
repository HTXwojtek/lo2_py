# iteracyjnie
def suma_itr(liczba):
    suma=0
    while liczba>0:
        suma+=liczba%10
        liczba=liczba//10
    return suma


# rekurencyjnie
def suma_rek(liczba):
    if liczba==0:
        return 0
    else:
        return suma_rek(liczba//10)+(liczba%10)
    
print(suma_rek())