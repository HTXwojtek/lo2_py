# Przykładowe dane wejściowe
# 4
# 1 2
# 3 1
# 3 2
# 4 3
# 1 4
# 4 2

#JEST TO ALGORYTM, GDZIE TABLICE W TABLICY OZNACZAJĄ, PRZEZ KTÓRE OSOBY DANA OSOBA JEST ZNANA
#Przykładowo, gdy osoba nr. 1 jest znana przez osoby 2, i 3 to tab[0] = [False, True, True, False]

def idol(tab, osoby):
    for i in range(osoby):
        for j in range(osoby):
            if tab[i][j] == False and j != i:
                break
            elif j == osoby - 1:
                for k in range(osoby):
                    if tab[k][i] == True and k != i:
                        break
                    elif k == osoby - 1:
                        return i+1

tab = [[False, False, True, True], [True, False, True, True], [False, False, False, True], [False, False, False, False]]
osoby = 4
                    
print(idol(tab, osoby)) # 2
        
tab = [[False, False, True, False, False, False], [False, True, False, False, False, True], [False, False, False, False, False, False], [True, True, True, False, True, True], [False, False, False, False, False, False], [False, False, False, False, False, False]]
osoby = 6

print(idol(tab, osoby)) # 4