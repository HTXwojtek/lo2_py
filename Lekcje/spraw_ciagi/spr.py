plik = open('lider.txt')

for linia in plik:
    a = list(map(int, linia.split()))
    print(a)

# zad 1
def mediana(tab):
    tab.sort()
    if len(tab) % 2 == 0:
        return (tab[len(tab) // 2 - 1] + tab[len(tab) // 2]) / 2
    return tab[len(tab) // 2]
    
print("Mediana:", mediana(a))


def find_min_max(tab):
    if len(tab)==1:
        return tab[0], tab[0]
    if len(tab)==2:
        return min(tab[0], tab[1]), max(tab[0], tab[1])
    
    mid=len(tab) // 2
    min1, max1 = find_min_max(tab[:mid])
    min2, max2 = find_min_max(tab[mid:])
    
    return min(min1, min2), max(max1, max2)

najmniejszy, najwiekszy = find_min_max(a)
print("najmniejszy element:", najmniejszy)
print("najwiekszy element:", najwiekszy)

# zad 2
def dominanta(tab):
    max_l=max_el=0
    max_els=[]
    for i in range(len(tab)):
        l=0
        for j in range(i, len(tab)):
            if tab[i]==tab[j]:
                l+=i
        if l>max_l:
            max_l=l
            max_el=tab[i]
    
    for i in range(len(tab)):
        l=0
        for j in range(i, len(tab)):
            if tab[i]==tab[j]:
                l+=i
        if l==max_l and tab[i] not in max_els:
            max_els.append(tab[i])
    return max_els

def lider(tab):
    kandydaci=dominanta(tab)
    for kandydant in kandydaci:
        l=0
        for i in range(len(tab)):
            if tab[i]==kandydant:
                l+=1
        if l>len(tab) / 2:
            return kandydant

print("lider:", lider(a))

# zad 3
def wyszukiwanie_binarne(tab, x):
    lewy, prawy=0, len(tab)-1
    while lewy<=prawy:
        srodek=(lewy + prawy)//2
        if tab[srodek]==x:
            return True
        elif tab[srodek]<x:
            lewy=srodek+1
        else:
            prawy=srodek-1
    return False

szukana_liczba=int(input("podaj liczbe: "))
znaleziono=wyszukiwanie_binarne(a, szukana_liczba)

if znaleziono:
    print(f"liczba {szukana_liczba} znajduje się w pliku")
else:
    print(f"liczba {szukana_liczba} nie znajduje się w pliku")


#zad 4
plik_bit=open('bitcoin.txt')
dane_bit=[]
for linia in plik_bit:
    dane_bit.append(list(map(int, linia.split())))

def najdluzsza_hossa(dane):
    najdluzsza_hossa_dlugosc=0
    najdluzsza_hossa_miesiac=0
    najdluzsza_hossa_poczatek=0
    najdluzsza_hossa_koniec=0
    
    for miesiac in range(len(dane)):
        dlugosc_hossy=0
        max_dlugosc_hossy=0
        poczatek_hossy=0
        
        for dzien in range(1, len(dane[miesiac])):
            if dane[miesiac][dzien]>dane[miesiac][dzien-1]:
                if dlugosc_hossy==0:
                    poczatek_hossy=dzien-1
                dlugosc_hossy+=1
            else:
                if dlugosc_hossy>max_dlugosc_hossy:
                    max_dlugosc_hossy=dlugosc_hossy
                    koniec_hossy=dzien-1
                    poczatek_hossy_koniec=poczatek_hossy
                dlugosc_hossy=0
        
        if dlugosc_hossy>max_dlugosc_hossy:
            max_dlugosc_hossy=dlugosc_hossy
            koniec_hossy=dzien-1
            poczatek_hossy_koniec=poczatek_hossy

        if max_dlugosc_hossy>najdluzsza_hossa_dlugosc:
            najdluzsza_hossa_dlugosc=max_dlugosc_hossy
            najdluzsza_hossa_miesiac= miesiac
            najdluzsza_hossa_poczatek=poczatek_hossy_koniec
            najdluzsza_hossa_koniec=koniec_hossy
    
    return najdluzsza_hossa_dlugosc, najdluzsza_hossa_miesiac + 1, najdluzsza_hossa_poczatek, najdluzsza_hossa_koniec

dlugosc_hossy,miesiac_hossy,poczatek_hossy,koniec_hossy=najdluzsza_hossa(dane_bit)
print(f"najdłuzsza hossa trwala {dlugosc_hossy} dni w miesiacu {miesiac_hossy}")


def zarobek_na_hossie(dane, miesiac, poczatek, koniec):
    poczatkowa_wartosc=dane[miesiac][poczatek]
    koncowa_wartosc=dane[miesiac][koniec]
    ilosc_bitcoinow=100000/poczatkowa_wartosc
    kwota_koncowa=ilosc_bitcoinow*koncowa_wartosc
    zarobek=kwota_koncowa-100000
    return round(zarobek)

zarobek = zarobek_na_hossie(dane_bit, miesiac_hossy - 1, poczatek_hossy, koniec_hossy)
print(f"inwestor zarobil {zarobek} dolarow na najluzszej hossie")


























