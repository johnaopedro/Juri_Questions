n = int(input())
valores=[]
for i in range(n):
    t = int(input())
    valor=abs(t-2015)
    if t>=2015:
        valor=valor+1
        val= str(valor)+ " A.C."
    else:
        val= str(valor)+ " D.C."
    valores.append(val)
for i in valores:
    print(i)