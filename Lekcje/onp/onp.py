def onp(wyrazenie):
    stos=[]
    for token in wyrazenie.split():
        if token.isdigit():
            stos.append(int(token))
        else:
            a=stos.pop()
            b=stos.pop()
            if token=='+':
                stos.append(a+b)
            elif token=='-':
                stos.append(a-b)
            elif token=='*':
                stos.append(a*b)
            elif token=='/':
                stos.append(a/b)
    return stos.pop()

wyrazenie='3 4 + 5 *'
print(f'Wynik ONP: {onp(wyrazenie)}')
                

