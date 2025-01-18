import random
def bubble(tab):
    straznik=1
    licznik=0
    for i in range(len(tab)):
        if straznik==0:
            break
        straznik=0
        for j in range(len(tab)-1):
            if tab[j]>tab[j+1]:
                tab[j],tab[j+1]=tab[j+1],tab[j]
                licznik+=1
                straznik=1
    return tab, licznik

tab=[]
for i in range(15):
    tab.append(random.randint(0,100))
print(bubble(tab)[1])

            
