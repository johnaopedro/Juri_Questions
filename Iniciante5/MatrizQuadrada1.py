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

    for i, linha in enumerate(matriz):
        for j, elemento in enumerate(linha):
            if j != len(linha) -1:
                print('{: >3}'.format(elemento), end=' ')
            else:
                print('{: >3}'.format(elemento))
    print()
    tamanho = int(input())