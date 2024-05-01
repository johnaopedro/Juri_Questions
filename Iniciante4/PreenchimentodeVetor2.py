n=int(input())
vetor=[]
j=0
cont=0
for i in range(1000):
    vetor.append(j)
    j+=1
    if j==n:
        j=0
for i in range(1000):
    print("N[%d] = %d"%(i, vetor[i]))
