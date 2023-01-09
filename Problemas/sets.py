funcionarios = {'Ana', 'Marcos', 'Alice', 'Pedro', 'Sophia', 'Bruno', 'Melissa'}
turno_dia = {'Ana', 'Marcos', 'Alice', 'Melissa'}
turno_noite = {'Pedro', 'Sophia', 'Bruno'}
tem_carro = {'Marcos', 'Alice', 'Bruno', 'Melissa'}

Lista1 = set(turno_noite).intersection(tem_carro) # Em comum
Lista2 = set(turno_dia).intersection(tem_carro) # Em comum
Lista3 = set(funcionarios).difference(tem_carro) # Diferença entre

print(Lista1)
print(Lista2)
print(Lista3)