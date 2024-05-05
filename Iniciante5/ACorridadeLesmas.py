import sys
try:
        vetordematriz = []
        maior=0
        for line in sys.stdin:
            ordem=int(line)
            entrada= input().split()
            for i in range(ordem):
                entrada[i]=int(entrada[i])
            for j in range(len(entrada)):
                if entrada[j]>maior:
                    maior=entrada[j]
            if maior>=20:
                print(3)
            elif maior>=10 and maior<20:
                print(2)
            else:
                print(1)
            maior=0            
except Exception as e:
    print("Ocorreu um erro:", e)