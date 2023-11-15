plik=open('trojkaty-dane.txt')

def troj_pro(a,b,c):
    if a^2+b^2==c^2 or a^2+c^2==b^2 or b^2+c^2==a^2:
        print('trojkat prostokatny')
        return True
    else:
        print('trojkat zwykly')
        return False

def troj():
    suma=0
    sum_pro=0
    for linia in plik:
        tab=linia.split()
        a=int(tab[0])
        b=int(tab[1])
        c=int(tab[2])
        if a+b>c and a+c>b and b+c>a:
            suma+=1
            print('mozna stworzyc taki trojkat', a,b,c)
            if troj_pro(a,b,c)==True:
                sum_pro+=1
        else:
            print('nie mozna stworzyc takiego trojkata', a,b,c)
    print(f'Razem jest {suma} trojkątów: {sum_pro} to trójkąty prostokątne')

troj()


