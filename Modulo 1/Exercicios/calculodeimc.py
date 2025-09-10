nome = input('Qual seu nome?')
altura = float(input(f'{nome},Qual sua altura?'))
peso = float(input('E qual seu peso?'))

imc = peso/ (altura**2)
if imc < 18.5:
    print(f'{imc:.2f} Abaixo do peso, Tudo ok')
elif imc <= 24.9:
    print(f'{imc:.2f} Peso normal, Tudo ok')
elif imc <= 29.9:
    print(f'{imc:.2f} Sobrepeso, Tudo ok')
elif imc <= 34.9:
    print(f'{imc:.2f} Obesidade grau 1, Cuidado com a saude')
elif imc <= 39.9: 
    print(f'{imc:.2f} Obesidade grau 2, Cuidado com a saude')
else:
    print(f'{imc:.2f} Obesidade grau 3, Cuidado com a saude')

#o valor calculado
#Uma mensagem de orientação baseada no resultado
#Itens críticos:
#O usuário informa o peso (kg) e a altura (m) .
#O programa calcula o IMC:
#IMC = peso / (altura ** 2)
#O IMC é desenhado junto com uma mensagem personalizada:
#IMC ≥ 30,0 →Cuidado com a Saúde
#IMC < 30,0 →Tudo ok
#📊 Itens Desejáveis:
#Você pode melhorar o programa utilizando a tabela abaixo para classificação mais detalhada:

#Faixa de IMC	Classificação
#< 18,5	Abaixo do peso
#18,5 – 24,9	Peso normal
#25,0 – 29,9	Sobrepeso
#30,0 – 34,9	Obesidade Grau I
#35,0 – 39,9	Obesidade Grau II
#≥ 40,0	Obesidade Grau III (mórbida)
#Critérios de Avaliação
#Itens críticos (obrigatórios)
#Nome do repositório correto
#Código funcionando corretamente
#Entrega dentro do prazo
#Itens desejáveis ​​(valem pontos extras)
#O programa exibe:
#Nome do usuário
#Valor do IMC
#Classificação detalhada com base na tabela acima
#Dica
#Entrada de dados cominput()
#Conversão de tipos ( float)
#Operadores aritméticos ( divisão /, potência **)
#Estrutura condicional com if, elif,else