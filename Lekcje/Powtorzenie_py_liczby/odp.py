import math
#zad 1
def prime(liczba):
    if liczba<2:
        return 0
    for i in range(2, int(math.sqrt(liczba)+1)):
        if liczba%i==0:
            return 0
    return 1

#zad 2
def zlozone(liczba):
    if liczba<2:
        return 0
    for i in range(2, int(math.sqrt(liczba)+2)):
        if liczba%i==0:
            return 1
    return 0

#zad 3
def lustrzane(a,b):
    if len(str(a))>3 or len(str(b))>3:
        return 0
    if str(a)==str(b)[::-1]:
        return 1
    return 0

#zad 4
def doskonale(liczba):
    suma=0
    for i in range(1, liczba//2+1):
        if liczba%i==0:
            suma+=i
    return suma==liczba

#zad 5
def armstronga(liczba):
    liczba2=liczba
    suma=0
    dl=len(str(liczba))
    while liczba>0:
        suma+=(liczba%10)**dl
        liczba=liczba//10
    return suma==liczba2

#zad 7
def rosnaca(liczba):
    if len(str(liczba))<2:
        return 0
    koniec=liczba%10
    liczba=liczba/10
    while liczba>0:
        if not koniec>liczba%10:
            return 0
        koniec=liczba%10
        liczba=liczba//10
    return 1

#zad 8
def cyferki(liczba):
    napis=str(liczba)
    for literka in napis:
        a=int(literka)
        if prime(a):
            return 1
        return 0

#zad 9
def nwd(a,b):
    while b!=0:
        a,b=b,a%b
    return a

maxnwd=0
plik1=open('dane.txt')
for linia in plik1:
    a,b=map(int, linia.split())
    nwd_ab=nwd(a,b)
    if maxnwd<nwd_ab:
        maxnwd=nwd_ab
print(maxnwd)

#zad 10
tab=[123,321,123123,33444554,123243]
maxseria=1
for i in range(0, len(tab)):
    liczba=tab[i]
    seria=1
    for j in range(i+1, len(tab)):
        if rosnaca(liczba):
            seria+=1
        
        if seria>maxseria:
            maxseria=seria
            maxliczba=liczba
print(maxseria, maxliczba)

#zad 11
plik=open('dane.txt')
tab=list(map(int, plik.read().split()))
maxseria=1
for i in range(0, len(tab)):
    liczba=tab[i]
    seria=1
    for j in range(i+1, len(tab)):
        if sorted(str(liczba))==sorted(str(tab[j])):
            seria+=1
        
        if seria>maxseria:
            maxseria=seria
            maxliczba=liczba
print(maxseria, maxliczba)






