def punkt_w_prostokacie(x:float,y:float,x1:float,y1:float,x2:float,y2:float):
    return (min(x1,x2)<=x<=max(x1,x2)) and (min(y1,y2)<=y<=max(y1,y2))

punkt=(3,4)
wierzcholek1=(1,1)
wierzcholek2=(5,5)

if punkt_w_prostokacie(punkt[0],punkt[1],wierzcholek1[0],wierzcholek1[1],wierzcholek2[0],wierzcholek2[1]):
    print("Punkt nalezy do prostokata")
else:
    print("Punkt nie nalezy do prostokata")
