x=int(input())
resultado=[]
cont=1
soma=0
N=0
while x!=0:
    if x%2==0:
        val=x+2
        soma=x
        while cont<5:
            soma=soma+val
            val= val+2
            cont+=1
    else:
        soma=x
        soma=soma+1
        val=soma+2
        while cont<5:
            soma=soma+val
            val= val+2
            cont+=1
    resultado.append(soma)
    N+=1
    cont=1
    soma=0
    x=0
    x=int(input())
for i in range(N):
    print(resultado[i])