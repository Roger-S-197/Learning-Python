class Funcionarios:
    def __init__(self, nome, sobrenome, data_nascimento):
        self.nome = nome
        self.sobrenome = sobrenome
        self.data_nascimento = data_nascimento

usuario1 = Funcionarios('Helena', 'Harper', '12/01/1990')
usuario2 = Funcionarios('Ada', 'Wong', '15/10/1980')
usuario3 = Funcionarios('Leon', 'Kennedy', '11/03/1976')

print(usuario1.nome)
print(usuario2.nome)
print(usuario3.nome)