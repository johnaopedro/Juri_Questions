#NADA A VER OQ EU FIZ AQUI NO INICIO, MAS VALE PARA LEMBRANÇA
#n=int(input())
#entrada=[]
#bate=0
#repetido=[0]
#entrada = input().split()
#for i in range(n):
#    entrada[i]=int(entrada[i])
#for i in range(n):
#    for j in range(i+1,n):
#        if entrada[i] != entrada[j]:
#            if entrada[i] not in repetido:
#                    bate +=1
#                    repetido.append(entrada[i])
#            elif entrada[j] not in repetido:
#                    bate+=1
#                    repetido.append(entrada[j])
#        elif entrada[i] == entrada[j]:
#            if entrada[i] not in repetido:
#                repetido.append(entrada[i])
#                bate += 1
#print(bate)
#print(repetido)

#CORRETO AQUI
# Lê o número de pessoas
N = int(input())

valores = list(map(int, input().split()))
menor=valores[0]
indices=1
for i in range(N):
    if valores[i]<menor:
        menor=valores[i]
        indices=i+1
    elif valores[i] == menor and (i + 1)<indices:
        indices = i + 1
print(indices)
