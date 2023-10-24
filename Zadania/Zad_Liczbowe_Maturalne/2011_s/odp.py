l1 = l2 = maxliczbadec = maxliczbabin = sum = 0
with open ('liczby.txt', 'r') as file:
    for line in file:
        number = line.split()[0]
        if int(number[-1]) == 0:
            l1 += 1
        if int(number, 2) > maxliczbadec:
            maxliczbadec = int(number, 2)
            maxliczbabin = number
        if len(number) == 9:
            sum += int(number, 2)
            l2 += 1
sum = bin(sum)[2:]
        
print('a) liczb parzystych w pliku jest:',l1)
print('b) najwieksza liczba w pliku jest:', maxliczbadec, 'natomiast w binarnym zapisie:', maxliczbabin)
print('c) suma liczb o 9 cyfrach w calym pliku w bin:', sum, 'takich liczb 9 cyfrowych jest:', l2)