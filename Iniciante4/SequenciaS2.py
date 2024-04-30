fracao=[1,]
j=1
s=0
cont=1
for i in range(2,39):
    if i%2==0:
        fracao.append((i+1)/(2**(i-j)))
        cont+=1
        j+=1
for i in range(len(fracao)):
    s = s + fracao[i]
print("%.2f"%s)