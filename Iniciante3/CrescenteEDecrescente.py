while True:
    x, y = input().split(" ")
    x=int(x)
    y=int(y)
    if x==y:
        break 
    elif x<0 and y>0:
        print("Decrescente")      
    elif x>0 and y<0:
        print("Decrescente")   
    elif x>y:
        print("Decrescente")
    elif x==y:
        break          
    else:
        print("Crescente")  