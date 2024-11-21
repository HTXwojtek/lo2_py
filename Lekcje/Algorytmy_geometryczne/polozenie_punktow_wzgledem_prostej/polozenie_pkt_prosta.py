import math
def prosta_ogolna(a:float, b:float,c:float, xp:float,yp:float):
    if a*xp+b*yp+c==0:
        print(f"Punkt ({xp},{yp}) leży na prostej {a}x+{b}y+c=0")
    else:
        print(f"Punkt ({xp},{yp}) nie leży na prostej {a}x+{b}y+c=0")

print("Wczytuję współczynniki A, B i C prostej Ax+By+C=0")
d=float(input("Podaj A: "))
e=float(input("Podaj B: "))
f=float(input("Podaj C: "))

print("Wczytuję współrzędne punktu (xp,yp)")
xp=float(input("Podaj xp: "))
yp=float(input("Podaj yp: "))


def odleglosc_pkt(a:float, b:float, c:float, xp:float, yp:float):
    d=float(abs(a*xp+b*yp+c)/math.sqrt(a**2+b**2))
    print(f"Odległość ({xp},{yp}) od prostej {a}x+{b}+c=0 wynosi: {d}")

print("Wczytuję współczynniki A, B i C prostej Ax+By+C=0")
d=float(input("Podaj A: "))
e=float(input("Podaj B: "))
f=float(input("Podaj C: "))

print("Wczytuję współrzędne punktu (xp,yp)")
xp=float(input("Podaj xp: "))
yp=float(input("Podaj yp: "))
odleglosc_pkt(d,e,f,xp,yp)
