#Funkcja obliczająca wartość funkcji
def wart(x: float):
 return x * (x * (x - 3) + 2) - 6 

def polowienie_przedzialow_it(a: float, b: float, epsilon: float):
    if wart(a) == 0.0: return a
    if wart(b) == 0.0: return b
    while b - a > epsilon:
        srodek = (a + b) / 2
        if wart(srodek) == 0.0: # jesli miejsce zerowe jest w srodku
            return srodek
        if wart(a) * wart(srodek) < 0:
            b = srodek
        else:
            a = srodek
    return round((a + b) / 2,8)


# Funkcja rekurencyjna
def polowienie_przedzialow_rek(a: float, b: float, epsilon: float):
    if wart(a) == 0.0:
        return a
    if wart(b) == 0.0:
        return b
    srodek = (a + b) / 2
    if b - a <= epsilon:
        return round(srodek,8)
    if wart(a) * wart(srodek) < 0:
        return polowienie_przedzialow_rek(a, srodek, epsilon)
    return polowienie_przedzialow_rek(srodek, b, epsilon)


#PROGRAM - Obliczanie miejsc zerowych metodą połowienia przedziałów
a = -10; b = 10; epsilon = 0.00001
print("Znalezione miejsce zerowe wynosi (iteracyjnie): ", 
polowienie_przedzialow_it(a, b, epsilon))
print("Znalezione miejsce zerowe wynosi (rekurencyjnie): ", 
polowienie_przedzialow_rek(a, b, epsilon))

