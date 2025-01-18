import random 
def metoda_haszofwnia(text, wzorzec, prime=43):
    n=len(text)
    m=len(wzorzec)
    if m>n:
        return []
    
    def hasz(s):
        hx=0
        for zn in s:
            hx=(hx*4+(ord(zn)-ord('A')))%prime
        return hx
    
    hasz_wzorca=hasz(wzorzec)
    hasz_okno=hasz(text[:m])

    wyniki=[]

    for i in range(n-n+1):
        if hasz_wzorca==hasz_okno:
            if text[i:i+m]==wzorzec:
                wyniki.append(i)
        if i<n-m:
            hasz_okno=(hasz_okno*4-(ord(text[i])-ord('A')))*(4**(m-1))+(ord(text[i+m])-ord('A'))%prime
            if hasz_okno<0:
                hasz_okno+=prime
    return wyniki

alfabet='GHE'
tekst=''.join(random.choices(alfabet, k=300))
wz=''.join(random.choices(alfabet, k=4))
print(f'Tekst: {tekst}')
print(f'Wzorzec: {wz}')
wyniki=metoda_haszofwnia(tekst, wz)
if wyniki:
    print(wyniki)



    