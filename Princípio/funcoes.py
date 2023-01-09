def soma(*numeros):
    a = 0
    for num in numeros:
        a += num
    return a

x = soma(2, 3, 4, 7, 181)

print(x)