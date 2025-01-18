def sort_wstawienie(tab):
    for i in range(1, len(tab)):
        key=tab[i]
        j=i-1
        while j>=0 and tab[j]<key:
            tab[j+1]=tab[j]
            j-=1
        tab[j+1]=key
    return tab


tab=[8,4,6,2,5]
print(f'{sort_wstawienie(tab)}')