from math import fabs
# iteracyjnie
def pierw_it(pole,eps):
    a=float(1)
    b=float(pole)
    while fabs(a-b)>=eps:
        a=(a+b)/2
        b=pole/a
    return a
# rekurencyjnie
def pierw_rek(pole,eps,a=1.0):
    a=(a+pole/a)/2
    if fabs(pole-a**2)>eps:
        a=pierw_rek(pole,eps,a)
    return a




x=int(input("Podaj liczbę pod pierwiastkiem: "))
e=int(input("Podaj dokładność (ilość miejsc po przecinku): "))
dok=float(round(0.1**e,e))
print(f"Pierwiastek kw. z liczby {x} wynosi (it): {pierw_it(x,dok)}")
print(f"Pierwiastek kw. z liczby {x} wynosi (rek): {pierw_rek(x,dok)}")