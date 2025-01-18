import random

def pkt_w_trojkacie(x,y):
    if y>=0 and y<=(2*x)+6 and y<=(-3*x)+6:
        return True
    return False

def pole_trojkata_monte_carlo(ilosc_pkt):
    trafienia=0
    for _ in range(ilosc_pkt):
        x=random.uniform(0,3)
        y=random.uniform(0,6)
        if pkt_w_trojkacie(x,y):
            trafienia+=1

    pole_prostokata=3*6
    pole_trojkata=(trafienia/ilosc_pkt)*pole_prostokata
    return pole_trojkata

ilosc_pkt=10000
pole=pole_trojkata_monte_carlo(ilosc_pkt)
print(f'Oszacowane pole trójkąta wynosi: {pole}')
    

    





