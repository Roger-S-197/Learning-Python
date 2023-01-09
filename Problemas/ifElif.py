altura = float(input('Qual é a sua altura em cm? '))
peso = float(input('Qual é o seu peso em kg? '))

imc = float(peso / (altura ** 2))

if imc < 18.5:
    print(f'Você está muito magro(a), seu imc é de {imc}')

elif imc < 24.9:
    print(f'Você está com um peso bom, seu imc é de {imc}')

elif imc < 29.9:
    print(f'Você está com sobrepeso, seu imc é de {imc}')

elif imc < 39.9:
    print(f'Você está obeso(a), seu imc é de {imc}')

else:
    print(f'Obesidade grave, seu imc é de {imc}')