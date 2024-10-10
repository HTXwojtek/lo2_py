# Program obliczjący silnię z podanej liczby naturalnej
# W matematyce:
# Silnia liczby naturalnej n jest to iloczyn wszystkich liczby dodatnich nie większych niż n
# Na przykład silnią liczby 5 jest wartość równania 1⋅2⋅3⋅4⋅5
# Silnię liczby n oznacza się w następujący sposób: n! = 1*2*3*...*n
# Tak więc np. 5!=1⋅2⋅3⋅4⋅5=120


# iteracyjnie
def silnia_it(n):
    s = 1
    for i in range(2,n+1):
        s *= i
    return s

# rekurencyjnie
def silnia_rek(n):
    if n > 1:
        return n*silnia_rek(n-1)
    return 1

# Wywołanie funkcji
m=int(input("Podaj m: "))
print("Silnia iteracyjnie: ",silnia_it(m))
print("Silnia rekurencyjnie: ",silnia_rek(m))
