Numero=int(input())
Um=1
for i in range(Numero):
    NumSoma=int(input())
    for j in range(NumSoma-1):
        if Um>0:
            Um-=1
        else:
            Um+=1
    print(Um)
    Um=1