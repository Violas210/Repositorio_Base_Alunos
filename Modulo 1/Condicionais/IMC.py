print('Vamos monitorar seu IMC e analizar se esta tudo bem com sua saude\n \n|------- RESPONDA AS PERGUNTAS A SEGUIR -------|\n')

peso = float(input('Digite o seu peso: '))
altura = float(input('Digite a sua altura: '))

imc = peso / (altura ** 2)

print(f'\nO seu IMC é de {imc:.2f} Voce está... ')
print('\n|----------------------------------------------------------|')
print('| Faixa de IMC               | Clasificação                |')
print('|----------------------------------------------------------|')
if imc < 18.5:
    print('| <18.5                      | abaixo do peso              |')

elif imc >= 18.5 and imc < 24.9:
    print('| 18.5 - 24.9                | peso normal                |')    

elif imc >= 25.0 and imc < 29.9:
    print('| 25.0 - 29.9                | Sobrepeso                  |')    

elif imc >= 30.0 and imc < 34.9:
    print('| 30.0 - 34.9                | Obesidade Grau I           |')    

elif imc >= 35.0 and imc < 39.9:
    print('| 35.0 - 39.9                 | Obesidade Grau II         |')    

elif imc >= 40:
    print('| >= 40                      |Obesidade Grau III (mórbida)|')    

print('|----------------------------------------------------------|')