dia1 = input().split("Dia ")
hh, mm, ss = input().split(" : ")
dia2 = input().split("Dia ")
hh1, mm1, ss1 = input().split(" : ")
dia1=int(dia1[1])
dia2=int(dia2[1])
hh=int(hh)
mm=int(mm)
ss=int(ss)
hh1=int(hh1)
mm1=int(mm1)
ss1=int(ss1)
horaT = 0
minT = 0
segT = 0

difdia = dia2 - dia1

horaT = hh1 - hh
minT = mm1 - mm
segT = ss1 - ss

if segT < 0:
    segT += 60
    minT -= 1

if minT < 0:
    minT += 60
    horaT -= 1

if horaT < 0:
    horaT += 24
    difdia -= 1

print("%d dia(s)" % difdia)
print("%d hora(s)" % horaT)
print("%d minuto(s)" % minT)
print("%d segundo(s)" % segT)