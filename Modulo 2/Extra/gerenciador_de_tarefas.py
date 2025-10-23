import os
tarefas = {

    "tarefas" : ["Arrumar o quarto", "Lavar a louça"],
    "data" : ["17/10", "17/10"]

}

def mostrar_tarefa():
    barra = f'|{30*'-'}|'
    print(barra)
    for i in range(len(tarefas['tarefas'])):
        print(f'| {i+1} - Tarefa : {tarefas['tarefas'][i]} | Data: {tarefas['data'][i]}')
    input('| Aperte enter para continuar...')

def adicionar_tarefas():
    barra = f'|{30*'-'}|'
    print(barra)
    tarefa = input('| Nome da tarefa: ')
    data = input('| Data: ')
    tarefas['tarefas'].append(tarefa)
    tarefas['data'].append(data)
    print('| Tarefa adicionada com sucesso')
    input('| Aperte enter para continuar...')


def remover_tarefas():
    barra = f'|{30*'-'}|'
    print(barra)
    for i in range(len(tarefas['tarefas'])):
        print(f'| {i+1} - Tarefa : {tarefas['tarefas'][i]} | Data: {tarefas['data'][i]}')
    id_tarefa = int(input('| Digite o número da tarefa que deseja remover: '))
    
    if id_tarefa > 0:
        tarefa = tarefas['tarefas'].pop(id_tarefa-1)
        tarefas['data'].pop(id_tarefa-1)
    
    else:
         print('| ID invalido')
    
    print(f'| Tarefa "{tarefa}" removida com sucesso.')
    input('| Aperte enter para continuar...')


def menu():
    while True: 
        try:                                                                                    
            os.system('cls')
            barra = f'|{30*'-'}|'
            print(barra)
            print('| 1 - Mostrar tarefas')
            print('| 2 - Adicionar tarefas')
            print('| 3 - Remover tarefas')
            print('| 4 - Sair')
            print(barra)
            opc = int(input('| Escolha o número da opção: '))
            if opc == 1:
                os.system('cls')
                mostrar_tarefa()
            elif opc == 2:
                    os.system('cls')
                    adicionar_tarefas()
            elif opc == 3:
                    os.system('cls')
                    remover_tarefas()
            elif opc == 4:
                    print('Saindo do programa......')
                    break
                    
            else:
                    os.system('cls')
                    print('Opção invalida!')
                    input('| Aperte enter para continuar...')
        except: 
             print('| Erro escolha uma opção valida!')
             input('| Aperte enter para continuar...')



menu()