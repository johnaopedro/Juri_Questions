i=1
j=7
h=j
while(i<10):
    print("I=%d J=%d"%(i,j))
    j=j-1
    if (h-3)==j:
        j=j+5
        h=j
        i=i+2
