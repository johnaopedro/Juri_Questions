x=[]
for i in range(100):
    x.append(float(input()))
for _ in range(100):
    if x[_]<=10:
        print("A[%d] = %.1f"%(_,x[_]))