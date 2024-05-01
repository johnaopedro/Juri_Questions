n=int(input())
x=[]
for i in range(10):
    x.append(n)
    n=n+n

for _ in range(10):
    print("N[%d] = %d"%(_,x[_]))