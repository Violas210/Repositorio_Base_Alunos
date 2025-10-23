# Escreva um programa que pede ao usuário o nome de um aluno e as notas de 3 provas que este aluno realizou.
# No fim o programa deve mostrar na tela a média das 3 provas
# Dica:
# Para calcular a média das provas você deve dividir a soma das notas das provas pela quantidade de provas realizadas
# media = soma / 3

# OUTPUT ESPERADO:

# | ______________________________ |
# | SISTEMA DE PROVAS
# | ______________________________ |
# | Nome do aluno: Fulano
# | Nota da primeira prova: 9.8
# | Nota da segunda prova: 7
# | Nota da terceira prova: 8.5
# | ______________________________ |
# | Aluno: Fulano 
# | Média: 8.43
# | Aluno aprovado
# | ______________________________ |

# ------------------------------------------ ESCREVA SEU CÓDIGO ABAIXO -----------------------------------------------------------

print('|-------------------- \n SISTEMA DE PROVAS \n--------------------|')
nome = input ("|Digite o nome do aluno: ")
nota1 = float(input("|Digite a nota da primeira prova do aluno: "))
nota2 = float(input("|Digite a nota da segunda prova do aluno: "))
nota3 = float(input("|Digite a nota da terceira prova do aluno: "))
nota4 = float(input("|Digite a nota da quarta prova do aluno: "))

Média = round((nota1 + nota2 + nota3 + nota4) /4, 2)
print('|____________________|')

if Média >= 5:
    print(f'O aluno(a) {nome} foi aprovado com uma média de: {Média}.')
else:
    print(f'O aluno(a) {nome} reprovou com uma média de: {Média}.')