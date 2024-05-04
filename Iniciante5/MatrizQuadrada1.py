tamanho=int(input())
while tamanho!=0:
    soma_media = 0
    matriz = []
    valores = []
    cont=0
    for i in range(tamanho):
        linha = []
        for j in range(tamanho):
            linha.append(0)
        matriz.append(linha)

    for j in range(tamanho):
        for i in range(tamanho):
            matriz[i][j] = 1

    tamanho=int(input())
for i in range(len(matriz)):
    for j in range(len(matriz)):
        if j<(len(matriz))-1:
            print(matriz[i][j], end=" ")
        else:
            print(matriz[i][j])