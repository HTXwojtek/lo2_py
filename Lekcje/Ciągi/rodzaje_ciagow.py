def czy_geometryczny(tab):
    q = tab[1] / tab[0]
    for i in range(1, len(tab)):
        if tab[i] / tab[i - 1] != q:
            return False
    return True

def czy_arytmetyczny(tab):
    r = tab[1] - tab[0]
    for i in range(1, len(tab)):
        if tab[i] - tab[i - 1] != r:
            return False
    return True

print(czy_geometryczny([3,9,27,81])) # True
print(czy_arytmetyczny([3,9,27,81])) # False
print(czy_geometryczny([3,6,9,12])) # False
print(czy_arytmetyczny([3,6,9,12])) # True

def czy_rosnacy(tab):
    for i in range(1, len(tab)):
        if tab[i] <= tab[i - 1]:
            return False
    return True

def czy_malejacy(tab):
    for i in range(1, len(tab)):
        if tab[i] >= tab[i - 1]:
            return False
    return True

print(czy_rosnacy([1,2,3,4])) # True
print(czy_malejacy([1,2,3,4])) # False
print(czy_malejacy([8,4,2,0])) # True
print(czy_rosnacy([8,4,2,0])) # False