# Dada a lista numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Crie um dicionário com duas chaves: "pares" e "ímpares", onde cada chave terá uma lista com os números correspondentes.


# ------------------------------------------ ESCREVA SEU CÓDIGO ABAIXO -----------------------------------------------------------

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

numero = {

    'impares':[],
    'pares':[]
}

for n in numeros:
    if n % 2 == 0:
        numero['pares'].append(n)

    else:
        numero['impares'].append(n)

print(numero)