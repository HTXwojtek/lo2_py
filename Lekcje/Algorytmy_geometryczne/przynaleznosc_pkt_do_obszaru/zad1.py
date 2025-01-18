from math import sqrt

def punkt_w_pierscieniu(x,y,xs,ys,r1,r2):
    odleglosc=sqrt((x-xs)**2+(y-ys)**2)
    return min(r1,r2)<=odleglosc<=max(r1,r2)

punkt=(4,3)
srodek=(2,3)
promien1=2
promien2=4

if punkt_w_pierscieniu(punkt[0],punkt[1],srodek[0],srodek[1], promien1,promien2):
    print("Punkt nalezy do okregu.")
else:
    print("Punkt nie nalezy do okregu.")