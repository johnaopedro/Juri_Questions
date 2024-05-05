numero = int(input())
resposta=[]
for i in range(numero):
    ordem, ordem1 = input().split()
    if ordem=="tesoura" and ordem1=="papel":
        resposta.append("Bazinga!")
    elif ordem=="papel" and ordem1=="pedra":
        resposta.append("Bazinga!")
    elif ordem=="pedra" and ordem1=="lagarto":
        resposta.append("Bazinga!")
    elif ordem=="lagarto" and ordem1=="Spock":
        resposta.append("Bazinga!")
    elif ordem=="Spock" and ordem1=="tesoura":
        resposta.append("Bazinga!")
    elif ordem=="tesoura" and ordem1=="lagarto":
        resposta.append("Bazinga!")
    elif ordem=="lagarto" and ordem1=="papel":
        resposta.append("Bazinga!")
    elif ordem=="papel" and ordem1=="Spock":
        resposta.append("Bazinga!")
    elif ordem=="Spock" and ordem1=="pedra":
        resposta.append("Bazinga!")
    elif ordem=="pedra" and ordem1=="tesoura":
        resposta.append("Bazinga!")
    elif ordem==ordem1:
        resposta.append("De novo!")
    else:
        resposta.append("Raj trapaceou!")
for i,j in enumerate(resposta):
    print("Caso #%d: %s"%(i+1,j))