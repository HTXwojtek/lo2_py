import random
rzuty=1000
trafienia=0
a=2
b=1
for i in range(1,rzuty+1):
    x=2*random.random()-1
    y=2*random.random()-1
    if (x/a)**2+(y/b)**2<=1:
        trafienia+=1

przyblizona_liczba_pi=4*(trafienia/rzuty)
print(przyblizona_liczba_pi)