print('||--------------------||\n CALCULADORA \n||--------------------||')

print('Opções\n 1 Soma \n 2 Subtração \n 3 Multiplicação \n 4 Divisão')

opcoes = int(input('Escolha uma das opções: '))

if opcoes == 1:
    num1 = int(input('Digite o Primeiro numero: '))
    num2 = int(input('Digite o Segundo numero: '))
    print(f'O resulto é: {num1 + num2}')

elif opcoes == 2:
    num1 = int(input('Digite o Primeiro numero: '))
    num2 = int(input('Digite o Segundo numero: '))
    print(f'O resultado é: {num1 - num2}')

elif opcoes == 3:
    num1 = int(input('Digite o Primeiro numero: '))
    num2 = int(input('Digite o Segundo numero: '))
    print(f'O resultado é: {num1 * num2}')

elif opcoes == 4:
    num1 = int(input('Digite o Primeiro numero: '))
    num2 = int(input('Digite o Segundo numero: '))
    print(f'O resultado é: {num1 / num2}')

else:
    print('Isso não é uma opção')
