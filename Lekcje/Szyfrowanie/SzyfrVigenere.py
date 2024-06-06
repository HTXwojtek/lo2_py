tekst='Ala ma 3 koty!'
klucz='kebab'
alfabet='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
cyfry = '0123456789'

def encrypt(tekst, klucz, alfabet):
    szyfrogram=''
    tekst=tekst.upper()
    klucz=klucz.upper().replace(" ", "")
    dl_klucz=len(klucz)
    i=0

    for literka in tekst:
        if literka in alfabet:
            tekst_index=alfabet.find(literka)
            klucz_index=alfabet.find(klucz[i % dl_klucz])
            c=(tekst_index+klucz_index) % len(alfabet)
            szyfrogram+=alfabet[c]
            i+=1
        elif literka in cyfry:
            tekst_index=cyfry.find(literka)
            klucz_index=alfabet.find(klucz[i % dl_klucz]) % 10
            c=(tekst_index+klucz_index) % len(cyfry)
            szyfrogram+=cyfry[c]
            i+=1
        else:
            szyfrogram += literka

    return szyfrogram


def decrypt(tekst, klucz, alfabet):
    odwrocony_klucz=''
    for i in klucz.upper().replace(" ", ""):
        klucz_index=(len(alfabet)-alfabet.find(i)) % len(alfabet)
        odwrocony_klucz+=alfabet[klucz_index]
    return encrypt(tekst, odwrocony_klucz, alfabet)


zaszyfrowane=encrypt(tekst, klucz, alfabet)
print(zaszyfrowane)
print(decrypt(zaszyfrowane, klucz, alfabet))

