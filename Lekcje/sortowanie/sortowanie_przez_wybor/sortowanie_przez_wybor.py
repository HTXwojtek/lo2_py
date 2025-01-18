def sort_wybor(tab):
    licznik=0
    for i in range(len(tab)):
        min_indeks=i
        for j in range(i+1, len(tab)):
            if tab[j]<tab[min_indeks]:
                min_indeks=j
                licznik+=1
        tab[i],tab[min_indeks]=tab[min_indeks],tab[i]
    return tab, licznik

tab=[21312,54,57,8,3,4,6,7,1]
print(f'Ilosc powtorzen: {sort_wybor(tab)[1]}')
print(sort_wybor(tab)[0])