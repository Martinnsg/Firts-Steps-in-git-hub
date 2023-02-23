#jogo de dados
from random import randint
from time import sleep
from operator import itemgetter
jogo = {'jogador1': randint(1,6),
        'jogador2': randint(1,6),
        'jogador3': randint(1,6),
        'jogador4': randint(1,6)}
ranking = dict()

print('Valores sorteados: ')
for k,v in jogo.items():
    sleep(1)
    print(f'{k}: {v}')

ranking = sorted(jogo.items(), key = itemgetter(1), reverse = True)
for k,v in enumerate(ranking):
    sleep(1)
    print(f'{k+1}º colocado: {v}')