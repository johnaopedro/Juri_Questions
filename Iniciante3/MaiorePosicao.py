i=0
b=0
entrada=0
while(i<100):
    a=int(input())
    if a>b:
        b=a
        entrada=i
    else:
        a=a
    i=i+1
print(b)
if b>a:
    print(entrada+1)
else:
    print(i)
