# Métodos para Strings

mensagem = 'Eu amo treinamento físico'

print(mensagem.lower()) #todo em minúsculo
print(mensagem.upper()) # todo em maiúsculo
print(mensagem.capitalize()) # a primeira em maiúsculo
print(mensagem.find('f')) # encontra a posição
print(mensagem.find('amo')) # posição
print(mensagem.replace('a', 'e')) # troca
print(mensagem.replace('físico', 'de alta performace')) #troca
print(mensagem.strip()) # Retira os espaços do inicio
print(mensagem.__len__())