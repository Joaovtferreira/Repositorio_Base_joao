# Calcule a média das notas utilizando um loop while e também um loop for


# ------------------------------------------ ESCREVA SEU CÓDIGO ABAIXO -----------------------------------------------------------

notas = ['9.5', '10', '6.75', '5.5']

# LOOP WHILE

soma = 0
contador = 0
quantidade = len(notas)
while contador < len(notas):
    nota = float(notas[contador])
    soma = soma + nota
    contador += 1

media = soma / quantidade
print(media)


# LOOP FOR
soma = 0 
for i in notas:
    nota = float(i)
    soma = soma + nota

media = soma / len(notas)

print(media)