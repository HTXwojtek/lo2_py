def spr_pkt_odc(xa:float,ya:float,ab:float,yb:float,xc:float,yc:float):
    #wyznaczmy współczynniki prostej Ax+By+C=0
    A=yb-ya
    B=xa-xb
    C=xb*ya-xa*yb
    #Sprawdzam, czy pkt C lezy na prostej Ax+By+C=0
    if A*xc+B*yc+C!=0:
        return False
    if min(xa,xb)<=xc<=max(xa,xb) and min(ya,yb)<=yc<=max(ya,yb):
        return True
    else:
        return False

xa=float(input("Podaj xa: "))
ya=float(input("Podaj ya: "))
xb=float(input("Podaj xb: "))
yb=float(input("Podaj yb: "))
xc=float(input("Podaj xc: "))
yc=float(input("Podaj yc: "))

if spr_pkt_odc(xa,ya,xb,yb,xc,yc):
    print("Punkt C należy do odcinka AB.")
else:
    print("Punkt C nie należy do odcinka AB.")

