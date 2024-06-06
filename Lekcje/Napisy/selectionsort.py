# selectionsort
def sortuj(napis):
    tab=list(napis)
    for j in range(0, len(tab)):
        max=j
        for i in range(j, len(tab)):
            if tab[max]>tab[i]:
                max=i
        tab[max],tab[j]=tab[j],tab[max]
    return "".join(tab)

nap='pies'
print(sortuj(nap))