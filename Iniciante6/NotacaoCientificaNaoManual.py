##NOTAÇÃO CIENTIFICA NAO MANUAL.
n=float(input())
n_str=str(n)
printando=format(n, ".4E")

if n_str[0]=="-":
    if n==-0:
        print("%s"%printando)
    else:
        print("%s"%printando)
else:
    print("+%s"%printando)