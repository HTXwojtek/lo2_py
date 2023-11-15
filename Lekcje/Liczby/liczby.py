import math
#liczby zlozone
def zloz(liczba):
    if liczba<2:
        return 0
    for i in range(2, int(math.sqrt(liczba)+1)):
        if liczba%i==0:
            return 1
    return 0

#liczba pierwsza
def prime(liczba):
    if liczba<2:
        return 0
    for i in range(2, int(math.sqrt(liczba)+1)):
        if liczba%i==0:
            return 0
    return 1

#polpierwsz
def semiprime(liczba):
    tab=[]
    i=2
    while liczba>1:
        if liczba%i==0:
            tab.append(i)
            liczba=liczba//i
        else:
            i+=1
    if len(tab)==2:
        return 1
    return 0

def super_prime(liczba):
    if prime(liczba)==0:
        return 0
    suma=0
    napis=str(liczba)
    for literka in napis:
        suma+=int(literka)
    return(prime(suma))

#liczby blizniacze
def bliz(a,b):
    if prime(a) and prime(b) and abs(a-b)==2:
        return 1
    return 0

#liczba doskonala
def doskonale(liczba):
    suma=0
    for i in range(1, liczba//2+1):
        if liczba%i==0:
            suma+=i
    return suma==liczba

#liczba narcystyczna/armstronga
def narcyz(liczba):
    liczba2=liczba
    suma=0
    dl=len(str(liczba))
    while liczba>0:
        suma+=(liczba%10)**dl
        liczba=liczba//10
    return suma==liczba2

# liczby wesole
def suma_cyfr(napis):
    suma=0
    for literka in napis:
        suma+=int(literka)**2
    return suma

def wesole(liczba):
    liczba=pierwotna=suma_cyfr(str(liczba))
    while liczba>1:
        print(liczba)
        liczba=suma_cyfr(str(liczba))
        if liczba==pierwotna:
            return 0
        return 1
    
#wesole inny sposob
def wesole2(liczba):
    tab=[]
    while liczba != 1 and liczba not in tab:
        tab.append(liczba)
        liczba=sum(int(digit)**2 for digit in str(liczba))
    return liczba == 1