import math

def zlozone(liczba):
    if liczba<2:
        return 0
    for i in range(2,int(math.sqrt(liczba)+1)):
        if pierwsza(liczba):
            return False
    return True

def pierwsza(liczba):
     for i in range(2,liczba//2+1):
        if liczba%i==0:
            return False
     return True

def perfect(liczba):
    if liczba<2:
        return 0
    suma=1
    for i in range(2,liczba//2+1):
        suma+=i
    return suma==liczba

def nwd(a,b):
    while b!=0:
        a,b=b,a%b
    return a

def narcyz(liczba):
    liczba2=liczba
    suma=0
    dl=len(str(liczba))
    while(liczba>0):
        suma+=(liczba%10)**dl
        liczba=liczba//10
    return suma==liczba2

plik=open('liczby.txt')
suma_zl=0
max_pier=0
suma_dosk=0
suma_pier=0
suma_narc=0
makspole=0
for linia in plik:
    a,b=map(int,linia.split())
    if zlozone(a):
        suma_zl+=1
    if zlozone(b):
        suma_zl+=1
    if pierwsza(a) and a>max_pier:
        max_pier=a
    if pierwsza(b):
        max_pier=max(max_pier,b)
    if perfect(a):
        suma_dosk+=1
    if perfect(b):
        suma_dosk+=1
    if nwd(a,b)!=1:
        suma_pier+=1
    if narcyz(a):
        suma_narc+=1
    if narcyz(b):
        suma_narc+=1
    if makspole<a*b:
        makspole=a*b
        maksa=a
        maksb=b

print(max_pier,suma_zl,suma_pier,suma_dosk,suma_narc,maksa,maksb)