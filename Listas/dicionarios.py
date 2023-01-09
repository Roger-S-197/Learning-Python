aluno = {'nome': 'Ana', 'Idade': 16, 'nota-final': 'A', 'aprovação': True}
#           Key     Value

# print(aluno['nome'])

# aluno['nome'] = 'Jose'
# print(aluno)

aluno.update({'nome': 'John', 'Idade': 50, 'nota-final': 'S', 'Status': 'Vivo'})
del aluno['nome']
print(aluno.get('nome', 'Spartan-117'))
print(aluno.get('endereço', 'UNSC'))
print(aluno)