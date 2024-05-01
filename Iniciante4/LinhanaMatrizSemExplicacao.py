def criar_matriz(tamanho):
    matriz=[]
    valores=[]
    for _ in range(tamanho):
        linha = []
        for _ in range(tamanho):
            linha.append(0)
        matriz.append(linha)
    referencia_linha = int(input())
    ordem = input()
    for i in range(tamanho*tamanho):
        valor = input()
        valores.append(valor)
    for elementos in range(len(valores)):
        valores[elementos] = float(valores[elementos])

    for i in range(tamanho):
        for j in range(tamanho):
            matriz[i][j] = valores[i * tamanho + j]

    soma_media = sum(matriz[referencia_linha]) #Soma Tudo
    if ordem == 'S':
        soma_media=soma_media
    elif ordem == 'M':
        soma_media = soma_media/tamanho

    return matriz, soma_media
def main():
    tamanho = 12
    resultado = criar_matriz(tamanho)
    if resultado:
        matriz, soma_media = resultado #Matriz pega matriz e soma a soma
        print("%.1f"%soma_media)
if __name__ == "__main__":
    main() 