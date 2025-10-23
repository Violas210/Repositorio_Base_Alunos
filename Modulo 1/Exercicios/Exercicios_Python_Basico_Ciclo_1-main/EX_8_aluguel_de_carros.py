# Aluguel de carros:
# Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado
# Calcule o preço a pagar, sabendo que o carro custa R$ 60 por dia e R$ 0.15 por km rodado

# OUTPUT ESPERADO:

# Por quantos dias o carro foi alugado: 10
# Quantos km o carro rodou: 500
# Você andou 500.0km por 10 dias, então o preço a pagar é R$675.00.

# ------------------------------------------ ESCREVA SEU CÓDIGO ABAIXO -----------------------------------------------------------

dias = float(input('Por quntos dias o carro foi alugado: '))
km = float(input('Por quantoas km o carro percorreu: '))
total_dias = dias * 60 
total_km = km * 0.15 
pagar_total = total_dias + total_km
print(f'Voce andou por {dias} dias e percorreu {km}km, então o preço à se pagar é de: R${pagar_total}')
