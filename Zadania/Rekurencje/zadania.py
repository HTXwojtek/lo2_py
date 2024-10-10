# zad 1
# def ciag_itr(n):
#     wyraz=(-3+(5*(n-1)))
#     return wyraz

# def ciag_rek(n):
#     if n==1:
#         return -3
#     else:
#         return ciag_rek(n-1)+5
    
# print('iteracyjnie:', ciag_itr(5))
# print('rekurencyjnie:', ciag_rek(5))

#zad 2
# def na_bin_itr(n):
#     suma=''
#     while n>0:
#         if n%2==0:
#             suma+='0'
#             n=n//2
#         elif n%2:
#             suma+='1'
#             n=n//2
#     return suma[::-1]

# def na_bin_rek(n):
#     suma=''
#     if n==0:
#         return suma
#     elif n%2==0:
#         suma+='0'
#     elif n%2:
#         suma+='1'
#     suma+=na_bin_rek(n//2)
#     return suma
        

# print('iteracyjny', na_bin_itr(20))
# print('rekurencyjny', na_bin_rek(20)[::-1])


#zad 3
# def funk_rek(n):
#     if n==1:
#         return 1
#     if n==2:
#         return 2
#     else:
#         return funk_rek(n-1)-funk_rek(n-2)+3
    
# print(funk_rek(6))


#zad 4
# def nwd_itr(a,b):
#     while a:
#         a,b=b%a,a
#     return b

# def nwd_rek(a,b):
#     if a==b:
#         return a
#     if b>a:
#         a,b=b,a
#     a-=b
#     return nwd_rek(a,b)

# print('iteracyjny', nwd_itr(5,3))
# print('rekurencyjny', nwd_rek(5,3))

#zad 5
# def geo_itr(n):
#     wynik=128
#     for i in range(n-1):
#         wynik=wynik*0.25
#     return wynik

# def geo_rek(n):
#     if n==1:
#         return 128
#     else: 
#         return int(geo_rek(n-1)/4)

# print('iteracyjny', geo_itr(3))
# print('rekurencyjny', geo_rek(3))


#zad 6
def nwd6_itr(a,b):
    while a:
        a,b=b%a,a
    return b

def nwd6_rek(a,b):
    if b>a:
        a,b=b,a
    if b==0:
        return a
    a=a%b
    if a==b:
        return a
    else:
        return nwd6_rek(a,b)

print('iteracyjny', nwd6_itr(5,3))
print('rekurencyjny', nwd6_rek(5,3))