# Przykład obliczania pola obszaru zamkniętego funkcji metodą prostokątów
def wart(x):
    return 2*x-1

def pole_obszaru_pr(a, b, n):
    w = (b-a)/n
    p=0
    for i in range(1,n+1):
        x=a+w*i-w/2
        p=p+w*abs(wart(x))
    return p

print(f"Pole obszaru zamkniętego dla n=5: {pole_obszaru_pr(-4,5,5)}")
print(f"Pole obszaru zamkniętego dla n=20: {pole_obszaru_pr(-4,5,20)}")
print(f"Pole obszaru zamkniętego dla n=50: {pole_obszaru_pr(-4,5,100)}")


