import os



tarefas = {
    'metas' : ['lavar a louca', 'limpar a casa', 'pegar a roupa do varal'],
    'datas' : ['01/07', '01/07', '01/07']
}

barra = ((f'|{30 *'-'}|'))

def mostrar_tarefas():
    print(barra)
    print('| TAREFAS DIARIAS:')
    for i in range(len(tarefas['metas'])):
        print(f"| {i+1}. tarefa: {tarefas['metas'][i]} - data: {tarefas['datas'][i]}")
    print(barra)


def adicionar_tarefas():
    print('| TAREFAS DIARIAS:')
    nome_tarefa = input(f'| nome da tarefa: ')
    data_tarefa = input(f'| data da tarefa (dia/mes): ')
    tarefas['metas'].append(nome_tarefa)
    tarefas['datas'].append(data_tarefa)
    print(barra)


def remover_tarefas():
    mostrar_tarefas()
    




def mostrar_menu():
    while True:
        print('| MENU DE TAREFAS')
        print(barra)
        print('| (1) Mostrar tarefas ')
        print('| (2) Adicionar tarefa ')
        print('| (3) Remover tarefa')
        print('| (4) Sair')
        print(barra)
        opcao = input('| escolha uma das opcoes: ')
        print(barra)

        if opcao == '1':
            mostrar_tarefas()
            input('| aperte enter pra continuar...')

        elif opcao == '2':
            adicionar_tarefas()
            input('| aperte enter pra continuar...')

        elif opcao == '3':
            # remover_tarefas()
            input('| aperte enter pra continuar...')
            
        elif opcao == '4':
            print('| saindo.....')
            break

        else:
            print('| opcao nao definida')
            input('| aperte enter pra continuar...')






mostrar_menu()
