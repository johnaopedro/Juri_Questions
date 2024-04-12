v1, v2, v3 = input().split()

v1 = int(v1)
v2 = int(v2)
v3 = int(v3)

maiorab = float((v1+v2+abs(v1-v2))/2)
maior = float(((maiorab + v3 +abs(maiorab-v3)))/2)

print("%d eh o maior"%maior)