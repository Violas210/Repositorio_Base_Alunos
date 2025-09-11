
print('SISTEMA DE PROVA')

qtd_prova = int(input('Digite quantas provas o aluno realizou: '))

print('Digite quanto o aluno tirou em cada prova')
cont = 1
soma = 0

while cont <= qtd_prova:
    nota = float(input(f'Digite a nota do aluno na prova {cont}: '))
    soma += nota
    cont += 1

media = soma / qtd_prova
print(f'O aluno obteve a média de: {media}')