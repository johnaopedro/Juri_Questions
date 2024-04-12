a = int(input())
ano=0
mes=0
dia=0
while(a>364):
    a=a-365
    ano = ano+1
while(a>29):
    a=a-30
    mes=mes+1
dia=a
print("%d ano(s)"%ano)
print("%d mes(es)"%mes)
print("%d dia(s)"%dia)