import sys
try:
        vetordematriz = []
        for line in sys.stdin:
            tamanho=int(line)
            if not tamanho:
                break
            matriz = []
            for i in range(tamanho):
                linha = []
                for j in range(tamanho):
                    if i==j and i!=(tamanho-1-j):
                        linha.append(1)
                    elif i==(tamanho-j-1):
                        linha.append(2)
                    else:
                        linha.append(3)
                matriz.append(linha)

            vetordematriz.append(matriz)

            for i, linha in enumerate(matriz):
                for j, elemento in enumerate(linha):
                        print(elemento, end='')
                print()
except Exception as e:
    print("Ocorreu um erro:", e)