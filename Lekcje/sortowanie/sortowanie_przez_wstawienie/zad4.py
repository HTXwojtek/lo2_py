def sort_wstawienie(tab):
    for i in range(1, len(tab)):
        key=tab[i]
        j=i-1
        while j>=0 and tab[j]>key:
            tab[j+1]=tab[j]
            j-=1
        tab[j+1]=key
    return tab


# generator tablicy
# import random
# tablica = [
#     [random.randint(1, 100) for _ in range(5)] for _ in range(5)
# ]
# print(tablica)

macierz=[[40, 55, 34, 14, 29], [52, 68, 33, 37, 47], [94, 27, 87, 26, 13], [36, 74, 83, 99, 96], [44, 49, 98, 41, 62]]
