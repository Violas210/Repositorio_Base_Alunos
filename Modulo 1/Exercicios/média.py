print('|____________________|\n Sistema de prova \n|____________________|')


nome = input ("|Digite o nome do aluno: ")
nota1 = float(input("|Digite a nota da primeira prova do aluno: "))
nota2 = float(input("|Digite a nota da segunda prova do aluno: "))
nota3 = float(input("|Digite a nota da terceira prova do aluno: "))
nota4 = float(input("|Digite a nota da quarta prova do aluno: "))

Média = round((nota1 + nota2 + nota3 + nota4) /4, 2)
print('|____________________|')
print(f'|a média do {nome} é: {Média}. o aluno esta aprovado? {Média >=5}  ')                   
