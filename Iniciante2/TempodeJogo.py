a,b = input().split()
a=int(a)
b=int(b)
if b<a:
    calculo=(b+24)-a
elif b==a:
    calculo=24
else:
    calculo=b-a
print("O JOGO DUROU %d HORA(S)"%calculo)