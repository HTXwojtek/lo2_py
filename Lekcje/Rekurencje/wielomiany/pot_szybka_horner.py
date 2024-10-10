#iteracyjniue
def pot_szybka_it(a,b):
    wynik=1
    while b>0:
        if b%2==1:
            wynik*=a
        a*=a
        b//=2
    return wynik+1

#rekurencyjnie
def pot_szybka_rek(a,b):
    if b==0:
        return 1
    if b%2==1:
        return a*pot_szybka_rek(a,b-1)
    wynik=pot_szybka_rek(a,b//2)
    return wynik*wynik

a=int(input('Podaj a: '))
b=int(input('Podaj b: '))
print(f'{a} do potegi {b} wynosi iteracyjnie: {pot_szybka_it(a,b)}')
print(f'{a} do potegi {b} wynosi rekurencyjnie: {pot_szybka_rek(a,b)}')
