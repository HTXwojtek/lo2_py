import math

def sito(tab):
    for i in range(2, int(math.sqrt(len(tab))+1)):
        if tab[i]:
            for a in range(i+i, len(tab), i):
                tab[a]=0

tab=[1]*100
tab[0],tab[1]=0,0
sito(tab)
