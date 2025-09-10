quantidade_bandas = int(input('liste a quantidade de bandas: '))
contador = 1
bandas = []
while contador <= quantidade_bandas:
    nome = input(f'qual o nome da banda {contador}: ')
    bandas.append(nome)
    
    contador = contador +1

print(bandas)