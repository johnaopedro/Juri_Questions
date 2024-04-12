a,b,c = input().split()
a = float(a)
b = float(b)
c = float(c)
if a==0:
    print("Impossivel calcular")
else:
    discriminante = b**2 - 4*a*c
    if discriminante < 0:
        print("Impossivel calcular")
    else:
        calculo1= float((((-1)*b)+(((b**2)-(4*a*c))**0.5))/(2*a))
        calculo2= float((((-1)*b)-(((b**2)-(4*a*c))**0.5))/(2*a))
        print("R1 = %.5f" %calculo1)
        print("R2 = %.5f" %calculo2)