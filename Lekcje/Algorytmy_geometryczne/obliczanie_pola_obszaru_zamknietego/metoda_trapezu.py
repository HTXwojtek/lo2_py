# Obliczanie pola obszaru zamkniętego za pomocą metody trapezów
def wart(x):
    return 2*x-1

def pole_obszaru_tr(a, b, n):
    w = (b-a)/n
    s=0
    for i in range(1, n):
        x = a + w * i
        s=s+abs(wart(x))
        p = w/2 * (abs(wart(a))+abs(wart(b))+2*s)
    return p


print(f"Pole obszaru zamkniętego dla n=5: {pole_obszaru_tr(-4,5,5)}")
print(f"Pole obszaru zamkniętego dla n=20: {pole_obszaru_tr(-4,5,20)}")
print(f"Pole obszaru zamkniętego dla n=50: {pole_obszaru_tr(-4,5,100)}")