# Forma 1

valores = []

for x in range(6):
    valores.append(x * 10)

print(valores)

# Forma dentro de uma List Comprehensoin
multi = [x * 10 for x in range(6)]
print(multi)