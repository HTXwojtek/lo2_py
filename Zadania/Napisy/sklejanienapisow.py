napis1='koteczek'
napis2='pies'
noweslowo=''

if len(napis1)<len(napis2):
    napis1,napis2=napis2,napis1

for i in range(len(napis1)):
    noweslowo+=napis1[i]
    if i<len(napis2):
        noweslowo+=napis2[i]
print(noweslowo)