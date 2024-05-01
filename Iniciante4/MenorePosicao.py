n=int(input())
vetor=[]
valores = input().split()
for i in range(n):
    valores[i]=int(valores[i])
menor = valores[0]
posicao = 0
for i in range(1, n):
    if valores[i] < menor:
        menor = valores[i]
        posicao = valores.index(valores[i])
print("Menor valor: %d"%menor)
print("Posicao: %d"%posicao)
