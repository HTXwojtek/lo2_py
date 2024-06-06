def srednia(tab):
    q = len(tab)
    p = 0
    for element in tab:
        p += element
    return p/q

print(srednia([1,2,3,4,5,6,7,8,9,10])) # 5.5

def mediana(tab):
    tab.sort()
    if len(tab) % 2 == 0:
        return (tab[len(tab)//2 - 1] + tab[len(tab)//2]) / 2
    return tab[len(tab)//2]

print(mediana([1,2,3,4,5,6,7,8,9,10])) # 5.5
print(mediana([1,2,3,4,5,6,7,8,9])) # 5

def dominanta(tab):
    max_l = max_el = 0
    max_els = []
    for i in range(len(tab)):
        l = 0
        for j in range(i, len(tab)):
            if tab[i] == tab[j]:
                l += 1
        if l > max_l:
            max_l = l
            max_el = tab[i]

    for i in range(len(tab)):
        l = 0
        for j in range(i, len(tab)):
            if tab[i] == tab[j]:
                l += 1
        if l == max_l and tab[i] not in max_els:
            max_els.append(tab[i])

    return max_els
print(dominanta([1,1,1,1,2,2,3,4,4,4,4,1,1,2,2,6,7,8,2])) # [1]
print(dominanta([1,1,1,1,2,2,3,4,4,4,4,1,1,2,2,6,7,8,2,4,4])) # [1, 4]

def lider_zbioru(tab):
    kandydaci = dominanta(tab)
    for kandydat in kandydaci:
        l=0
        for i in range(len(tab)):
            if tab[i] == kandydat:
                l+=1
        if l > len(tab) / 2:
            return kandydat

print(lider_zbioru([2,2,1,1,1,2,2,2])) # 2
print(lider_zbioru([1,2])) # None
print(lider_zbioru([1,2,3,4,5,1,1,1,5,5,5,5,5,5,5])) # 5