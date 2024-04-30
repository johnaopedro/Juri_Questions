N= int(input())
j=[0, 1]
for i in range(2, N):
    j.append(j[-1] + j[-2])
for i in range(N):
    if i==N-1:
        print(j[i])
    else:
        print(j[i], end=" ")