a = float(input())
if a>=0 and a<=400:
    calculo=((a*15)/100)
    calculot=((a*15)/100)+a
    print("Novo salario: %.2f"%calculot)
    print("Reajuste ganho: %.2f"%calculo)
    print("Em percentual: 15 %")
elif a>400 and a<=800:
    calculo=((a*12)/100)
    calculot=((a*12)/100)+a
    print("Novo salario: %.2f"%calculot)
    print("Reajuste ganho: %.2f"%calculo)
    print("Em percentual: 12 %")
elif a>800 and a<=1200:
    calculo=((a*10)/100)
    calculot=((a*10)/100)+a
    print("Novo salario: %.2f"%calculot)
    print("Reajuste ganho: %.2f"%calculo)
    print("Em percentual: 10 %")
elif a>1200 and a<=2000:
    calculo=((a*7)/100)
    calculot=((a*7)/100)+a
    print("Novo salario: %.2f"%calculot)
    print("Reajuste ganho: %.2f"%calculo)
    print("Em percentual: 7 %")
elif a>2000:
    calculo=((a*4)/100)
    calculot=((a*4)/100)+a
    print("Novo salario: %.2f"%calculot)
    print("Reajuste ganho: %.2f"%calculo)
    print("Em percentual: 4 %")