from math import sqrt
# zad 1
def zad1(n):
    if n==1:
        return 4
    elif n>1:
        return (2*zad1(n-1))-2*n

#zad 2
def prime(a):
    if a<2:
        return False
    for i in range(2, int(sqrt(a))+1):
        if a%i==0:
            return False
    return True

def horner(wsp, st):
    if st==0:
        return wsp[0]
    else:
        if prime(wsp[st]):
            x=1
        else:
            x=-1
    return x*horner(wsp, st-1)+wsp[st]

# plik=open('wielomiany.txt')
# for linia in plik:
#     wsp=list(map(int, linia.split()))
#     st=len(wsp)-1
#     print(horner(wsp, st))

#zad 3
def pod_it(a,b):
    wynik=1
    while b>0:
        if b%2==1:
            wynik*=a
        a*=a
        b//=2
    return wynik

def pot_rek(a,b):
    if b==0:
        return 1
    if b%2==1:
        return a*pot_rek(a,b-1)
    wynik=pot_rek(a,b//2)
    return wynik*wynik

# x=int(input('Podaj pierwsza liczbe: '))
# n=int(input('Podaj pierwsza potege liczby: '))
# y=int(input('Podaj druga liczbe: '))
# m=int(input('Podaj druga potege liczby: '))
# print('iteracyjnie:', pod_it(x,n)+pod_it(y,m), 'rekurencyjnie:', pot_rek(x,n)+pot_rek(y,m))


#zad 4
# def wyszukaj(tab, l, dl):
#     if tab[dl]==l:
#         return dl
#     return wyszukaj(tab, l, dl-1)

# tab=[1,4,56,78, 9,90] 
# print(wyszukaj(tab,78,len(tab)-1))

#zad 5
def czy_palindrom(slowo):
    if len(slowo) <= 1:
        return True
    if slowo[0] != slowo[-1]:
        return False
    return czy_palindrom(slowo[1:-1])

# slowo=input('Podaj slowo: ').strip().lower()
# print(czy_palindrom(slowo))

#zad 6
def horner_it(wsp, p):
    wynik=0
    for an in wsp:
        wynik=wynik*p+an
    return wynik

def horner_rek(wsp, st, p):
    if st==0:
        return wsp[0]
    return p*horner_rek(wsp, st-1, p)+wsp[st]

# lista=input(f'Podaj liczbę zapisaną w systemie 20: ')
# wsp=[]
# for i in lista:
#     if i.isnumeric():
#         wsp.append(int(i))
#     else:
#         wsp.append(int(ord(i))-55)
# print(f'Wartość liczby {lista} o postawie 20 wynosi (it): {horner_it(wsp, 20)}')
# print(f'Wartość liczby {lista} o postawie 20 wynosi (rek): {horner_rek(wsp, len(wsp)-1, 20)}')

#zad 7




