p, n = map(int, input().split())
valores = list(map(int, input().split()))
x = True
for i in range(n - 1):
    if abs(valores[i] - valores[i + 1]) > p:
        x = False
        break

if x:
    print("YOU WIN")
else:
    print("GAME OVER")