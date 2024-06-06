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
