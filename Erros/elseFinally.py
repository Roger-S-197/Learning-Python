try:
    valor = int(input('Digite o valor do seu produto: '))
    print(type(valor))
    print(valor)
except ValueError:
    print('Favor digitar um valor numérico')
# else: 
#  resultado = valor * 2
#  print(resultado)

finally:
    print('codigo ok')

print('Mais codigo abaixo')