max = -1000000
min = 1000000
suma = suma2 = suma3 = liniamax = liniamin = 0
linia = 1

with open ('liczby.txt', 'r') as file:
    for line in file:
        liczba_jedynek = 0
        napis = str(int(line))
        for letter in napis:
            liczba_jedynek += int(letter)
        zeros_sum = len(str(line.strip()))-liczba_jedynek
        if zeros_sum > liczba_jedynek:
            suma += 1
with open ('Ad4_015.txt', 'r') as file:
    for line in file:
        number = int(line, 2)
        if number % 2 == 0:
            suma2 += 1
            if number % 8 == 0:
                suma3 += 1
with open ('Ad4_015.txt', 'r') as file:
    for line in file:
        number=(int(line, 2))
        if number>max:
            max = number
            liniamax = linia
        elif number<min:
            min = number
            liniamin = linia
        linia+=1

print('4.1.', suma)
print('4.2.', 'liczb podzielnych przez 2:', suma2, 'liczb podzielnych przez 8:', suma3)
print('4.3.',' Największa liczba to:', max,'w linii', liniamax, 'Najmniejsza liczba to:' , min, 'w linii', liniamin)