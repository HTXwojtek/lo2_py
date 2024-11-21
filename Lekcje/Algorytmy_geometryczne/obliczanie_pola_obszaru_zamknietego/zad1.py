def wart(x):
    return x**2-4

def pole_obszaru_pr(a, b, n):
    w = (b-a)/n
    p=0
    for i in range(1,n+1):
        x=a+w*i-w/2
        p=p+w*abs(wart(x))
    return p

def pole_obszaru_tr(a, b, n):
    w = (b-a)/n
    s=0
    for i in range(1, n):
        x = a + w * i
        s=s+abs(wart(x))
        p = w/2 * (abs(wart(a))+abs(wart(b))+2*s)
    return p

print(f"Pole obszaru zamkniętego (metoda prostokatow) dla n=4: {pole_obszaru_pr(-2,2,4)}")
print(f"Pole obszaru zamkniętego (metoda prostokatow) dla n=20: {pole_obszaru_pr(-2,2,10)}")
print(f"Pole obszaru zamkniętego (metoda prostokatow) dla n=50: {pole_obszaru_pr(-2,2,50)}")
print(f"Pole obszaru zamkniętego (metoda prostokatow) dla n=100: {pole_obszaru_pr(-2,2,100)}")


print(f"Pole obszaru zamkniętego (metoda trapezow) dla n=4: {pole_obszaru_tr(-2,2,4)}")
print(f"Pole obszaru zamkniętego (metoda trapezow) dla n=20: {pole_obszaru_tr(-2,2,10)}")
print(f"Pole obszaru zamkniętego (metoda trapezow) dla n=50: {pole_obszaru_tr(-2,2,50)}")
print(f"Pole obszaru zamkniętego (metoda trapezow) dla n=100: {pole_obszaru_tr(-2,2,100)}")