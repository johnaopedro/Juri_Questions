while True:
    n = int(input())
    cont=1
    if n==0:
        break
    for i in range(0,1):
        for k in range(0,n):
            if k==(n-1):
                print("%d"%cont) 
            else:
                print("%d"%cont, end=" ")
            cont+=1