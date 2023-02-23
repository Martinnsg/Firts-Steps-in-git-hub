# filme = {'titulo': 'Star Warts', 'ano': 1977, 'diretor':'Gerorge Lucas'}
# print(filme.values())
# print(filme.keys())
# print(filme.items())
# for k,v in filme.items():
#     print(f'O {k} é {v}' ,end=', ')

# pessoas = {'nome': 'Gustavo', 'sexo': 'M', 'idade': 22 }
# print(f'\nO {pessoas["nome"]} tem {pessoas["idade"]} anos.')
# print(pessoas.items ())

estado = dict()
brasil = list()
for c in range (0,3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do estado: '))
    brasil.append(estado.copy())


for k, v in brasil.items():
    print(f'O campo {k} tem valor {v}')