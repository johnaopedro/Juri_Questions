#Formador de triangulo alternativo q soma os dois menores lados.

A, B, C, D = map(int, input().split())
entrada=[]
for i in range(4):
    if A>B and A>C and A>D:
        entrada.append(A)
        A=0
    elif B>A and B>C and B>D:
        entrada.append(B)
        B=0
    elif C>A and C>B and C>D:
        entrada.append(C)
        C=0
    else:
        entrada.append(D)
        D=0
for i in range(2): #Metade porque vai trocando até a metade, nesse caso 10.
    entrada[i], entrada[3 - i] = entrada[3 - i], entrada[i] #Começa no 19-0
A=entrada[0]
B=entrada[1]
C=entrada[2]
D=entrada[3]
if A + B > C or B + C > D:
    print("S")
else:
    print("N")