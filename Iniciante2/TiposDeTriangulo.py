a,b,c = input().split()
e=True
a=float(a)
b=float(b)
c=float(c)
if a < b:
    a, b = b, a
if a < c:
    a, c = c, a
if b < c:
    b, c = c, b

if a >= b + c:
    print("NAO FORMA TRIANGULO")
    e = False

if e==True:
    if (a**2)==(((b**2)+(c**2))):
        print("TRIANGULO RETANGULO")
    elif (a**2)>(((b**2)+(c**2))):
        print("TRIANGULO OBTUSANGULO")
    elif (a**2)<(((b**2)+(c**2))):
        print("TRIANGULO ACUTANGULO")

if e==True:
    if a==b and a==c:
        print("TRIANGULO EQUILATERO")
    elif a==b and a!=c:
        print("TRIANGULO ISOSCELES")
    elif a!=b and a==c:
        print("TRIANGULO ISOSCELES")
    elif c==b and a!=c:
        print("TRIANGULO ISOSCELES")