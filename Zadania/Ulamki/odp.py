def nwd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def nww(a, b):
    return a * b // nwd(a, b)

def wlasciwe(licz, mian):
    cal=licz//mian
    ul=licz%mian
    if cal==0:
        return str(licz) + '/' + str(mian)
    elif ul==0:
        return str(cal)+ ' calosci'
    else:
        return str(cal)+' całości i '+str(ul)+'/'+str(mian)

def dodawanie(u1, u2):
    licznik1, mianownik1 = map(int, u1.split('/'))
    licznik2, mianownik2 = map(int, u2.split('/'))
    fin_licz=fin_mian=fin_nwd=stosunek1=stosunek2=0
    if mianownik1==mianownik2:
        fin_licz=licznik1+licznik2
        fin_mian=mianownik1
        fin_nwd = nwd(fin_licz, fin_mian)
        if fin_nwd != 1:
            fin_mian = fin_mian // fin_nwd
            fin_licz = fin_licz // fin_nwd
        return wlasciwe(fin_licz, fin_mian)
    else:
        fin_mian=nww(mianownik2, mianownik1)
        stosunek1=fin_mian//mianownik1
        stosunek2=fin_mian//mianownik2
        fin_licz=(stosunek1*licznik1)+(stosunek2*licznik2)
        fin_nwd = nwd(fin_licz, fin_mian)
        if fin_nwd != 1:
            fin_mian = fin_mian // fin_nwd
            fin_licz = fin_licz // fin_nwd
        return wlasciwe(fin_licz, fin_mian)

def odejmowanie(u1, u2):
    licznik1, mianownik1 = map(int, u1.split('/'))
    licznik2, mianownik2 = map(int, u2.split('/'))
    fin_licz=fin_mian=fin_nwd=stosunek1=stosunek2=0
    if mianownik1==mianownik2:
        fin_licz=licznik1-licznik2
        fin_mian=mianownik1
        fin_nwd = nwd(fin_licz, fin_mian)
        if fin_nwd != 1:
            fin_mian = fin_mian // fin_nwd
            fin_licz = fin_licz // fin_nwd
        return wlasciwe(fin_licz, fin_mian)
    else:
        fin_mian=nww(mianownik2, mianownik1)
        stosunek1=fin_mian//mianownik1
        stosunek2=fin_mian//mianownik2
        fin_licz=(stosunek1*licznik1)-(stosunek2*licznik2)
        fin_nwd = nwd(fin_licz, fin_mian)
        if fin_nwd != 1:
            fin_mian = fin_mian // fin_nwd
            fin_licz = fin_licz // fin_nwd
        return wlasciwe(fin_licz, fin_mian)


def mnożenie(u1,u2):
    licznik1, mianownik1 = map(int, u1.split('/'))
    licznik2, mianownik2 = map(int, u2.split('/'))
    fin_licz=fin_nwd=fin_mian=0
    fin_licz=licznik1*licznik2
    fin_mian=mianownik1*mianownik2
    fin_nwd = nwd(fin_licz, fin_mian)
    if fin_nwd != 1:
        fin_mian = fin_mian // fin_nwd
        fin_licz = fin_licz // fin_nwd
    return wlasciwe(fin_licz, fin_mian)



while True:
    print('Co robimy szefie?')
    print('1.Dodajemy')
    print('2.Odejmujemy')
    print('3.Mnożymy')
    odp = int(input())

    ulamek1 = input('Podaj pierwszy ułamek:')
    ulamek2 = input('Podaj drugi ułamek:')

    if odp == 1:
        print(dodawanie(ulamek1, ulamek2))
        break
    if odp == 2:
        print(odejmowanie(ulamek1, ulamek2))
        break
    if odp == 3:
        print(mnożenie(ulamek1, ulamek2))
        break
    else:
        print('zle')


