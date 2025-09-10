nome = input('qual e o nome do produto?: ')
valortotal = int(input('qual o preço do produto?: '))
porcentagem = float(input('qual o desconto do produto?: '))
desconto = valortotal * (porcentagem / 100)
valornovo = valortotal - desconto
print(f'o {nome} com {porcentagem} % de desconto fica com o valor de:{valornovo}' )