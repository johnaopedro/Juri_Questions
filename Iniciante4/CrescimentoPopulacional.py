N = int(input())
saidas = []

for _ in range(N):
    a, b, c, d = map(float, input().split())
    contA = 0    
    while a <= b:
        a += int(a * c / 100)
        b += int(b * d / 100)
        contA += 1
        
        if contA > 100:
            saidas.append("Mais de 1 seculo.")
            break
    if contA <= 100:
        saidas.append("%d anos."%contA)

for saida in saidas:
    print(saida)
