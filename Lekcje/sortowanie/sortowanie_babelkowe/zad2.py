import random
def bubble(tab):
    straznik=1
    for i in range(len(tab)):
        if straznik==0:
            break
        straznik=0
        for j in range(len(tab)-1):
            if tab[j]>tab[j+1]:
                tab[j],tab[j+1]=tab[j+1],tab[j]
            straznik=1
    return tab

tab=[]
for i in range(20):
    tab.append(random.randint(1, 9999999))
    
print(bubble(tab))