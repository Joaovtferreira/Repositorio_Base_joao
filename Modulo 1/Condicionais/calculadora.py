# |------------------------------|
# | Calculadora
# |------------------------------|
# | 1 - Soma
# | 2 - Subtração
# | 3 - Multiplicação
# | 4 - Divisão
# |------------------------------|
# | Escolha uma das opções: 2
# | Digite o primeiro número:100
# | Digite o segundo número:30
# | O resultado é: 70.0


# print('|------------------------------|  | Calculadora  |------------------------------|  | 1 - Soma | 2 - Subtração | 3 - Multiplicação | 4 - Divisão|------------------------------|')

continuar = 's' 
while continuar == 's':

    print(f'|{30 *'-'}|')
    print('| CALCULADORA')
    print(f'|{30 *'-'}|')
    print('| 1 - SOMA')
    print('| 2 - SUBTRACAO')
    print('| 3 - MULTIPLICACAO')
    print('| 4 - DIVISAO')
    print(f'|{30 *'-'}|')


    conta = input('| escolha uma das opcoes para o calculo:' )

    numero1 = float(input('| escolha um numero:' ))
    numero2 = float(input('| escolha outro numero:' ))

    if conta == '1':
        soma = numero1 + numero2
        print(f'| a soma é:{soma}')

    elif conta == '2':
        subtracao = numero1 - numero2
        print(f'| a subtracao é:{subtracao}')

    elif conta == '3':
        multiplicacao = numero1 * numero2
        print(f'| a multiplicacao é:{multiplicacao}')

    elif conta == '4':
        divisao = numero1 / numero2
        print(f'| a divisao é:{divisao}')

    else:
        print('| opcao de calculo nao definida, encerrar o programa.')

    continuar = input('deseja continuar? (s/n)')

print('fim do programa')