def wyszukaj_wzorzec(tekst,wzorzec):
    dl_tekstu=len(tekst)
    dl_wzorzec=len(wzorzec)
    pozycje=[]
    if dl_wzorzec>dl_tekstu:
        print('Wzorzec msui byc krotszy od tekstu')
    else:
        for i in range(len(tekst)-len(wzorzec)+1):
            if tekst[i:i+dl_wzorzec]==wzorzec:
                pozycje.append(i)
        return pozycje


tekst=input('Podaj tekst: ').lower() # Anna Tomasz Anna Jan Maria Anna
wzorzec=input('Podaj wzorzec: ').lower() # Anna
wynik=wyszukaj_wzorzec(tekst,wzorzec)
if wynik:
    print(f'Wzorzec {wzorzec} znaleziono na pozycjach: {wynik}\nŁączna liczba wystąpień: {len(wynik)}')
else:
    print('Wzorzec nie zostal znaleziony')
