import math
def wart(x):
    return math.sin(2*x) - 4

def pole_obs_pr(a,b,n):
    w=(b-a)/n
    p=0
    for i in range(1,n+1):
        x=a+w*i-w/2
        p=p+w*abs(wart(x))
    return p

def pole_obs_tr(a,b,n):
    w=(b-a)/n
    s=0
    for i in range(1,n):
        x=a+w*i
        s=s+abs(wart(x))
        p=w/2*(abs(wart(a))+abs(wart(b))+2*s)
    return p

print(f'Pole obszaru zamknietego metoda prostokatow dla n=10: {pole_obs_pr(1,5,10)}')
print(f'Pole obszaru zamknietego metoda prostokatow dla n=100: {pole_obs_pr(1,5,100)}')
print(f'Pole obszaru zamknietego metoda prostokatow dla n=1000: {pole_obs_pr(1,5,1000)}')

print(f'Pole obszaru zamknietego metoda trapezow dla n=10: {pole_obs_tr(1,5,10)}')
print(f'Pole obszaru zamknietego metoda trapezow dla n=100: {pole_obs_tr(1,5,100)}')
print(f'Pole obszaru zamknietego metoda trapezow dla n=1000: {pole_obs_tr(1,5,1000)}')

