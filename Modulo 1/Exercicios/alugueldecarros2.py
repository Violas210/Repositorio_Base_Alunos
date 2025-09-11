modelo = input('Qual o modelo do carro?:  ')
dias = float(input('Por quntos dias o carro foi alugado: '))
km = float(input('Por quantos km o carro percorreu: '))

valor = 0

if modelo == 'Vectra':
    valor = 100

elif modelo == 'mercedes':
    valor = 800

elif modelo == 'Hilux':
    valor = 1000

else:
    valor = 60


total_dias = dias * valor
total_km = km * 0.15
pagar_total = total_dias + total_km
print(f'Voce alugou o carro {modelo} andou por {dias} dias e percorreu {km}km, então o preço à se pagar é de: R${pagar_total}')