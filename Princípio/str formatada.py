# String Formatada

nome = 'Roger'
sobrenome = 'Silvério'
profissao = 'Programador'

texto = 'O ' + nome + ' ' + sobrenome + ' é um excelente ' + '[' + profissao + ']'
print(texto)

texto2 = f'O {nome} {sobrenome} e um excelente [{profissao}]'
print(texto2)

# O Roger Silvério sempre teve jeito para ser um excelente programador
texto3 = f'O {nome} {sobrenome} sempre teve jeito para ser um excelente {profissao}'
print(texto3)