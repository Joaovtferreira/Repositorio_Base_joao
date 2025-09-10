# Utilize um loop while e um loop for para contar de 0 até o número que o usuário digitar:

# ------------------------------------------ ESCREVA SEU CÓDIGO ABAIXO -----------------------------------------------------------

# LOOP WHILE


contador = 0
fim = int(input('escolha o valor final da sua conta: '))
while contador <= fim:
    print(contador)

    contador = contador+1

print('------resultado completo------')


# LOOP FOR

for i in range(fim+1):
 
    print(i)

contador = 0 
fim = int(input('digite o final da conta: '))