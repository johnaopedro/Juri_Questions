valor1 = int(input())
vetor = []
vetor.append(valor1)
while True:
    valores = int(input())
    if valores>valor1:
        break
    vetor.append(valores)
soma=0
cont=0
while soma<valores:
    soma=soma+valor1
    valor1=valor1+1
    cont=cont+1
print(cont)
    
##21, 22 = 2
##3, 4, 5, 6, 7 = 5