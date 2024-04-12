a=float(input())
i=0
while(i<a):
    x,y,z = map(float,input().split())
    calculo=((x*2)+(y*3)+(z*5))/10
    print("%.1f"%calculo)
    calculo=0
    i=i+1