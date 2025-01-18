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

print(bubble([2,4,3,5,6,1]))
            