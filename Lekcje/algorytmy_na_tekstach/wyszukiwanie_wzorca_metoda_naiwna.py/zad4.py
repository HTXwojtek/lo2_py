def wyszukaj_wzorzec_plik(nazwa_pliku,wzorzec):
    with open(nazwa_pliku, 'r') as plik:
        linie=plik.readlines()
    
    znalezione_linie=[]
    numer_linii=1

    for linia in linie:
        if wzorzec in linia.lower():
            znalezione_linie.append(numer_linii)
        numer_linii+=1
    
    return znalezione_linie 

plik=input('Podaj nazwe pliku: ').lower() # dokument.txt
wzorzec=input('Podaj wzorzec: ').lower() # Python
wynik=wyszukaj_wzorzec_plik(plik,wzorzec)
if wynik:
    print(f'Wzorzec {wzorzec} w pliku: {plik} znaleziono w liniach: {wynik} ')
else:
    print('Wzorzec nie zostal znaleziony')