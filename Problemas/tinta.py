usuario = int(input('Qual é o rendimento da lata? '))
parede = int(input('Qual é a altura da parece? '))
largura = int(input('Qual é a largura da parece? '))
'''
area = parede * largura
resultado = area / 5
resultado = resultado - usuario
print('Você precisa de', resultado, 'latas de tinta.')
'''
def calculo_tinta():
    m2 = parede * largura
    total = m2 / usuario
    print(f'Você precisa de {total} latas de tinta')

calculo_tinta()