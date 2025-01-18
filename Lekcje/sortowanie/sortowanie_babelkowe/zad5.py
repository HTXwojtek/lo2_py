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

plik=open('sortowanie/sortowanie_babelkowe/liczby2.txt')
tab=[]
for i in range(len(plik.read())):
    for linia in plik:
        tab.append(linia.split())
    print(tab)
  