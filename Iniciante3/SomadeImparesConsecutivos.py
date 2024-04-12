a=input()
a=int(a)
i=0
soma=0
while i<a:
    x,y = input().split()
    x=int(x)
    y=int(y)
    if x>y:
        menor=y
        maior=x
        menor=menor+1
        while menor<maior:
            if menor%2!=0:
                soma=soma+menor
                menor=menor+1
            menor=menor+1
    else:
        menor=x
        maior=y
        menor=menor+1
        while menor<maior:
            if menor%2!=0:
                soma=soma+menor
                menor=menor+1
            menor=menor+1
    print(soma)
    soma=0
    i=i+1