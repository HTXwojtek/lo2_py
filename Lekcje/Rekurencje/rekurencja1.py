# Program odliczający od n do zera
import time
# Odliczanie w sposób iteracyjny
def odliczanie_it(ile):
    for i in reversed(range(1,11)):
        print(i)
        time.sleep(0.5)
    print("KONIEC")

# Odliczanie w sposób rekurencyjny

def odliczanie_rek(ile):
    if (ile == 0):
        print("KONIEC")
    else:
        print(ile)
        time.sleep(0.5)
        odliczanie_rek(ile-1)

# Wywołanie funkcji
odliczanie_it(15)
odliczanie_rek(10)
