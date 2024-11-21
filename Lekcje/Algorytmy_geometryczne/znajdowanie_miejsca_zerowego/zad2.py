def wart(x: float, a: float, b: float):
    return a * x + b

def znajdz_przedzial_liniowy(a: float, b: float):
    p=5
    while wart(-p, a, b) * wart(p, a, b) > 0:
        p+=5
    return -p, p

def polowienie_przedzialow_liniowe_it(a: float, b: float, epsilon: float):
    lewy,prawy=znajdz_przedzial_liniowy(a, b)
    while prawy-lewy>epsilon:
        srodek=(lewy+prawy) / 2
        if wart(srodek, a, b)==0.0:
            return srodek
        elif wart(lewy, a, b) * wart(srodek, a, b)<0:
            prawy=srodek
        else:
            lewy=srodek
    return round((lewy + prawy) / 2, 8)

def polowienie_przedzialow_liniowe_rek(lewy: float, prawy: float, a: float, b: float, epsilon: float):
    srodek = (lewy + prawy) / 2
    if prawy - lewy <= epsilon:
        return round(srodek, 8)
    if wart(srodek, a, b) == 0.0:
        return srodek
    elif wart(lewy, a, b) * wart(srodek, a, b) < 0:
        return polowienie_przedzialow_liniowe_rek(lewy, srodek, a, b, epsilon)
    else:
        return polowienie_przedzialow_liniowe_rek(srodek, prawy, a, b, epsilon)


a=float(input("Podaj współczynnik a (różny od 0): "))
b=float(input("Podaj współczynnik b: "))
epsilon=0.00001

if a==0:
    print("Wartość a nie może być równa 0.")
else:
    miejsce_zero_it = polowienie_przedzialow_liniowe_it(a, b, epsilon)
    print("Znalezione miejsce zerowe (iteracyjnie):", miejsce_zero_it)

    lewy, prawy = znajdz_przedzial_liniowy(a, b)
    
    miejsce_zero_rek = polowienie_przedzialow_liniowe_rek(lewy, prawy, a, b, epsilon)
    print("Znalezione miejsce zerowe (rekurencyjnie):", miejsce_zero_rek)



