# Crie uma lista com 3 dicionários, cada um representando uma pessoa (contendo nome, idade, cidade). Use um laço para imprimir o nome de cada pessoa.



# ------------------------------------------ ESCREVA SEU CÓDIGO ABAIXO -----------------------------------------------------------

pessoas = [

   {'nome' : 'Gabriel',
   'idade' : '15',
   'cidade' : 'Santana de parnaiba'
   },
   {'nome' : 'Larissa',
    'idade' : '15',
    'cidade' : 'Cajamar'
    },
    {'nome' : 'Eloha',
     'idade' : '15',
     'cidade' : 'Santana de parnaiba' }
]

for nome in pessoas:
    print(nome['nome'])