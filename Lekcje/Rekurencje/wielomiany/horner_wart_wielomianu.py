def horner_it(wsp, x):
    wynik=0
    for an in wsp:
        wynik=wynik*x+an
    return wynik

def horner_rek(wsp, st, x):
    if st==0:
        return wsp[0]
    return horner_rek(wsp, st-1, x)


lista=list(map(float, input('Podaj wspolczynniki wielomianu: ').split()))
print(lista)
print("iteracyjnie dla wspolczynnikow", lista, horner_it(lista,2), 'rekurencyjnie',horner_rek(lista,3,2))