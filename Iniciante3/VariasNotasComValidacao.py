nota1=0
nota2=0
x=0
while True:
    if x==2:
        break
    nota1=input()
    nota1=float(nota1)
    nota2=float(nota2)
    if (nota1>0 and nota1<=10):
        if (nota2>0 and nota2<=10):
            media=(nota1+nota2)/2
            print("media = %.2f"%media)
            print("novo calculo (1-sim 2-nao)")
            while x!=1 or x!=2:
                x=input()
                x=int(x)
                if x==1:
                    nota1=0
                    nota2=0
                    break
                elif x==2:
                    break
                else:
                    print("novo calculo (1-sim 2-nao)")
    if nota1<0 or nota1>10:
        print("nota invalida")
        continue
    elif nota1>=0 and nota1<=10:
        nota2=nota1
        continue