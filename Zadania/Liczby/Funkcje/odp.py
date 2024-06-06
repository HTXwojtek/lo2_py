import math
def zlozone(liczba):
    if liczba<2:
        return 0
    for i in range(2, int(math.sqrt(liczba)+1)):
        if liczba%i==0:
            return 1
    return 0

def pierwsza(liczba):
    if liczba<2:
        return 0
    for i in range(2, int(math.sqrt(liczba)+1)):
        if liczba%i==0:
            return 0
    return 1

def doskonala(liczba):
    suma=0
    for i in range(1, int(liczba//2+1)):
        if liczba%i==0:
            suma+=i
    return suma==liczba

def nwd(a,b):
    while b!=0:
        a,b=b,a%b
    return a

def niewzgledniepier(a,b):
    if nwd(a,b)==1:
        return 0
    return 1

def narcyz(liczba):
    suma=0
    liczba2=liczba
    dl=len(str(liczba))
    while liczba>0:
        suma+=(liczba%10)**dl
        liczba=liczba//10
    return liczba2==suma
l1=maxpierwsza=makspole=maksa=maksb=l3=l4=l5=0
plik=open('dane.txt')
for linia in plik:
    a,b=map(int, linia.split())
    l1+=zlozone(a)
    l1+=zlozone(b)
    if pierwsza(a):
        maxpierwsza=max(maxpierwsza,a)
    if pierwsza(b):
        maxpierwsza=max(maxpierwsza,b)
    l3+=doskonala(a)
    l3+=doskonala(b)
    l4+=niewzgledniepier(a,b)
    if makspole<a*b:
        makspole=a*b
        maksa=a
        maksb=b
    if narcyz(a):
        print(a)
    if narcyz(b):
        print(b)
print(f'zad 1: {l1}, zad 2: {maxpierwsza}, zad 3: {l3}, zad4: {l4}, zad5: makspole {makspole}, boki: {maksa}, {maksb}')