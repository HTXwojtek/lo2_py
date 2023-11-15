import math
# a
def prime(liczba):
    if liczba<2:
        return 0
    for i in range(2,int(math.sqrt(liczba))+1):
        if liczba%i==0:
            return 0
    return 1

def super_prime(liczba):
    if prime(liczba)==0:
        return 0
    suma=0
    napis=str(liczba)
    for literka in napis:
        suma+=int(literka)
    return(prime(suma))

def super_b_prime(liczba):
    if prime(liczba)==0:
        return 0
    suma=0
    napis=str(bin(liczba))[2:]
    for literka in napis:
        suma+=int(literka)
    return(prime(suma))

# b.1
def suma_cyfr(liczba):
    suma=0
    napis=str(liczba)
    for literka in napis:
        suma+=int(literka)
    if prime(suma)==0:
        return 0
    else:
        return 1

# b.2
def super_b_prime_b(liczba):
    if prime(liczba)==0:
        return 0
    suma=0
    napis=str(bin(liczba))[2:]
    for literka in napis:
        suma+=int(literka)
    if prime(suma):
        return liczba

plik=open('2.txt')
l1=0
suma_b=0
for el in plik:
    liczba=int(el)
    suma_b+=super_b_prime_b(liczba)
print(prime(suma_b))
