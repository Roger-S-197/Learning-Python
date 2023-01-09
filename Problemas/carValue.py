renda = int(input('Qual rua renda mensal? '))
carro = int(input('Qual valor do automovel? '))

def calculo():
    valores = carro / renda
    print(f'Para comprar o carro você precisa trabalhar sem gastar um centavo por {valores} meses')

calculo()