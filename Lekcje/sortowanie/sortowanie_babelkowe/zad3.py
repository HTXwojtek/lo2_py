plik=open('sortowanie_babelkowe/liczby1.txt')
tab=[]
for linia in plik:
    tab.append(int(linia))

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

print(bubble(tab))
            