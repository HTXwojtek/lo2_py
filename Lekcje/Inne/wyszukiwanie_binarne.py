# do wyszukiwania binarnego potrzebujemy posortowanej listy

def wyszukiwanie(tab, el):
    lewo = 0
    prawo = len(tab) - 1

    while lewo <= prawo:
        srd = (lewo + prawo) // 2
        kandydat = tab[srd]
        if kandydat == el:
            return srd
        if kandydat > el:
            prawo = srd - 1
        else:
            lewo = srd + 1
    return None