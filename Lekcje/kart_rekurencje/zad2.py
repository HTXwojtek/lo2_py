def catalan(n):
    if n==0:
        return 1
    else:
        return (((4*n)+2)/(n+2))*catalan(n-1)
    


i=0
parzyste=nieparzyste=0
while True:
    l=catalan(i)
    if l>1000000.0:
        break
    print(l)
    if l%2==0:
        parzyste+=1
    else:
        nieparzyste+=1
    i+=1
print('parzyste:', parzyste, 'nieparzyste:', nieparzyste)