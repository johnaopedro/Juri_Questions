N=int(input())
j=[]
for i in range(0,N):
    j.append(N-i)
soma=j[0]
for i in range(1,N):
    soma=soma*j[i]
print(soma)
