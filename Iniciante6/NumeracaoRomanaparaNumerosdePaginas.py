def roman(num):
    normais = [
        1000, 900, 500, 400,
        100, 90, 50, 40,
        10, 9, 5, 4,
        1
        ]
    romanos = [
        "M", "CM", "D", "CD",
        "C", "XC", "L", "XL",
        "X", "IX", "V", "IV",
        "I"
        ]
    roman_num = ''
    i = 0
    while  num > 0:
        for _ in range(num // normais[i]): #Armazena toda divisão e atualiza para a prox
            roman_num += romanos[i]
            num -= normais[i]
        i += 1
    return roman_num
#main
n=int(input())
print(roman(n))
