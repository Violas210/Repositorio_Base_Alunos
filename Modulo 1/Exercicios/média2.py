from colorama import init,Fore 
init(autoreset=True)

print('|____________________|\n Sistema de prova \n|____________________|')

nome = input ("|Digite o nome do aluno: ")
nota1 = float(input("|Digite a nota da primeira prova do aluno: "))
nota2 = float(input("|Digite a nota da segunda prova do aluno: "))
nota3 = float(input("|Digite a nota da terceira prova do aluno: "))
nota4 = float(input("|Digite a nota da quarta prova do aluno: "))

Média = round((nota1 + nota2 + nota3 + nota4) /4, 2)
print('|____________________|')

if Média >= 5:
    print(Fore.GREEN+f'O aluno(a) {nome} foi aprovado com uma média de: {Média}.')
else:
    print(Fore.RED+f'O aluno(a) {nome} reprovou com uma média de: {Média}.')