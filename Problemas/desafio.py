idade = int(input('Qual sua idade? '))

if idade < 15:
    print("Você é muito jovem")
elif idade in range (14, 18):
    print("Você é um(a) adolescente(a)")
elif idade in range (19, 23):
    print("Você é um(a) Jovem")
elif idade in range (24, 30):
    print("Você já sabe pagar contas muito bem")
elif idade in range (31, 41):
    print("Você é um(a) adulto(a)")
else:
    print("Agora bora ver no que vai dar")