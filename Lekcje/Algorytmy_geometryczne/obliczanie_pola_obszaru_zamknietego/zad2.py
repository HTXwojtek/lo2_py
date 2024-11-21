import math
# def wart(x):
#     return math.sin(x) + 3*math.cos(x) - 1

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

# print(f"metoda prostokatow {pole_obszaru_pr(0,math.pi/2,100)}")
# print(f"metoda trapezow {pole_obszaru_tr(0,math.pi/2,100)}")
# wynik=math.sqrt(3)+1

#a
# def wart(x):
#     return math.sin(x)
# print(f"metoda prostokatow {pole_obszaru_pr(0,math.pi,1000)}")
# print(f"metoda trapezow {pole_obszaru_tr(0,math.pi,1000)}")

#b
# def wart(x):
#     return 1 / (x**2+1)
# print(f"metoda prostokatow {pole_obszaru_pr(0,1,1000)}")
# print(f"metoda trapezow {pole_obszaru_tr(0,1,1000)}")

#c
# def wart(x):
#     return math.sqrt(2*x)
# print(f"metoda prostokatow {pole_obszaru_pr(0,8,1000)}")
# print(f"metoda trapezow {pole_obszaru_tr(0,8,1000)}")

#d
def wart(x):
    return x*math.sin(4*x)
print(f"metoda prostokatow {pole_obszaru_pr(0,math.pi/4,1000)}")
print(f"metoda trapezow {pole_obszaru_tr(0,math.pi/4,1000)}")
