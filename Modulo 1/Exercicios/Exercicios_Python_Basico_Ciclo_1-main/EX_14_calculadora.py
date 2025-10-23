# Escreva um código que mostre na tela um "MENU" de opções de operações matematicas (Adição, Subtração, Divisão e Multiplicação)
# O usuário deve escolher uma das opções e depois inserir dois números para serem calculados de acordo com a operação escolhida.
# No fim mostre o resultado da operação

# OUTPUT ESPERADO:

#----------------------------------------- Exemplo 1 (Soma)

# |------------------------------|
# | Calculadora
# |------------------------------|
# | 1 - Soma
# | 2 - Subtração
# | 3 - Multiplicação
# | 4 - Divisão 
# |------------------------------|
# | Escolha uma das opções: 1
# | Digite o primeiro número:10
# | Digite o segundo número:10
# | O resultado é: 20.0

# ----------------------------------------- Exemplo 2 (Multiplicação)

# |------------------------------|
# | Calculadora
# |------------------------------|
# | 1 - Soma
# | 2 - Subtração
# | 3 - Multiplicação
# | 4 - Divisão 
# |------------------------------|
# | Escolha uma das opções: 3
# | Digite o primeiro número:10
# | Digite o segundo número:10
# | O resultado é: 100.0

# ----------------------------------------- Exemplo 3 (Opção inválida)

# |------------------------------|
# | Calculadora
# |------------------------------|
# | 1 - Soma
# | 2 - Subtração
# | 3 - Multiplicação
# | 4 - Divisão 
# |------------------------------|
# | Escolha uma das opções: 6
# | Digite o primeiro número:1
# | Digite o segundo número:2
# | ERRO. Escolha uma opção válida.



# ------------------------------------------ ESCREVA SEU CÓDIGO ABAIXO -----------------------------------------------------------

print('|--------------------|\n      CALCULADORA \n|--------------------|')

print(' |Opções\n |1 Soma \n |2 Subtração \n |3 Multiplicação \n |4 Divisão \n|--------------------|')

opcoes = int(input('Escolha uma das opções: '))

if opcoes == 1:
    num1 = int(input('| Digite o Primeiro numero: '))
    num2 = int(input('| Digite o Segundo numero: '))
    print(f'| O resulto é: {num1 + num2}')

elif opcoes == 2:
    num1 = int(input('| Digite o Primeiro numero: '))
    num2 = int(input('| Digite o Segundo numero: '))
    print(f'| O resultado é: {num1 - num2}')

elif opcoes == 3:
    num1 = int(input('| Digite o Primeiro numero: '))
    num2 = int(input('| Digite o Segundo numero: '))
    print(f'| O resultado é: {num1 * num2}')

elif opcoes == 4:
    num1 = int(input('| Digite o Primeiro numero: '))
    num2 = int(input('| Digite o Segundo numero: '))
    print(f' |O resultado é: {num1 / num2}')

else:
    print('| Isso não é uma opção')
