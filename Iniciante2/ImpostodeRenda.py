
a = float(input())

if a>=0 and a<=2000:
    print("Isento")
elif a>2000 and a<=3000:
    calculo=((a-2000)*8)/100
    print("R$ %.2f"%calculo)
elif a>3000 and a<=4500:
    calculo=(0.18*(a-3000))+(0.08*1000)
    print("R$ %.2f"%calculo)
else:
    calculo = (1000 * 0.08) + (1500 * 0.18) + ((a - 4500) * 0.28)
    print("R$ %.2f" % calculo)