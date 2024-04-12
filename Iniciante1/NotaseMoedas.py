a = float(input()) * 100 
centena = a // 10000
a %= 10000
cinquenta = a // 5000
a %= 5000
vinte = a // 2000
a %= 2000
dez = a // 1000
a %= 1000
cinco = a // 500
a %= 500
dois = a // 200
a %= 200
um = a // 100
a %= 100
cinq = a // 50
a %= 50
vnt = a // 25
a %= 25
dec = a // 10
a %= 10
cin = a // 5
a %= 5
uum = a

print("NOTAS:")
print("%d nota(s) de R$ 100.00" % centena)
print("%d nota(s) de R$ 50.00" % cinquenta)
print("%d nota(s) de R$ 20.00" % vinte)
print("%d nota(s) de R$ 10.00" % dez)
print("%d nota(s) de R$ 5.00" % cinco)
print("%d nota(s) de R$ 2.00" % dois)
print("MOEDAS:")
print("%d moeda(s) de R$ 1.00" % um)
print("%d moeda(s) de R$ 0.50" % cinq)
print("%d moeda(s) de R$ 0.25" % vnt)
print("%d moeda(s) de R$ 0.10" % dec)
print("%d moeda(s) de R$ 0.05" % cin)
print("%d moeda(s) de R$ 0.01" % uum)