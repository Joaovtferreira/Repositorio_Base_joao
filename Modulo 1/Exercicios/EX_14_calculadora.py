# Escreva um código que mostre na tela um "MENU" de opções de operações matematicas (Adição, Subtração, Divisão e Multiplicação)
# O usuário deve escolher uma das opções e depois inserir dois números para serem calculados de acordo com a operação escolhida.
# No fim mostre o resultado da operação

# OUTPUT ESPERADO:

#----------------------------------------- Exemplo 1 (Soma)

# |------------------------------|
# | Calculadora
# |------------------------------|
# | 1 - Soma
# | 2 - Subtração
# | 3 - Multiplicação
# | 4 - Divisão 
# |------------------------------|
# | Escolha uma das opções: 1
# | Digite o primeiro número:10
# | Digite o segundo número:10
# | O resultado é: 20.0

# ----------------------------------------- Exemplo 2 (Multiplicação)

# |------------------------------|
# | Calculadora
# |------------------------------|
# | 1 - Soma
# | 2 - Subtração
# | 3 - Multiplicação
# | 4 - Divisão 
# |------------------------------|
# | Escolha uma das opções: 3
# | Digite o primeiro número:10
# | Digite o segundo número:10
# | O resultado é: 100.0

# ----------------------------------------- Exemplo 3 (Opção inválida)

# |------------------------------|
# | Calculadora
# |------------------------------|
# | 1 - Soma
# | 2 - Subtração
# | 3 - Multiplicação
# | 4 - Divisão 
# |------------------------------|
# | Escolha uma das opções: 6
# | Digite o primeiro número:1
# | Digite o segundo número:2
# | ERRO. Escolha uma opção válida.



# ------------------------------------------ ESCREVA SEU CÓDIGO ABAIXO ----------------------------------------------------------

print('| ------------------------------ |')
print('| calculadora')
print('| ------------------------------ |')
print('| 1 - soma')
print('| 2 - subtracao')
print('| 3 - multiplicacao')
print('| 4 - divisao')
print('| ------------------------------ |')
conta = int(input('| escolha uma das opcoes: '))



if conta == 1:
    numero1 = float(input('| digite o primeiro numero: '))
    numero2 = float(input('| digite o segundo numero: '))
    soma = numero1 + numero2
    print(f'| o resultado e: {soma}')
elif conta == 2:
    numero1 = float(input('| digite o primeiro numero: '))
    numero2 = float(input('| digite o segundo numero: '))
    subtracao = numero1 - numero2
    print(f'| o resultado e: {subtracao}')
elif conta == 3:
    numero1 = float(input('| digite o primeiro numero: '))
    numero2 = float(input('| digite o segundo numero: '))
    multiplicacao = numero1 * numero2
    print(f'| o resultado e: {multiplicacao}')
elif conta == 4:
    numero1 = float(input('| digite o primeiro numero: '))
    numero2 = float(input('| digite o segundo numero: '))
    divisao = numero1 / numero2
    print(f'| o resultado e: {divisao}')
else:
    print('| ERRO.escolha uma opcao valida.')