import csv 

email = input('digite o email: ')
senha = input('digite a senha: ')


with open("usuarios.csv", "r", newline='', encoding="utf-8") as arquivo:
     
    leitor = csv.reader(arquivo)

    for linha in leitor:
        if linha[1] == email:
            if linha[2] == senha:
                print('Acesso permitido')
                break
            else:
                print('acesso negado')
                break
        else:
            continue
        print('email e senha nao cadastrado')

# if email == :
#     if senha == 'jjjj':
#         print('acesso permitido')
# else:
#     print('acesso negado')