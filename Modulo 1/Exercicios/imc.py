altura = float(input('Qual é a sua altura: '))
peso = float(input('Qual o seu peso: '))

imc = peso / altura ** 2

print(f'O seu imc é de: {imc:.2f}')