#czy liczby sa lustrzane np. 123 321
def lustrzane(a,b):
    if str(a)==str(b)[::-1]:
        return 1
    return 0

#anagramy
def anagram(a,b):
    if sorted(str(a))==sorted(str(b)):
        return 1
    return 0

#najdłuższa rosnącą serię liczb w pliku
plik=open('dane.txt')
# WAZNE!
tab=list(map(int, plik.read().split()))

seria=maxseria=1
for i in range(len(tab)-1):
    if tab[i+1]>tab[i]:
        seria+=1
        if seria>maxseria:
            maxseria=seria
    else:
        seria=1

print(maxseria)

#liczba z najwieksza iloscia anagramow w pliku
tab=[123,213,332,233,321,223]
maxseria=1
for i in range(0, len(tab)):
    liczba=tab[i]
    seria=1
    for j in range(i+1, len(tab)):
        if sorted(str(liczba))==sorted(str(tab[j])):
            seria+=1
        
        if seria>maxseria:
            maxseria=seria
            maxliczba=liczba
print(maxseria, maxliczba)

