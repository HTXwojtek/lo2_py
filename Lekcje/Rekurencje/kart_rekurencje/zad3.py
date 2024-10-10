def silnia(n):
    if n>1:
        return n*silnia(n-1)
    return 1

def newton(n,k):
    if not n>=k>=0:
        return None
    else:
        return silnia(n)/(silnia(k)*silnia((n-k)))

print(newton(10,2))
    