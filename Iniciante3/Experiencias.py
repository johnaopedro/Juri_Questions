n=int(input())
i=0
coelho=0
ratos=0
sapos=0
pcoelho=0
pratos=0
psapos=0
while(i<n):
    x,y= map(str,input().split(" "))
    x=int(x)
    if y=="C":
        coelho=coelho+x
    elif y=="R":
        ratos=ratos+x
    elif y=="S":
        sapos=sapos+x
    x=0
    y=""
    i=i+1
total = sapos+coelho+ratos
pcoelho= float((coelho*100)/total)
pratos= float((ratos*100)/total)
psapos= float((sapos*100)/total)

print("Total: %d cobaias"%total)
print("Total de coelhos: %d"%coelho)
print("Total de ratos: %d"%ratos)
print("Total de sapos: %d"%sapos)
print("Percentual de coelhos: %.2f %%"%pcoelho)
print("Percentual de ratos: %.2f %%"%pratos)
print("Percentual de sapos: %.2f %%"%psapos)
