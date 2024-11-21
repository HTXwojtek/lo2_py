import math
# def spr_pkt_odc(xa:float, ya:float,xb:float, yb:float,xc:float,yc:float):
#     # wyznaczamy współczynniki prostej Ax+Bx+C=0
#     A=yb-ya
#     B=xa-xb
#     C=xb*ya-xa*yb
#     # sprawdzam, czy pkt C lezy na prostej Ax+Bx+c=0
#     if A*xc+B*yc+C!=0:
#         return False
#     if min(xa,xb)<=xc<=max(xa,xb) and min(ya,yb)<=yc<=max(ya,yb):
#         return True
#     else:
#         return False
    

def spr_pkt_odc(xa:float, ya:float,xb:float, yb:float,xc:float,yc:float):
    A=yb-ya
    B=xa-xb
    C=xb*ya-xa*yb
    if min(xa,xb)<=xc<=max(xa,xb) and min(ya,yb)<=yc<=max(ya,yb):
        if A*xc+B*yc+C==0:
            return 'pkt nalezy do prostej'
        return abs(A*xc+B*yc+C)/math.sqrt(A**2+B**2)
    return f'odleglosc od prostej {min(math.sqrt((xb-xc)**2+(yb-yc)**2),math.sqrt((xa-xc)**2+(ya-yc)**2))}'


xa=float(input("Podaj xa: "))
ya=float(input("Podaj ya: "))
xb=float(input("Podaj xb: "))
yb=float(input("Podaj yb: "))
xc=float(input("Podaj xc: "))
yc=float(input("Podaj yc: "))

# if spr_pkt_odc(xa,ya,xb,yb,xc,yc):
#     print("Punkt C należy do odcinka AB")
# else:
#     print("Punkt C nie należy do odcinka AB")


print(spr_pkt_odc(xa,ya,xb,yb,xc,yc))