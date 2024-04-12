v1, v2, v3 = input().split()

v1 = int(v1)
v2 = int(v2)
v3 = float(v3)

v4, v5, v6 = input().split()

v4 = int(v4)
v5 = int(v5)
v6 = float(v6)

Valor = float((v3*v2)+(v6*v5))

print("VALOR A PAGAR: R$ %.2f" % Valor)