n = int(input())  # Qual linha será usada para média e soma
ordem = input()
linha = []
coluna = []

# Preenchendo a coluna
for i in range(11):
    coluna.append(float(input()))

# Preenchendo a linha
for i in range(11):
    linha_atual = []
    for k in range(11):
        linha_atual.append(float(input()))
    linha.append(linha_atual)

# Calculando a soma ou média da linha especificada
if ordem == "S":
    soma = sum(linha[n])
    print("%.1f" %soma)
elif ordem == "M":
    media = sum(linha[n]) / len(linha[n])
    print("%.1f"%media)

# Imprimindo a matriz
print("Matriz:")
for i in range(11):
    print("%d" % coluna[i])
    for k in range(11):
        print("%d" % linha[i][k], end=" ")
    print()  # Nova linha após cada linha da matriz

