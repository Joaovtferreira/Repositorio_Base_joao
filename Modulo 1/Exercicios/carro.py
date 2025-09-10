continuar = 's' 
while continuar == 's':


   nome = input('digite o nome do carro:')
   valor = float(input('digite o valor do carro:'))
   litro = float(input('digite o consumo de km por litro:'))
   print(f'{30 *'-'}')
   print(f'| carro: {nome}')
   print(f'| valor: {valor}')
   print(f'| consumo por litro: {litro}')
   print(f'{30 *'-'}')

   continuar = input('deseja continuar? (s/n)')

print('fim do programa')