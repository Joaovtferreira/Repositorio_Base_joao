# TIPOS DE DADOS

# --------------------------STRING (str)----------------------------
# strings sao textos, eles devem sempre estar com aspas simples ' ' ou aspas duplas " "

texto1 = 'oi'
texto2 = "tudo bom?"
# use o comando type() para verificar o tipo de dado em uma variavel
print(type(texto1))

# -------------------------INTEIROS (int)----------------------------
# os inteiros sao numeros inteiros e podem ser utilizados para operacoes matematicas
numero1 = 10
numero2 = 30
print(type(numero1))
print(numero1+numero2)
print(numero1 * texto1) # e possivel multiplicar inteiros com string

# ------------------------DECÍMAIS (float)---------------------------
# para numeros nao inteiros, usamos a representacao de "ponto flutuante" ou seja "float"
numero3 = 3.5
numero4 = 5.7
print(type(numero3))

# ------------------------LÓGICO (bool)-----------------------------
# quando falamos de tipo logico de dados, imaginamos "verdadeiro" ou "falso" (true, false)
# em python classificamos esse tipo como tipo boleano, bool

v = True
f = False
print(type(v))