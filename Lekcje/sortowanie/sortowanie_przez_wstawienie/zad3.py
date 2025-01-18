def sort_wstawienie(tab):
    przez=0
    for i in range(1, len(tab)):
        key=tab[i]
        j=i-1
        while j>=0 and tab[j]>key:
            tab[j+1]=tab[j]
            przez+=1
            j-=1
        tab[j+1]=key
    return tab, przez


tab=[8,4,6,2,5]
wynik=sort_wstawienie(tab)
print(f'{wynik[0]}, ilosc przesunieć: {wynik[1]}')