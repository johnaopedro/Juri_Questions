n = int(input())
perfeito = []

for _ in range(n): #O _ Permite que funcione n vezes
    teste = int(input())
    testador=0
    cont=0
    for i in range(1, teste+1):
        if teste%i==0:
            cont+=1
    
    if cont==2:
        perfeito.append("%d eh primo"%teste)
    else:
        perfeito.append("%d nao eh primo"%teste)
for i in range(n):
    print(perfeito[i])