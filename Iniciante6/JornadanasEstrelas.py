n=int(input())
valores = list(map(int, input().split()))
carneiros=0
i=0
while True:
    if i>n:
        break
    if valores[i]>0:
        if valores[i]%2==0:
            valores[i]-=1
            carneiros+=1
            i-=1
        else:
            valores[i]-=1
            carneiros+=1
            i+=1
    else:
        break
soma=0
for i in range(n):
    soma+=valores[i]
print(carneiros, soma)