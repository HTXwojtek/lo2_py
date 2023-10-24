# import math
# plik=open('2.txt')
# # a
# def prime(liczba):
#     if liczba<2:
#         return 0
#     for i in range(2,int(math.sqrt(liczba))+1):
#         if liczba%i==0:
#             return 0
#     return 1

# def super_prime(liczba):
#     if prime(liczba)==0:
#         return 0
#     suma=0
#     napis=str(liczba)
#     for literka in napis:
#         suma+=int(literka)
#     return(prime(suma))

# def super_b_prime(liczba):
#     if prime(liczba)==0:
#         return 0
#     suma=0
#     napis=str(bin(liczba))[2:]
#     for literka in napis:
#         suma+=int(literka)
#     return(prime(suma))

# suma=0
# for el in plik:
#     liczba=int(el)
#     suma+=super_b_prime(liczba)
# print(suma)
    

# # b.1
# def suma_cyfr(liczba):
#     suma=0
#     napis=str(liczba)
#     for literka in napis:
#         suma+=int(literka)
#     if prime(suma)==0:
#         return 0
#     else:
#         return 1
    
# suma=0
# for el in plik:
#     liczba=int(el)
#     suma+=suma_cyfr(liczba)
# print(suma)

# # b.2
# def super_b_prime_b(liczba):
#     if prime(liczba)==0:
#         return 0
#     suma=0
#     napis=str(bin(liczba))[2:]
#     for literka in napis:
#         suma+=int(literka)
#     if prime(suma):
#         return liczba

# plik=open('2.txt')
# l1=0
# suma_b=0
# for el in plik:
#     liczba=int(el)
#     suma_b+=super_b_prime_b(liczba)
# print(prime(suma_b))

import math

def prime(number):
    if number<2:
        return 0
    for i in range(2, int(math.sqrt(number))+1):
        if number%i==0:
            return 0
    return 1

def superprime(number):
    if prime(number) == 0:
        return 0
    suma = 0
    napis = str(number)
    for letter in napis:
        suma += int(letter)
    if prime(suma) == 0:
        return 0
    return prime(suma)

def super_b_prime(number):
    if superprime(number) == 0:
        return 0
    suma = 0
    napis = str(bin(number))[2:]
    for letter in napis:
        suma += int(letter)
    return prime(suma)

def sum_digits(number):
    sum = 0
    napis = str(number)
    for letter in napis:
        sum += int(letter)
    return sum

l1 = l2 = l3 = lp = 0
with open ('Ad5_1.txt', 'r') as file1, open ('Ad5_2.txt', 'r') as file2, open ('Ad5_3.txt', 'r') as file3:
    for line in file1:
        a = int(line)
        if super_b_prime(a):
            l1 += 1
    for line in file2:
        if super_b_prime(a):
            l2 += 1
    for line in file3:
        if super_b_prime(a):
            l3 += 1
    for i in range(100, 10000 + 1):
        if prime(sum_digits(i)):
            lp += 1
print('A)','1.',l1,'2.', l2,'3.', l3)
print('B)','1.',lp)