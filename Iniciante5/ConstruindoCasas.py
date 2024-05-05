resultado=[]
while True:
    entrada = input().split()
    if len(entrada)==1:
        break
    a,b,c = map(int, entrada)
    calculo = (((a * b) / c) * 100) ** 0.5
    calculo = int(calculo)
    resultado.append(calculo)

for i in resultado:
    print(i)