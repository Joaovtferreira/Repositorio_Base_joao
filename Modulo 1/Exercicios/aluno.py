from colorama import init,Fore 

init(autoreset=True)

nome = input('qual e seu nome?' )
n1 = float (input('qual a sua primeira nota?: '))
n2 = float (input('qual a sua segunda nota?: '))
n3 = float (input('qual a sua terceira nota?: '))
resultado = round((n1 + n2 + n3) /3, 1)
print('o aluno' ,nome, 'tirou', resultado)
if resultado >= 5:
    print(Fore.GREEN + 'aluno aprovado')
else:
    print(Fore.RED + 'aluno reprovado!')