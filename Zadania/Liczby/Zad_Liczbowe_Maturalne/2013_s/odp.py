def growing(number):
    ending = number%10
    number //= 10
    while number > 0:
        if not ending >= number % 10:
            return 0
        ending = number % 10
        number //= 10
    return 1

l1 = l2 = l3 = maxnumber = 0
minnumber = 2000000
with open ('dane.txt','r') as file:
    for line in file:
        number = str(int(line))
        number_dec = str(int(line, 8))
        if number[0] == number[-1]:
            l1 += 1
        if number_dec[0] == number_dec[-1]:
            l2 += 1
        if growing(int(number)):
            l3 += 1
            if maxnumber<int(number):
                maxnumber = int(number)
            if minnumber>int(number):
                maxnumber = int(number)

print(l1)
print(l2)
print(l3)
print(maxnumber, minnumber)