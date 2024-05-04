tamanho = int(input())
vetordematriz = []

while tamanho != 0:
    matriz = []
    for i in range(tamanho):
        valor=i+1
        linha = []
        n=1
        linha.append(valor)
        while valor !=1:
            valor=valor-1
            linha.append(valor)
            n=n+1
        valor=valor+1
        for j in range(tamanho-n):
            linha.append(valor)
            valor=valor+1
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