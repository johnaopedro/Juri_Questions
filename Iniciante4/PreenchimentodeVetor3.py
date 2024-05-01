n=float(input())
vetor=[]
for i in range(100):
    vetor.append(n)
    n=n/2
for i in range(100):
    print("N[%d] = %.4f"%(i, vetor[i]))