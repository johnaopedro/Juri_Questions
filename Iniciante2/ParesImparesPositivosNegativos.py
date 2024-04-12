a=int(input())
b=int(input())
c=int(input())
d=int(input())
e=int(input())
contadorimpar=0
contadorpar=0
contadorpos=0
contadorneg=0
if a%2==0:
    contadorpar = contadorpar+1
else:
    contadorimpar= contadorimpar+1
if a>0:
    contadorpos = contadorpos+1
elif a<0:
    contadorneg= contadorneg+1

if b%2==0:
    contadorpar = contadorpar+1
else:
    contadorimpar= contadorimpar+1
if b>0:
    contadorpos = contadorpos+1
elif b<0:
    contadorneg= contadorneg+1

if c%2==0:
    contadorpar = contadorpar+1
else:
    contadorimpar= contadorimpar+1
if c>0:
    contadorpos = contadorpos+1
elif c<0:
    contadorneg= contadorneg+1

if d%2==0:
    contadorpar = contadorpar+1
else:
    contadorimpar= contadorimpar+1
if d>0:
    contadorpos = contadorpos+1
elif d<0:
    contadorneg= contadorneg+1

if e%2==0:
    contadorpar = contadorpar+1
else:
    contadorimpar= contadorimpar+1
if e>0:
    contadorpos = contadorpos+1
elif e<0:
    contadorneg= contadorneg+1

print("%d valor(es) par(es)"%contadorpar)
print("%d valor(es) impar(es)"%contadorimpar)
print("%d valor(es) positivo(s)"%contadorpos)
print("%d valor(es) negativo(s)"%contadorneg)