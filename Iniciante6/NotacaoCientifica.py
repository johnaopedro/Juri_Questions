##NOTAÇÃO CIENTIFICA MANUAL.
n=float(input())
n_str=str(n)
decimal=float(10)
cont=0
nfinal=float(0)
sinal=""
if n%10==0:
    cont=1
if (n*-1)%10==0:
    cont=1
if n>0:
    if n<1:
        while True:
            if nfinal<10 and nfinal>=1:
                break
            nfinal=n*decimal
            decimal=decimal*10
            cont+=1
            sinal="-"
    elif n>=10:
        while True:
            if nfinal<10 and nfinal>=1:
                break
            nfinal=n/decimal
            decimal=decimal*10
            cont+=1
            sinal="+"
    else:
        nfinal=n
        sinal="+"
elif n<0:
    if n>-1:
        while True:
            if nfinal>-10 and nfinal<=-1:
                break
            nfinal=n*decimal
            decimal=decimal*10
            cont+=1
            sinal="-"
    elif n<=-10:
        while True:
            if nfinal>-10 and nfinal<=-1:
                break
            nfinal=n/decimal
            decimal=decimal*10
            cont+=1
            sinal="+"
    else:
        nfinal=n
        sinal="+"
nfinal_str= "{:.4E}".format(nfinal)
posicao = ['E', 'e']
# Encontrando a posição do primeiro caractere a buscar na string
primeira_ocorrencia = len(nfinal_str)  # Inicializa com um valor grande
for char in posicao:
    pos = nfinal_str.find(char)
    if pos != -1 and pos < primeira_ocorrencia:
        primeira_ocorrencia = pos

# Se encontrarmos algum dos caracteres a buscar
if primeira_ocorrencia != len(nfinal_str):
    # Removemos a parte da string antes da primeira ocorrência
    nfinal_str = nfinal_str[:primeira_ocorrencia]
if cont==0:
    cont=str("00")
elif cont<10:
    cont=str("0%d"%cont)
else:
    cont=str(cont)
if n_str[0]=="-":
    if n==-0:
        print("-%sE%s%s"%(nfinal_str,sinal,cont))
    else:
        print("%sE%s%s"%(nfinal_str,sinal,cont))
else:
    print("+%sE%s%s"%(nfinal_str,sinal,cont))