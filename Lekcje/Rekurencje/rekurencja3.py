# W matematyce:
#
# F(0) = 0
# F(1) = 1
# F(n) = F(n-1) + F(n-2)
#
# To samo zapisane w języku Python:
#
# def F(n):
#         if n == 0:  # <-- warunek stopu
#                 return 0
#         elif n == 1: # <-- warunek stopu
#                 return 1
#         else:
#                 return F(n - 1) + F(n - 2)


# Program wyznaczający n-ty wyraz ciągu Fibonacciego

# iteracyjnie
def Fibo_it(n):
    a, b = 0, 1
    for i in range(n):
        b+=a
        a = b-a
    return a

# rekurencyjnie
def Fibo_rek(n):
    if n == 0:  # <-- warunek stopu
        return 0
    elif n == 1:  # <-- warunek stopu
        return 1
    else:
        return Fibo_rek(n - 1) + Fibo_rek(n - 2)

# Wywołanie funkcji
m=int(input("Podaj n: "))
print("Wuraz n-ty ciągu Fibonacciego iteracyjnie: ",Fibo_it(m))                             
print("Wuraz n-ty ciągu Fibonacciego rekurencyjnie: ",Fibo_rek(m))
