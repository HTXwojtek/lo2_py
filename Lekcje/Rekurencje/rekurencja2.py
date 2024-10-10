# W matematyce:
#
# f(0) = 0
# f(n) = n + f(n - 1)
#
# Rozwinięcie:
#
# f(5) = 5 + f(5 - 1)
#          = 5 + f(4) = 5 + (4 + f(4 - 1))
#          = 5 + (4 + f(3)) = 5 + (4 + (3 + f(3 - 1)))
#          = 5 + (4 + (3 + f(2))) = 5 + (4 + (3 + (2 + f(2 - 1))))
#          = 5 + (4 + (3 + (2 + f(1))) = 5 + (4 + (3 + (2 + (1 + f(1 - 1)))))
#          = 5 + (4 + (3 + (2 + (1 + f(0)))) = 5 + (4 + (3 + (2 + (1 + 0))))
#          = 15

# Program sumujący kolejne liczby naturalne od 1 do n

# iteracyjnie
def suma_it(n):
    sum=0
    for i in range(n+1):
        sum+=i
    return sum

# rekurencyjnie
def suma_rek(n):
    if (n == 0):
        return 0
    else:
        return n + suma_rek(n-1)

# Wywołanie funkcji
x=int(input("Podaa x: "))
print("Suma iteracyjnie: ",suma_it(x))
print("Suma rekurencyjnie: ",suma_rek(x))
