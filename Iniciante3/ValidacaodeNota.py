nota1=0
nota2=0
while True:
    nota1=input()
    nota1=float(nota1)
    nota2=float(nota2)
    if (nota1>0 and nota1<=10):
        if (nota2>0 and nota2<=10):
            media=(nota1+nota2)/2
            print("media = %.2f"%media)
            break
    if nota1<0 or nota1>10:
        print("nota invalida")
        continue
    elif nota1>=0 and nota1<=10:
        nota2=nota1
        continue