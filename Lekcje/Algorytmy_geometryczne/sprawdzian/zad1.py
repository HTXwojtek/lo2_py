def wart(x:float):
    return -((x-3)*(x-3)*(x-3))+2

def polowienie_przedzialow(a:float, b:float, epsilon: float):
    if wart(a)== 0.0: return a
    if wart(b) == 0.0: return b
    while b - a>epsilon:
        srodek=(a+b)/2
        if wart(srodek) ==0.0:
            return srodek
        if wart(a)*wart(srodek) <0:
            b=srodek
        else:
            a=srodek
    return round((a+b)/2,8)

a=-1
b=10
epsilon=float(input('Podaj przyblizenie (epsilon): '))
print(f'Znalezione miejsce zerowe wynosi: {polowienie_przedzialow(a,b,epsilon)}')

