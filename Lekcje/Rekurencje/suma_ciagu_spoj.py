tab=[4,-2,8,-4,3,6,-2,5]
maxsuma=0
for k in range(len(tab)):
    suma=0
    liczby=''
    for i in range(k, len(tab)):
        suma+=tab[i]
        liczby+=str(tab[i])+' '
    if suma>maxsuma:
        maxsuma=suma
        maxliczby=liczby # tab[k:(i+1)]
print(f'suma: {maxsuma}, ciąg tej sumy: {maxliczby}')
plik=open('')