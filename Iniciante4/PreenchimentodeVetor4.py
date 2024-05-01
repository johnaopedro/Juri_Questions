par=[]
impar=[]
for i in range(15):
    n=int(input())
    if n%2==0:
        par.append(n)
    else:
        impar.append(n)
    if len(par)==5:
        for k in range(5):
            print("par[%d] = %d"%(k, par[k]))
        par=[]
    if len(impar)==5:
        for k in range(5):
            print("impar[%d] = %d"%(k, impar[k]))
        impar=[]
for i in range(len(impar)):
    print("impar[%d] = %d"%(i, impar[i]))
for i in range(len(par)):
    print("par[%d] = %d"%(i, par[i]))