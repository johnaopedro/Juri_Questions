a,b,c,d = input().split()
horaI=int(a)
minI=int(b)
horaF=int(c)
minF=int(d)
if horaF<=horaI:
    horaT=(horaF+24)-horaI
else:
    horaT=horaF-horaI
if minI>minF:
    sobra=minI-minF
    horaT= horaT-1
    minT=60-sobra
elif minF==minI:
    minT=0
else:
    minT=minF-minI
if horaT>=24 and minT>0:
    horaT=0

print("O JOGO DUROU %d HORA(S) E %d MINUTO(S)"%(horaT,minT))