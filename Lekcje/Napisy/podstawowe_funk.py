def lower(napis):
    for literka in napis:
        if not 'a'<=literka<='z':
            return 0
    return 1

def upper(napis):
    for literka in napis:
        if not 'A'<=literka<='Z':
            return 0
    return 1

def rosnacy(napis):
    napis=napis.lower()
    for i in range(len(napis)-1):
        if not napis[i+1]>napis[i]:
            return 0
    return 1

def nierosnacy(napis):
    napis=napis.lower()
    for i in range(len(napis)-1):
        if not napis[i+1]<napis[i]:
            return 0
    return 1

plik=open('napis.txt')
wyrazy=plik.read().split()
l=0
for wyraz in wyrazy:
    l+=rosnacy(wyrazy)
print(l)