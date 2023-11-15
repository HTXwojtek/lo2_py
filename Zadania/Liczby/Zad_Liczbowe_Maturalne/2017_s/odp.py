# zadanie 4.1
with open("binarne.txt","r") as plik:
    licznik1 = maxlen = maxnapis = 0
    for linia in plik:
        napis=linia.strip()
        len_now = len(napis)
        cykle = []
        for i in range(0,len_now,(len_now//2)):
            cykle.append(napis[i:i+len_now//2])
        if len(set(cykle))==1:
            licznik1 += 1
            if len_now > maxlen:
                maxlen = len_now
                maxnapis = napis
    print(licznik1, maxnapis, maxlen)

# zadanie 4.2

with open("binarne.txt","r") as plik:
    minlen=9999999999
    licznik2=0
    for linia in plik:
        segmenty = []
        napis = linia.strip()
        for i in range(0,len(napis),4):
            segmenty.append(napis[i:i+4])
        for liczba in segmenty:
            if int(liczba, 2)>9:
                if len(napis)<minlen:
                    minlen=len(napis)
                licznik2+=1
                break
    print(licznik2,minlen)

# zadanie 4.3

with open("binarne.txt","r") as plik:
    max=-999999
    maxbin=maxdec=0
    for linia in plik:
        napis=linia.strip()
        if int(napis,2)>65535:
            continue
        else:
            if int(napis,2)>maxdec:
                maxdec=int(napis,2)
                maxbin=int(napis)
    print(maxdec,maxbin)