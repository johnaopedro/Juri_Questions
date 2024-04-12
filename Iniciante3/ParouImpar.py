n=int(input())
b="EVEN"
c="ODD"
d="POSITIVE"
e="NEGATIVE"
i=0
while(i<n):
    a=int(input())
    if a>0:
        if a%2==0:
            print(b+" "+d)
        else:
            print(c+" "+d)
    elif a<0:
        if a%2==0:
            print(b+" "+e)
        else:
            print(c+" "+e)
    else:
        print("NULL")
    i=i+1
