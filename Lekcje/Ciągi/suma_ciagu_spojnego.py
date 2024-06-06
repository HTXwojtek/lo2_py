def suma_kadane(tab):
    najdotejpory = najsuma = tab[0]
    for liczba in tab[1:]:
        najdotejpory = max(liczba, najdotejpory + liczba)
        najsuma = max(najsuma, najdotejpory)
    return najsuma

print(suma_kadane([1, 2, -3, 4, -1, 2, 1, -5, 4]))  # 6
print(suma_kadane([1, 2, -3, 4, -1, 2, 1, -5, 4, 1]))  # 7
print(suma_kadane([1, 2, -3, 4, -1, 2, 1, -5, 4, 1, 2]))  # 8

#Złożoność czasowa: O(n)