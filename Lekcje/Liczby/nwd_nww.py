#nwd
def nwd(a,b):
    while b!=0:
        a,b=b,a%b
    return a

#nww
def nww(a,b):
    return a*b//nwd(a,b)

#nww - metoda bez uzyca nwd()
def nww2(a,b):
    a1,b1=a,b
    while a!=b:
        if a>b:
            b+=b1
        else:
            a+=a1
    return a