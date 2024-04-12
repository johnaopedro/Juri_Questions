a=int(input())
b=int(input())
soma=0

if a>b:
    while(a-1>b):
        b=b+1
        if b%2!=0:
            soma=soma+b      
elif b>a:
    while(b-1>a):
        a=a+1
        if a%2!=0:
            soma=soma+a
print(soma)