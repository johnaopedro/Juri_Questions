casos = int(input())
resultado=[]
for i in range(casos):
    a,b= map(int, input().split())
    calculo = ((a*2)+(b*2))/2
    calculo=int(calculo)
    resultado.append(calculo)
for i in resultado:
    print(i)