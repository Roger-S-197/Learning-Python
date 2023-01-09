from datetime import datetime

class Funcionarios:
    def __init__(self, nome, sobrenome, ano_nascimento):
        self.nome = nome
        self.sobrenome = sobrenome
        self.ano_nascimento = ano_nascimento

    def nome_completo(self):
        return (self.nome + ' ' + self.sobrenome)

    def idade_funcionarios(self):
        ano_atual = datetime.now().year
        self.ano_nascimento = int(ano_atual - self.ano_nascimento)
        return self.ano_nascimento


usuario1 = Funcionarios('Helena', 'Harper', 1990)
usuario2 = Funcionarios('Ada', 'Wong', 1980)
usuario3 = Funcionarios('Leon', 'Kennedy', 1976)

print(Funcionarios.nome_completo(usuario1))
print(Funcionarios.nome_completo(usuario2))
print(Funcionarios.nome_completo(usuario3))
print(Funcionarios.idade_funcionarios(usuario1))