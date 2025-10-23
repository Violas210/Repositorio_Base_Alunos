# Utilize um loop while e um loop for para adicionar itens na lista.
# Peça para que o usuário digite quantos filmes deseja adicionar, e também os nomes dos filmes



# ------------------------------------------ ESCREVA SEU CÓDIGO ABAIXO -----------------------------------------------------------

filmes = [] # Não apague esta lista

# LOOP WHILE
cont = 1
q_filmes = int(input('Digite quantos filmes voce quer adicionar a lista: '))

while cont <= q_filmes:
    nome = input(f'Digite o nome do {cont}º filme: ')    
    cont = cont + 1
    filmes.append(nome)
print(filmes)






# LOOP FOR

cont = 2
qtd_filmes = int(input(f'DSigite quanto filmes voce deseja adicionar a sua lista: '))

for cont in range(qtd_filmes): 
    cont = cont + 1
    nome = input(f'Digite o nome do filme que deseja adicionar: ')
    filmes.append(nome)
print(filmes)


