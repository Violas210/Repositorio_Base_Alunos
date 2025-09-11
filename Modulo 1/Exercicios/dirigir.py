idade = int(input('Qual é a sua idade: '))
habilitacao = str(input('Você tem habilitação? (s/n?): '))
print(f'Você é maior idade? {idade >= 18 and habilitacao == 's'}') 