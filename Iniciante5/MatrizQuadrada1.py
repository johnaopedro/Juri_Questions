tamanho = int(input())
vetordematriz = []

while tamanho != 0:
    matriz = []
    for i in range(tamanho):
        linha = []
        for j in range(tamanho):
            dist_centro = min(i, j, tamanho - i - 1, tamanho - j - 1)
            valor = dist_centro + 1
            linha.append(valor)
        matriz.append(linha)

    vetordematriz.append(matriz)

    tamanho = int(input())

for i, matriz in enumerate(vetordematriz):
    for j, linha in enumerate(matriz):
        print(' '.join(map(str, linha)))
    if i != len(vetordematriz) - 1:
        print()

