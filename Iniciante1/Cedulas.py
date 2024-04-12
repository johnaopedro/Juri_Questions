a = int(input())
centena = 0
cinquenta = 0
vinte=0
dez=0
cinco=0
dois=0
um=0
valor=a
while(a>99):
    a = a-100
    centena = centena + 1
while (a>49):
    a = a-50
    cinquenta = cinquenta +1
while(a>19):
    a = a-20
    vinte = vinte+1
while(a>9):
    a = a -10
    dez=dez+1
while(a>4):
    a=a-5
    cinco=cinco+1
while(a>1):
    a=a-2
    dois=dois+1
while(a>0):
    a=a-1
    um=um+1

print("%d"%valor)
print("%d nota(s) de R$ 100,00"%centena)
print("%d nota(s) de R$ 50,00"%cinquenta)
print("%d nota(s) de R$ 20,00"%vinte)
print("%d nota(s) de R$ 10,00"%dez)
print("%d nota(s) de R$ 5,00"%cinco)
print("%d nota(s) de R$ 2,00"%dois)
print("%d nota(s) de R$ 1,00"%um)