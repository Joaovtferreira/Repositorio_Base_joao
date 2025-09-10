# Utilize um loop while e um loop for para adicionar itens na lista.
# Peça para que o usuário digite quantos filmes deseja adicionar, e também os nomes dos filmes



# ------------------------------------------ ESCREVA SEU CÓDIGO ABAIXO -----------------------------------------------------------

filmes = [] # Não apague esta lista

# LOOP WHILE

contador = 0 
fim = float(input('quantos filmes deseja adicionar: '))
while contador < fim:
    adicionar = input('digite o nome do filme: ')
    filmes.append(adicionar)
    contador = contador + 1
    
print(filmes)


# LOOP FOR


fim = int(input('quantos filmes deseja adicionar: '))
for filme in range(fim):
    adiçao = input('digite o nome do filme: ')
    filmes.append(adiçao)

print(filmes)