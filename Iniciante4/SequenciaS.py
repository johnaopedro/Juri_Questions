h=[]
s=0
for i in range(1,101):
    h.append(1/i)
for i in range(100):
    s = s + h[i]
print("%.2f"%s)
