dias = float(input('Por quntos dias o carro foi alugado: '))
km = float(input('Por quantoas km o carro percorreu: '))
total_dias = dias * 60 
total_km = km * 0.15 
pagar_total = total_dias + total_km
print(f'Voce andou por {dias} dias e percorreu {km}km, então o preço à se pagar é de: R${pagar_total}')

