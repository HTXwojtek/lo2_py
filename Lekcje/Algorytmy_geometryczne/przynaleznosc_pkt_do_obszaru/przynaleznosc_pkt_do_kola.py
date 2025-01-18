from math import sqrt

def punkt_w_kole(x,y,xs,ys,r):
    odleglosc=sqrt((x-xs)**2+(y-ys)**2)
    return odleglosc<=r

punkt=(4,3)
srodek=(2,3)
promien=2

if punkt_w_kole(punkt[0],punkt[1],srodek[0],srodek[1], promien):
    print("Punkt nalezy do kola.")
else:
    print("Punkt nie nalzey do kole.")

