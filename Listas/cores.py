cores = ['amarelo', 'verde', 'azul', 'vermelho']

cor_cliente = input('Digite a cor desejada: ')
if cor_cliente.lower() in cores:
    print('Sim')
else:
    print('Não temos esta cor em estoque')



# .lower() resolve o problema de letras maiúsculas