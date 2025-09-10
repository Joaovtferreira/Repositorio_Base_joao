# Utilize um loop while e um loop for para percorrer a lista e exibir os valores dos items contidos na lista

# ------------------------------------------ ESCREVA SEU CÓDIGO ABAIXO -----------------------------------------------------------

frutas = ['maçã', 'banana', 'morango', 'uva', 'laranja']

# LOOP WHILE

contador = 0
while contador < len(frutas):
    print(frutas[contador])
    contador = contador + 1 

print(contador)

# LOOP FOR

cont = 0
for fruta in frutas:
    print(f'{fruta}')
    cont = cont +1

#print(f'A lista tem {cont} frutas.')
    

