def pole_tr(x1,y1,x2,y2,x3,y3):
    return abs((x1*(y2-y3)+x2*(y3-y1)+x3*(y1-y2))/2.0)

def punkt_w_trojkacie(x,y,x1,y1,x2,y2,x3,y3):
    pole_podst=pole_tr(x1,y1,x2,y2,x3,y3)
    print(f'Pole trojkata ABC: {pole_podst}')
    pole1=pole_tr(x,y,x2,y2,x3,y3)
    pole2=pole_tr(x1,y1,x,y,x3,y3)
    pole3=pole_tr(x1,y1,x2,y2,x,y)
    print(f'Pole trojkata 1: {pole1}, Pole trojkata 2: {pole2}, Pole trojkata 3 {pole3}, Suma: {pole1+pole2+pole3}')
    return pole_podst==(pole1+pole2+pole3)

punkt=(3,4)
w1=(0,0)
w2=(5,0)
w3=(0,5)
if punkt_w_trojkacie(punkt[0], punkt[1], w1[0],w1[1],w2[0],w2[1],w3[0],w3[1]):
    print('Punkt nalezy do trojkata')
else:
    print('Punkt nie nalezy do trojkata')