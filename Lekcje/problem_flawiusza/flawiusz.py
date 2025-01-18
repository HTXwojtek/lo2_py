def flawiusz(n,k):
    osoby=list(range(1, n+1))
    index=0
    while len(osoby)>1:
        index=(index+k-1)%len(osoby)
        osoby.pop(index)
    return osoby[0]

n=7
k=3
print(f'Ocalona osoba: {flawiusz(n,k)}')
    