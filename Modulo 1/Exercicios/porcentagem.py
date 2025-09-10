# • Cálculo de Porcentagem de um Número.
# • O programa deve calcular e exibir o valor que corresponde a essa
# porcentagem do total. Exemplo: se o usuário digitar 200 como
# valor total e 15 como porcentagem, o programa deverá calcular
# que 15% de 200 é 30.
# • Exemplo de fórmula:
# valor_parte = valor_total * (porcentagem / 100)


numerointeiro1 = int(input('digite o numero inteiro:'))
numerointeiro2 = int(input('digite outro numero inteiro:'))
numeropor100 = int(input('digite a porcentagem:'))
numerossomados = numerointeiro1 + numerointeiro2

porcentagem = numerossomados * (numeropor100 / 100)
print(porcentagem)