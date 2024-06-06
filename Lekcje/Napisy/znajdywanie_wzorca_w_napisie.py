napis="ala ma kota a kot ma ale"
wzorzec="kot"
tab=[]

for i in range(len(napis)-len(wzorzec)-1):
    if wzorzec[0]==napis[i]:
        znaleziono=True
        for j in range(len(wzorzec)):
            if not wzorzec[j]==napis[i+j]:
                znaleziono=False
                break
        if znaleziono:
            tab.append(i)

if len(tab):
    print('znaleziono od pozycji:', *tab)
else:
    print('nie znaleziono') 
