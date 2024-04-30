x, y = map(int, input().split())
x=int(x)
y=int(y)
m=y
j=1
y=int(y/x)
for i in range(1,y+1):
    for k in range(1,x+1):
        if k==x:
            print("%d"%j) 
        else:
            print("%d"%j,end=" ")
        j+=1
    if j>=m:
        j=j