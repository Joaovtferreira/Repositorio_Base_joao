# Crie um programa que receba um número inteiro e dia qual é o dia da semana correspondente a este número
# Os dias são:
# 1 - domingo
# 2 - Segunda
# 3 - Terça
# 4 - Quarta
# 5 - Quinta
# 6 - Sexta
# 7 - Sábado

# OUTPUT ESPERADO

# Digite um número: 1
# Domingo

# Digite um número: 2
# Segunda

# Digite um número: 8
# Número errado

# ------------------------------------------ ESCREVA SEU CÓDIGO ABAIXO -----------------------------------------------------------
dia = int(input('digite um numero: '))
if dia == 1:
    print('domingo')
elif dia == 2:
    print('segunda')
elif dia == 3:
    print('terca')
elif dia == 4:
    print('quarta')
elif dia == 5:
    print('quinta')
elif dia == 6:
    print('sexta')
elif dia == 7:
    print('sabado')
else:
    print('numero errado.')