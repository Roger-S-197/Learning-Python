class Funcionarios:
    def __init__(self, nome, sobrenome, data_nascimento):
        self.nome = nome
        self.sobrenome = sobrenome
        self.data_nascimento = data_nascimento

    def nome_completo(self):
        return self.nome + ' ' + self.sobrenome

usuario1 = Funcionarios('Helena', 'Harper', '12/01/1990')
usuario2 = Funcionarios('Ada', 'Wong', '15/10/1980')
usuario3 = Funcionarios('Leon', 'Kennedy', '11/03/1976')

print(usuario1.nome, usuario1.sobrenome) # meu jeito
print(usuario2.nome_completo()) # jeito proposto
print(Funcionarios.nome_completo(usuario3)) # jeito legal
