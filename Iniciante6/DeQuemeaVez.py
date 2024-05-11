Numero = int(input())
for i in range(Numero):
    j1, e1, j2, e2 = input().split(" ")
    n1, n2 = map(int, input().split())
    soma = n1 + n2
    if e1 == "PAR" and soma % 2 == 0:
        print(j1)
    elif e1 == "IMPAR" and soma % 2 != 0:
        print(j1)
    else:
        print(j2)
    soma = 0
