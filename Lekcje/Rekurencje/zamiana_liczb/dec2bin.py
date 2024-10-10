# iteracyjnie
def dec2bin_it(liczba):
    tab=[]
    while liczba!=0:
        tab.insert(0,int(liczba)%2)
        liczba=liczba//2
    liczbabin="".join(map(str,tab))
    return liczbabin

#rekurencyjna
def dec2bin_rek(liczba):
    if liczba>1:
        return dec2bin_rek(liczba//2)+str(liczba%2)
    else:
        return str(liczba%2)

x=int(input("Podaj liczbę w systemie dziesiętnym: "))
print(f"Liczba binarna (iteracyjnie): {dec2bin_it(x)}")
print(f"Liczba binarna (rekurencyjnie): {dec2bin_rek(x)}")