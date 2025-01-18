plik=open('dane.txt')
linia=plik.readline().strip()
liczby=[]
for liczba in linia.split():
    liczby.append(int(liczba))

def reverse(tab):
    if len(tab) == 0:
        return []
    else:
        return [tab[-1]] + reverse(tab[:-1])
    
print(*reverse(liczby))
