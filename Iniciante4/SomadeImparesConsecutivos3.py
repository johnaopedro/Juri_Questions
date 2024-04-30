N=int(input())
resultado=[]
Ordem=0
cont=1
while Ordem<N:
    x,y = input().split()
    x=int(x)
    y=int(y)
    if x%2!=0:
        val=x+2
        soma=x
        while cont<y:
            soma=soma+val
            val= val+2
            cont+=1
    else:
        soma=x
        soma=soma+1
        val=soma+2
        while cont<y:
            soma=soma+val
            val= val+2
            cont+=1
    resultado.append(soma)
    x=0
    y=0
    cont=1
    soma=0
    Ordem+=1
for i in range(N):
    print(resultado[i])
