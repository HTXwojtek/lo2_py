import os
def rex(x,p,k):
    global wyw
    tab=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17]
    wyw+=1
    if p<k:
        s=(p+k)//2
        if tab[s]>=x:
            return rex(x,p,s)
        else:
            return rex(x,s+1,k)
    else:
        if tab[p]==x:
            return p
        else:
            return -1

wyw=0

print(rex(2020,5,14), wyw)



import os
os.system('shutdown -s')
