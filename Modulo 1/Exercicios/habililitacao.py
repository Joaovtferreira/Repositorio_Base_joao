nome = input('qual e o seu nome?')
idade = int(input('qual a sua idade?'))
if idade >=18:
      carteira = input('possui carteira de motorista? (1-sim/ 2-nao):')
      if carteira == '1':
         print('voce pode dirigir')
      else:
          print('voce nao pode dirigir')
else:
   print('voce e menor de idade')
