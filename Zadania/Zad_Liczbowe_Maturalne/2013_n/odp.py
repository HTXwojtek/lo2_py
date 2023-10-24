l1 = 0
tab = []
with open ('dane_anagramy.txt', 'r') as file:
    for line in file:
        a, b = line.split()
        if sorted(a) == sorted(b):
            l1 += 1
        tab.append(a)
        tab.append(b)

maxanagram = 1
for i in range(len(tab)):
    anagram = 1
    number = tab[i]
    for j in range(i+1, len(tab)):
        if sorted(number) == sorted(tab[j]):
            anagram += 1
    if maxanagram < anagram:
        maxanagram = anagram

print(l1)
print(maxanagram)