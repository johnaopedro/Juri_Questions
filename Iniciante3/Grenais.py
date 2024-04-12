x=0
y=0
empate=0
grenais=0
n=0
gremio=0
inter=0
while True:
    if x==0 and y==0:
        x,y=input().split()
        x=int(x)
        y=int(y)
    print("Novo grenal (1-sim 2-nao)")
    grenais=grenais+1
    n=input()
    n=int(n)
    if n==1:
        if x==y:
            empate=empate+1
        if x>y:
            inter=inter+1
        elif y>x:
            gremio=gremio+1
        x=0
        y=0
    elif n==2:
        if x==y:
            empate=empate+1
        if x>y:
            inter=inter+1
        elif y>x:
            gremio=gremio+1        
        print("%d grenais"%grenais)
        print("Inter:%d"%inter)
        print("Gremio:%d"%gremio)
        print("Empates:%d"%empate)
        if inter>gremio:
            print("Inter venceu mais")
        elif gremio>inter:
            print("Gremio venceu mais")
        else:
            print("Nao houve vencedor")
        break


