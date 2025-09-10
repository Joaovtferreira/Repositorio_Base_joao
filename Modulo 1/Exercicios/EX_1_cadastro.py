# Escreva um programa que pede ao usuário o nome, idade, e-mail e senha para um cadastro e depois exiba as informações na tela:

# OUTPUT ESPERADO:

# | ------------------------------ |
# | ---------- CADASTRO ---------- |
# | ------------------------------ |
# | Nome: Maria
# | Idade: 17
# | Email: maria@email.com
# | Senha: 123123

# | ------------------------------ |
# | ----- USUÁRIO CADASTRADO ----- |
# | Seja bem vindo(a) Maria!
# | Email: maria@email.com
# | ------------------------------ |

# ------------------------------------------ ESCREVA SEU CÓDIGO ABAIXO -----------------------------------------------------------

print('| ------------------------------ |')
print('| ---------- cadastro ---------- |')
print('| ------------------------------ |')
nome = input('| nome: ')
idade = input('| idade: ')
email = input('| email: ')
senha = int(input('| senha: '))
if senha == 123123:
    print('| ------------------------------ |')
    print('| ----- USUARIO CADASTRADO ----- |')
    print(f'| seja bem vindo(a) {nome}! ')
    print(f'| email: {email}')
    print('| ------------------------------ |')
else:
    print('senha incorreta')