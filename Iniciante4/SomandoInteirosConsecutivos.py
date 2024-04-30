entrada = input().split()
for elementos in range(len(entrada)):
    entrada[elementos] = int(entrada[elementos])
A = entrada[0]
j=1
N=0
while True:
    if entrada[j]>0:
        N=entrada[j]
        break
    j+=1
soma=0
i=0
while A>=i:
    soma=soma + i
    i=i+1
i=N-1
while i>0:
    soma=soma+i
    i=i-1
print(soma)