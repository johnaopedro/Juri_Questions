a, b, c, d = input().split()
a=float(a)
b=float(b)
c=float(c)
d=float(d)

calculo = ((a*2)+(b*3)+(c*4)+(d*1))/10

if calculo>=7:
    print("Media: %.1f"%calculo)
    print("Aluno aprovado.")
elif calculo<5:
    print("Media: %.1f"%calculo)
    print("Aluno reprovado.")
elif calculo>=5 or calculo<7:
    print("Media: %.1f"%calculo)
    print("Aluno em exame.")
    e = float(input())
    calculo= ((calculo+e)/2)
    if calculo>=5:
        print("Nota do exame: %.1f"%e)
        print("Aluno aprovado.")
        print("Media final: %.1f"%calculo)
    else:
        print("Nota do exame: %.1f"%e)
        print("Aluno reprovado.")
        print("Media final: %.1f"%calculo)