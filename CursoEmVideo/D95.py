import os
total = 0
jogador = dict()
partidas = []
lista = []
while True:
  
    jogador['nome'] = str(input('Nome do jogador: '))
    try:
        n = int(input(f'Quantas partidas jogadas pelo {jogador["nome"]}: '))
    except:
        print('ERRO!')
    try:
        for i in range (0,n):
            partidas.append(int(input(f'Quantos gols ele fez na partida {i+1}: ')))
    except:
        print('ERRO!')  
        
    jogador['gols'] = partidas[:]
    jogador['total'] = sum(partidas)
    lista.append(jogador.copy())
    jogador.clear()
    partidas.clear()
    while True:
        cond = str(input('Deseja continuar? [S/N]')).upper()
        if cond in 'SN':
            break
        print('ERRO! Digite S ou N')
    if cond == 'N':
        break
os.system('cls')
while True:
    print('-='*40)
    for i,v in enumerate(lista):
        print(f'{i:>3}',end = ' ')
        for k in v.values():
            print(f'{str(k):<15}', end = '')
        print()
    print()
    j = int(input('Deseja ver o rendimento de qual jogador: '))
    print('-='*40)
    print(f'   -LEVANTAMENTO DO JOGADOR {lista[j]["nome"]}')
    for c,d in enumerate(lista[j]['gols']):
        print(f'   No jogo {c+1} ele fez {d}')
    print('-='*40)    
    print()
