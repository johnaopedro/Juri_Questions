#Criando Matriz com 0. Definindo tamanho para caso queira.
#Nesse exercicio o tamanho já esta definido em 11.
def criar_matriz(tamanho):
    matriz=[]
    for _ in range(tamanho):
        linha = []
        for _ in range(tamanho):
            linha.append(0)
        matriz.append(linha)
    #print(matriz) para vizualizar o tamanho da matriz
    return matriz

#Recebendo o valor n para qual linha 
def OperandoMatriz(tamanho,matriz):
    referencia_linha = int(input(f"Digite o número da linha de referência (de 0 a {tamanho - 1}): "))
#Utilizar para verificar se valor não é nulo. Não utilizarei agr    
#    if referencia_linha < 0 or referencia_linha >= tamanho:
#        print(f"Número de linha inválido. Por favor, escolha um número de 0 a {tamanho - 1}.")
#        return None

#Recebendo para ver se é M ou S para media ou soma
    ordem = input()
#Utilizar para verificar se valor não é nulo. Não utilizarei agr    
#    if operacao != 'S' and operacao != 'M':
#        print("Operação inválida. Por favor, digite 'S' para soma ou 'M' para média.")
#        return None

# Calculando o número total de elementos na matriz
    total_elementos = tamanho * tamanho

    # Recebendo os valores para preencher a matriz
    valores = input().split()
#Verificador de valores, se foram todos    
#    if len(valores) != total_elementos:
#        print(f"Quantidade de valores incorreta. Por favor, insira {total_elementos} valores.")
#        return None

    # Convertendo os valores para números com ponto flutuante
    valores = [float(valor) for valor in valores]

    # Preenchendo a matriz com os valores fornecidos
    for i in range(tamanho):
        for j in range(tamanho):
            matriz[i][j] = valores[i * tamanho + j]

    # Calculando a soma ou média da linha de referência
    soma_media=float(soma_media)
    soma_media = sum(matriz[referencia_linha]) #Soma Tudo
    if ordem == 'M':
        soma_media = soma_media/tamanho

    return matriz, soma_media
def main():
    #Definir tamanho:
    tamanho = 11
    #criar matriz:
    matriz = criar_matriz(tamanho)
    matriz, soma_media = OperandoMatriz(tamanho, matriz)
    #Printar matriz se quiser
    #print("Matriz:")
    #for linha in matriz:
        #Print da linha escolhida se quiser
        #Print(linha)
        #Print da soma ou media
    print(soma_media)