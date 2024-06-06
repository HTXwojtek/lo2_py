# bubblesort
def sortuj(napis):
    tab=list(napis)
    for j in range(len(tab)):
        for i in range(len(tab)-1-j):
            if tab[i].lower()>tab[i+1].lower():
                tab[i],tab[i+1]=tab[i+1],tab[i]
    return "".join(tab)

nap="pies"
print(sortuj(nap))