from math import sqrt
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

def odl_pkt_odc(xa:float,ya:float,xb:float,yb:float,xc:float,yc:float):
    A = yb - ya
    B = xa - xb
    C = xb * ya - xa * yb
    odleglosc=abs(A*xc+B*yc+C)/sqrt(A**2+B**2)
    t=((xc-xa)*(xb-xa)+(yc-ya)*(yb-ya))/((xb-xa)**2+(yb-ya)**2)
    #wyznaczam współrzędne rzutu punktu C na odcinek AB (wsp. punktu D)
    xd=xa+t*(xb-xa)
    yd=ya+t*(yb-ya)
    if spr_pkt_odc(xa,ya,xb,yb,xd,yd)==True:
        return odleglosc
    else:
        odl_A=sqrt((xc-xa)**2+(yc-ya)**2)
        odl_B=sqrt((xc-xb)**2+(yc-yb)**2)
        return min(odl_A,odl_B)

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
    print(f"Odległość punktu C od odcinka AB wynosi: {odl_pkt_odc(xa,ya,xb,yb,xc,yc)}")