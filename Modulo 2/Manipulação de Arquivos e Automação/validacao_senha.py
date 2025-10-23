import json

with open('senha.json', 'r', encoding='utf-8') as f:
    dados = json.load(f)

email = input('Digite o seu email: ')
senha = input('Digite a sua senha: ')

if email == dados['Email'] and senha == dados['Senha']:
    print('Acesso Liberado Vacilão')
else:
    print('Sai daqui Vacilão')
