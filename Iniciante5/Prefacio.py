import math

A,B = input().split()
A = int(A)
B = int(B)
if(B < 0): 
    division = math.ceil(A/B)
    B = B * (-1)
    resto = A % B
else:
    division = math.floor(A/B)
    resto = A % B
    
print('%d %d'%(division,resto))