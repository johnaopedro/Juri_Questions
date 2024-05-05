tamanho = int(input())
vetordematriz = []
digitos=0
valor=0
while tamanho != 0:
    matriz = []
    for i in range(tamanho):
        linha=[]
        for j in range(tamanho):
            valor=2**(i+j)
            linha.append(valor)
            if j==tamanho-1:
                digitos=0
                digitos=len(str(valor))
        matriz.append(linha)

    vetordematriz.append(matriz)

    for i, linha in enumerate(matriz):
        for j, elemento in enumerate(linha):
            if j != len(linha) -1:
                print('{: >{}}'.format(elemento, digitos), end=' ')
            else:
                print('{: >{}}'.format(elemento, digitos))
    print()
    tamanho = int(input())