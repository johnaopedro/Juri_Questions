a, b = input().split()
a=int(a)
b=int(b)
soma=0
while True:
    if a<=0:
        break
    elif b<=0:
        break
    if a>b:
        maior=a
        menor=b
        for i in range(b, a+1):
            soma=soma+i
        print(" ".join(map(str, range(b, a+1))), "Sum=%d" % soma)
            
    else:
        maior=b
        menor=a
        for i in range(a, b+1):
            soma=soma+i
        print(" ".join(map(str, range(a, b+1))), "Sum=%d" % soma)
            
    soma=0
    a, b = input().split()
    a=int(a)
    b=int(b)
