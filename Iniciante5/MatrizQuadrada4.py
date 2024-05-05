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
                        linha.append(2)                      
                    elif i==(tamanho-j-1) and i!=j:
                        linha.append(3)
                    else:
                        dist_centro = min(i, j, tamanho - i - 1, tamanho - j - 1)
                        valor = dist_centro
                        linha.append(valor)
                matriz.append(linha)
            vetordematriz.append(matriz)

            for i, linha in enumerate(matriz):
                for j, elemento in enumerate(linha):
                        print(elemento, end='')
                print()
            print()
except Exception as e:
    print("Ocorreu um erro:", e)