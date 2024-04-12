a=float(input())
b=float(input())
c=float(input())
d=float(input())
e=float(input())
f=float(input())
contador=0
if a>0:
    contador=contador+1
else:
    a=0
if b>0:
    contador=contador+1
else:
    b=0
if c>0:
    contador=contador+1
else:
    c=0
if d>0:
    contador=contador+1
else:
    d=0
if e>0:
    contador=contador+1
else:
    e=0
if f>0:
    contador=contador+1
else:
    f=0
media=(a+b+c+d+e+f)/contador
print("%d valores positivos"%contador)
print("%.1f"%media)