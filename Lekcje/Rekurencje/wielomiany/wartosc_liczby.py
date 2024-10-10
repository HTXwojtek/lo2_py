#iteracyjnie
def horner_it(wsp, p):
    wynik=0
    for an in wsp:
        wynik=wynik*p+an
    return wynik

def horner_rek(wsp, st, p):
    if st==0:
        return wsp[0]
    return p*horner_rek(wsp, st-1, p)+wsp[st]

p=int(input('Podaj postawe systemu: '))
lista=input(f'Podaj liczbę zapisaną w systemie {p}: ')
wsp=[]
for i in lista:
    if i.isnumeric():
        wsp.append(int(i))
    else:
        wsp.append(int(ord(i))-55)
print(f'Wartość liczby {lista} o postawie {p} wynosi (it): {horner_it(wsp, p)}')
print(f'Wartość liczby {lista} o postawie {p} wynosi (rek): {horner_rek(wsp, len(wsp)-1, p)}')
