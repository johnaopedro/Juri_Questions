a, b = input().split()
a=int(a)
b=int(b)

if a==1:
    calculo= float(4*b)
elif a==2:
    calculo=float(4.5*b)
elif a==3:
    calculo=float(5*b)
elif a==4:
    calculo=float(2*b)
elif a==5:
    calculo=float(1.5*b)

print("Total: R$ %.2f"%calculo)