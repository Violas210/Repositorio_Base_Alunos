preco = float(input('Digite o preço do produto: '))
porcentagem = float(input('Digite o valor de desconto: '))
desconto = preco * porcentagem/ 100
print(f'O valor original é: R${preco}')
print(f'O valor com desconto é: R${desconto}')