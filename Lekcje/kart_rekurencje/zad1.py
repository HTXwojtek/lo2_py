def zad1(n):
    if n==1:
        return -1
    elif n>1:
        return -(zad1(n-1))*n-3

print('zad1:', zad1(4))