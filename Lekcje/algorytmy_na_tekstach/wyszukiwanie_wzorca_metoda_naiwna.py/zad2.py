def wyszukaj_wzorzec(tekst,wzorzec):
    dl_tekstu=len(tekst)
    dl_wzorzec=len(wzorzec)
    pozycje=0
    if dl_wzorzec>dl_tekstu:
        print('Wzorzec msui byc krotszy od tekstu')
    else:
        for i in range(len(tekst)-len(wzorzec)+1):
            if tekst[i:i+dl_wzorzec]==wzorzec:
                pozycje+=1
        return pozycje


tekst=input('Podaj tekst: ').upper() # ACTGACTGCTAGCTAGACTG
wzorzec=input('Podaj wzorzec: ').upper() # CTG
wynik=wyszukaj_wzorzec(tekst,wzorzec)
if wynik:
    print(f'Wzorzec {wzorzec} występuje {wynik} razy w sekwencji DNA')
else:
    print('Wzorzec nie zostal znaleziony')
