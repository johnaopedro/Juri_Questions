valor1 = int(input())
vetor = []
vetor.append(valor1)
while True:
    idades = int(input())
    vetor.append(idades)
    if idades<0:
        break
media=float(0)
valor=0
for i in range(len(vetor)-1):
    valor=valor + vetor[i]
media = valor/((len(vetor))-1)
print("%.2f"%media)