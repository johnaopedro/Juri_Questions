a,b,c,d = input().split()

a = int(a)
b = int(b)
c = int(c)
d = int(d)
cd=c+d
ab=a+b
if (b>c) and (d>a) and (cd>ab) and c>0 and d>0 and (a%2==0):
    print("Valores aceitos")
else:
    print("Valores nao aceitos")


