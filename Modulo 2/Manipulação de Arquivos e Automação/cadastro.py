import csv 

nome = input('nome: ')
email = input('email: ')
senha = input('senha: ')

with open("usuarios.csv", "a", newline='', encoding="utf-8") as arquivo:
    escritor = csv.writer(arquivo)
    escritor.writerow([nome, email, senha])
