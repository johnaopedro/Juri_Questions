x=[]
for i in range(10):
    n=int(input())
    if n<1:
        n=1
    x.append(n)
for _ in range(10):
    print("X[%d] = %d"%(_,x[_]))