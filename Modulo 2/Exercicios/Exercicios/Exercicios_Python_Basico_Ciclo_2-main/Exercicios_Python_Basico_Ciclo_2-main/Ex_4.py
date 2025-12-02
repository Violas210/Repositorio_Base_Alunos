# Calcule a média das notas utilizando um loop while e também um loop for


# ------------------------------------------ ESCREVA SEU CÓDIGO ABAIXO -----------------------------------------------------------

notas = ['9.5', '10', '6.75', '5.5']

cont = 0
soma = 0 

while cont <= 3:
    nota = float(notas[cont])
    cont += 1
    soma = soma + nota

media = soma / 4    
print(media)


# LOOP FOR

soma = 0
for nota in notas:
    soma = soma + float(nota)

media = soma / len(notas)
print(media)
