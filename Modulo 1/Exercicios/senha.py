a = 'code'
b = 'rant'
c = 'prog'


senha = input('digite a senha! ')
if senha in (a, b, c):
    print('senha correta!')
else:
    print('senha incorreta!')
    print('tente novamente')