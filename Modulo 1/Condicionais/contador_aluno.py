provas = int(input('quantas provas voce fez? '))

contador = 1
soma = 0
while contador <= provas:
    nota = float(input(f'digite a nota da prova {contador}: '))
    soma = soma + nota
    contador = contador +1


media = soma /provas
print(f'sua nota e {media:.2f}')
   