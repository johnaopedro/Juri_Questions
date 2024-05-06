entrada = input()
#Num significativos, basicamente binario, ou seja, *** é 2²+2¹+2°=4+2+1=7
gritos=0 #contador de gritos
resultado=[]
soma=0
while True:
    if entrada=="--*":
        #2²*0+2¹*0+2°*1=0+0+1=1
        soma+=1
    elif entrada=="-*-":
        #2²*0+2¹*1+2°*0=0+2+0=2
        soma+=2
    elif entrada=="*--":
        #2²*1+2¹*0+2°*0=4+0+0=4
        soma+=4
    elif entrada=="**-":
        #2²*1+2¹*1+2°*0=4+2+0=6
        soma+=6
    elif entrada=="-**":
        #2²*0+2¹*1+2°*1=0+2+1=3
        soma+=3
    elif entrada=="*-*":
        #2²*1+2¹*0+2°*1=4+0+1=5
        soma+=5
    elif entrada=="***":
        #2²*1+2¹*1+2°*1=4+2+1=7
        soma+=7
    elif entrada=="---":
        soma+=0
    if entrada == "caw caw":
        gritos += 1
        resultado.append(soma)
        soma = 0
    if gritos==3:
        break  
    entrada = input()
for i in resultado:
    print(i)