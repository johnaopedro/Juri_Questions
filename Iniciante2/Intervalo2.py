a=int(input())
i=0
ine=0
out=0
while(i<a):
    b=int(input())
    i=i+1
    if b>=10 and b<=20:
        ine=ine+1
    else:
        out=out+1
print("%d in"%ine)
print("%d out"%out)