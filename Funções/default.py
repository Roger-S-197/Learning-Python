# Default = Aquele que você define o valor no parametro
def boas_vindas(nome, quantidade=7):
    print(f'Olá {nome}.')
    print(f'Temos {str(quantidade)} laptops em estoque')

boas_vindas('Marcos')


# Non-Default = Aquele que você não define o valor no parametro
def boas_vindas(nome, quantidade):
    print(f'Olá {nome}.')
    print(f'Temos {str(quantidade)} laptops em estoque')

boas_vindas('Marcos', 6)

