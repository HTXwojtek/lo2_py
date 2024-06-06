import math

def prime(liczba):
    if liczba<2:
        return 0
    for i in range(2, int(math.sqrt(liczba)+1)):
        if liczba%i==0:
            return 0
    return 1

def super_prime(liczba):
    if prime(liczba)==0:
        return 0
    suma=0
    if prime(liczba):
        return 1
    napis=str(liczba)
    for literka in napis:
        suma+=int(literka)
    return prime(suma)
    
def super_b_prime(liczba):
    if super_prime(liczba)==0:
        return 0
    suma=0
    napis=str(bin(liczba))[2::]
    for literka in napis:
        suma+=int(literka)
    if prime(suma):
        return 1
    
def suma_cyfr(liczba):
    suma=0
    napis=str(liczba)
    for literka in napis:
        suma+=int(literka)
    return suma
    
plik1=open('1.txt')
plik2=open('2.txt')
plik3=open('3.txt')

a1=a2=a3=0
for el in plik1:
    liczba=int(el)
    a1+=super_b_prime(liczba)
print(a1)
for el in plik2:
    liczba=int(el)
    a2+=super_b_prime(liczba)
print(a2)
for el in plik3:
    liczba=int(el)
    a3+=super_b_prime(liczba)
print(a3)

suma=0
for i in range(100, 10000 +1):
    if prime(suma_cyfr(i)):
        suma+=1
print(suma)