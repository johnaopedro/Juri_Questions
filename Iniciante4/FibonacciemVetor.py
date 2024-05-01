n=int(input())
vetor=[0,1]
fib=[]
for i in range(n):
    fib.append(int(input()))
    for k in range(2,fib[i]+1):
        vetor.append(vetor[-1]+vetor[-2])
for i in range(n):
    print("Fib(%d) = %d"%(fib[i],vetor[fib[i]]))