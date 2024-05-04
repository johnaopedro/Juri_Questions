def criar_matriz(tamanho):
    soma_media = 0
    matriz = []
    valores = []
    cont=0
    for _ in range(tamanho):
        linha = []
        for _ in range(tamanho):
            linha.append(0)
        matriz.append(linha)

    ordem = input()
    for i in range(tamanho * tamanho):
        valor = input()
        valores.append(valor)
    for elementos in range(len(valores)):
        valores[elementos] = float(valores[elementos])

    for i in range(tamanho):
        for j in range(tamanho):
            matriz[i][j] = valores[i * tamanho + j]

    for i in range(tamanho):
        for j in range(tamanho):
            if i<(tamanho-j-1):
                soma_media += matriz[i][j]
                cont+=1

    if ordem == 'S':
        soma_media = soma_media
    elif ordem == 'M':
        soma_media = soma_media / cont

    return soma_media

def main():
    tamanho = 12
    soma_media = criar_matriz(tamanho)
    print("%.1f" % soma_media)

if __name__ == "__main__":
    main()