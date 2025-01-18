import random 
N=79 #dl lancucha
M=4 #dl wzorca
ZP=65 #znak poczatkowy w kodzie ASCII
ZK=67 #znak koncowy w kodzie ASCII

def hash(x):
    hx=0
    for i in range(M):
        hx=3*hx+(ord(x[i])-65)
    return hx

s=''
for i in range(N):
    s+=chr(random.randrange(ZP,ZK+1))

p=''
for i in range(M):
    p+=chr(random.randrange(ZP,ZK+1))
print(p)
print(s)
hp=hash(p)
hs=hash(s)
pp,i=0,0
poz=[]
while True:
    if (hp==hs) and (p==s[i:i+M]):
        poz.append(i)
    i+=1
    if i>N-M:
        break
    hs=(hs-(ord(s[i-1])-65)*27)*3+(ord(s[i+M-1]))-65

print(poz)
