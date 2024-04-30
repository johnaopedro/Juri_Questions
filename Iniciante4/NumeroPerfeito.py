n = int(input())
perfeito = []

for _ in range(n): #O _ Permite que funcione n vezes
    teste = int(input())
    divisor_sum = 0
    testador=0
    for i in range(1, teste+1):
        testador+=i
        if teste == testador:
            break
    
    if testador == teste and testador!=1:
        perfeito.append("%d eh perfeito"%teste)
    else:
        perfeito.append("%d nao eh perfeito"%teste)
for i in range(n):
    print(perfeito[i])