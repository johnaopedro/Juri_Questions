import sys

try:
    vetordematriz = []
    for line in sys.stdin:
        tamanho = int(line)
        if not tamanho:
            break
        matriz = []
        tamanhopor2 = tamanho // 2
        tamanhopor3 = int(tamanho /3)
        for i in range(tamanho):
            linha = []
            for j in range(tamanho):
                if i == tamanhopor2 and j == tamanhopor2:
                    linha.append(4)
                elif i >tamanhopor3-1 and i<(tamanho-(tamanhopor3)) and j>tamanhopor3-1 and j<(tamanho-tamanhopor3):
                    linha.append(1)
                elif i == j and i != (tamanho - 1 - j):
                    linha.append(2)
                elif i == (tamanho - j - 1):
                    linha.append(3)
                else:
                    linha.append(0)
            matriz.append(linha)
        vetordematriz.append(matriz)

        for linha in matriz:
            print(''.join(map(str, linha)))
        print()
except Exception as e:
    print("Ocorreu um erro:", e)
