def criar_matriz(tamanho):
    # Criando uma matriz preenchida com zeros
    matriz = [[0 for _ in range(tamanho)] for _ in range(tamanho)]

    # Recebendo a entrada do usuário para a referência da linha
    referencia_linha = int(input(f"Digite o número da linha de referência (de 0 a {tamanho - 1}): "))
    if referencia_linha < 0 or referencia_linha >= tamanho:
        print(f"Número de linha inválido. Por favor, escolha um número de 0 a {tamanho - 1}.")
        return None

    # Recebendo a entrada do usuário para soma ou média
    operacao = input("Digite 'S' para soma ou 'M' para média: ").upper()
    if operacao != 'S' and operacao != 'M':
        print("Operação inválida. Por favor, digite 'S' para soma ou 'M' para média.")
        return None

    # Calculando o número total de elementos na matriz
    total_elementos = tamanho * tamanho

    # Recebendo os valores para preencher a matriz
    valores = input(f"Digite os {total_elementos} valores separados por espaço: ").split()
    if len(valores) != total_elementos:
        print(f"Quantidade de valores incorreta. Por favor, insira {total_elementos} valores.")
        return None

    # Convertendo os valores para números inteiros
    valores = [int(valor) for valor in valores]

    # Preenchendo a matriz com os valores fornecidos
    for i in range(tamanho):
        for j in range(tamanho):
            matriz[i][j] = valores[i * tamanho + j]

    # Calculando a soma ou média da linha de referência
    soma_media = sum(matriz[referencia_linha])
    if operacao == 'M':
        soma_media /= tamanho

    return matriz, soma_media

def main():
    # Pedindo ao usuário para especificar o tamanho da matriz
    tamanho = int(input("Digite o tamanho da matriz (por exemplo, 11 para uma matriz 11x11): "))

    # Chamando a função e imprimindo a matriz e a soma/média da linha de referência
    resultado = criar_matriz(tamanho)
    if resultado:
        matriz, soma_media = resultado
        print("Matriz:")
        for linha in matriz:
            print(linha)
        print("Soma/Média da linha de referência:", soma_media)

if __name__ == "__main__":
    main()
