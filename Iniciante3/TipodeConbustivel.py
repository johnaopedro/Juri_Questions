x=0
alcool=0
gasolina=0
diesel=0
while True:
    x=int(input())
    if x==1:
        alcool=alcool+1
    if x==2:
        gasolina=gasolina+1
    if x==3:
        diesel=diesel+1
    if x==4:
        break
print("MUITO OBRIGADO")
print("Alcool: %d"%alcool)
print("Gasolina: %d"%gasolina)
print("Diesel: %d"%diesel)