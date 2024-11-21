def wart(x: float, a: float, b: float, c: float):
    return a * x**2 + b * x + c

def znajdz_przedzial_kwadratowy(sr: float, a: float, b: float, c: float):
    p = sr + 5
    while wart(-p, a, b, c) * wart(sr, a, b, c) > 0:
        p += 5
    return -p, p

def polowienie_przedzialow_kwadratowe_it(a: float, b: float, c: float, epsilon: float, left: float, right: float):
    while right - left > epsilon:
        srodek = (left + right) / 2
        if wart(srodek, a, b, c) == 0.0:
            return srodek
        elif wart(left, a, b, c) * wart(srodek, a, b, c) < 0:
            right = srodek
        else:
            left = srodek
    return round((left + right) / 2, 8)

def polowienie_przedzialow_kwadratowe_rek(a: float, b: float, c: float, epsilon: float, left: float, right: float):
    srodek = (left + right) / 2
    if right - left <= epsilon:
        return round(srodek, 8)
    if wart(srodek, a, b, c) == 0.0:
        return srodek
    elif wart(left, a, b, c) * wart(srodek, a, b, c) < 0:
        return polowienie_przedzialow_kwadratowe_rek(a, b, c, epsilon, left, srodek)
    else:
        return polowienie_przedzialow_kwadratowe_rek(a, b, c, epsilon, srodek, right)


a = float(input("Podaj współczynnik a (różny od 0): "))
b = float(input("Podaj współczynnik b: "))
c = float(input("Podaj współczynnik c: "))
epsilon=0.00001


delta = b**2 - 4 * a * c

if a == 0 or delta <= 0:
    print("Nie mogę obliczyć miejsc zerowych ze względu na podane przez ciebie dane")
else:
    sr = -b / (2 * a)
    
    #[-p, sr]
    lewy1, prawy1 = znajdz_przedzial_kwadratowy(sr, a, b, c)
    miejsce_zero1_it = polowienie_przedzialow_kwadratowe_it(a, b, c, epsilon, lewy1, sr)
    miejsce_zero1_rek = polowienie_przedzialow_kwadratowe_rek(a, b, c, epsilon, lewy1, sr)
    
    print("Pierwsze miejsce zerowe (iteracyjnie):", miejsce_zero1_it)
    print("Pierwsze miejsce zerowe (rekurencyjnie):", miejsce_zero1_rek)
    
    #[sr, p]
    lewy2, prawy2 = sr, prawy1
    miejsce_zero2_it = polowienie_przedzialow_kwadratowe_it(a, b, c, epsilon, sr, prawy2)
    miejsce_zero2_rek = polowienie_przedzialow_kwadratowe_rek(a, b, c, epsilon, sr, prawy2)
    
    print("Drugie miejsce zerowe (iteracyjnie):", miejsce_zero2_it)
    print("Drugie miejsce zerowe (rekurencyjnie):", miejsce_zero2_rek)





