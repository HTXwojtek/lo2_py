# interacyjnie
def dec2sys_it(liczba,podst):
    tab=[]
    while liczba!=0:
        if liczba%podst>9:
            tab.insert(0,chr(55+liczba%podst))
        else:
            tab.insert(0,liczba%podst)
        liczba=liczba//podst
    liczbabin="".join(map(str,tab))
    return liczbabin

def dec2sys_rek(liczba,podst):
    if liczba>(podst-1):
        if liczba%podst>9:
            return dec2sys_rek(liczba//podst,podst)+chr(55+liczba%podst)
        else:
            return dec2sys_rek(liczba//podst,podst)+str(liczba%podst)
    else:
        if liczba%podst>9:
            return chr(55+liczba%podst)
        else:
            return str(liczba%podst)



x=int(input("Podaj liczbę w systemie dziesiętnym: "))
p=int(input("Podaj podstawę:"))
print(f"Liczba {x} w systemie o podstawie {p} ma zapis (iteracyjnie): {dec2sys_it(x,p)}")
print(f"Liczba {x} w systemie o podstawie {p} ma zapis (rekurencyjnie): {dec2sys_rek(x,p)}")