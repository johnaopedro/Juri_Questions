a = int(input())
hora=0
minuto=0
segundo=0
while(a>3599):
    a=a-3600
    hora=hora+1
while(a>59):
    a=a-60
    minuto=minuto+1
segundo=a
print("%d:%d:%d" % (hora, minuto, segundo))