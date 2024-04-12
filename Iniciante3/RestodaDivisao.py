x=int(input())
y=int(input())
soma=0
if x<y:
    while(x<y):
        x=x+1
        if x%5==2:
            print(x)
        elif x%5==3:
            print(x)
elif y<x:
    while(y<x):
        y=y+1
        if y%5==2:
            print(y)
        elif y%5==3:
            print(y)