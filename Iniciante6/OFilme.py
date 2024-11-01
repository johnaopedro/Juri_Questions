vi,vf= map(float, input().split())
porcentagem=0
diferenca=0
if vi==vf:
    print("0.00%")
else:
    diferenca = vf - vi
    porcentagem = (diferenca / vi) * 100
    print("%.2f%%" %porcentagem)