ordem, ordem1, ordem2 = map(int, input().split())
#subiu 1 para o 2, constante ou subiu 2 para o 3 ok
if ordem>ordem1 and ordem1<=ordem2:
    print(":)")
#subiu 1 para o 2, constante ou desceu 2 para o 3 ok
elif ordem<ordem1 and ordem1>=ordem2:
    print(":(")
#subiu 1,2 e 3, subiu mais do 1 para o 2
elif ordem<ordem1 and ordem1<ordem2 and (ordem1-ordem)>(ordem2-ordem1):
    print(":(")
#subiu 1,2 e 3, subiu mais do 2 para o 3
elif ordem<ordem1 and ordem1<ordem2 and (ordem1-ordem)<=(ordem2-ordem1):
    print(":)")
#desceu 1,2 e 3, desceu mais do 1 para o 2
elif ordem>ordem1 and ordem1>ordem2 and (ordem1-ordem2)<(ordem-ordem1):
    print(":)")
#desceu 1,2 e 3, desceu mais do 1 para o 2
elif ordem>ordem1 and ordem1>ordem2 and (ordem1-ordem2)>=(ordem-ordem1):
    print(":(")
elif ordem==ordem1 and ordem1<ordem2:
    print(":)")
elif ordem==ordem1 and ordem1>ordem2:
    print(":(")
else:
    print(":(")
