import math
plik=open('dane.txt')
wyniki=open('wyniki.txt','w')

def prosta_ogolna(a:float, b:float,c:float, xp:float,yp:float):
    if a*xp+b*yp+c==0:
        return 'TAK'
    else:
        return 'NIE'

def odleglosc_pkt(a:float, b:float, c:float, xp:float, yp:float):
    d=float(abs(a*xp+b*yp+c)/math.sqrt(a**2+b**2))
    return d


# wyniki.write('wyniki')
for linia in plik:
    a,b,c,xp,yp=map(float, linia.split())
    wyniki.write(f'{a}x+{b}y+C=0 ({xp},{yp})\t\tCzy nalezy: {prosta_ogolna(a,b,c,xp,yp)}\t\todleglosc pkt: {odleglosc_pkt(a,b,c,xp,yp)}\n')


