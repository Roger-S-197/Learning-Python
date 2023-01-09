# Forma 1

itens = ['mesa', 'telefone', 'caneta', 'celular', 'carregador', 'monitor']
itens1 = []

for x in itens:
    if 'e' in x:
        itens1.append(x)

print(itens1)

# Forma 2 (Melhorada)

escritorio = ['mesa', 'telefone', 'caneta', 'celular', 'carregador', 'monitor']

contem = [x for x in escritorio if 'a' in x]