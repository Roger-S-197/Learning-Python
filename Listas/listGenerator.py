from sys import getsizeof
# Generation Expression

numeros = [x * 10 for x in range(500)]

# print(numeros)
print(type(numeros))
print(getsizeof(numeros))

num = (x * 10 for x in range(500))

# print(list(num))
print(type(num))
print(getsizeof(num))