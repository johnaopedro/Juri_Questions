i=0
x=input()
x=int(x)
while i<x:
    a, b = input().split()
    a=float(a)
    b=float(b)
    if b==0:
        print("divisao impossivel")
    elif a==0:
        print(0.0)
    else:
        div=a/b
        print(div)
    i=i+1