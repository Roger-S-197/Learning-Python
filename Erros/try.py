# Erros
    # Excelente para testes
    # Não realiza o 'stop' no programa
    # Mensagens customizadas quando encontra um erro

try:
    item = ['chaves', 'carteira', 'celular']
    print(item[2])
except IndexError:
    print('Index não existe')