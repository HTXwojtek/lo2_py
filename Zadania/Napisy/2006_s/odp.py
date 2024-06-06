# Otwarcie pliku i odczytanie zawartości
with open('dane.txt', 'r') as file:
    zawartosc = file.read().splitlines()

#zad 1
licznik = {}
for slowo in zawartosc:
    if slowo in licznik:
        licznik[slowo] += 1
    else:
        licznik[slowo] = 1
najwiecej_wystapien = max(licznik, key=licznik.get)
powtarzajace_sie_slowa = []
for slowo in licznik:
    if licznik[slowo] > 1:
        powtarzajace_sie_slowa.append(slowo)
ilosc_powtarzajacych_sie_slow = len(powtarzajace_sie_slowa)

#zad 2
def czy_parzysta(szesnastkowa):
    dziesietna = int(szesnastkowa, 16)
    return dziesietna % 2 == 0
liczba_parzystych = 0
for liczba in zawartosc:
    if czy_parzysta(liczba):
        liczba_parzystych += 1

#zad 3
def czy_palindrom(slowo):
    return slowo == slowo[::-1]
liczba_palindromow = 0
for slowo in zawartosc:
    if czy_palindrom(slowo):
        liczba_palindromow += 1


with open('wyniki1.txt', 'a') as file:
    file.write(f"a) {str(ilosc_powtarzajacych_sie_slow)}\n")
    file.write(f"{najwiecej_wystapien}\n")
    file.write(f"{licznik[najwiecej_wystapien]}\n")
    file.write(f"b) {liczba_parzystych}\n")
    file.write(f"c) {liczba_palindromow}\n")